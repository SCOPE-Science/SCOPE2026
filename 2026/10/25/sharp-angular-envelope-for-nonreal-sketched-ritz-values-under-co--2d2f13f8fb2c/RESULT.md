# Sharp angular envelope for nonreal sketched Ritz values under codimension-one coordinate sampling

## Finding
Let \(s\geq 2\), let \(S=[I_s\;0]\in\mathbb R^{s\times(s+1)}\), and let \(Q\in\mathbb R^{(s+1)\times2}\) have orthonormal columns such that \(SQ\) has full column rank. Because the trial plane has codimension-one observation, the two singular values of \(SQ\) are \(1\) and \(\gamma\), with \(0<\gamma\leq1\). Let \(A=A^{\mathsf T}\) satisfy \(0<mI\preceq A\preceq LI\), with \(m<L\), and form the two-dimensional sketched Rayleigh–Ritz matrix
\[
H=(SQ)^\dagger SAQ.
\]
Then every eigenvalue \(\lambda\in\mathbb C\) of \(H\) obeys the **sharp envelope**
\[
\boxed{\lvert\operatorname{Im}\lambda\rvert\leq
\frac{L-m}{2}\sqrt{\frac{\gamma^{-1}-1}{2}}.}
\]
For each \(s\geq2\), \(m<L\), and \(0<\gamma<1\), equality is realized by a real symmetric positive-definite \(A\) having extreme eigenvalues exactly \(m,L\). Its sketched Ritz matrix has a nonreal conjugate pair. For \(\gamma=1\), the sketched Ritz matrix is symmetric and its eigenvalues are real. In particular, no strictly positive observation-angle tolerance below complete containment can universally prevent nonreal sketched Ritz values, even for an arbitrarily small positive spectral width.

## Assumptions and scope
All matrices, subspaces and computations are real and in exact arithmetic. The sketch \(S\) orthogonally observes exactly \(s\) of \(s+1\) coordinates, without row rescaling, and the trial space has dimension exactly two. The nontrivial principal angle \(\theta\in[0,\pi/2)\) between the trial space and the observed hyperplane satisfies \(\gamma=\cos\theta\). Thus the envelope may also be written
\[
\frac{L-m}{2}\sqrt{\frac{\sec\theta-1}{2}}.
\]
The full-column-rank condition is necessary for this definition of the two-dimensional least-squares sketch to have its stated similarity-invariance. The bounds \(m,L\) may be spectral enclosures; equality sharpness uses the actual endpoint eigenvalues. This is not a claim about general random sketches, general trial dimensions or floating-point errors.

## Proof
**1. Orthogonal normal form.** Denote the observed coordinate hyperplane by \(W\). Since the two-dimensional trial plane \(V=\operatorname{range}(Q)\) lies in \(\mathbb R^{s+1}\), the intersection \(V\cap W\) has dimension at least one. Use an orthogonal basis of the trial plane and an orthogonal change of coordinates within \(W\) to represent its columns as
\[
q_1=\gamma e_1+\sqrt{1-\gamma^2}\,e_{s+1},\qquad q_2=e_2.
\]
These changes do not alter the eigenvalues of \((SQ)^\dagger SAQ\): an orthogonal trial-basis change is an orthogonal similarity and a rotation of observed coordinates cancels in the pseudoinverse. Define
\[
q_3=-\sqrt{1-\gamma^2}\,e_1+\gamma e_{s+1},\qquad
 t=\frac{\sqrt{1-\gamma^2}}{\gamma}.
\]
Then \(q_1,q_2,q_3\) are orthonormal, \(e_1=\gamma q_1-\sqrt{1-\gamma^2}\,q_3\), and the nonzero first two rows of \(SQ\) form \(\operatorname{diag}(\gamma,1)\). Extra observed rows are zero.

**2. Contractive reduction.** Put \(c=(L+m)/2\), \(d=(L-m)/2>0\), and \(B=(A-cI)/d\). Then \(B=B^{\mathsf T}\) and \(\lVert B\rVert_2\leq1\). Define five real entries
\[
a=q_1^{\mathsf T}Bq_1,\quad b=q_1^{\mathsf T}Bq_2,\quad
\nu=q_1^{\mathsf T}Bq_3,\quad v=q_2^{\mathsf T}Bq_3,\quad k=q_2^{\mathsf T}Bq_2.
\]
A direct computation using the two sampled rows yields
\[
H=cI+d\begin{pmatrix}a-t\nu&b-tv\\b&k\end{pmatrix}.
\]
Its characteristic discriminant shows that, for any nonreal eigenvalue,
\[
\left(\frac{\operatorname{Im}\lambda}{d}\right)^2
=t bv-b^2-\frac{(a-k-t\nu)^2}{4}
\leq tbv-b^2.
\]
If both eigenvalues are real, the required inequality is automatic.

**3. Exact angular maximization.** From \(\lVert Bq_2\rVert_2\leq1\), orthogonality gives \(b^2+v^2\leq1\). The quadratic form \(t bv-b^2\) on the unit disk is maximized by the top eigenvalue of
\[
\begin{pmatrix}-1&t/2\\t/2&0\end{pmatrix},
\]
which is
\[
\frac{\sqrt{1+t^2}-1}{2}=
\frac{\gamma^{-1}-1}{2}.
\]
Multiplication by \(d\) proves the claimed envelope for both members of a possible conjugate pair.

