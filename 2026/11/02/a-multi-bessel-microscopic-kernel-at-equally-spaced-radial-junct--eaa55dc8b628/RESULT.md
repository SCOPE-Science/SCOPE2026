# A multi-Bessel microscopic kernel at equally spaced radial junctions

## Finding
Fix an integer \(q\ge 3\), write \(\omega=e^{2\pi i/q}\), and equip the \(q\)-ray star \(E_q=\bigcup_{r=0}^{q-1}\{t\omega^r:0\le t\le 1\}\) with the probability measure
\[
\int_{E_q}f\,d\mu_q=\frac1q\sum_{r=0}^{q-1}\int_0^1 f(t\omega^r)\,dt.
\]
Let \(K_N(z,w)\) denote the reproducing kernel of the space of all complex polynomials of degree at most \(N\), with this \(L^2(\mu_q)\) inner product. Put \(a_h=(2h+1)/q\), and \(m_h=\lfloor(N-h)/q\rfloor\), for \(0\le h<q\). Define \(J_j^{(a)}(t)=P_j^{(0,a-1)}(2t-1)\), where \(P_j^{(\alpha,\beta)}\) denotes the usual Jacobi polynomial. Then the **entire two-variable kernel** is
\[
K_N(z,w)=q\sum_{\substack{0\le h<q\\m_h\ge0}}(z\overline w)^h
 \sum_{j=0}^{m_h}(2j+a_h)J_j^{(a_h)}(z^q)
 \overline{J_j^{(a_h)}(w^q)}. \tag{1}
\]
In particular, with \(m=\lfloor N/q\rfloor\),
\[
K_N(0,0)=\left[\frac{\Gamma(m+1+1/q)}{\Gamma(1+1/q)\Gamma(m+1)}\right]^2
\sim\frac{m^{2/q}}{\Gamma(1+1/q)^2}. \tag{2}
\]

**Microscopic junction theorem.** Let \({}_0F_1(;a;u)=\sum_{k=0}^{\infty}u^k/((a)_k k!)\), an entire function of \(u\). As \(N\to\infty\), the following limit holds locally uniformly for \((\zeta,\eta)\in\mathbb C^2\):
\[
\frac{K_N(m^{-2/q}\zeta,m^{-2/q}\eta)}{m^{2/q}}
\longrightarrow \mathcal K_q(\zeta,\eta), \tag{3}
\]
where the explicit positive-definite **multi-Bessel kernel** is
\[
\mathcal K_q(\zeta,\eta)
=2q\sum_{h=0}^{q-1}\frac{(\zeta\overline\eta)^h}{\Gamma(a_h)^2}
 \int_0^1 s^{2a_h-1}
 {}_0F_1(;a_h;-s^2\zeta^q)
 \overline{{}_0F_1(;a_h;-s^2\eta^q)}\,ds. \tag{4}
\]
The diagonal normalization is exact: \(\mathcal K_q(0,0)=\Gamma(1+1/q)^{-2}\). Thus the natural microscopic distance to the junction is \(N^{-2/q}\), and the squared evaluation norm grows at the fractional rate \(N^{2/q}\). This is a one-claim package: formulas (1), (2), and (4) give the exact finite-degree and microscopic forms of the same polynomial reproducing kernel.

## Assumptions and scope
The integer \(q\) is fixed as \(N\to\infty\). Each ray has unit length and uniform arclength density, with total measure one. The polynomial degree is at most \(N\); it is **not** a homogeneous-degree space, and no area measure on the disk is used. Evaluation points in (3) can be arbitrary complex points, not only points on the rays. The kernel is holomorphic in its first variable and antiholomorphic in its second. The number \(m=\lfloor N/q\rfloor\) tends to infinity; it is positive for all sufficiently large \(N\). Formula (1) is valid also for \(0\le N<q\).

## Proof
**Orthogonal congruence blocks and exact normalization.** The \(q\)-fold angular averaging shows that powers \(z^k,z^\ell\) are orthogonal whenever \(k\not\equiv\ell\pmod q\). Consequently the polynomial space is the orthogonal direct sum of the subspaces \(z^h R(z^q)\), where \(\deg R\le m_h\) and \(0\le h<q\). With \(a=a_h\), the substitution \(u=t^q\) gives
\[
\|z^hR(z^q)\|_{L^2(\mu_q)}^2
 =\int_0^1 t^{2h}|R(t^q)|^2dt
 =\frac1q\int_0^1u^{a-1}|R(u)|^2du. \tag{5}
\]
The shifted Jacobi orthogonality identity for \(a>0\) is
\[
\int_0^1u^{a-1}J_j^{(a)}(u)J_k^{(a)}(u)du
 =\frac{\mathbf1_{j=k}}{2j+a}. \tag{6}
\]
Hence \(\{\sqrt{q(2j+a_h)}z^h J_j^{(a_h)}(z^q)\}_{h,j}\) is an orthonormal polynomial basis, proving (1). At \(z=0\), only \(h=0\) survives, and \(J_j^{(a)}(0)=(-1)^j(a)_j/j!\). Therefore
\[
K_N(0,0)=\sum_{j=0}^m\frac{2j+a}{a}\left(\frac{(a)_j}{j!}\right)^2,
\quad a=1/q. \tag{7}
\]
The sum telescopes because the difference of consecutive values of \(((a+1)_m/m!)^2\) is exactly its \(j=m\) summand, proving the gamma formula in (2). The asymptotic follows from the standard gamma ratio.

