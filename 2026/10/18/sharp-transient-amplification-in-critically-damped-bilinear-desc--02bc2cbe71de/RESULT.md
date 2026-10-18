# Sharp transient amplification in critically damped bilinear descent-ascent

## Finding

Consider the dissipative gradient descent-ascent (DGDA) iteration applied to the real zero-sum bilinear game \(\min_x\max_y x^{\mathsf T}Ay\), where \(A\in\mathbb R^{d\times d}\) obeys \(A^{\mathsf T}A=a^2I\) for some \(a>0\). Thus the game is nonsingular and has condition number one. Write \(z=(x,y)\), let \(\widehat z\) denote its auxiliary state, and apply the parameter choice \(\rho=1/2\) and \(\eta=1/a\) identified for bilinear DGDA in [1]. Let \(T\) be the resulting real linear update on \((z,\widehat z)\), equipped with the standard Euclidean product norm.

For **every** integer \(k\ge0\), every \(d\ge1\), and every such \(A\), the **exact** squared induced gain is
\[
\boxed{\|T^k\|_2^2=2^{-k}\bigl(1+k^2+k\sqrt{k^2+2}\bigr).}
\]
Its unique maximizing integer is \(k=3\), and the sharp all-time squared amplification is
\[
\boxed{\sup_{k\ge0}\|T^k\|_2^2=\frac{10+3\sqrt{11}}8.}
\]
For the natural *synchronized* initialization \(\widehat z_0=z_0\ne0\), the original (nonauxiliary) variables satisfy
\[
\boxed{\frac{\|z_k\|_2^2}{\|z_0\|_2^2}=\frac{(k+1)^2}{2^k},\qquad
\sup_{k\ge0}\frac{\|z_k\|_2^2}{\|z_0\|_2^2}=\frac94,}
\]
with the latter maximum uniquely at \(k=2\). Hence a condition-number-one game under these convergent parameter values has a real, finite-time *increase* in both full-state and original-variable squared error.

Although the spectral radius of \(T\) is \(2^{-1/2}\), its critical Jordan structure gives
\[
\lim_{k\to\infty}\frac{2^k\|T^k\|_2^2}{k^2}=2.
\]
There is therefore **no finite** \(C\) satisfying \(\|T^k\|_2^2\le C2^{-k}\) for all \(k\), whereas a finite prefactor exists for each strictly slower squared geometric base \(r>1/2\). This does not conflict with the weaker uniform linear-convergence bound in [1].

## Assumptions and scope

All calculations use exact arithmetic. Take \(d\ge1\), \(a>0\), \(A\in\mathbb R^{d\times d}\) with \(A^{\mathsf T}A=a^2I\); this implies \(AA^{\mathsf T}=a^2I\). The unique saddle is \((0,0)\). Define
\[
M=\begin{pmatrix}0&A\\-A^{\mathsf T}&0\end{pmatrix},\quad J=M/a,\quad
T=\begin{pmatrix}\frac12I-J&\frac12I\\\frac12I&\frac12I\end{pmatrix}.
\]
Here each identity block has dimension \(2d\). The DGDA updates are precisely \(z_{k+1}=(\frac12I-J)z_k+\frac12\widehat z_k\) and \(\widehat z_{k+1}=\frac12z_k+\frac12\widehat z_k\). The initial state may be arbitrary for the operator-norm formula; the second formula assumes \(\widehat z_0=z_0\). The norm on the full state is \(\|(z,\widehat z)\|_2^2=\|z\|_2^2+\|\widehat z\|_2^2\).

## Proof

**Complex normal-form reduction.** Since \(J^{\mathsf T}=-J\) and \(J^2=-I\), its complexification is unitarily diagonalizable with eigenvalues \(i\) and \(-i\). Under the same unitary transformation on both full-state blocks, \(T\) becomes a direct sum of the \(2\times2\) complex matrix
\[
B=\begin{pmatrix}\frac12-i&\frac12\\\frac12&\frac12\end{pmatrix}
\]
and its complex conjugate, with equal multiplicities. Consequently \(\|T^k\|_2=\|B^k\|_2\), and the real operator norm equals the complex singular norm by real-complex norm invariance.

