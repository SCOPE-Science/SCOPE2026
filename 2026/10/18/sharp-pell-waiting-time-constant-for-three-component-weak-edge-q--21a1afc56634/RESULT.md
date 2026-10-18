# Sharp Pell waiting-time constant for three-component weak-edge quantum pulsation

## Finding
Let \(L\) be the unweighted three-vertex path Laplacian and set
\[
 F(s)=\left|[\cos(s\sqrt L)]_{3,1}\right|^2
 =\left(\frac13-\frac12\cos s+\frac16\cos(\sqrt3s)\right)^2,\qquad s\geq0.
\]
The transfer envelope never reaches unity at finite \(s\), but its sharp asymptotic high-fidelity waiting-time constant is
\[
 \boxed{\liminf_{s\to\infty}s^2\bigl(1-F(s)\bigr)=\frac{\pi^4}{144}.}
\]
An explicit sequence attaining the lower asymptotic envelope is obtained from the positive Pell solutions
\[
 p_n+q_n\sqrt3=(2+\sqrt3)^{2n+1}\quad(n=0,1,2,\ldots),
 \qquad \Delta_n=\pi(\sqrt3q_n-p_n),
 \qquad s_n=\pi q_n-\frac{\Delta_n}{2\sqrt3}.
\]
Then \(p_n\) is even, \(q_n\) is odd, and
\[
 \lim_{n\to\infty}s_n^2(1-F(s_n))=\frac{\pi^4}{144}.
\]
The constant is a sharp asymptotic cost along optimal high-fidelity subsequences, **not** a uniform inverse-error waiting-time formula for every fidelity target.

## Assumptions and scope
The wave operator is the symmetric mass-normalized Laplacian of three identical components joined in a path by equal weak edges,
\[
 L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}.
\]
Hosaka and Segawa (arXiv:2610.07768v1, Theorem 3.1 and the three-component example) show that a corresponding discrete-time weak-edge quantum walk has a leading endpoint-to-endpoint finding probability given by \(F(s)\), where \(s=\tau/\sqrt m\), \(m\) is the common internal arc count of the components, and the physical step count is of order \(\tau/\sqrt{2\varepsilon}\). The present assertion is an exact statement about the limiting wave envelope \(F\). In the source's unscaled variable,
\[
 \liminf_{\tau\to\infty}\tau^2\bigl(1-F(\tau/\sqrt m)\bigr)=\frac{m\pi^4}{144}.
\]
The source's weak-edge asymptotic is taken first for each fixed \(\tau\), followed by the large-\(\tau\) envelope limit. No uniform joint \(\varepsilon\to0\), \(\tau\to\infty\) error bound is asserted.

## Proof
**Spectral reduction.** The matrix \(L\) has distinct eigenvalues \(0,1,3\). Its three spectral projectors satisfy
\[
 [P_0]_{31}=\frac13,\quad[P_1]_{31}=-\frac12,\quad[P_3]_{31}=\frac16.
\]
Functional calculus gives the displayed formula for the real endpoint amplitude \(A(s)\) with \(F(s)=A(s)^2\). The pointwise bounds \(-1/3\leq A(s)\leq1\) hold. The upper endpoint \(A=1\) requires both \(\cos s=-1\) and \(\cos(\sqrt3s)=1\). There is no such \(s\), since it would require \(s=\pi q\) for an odd integer \(q\) and \(\sqrt3s=\pi p\) for an even integer \(p\), contradicting irrationality of \(\sqrt3\). Since \(A\geq-1/3\), also \(F(s)<1\) at every finite \(s\).

