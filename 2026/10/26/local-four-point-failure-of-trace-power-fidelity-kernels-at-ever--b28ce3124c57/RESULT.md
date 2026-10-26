# Local four-point failure of trace-power fidelity kernels at every mixed-state purity

## Finding
For every integer \(d\ge2\), every exponent \(0<r<1\), and every \(0<q<1\), there are four mutually isospectral, strictly positive density matrices \(\rho_0,\ldots,\rho_3\in M_d(\mathbb C)\) whose trace-power Gram matrix has inertia \((3,1,0)\): three strictly positive eigenvalues and exactly one strictly negative eigenvalue.

Specifically, write the Pauli matrices
\[
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}
\]
and embed their linear combinations in a fixed two-dimensional coordinate corner. Let
\[
\rho_j=\frac1d I_d+\frac qd\left[\bigl(\cos(j\pi/2)\sigma_x+\sin(j\pi/2)\sigma_y\bigr)\oplus0_{d-2}\right],\qquad j=0,1,2,3.
\]
For the trace-power kernel
\[
\mathcal K_r(P,Q)=\operatorname{Tr}\left[(P^{1/2}QP^{1/2})^r\right],
\]
let \(G^{(d)}_{r,q}=[\mathcal K_r(\rho_i,\rho_j)]_{i,j=0}^3\). Its unique negative eigenvalue is
\[
\boxed{\lambda_-(d,r,q)=\frac1{d^{2r}}\left((1+q)^{2r}+(1-q)^{2r}+2(1-q^2)^r-2(1+u)^r-2(1-u)^r\right)<0,\quad u=q\sqrt{2-q^2}.}
\]
This eigenvalue is carried by \((1,-1,1,-1)^{\mathsf T}\) and has the sharp small-purity expansion
\[
\boxed{\lambda_-(d,r,q)=-\frac{2r^2(1-r^2)}{3d^{2r}}q^4+O(q^6)\quad(q\downarrow0).}
\]
Each \(\rho_j\) has the same spectrum \(\{(1+q)/d,(1-q)/d,1/d,\ldots,1/d\}\), and \(\|\rho_j-I_d/d\|_{\mathrm{op}}=q/d\). Consequently every neighborhood of \(I_d/d\) contains four faithful isospectral states giving a non-positive-semidefinite trace-power kernel, for every \(0<r<1\). At \(r=1\), by contrast, \(\mathcal K_1(P,Q)=\operatorname{Tr}(PQ)\) is a Hilbert--Schmidt Gram kernel of arbitrary finite order.

## Assumptions and scope
The ambient algebra is \(M_d(\mathbb C)\), its trace is the ordinary, unnormalized matrix trace, and the density matrices have trace one. The power is defined by the positive functional calculus. The family has two noncommuting Pauli directions in a common two-dimensional corner. The strict claim requires \(d\ge2\), \(0<r<1\), \(0<q<1\). No assertion of a sharp global lower eigenvalue over all quadruples is made.

## Proof
**Spectral reduction.** First take \(d=2\) and \(\tau_j=\tfrac12(I_2+q(\cos(j\pi/2)\sigma_x+\sin(j\pi/2)\sigma_y))\). If the two Pauli directions make an angle \(\theta\), then
\[
\operatorname{Tr}(\tau_i\tau_j)=\tfrac12(1+q^2\cos\theta),\qquad
\det(\tau_i^{1/2}\tau_j\tau_i^{1/2})=\frac{(1-q^2)^2}{16}.
\]
The two positive eigenvalues of \(\tau_i^{1/2}\tau_j\tau_i^{1/2}\) therefore give the following three entries of the real circulant \(4\times4\) kernel: a diagonal entry \(D\), an adjacent entry \(A\), and an opposite entry \(B\), where
\[
\begin{aligned}
D&=4^{-r}\left[(1+q)^{2r}+(1-q)^{2r}\right],\\
A&=4^{-r}\left[(1+u)^r+(1-u)^r\right],\\
B&=4^{-r}\,2(1-q^2)^r,\qquad u=q\sqrt{2-q^2}.
\end{aligned}
\]
Hence the four eigenvalues are \(D+2A+B\), \(D-B\) twice, and \(D-2A+B\). The first is positive, and the second is strictly positive by strict arithmetic--geometric mean because \(q>0\). It remains to prove \(D-2A+B<0\).

