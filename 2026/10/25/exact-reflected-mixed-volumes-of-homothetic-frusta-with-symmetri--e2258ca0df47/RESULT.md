# Exact reflected mixed volumes of homothetic frusta with symmetric bases

## Finding
Let \(d\ge3\), let \(B\subset\mathbb R^{d-1}\) be any full-dimensional centrally symmetric convex body centered at the origin, and let \(0\le a\le1\). Form the frustum
\[
 F_a(B)=\operatorname{conv}\bigl(B\times\{0\},\ aB\times\{1\}\bigr).
\]
For every \(\lambda\ge0\), its complete reflected Minkowski-volume polynomial is independent of the *shape* of \(B\):
\[
 \boxed{\frac{\operatorname{vol}_d(F_a(B)+\lambda(-F_a(B)))}{\operatorname{vol}_d(F_a(B))}
 =\frac{2(1+\lambda)^d-(a+\lambda)^d-(1+a\lambda)^d}{1-a^d}}
 \quad (0\le a<1),
\]
with continuous value \((1+\lambda)^d\) at \(a=1\).
Consequently, for every \(1\le k\le d-1\),
\[
 \boxed{\frac{V_d(F_a(B)[d-k],(-F_a(B))[k])}{\operatorname{vol}_d(F_a(B))}
 =R_{d,k}(a)=1+\frac{(1-a^k)(1-a^{d-k})}{1-a^d}}
 \quad (0\le a<1),
\]
with \(R_{d,k}(1)=1\). Thus \(R_{d,k}(0)=2\), and for each interior index \(k\), \(R_{d,k}(a)\) strictly decreases from \(2\) to \(1\) as \(a\) increases from \(0\) to \(1\). For each fixed \(0<a<1\), the coefficient profile is symmetric in \(k\), increases strictly toward the middle, and decreases strictly afterward (the two middle indices tie when \(d\) is odd).

In particular, the exact difference-body ratio is
\[
 \frac{\operatorname{vol}_d(F_a(B)-F_a(B))}{\operatorname{vol}_d(F_a(B))}
 =\frac{2^{d+1}-2(1+a)^d}{1-a^d},
\]
for \(a<1\), interpolating from \(2^{d+1}-2\) for a pyramid to \(2^d\) for a prism. None of these expressions depends on the base geometry beyond central symmetry and full dimension.

## Assumptions and scope
A convex body is a compact convex set with nonempty interior in its affine span. The dilation \(aB\) is centered at the symmetry center, which has been translated to the origin. For \(a=0\) the upper face reduces to one apex; for \(a=1\) the body is a prism. An arbitrary common horizontal shear of the upper face, and any invertible affine image, gives the same normalized formulas. No polyhedrality, smoothness, or strict convexity of \(B\) is assumed.

Mixed volumes use the symmetric Minkowski polynomial convention
\[
 \operatorname{vol}_d(K+\lambda L)=\sum_{k=0}^d\binom dk V_d(K[d-k],L[k])\lambda^k
 \quad(\lambda\ge0).
\]
The endpoints have \(V_d(K[d],L[0])=\operatorname{vol}_d(K)\) and \(V_d(K[0],(-K)[d])=\operatorname{vol}_d(K)\). The theorem claims the new exact formula for every interior coefficient; the planar trapezoid case is intentionally not claimed as a novelty contribution.

## Proof
**1. Exact sections of the reflected Minkowski sum.** Put \(b=1-a\). At height \(u\in[0,1]\), the horizontal section of \(F_a(B)\) is \((1-bu)B\). Since \(-B=B\), the section of \(\lambda(-F_a(B))\) at height \(-\lambda v\), with \(v\in[0,1]\), is \(\lambda(1-bv)B\). When \(\lambda>0\), the slice of their Minkowski sum at height \(z=u-\lambda v\) is the union of centered homothetic copies
\[
 \bigl(1+\lambda-b(u+\lambda v)\bigr)B
\]
over all admissible \(u,v\in[0,1]\) with that height. The scales are nested because every copy has the same centrally symmetric base \(B\).

For \(-\lambda\le z\le1\), minimizing \(u+\lambda v\) subject to \(u-\lambda v=z\) and the interval constraints gives exactly \(|z|\): choose \((u,v)=(z,0)\) for \(z\ge0\), or \((0,-z/\lambda)\) for \(z\le0\). Every other admissible pair yields a smaller centered copy. Thus the entire section at height \(z\) is **exactly**
\[
 \bigl(1+\lambda-b|z|\bigr)B,
 \qquad -\lambda\le z\le1.
\]
The same conclusion for \(\lambda=0\) holds by direct inspection or continuity.

**2. Integrating the sections.** For \(0\le a<1\), integrating the \((d-1)\)-dimensional horizontal volumes gives
\[
\begin{aligned}
\operatorname{vol}_d(F_a(B)+\lambda(-F_a(B)))
&=\operatorname{vol}_{d-1}(B)\int_{-\lambda}^{1}
       (1+\lambda-b|z|)^{d-1}\,dz\\
&=\frac{\operatorname{vol}_{d-1}(B)}{d(1-a)}
 \bigl[2(1+\lambda)^d-(a+\lambda)^d-(1+a\lambda)^d\bigr].
\end{aligned}
\]
Similarly, direct slicing of the original frustum gives
\[
 \operatorname{vol}_d(F_a(B))
 =\operatorname{vol}_{d-1}(B)\int_0^1(1-bu)^{d-1}\,du
 =\frac{\operatorname{vol}_{d-1}(B)(1-a^d)}{d(1-a)}.
\]
Dividing proves the asserted Minkowski polynomial. When \(a=1\), the body is a translate of the centrally symmetric prism \(B\times[-1/2,1/2]\), hence \(F_1(B)+\lambda(-F_1(B))\) is a translate of \((1+\lambda)F_1(B)\), proving its endpoint separately.

