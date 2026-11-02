# Universal half-step phase ordering for two regular weighted Bergman kernel orbits

## Finding

For **every** pair of integers \(p,d\ge 2\), every \(0<r,s<1\), and every relative rotation \(\theta\), consider the \(2d\) normalized reproducing kernels of the weighted Bergman space with kernel
\[
K_p(z,w)=(1-z\overline w)^{-p},
\]
at the two regular \(d\)-gons \(r\exp(2\pi i j/d)\) and \(s\exp(i\theta+2\pi i j/d)\), \(0\le j<d\). Write \(D_{p,d}(\theta)\) for the determinant of their Gram matrix.

**Global strict phase ordering:** for any two angles,
\[
D_{p,d}(\theta_1)>D_{p,d}(\theta_2)
\quad\Longleftrightarrow\quad
\cos(d\theta_1)<\cos(d\theta_2).
\]
Consequently, the *unique* determinant-maximizing phase modulo \(2\pi/d\) is
\[
\boxed{\theta\equiv\pi/d\pmod{2\pi/d}.}
\]
This result includes unequal radii, all integer powers \(p\ge2\), and the collision configuration \(r=s\) (for which the unrotated union has duplicates).

A closed product gives the exact optimum. Define, for \(0\le k<d\),
\[
F_{p,d,k}(w)=\sum_{j\ge0}\binom{p+k+dj-1}{p-1}w^j
=\frac{P_{p,d,k}(w)}{(1-w)^p},\qquad t=(rs)^d.
\]
Then \(P_{p,d,k}\) is an explicitly computable polynomial and
\[
\boxed{\begin{aligned}
D_{p,d}^{\mathrm{max}}={}&d^{2d}(rs)^{d(d-1)}(1-r^2)^{pd}(1-s^2)^{pd}\\[-2pt]
&\times \prod_{k=0}^{d-1}\left[
\frac{P_{p,d,k}(r^{2d})P_{p,d,k}(s^{2d})}
{(1-r^{2d})^p(1-s^{2d})^p}
-\frac{P_{p,d,k}(-t)^2}{(1+t)^{2p}}
\right].
\end{aligned}}
\]
All bracket factors are strictly positive. The strict phase ordering is stronger than merely determining an optimum: it compares any two rotations without changing radii.

## Assumptions and scope

The kernel is the standard normalized power-weight Bergman kernel (for the area weight proportional to \((1-|z|^2)^{p-2}\)), with positive integer exponent \(p\ge2\). Both circular orbits have the *same* cardinality \(d\ge2\) and are individually regular. The radii are strictly interior and nonzero. Each Gram vector is normalized to unit norm, so diagonal entries equal one. The determinant is invariant under a common rotation and periodic in \(\theta\) with period \(2\pi/d\). No claim is made for unequal orbit cardinalities or noninteger powers.

## Proof

**Step 1: Fourier-block Gram factorization.** Expand
\[
(1-z\bar w)^{-p}=\sum_{n\ge0}\binom{p+n-1}{p-1}z^n\bar w^n.
\]
Apply the unitary \(d\)-point discrete Fourier transform separately to the kernels from each orbit. The resulting \(2d\)-dimensional Gram matrix splits into \(d\) Hermitian blocks
\[
\begin{pmatrix}A_k&C_k(\theta)\\ \overline{C_k(\theta)}&B_k\end{pmatrix},
\]
where
\[
\begin{aligned}
A_k&=d\,r^{2k}F_{p,d,k}(r^{2d}),\\
B_k&=d\,s^{2k}F_{p,d,k}(s^{2d}),\\
C_k(\theta)&=d\,(rs)^k e^{-ik\theta}
F_{p,d,k}((rs)^d e^{-id\theta}).
\end{aligned}
\]
(The phase in \(C_k\) can be conjugated by changing the Fourier convention; its absolute value is invariant.) Therefore the *unit-normalized* kernel Gram determinant equals
\[
D_{p,d}(\theta)=(1-r^2)^{pd}(1-s^2)^{pd}
\prod_{k=0}^{d-1}\bigl(A_kB_k-|C_k(\theta)|^2\bigr).
\tag{1}
\]

