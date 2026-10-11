# Exact arithmetic nullities in two-view Fourier tomography of finite-field conics

## Finding

Let \(q\) be any odd prime power, \(F=\mathbb F_q\), and
\[
C_q=\{(x,y)\in F^2:x^2+y^2=1\},\qquad
n=|C_q|=q-\chi_q(-1),
\]
where \(\chi_q\) is the quadratic character on \(F\). Then \(4\mid n\).
For a projective direction \(u=[u_1:u_2]\in\mathbb P^1(F)\), the (unscaled) directional Fourier measurements of an arbitrary complex function \(f:C_q\to\mathbb C\) are
\[
\mathcal T_u f(t)=\sum_{z=(x,y)\in C_q}f(z)\psi(t(u_1x+u_2y)),\qquad t\in F,
\]
where \(\psi:F\to\mathbb C^\times\) is any nontrivial additive character. A change of representative for \(u\) permutes the frequency parameter \(t\).

For two **nonisotropic** projective directions \(u,v\), namely \(Q(u)=u_1^2+u_2^2\ne0\) and \(Q(v)\ne0\), use the étale quadratic \(F\)-algebra \(A=F[J]/(J^2+1)\), with conjugation \(\overline{a+bJ}=a-bJ\), to define
\[
U=\{z\in A:z\bar z=1\},\quad
a_u=\frac{u_1+Ju_2}{u_1-Ju_2}\in U,\quad
r_{u,v}=a_v a_u^{-1},\quad d=\operatorname{ord}_U(r_{u,v}),\quad h=\frac nd.
\]
The group \(U\) is cyclic of order \(n\), and these expressions are independent of the projective representatives. Write \(\sigma_u=\chi_q(Q(u))\). Then the complete complex nullity of the combined two-view Fourier sampling map is
\[
\boxed{\dim_{\mathbb C}\ker(\mathcal T_u,\mathcal T_v)=
\begin{cases}
(h-1)/2,&h\text{ odd},\\
(h-2)/2,&h\text{ even and }\sigma_u=1,\\
h/2,&h\text{ even and }\sigma_u=-1.
\end{cases}}
\]
In particular, **the two Fourier slices determine every complex-valued function on the conic** if and only if \(d=n\), or \(d=n/2\) and \(\sigma_u=1\). The full kernel is also explicit: functions in the kernel are constant on cosets of \(\langle r_{u,v}\rangle\) and are negated by \(z\mapsto a_u z^{-1}\); the indicators of paired cosets, with opposite signs, form a basis.

Among the \(n\) nonisotropic projective directions, the exact number of **unordered pairs of distinct directions** with injective two-view sampling is
\[
\boxed{\frac{n\varphi(n)}2+\frac{n\varphi(n/2)}4.}
\]
If \(q\equiv1\pmod4\), there are exactly two isotropic projective directions, and **either single isotropic Fourier slice is already injective** on \(\mathbb C^{C_q}\). Hence the minimum number of directions is one when \(q\equiv1\pmod4\), and two when \(q\equiv3\pmod4\). The total count of unordered injective *distinct-direction pairs*, allowing isotropic directions, is the preceding displayed count plus \(2n+1\) when \(q\equiv1\pmod4\), and is unchanged when \(q\equiv3\pmod4\).

## Assumptions and scope

The finite field has odd characteristic; complex coefficients are completely unrestricted, including signs and phases. Fourier samples include **all** \(q\) frequencies on each chosen one-dimensional line through the Fourier origin. The measurement operator is linear, not a phase-retrieval or intensity-only operator. The formulas are valid for all odd prime powers, including nonprime fields, and count actual projective directions rather than chosen vector representatives. In the zero-nullity criterion and two-view count, the two directions are distinct, although the nullity formula also holds when they coincide. There is no normalization ambiguity because multiplying all Fourier measurements by a common nonzero factor preserves kernels.

## Proof

