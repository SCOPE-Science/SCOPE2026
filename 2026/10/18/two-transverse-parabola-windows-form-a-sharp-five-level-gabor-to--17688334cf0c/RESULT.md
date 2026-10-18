# Two transverse parabola windows form a sharp five-level Gabor tomography frame

## Finding
For any odd prime power \(q\ge3\), the two normalized indicators of the transverse finite-field parabolas
\[
S_0=\{(t,t^2):t\in\mathbb F_q\},\qquad S_1=\{(t^2,t):t\in\mathbb F_q\}
\]
form an **informationally complete two-window Gabor intensity measurement** on the complex space of dimension \(q^2\). More strongly, the linear operator that measures arbitrary complex matrices against all the orbit projectors has an exactly five-level, nonzero singular spectrum. The eigenvalues of its Hilbert–Schmidt normal operator and their multiplicities are
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
1&2q^2(q-1)\\
2&q^2(q-1)^2\\
q&2(q-1)\\
2q&(q-1)^2\\
2q^2&1.
\end{array}
\]
Consequently, for every complex \(q^2\times q^2\) matrix \(X\),
\[
\|X\|_{\mathrm{HS}}^2\ \le\
\sum_{j=0}^1\sum_{x,\xi\in\mathbb F_q^2}
|\operatorname{tr}(X P_{j,x,\xi})|^2
\ \le\ 2q^2\|X\|_{\mathrm{HS}}^2.
\]
Both constants are attained by nonzero matrices. The operator's exact condition number is \(\sqrt2q\); its linear inversion determines every matrix, and in particular determines every vector from its two sets of squared short-time Fourier measurements up to an unavoidable global phase.

Each individual window has projector-span dimension \(q^4-q^3+q^2-q+1<q^4\). No single window supported on at most \(q\) group elements admits informationally complete **linear matrix** tomography. Thus two is the smallest possible number of windows with at most \(q\) nonzero samples each that permits linear tomography on \(\mathbb F_q^2\).

## Assumptions and scope
Let \(\mathbb F_q\) be the field of odd order \(q\) and \(\psi:\mathbb F_q\to\mathbb C\) a nontrivial additive character of unit modulus. Put \(G=\mathbb F_q^2\), \(N=q^2\), with counting-measure inner product on \(\mathbb C^G\). Fix the dot product \(\xi\cdot u=\xi_1u_1+\xi_2u_2\). Define \(g_j=q^{-1/2}\mathbf1_{S_j}\), hence \(\|g_j\|_2=1\). Translation and modulation act by
\[
(T_xf)(u)=f(u-x),\qquad(M_\xi f)(u)=\psi(\xi\cdot u)f(u),\qquad \pi(x,\xi)=M_\xi T_x.
\]
Define \(P_{j,x,\xi}=|\pi(x,\xi)g_j\rangle\langle\pi(x,\xi)g_j|\) and
\[
(\mathcal LX)_{j,x,\xi}=\operatorname{tr}(X P_{j,x,\xi}),
\quad \mathcal L:\mathbb C^{N\times N}\to\mathbb C^{2N^2}.
\]
The matrix space has the Hilbert–Schmidt inner product \(\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^*Y)\). The claim is about the linear measurement of **all complex matrices**, not the minimal number of generic intensity measurements or the possible existence of a one-window system recovering only rank-one projectors. Distinct integer powers of \(q\) used below are distinct for odd \(q\ge3\).

## Proof
**1. Diagonalization of the orbit-projector frame operator.** For \(s,\eta\in G\), let \(W_{s,\eta}=M_\eta T_s\). Weyl matrices obey
\[
\operatorname{tr}(W_{s,\eta}^*W_{t,\zeta})
=N\,\mathbf1_{s=t}\mathbf1_{\eta=\zeta}.
\]
Conjugating a Weyl matrix by \(\pi(x,\xi)\) multiplies it by a character of the \(N^2\)-element time-frequency group; these characters are mutually orthogonal. Put
\[
A_j(s,\eta)=\langle g_j,W_{s,\eta}g_j\rangle.
\]
For each \(j\), the absolute value of \(\operatorname{tr}(P_{j,x,\xi}W_{s,\eta})\) is \(|A_j(s,\eta)|\), independent of \(x,\xi\), and the corresponding phase is the character indexed by \((s,\eta)\). Orthogonality shows that \(W_{s,\eta}/\sqrt N\) is an eigenvector of \(\mathcal L^*\mathcal L\) with eigenvalue
\[
\lambda(s,\eta)=N\bigl(|A_0(s,\eta)|^2+|A_1(s,\eta)|^2\bigr).
\]
This standard Weyl/ambiguity-function reduction is used here only after explicitly evaluating both geometrically defined windows.

**2. Exact ambiguity of the first parabola.** Let \(s=(a,b)\). The intersection \(S_0\cap(S_0+s)\) consists of those \((t,t^2)\) for which \(b=2at-a^2\). Since the characteristic is odd, if \(a\ne0\) there is exactly one solution \(t=(b+a^2)/(2a)\), so \(|A_0(s,\eta)|=q^{-1}\) for every \(\eta\). If \(a=0\) and \(b\ne0\), there is no solution, so the ambiguity vanishes identically.

