# A sharp one-quarter law for nonreal sketched Ritz pairs

## Finding

Let a real symmetric positive-definite matrix be compressed to a two-dimensional orthonormal trial space, and suppose the out-of-space residual has rank one. If the sketch is exactly isometric on the trial space and its coupling to the residual direction has fixed magnitude but a uniformly random direction in the trial plane, the sketched Rayleigh–Ritz matrix has a nonreal conjugate eigenvalue pair with probability **at most \(1/4\)**. This is a sharp, attained bound, not a large-dimensional limit.

If the two standard Ritz values are separated by \(\Delta>0\), the residual norm is \(\rho>0\), and the sketch cross-coupling length is \(\tau>0\), define \(t=\rho\tau/\Delta\). In the balanced-residual configuration, the exact nonreal probability is

\[
P(t)=\begin{cases}
0,&0<t\le1/2,\\
\displaystyle\frac{1}{\pi}\arccos\!\left(\frac{\sqrt{t^2+2}-1}{t}\right),&t>1/2.
\end{cases}
\]

It has the unique maximum \(P(\sqrt2)=1/4\), decreases back to zero as \(t\to\infty\), and exhibits the sharp onset \(t=1/2\). Moreover, a three-dimensional positive-definite example attains probability \(1/4\) while the sketch is an arbitrarily accurate **whole-space** subspace embedding and remains exactly isometric on the trial plane. The matrix instance varies as the distortion tends to zero; no fixed-gap impossibility is claimed.

## Assumptions and scope

Take any \(m\ge3\), symmetric \(A\in\mathbb R^{m\times m}\), and \(U\in\mathbb R^{m\times2}\) with \(U^{\mathsf T}U=I_2\). Assume that the two eigenvalues of \(K=U^{\mathsf T}AU\) are distinct, \(\lambda_1<\lambda_2\), and that the orthogonal residual has rank one:

\[
(I-UU^{\mathsf T})AU=nr^{\mathsf T},\qquad
\|n\|_2=1,\quad U^{\mathsf T}n=0,\quad r\in\mathbb R^2.
\]

Rotate the columns of \(U\) so that \(K=\operatorname{diag}(\lambda_1,\lambda_2)\); this does not change the trial space. Write \(\rho=\|r\|_2\) and \(\Delta=\lambda_2-\lambda_1\). If \(\rho=0\), the trial space is invariant and all sketched Ritz values are real. For \(\rho>0\), consider sketches \(S\) for which

\[
U^{\mathsf T}S^{\mathsf T}SU=I_2,\qquad
U^{\mathsf T}S^{\mathsf T}Sn=g,
\quad g=\tau(\cos\phi,\sin\phi)^{\mathsf T},
\quad \phi\sim\operatorname{Uniform}[0,2\pi).
\]

This is an explicit *circular cross-coupling sketch ensemble*, not a claim about generic Gaussian, CountSketch, or Fourier sketches. It is realizable: for any prescribed \(g\), take the Gram operator on \(\operatorname{span}\{U,n\}\) to be

\[
G=\begin{pmatrix}I_2&g\\g^{\mathsf T}&1+\tau^2\end{pmatrix},
\]

which is positive definite by its Schur complement; extend by the identity on the orthogonal complement and set \(S=G^{1/2}\). If \(\tau<1\), the bottom-right entry may instead be \(1\); that alternative Gram operator has eigenvalues \(1-\tau,1,1+\tau\) on this three-dimensional span. In the latter construction, \(S\) preserves all squared norms to relative error at most \(\tau\).

The sketched projected matrix is defined exactly as in sketched Rayleigh–Ritz, \(H=(SU)^{\mathsf T}(SAU)\). The event studied is that **both eigenvalues of the real \(2\times2\) matrix \(H\) are nonreal**; a repeated real eigenvalue at the discriminant boundary is not counted.

## Proof

**Reduction.** Since \(AU=UK+nr^{\mathsf T}\) and \((SU)^{\mathsf T}SU=I_2\),

