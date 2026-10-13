# Exact positive flat bands from a coupling-tuned resonance in ring chains

## Finding
For the periodic chain of rings with interpolating circulant vertex conditions, an exact coupling-resonance criterion supplements the familiar edge-commensurability mechanism. At the Kirchhoff endpoint \(\gamma=0\), for all strictly positive edge lengths \(l_1,l_2,l_3\) with \(l_2+l_3=2\pi\), all coupling lengths \(\ell>0\), and each interior interpolation \(t\in(0,1)\), the complete positive flat-band/point spectrum is
\[
\sigma_{\mathrm{pp}}(H_{0,t})\cap(0,\infty)
=\bigl\{m^2:m\in\mathbb N_{\ge1},\ \sin(ml_1)\sin(ml_3)=0\ \text{or}\ 3m^2\ell^2\tan^2(\pi t/6)=1\bigr\}.
\]
The second alternative is independent of the edge lengths. In particular, if \(l_1/\pi\) and \(l_3/\pi\) are irrational, at most one positive flat band survives for fixed parameters; it occurs precisely if \(\cot(\pi t/6)/(\sqrt3\ell)\) is a positive integer.

## Assumptions and scope
The operator acts as \(-\mathrm d^2/\mathrm dx^2\) on the edges of the two-vertex periodic ring-chain cell defined in [1, Section 2]. All three edge lengths are positive, with the ring perimeter normalized to \(2\pi\). At every degree-three vertex, with ordered boundary values and outward derivatives, the self-adjoint condition is \((U(t)-I)\Psi+i\ell(U(t)+I)\Psi'=0\). The circulant \(U(t)\) has Fourier eigenvalues \(1,-\exp(-i\pi t/3),-\exp(i\pi t/3)\); this is [1, Eqs. (2.1)–(2.5)] with \(\gamma=0\). Here \(0<t<1\), \(\ell>0\), and the angular Bloch parameter runs through \((-\pi,\pi]\). Only strictly positive energies are classified. We do not assert anything about negative or zero point spectrum, spectral multiplicity, or the non-flat band locations.

## Proof
Let \(k>0\), set \(c=\cos(\pi t/3)\), so \(1/2<c<1\), and use the original *un-divided* fiber secular equation [1, Eq. (2.10)]
\[
0=k^6P_6+k^4P_4+k^2P_2+k^2\bigl(P_s\sin\theta+P_c\cos\theta\bigr),
\]
because \(P_5=P_3=P_1=P_0=0\) at \(\gamma=0\). Section 4 of [1] gives the Bloch coefficients
\[
\begin{aligned}
P_c&=-16\ell^2(c+1)\,[3k^2\ell^2(c-1)-(c+1)]\,[\sin(kl_2)+\sin(kl_3)],\\
P_s&=32k\ell^3\sqrt3\,\sin(\pi t/3)(c+1)\,[\cos(kl_3)-\cos(kl_2)].
\end{aligned}
\]
All prefactors outside the final brackets are nonzero: in particular \(3k^2\ell^2(c-1)-(c+1)<0\). The equality of a fiber eigenvalue for a positive-measure set of Bloch phases forces both sinusoidal coefficients and the constant coefficient to vanish. Since \(l_2+l_3=2\pi\),
\[
\begin{aligned}
\sin(kl_2)+\sin(kl_3)&=2\sin(\pi k)\cos(k(\pi-l_3)),\\
\cos(kl_3)-\cos(kl_2)&=-2\sin(\pi k)\sin(k(l_3-\pi)).
\end{aligned}
\]
The simultaneous vanishing is equivalent to \(\sin(\pi k)=0\), since the two phase factors cannot vanish simultaneously. Consequently every positive flat-band momentum is \(k=m\in\mathbb N_{\ge1}\).

At such \(m\), write \(S_m=\sin(ml_1)\sin^2(ml_3)\). The trigonometric identities \(\sin(ml_2)=-\sin(ml_3)\) and
\[
\sin(m(l_1+l_2-l_3))
+\sin(m(l_2+l_3-l_1))
+\sin(m(l_3+l_1-l_2))
=\sin(ml_1)\bigl[1-4\sin^2(ml_3)\bigr]
\]
reduce [1, Section 4, Eqs. for \(P_6,P_4,P_2\)] to
\[
P_6=-72\ell^6(c-1)^2S_m,\qquad
P_4=-48\ell^4(c^2-1)S_m,\qquad
P_2=-8\ell^2(c+1)^2S_m.
\]
The constant coefficient therefore factors *exactly* as
\[
\begin{aligned}
m^6P_6+m^4P_4+m^2P_2
&=-8m^2\ell^2S_m\left[3m^2\ell^2(c-1)+(c+1)\right]^2.
\end{aligned}
\]
Since \(m,\ell>0\), this vanishes precisely if \(\sin(ml_1)\sin(ml_3)=0\), or if
\[
3m^2\ell^2\frac{1-c}{1+c}=1.
\]
The half-angle identity \((1-c)/(1+c)=\tan^2(\pi t/6)\) gives the asserted condition. All steps are reversible, and these zeros solve the actual fiber matching determinant for **every** Bloch phase. By Floquet decomposition, the resulting constant fiber branch is a flat band and gives infinite-multiplicity point spectrum; conversely, a point eigenvalue of the direct integral must be a fiber eigenvalue on a set of Bloch phases of positive measure, which the trigonometric secular equation permits only in the classified cases.

For irrational \(l_1/\pi\) and \(l_3/\pi\), the sine alternative never holds at a positive integer; the resonance condition determines at most one positive integer \(m\). Solving it for \(t\) gives \(t_m=(6/\pi)\arctan(1/(\sqrt3m\ell))\). It is an interior parameter exactly when \(m\ell>1\). For a concrete incommensurate example take \(l_1=\sqrt2\), \(l_3=\sqrt3\), \(l_2=2\pi-\sqrt3\), \(\ell=1\), \(m=2\), and \(t=(6/\pi)\arctan(1/(2\sqrt3))\); then \(E=4\) is a flat-band energy even though \(1,l_1/\pi,l_3/\pi\) are rationally independent.

## Verification
Execute `python3 verify.py` (standard-library Python 3). The checker compares the multivariate polynomial coefficients of the secular constant term with the claimed perfect-square factorization **exactly**, checks the trigonometric reduction and parameter inequality at sample values, and separately assembles the six-equation Floquet matching determinant for a distinct irrational-length tuned example to test representative phases. The sample floating-point checks are *not* proofs of universal assertions; the preceding algebra and analytic Floquet argument are the proof. The direct determinant test uses \(m=1\), \(t=1/2\), \(l_1=\sqrt2\), \(l_3=\sqrt3\), and \(\ell=\cot(\pi/12)/\sqrt3\).

## Relationship to prior work
Exner and Pekař [1] derive the full dispersion equation and list the rational-edge-length construction as a sufficient flat-band mechanism in their section on interpolation from Kirchhoff conditions. The present argument uses their exact secular coefficients but solves the simultaneous Bloch-coefficient and constant-term zero conditions, revealing a tuned-coupling branch and giving an if-and-only-if classification of the *whole positive point spectrum* for this interior subfamily. Crucially, the predecessor [3, Section 2.1] **already proves the preferred-orientation endpoint resonance** \(m\ell=1\) at \(t=1\), including for irrational lengths. Our equation specializes to precisely that result at \(t=1\), but [2,3] do not treat the nontrivial interior family \(0<t<1\); the new result is an exact interpolation law and completeness classification, not discovery of the endpoint phenomenon. The result is therefore a refinement within an existing explicitly studied model, not a new derivation of that model's secular equation.

## Limitations
The theorem is restricted to \(\gamma=0\), \(0<t<1\), nondegenerate positive edges and positive energies. It does not imply that the flat band is spectrally isolated, nor determine its multiplicity beyond infinite degeneracy by translations. It does not classify the remaining absolutely continuous bands. The literature comparison used the complete 2024 arXiv text and available metadata for the 2024 journal article; an unnoticed equivalent claim in a weakly indexed source or an inaccessible journal-version change remains possible. 
## References
[1] P. Exner and J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, arXiv:2403.09457v1 (public 2024-03-14), Sections 2 and 4, Appendix A; *Journal of Mathematical Physics* **65** (2024), 092102, doi:10.1063/5.0208361.

[2] M. Baradaran, P. Exner, and M. Tater, *Ring chains with vertex coupling of a preferred orientation*, arXiv:1912.03667; *Reviews in Mathematical Physics* **33** (2021), 2060005.

[3] M. Baradaran, P. Exner, and M. Tater, *Spectrum of periodic chain graphs with time-reversal non-invariant vertex coupling*, arXiv:2012.14344; *Annals of Physics* **443** (2022), 168992.