**1. The finite-field norm-one conic.** Identify \((x,y)\) with \(z=x+Jy\in A\). Then \(C_q\) is exactly \(U=\{z:z\bar z=1\}\). If \(-1\) is nonsquare, \(A\cong\mathbb F_{q^2}\) and \(U\) is the kernel of the norm to \(F\), hence cyclic of order \(q+1\). If \(-1\) is square, \(A\cong F\times F\), conjugation interchanges the factors, and \(U\cong F^\times\), cyclic of order \(q-1\). This proves the cardinality and \(4\mid n\). The norm is \(Q(a+bJ)=a^2+b^2\).

**2. A Fourier slice is an entire family of fibre sums.** Fix a nontrivial additive character \(\psi\). For \(u\), set \(\ell_u(x,y)=u_1x+u_2y\) and \(S_u f(c)=\sum_{z\in C_q:\ell_u(z)=c}f(z)\). Then \(\mathcal T_u f(t)=\sum_{c\in F}S_u f(c)\psi(tc)\). The \(q\)-point additive Fourier matrix is invertible, including when \(q\) is not prime. Consequently \(\mathcal T_u f\equiv0\) if and only if every \(S_u f(c)=0\).

**3. Nonisotropic fibres are reflected pairs.** For \(Q(u)\ne0\), identify \(u\) with \(u_1+Ju_2\), which is invertible in \(A\). On \(U\), the map
\[
R_u(z)=a_u\bar z=a_u z^{-1},\qquad a_u=u/\bar u
\]
is an involution preserving \(\ell_u\). Indeed the real (\(F\)-valued) part of \(u\bar z\) is \(\ell_u(z)\), and \(u\overline{R_u(z)}=\bar u z\), which has the same real part. More explicitly, writing \(u^{\perp}=(-u_2,u_1)\), every point with \(\ell_u(z)=c\) has the unique form \(z=(c/Q(u))u+t u^{\perp}\), and its conic equation becomes \(t^2Q(u)+c^2/Q(u)=1\). In these coordinates \(R_u\) sends \(t\) to \(-t\), since it fixes the projection along \(u\) and negates the perpendicular component. Thus the nonempty fibres are precisely the \(R_u\)-orbits, either singleton fixed points or reflected pairs; no higher multiplicities are possible. All fibre sums vanish precisely when
\[
f(R_u z)=-f(z)\qquad (z\in U),
\]
where the equation at a fixed point correctly forces \(f(z)=0\) over \(\mathbb C\).

**4. The dihedral quotient gives all ghosts.** The product \(R_vR_u\) multiplies each \(z\in U\) by \(a_v a_u^{-1}=r_{u,v}\). A function anti-invariant under both involutions is invariant under multiplication by \(r_{u,v}\), hence descends to \(W=U/\langle r_{u,v}\rangle\), a cyclic group of order \(h=n/d\). On \(W\), the remaining antisymmetry is \(g(a_u w^{-1})=-g(w)\). Therefore every orbit of size two contributes one free complex parameter, and each fixed point contributes none. The number of fixed points is the number of solutions to \(w^2=a_u\) in \(W\): one if \(h\) is odd, two if \(h\) is even and \(a_u\) is square in \(W\), and zero otherwise.

When \(h\) is even, \(\langle r_{u,v}\rangle\subset U^2\); therefore \(a_u\) is square in \(W\) precisely when it is square in \(U\). This is equivalent to \(Q(u)\) being square in \(F^\times\): if \(Q(u)=s^2\), then \(u/s\in U\) and \((u/s)^2=u/\bar u=a_u\); conversely, if \(z\in U\) satisfies \(z^2=a_u\), then \(u/z\) is fixed by conjugation, lies in \(F^\times\), and \(Q(u)=(u/z)^2\). Moreover, for even \(h\) the rotation \(r_{u,v}\) lies in \(U^2\), so \(a_u\) and \(a_v\) have the same square class and \(\sigma_u=\sigma_v\); the formula is thus symmetric in its two directions. Substituting the fixed-point counts yields the three-case nullity formula, and the opposite-sign coset differences produce the claimed full kernel basis.