\[
H=K+gr^{\mathsf T}
=\begin{pmatrix}
\lambda_1+g_1r_1&g_1r_2\\
g_2r_1&\lambda_2+g_2r_2
\end{pmatrix}.
\]

Its characteristic discriminant is

\[
\mathcal D=
(\Delta-g_1r_1+g_2r_2)^2+4g_1g_2r_1r_2
=\Delta^2+(g^{\mathsf T}r)^2-2\Delta(g_1r_1-g_2r_2).
\]

The eigenvalues are nonreal if and only if \(\mathcal D<0\). Independent sign changes of the two Ritz-basis vectors leave the distribution of the isotropic \(g\) unchanged, so we may assume \(r_1,r_2\ge0\). If either is zero, \(H\) is triangular and no nonreal pair is possible. Otherwise \(r_1,r_2>0\). If \(g_1g_2\ge0\), the first discriminant expression is nonnegative. If \(g_1<0<g_2\), put \(a=-g_1r_1>0\), \(b=g_2r_2>0\) to obtain

\[
\mathcal D=(\Delta+a+b)^2-4ab
=\Delta^2+2\Delta(a+b)+(a-b)^2>0.
\]

Thus a nonreal pair is possible only for \(g_1>0>g_2\), one of the four equal angular quadrants. This proves the universal probability bound \(\Pr(\mathcal D<0)\le1/4\). It depends on isotropic orientation, not on independence of sketch entries.

**Balanced-residual probability.** Take \(r=(\rho/\sqrt2)(1,1)^{\mathsf T}\) and \(g=\tau(\cos\phi,\sin\phi)^{\mathsf T}\). With \(\psi=\phi+\pi/4\) and \(t=\rho\tau/\Delta\), the preceding discriminant becomes

\[
\frac{\mathcal D}{\Delta^2}=1+t^2\sin^2\psi-2t\cos\psi.
\]

Set \(y=\cos\psi\in[-1,1]\). The inequality \(\mathcal D<0\) is

\[
t^2y^2+2ty-(1+t^2)>0,
\]

or, using its two explicit roots,

\[
y>h(t):=\frac{\sqrt{t^2+2}-1}{t};
\]

the other root is less than \(-1\) and is irrelevant. For \(t\le1/2\), \(h(t)\ge1\), so the probability is zero. For \(t>1/2\), uniformity of \(\psi\) yields the displayed \(P(t)=\arccos(h(t))/\pi\). Direct differentiation gives

\[
h'(t)=\frac{1-2/\sqrt{t^2+2}}{t^2}.
\]

Consequently \(h\) decreases until \(t=\sqrt2\) and increases thereafter. Since \(h(\sqrt2)=1/\sqrt2\), the unique maximum of \(P\) is exactly \(1/4\); also \(h(t)\to1\) as \(t\to\infty\), giving \(P(t)\to0\). At the maximum, \(\mathcal D<0\) precisely for \(-\pi/2<\phi<0\), apart from the zero-measure boundaries. This attains the universal bound.

**Sharp gap–residual onset.** By Cauchy–Schwarz, \(g_1r_1-g_2r_2\le\tau\rho\), whence

\[
\mathcal D\ge\Delta^2-2\Delta\tau\rho.
\]

Therefore all orientations give real eigenvalues when \(\tau\rho\le\Delta/2\). Conversely, for the balanced residual choose \(g=(\tau/\sqrt2)(1,-1)^{\mathsf T}\), giving \(g^{\mathsf T}r=0\) and \(\mathcal D=\Delta^2-2\Delta\tau\rho<0\) whenever \(\tau\rho>\Delta/2\). This threshold is exact over the admissible residual/sketch orientations. The sufficiency is consistent with elementary symmetric-matrix perturbation bounds; the angular probability and its sharp universal value are the additional quantitative content.

**Arbitrarily small embedding distortion.** For each \(0<\delta<1/\sqrt2\), put