**Defective critical eigenvalue.** Put \(\lambda=(1-i)/2\) and \(N=B-\lambda I\). Direct multiplication gives
\[
N=\frac12\begin{pmatrix}-i&1\\1&i\end{pmatrix},\qquad N^2=0,\quad N\ne0,\quad\|N\|_2=1.
\]
Hence \(B^k=\lambda^k(I+kN/\lambda)\). A nonzero rank-one nilpotent \(2\times2\) matrix of singular norm one is unitarily similar to \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), up to a harmless complex phase. For a complex number \(t\), direct diagonalization of the Hermitian Gram matrix gives
\[
\left\|\begin{pmatrix}1&t\\0&1\end{pmatrix}\right\|_2^2=
\frac{2+|t|^2+|t|\sqrt{|t|^2+4}}2.
\]
Here \(|\lambda|^2=1/2\) and \(|k/\lambda|=\sqrt2k\). Substitution yields the exact squared-gain formula. Its leading coefficient is \(2k^2 2^{-k}\), proving the sharp asymptotic and failure of a pure \(2^{-k}\) squared-rate bound.

**Exact global discrete peak.** The values at \(k=0,1,2,3\) are respectively \(1\), \((2+\sqrt3)/2\), \((5+2\sqrt6)/4\), and \((10+3\sqrt{11})/8\). The last exceeds the value at \(k=2\) because \(3\sqrt{11}>4\sqrt6\), and it exceeds those at \(k=0,1\). For every integer \(k\ge4\), \(k\sqrt{k^2+2}\le k^2+1\), so the gain is at most \(2^{-k}(2k^2+2)\). This upper bound decreases for integers \(k\ge4\) and is at most \(34/16\), strictly below the value at \(k=3\). The supremum is therefore sharp and unique.

**Synchronized original variables.** In each \(i\)-eigenspace, apply \(B^k\) to the vector \((w,w)\). The first component is exactly \((k+1)\lambda^k w\), and the second is \((1+ik)\lambda^k w\). Conjugate modes satisfy the same squared-norm identities. Consequently \(\|z_k\|_2^2=(k+1)^22^{-k}\|z_0\|_2^2\) and \(\|(z_k,\widehat z_k)\|_2^2=(k^2+k+1)2^{-k}\|(z_0,\widehat z_0)\|_2^2\). The original-variable squared gain increases from \(1\) to \(2\) to \(9/4\) and then decreases strictly, since the consecutive gain ratio is \((k+2)^2/[2(k+1)^2]<1\) exactly when \(k\ge2\).

## Verification

Run `python verify_dgda.py` with Python 3 (standard library only). The script directly multiplies complex and real update matrices and verifies their powers against the closed formulas for forty-one successive integers, including their behavior on synchronized nonzero initial states. It checks the nilpotency, exact finite-horizon comparisons numerically, and exact algebraic peak inequalities. Its recorded output is in `verification_output.txt`. The infinite-time statement and universal-dimensional result are established by the proof above, not extrapolated from these finite checks.

## Relationship to prior work

The DGDA update, its condition-number-one recommended parameters and its bilinear spectral-radius convergence analysis belong to Zheng, Loizou, You and Mallada [1, Secs. III–IV, Appendix B]. Their convergence theorem bounds a geometric rate but does not assert the exact norm of every update power, the sharp transient peak, the synchronized primal spike, or the Jordan prefactor of the exact spectral base. This result retains the same algorithm without modifying its update.

Montbrun and Renault [2] analyze the different two-step OGDA recursion and optimal asymptotic geometric ratios for bilinear games. Those results do not give the DGDA matrix-power norm. General Jordan and nonnormal-matrix formulas are classical [3]; the novelty claimed here is the DGDA-specific critical-mode identification and exact global finite-horizon amplification, **not** the nilpotent-binomial identity in isolation.

## Limitations

The claim is restricted to nonsingular square bilinear games with equal singular values and the specified parameters; it does not assert a universal transient factor for ill-conditioned games or other step choices. The full-state worst-case initial condition need not have synchronized auxiliary variables, whereas the separate \(9/4\) statement does. Finite initial amplification does not imply failure of asymptotic convergence. Earlier sources using alternative coordinates or norms might express an equivalent power law; independent literature assessment remains desirable.

## References

[1] T. Zheng, N. Loizou, P. You and E. Mallada, "Dissipative Gradient Descent Ascent Method: A Control Theory Inspired Algorithm for Min-max Optimization," arXiv:2403.09090v1, first publicly submitted 2024-03-14; IEEE Control Systems Letters 8 (2024), 2009–2014. https://arxiv.org/abs/2403.09090

[2] É. de Montbrun and J. Renault, "Optimistic Gradient Descent Ascent in Zero-Sum and General-Sum Bilinear Games," arXiv:2208.03085, first publicly submitted 2022-08-05. https://arxiv.org/abs/2208.03085

[3] L. N. Trefethen and M. Embree, *Spectra and Pseudospectra: The Behavior of Nonnormal Matrices and Operators*, Princeton University Press, 2005, for general nonnormal transient-growth context (not an algorithm-specific comparison).