**5. Injectivity and totient count.** The nullity is zero only for \(h=1\), or for \(h=2\) when \(\sigma_u=1\). Every nonisotropic projective direction corresponds bijectively to \(a_u\in U\): surjectivity follows from \(|U|=n\) and injectivity from \(u/\bar u=v/\bar v\Rightarrow u/v\in F^\times\). Precisely \(n/2\) of those directions have \(\sigma_u=1\), because \(U\) is cyclic of even order. For fixed \(u\), there are \(\varphi(n)\) choices of \(v\) with \(r_{u,v}\) of order \(n\), and when \(u\) has square norm there are \(\varphi(n/2)\) further choices with \(r_{u,v}\) of order \(n/2\). Division by two for unordered pairs proves the formula. Since \(n\ge4\), these choices are all distinct-direction pairs.

**6. Isotropic directions.** The condition \(Q(u)=0\) has two projective solutions exactly when \(-1\) is square. In the split algebra these are the two projections onto a field factor. The coordinate of any \(z\in U\cong F^\times\) in either factor is injective, so each isotropic \(\ell_u\) labels the \(q-1=n\) conic points without collisions. Its Fourier slice is therefore injective. In the nonsplit case no isotropic directions exist, while any nonisotropic single direction has at least one reflected pair and is not injective. The total pair count follows by adding the \(2n+1\) pairs containing an isotropic direction when they exist.

## Verification

The standalone `verify.py` uses Python 3 standard library and constructs \(C_q\), all projective directions, and the exact 0–1 incidence matrices of their fibres. It directly computes combined matrix ranks by modular Gaussian elimination (over two auxiliary primes for selected cases), independently of the group-theoretic kernel proof. It verifies 1,914 unordered nonisotropic pairs for ten finite fields, including the nonsplit and split quadratic extension fields \(\mathbb F_9,\mathbb F_{25},\mathbb F_{49}\), tests every predicted nullity and the injective-pair totient count, and tests single isotropic views when present. Invoke `python3 verify.py`; its final output begins `VERIFY_OK`. These finite comparisons are checks, not a proof for arbitrary \(q\).

## Relationship to prior work

The discrete Fourier slice theorem, finite-field line-sum transforms, and image reconstruction from X-rays are established; their principles are used here rather than claimed as new. In particular, Koh (2012) establishes uniform endpoint norm inequalities for finite-field X-ray and Radon transforms with all lines; the present result instead evaluates the **exact kernel of two fixed directional Fourier slices on one norm-one conic**. Chandra and Svalbe (2014) derive exact number-theoretic Radon reconstruction for full discrete images using an appropriate collection of directions, not this two-direction conic-restricted kernel. Iosevich, Mayeli and Pakianathan (2015) analyze orthogonal exponential bases and tilings in prime-field planes; those are distinct from arbitrary complex-weighted conic reconstruction with two frequency-line subsets. Classical discrete tomography explores switching components and reconstruction from prescribed lattice X-rays, but does not supply the finite-field conic-specific arithmetic count here. No assertion of independent historical priority is made.

## Limitations

The restriction to \(x^2+y^2=1\) and the use of all frequencies along each selected line are essential to the statement; the formula is not a universal multi-angle tomography result. It gives **injectivity and exact kernels**, not singular values, noise stability, positivity-constrained uniqueness, or an algorithmic robustness guarantee. Older finite-field tomography or norm-one torus literature might contain an equivalent form. Only same-model mathematical review and finite independent-code computations have been performed; independent external audit has not been performed.

## References

- D. Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, arXiv:1209.1215v1 (first public version September 6, 2012). https://arxiv.org/abs/1209.1215
- S. Chandra and I. Svalbe, *Exact image representation via a number-theoretic Radon transform*, IET Computer Vision **8** (2014), 338–346, first published August 1, 2014. https://doi.org/10.1049/iet-cvi.2013.0101
- A. Iosevich, A. Mayeli and J. Pakianathan, *The Fuglede Conjecture holds in \(\mathbb Z_p\times\mathbb Z_p\)*, arXiv:1505.00883v1 (first public version May 5, 2015). https://arxiv.org/abs/1505.00883
- R. J. Gardner and P. Gritzmann, *Discrete tomography: determination of finite sets by X-rays*, Transactions of the American Mathematical Society **349** (1997), 2271–2295. https://doi.org/10.1090/S0002-9947-97-01741-8