**Universal lower asymptotic bound.** Let \(s_j\to\infty\) be an arbitrary sequence on which \(s_j^2(1-F(s_j))\) remains bounded. If no such sequence exists the lower bound is immediate. Write
\[
 D(s)=1-A(s)=\tfrac12(1+\cos s)+\tfrac16(1-\cos(\sqrt3s))\geq0.
\]
Because \(1-F=D(2-D)\) and \(0\leq D\leq4/3\), bounded \(s^2(1-F)\) implies \(D=O(s^{-2})\). Thus there are odd positive integers \(q\) and even positive integers \(p\) such that
\[
 s=\pi q+u,\qquad \sqrt3s=\pi p+v,\qquad u,v=O(s^{-1}).
\]
Set \(\Delta=v-\sqrt3u=\pi(\sqrt3q-p)\). Taylor expansion, with its remainder controlled because \(u,v=O(s^{-1})\), yields
\[
 D=\frac{u^2}{4}+\frac{v^2}{12}+O(s^{-4})
 \ \geq\ \frac{(v-\sqrt3u)^2}{24}+O(s^{-4})
 =\frac{\Delta^2}{24}+O(s^{-4}).
\]
Here the exact nonnegative difference between the two quadratic forms is
\[
 \frac{u^2}{4}+\frac{v^2}{12}-\frac{(v-\sqrt3u)^2}{24}
 =\frac{(\sqrt3u+v)^2}{24}.
\]
Hence \(1-F=2D-D^2\geq\Delta^2/12+O(s^{-4})\). Integer irrationality supplies \(|p^2-3q^2|\geq1\), while \(q\sim s/\pi\) and \(p\sim\sqrt3q\). Consequently,
\[
 |\Delta|=\frac{\pi|p^2-3q^2|}{\sqrt3q+p}
 \geq\frac{\pi}{\sqrt3q+p},\qquad
 \liminf s^2\Delta^2\geq\frac{\pi^4}{12}.
\]
Combining these bounds proves \(\liminf s^2(1-F(s))\geq\pi^4/144\) along every bounded-cost sequence, and therefore along all positive times.

**Sharpness by Pell parity.** The integer expansion \((2+\sqrt3)^{2n+1}=p_n+q_n\sqrt3\) satisfies \(p_n^2-3q_n^2=1\), with \(p_n\) even and \(q_n\) odd: multiplying by \((2+\sqrt3)^2=7+4\sqrt3\) preserves these parities. Furthermore \(q_n\to\infty\) and
\[
 \Delta_n=\pi(\sqrt3q_n-p_n)=-\frac{\pi}{p_n+\sqrt3q_n}.
\]
Choose \(s_n=\pi q_n-\Delta_n/(2\sqrt3)\). Its two phase errors are exactly \(u_n=-\Delta_n/(2\sqrt3)\) and \(v_n=\Delta_n/2\); they saturate the quadratic lower bound. Since \(s_n\sim\pi q_n\) and \(\Delta_n\sim-\pi/(2\sqrt3q_n)\),
\[
 1-F(s_n)=\frac{\Delta_n^2}{12}+O(q_n^{-4}),\qquad
 s_n^2(1-F(s_n))\longrightarrow\frac{\pi^4}{144}.
\]
This matches the lower bound. \(\square\)

## Verification
The standalone file `verify.py` checks the exact Laplacian spectral projectors and quadratic phase inequality symbolically. It constructs integer Pell solutions, tests their parities and norm-one property exactly, and evaluates the resulting high-precision transfer infidelities against \(\pi^4/144\). The finite computational checks are corroborating checks, not a substitute for the universal proof above.

## Relationship to prior work
Hosaka and Segawa, *Pulsation of quantum walk on finite graph* (arXiv:2610.07768v1, 6 October 2026), establish the weak-edge reduction and explicitly provide the three-component leading transfer formula. That reduction and formula are taken as existing results. Classical spectral criteria for perfect and pretty-good quantum state transfer (including work of Godsil and subsequent discrete-time quantum-walk classifications) concern attainability or arbitrarily close transfer, not the particular sharp asymptotic Pell coefficient derived here. Exact transfer classifications of general three-mode symmetric wave systems may likewise determine the supremum without specifying the quantitative near-transfer waiting-time constant. The increment claimed here is precisely the \(\liminf\) coefficient and its optimal Pell realization.

## Limitations
This result treats only the stated equal-mass, equal-link three-component envelope and its prescribed time normalization. It does not yield a bound on the actual discrete-time walk uniform in very large observation times, the first time to cross every chosen error tolerance, or arbitrary inhomogeneous three-component couplings. Existing general Diophantine approximation theorems may contain components of the proof; the exact coefficient is presented as a model-specific quantitative consequence, subject to independent literature review.

## References
1. T. Hosaka and E. Segawa, *Pulsation of quantum walk on finite graph*, arXiv:2610.07768v1 (first posted 2026-10-06), https://arxiv.org/abs/2610.07768.
2. C. Godsil, *State transfer on graphs*, arXiv:1102.4898 (2011), https://arxiv.org/abs/1102.4898.
3. A. Chan and H. Zhan, *Pretty good state transfer in discrete-time quantum walks*, J. Phys. A: Math. Theor. **56** (2023) 165305; arXiv:2105.03762, https://arxiv.org/abs/2105.03762.
