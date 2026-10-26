# Moment-shifted parity resonances for maximal Slepian concentration on two distant intervals

## Finding

The leading two eigenvalues of a sine-kernel Fourier-concentration operator on two equal and distant intervals meet **exactly** at infinitely many separations, and the crossings are transverse. Their locations have a nonzero, shape-dependent correction to equally spaced resonances.

Fix \(B>0\), \(\ell>0\), and \(B\ell<1\). For \(L>\ell/2\), define
\[
I=[-\ell/2,\ell/2],\qquad E_L=(I-L)\cup(I+L),\qquad k_B(t)=\frac{\sin(\pi Bt)}{\pi t},\quad k_B(0)=B.
\]
The positive compact concentration operator on \(L^2(E_L)\) has kernel \(k_B(x-y)\). Let \(A\) be its one-interval counterpart on \(L^2(I)\), let \(\lambda_0\) be the largest eigenvalue of \(A\), and let \(u\) be the positive, even, real, \(L^2(I)\)-normalized eigenfunction belonging to \(\lambda_0\). Put
\[
M=\int_Iu(t)\cos(\pi Bt)\,dt,\qquad
M_1=\int_I t u(t)\sin(\pi Bt)\,dt.
\]
Both \(M\) and \(M_1\) are strictly positive. For all sufficiently large integers \(n\) there is a unique \(L_n\) in
\[
\left[\frac{n}{2B}-\frac{1}{8B},\frac{n}{2B}+\frac{1}{8B}\right]
\]
such that the largest eigenvalue of the full two-interval operator has **exact multiplicity two**, with one even and one odd real eigenfunction. At that point the respective parity eigenvalue branches cross transversely. Furthermore,
\[
\boxed{\displaystyle L_n=\frac{n}{2B}+\frac{M_1}{\pi M n}+O(n^{-2}).}
\]
Writing \(\lambda_+(L)\) and \(\lambda_-(L)\) for the respective top parity branches and \(\Delta(L)=\lambda_+(L)-\lambda_-(L)\), the stronger expansion is
\[
\Delta(L)=\frac{M^2}{\pi L}\sin(2\pi BL)-\frac{MM_1}{\pi L^2}\cos(2\pi BL)+O(L^{-3}),\qquad L\to\infty.
\]
The error constants may depend on the fixed \(B\) and \(\ell\). The displayed location formula applies to the **half-distance** \(L\) between the interval centers, not their full center-to-center distance.

## Assumptions and scope

The frequency-space Fourier projection is normalized with \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\), so that its restriction to \([-B/2,B/2]\) has the kernel \(k_B(x-y)\). The spatial set is the union of **two equal intervals** centered at \(\pm L\). The strict inequality \(B\ell<1\) ensures strict positivity of \(k_B(t-s)\) for all \(t,s\in I\); it is sufficient rather than claimed optimal. No assertion is made for unequal components, arbitrary bands, or all finite separations.

## Proof

**1. Single-interval principal mode.** The kernel \(k_B(t-s)\) is real, continuous, and strictly positive for all \(t,s\in I\), since \(B\ell<1\). Thus the compact positivity-improving integral operator \(A\) has a simple largest eigenvalue \(\lambda_0>0\), an everywhere positive continuous eigenfunction \(u\), and a strict gap \(\gamma=\lambda_0-\lambda_1>0\) to the rest of its spectrum. Reflection symmetry makes \(u\) even. On \(I\), \(\cos(\pi Bt)>0\), and \(t\sin(\pi Bt)\) is positive except at \(t=0\); hence \(M>0\) and \(M_1>0\).

**2. Exact parity reduction.** Identify the two components with two copies of \(L^2(I)\), reflecting the left component's local coordinate. The operator becomes
\[
\begin{pmatrix}A&C_L\\ C_L&A\end{pmatrix},\qquad
(C_Lf)(t)=\int_I k_B(2L+t+s)f(s)\,ds.
\]
The even and odd spaces therefore carry exactly \(A+C_L\) and \(A-C_L\), respectively. The kernel is symmetric, so \(C_L\) is self-adjoint. Uniformly for \(t,s\in I\), \(k_B(2L+t+s)=O(L^{-1})\), and hence \(\|C_L\|=O(L^{-1})\). In particular, for sufficiently large \(L\), both parity operators have isolated simple leading eigenvalues \(\lambda_+(L)\) and \(\lambda_-(L)\) near \(\lambda_0\), separated from all remaining eigenvalues by at least \(\gamma/2\). They are the two largest full-operator eigenvalues, possibly tied.

**3. Odd-order splitting.** Standard simple-eigenvalue resolvent perturbation, uniform in sufficiently small self-adjoint \(C\), gives
\[
\lambda_{\mathrm{top}}(A+C)=\lambda_0+\langle u,Cu\rangle+q_2(C)+O(\|C\|^3),
\]
where \(q_2(C)=\langle Cu,(\lambda_0-A)^{-1}_{u^\perp}Cu\rangle\) is homogeneous quadratic in \(C\). Subtracting the corresponding expansion for \(A-C\) cancels the even-order term:
\[
\Delta(L)=2\langle u,C_Lu\rangle+O(L^{-3}).
\]
The same analytic perturbation argument differentiates in \(L\), giving \(\Delta'(L)=2\frac{d}{dL}\langle u,C_Lu\rangle+O(L^{-3})\), because \(\|C_L'\|=O(L^{-1})\).