**4. Attainment for every nonzero angle.** Fix \(0<\gamma<1\) and set
\[
 b_*=\sqrt{\frac{1-\gamma}{2}},\qquad
 v_*=\sqrt{\frac{1+\gamma}{2}},\qquad
 h=b_*q_1+v_*q_3.
\]
Let \(B=q_2h^{\mathsf T}+hq_2^{\mathsf T}\), setting its action to zero on the orthogonal complement of \(\operatorname{span}\{q_1,q_2,q_3\}\), and let \(A=cI+dB\). Since \(q_2\perp h\) and \(\lVert h\rVert_2=1\), the eigenvalues of \(B\) are \(-1,0,1\) together with zeros; hence \(A\) is positive definite and has extreme eigenvalues exactly \(m,L\). Here \(a=k=\nu=0\), \(b=b_*\), \(v=v_*\), and \(tv_*-b_*=b_*/\gamma\), so
\[
H=cI+d\begin{pmatrix}0&-b_*/\gamma\\b_*&0\end{pmatrix}.
\]
Its eigenvalues are
\[
c\pm i d\sqrt{\frac{\gamma^{-1}-1}{2}},
\]
which attain the envelope. At \(\gamma=1\), \(V\subseteq W\) and \((SQ)^\dagger SAQ=Q^{\mathsf T}AQ\), which is real symmetric.

## Verification
An exact rational three-dimensional witness takes
\[
S=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},\quad
Q=\begin{pmatrix}3/5&0\\0&1\\4/5&0\end{pmatrix},\quad
A=\begin{pmatrix}6&-1&0\\-1&6&2\\0&2&6\end{pmatrix}.
\]
The eigenvalues of \(A\) are \(6-\sqrt5,6,6+\sqrt5\), while
\[
(SQ)^\dagger SAQ=\begin{pmatrix}6&-5/3\\1&6\end{pmatrix}
\]
has eigenvalues \(6\pm i\sqrt{5/3}\), achieving equality for \(\gamma=3/5\).

Run `python3 verify.py` beside this document for the exact rational identities, seven independently constructed sharpness instances, and 2,048 bounded-norm symmetric tests. Random tests confirm only sampled finite instances and are not the proof of the universal claim; the preceding argument is the proof.

## Relationship to prior work
Liu and Liu (2026) explicitly construct the sketched Rayleigh–Ritz matrix and emphasize that even a symmetric positive-definite original problem may yield nonreal sketched eigenpairs, motivating their real-Schur formulation. Nakatsukasa and Tropp (2024, Section 6.8) already discuss this qualitative nonreal-eigenvalue phenomenon. Neither inspected source gives the exact spectral-width and observation-angle envelope above or a family attaining it for every positive angle. An earlier three-state E-optimal two-row Krylov sampling construction already attains the same constant within its restricted SPD family: its parameter \(p=	an\theta\) gives the ratio \(\sqrt{(\sqrt{1+p^2}-1)/2}\). That family provides sharpness *from below*, but not an upper bound valid for arbitrary SPD matrices and arbitrary trial planes. The present contribution is this universal upper bound, with a full equality family, rather than the numerical constant alone. Hrobat and Nakatsukasa (2026) study snapshot and row subsampling for sequences of eigenvalue problems; the inspected algorithmic material does not establish this universal extremal envelope. Kahan's classical nearly-Hermitian spectral bounds control imaginary parts by skew-Hermitian deviation in general, rather than characterize the constrained sampled-SPD extremum proved here. Thus the result is a sharp specialization, not the initial observation that sketched symmetric eigenproblems may exhibit nonreal Ritz values.

## Limitations
The classification relies on a two-dimensional trial space and a codimension-one orthogonal coordinate sketch. It does not cover arbitrary sampling weights, arbitrary sketch subspace codimension, higher-dimensional projected matrices, stochastic probability of a nonreal pair, asymptotic eigensolver convergence, or finite-precision implementations. The bound is in terms of exact singular values and spectral enclosures. Literature equivalence outside the inspected sources remains possible; no claim of exhaustive priority or independent verification is made.

## References
1. Jingyu Liu and Yuqi Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1, first public 2026-10-15, Sections 1 and 3.1. https://arxiv.org/html/2610.22261v1
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183–1214, DOI:10.1137/23M1565413, Sections 6.3 and 6.8. https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf
3. Francesco Hrobat and Yuji Nakatsukasa, *Solving a sequence of eigenvalue problems using snapshot and row subsampling*, arXiv:2610.19326v1, first public 2026-10-14. https://arxiv.org/abs/2610.19326
4. William Kahan, *Spectra of Nearly Hermitian Matrices*, Technical Report UCB/ERL M420 (1974); Proceedings of the American Mathematical Society 48 (1975), 11–17. https://www2.eecs.berkeley.edu/Pubs/TechRpts/1974/28755.html
