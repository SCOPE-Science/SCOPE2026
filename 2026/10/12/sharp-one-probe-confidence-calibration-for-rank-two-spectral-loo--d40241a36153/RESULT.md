# Sharp one-probe confidence calibration for rank-two spectral look-ahead

## Finding

**Theorem (sharp rank-two conditional risk and its inverse).** Let \(E\in\mathbb R^{m\times n}\) be a deterministic matrix of rank exactly two, with both dimensions at least two. Draw \(g\sim N(0,I_n)\), independently of \(E\), and define
\[
q=\frac{Eg}{\|Eg\|_2},\qquad H(E,g)=\|q^{\mathsf T}E\|_2.
\]
The denominator is nonzero with probability one. The statistic is the one-column projected-block spectral-norm indicator of a Gaussian look-ahead randomized QB step.

For every real \(0<t<1\), the exact worst-case probability, with the supremum taken over **all rank-two real residual matrices of any admissible dimensions**, is
\[
\boxed{\sup_{\operatorname{rank}(E)=2}\Pr\!\left[H(E,g)<t\|E\|_2\right]
=\Phi(t):=\frac2\pi\arctan\!\left(\frac{t^2}{2\sqrt{1-t^2}}\right).}
\]
The supremum is achieved, not merely approached: the ratio of nonzero singular values is exactly \(\sigma_2(E)/\sigma_1(E)=t/\sqrt2\). In particular, \(\Phi(1/2)=0.09125789668597989\ldots\): a one-column look-ahead can report less than half the true residual spectral norm with sharp probability about 9.13% even with a fresh Gaussian probe.

For every confidence level \(0<\delta<1\), set
\[
c_\delta=\tan(\pi\delta/2),\qquad
t_\delta=\sqrt{2c_\delta\left(\sqrt{1+c_\delta^2}-c_\delta\right)}.
\]
Then the **sharp uniform one-sided confidence bound** is
\[
\boxed{\Pr\!\left[\|E\|_2>\frac{H(E,g)}{t_\delta}\right]\le\delta.}
\]
No larger value than \(t_\delta\) can replace it for all rank-two residuals. For example, \(1/t_{0.1}=1.922557310134\ldots\) is the smallest universal multiplicative upper-confidence factor at the 90% level in this rank-two setting.

## Assumptions and scope

All arithmetic is exact and real. The Gaussian vector is independent of the tested residual matrix. The residual may instead be random and history-dependent if, conditional on the history, its rank is exactly two and the new Gaussian vector is independent of that history; the conclusions then hold for each such conditional residual and hence also unconditionally. No distribution of the residual itself is assumed. This is a statement about a single look-ahead projected block, not about the final pruned QB approximation.

In a Gaussian matrix-free QB look-ahead step with one column, \(Y=Eg\), \(q=\operatorname{orth}(Y)\), and \(B=q^{\mathsf T}E\). Because the new basis vector is orthogonal to previously retained basis vectors, \(B\) is also the new row block obtained by projecting the original operator when \(E\) is the current residual. Scaling a single Gaussian column leaves \(q\) unchanged.

## Proof

Write the thin singular-value decomposition as
\[
E=U\operatorname{diag}(\sigma_1,\sigma_2)V^{\mathsf T},
\qquad \sigma_1\ge\sigma_2>0,
\]
where \(U,V\) have two orthonormal columns. The Gaussian coordinates \(h=V^{\mathsf T}g\) are independent standard normals \(h_1,h_2\). Set \(r=\sigma_2/\sigma_1\in(0,1]\). Computing the projected row directly gives
\[
\frac{H(E,g)^2}{\|E\|_2^2}
=\frac{h_1^2+r^4h_2^2}{h_1^2+r^2h_2^2}.
\tag{1}
\]
This is an exact identity of random variables, independent of the ambient dimensions and singular vectors. It lies between \(r^2\) and \(1\) almost surely. For \(r\ge t\) the underestimation event has probability zero. For \(0<r<t<1\), rearranging (1) gives precisely
\[
\{H<t\sigma_1\}=
\left\{\left|\frac{h_1}{h_2}\right|
<r\sqrt{\frac{t^2-r^2}{1-t^2}}\right\},
\]
up to null events. The ratio of two independent standard real normals is a standard Cauchy random variable. Its absolute cumulative distribution is \(\Pr(|C|<a)=(2/\pi)\arctan(a)\) for \(a\ge0\). Thus, for each fixed singular-value ratio,
\[
\Pr(H<t\sigma_1)=
\begin{cases}
\frac2\pi\arctan\!\left(r\sqrt{\frac{t^2-r^2}{1-t^2}}\right),&0<r<t,\\
0,&t\le r\le1.
\end{cases}
\tag{2}
\]
Maximizing (2) in \(r\) is equivalent to maximizing \(r^2(t^2-r^2)\) on \([0,t]\). The exact identity
\[
\frac{t^4}{4}-r^2(t^2-r^2)
=\left(r^2-\frac{t^2}{2}\right)^2\ge0
\]
proves the unique maximizer \(r=t/\sqrt2\). Taking \(E=\operatorname{diag}(1,t/\sqrt2)\) proves attainment and yields the displayed \(\Phi(t)\).