**4. Moment expansion with constants.** Let \(\theta=2\pi BL\) and \(z=t+s\). Since \(|z|\le\ell\), uniformly
\[
\frac{1}{\pi(2L+z)}=\frac1{2\pi L}-\frac{z}{4\pi L^2}+O(L^{-3}).
\]
Use \(\sin(\theta+\pi Bz)=\sin\theta\cos(\pi Bz)+\cos\theta\sin(\pi Bz)\) and the evenness of \(u\). The double integral of \(u(t)u(s)\cos(\pi B(t+s))\) is \(M^2\); that of \(u(t)u(s)\sin(\pi B(t+s))\) vanishes. The double integral of \((t+s)u(t)u(s)\sin(\pi B(t+s))\) equals \(2MM_1\); the corresponding cosine integral vanishes. Consequently,
\[
2\langle u,C_Lu\rangle=
\frac{M^2}{\pi L}\sin\theta-\frac{MM_1}{\pi L^2}\cos\theta+O(L^{-3}).
\]
Differentiating the uniform kernel Taylor expansion and the perturbation remainder also yields
\[
\Delta'(L)=\frac{2BM^2}{L}\cos(2\pi BL)+O(L^{-2}).
\]

**5. Infinite exact crossings.** Let \(J_n=[n/(2B)-1/(8B),n/(2B)+1/(8B)]\). At its endpoints, the leading sine term of \(\Delta\) has opposite signs, of magnitude \(M^2/(\sqrt2\pi L)\). For sufficiently large \(n\), the lower-order errors cannot change those signs, so continuity gives a zero \(L_n\). On \(J_n\), the cosine has constant sign \((-1)^n\) and magnitude at least \(1/\sqrt2\). Thus the displayed derivative expansion makes \(\Delta\) strictly monotone throughout \(J_n\): the root is unique and transverse. The other parity-sector eigenvalues remain at least \(\gamma/2\) below the two near \(\lambda_0\), so the resulting top eigenspace has exact dimension two. Its parity branches exchange order across each crossing.

Finally, set \(L_n=n/(2B)+\delta_n\). The gap expansion first gives \(\delta_n=O(n^{-1})\); substituting \(\sin(2\pi BL_n)=(-1)^n[2\pi B\delta_n+O(n^{-3})]\) and \(\cos(2\pi BL_n)=(-1)^n[1+O(n^{-2})]\) gives
\[
\delta_n=\frac{M_1}{2\pi BM L_n}+O(n^{-2})=\frac{M_1}{\pi M n}+O(n^{-2}),
\]
which completes the proof.

## Verification

The proof of infinitely many exact crossings is analytic; numerical quadrature is only a supplementary consistency check. The included `numerical_check.py` uses Gauss–Legendre Nyström discretization, a finite symmetric eigenproblem, and bracketed root finding for \(B=1\), \(\ell=0.8\). With 64 quadrature nodes, approximate roots at \(n=10,20,40,80\) differ from the two-term prediction by about \(5.27\cdot10^{-6},6.59\cdot10^{-7},8.24\cdot10^{-8},1.03\cdot10^{-8}\), respectively. These data are not claimed as rigorous enclosures or an infinite-dimensional certificate.

## Relationship to prior work

Degeneracies of **bandpass prolate** integral operators were known already in the classical work of Morrison (1963, 1965); Fourier duality makes this a genuinely relevant antecedent to the two-spatial-window problem. The claim here is the **large-separation resonance sequence for the largest** concentration eigenvalue and its explicit positive moment-dependent \(n^{-1}\) displacement, rather than the first observation that bandpass degeneracies can occur. SenGupta and collaborators (2012) establish operator properties and convergent numerical methods for disconnected frequency bands. Hogan and Lakey (2017) develop bandpass-prolate numerical approximations, include a parity decomposition, and discuss known degeneracies, but their inspected formulae do not imply the displayed asymptotic crossing locations. Fahs and Krasovsky (arXiv:2003.08136, initial public posting 18 March 2020) study the two-interval sine-kernel **Fredholm determinant** in a different large-bandwidth regime, not the fixed-bandwidth dominant-eigenvalue parity crossings proved here.

## Limitations

The theorem requires two symmetric equal intervals with \(B\ell<1\). The number \(N\) beyond which every asserted crossing exists is not optimized or explicitly computed, and no claim is made that these are all crossings outside the specified windows. Prior work establishes the general **possibility** of spectral degeneracy. Full text of Morrison's 1963 and 1965 articles was not accessible in this examination, so historical priority for more detailed quantitative separation claims remains a material uncertainty; the accessible abstract, 1962 announcement, and later papers referring to Morrison were considered. No independence or external validation is claimed.

## References

1. J. A. Morrison, *On the eigenfunctions corresponding to the bandpass kernel, in the case of degeneracy*, Quart. Appl. Math. 21 (1963), 13–19. DOI: 10.1090/qam/145306.
2. J. A. Morrison, *Dual Formulation for the Eigenfunctions Corresponding to the Bandpass Kernel, in the Case of Degeneracy*, J. Math. Phys. 44 (1965), 313–326. DOI: 10.1002/sapm1965441313.
3. I. SenGupta, B. Sun, W. Jiang, G. Chen, M. C. Mariani, *Concentration Problems for Bandpass Filters in Communication Theory over Disjoint Frequency Intervals and Numerical Solutions*, J. Fourier Anal. Appl. 18 (2012), 182–210. DOI: 10.1007/s00041-011-9197-y.
4. J. A. Hogan and J. D. Lakey, *On the Numerical Evaluation of Bandpass Prolates II*, J. Fourier Anal. Appl. 23 (2017), 35–57. DOI: 10.1007/s00041-016-9465-y.
5. B. Fahs and I. Krasovsky, *Sine-kernel determinant on two large intervals*, arXiv:2003.08136 (first posted 18 March 2020); later Comm. Pure Appl. Math. 77 (2024), 1958–2029.
