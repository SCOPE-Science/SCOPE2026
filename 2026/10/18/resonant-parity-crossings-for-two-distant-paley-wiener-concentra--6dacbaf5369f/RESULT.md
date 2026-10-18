# Resonant parity crossings for two distant Paley–Wiener concentration intervals

## Finding

Fix a half-length \(a>0\) and a frequency half-bandwidth \(W>0\) satisfying \(4Wa<1\). Put \(\omega=2\pi W\), \(I=[-a,a]\), and
\[
K_W(t)=\begin{cases}\frac{\sin(\omega t)}{\pi t},&t\ne0,\\2W,&t=0.\end{cases}
\]
The positive compact operator \(T:L^2(I)\to L^2(I)\) has kernel \(K_W(x-y)\). Its maximal eigenvalue \(\lambda\) is simple, with a strictly positive, even, real normalized eigenfunction \(\phi\). Define
\[
A=\int_{-a}^{a}\phi(x)\cos(\omega x)\,dx,\qquad
B=\int_{-a}^{a}x\phi(x)\sin(\omega x)\,dx,
\]
\[
q(x)=\sin(\omega x),\qquad
L=\frac{A^2}{\pi^2}\big\langle q,(\lambda-T)_{\phi^\perp}^{-1}q\big\rangle,
\qquad \tau_*=\frac{2B}{\omega A}.
\]
All three quantities \(A,B,L\) and \(\tau_*\) are positive. The inverse is the bounded inverse of \(\lambda I-T\) restricted to the orthogonal complement of \(\phi\).

For \(D>2a\) let \(E_D=I\cup(D+I)\). Denote by \(\Lambda_1(D)\ge\Lambda_2(D)\) the largest two eigenvalues of the compact sinc concentration operator with kernel \(K_W(x-y)\) on \(L^2(E_D)\). Equivalently, \(\Lambda_1(D)\) is the optimal fraction of the squared \(L^2\)-norm of a signal with Fourier support in \([-W,W]\) that can be captured inside \(E_D\).

For any integer \(n\to\infty\), set \(d_n=n\pi/\omega\) and \(D=d_n+\tau/d_n\). Uniformly for \(\tau\) in every fixed compact subset of \(\mathbb R\),
\[
\boxed{\displaystyle
\Lambda_{1,2}(D)=\lambda+\frac1{d_n^2}
\left[L\ \pm\ \frac{|\omega A^2\tau-2AB|}{\pi}\right]
+O_{a,W,\tau\text{-compact}}(d_n^{-3}).}
\]
The signs correspond to the sorted first and second eigenvalues.

For every sufficiently small fixed \(\eta>0\), and every sufficiently large integer \(n\), there is **exactly one** separation \(D_n^*\) satisfying \(|d_n(D_n^*-d_n)-\tau_*|<\eta\) at which the two top eigenvalues are equal. It has the expansion
\[
\boxed{\displaystyle D_n^*=d_n+\frac{\tau_*}{d_n}+O_{a,W}(d_n^{-2}),\qquad
\Lambda_1(D_n^*)=\Lambda_2(D_n^*)=\lambda+\frac{L}{d_n^2}+O_{a,W}(d_n^{-3}).}
\]
Thus the genuine eigenvalue-crossing separations are displaced to the right of the naive sinc zeros \(d_n\) by a positive amount of order \(d_n^{-1}\).

Away from or near these resonances, the following weaker but global asymptotic also holds as \(D\to\infty\):
\[
\boxed{\displaystyle
\Lambda_{1,2}(D)=\lambda\pm\frac{A^2|\sin(\omega D)|}{\pi D}+O_{a,W}(D^{-2}).}
\]

## Assumptions and scope

The Fourier transform is \(\widehat f(\xi)=\int_{\mathbb R} f(x)e^{-2\pi i x\xi}\,dx\). The bandlimited class is the closed subspace of \(L^2(\mathbb R)\) with Fourier support in \([-W,W]\). The integrable kernel \(K_W\) is the inverse Fourier transform of its indicator and is positive definite. For each finite-measure set, compressing the band-projection kernel to that set gives a compact nonnegative self-adjoint operator, whose top eigenvalue equals the corresponding energy-concentration optimum.

The restriction \(4Wa<1\) ensures \(K_W(x-y)>0\) for all \(x,y\in I\): indeed \(|\omega(x-y)|\le4\pi Wa<\pi\). Standard positivity-improving compact-operator theory then gives a simple positive top eigenvalue. Reflection symmetry forces its eigenfunction to be even. Also \(\omega a<\pi/2\), so both \(\cos(\omega x)>0\) and \(x\sin(\omega x)\ge0\) on \(I\), proving \(A,B>0\). The positivity of \(L\) follows because \(q\ne0\) is odd and orthogonal to \(\phi\), and the reduced resolvent is strictly positive.

