# Exponentially thin parameter gaps in a max-plus reset oscillator

## Finding

For the max-plus map
\[
F_R(X,Y)=(Y+\max(0,RX),\ 1-\max(0,RX)),\qquad 1<R<4,
\]
start with \((X_0,Y_0)=(1,1)\). For each sufficiently large integer \(n\), define
\[
\theta_n=\pi/n,\quad q_n=2\cos\theta_n,\quad r_n=q_n^2,
\quad D_n=\frac{nq_n^n}{4\sin^2\theta_n},\quad
I_n=[r_n-3/D_n,r_n].
\]
The all-positive-branch first-coordinate formula is
\[
H_j(R)=1+R^{(j+1)/2}\frac{\sin(j\theta(R))}{\sin\theta(R)},
\qquad \theta(R)=\arccos(\sqrt R/2).
\]
There are unique roots \(R_X(n),R_Y(n+1)\) in \(I_n\) of
\[
H_n(R_X(n))=0,\qquad H_n(R_Y(n+1))=1/R_Y(n+1).
\]
They satisfy \(R_X(n)<R_Y(n+1)<r_n\). At each of these roots and all intermediate parameters, the iterates through time \(n-1\) really do lie in the positive first-coordinate branch. The parameter gap between the successive branch-exit thresholds has the sharp law
\[
\boxed{\ R_Y(n+1)-R_X(n)
=\frac{\tan^2(\pi/n)}{n[2\cos(\pi/n)]^n}
\bigl(1+O(q_n^{-n})\bigr)
=\frac{\pi^2}{2^nn^3}\bigl(1+O(n^{-1})\bigr).\ }
\]
Define \(R_Y(n)\) by the analogous root \(H_{n-1}(R_Y(n))=1/R_Y(n)\), in the interval \(I_{n-1}\). Then the separation between consecutive same-window boundary roots has the contrasting size
\[
R_X(n)-R_Y(n)\sim \frac{8\pi^2}{n^3},\qquad
\frac{R_Y(n+1)-R_X(n)}{R_X(n)-R_Y(n)}\sim\frac{2^{-n}}8.
\]
The last quotient quantifies exponential smallness of the intervening gap relative to the neighboring polynomial-width reset window.

## Assumptions and scope

All asymptotics are for integers \(n\to\infty\); the integer threshold is absolute and is not optimized. The state has the specific initial value \((1,1)\); the parameter satisfies \(1<R<4\). The terms *branch-exit thresholds* and *parameter gap* refer to the stated zero equations along this initial orbit. The theorem does not classify attractors for arbitrary initial conditions and does not assert a dynamical type inside each gap.

On the positive branch, set \(A_R=\begin{pmatrix}R&1\\-R&0\end{pmatrix}\). Its eigenvalues are \(\sqrt R\exp(\pm i\theta(R))\), where \(\theta(R)=\arccos(\sqrt R/2)\), and the affine recursion is \((X_{j+1},Y_{j+1})=A_R(X_j,Y_j)+(0,1)\). In particular \(X_{j+2}=RX_{j+1}-RX_j+1\), with \(X_0=1\) and \(X_1=1+R\), giving the formula for \(H_j\).

## Proof

**Exact derivative.** At \(R=r_n\), one has \(\theta=\pi/n\) and \(H_n(r_n)=1\). Differentiating the trigonometric expression, using \(dR/d\theta=-4(2\cos\theta)\sin\theta\), gives
\[
H_n'(r_n)=\frac{n[2\cos(\pi/n)]^n}{4\sin^2(\pi/n)}=D_n>0.
\]
Since \(q_n\to2\), the displacement \(D_n^{-1}\) is exponentially small in \(n\), up to a polynomial factor.

**Uniform local control.** For \(R\in I_n\), the angle displacement obeys \(|\theta(R)-\pi/n|=O(q_n^{-n}n^{-2})\), since \(|d\theta/dR|=O(n)\). Elementary differentiation of the displayed \(H_n\), using \(\sin\theta\asymp n^{-1}\), \(d\theta/dR=O(n)\), and \(d^2\theta/dR^2=O(n^3)\), yields the uniform bound
\[
\sup_{R\in I_n}|H_n''(R)|=O(q_n^nn^6).
\]
Also \(D_n\asymp q_n^nn^3\). Taylor's theorem therefore implies, uniformly for \(0\le c\le3\),
\[
H_n(r_n-c/D_n)=1-c+O(q_n^{-n}),\qquad
H_n'(R)=D_n\bigl(1+O(q_n^{-n})\bigr)>0\quad(R\in I_n).
\]
Thus \(H_n\) passes once through both levels \(0\) and \(1/R\) on \(I_n\): its value at the left endpoint is negative, and its value at the right endpoint is one, exceeding \(1/r_n\). As it is strictly increasing, the roots are unique, with \(R_X(n)<R_Y(n+1)<r_n\).