The function \(\Phi:(0,1)\to(0,1)\) is strictly increasing and continuous, with limits zero and one at its endpoints. Put \(c=\tan(\pi\delta/2)\) and solve \(\Phi(t)=\delta\). Writing \(u=t^2\), the equation is \(u^2=4c^2(1-u)\). Its unique solution in \((0,1)\) is \(u=2c(\sqrt{1+c^2}-c)\), proving the formula for \(t_\delta\). The confidence event is exactly the underestimation event at \(t_\delta\); the rank-two example above attains equality, proving that the factor cannot be improved. Conditioning on previous history preserves the same proof for each deterministic realization of the residual.

## Verification

Run `python verify.py` with Python 3 and the standard library. It checks 3,584 exact-rational two-coordinate matrix-projection identities, 171 exact-rational instances of the sharp quadratic square identity, eight inverse-confidence cases, and 510,000 seeded Gaussian draws over three thresholds. The finite experiments corroborate, but do not establish, the continuum supremum or the probability formula; these follow from the preceding proof and the standard normal-ratio/Cauchy identity.

## Relationship to prior work

Smith, Do, and Chen [1], Algorithm 4.1 and §4.1, introduce the projected spectral-norm look-ahead \(\|B_i\|_2\) with \(B_i=Q_i^{\mathsf T}E_{i-1}\). Their Theorem 4.3 obtains a spectral-norm error guarantee using a general probabilistic projection bound, but does not give the exact one-probe rank-two underestimation law or its sharp singular-value maximization. Their adjoint-free Algorithm 4.3 instead tests \(\|E_{i-1}\Omega_i\|_2\); its random scale and probability law differ, and this theorem does not apply to that indicator.

Saibaba [2], in particular Theorem 9, gives general singular-value bounds for randomized subspace iteration that underlie the general comparison in [1]; those bounds do not imply the exact sharp probability and inverse confidence factor given above. Meier and Nakatsukasa [3] analyze numerical-rank estimation from Gaussian two-sided sketches, a different estimator with concentration-style accuracy results. The elementary Cauchy ratio distribution is classical; only its exact optimization for this particular look-ahead statistic and confidence calibration are asserted here.

## Limitations

The singular-spectrum minimax classification is restricted to rank exactly two, one **real Gaussian** probe, one projected-row norm, independent fresh sampling, and exact arithmetic. It does not claim a uniform bound for rank greater than two, complex probes, the forward-only sketch-norm indicator, earlier/later adaptive decisions, multi-column block norms, approximate power-iteration norms, or floating-point implementations. In a full algorithm, a stopping decision and rank pruning interact with additional random variables; the result must not be treated as an exact probability for the entire output.

## References

[1] A. I. Smith, E. Do and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1, first submitted 2026-07-07; especially §4.1, Algorithm 4.1, Theorem 4.3 and Algorithm 4.3. https://arxiv.org/pdf/2607.06758

[2] A. K. Saibaba, *Randomized Subspace Iteration: Analysis of Canonical Angles and Unitarily Invariant Norms*, SIAM Journal on Matrix Analysis and Applications **40** (2019), 23–48; preprint arXiv:1804.02614. https://arxiv.org/pdf/1804.02614

[3] M. Meier and Y. Nakatsukasa, *Fast randomized numerical rank estimation for numerically low-rank matrices*, Linear Algebra and its Applications **686** (2024), 1–32, DOI:10.1016/j.laa.2024.01.001. https://doi.org/10.1016/j.laa.2024.01.001