Every assertion fixes \(a,W\) before taking \(n\) or \(D\) to infinity. No uniformity up to the bandwidth threshold \(4Wa=1\) is claimed.

## Proof

**1. Exact block and parity reduction.** Identify the space \(L^2(E_D)\) with two copies of \(L^2(I)\), one translated by \(D\). The full integral operator has the block matrix
\[
\mathcal T_D=\begin{pmatrix}T&B_D\\B_D^*&T\end{pmatrix},
\qquad B_D(x,y)=K_W(D+y-x).
\]
Let \((Rf)(x)=f(-x)\). Since \(RTR=T\), conjugating the block matrix by the unitary \(\operatorname{diag}(I,R)\) gives
\[
\begin{pmatrix}T&C_D\\C_D&T\end{pmatrix},
\qquad C_D(x,y)=K_W(D-x-y)=C_D(y,x).
\]
A constant two-component Hadamard unitary therefore decomposes \(\mathcal T_D\) **exactly**, for every separation, as the orthogonal direct sum of the two self-adjoint operators \(T+C_D\) and \(T-C_D\). Their respective top eigenvalues are denoted \(\lambda_+(D)\) and \(\lambda_-(D)\). Since \(\|C_D\|_{\mathrm{op}}=O_{a,W}(D^{-1})\) and \(\lambda\) is isolated from the remaining spectrum of \(T\), these are exactly the two largest eigenvalues of \(\mathcal T_D\), counted with multiplicity, once \(D\) is sufficiently large.

**2. Uniform resonant kernel expansion.** Write \(d=d_n=n\pi/\omega\), \(\varepsilon=(-1)^n\), and \(D=d+\tau/d\). For \(s=x+y\in[-2a,2a]\), the numerator obeys
\[
\sin(\omega(D-s))=\varepsilon\left[-\sin(\omega s)+\frac{\omega\tau}{d}\cos(\omega s)\right]+O(d^{-2}),
\]
while \((D-s)^{-1}=d^{-1}+s d^{-2}+O(d^{-3})\). Hence, uniformly on \(I\times I\) and on compact \(\tau\)-sets,
\[
C_D=\frac{\varepsilon}{d}U+\frac{\varepsilon}{d^2}V_\tau+O_{\mathrm{op}}(d^{-3}),
\]
\[
U(x,y)=-\frac{\sin(\omega(x+y))}{\pi},\qquad
V_\tau(x,y)=\frac{\omega\tau\cos(\omega(x+y))-(x+y)\sin(\omega(x+y))}{\pi}.
\]
The same expansion can be differentiated with respect to \(\tau\), with a uniform \(O_{\mathrm{op}}(d^{-3})\) remainder in that derivative. This follows by direct differentiation of the smooth kernel and the fact that \(D\asymp d\) uniformly on compact \(\tau\)-sets.

**3. Exact matrix elements.** Parity of \(\phi\) gives
\[
\langle\phi,U\phi\rangle=0,\qquad U\phi=-\frac{A}{\pi}q,
\qquad
\langle\phi,V_\tau\phi\rangle=\frac{\omega\tau A^2-2AB}{\pi}.
\]
For the last formula, expand \(\sin(\omega(x+y))\) and \(\cos(\omega(x+y))\) into products and cancel all integrals that contain a single odd factor. In particular the two terms involving \(x+y\) contribute exactly \(2AB\).

**4. Isolated-eigenvalue perturbation.** If \(T+tH_1+t^2H_2+O_{\mathrm{op}}(t^3)\) is self-adjoint and \(\lambda\) is isolated and simple with unit eigenvector \(\phi\), the resolvent/Schur-complement expansion gives its nearby eigenvalue as
\[
\lambda+t\langle\phi,H_1\phi\rangle+t^2\left[\langle\phi,H_2\phi\rangle+\big\langle QH_1\phi,(\lambda-T)_{\phi^\perp}^{-1}QH_1\phi\big\rangle\right]+O(t^3),
\]
where \(Q=I-|\phi\rangle\langle\phi|\). To verify the formula, solve the complementary eigenvector equation to first order as \(t(\lambda-T)_{\phi^\perp}^{-1}QH_1\phi+O(t^2)\), and substitute into the \(\phi\)-component. This derivation also gives uniform remainders for uniformly bounded perturbations and their first parameter derivatives.