**3. Extracting mixed volumes.** For each \(1\le k\le d-1\), the coefficient of \(\lambda^k\) in the numerator of the normalized polynomial is
\[
 \binom dk\bigl(2-a^k-a^{d-k}\bigr).
\]
Comparison with the stated mixed-volume convention yields
\[
 R_{d,k}(a)=\frac{2-a^k-a^{d-k}}{1-a^d}
 =1+\frac{(1-a^k)(1-a^{d-k})}{1-a^d}.
\]
The two endpoint coefficients are \(1\), as is required by the volumes of \(F_a(B)\) and its reflection.

**4. Strict interpolation and coefficient ordering.** For \(0<a<1\), let \(u=a^k\) and \(v=a^{d-k}\). The function \(f(u,v)=(1-u)(1-v)/(1-uv)\) satisfies
\[
 \frac{\partial f}{\partial u}=-\frac{(1-v)^2}{(1-uv)^2}<0,
 \qquad \frac{\partial f}{\partial v}=-\frac{(1-u)^2}{(1-uv)^2}<0.
\]
Both \(u\) and \(v\) increase strictly with \(a\), so \(R_{d,k}(a)=1+f(u,v)\) is strictly decreasing. Its values at \(a=0\) and \(a=1\) follow from the formula and continuity. For fixed \(0<a<1\), direct subtraction gives
\[
 R_{d,k+1}(a)-R_{d,k}(a)
 =\frac{(1-a)(a^k-a^{d-k-1})}{1-a^d},
\]
whose sign is respectively positive, zero, or negative according as \(2k<d-1\), \(2k=d-1\), or \(2k>d-1\). Reflection symmetry in \(k\) is immediate. Finally put \(\lambda=1\) in the exact volume formula to obtain the difference-body ratio and its endpoints.

## Verification
The self-contained `verify.py` first computes exact rational planar Minkowski-sum polygon areas for 60 trapezoid or triangle instances, including horizontally sheared frusta. It then tests 950 mixed-coefficient ratios for dimensions \(2\) through \(20\) using rational arithmetic, including their symmetry, strict monotonicity, coefficient-index ordering, and endpoint values. Separately, its optional NumPy/SciPy step constructs convex hulls in dimensions \(3\), \(4\), and \(5\), directly comparing 27 reflected Minkowski-sum volumes for cross-polytope bases to the predicted expression. The observed output is `FRUSTUM_EXACT_OK planar_hulls=60 rational_profiles=950 independent_high_dim_hulls=27`. These are regression checks, not proof of the assertion for arbitrary dimension or base; the integral computation above is the proof.

## Relationship to prior work
Fryš, Kotrbatý, Mouamine, and Wang establish the global Godbersen mixed-volume inequalities, higher-order extensions and simplex equality characterizations in *Higher-order Godbersen inequality and a characterization of simplices via the face lattice* (first public arXiv version 5 October 2026). Their inequalities do not identify the exact reflected Minkowski polynomial or the shape-independent coefficient profile for nonsimplex symmetric-base frusta.

A published note titled *Universal Santaló and volume-product laws for homothetic frusta* (11 October 2026) treats this same geometric construction but computes its polar volume, Santaló center, and Mahler product; those are different functionals and do not imply the displayed reflected mixed-volume formula. A published note titled *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* (11 October 2026) treats simplex frusta with noncentrally symmetric bases in dimensions at least three. Its two-dimensional trapezoid specialization intersects the elementary boundary case, which is excluded here from the new contribution, but its higher-dimensional statement does not imply the present centrally symmetric-base formulas.

The new result is therefore an exact all-index, all-dimensional metric-independent mixed-volume calculation for arbitrary symmetric convex bases, with strict parameter and index ordering. General mixed-volume polarization by itself permits coefficient extraction once the Minkowski polynomial is known; the key missing geometric input supplied here is the exact nested-section identity. Title or database-search absence alone is not regarded as proof of historical novelty.

## Limitations
The top and bottom faces must be homothetic around a common center after an affine shear, and the base must be centrally symmetric. The formula is not asserted for skew nonhomothetic prismatoids or for arbitrary asymmetric bases. It is a formula and strict monotonicity result on this natural family, not a new universal Godbersen inequality, a new simplex equality classification, or an optimal global stability modulus. Equivalent elementary frustum integrals could occur in older or differently indexed mixed-volume literature; complete historical priority requires independent investigation.

## References
1. F. Fryš, J. Kotrbatý, M. A. Mouamine, and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (first submitted 5 October 2026), https://arxiv.org/abs/2610.06806.
2. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers–Shephard inequality*, arXiv:2607.20387 (first submitted 22 July 2026), https://arxiv.org/abs/2607.20387.
3. *Universal Santaló and volume-product laws for homothetic frusta*, publicly posted mathematical result (11 October 2026), identifiable through the public published-finding corpus 2026 research catalogue.
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, publicly posted mathematical result (11 October 2026), identifiable through the public published-finding corpus 2026 research catalogue.
5. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220–233.
