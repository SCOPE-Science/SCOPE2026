# Exact exponent-four Green-energy minimum for three points on the Riemann sphere

## Finding
For the Fubini–Study Riemann sphere \(\mathbb P^1\) and any ordered triple \(W=(w_1,w_2,w_3)\), the fourth-exponent normalized Green energy has the exact sharp minimum
\[
\Theta_{3,4}(\mathbb P^1):=\min_W B_4(W;\mathbb P^1)=\frac{11e^6}{2240}.
\]
Its minimizers are exactly the triples whose Hopf sphere representatives form an equilateral triangle on a great circle. They constitute one orbit under rotations and permutations.

There is also a global quantitative stability inequality. If \(v_j\in S^2\subset\mathbb R^3\) are the associated unit vectors and \(S=v_1+v_2+v_3\), then
\[
B_4(W;\mathbb P^1)-\frac{11e^6}{2240}
\geq\frac{e^6}{6720}\bigl(7\|S\|^2+10\|S\|^4\bigr).
\]
The displayed lower-bound coefficients are explicit but are not asserted individually optimal.

## Assumptions and scope
The measure \(\mu_{\rm FS}\) is the rotation-invariant probability measure on \(\mathbb P^1\), identified through the Hopf map with normalized surface area \(d\sigma/(4\pi)\) on the unit sphere \(S^2\). Chordal distance is normalized by
\[
d_{\rm ch}(z,w)^2=\frac{1-\xi\cdot v}{2},
\]
where \(\xi,v\in S^2\) represent \(z,w\). The mean-zero Green kernel is
\[
U(z,w)=\frac12+\log d_{\rm ch}(z,w),
\]
with the logarithmic singularity interpreted in the integrable sense. For any ordered triple, including repeated points, put
\[
B_4(W;\mathbb P^1)=\int_{\mathbb P^1}\exp\!\left(4\sum_{j=1}^{3} U(z,w_j)\right)d\mu_{\rm FS}(z).
\]
All assertions concern cardinality three and exponent four, not arbitrary exponents or point counts.

## Proof
**1. Exact invariant polynomial.** Put \(u=v_1\cdot v_2\), \(v=v_1\cdot v_3\), and \(w=v_2\cdot v_3\). The normalized Green-kernel formula gives
\[
B_4(W;\mathbb P^1)=\frac{e^6}{64}\,T(u,v,w),\quad
T=\int_{S^2}\prod_{j=1}^{3}(1-\xi\cdot v_j)^2\frac{d\sigma(\xi)}{4\pi}.
\]
For arbitrary real vectors \(a_1,\dots,a_{2k}\in\mathbb R^3\), rotational invariance and Gaussian moment pairing yield the exact spherical identity
\[
\int_{S^2}\prod_{j=1}^{2k}(\xi\cdot a_j)\frac{d\sigma(\xi)}{4\pi}
=\frac{1}{3\cdot5\cdots(2k+1)}\sum_{\mathcal P}\prod_{\{i,j\}\in\mathcal P}(a_i\cdot a_j),
\]
where the sum is over all pair partitions and the empty product is one. The odd-degree moments vanish. Expanding the six linear factors and using the formulas for degrees two, four and six gives
\[
\boxed{105T=232+168(u+v+w)+16(u^2+v^2+w^2)
+56(uv+uw+vw)+8uvw.}\tag{1}
\]
The coefficients of (1) can be regenerated exactly using the included standalone rational-arithmetic checker.

**2. A globally nonnegative deficit.** Define \(a=u+\tfrac12\), \(b=v+\tfrac12\), \(c=w+\tfrac12\), and
\[
t=a+b+c,\qquad Q=a^2+b^2+c^2.
\]
Since the \(v_j\) are unit vectors,
\[
t=\frac12\|S\|^2\ge0,\qquad S=v_1+v_2+v_3.
\]
Substituting into (1) yields the exact algebraic identity
\[
105T-33=98t+26t^2-10Q+8abc.\tag{2}
\]
Each of \(a,b,c\) lies in \([-\tfrac12,\tfrac32]\), so the arithmetic–geometric mean inequality gives
\[
|abc|\le\frac{\max(|a|,|b|,|c|)}3Q\le\frac12Q.
\]
Consequently \(8abc\ge-4Q\).