\[
A_\delta=
\begin{pmatrix}
1&0&1/\sqrt2\\
0&1+\delta&1/\sqrt2\\
1/\sqrt2&1/\sqrt2&2
\end{pmatrix},\qquad U=[e_1\ e_2],\qquad n=e_3.
\]

Its leading principal minors are \(1\), \(1+\delta\), and \((2+3\delta)/2\), all strictly positive, so \(A_\delta\) is positive definite. Its Ritz gap is \(\Delta=\delta\), and its residual vector is \(r=(1,1)^{\mathsf T}/\sqrt2\), with \(\rho=1\). Draw \(\phi\) uniformly, take \(g=\sqrt2\delta(\cos\phi,\sin\phi)^{\mathsf T}\), and form

\[
G_\phi=\begin{pmatrix}1&0&g_1\\0&1&g_2\\g_1&g_2&1\end{pmatrix},
\qquad S_\phi=G_\phi^{1/2}.
\]

Because \(\sqrt2\delta<1\), the eigenvalues of \(G_\phi\) are \(1-\sqrt2\delta,1,1+\sqrt2\delta\), independently of phase. Hence \(S_\phi\) is a whole-space \(\sqrt2\delta\)-subspace embedding and is an exact isometry on the trial plane. Yet \(t=\sqrt2\), so its sketched projected matrix has a conjugate pair with probability exactly \(1/4\). For any target distortion \(0<\varepsilon<1\), choose \(\delta<\varepsilon/\sqrt2\). This establishes the stated sharp worst-case near-isometry phenomenon.

## Verification

Execute `python verify.py` with Python 3 and SymPy. The standalone checker verifies the discriminant identity and probability-profile derivative symbolically, proves the stated SPD determinant identity symbolically, tests 4,800 exact-rational nonsymmetric compression instances against the necessary quadrant condition, and compares 100,000 seeded uniform phases with the exact probability \(1/4\). The recorded deterministic run reported `PASS` with sample frequency `0.249330`. The exact probability and the all-parameter assertions follow from the proof above, not from sampling.

## Relationship to prior work

Liu and Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices* (arXiv:2610.22261v1, first public October 15, 2026), define \(H=(SU)^{\mathsf T}(SAU)\) for a sketch-orthonormal basis and explain the need for real Schur extraction because nonsymmetric projected matrices can have nonreal eigenpairs. Their discussed results concern real-arithmetic implementation and local subspace accuracy. The present theorem instead gives a sharp **probability over isotropic cross-coupling directions**, a dimension-three attaining construction, and a near-isometry limit. In particular, it does not claim that the basic possibility of complex sketched Ritz eigenvalues is new.

Nakatsukasa and Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. 45 (2024), §6.8, already observe that sRR may return nonreal eigenvalue estimates for symmetric matrices and discuss small nonsymmetric perturbations. That observation and classical spectral-gap perturbation estimates cover the broad mechanism, but not the explicit angular one-quarter law of this particular ensemble. Shao's *Stabilizing the Rayleigh–Ritz procedure by randomization* (arXiv:2604.01037v1) studies a different randomized extraction design and asymptotic target-eigenpair convergence.

## Limitations

The upper bound assumes exactly two trial Ritz values, a rank-one orthogonal residual, **uniform angular orientation with fixed coupling length**, and exact arithmetic. It is not a failure-probability guarantee for independently distributed Gaussian or structured fast sketches, and it does not concern higher-dimensional projected spectra or convergence of an iterative eigensolver. The sharp examples are constructed sketch distributions rather than standard implementation draws. An earlier equivalent specialized two-dimensional random perturbation calculation may exist; full historical priority is not established. Some sections of the motivating 2026 manuscript were not accessible for complete line-by-line comparison.

## References

1. Jingyu Liu and Yuqi Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1 (October 15, 2026), https://arxiv.org/abs/2610.22261 and https://arxiv.org/html/2610.22261.
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183–1214, §6.8; https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf; earlier public preprint arXiv:2111.00113.
3. Nian Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1 (April 1, 2026), https://arxiv.org/abs/2604.01037.