Apply it to \(T\pm C_D\) with \(t=d^{-1}\), \(H_1=\pm\varepsilon U\), and \(H_2=\pm\varepsilon V_\tau\). Using Step 3, the first-order term vanishes and the quadratic resolvent term equals \(L\) for both parity branches. Thus
\[
\lambda_\pm(d+\tau/d)=\lambda+\frac{1}{d^2}\left[L\pm\frac{\varepsilon}{\pi}(\omega A^2\tau-2AB)\right]+O(d^{-3}).
\]
Sorting the two branches proves the announced uniform crossover formula.

**5. Actual crossings rather than near-degeneracies.** Put \(F_n(\tau)=\lambda_+(d+\tau/d)-\lambda_-(d+\tau/d)\). The parameter-differentiable perturbation bound from Step 4 yields, near the positive constant \(\tau_*\),
\[
F_n(\tau)=\frac{2\varepsilon}{\pi d^2}(\omega A^2\tau-2AB)+O(d^{-3}),
\qquad
F_n'(\tau)=\frac{2\varepsilon\omega A^2}{\pi d^2}+O(d^{-3}).
\]
The second derivative estimate here is not required. Since \(A>0\), the derivative has constant nonzero sign on any fixed compact neighborhood of \(\tau_*\) when \(n\) is large. Opposite endpoint signs and the intermediate-value theorem give exactly one zero \(\tau_n\) in that neighborhood, with \(\tau_n=\tau_*+O(d^{-1})\). Taking \(D_n^*=d+\tau_n/d\) proves its location and the common eigenvalue. Equality is exact at this point because the two parity branches are genuine independent invariant subspaces, not an approximate splitting.

**6. General separation.** For unrestricted \(D\to\infty\), uniformly over \(x,y\in I\),
\[
C_D(x,y)=\frac{\sin(\omega D-\omega(x+y))}{\pi D}+O(D^{-2}).
\]
Taking its expectation in the even state \(\phi\) kills the cosine-of-\(D\) term and gives \(A^2\sin(\omega D)/(\pi D)+O(D^{-2})\). First-order isolated-eigenvalue perturbation for \(T\pm C_D\) (whose quadratic remainder is \(O(D^{-2})\)) yields the final sorted off-resonance formula.

## Verification

The accompanying standalone program `verification/check_sinc_gaps.py` reconstructs both parity-branch matrices by independent Gauss–Legendre quadrature on \(I\), computes \(\lambda,A,B,L\), compares the predicted quadratic coefficients to direct eigenspectra, and numerically locates the exact crossings of the discrete quadrature matrices for four growing separation indices. It uses \(a=1/4\) and \(W=1/2\), within the rigorous positivity range. At 160 quadrature nodes it finds approximately \(\tau_*=0.0422264619137\) and \(L=0.00859942411434\). The computed crossing scales for indices 20, 40, 80 and 120 approach this value; the branch-splitting and centroid asymptotics agree with the proven orders. All infinite-dimensional conclusions follow from the operator proof above, not from finite quadrature.

## Relationship to prior work

Abreu and Speckbacher's July 2026 theorem proves that a single interval is globally optimal for energy concentration among measurable sets of fixed measure. It is a rearrangement theorem, not an asymptotic for the first two eigenvalues of two distant components. Zelent's October 2026 stability work studies deviations from a *single* optimal interval; its detached-piece discussion involves a vanishing removed component, rather than two fixed-length components at diverging separation.

Fahs and Krasovsky study a sine-kernel **Fredholm determinant** in a large-bandwidth/two-gap regime, rather than the top two eigenvalues with fixed bandwidth and diverging geometric separation. Classical prolate-spheroidal theory supplies the single-interval spectral setting and spectral simplicity. A previously published concentration calculation on a very small detached piece is likewise not a claim about oscillatory parity crossings for two equal distant intervals. The current theorem instead identifies a cancellation of the first-order parity splitting at the sinc nodes, computes the next-order displacement, and shows that this cancellation creates infinitely many **exact** crossings.

## Limitations

The theorem requires the strict small time-bandwidth condition \(4Wa<1\), fixed \(a,W\), and two congruent intervals. It does not establish a crossing law for unequal component sizes, more than two components, or general time-bandwidth products. The next coefficient beyond the displayed critical-shift precision is not determined. Historical priority cannot be established by indexed literature searches alone: an equivalent earlier separated-sinc spectral calculation could be unindexed. The numerical checker uses finite-dimensional quadrature as a diagnostic only.

## References

1. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1, first posted 21 July 2026.
2. D. Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1, first posted 1 October 2026.
3. B. Fahs and I. Krasovsky, *Sine-kernel determinant on two large intervals*, arXiv:2003.08136, 2020.
4. D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—I*, Bell System Technical Journal 40 (1961), 43–63.
5. D. L. Donoho and P. B. Stark, *A note on rearrangements, spectral concentration, and the zero-order prolate spheroidal wavefunction*, IEEE Transactions on Information Theory 39 (1993), 257–260.