**Strict sign for every fractional exponent.** Set \(c=1-q^2\) and introduce two four-element multisets
\[
L=\{(1+q)^2,(1-q)^2,c,c\},\qquad R=\{1+u,1+u,1-u,1-u\}.
\]
All entries are positive when \(0<q<1\). Both sets have four entries, equal sums, and equal products \(c^4\), since \(1-u^2=c^2\). Let
\[
H(s)=\sum_{x\in L}\frac1{s+x}-\sum_{y\in R}\frac1{s+y}.
\]
A direct common-denominator calculation gives the exact rational identity
\[
H(s)=\frac{8q^4s(s-c)}{(s+c)(s+(1+q)^2)(s+(1-q)^2)((s+1)^2-u^2)},\qquad s>0.
\]
Every denominator is positive. Thus \(H(s)<0\) for \(0<s<c\), while \(H(s)>0\) for \(s>c\). Equality of the products gives \(\int_0^\infty H(s)\,ds=0\) by integrating the logarithmic derivatives, with cancellation at infinity. Therefore
\[
\int_0^\infty s^rH(s)\,ds=\int_0^\infty(s^r-c^r)H(s)\,ds>0
\]
for each \(0<r<1\); both integrals converge absolutely because \(H(s)=O(s)\) near zero and \(H(s)=O(s^{-3})\) at infinity. Using the standard fractional-power identity
\[
x^r=\frac{\sin(\pi r)}\pi\int_0^\infty s^{r-1}\frac{x}{s+x}\,ds\quad (x>0,\ 0<r<1),
\]
and the equal cardinalities of \(L,R\), we obtain
\[
\sum_{x\in L}x^r-\sum_{y\in R}y^r
=-\frac{\sin(\pi r)}\pi\int_0^\infty s^rH(s)\,ds<0.
\]
The left side is exactly \(4^r(D+B-2A)\). This proves the strict negative eigenvalue and its uniqueness in dimension two.

**All matrix dimensions.** For arbitrary \(d\ge2\), the density matrix decomposes as \(\rho_j=(2/d)\tau_j\oplus d^{-1}I_{d-2}\). Functional calculus on block-diagonal matrices yields
\[
G^{(d)}_{r,q}=(2/d)^{2r}G^{(2)}_{r,q}+(d-2)d^{-2r}J_4,
\]
where \(J_4\) is the all-ones matrix. The rank-one summand affects only the positive constant-vector eigenvalue. The three other Fourier eigenvectors are unchanged; hence the inertia remains \((3,1,0)\), and the displayed exact eigenvalue formula follows from scaling.

**Sharp quartic coefficient.** Expand the five scalar powers in the explicit eigenvalue formula at \(q=0\) using the generalized binomial theorem and \(u=q\sqrt{2-q^2}\). Constant and quadratic terms cancel identically, odd terms vanish by symmetry, and the fourth-degree coefficient is \(2r^2(r^2-1)/3\). This gives the displayed strictly negative quartic asymptotic. The uniform trace and spectrum statements follow immediately from the Pauli block. No nonzero purity threshold exists.

## Verification
The standalone standard-library script `verify.py` checks the resolvent identity with exact rational arithmetic at 270 parameter pairs, cross-checks 400 evaluations of the matrix-power kernel using explicit matrix products and eigenvalues against the closed formulas, and tests the quartic coefficient and dimension scaling. These are finite consistency checks only; the strict universal sign and all-dimensional statements follow from the preceding analytic proof.

## Relationship to prior work
Vuong and Osaka's 2026 three-point trace-positivity theorem proves positive semidefiniteness for triples at \(1/2\le r\le1\) and supplies a four-*pure*-qubit obstruction at its order-three boundary (Remark 2.4). The present theorem gives an exact quantitative four-point obstruction for **every strictly positive common spectrum**, including spectra arbitrarily close to the maximally mixed state, in every matrix dimension and for every \(0<r<1\). The pure endpoint does not imply the local assertion near the identity, and the quartic coefficient is additional quantitative information.

Fannes, de Melo, Roga and Życzkowski studied matrices of root fidelities, noted that four-point positivity can fail, and proved positive semidefiniteness of the *squared*-fidelity kernel on qubit states. For qubits its squared fidelity equals \(\operatorname{Tr}(PQ)+2\sqrt{\det P\,\det Q}\), a positive-semidefinite rank-one augmentation of the \(r=1\) trace-Gram kernel; it is not the \(r<1\) trace-power kernel studied here. Classical counterexamples for fractional entrywise Hadamard powers concern a distinct matrix functional and do not directly imply this trace-power claim.

## Limitations
This is an explicit isospectral family, not a solution of the global extremal negative-eigenvalue problem for arbitrary density quadruples. The novelty comparison is relative to inspected primary literature and targeted indexed searches; equivalences in more remote kernel-positivity or entrywise-power literature remain a priority risk. Computational tests do not independently certify the analytical argument. Independent external validation has not been performed.

## References
- T. D. Vuong and H. Osaka, *Three-Point Trace Positivity: Schatten Norm Compression and Interpolating Metrics*, arXiv:2610.11021, first submitted 2026-10-08, especially Theorem 1.1 and Remark 2.4, https://arxiv.org/abs/2610.11021.
- M. Fannes, F. de Melo, W. Roga and K. Życzkowski, *Matrices of fidelities for ensembles of quantum states and the Holevo quantity*, arXiv:1104.2271, especially Sections 3--4, https://arxiv.org/abs/1104.2271.
- C. H. FitzGerald and R. A. Horn, *On fractional Hadamard powers of positive definite matrices*, Journal of Mathematical Analysis and Applications **61** (1977), 633--642, https://doi.org/10.1016/0022-247X(77)90167-6.
- T. Jain, *Hadamard powers of some positive matrices*, Linear Algebra and Its Applications **528** (2017), 147--158, https://doi.org/10.1016/j.laa.2016.06.030.