When \(s=0\), write \(\eta=(c,d)\); then
\[
A_0(0,(c,d))=q^{-1}\sum_{t\in\mathbb F_q}\psi(ct+dt^2).
\]
If \(c=d=0\), this is \(1\). If \(d=0,c\ne0\), character orthogonality gives zero. If \(d\ne0\), completing the square and expanding the square modulus yields \(\bigl|\sum_t\psi(dt^2+ct)\bigr|^2=q\), hence \(|A_0|^2=q^{-1}\). To see the latter equality without invoking an unproved Gauss-sum formula, change variables \(u=t-v\) in the squared modulus. The inner sum over \(v\) becomes \(\sum_v\psi(2duv)\), which is \(q\) for \(u=0\) and zero otherwise because \(2d\ne0\). Thus the squared modulus is exactly \(q\).

**3. The transverse partner and multiplicities.** Exchanging coordinates sends \(S_0\) to \(S_1\), so the previous description holds with \(a,b\) and \(c,d\) interchanged. If the time shift \(s=(a,b)\) has both entries nonzero, the two squared ambiguities are \(q^{-2}\), giving \(\lambda=2\) for \(q^2(q-1)^2\) Weyl labels. If exactly one of \(a,b\) is nonzero, exactly one squared ambiguity is \(q^{-2}\), giving \(\lambda=1\) with multiplicity \(2q^2(q-1)\).

For \(s=0\) and \(\eta=(c,d)\), both entries nonzero yield \(\lambda=2q\) on \((q-1)^2\) labels; exactly one nonzero entry yields \(\lambda=q\) on \(2(q-1)\) labels; the zero frequency yields \(\lambda=2q^2\) once. These cases partition all \(q^4=N^2\) Weyl labels, proving the full spectral classification. In particular every eigenvalue is positive and the sharp least and greatest eigenvalues are \(1\) and \(2q^2\).

**4. Single-window obstruction and rank.** The first window's ambiguity is nonzero precisely on \(q^2\cdot q(q-1)+q(q-1)+1=q^4-q^3+q^2-q+1\) Weyl labels; the same holds for the second. Therefore neither window alone gives full linear matrix recovery. More generally, if a single window \(g\) has support \(S\) of cardinality at most \(q\), then \(A_g(s,\eta)=0\) whenever \(s\notin S-S\). The difference set obeys
\[
|S-S|\le1+|S|(|S|-1)\le1+q(q-1)<q^2=|G|.
\]
There is consequently an entire nonzero Weyl sector invisible to all its orbit projectors. One such window cannot span the matrix space, while the constructed pair does. This proves the claimed minimal window count within the stated sparsity class.

## Verification
A standalone finite-field program computes both ambiguity functions directly over \(G\times G\), checks the full five-level eigenvalue distribution for \(q=3,5,7,9\), and compares the predicted spectrum with a separately assembled dense lifted-projector Gram matrix for \(q=3,5\). The code includes explicit \(\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1)\) arithmetic and uses only finite-field operations and character evaluations. The observed multiplicities agree exactly with the theorem in each tested field. The complex Gram diagonalization agrees numerically within \(10^{-7}\); this serves as a normalization check and not as the proof for general \(q\). Reproduce with `python checks/verify_two_parabola_gabor.py`; the saved console output is at `checks/verification_output.txt` (NumPy required for the two dense checks).

## Relationship to prior work
The Weyl-ambiguity diagonalization and the general use of nonvanishing ambiguity functions for finite Gabor phase retrieval are established background (Bojarovska–Flinth; Bartusel). These works do not provide the specific two transverse parabola windows or their five exact eigenvalue levels and sparsity-optimal two-window construction. Grohs–Liehr–Rathmair investigate multiple STFT windows for lattice recovery on the real line, with a different ambient group and sampling model. Iosevich and collaborators study finite-field graph supports in **vector** Gabor orthonormal bases, not operator-valued intensity tomography. Results for two-tap cyclic tomography or single windows supported on hyperbolic shells concern different support regimes. The distinguishing assertion here is the simultaneous combination of explicit \(q\)-sparse supports on \(\mathbb F_q^2\), complete matrix recovery, exact conditioning and a minimal number of windows under this support cap.

## Limitations
The lower-bound obstruction is only for **linear informational completeness for all matrices** from one window with at most \(q\) support points. It does not rule out single-window recovery restricted to rank-one projectors, nor does it establish the least total support size or optimal conditioning among all two-window designs. The formula uses odd characteristic; characteristic two is excluded because the parabola difference map is not injective in its leading coordinate. The Weyl spectral argument is an ordinary finite-dimensional proof, with finite numerical checks supplied for reproducibility rather than as an infinite-field certificate. Priority remains subject to independent literature verification.

## References
1. R. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), Sections 2–3. https://arxiv.org/abs/1503.05800
2. D. Bartusel, *Injectivity conditions for STFT phase retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729v1 (June 14, 2022), Sections 2 and 4. https://arxiv.org/html/2206.06729v1
3. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620v1 (July 21, 2022). https://arxiv.org/abs/2207.10620
4. A. Iosevich and collaborators, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120 (2017). https://arxiv.org/abs/1712.09120
5. H. Führ and V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654 (2022). https://arxiv.org/abs/2201.08654