**Step 2: negative-real zeros of the residue numerators.** For every integer \(p\ge1\), set \(P_{1,d,k}(w)=1\). The generating-function identity \(F_{p+1,d,k}=(p+k)F_{p,d,k}/p+(d/p)wF'_{p,d,k}\) yields the *exact recurrence*
\[
P_{p+1,d,k}(w)=\frac{
\bigl(p+k+[p(d-1)-k]w\bigr)P_{p,d,k}(w)
+d w(1-w)P'_{p,d,k}(w)}{p}.
\tag{2}
\]
Induction from (2) gives
\[
\deg P_{p,d,k}=\left\lfloor\frac{p(d-1)-k}{d}\right\rfloor
\quad\text{and every coefficient of }P_{p,d,k}\text{ is strictly positive}.
\]
Indeed, writing \(P_{p,d,k}(w)=\sum_{j=0}^{m}c_jw^j\), with \(c_j=0\) outside this range, the coefficient of \(w^j\) on the right of (2) is
\[
\frac{(p+k+dj)c_j+(p(d-1)-k-d(j-1))c_{j-1}}{p}.
\]
All coefficients in the active range are positive, while the would-be coefficient of degree \(m+1\) is \((p(d-1)-k-dm)c_m/p\). This proves both positivity and the exact degree change. For completeness, here is a direct proof of *simple, strictly negative roots* (a special case of the classical Veronese real-rootedness phenomenon). Suppose \(P_{p,d,k}\) has \(m\) distinct negative roots \(z_1<\cdots<z_m<0\), with positive leading coefficient. Write \(b=p(d-1)-k\), so \(0\le b-dm<d\). At each \(z_j\), recurrence (2) reduces to
\[
P_{p+1,d,k}(z_j)=\frac{d}{p}z_j(1-z_j)P'_{p,d,k}(z_j).
\]
Those signs alternate. Since \(P_{p+1,d,k}(0)>0\), there is one root in \((z_m,0)\), and one between each two consecutive old roots. If \(b-dm>0\), the new polynomial has degree \(m+1\) and positive leading coefficient, so its sign at negative infinity additionally forces a root in \(( -\infty,z_1)\). Otherwise its degree remains \(m\). Exactly the required number of simple negative roots has been exhibited. The degree-zero base case follows from the same sign and degree argument. This completes the induction for all \(p,d,k\).

**Step 3: strict modulus monotonicity.** Every numerator is a positive constant times \(\prod_j(w+a_j)\), with \(a_j>0\) (empty product permitted). Put \(t=(rs)^d\in(0,1)\) and \(u=1+\cos(d\theta)\in[0,2]\). For each factor,
\[
|a_j+t e^{-id\theta}|^2=(a_j-t)^2+2a_jtu,
\qquad
|1-t e^{-id\theta}|^2=(1+t)^2-2tu.
\]
Each numerator factor is nonnegative and strictly increasing in \(u\), while the positive denominator is strictly decreasing. Thus, for each \(k\),
\[
|F_{p,d,k}(t e^{-id\theta})|^2
\quad\text{is strictly increasing as a function of }u.
\tag{3}
\]
Strictness also holds for constant numerator polynomials because \(p\ge2\) and \(t>0\); it also holds when a numerator vanishes at \(u=0\).

**Step 4: positivity and product ordering.** For \(0\le u<2\), the \(2d\) nodes are all distinct: their radii differ or their relative phase is not zero. Positive definiteness follows from the power-series kernel with every Taylor coefficient strictly positive, since a nontrivial linear combination of evaluations cannot vanish on every monomial (Vandermonde). Hence every \(2\times2\) Fourier block is positive definite and its determinant is strictly positive. By (3), each factor \(A_kB_k-|C_k(\theta)|^2\) strictly decreases in \(u\). When \(u=2\) and \(r=s\), the orbits coincide, so the Gram determinant is zero; otherwise the same strict ordering persists to \(u=2\). Their positive product (1) therefore strictly decreases in \(u\), proving the claimed equivalence and uniqueness. At the unique optimum, \(e^{-id\theta}=-1\); substituting this into (1) gives the stated exact product formula.

## Verification

A standalone Python 3 checker (`CHECK.py`, standard library only) reconstructs \(P_{p,d,k}\) using exact rational arithmetic, compares numerator coefficients against the defining binomial subsequences, independently computes complex determinants of the original \(2d\times2d\) Gram matrix and the Fourier-block product, and verifies strict phase ordering on sample grids. The final checker reports **7,598 passed assertions**. These finite calculations corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Marinescu and Xing (2026; first public September 21, 2026) investigate dependence of weighted Bergman kernels on weight parameters. That is motivating contemporary kernel theory, not a claim that their accessible abstract poses this two-ring determinant problem; their full text was not available for comparison. Jochemko (2016), Theorem 1.1, supplies general real-rootedness of Veronese numerator polynomials: that known input is **not** itself claimed as original. Karvonen, Särkkä and Tanaka (2019) discuss kernel determinant maximization and approximate Fekete points more generally, including Gaussian kernels, without the present all-parameter two-ring Bergman phase-ordering. The new statement is the strict global determinant ordering from combining the cyclic Fourier blocks with negative-real numerator roots. A previous Hardy/Szegő power-one result has a related staggering law, but its Cauchy-determinant argument does not cover higher kernel powers; the present theorem explicitly excludes \(p=1\) to separate the contribution.

## Limitations

The phase maximization is conditional on each orbit already forming a regular \(d\)-gon and on fixed radii. It is not a global design theorem over unrestricted \(2d\)-point sets, a radial-optimization theorem, or a statement about all real kernel exponents. No independent mathematical audit has been performed. Published literature or inaccessible full-text material could contain a stronger formulation not found in the described source comparison.

## References

1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258 (first public September 21, 2026). https://arxiv.org/abs/2609.24258
2. K. Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series*, arXiv:1602.09139 (first public February 29, 2016), especially Theorem 1.1. https://arxiv.org/html/1602.09139v2
3. T. Karvonen, S. Särkkä and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316 (first public December 16, 2019). https://arxiv.org/html/1912.07316v3