**Realizability of the itinerary.** For \(R\in I_n\), the angle satisfies \(0<j\theta(R)<\pi\) for all integers \(1\le j<n\) once \(n\) is large enough. Consequently \(H_j(R)>1>0\) for these indices, including at both roots. Hence the formulas computed on the formal all-positive branch equal the genuine iterates of \(F_R\) up to the stated exit thresholds. Further, \(Y_{n+1}=1-RX_n\), which identifies the second root with the first zero of the next ordinate.

**Gap asymptotics.** The mean-value theorem applied between the roots gives
\[
\frac1{R_Y(n+1)}=H_n'(\xi_n)[R_Y(n+1)-R_X(n)]
\]
for some intermediate \(\xi_n\). Because \(R_Y(n+1)=r_n+O(D_n^{-1})\),
\[
R_Y(n+1)-R_X(n)=\frac1{r_nD_n}\bigl(1+O(q_n^{-n})\bigr)
=\frac{\tan^2(\pi/n)}{nq_n^n}\bigl(1+O(q_n^{-n})\bigr).
\]
Expanding \(\tan(\pi/n)\) and \(q_n=2\cos(\pi/n)\) gives \(G_n=\pi^22^{-n}n^{-3}(1+O(n^{-1}))\). The uniform error is relative; no finite-enumeration inference is used.

**Comparison with adjacent thresholds.** The same existence argument at index \(n-1\) places \(R_Y(n)=r_{n-1}+O(D_{n-1}^{-1})\), and the argument above places \(R_X(n)=r_n+O(D_n^{-1})\). Their difference is
\[
r_n-r_{n-1}+O(D_{n-1}^{-1}+D_n^{-1})
=\frac{8\pi^2}{n^3}\bigl(1+O(n^{-1})\bigr),
\]
because \(4\cos^2(\pi/n)=4-4\pi^2/n^2+O(n^{-4})\). Dividing the two estimates proves the quoted scale separation.

## Verification

The self-contained script `tools/check_gap.py` checks the affine recurrence against the trigonometric expression at three values of \(R\), locates both roots numerically with high precision for eight integers, verifies pre-exit positivity, and compares the measured gap with the closed-form leading expression. Running it in the package with Python, SymPy, and mpmath prints `RESET_GAP_CHECK_OK`. Finite checks do not prove existence, uniqueness, admissibility or the asymptotic error bounds; those follow from the analytic proof above.

## Relationship to prior work

Yamazaki and Ohmori (arXiv:2107.09300v1, 2021) introduce the parameterized max-plus map, derive its oscillatory closed form, identify inequalities defining reset-cycle windows, tabulate numerical root thresholds and discuss a rough relation between period and the eigenvalue angle. Ohmori and Yamazaki (arXiv:2402.06230v1, 2024) extend the model and revisit its bifurcation windows. These prior contributions, including the exact closed-form recurrence, are not claimed as new. The present claim isolates the exponentially thin gaps between successive exit-root equations, gives their sharp \(\pi^2\) prefactor and relative error, and proves a contrast with neighboring window widths. The result is a quantitative consequence that is not stated in the inspected sources.

## Limitations

The result concerns sufficiently large integer indices and one chosen initial point; it does not give an optimized smallest admissible integer. It does not infer quasi-periodicity, chaos, basin structure, or universal dynamics for parameters between the roots. The finite verification is illustrative; publication priority beyond the inspected primary literature remains uncertain.

## References

- T. Yamazaki and T. Ohmori, *Periodicity of Limit Cycles in a Max-Plus Dynamical System*, arXiv:2107.09300v1 (2021-07-20), especially the exact recurrence and parameter-window threshold table.
- T. Ohmori and T. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Max-Plus Dynamical System*, arXiv:2402.06230v1 (2024-02-09), especially the parameter-dependence and periodic-orbit discussion.
