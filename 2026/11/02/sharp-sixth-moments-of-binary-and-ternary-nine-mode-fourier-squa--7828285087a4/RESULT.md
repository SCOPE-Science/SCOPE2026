# Sharp sixth moments of binary and ternary nine-mode Fourier squares

## Finding
Let \(q\in\{2,3\}\), \(\zeta_q=e^{2\pi i/q}\), and for a phase matrix \(A=(a_{ij})_{0\le i,j\le2}\) with \(a_{ij}\in\{1,\zeta_q,\ldots,\zeta_q^{q-1}\}\) define
\[
P_A(z,w)=\sum_{i=0}^{2}\sum_{j=0}^{2}a_{ij}z^i w^j,\qquad
M_6(A)=\int_{\mathbb T^2}|P_A(z,w)|^6\,dm(z)\,dm(w).
\]
The sharp phase-alphabet minima are
\[
\boxed{\min_{A\text{ binary}}M_6(A)=1641,\qquad
\min_{A\text{ ternary}}M_6(A)=1197.}
\]
All minimizers are classified up to the transformations \(a_{ij}\mapsto\zeta_q^{\alpha+\beta i+\gamma j}a_{ij}\), where \(\alpha,\beta,\gamma\in\mathbb Z/q\mathbb Z\). Each class has a unique normalization \(a_{00}=a_{10}=a_{01}=1\). In the order
\[
(a_{02},a_{11},a_{12},a_{20},a_{21},a_{22})=(\zeta_q^{u_1},\ldots,\zeta_q^{u_6}),
\]
the normalized binary minimizers have exponent vectors
\[
(0,0,1,1,0,1),\quad(0,1,1,1,0,1),\quad(1,0,0,0,1,1),\quad(1,1,0,0,1,1),
\]
and the normalized ternary minimizers have exponent vectors
\[
(0,1,2,0,2,1),\qquad(0,2,1,0,1,2).
\]
In particular the ternary minimizers are exactly the order-three Fourier coefficient matrix and its complex conjugate, up to common phase and two frequency translations. There are exactly \(32\) labelled binary minimizers and \(54\) labelled ternary minimizers without normalization.

## Assumptions and scope
All coefficients have modulus one and belong to the specified finite alphabet. Haar measure on each circle is probability normalized. Frequency exponents range over the full \(3\times3\) rectangle, and no finite-grid aliasing is used. The statement optimizes over all \(2^9\) or \(3^9\) arrays, not only symmetric or Hadamard arrays. These are sixth-power moments, not sixth roots.

## Proof
Multiplication of coefficients by \(\zeta_q^{\alpha+\beta i+\gamma j}\) changes \(P_A(z,w)\) into \(\zeta_q^\alpha P_A(\zeta_q^\beta z,\zeta_q^\gamma w)\). Haar invariance preserves \(M_6\). The three exponents \(\alpha,\beta,\gamma\) uniquely normalize entries \((0,0),(1,0),(0,1)\) to one; the remaining six phases range independently over \((\mathbb Z/q\mathbb Z)^6\). There are therefore exactly \(q^6\) normalized cases, each representing precisely \(q^3\) labelled arrays.

Character orthogonality gives the exact finite identity
\[
M_6(A)=\sum_{r=0}^{6}\sum_{s=0}^{6}\left|[z^r w^s]P_A(z,w)^3\right|^2.
\]
For any normalized exponent vector \(u\), define integers \(C_{r,s,e}(u)\) by counting ordered triples \(((i_1,j_1),(i_2,j_2),(i_3,j_3))\in(\{0,1,2\}^2)^3\) such that \(\sum i_\ell=r\), \(\sum j_\ell=s\), and the sum of their six free-entry exponents is congruent to \(e\pmod q\). Thus
\[
[z^r w^s]P_A^3=\sum_{e=0}^{q-1}C_{r,s,e}(u)\zeta_q^e.
\]
For \(q=2\) the exact squared modulus is \((C_0-C_1)^2\). For \(q=3\), using \(\zeta_3^2=-1-\zeta_3\), put \(X=C_0-C_2\), \(Y=C_1-C_2\); then the squared modulus is \(X^2-XY+Y^2\). These are nonnegative *integers* with no numerical approximation.

The complete exhaustive integer computation, reproduced independently by (i) ordered triples of the nine frequency positions and (ii) unordered triples with exact multinomial coefficients, evaluates all \(64\) normalized binary and \(729\) normalized ternary arrays. Both routes agree *for every array*. Their exact minima and full sets of attaining exponent vectors are the numbers stated in the Finding. The embedded checker is complete standalone Python 3 code for these finite sums; it also prints the entire exact distribution of sixth moments. The accompanying CSV records this distribution (19 distinct binary values and 63 distinct ternary values). Since every admissible array is represented and every arithmetic operation is integral, this finite certificate proves the global finite-alphabet optima and the entire minimizer classification.

## Verification
Execute `python3 sixth_moment_checker.py` in the directory containing the two accompanying artifacts. Its independent coefficient-counting routes agree at every normalized phase choice, and it asserts the minima, number of minimizers, number of distinct values, and total configurations. As an additional check, the explicit minimizers give the same sixth moments by direct exact discrete Fourier quadrature on a \(24\times24\) angular grid: since the integrand has Fourier degrees at most six in each variable, that quadrature is exact in exact arithmetic. A numerical implementation of this last check produced the displayed integer values, but the independent integer enumeration is the proof certificate.

## Relationship to prior work
Balister, Bollobás, Morris, Sahasrabudhe and Tiba prove existence of flat one-variable Littlewood polynomials with sign coefficients; their theorem does not determine the sharp sixth moment for this two-variable nine-term aperture. A related published record, *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, gives exact **fourth** moments and the ternary Fourier minimizers for the same support. The present claim concerns the **sixth** moment and the binary and ternary sixth-moment optimizer classes. The fourth moment does not determine the sixth moment: normalized ternary exponent vectors \((0,0,1,0,2,0)\) and \((0,1,2,0,2,0)\) both have fourth moment \(133\), but have sixth moments \(2682\) and \(2367\) respectively. Consequently the previously tabulated fourth-moment values cannot simply be relabelled as the present certificate. Exact prior priority of an independent sixth-moment census remains subject to bibliographic verification.

## Limitations
Only the alphabets of orders two and three and the fixed \(3\times3\) frequency rectangle are treated. The theorem does not assert global minimization over arbitrary complex unimodular phases, any other alphabet, nonunit magnitudes or larger apertures. It is an exact finite classification, not an asymptotic inequality or a general noise-robustness theorem. No independent mathematical audit has been performed.

## References
1. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464 (first public 2019-07-22), Annals of Mathematics 192 (2020), 977–1004, DOI:10.4007/annals.2020.192.3.6.
2. *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, publicly indexed research record: published October 2026; fourth-moment result only, as indexed.