**Uniform microscopic limit.** The terminating hypergeometric identity
\[
(-1)^jJ_j^{(a)}(u)=\frac{(a)_j}{j!}\,{}_2F_1(-j,j+a;a;u) \tag{8}
\]
holds for all \(a>0\). Fix a compact disk \(|v|\le R\) and use \(u=v/m^2\). For \(0<\delta\le j/m\le1+O(m^{-1})\), the gamma ratio and coefficientwise convergence of (8) yield uniformly in \(v\):
\[
m^{1-a}(-1)^jJ_j^{(a)}(v/m^2)
\longrightarrow \frac{s^{a-1}}{\Gamma(a)}{}_0F_1(;a;-s^2v)
\quad\text{when }j/m\to s\in[\delta,1]. \tag{9}
\]
Here uniformity follows from the power-series majorant: for \(j\le m+C\), the absolute value of the \(k\)-th hypergeometric term is bounded by \((C_R)^k/((a)_k k!)\), independent of \(j,m\); the bound is summable. Moreover, throughout \(0\le j\le m+C\), the same argument and the gamma-ratio estimate imply
\[
|J_j^{(a)}(v/m^2)|\le C_{a,R}(j+1)^{a-1}. \tag{10}
\]
The portion \(0\le j<\delta m\) of the \(h\)-th normalized kernel is therefore at most \(C\delta^{2a_h}\) on compact \((\zeta,\eta)\)-sets, because \(\sum_{j<\delta m}(j+1)^{2a_h-1}=O((\delta m)^{2a_h})\). On \(\delta m\le j\le m_h\), insert (9) into (1) with \(z=m^{-2/q}\zeta\), \(w=m^{-2/q}\eta\). As \(m_h/m\to1\), the resulting Riemann sum converges locally uniformly to the \(h\)-th term of (4), noting that \(2a_h-4h/q=2/q\). Finally let \(\delta\downarrow0\); the integrals converge because \(a_h>0\). This proves (3)-(4) with all \(q\) residue sectors simultaneously. Setting \(\zeta=\eta=0\) in (4), only \(h=0\) contributes and the integral is \(1/(2a_0)\), proving the stated diagonal normalization. Positive definiteness follows as a locally uniform limit of positive-definite kernels, or directly from the integral-of-squares representation (4).

## Verification
The standalone, standard-library-only file `star_kernel_checker.py` reconstructs exact rational moment Gram matrices with entries \(\langle z^j,z^k\rangle=\mathbf1_{j\equiv k\ ({\rm mod}\ q)}/(j+k+1)\), inverts them over exact fractions, and compares their kernels with (1) for rational evaluation points. It verifies (2) independently for five ray counts over thirteen successive degrees and compares the diagonal gamma-ratio limit numerically. The recorded invocation is `python3 star_kernel_checker.py`; it prints `PASS: 174 exact and asymptotic finite checks`. This finite computation does not establish the locally uniform infinite-degree limit; (8)-(10) and the Riemann-sum argument do.

## Relationship to prior work
Marinescu and Vu (arXiv:2210.11031, first public 2022-10-20) establish polynomial bounds for Bergman kernels associated with piecewise-smooth totally real sets, explicitly noting that singular-point asymptotics are more complicated than at smooth points. Their Theorems 1.4-1.5 supply no q-junction microscopic two-variable formula. Milovanović (preprint posted 2024-12-23, subsequently Axioms 2025) studies orthogonal polynomials on radial rays. In §6.1, especially its moment formula (30) and Theorem 5, the angular congruence-block decomposition underlying (5) is an established ingredient. That paper does not state the locally uniform polynomial kernel limit (3)-(4), or the fractional gamma-normalized junction asymptotic (2). These ingredients must not be claimed new independently. Danka and Totik (arXiv:1504.03968) establish sharp Christoffel asymptotics on unions of Jordan curves/arcs with power weights, including Bessel behavior at arc endpoints. That classical one-arc endpoint result is related but does not explicitly identify the simultaneous \(q\)-channel two-variable kernel at a transverse common junction. The original 59-page manuscript was not fully accessible for comparison in this review; that remains a real priority risk.

## Limitations
The theorem concerns exact, equidistant, equal-length rays with uniform weights. It makes no claim about uneven ray angles, variable weights, perturbation stability, or universality beyond this class. The special-function reduction is classical; the proposed new mathematical content is the complete junction-rescaled kernel and its exact normalization, not the existence of Jacobi polynomials. Broader uninspected literature on multiply connected or intersecting arcs could contain an equivalent statement. Independent mathematical audit has not been performed.

## References
- G. Marinescu and D.-V. Vu, *Bergman kernel functions associated to measures supported on totally real submanifolds*, arXiv:2210.11031, initially posted 2022-10-20; J. Reine Angew. Math. 810 (2024), 217–251.
- G. V. Milovanović, *Orthogonal Polynomials on Radial Rays in the Complex Plane: Construction, Properties and Applications*, preprints.org manuscript 202412.1898, posted 2024-12-23; Axioms 14 (2025), 65, DOI 10.3390/axioms14010065.
- T. Danka and V. Totik, *Christoffel functions with power type weights*, arXiv:1504.03968, initially posted 2015-04-15; J. Eur. Math. Soc. 20 (2018), 747–796.
- NIST Digital Library of Mathematical Functions, Chapter 18 (Jacobi polynomials and Christoffel–Darboux kernels); hypergeometric and Bessel-series identities used explicitly in the proof.