Furthermore, directly from the definitions,
\[
a=t-S\cdot v_3,\quad b=t-S\cdot v_2,\quad c=t-S\cdot v_1.
\]
Because \(\sum_j S\cdot v_j=\|S\|^2=2t\), we have
\[
Q=\sum_{j=1}^{3}(t-S\cdot v_j)^2
=\sum_{j=1}^{3}(S\cdot v_j)^2-t^2
\le3\|S\|^2-t^2=6t-t^2.\tag{3}
\]
Combining (2) and (3) proves the fully global estimate
\[
105T-33\ge98t+26t^2-14Q\ge14t+40t^2\ge0.\tag{4}
\]
Therefore \(T\ge33/105=11/35\). After multiplication by \(e^6/64\), the claimed sharp minimum and stability bound follow, because \(14t+40t^2=7\|S\|^2+10\|S\|^4\).

**3. Attainment and uniqueness.** Equality in (4) requires \(t=0\), equivalently \(v_1+v_2+v_3=0\). Pairing this relation with each unit vector shows that all distinct pairwise dot products equal \(-1/2\). Thus the vectors are exactly a regular triangle in a plane through the origin. Such triples exist, yield \(T=11/35\), and are congruent under \(\mathrm{SO}(3)\), which is the rotation action of \(\mathrm{PSU}(2)\) on \(\mathbb P^1\). This proves sharpness and all equality cases.

## Verification
The complete symbolic moment expansion (1), the shifted polynomial identity (2), and the numerical normalization-free equality \(T=11/35\) for an equilateral triple were independently checked by exact rational arithmetic in the included `check_energy.py` (Python standard library only). Its expected output is `CHECK_OK`.

A separate direct computation at an equilateral configuration uses three equatorial spinor roots and reduces the integral to the beta moments
\[
\int_{0}^{1}\bigl(s^6+(1-s)^6+4s^3(1-s)^3\bigr)\,ds=\frac{11}{35}.
\]
This confirms the normalization without relying on (1). The global nonnegativity and uniqueness in (4) are proven analytically for all triples; they are not inferences from finite experiments.

## Relationship to prior work
Hedenmalm and Xie (2026), arXiv:2610.15004v1, define this mean-zero Green energy and its Fubini–Study normalization. Their Theorem 6.16 already determines the exact minimum at exponent two for three points, and their Theorem 6.20 identifies a Bombieri–Weyl norm formulation at exponent two for arbitrary cardinality. Their Problem 6.23 expressly leaves the minimizers and constants for the three-point case at exponents different from two unresolved, while Problem 6.19 discusses higher even exponents through powers of binary forms. The present result solves the next even exponent, four, in the three-point case by an independent spherical-moment computation, and supplies a global barycentric deficit. It does not claim the previously known exponent-two minimizer result as new.

The Bombieri norm background also appears in classical inequalities for products of homogeneous polynomials; the general asymptotic estimates of Aldaz and Render (arXiv:2402.19153) concern different norm bounds and do not directly provide the present finite three-node optimum. A complete historical priority guarantee is not asserted.

## Limitations
The theorem does not solve other exponents, four or more nodes, different compact surfaces, or the optimal coefficient of the displayed global stability estimate. The originality comparison is based on publicly accessible sources and indexed comparisons; unindexed or inaccessible earlier formulations could overlap. No independent scientific audit has been performed.

## References
H. Hedenmalm and S.-Y. Xie, *Exponential Green energies, quantization, and minimizers on compact Riemann surfaces*, arXiv:2610.15004v1 (first posted 2026-10-10), especially Sections 6.2–6.5, Theorem 6.16, Theorem 6.20, and Problem 6.23. https://arxiv.org/html/2610.15004v1

J. M. Aldaz and H. Render, *Asymptotic bounds for Bombieri's inequality on products of homogeneous polynomials*, arXiv:2402.19153 (2024), a related but nonidentical product-norm setting. https://arxiv.org/abs/2402.19153
