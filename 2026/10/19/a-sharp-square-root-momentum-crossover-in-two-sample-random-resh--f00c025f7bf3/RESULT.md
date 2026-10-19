# A sharp square-root momentum crossover in two-sample random reshuffling

## Finding
For the two strongly convex component losses
\[
f_1(x)=\frac12(x-1)^2,\qquad f_2(x)=\frac12(x+1)^2,
\]
consider the ordinary heavy-ball random-reshuffling algorithm with a **constant** per-component stepsize \(r>0\) and momentum \(b\in[0,1)\). A fresh independent uniform permutation of the two components is used in each epoch, with momentum carried across epochs. For every \(0<r<2(1+b)\) and every deterministic initial pair, the mean-squared error at completed epochs tends to
\[
\boxed{
V_{\rm RR}(r,b)=
\frac{r^2\left[4b^2(1+b)+r(1-4b-5b^2)+2br^2\right]}
{(1-b^2)(2+2b-r)\left[r^2-2(1+b)r+2(1+b^2)\right]}.
}
\]
In the same stable interval, independent uniform **with-replacement** component choices at each individual step have stationary mean-squared error
\[
V_{\rm iid}(r,b)=\frac{r(1+b)}{(1-b)(2+2b-r)}.
\]
The same covariance calculation resolves the **within-epoch phase**: in the stationary regime the preceding odd-indexed iterate has mean-squared error
\[
V_{\rm odd}(r,b)=\frac{r^2\left[b^2r-4br+4b+2r^2-5r+4\right]}
{(1-b^2)(2+2b-r)\left[r^2-2(1+b)r+2(1+b^2)\right]}.
\]
For small stepsize, \(V_{\rm odd}(r,b)\sim r^2/(1-b^4)\) at every fixed \(b\in[0,1)\), whereas the completed-epoch variance is cubic at zero momentum and quadratic at fixed positive momentum. Thus the limiting ratio of the completed-epoch to the intermediate-phase variances is \(b^2\) for fixed \(b>0\) and is asymptotic to \(r/4\) for \(b=0\). This phase distinction is invisible to results only on variance averaged across all individual steps.

The two equations share the same exact average objective \(F(x)=(x^2+1)/2\), with unique minimizer \(x_*=0\). Thus their stationary expected objective gaps are precisely half of these mean-squared errors.

The resulting small-stepsize transition is sharp:
\[
\begin{aligned}
V_{\rm RR}(r,0)&=\frac{r^3}{(2-r)(r^2-2r+2)}\sim \frac14r^3,\\
V_{\rm RR}(r,b)&\sim \frac{b^2}{1-b^4}r^2\quad\text{for each fixed }b\in(0,1),\\
V_{\rm RR}(r,b(r))&=r^2\left[b(r)^2+\frac r4\right](1+o(1))
\quad\text{if }r\downarrow0,\ b(r)\to0.
\end{aligned}
\]
Consequently, if \(b(r)/\sqrt r\to c\in[0,\infty)\), then \(V_{\rm RR}/r^3\to c^2+1/4\); if \(b(r)\to0\) but \(b(r)/\sqrt r\to\infty\), then \(V_{\rm RR}/[r^2b(r)^2]\to1\). The crossover occurs at \(b\asymp\sqrt r\): among vanishing nonnegative momentum schedules, the cubic completed-epoch error floor persists exactly when \(b=O(\sqrt r)\). For fixed \(b>0\), random reshuffling still improves on iid sampling by one power of the stepsize, but loses one power of the unusually small \(r^3\) zero-momentum error floor.

## Assumptions and scope
Let \(x_{-1},x_0\in\mathbb R\) be deterministic, independent of all future permutations. For each epoch \(k\ge0\), independently choose \(\pi_k=(1,2)\) or \((2,1)\), each with probability \(1/2\). At component step \(t=2k,2k+1\), update
\[
x_{t+1}=x_t-r f'_{\pi_k(t-2k+1)}(x_t)+b(x_t-x_{t-1}).
\]
Momentum is not restarted or reinitialized between epochs. Only the scalar losses above, independent epoch permutations, exact gradients, and the indicated parameter interval are asserted. The mean-squared-error statement samples \(x_{2k}\) **after complete epochs**, not an average of both within-epoch phases. The comparator instead draws each individual component index independently with replacement. The expectations include the randomness in permutations or independent component choices.

## Proof
Write \(a=1+b-r\), and define
\[
A=\begin{pmatrix}a&-b\\1&0\end{pmatrix},\qquad
B=A^2=\begin{pmatrix}a^2-b&-ab\\a&-b\end{pmatrix},\qquad
q=r\begin{pmatrix}b-r\\1\end{pmatrix}.
\]
Let \(Y_k=(x_{2k},x_{2k-1})^{\mathsf T}\). Evaluating the two component gradients and using that one permutation has the sign opposite to the other gives the **exact** epoch recurrence
\[
Y_{k+1}=BY_k+q\xi_k,
\]
where the \(\xi_k\) are independent equiprobable signs. In particular, the per-epoch mean forcing vanishes, although the individual steps have nonzero gradient noise at the optimizer.

The characteristic polynomial of \(A\) is \(\lambda^2-a\lambda+b\). The three strict Schur conditions for this real quadratic are
\[
1-b>0,\qquad 1-a+b=r>0,\qquad 1+a+b=2(1+b)-r>0.
\]
They hold exactly on the stipulated stable parameter region. Therefore \(\rho(B)=\rho(A)^2<1\). It follows from the epoch recursion that \(\mathbb E Y_k=B^kY_0\to0\), and the covariance converges to the unique symmetric matrix
\[
\Sigma=\sum_{j=0}^{\infty}B^jqq^{\mathsf T}(B^{\mathsf T})^j,
\qquad \Sigma=B\Sigma B^{\mathsf T}+qq^{\mathsf T}.
\]
The same absolutely convergent linear series produces the unique invariant law of the epoch states; it does not imply almost-sure convergence of individual iterates for fixed positive stepsize.

For completeness, put \(p=a^2-b\), \(s=-ab\), \(t=a\), \(u=-b\), and write \(\Sigma=\begin{psmallmatrix}X&Y\\Y&Z\end{psmallmatrix}\). Expanding the Lyapunov equation yields the fully specified three-by-three linear system
\[
\begin{aligned}
X&=p^2X+2psY+s^2Z+r^2(b-r)^2,\\
Y&=ptX+(pu+st)Y+suZ+r^2(b-r),\\
Z&=t^2X+2tuY+u^2Z+r^2.
\end{aligned}
\]
Its coefficient matrix is invertible because \(\rho(B)<1\). Solving yields \(X=V_{\rm RR}(r,b)\) displayed in the finding. To make the critical algebra independently checkable, the other two solution entries have a common denominator
\[
\Delta=(1-b^2)(2+2b-r)\left[r^2-2(1+b)r+2(1+b^2)\right]
\]
and satisfy
\[
\begin{aligned}
\Delta Y&=-r^2(3b^2r-4b^2-3br^2+6br-4b+r^3-3r^2+3r),\\
\Delta Z&=r^2(b^2r-4br+4b+2r^2-5r+4).
\end{aligned}
\]
Direct substitution of all three entries into the stated linear system is a rational-polynomial identity; the accompanying exact checker verifies it. The last factor in \(\Delta\) equals \((r-1-b)^2+(1-b)^2>0\), and the other factors are positive in the stipulated region.

For iid component choices, the single-step state has the recurrence \(Z_{t+1}=AZ_t+(r,0)^{\mathsf T}\varepsilon_t\), with independent equiprobable signs. Its discrete Lyapunov equation, solved by the same three-entry procedure, has top-left entry \(V_{\rm iid}(r,b)\).

Finally, inserting \(b=0\) gives the exact cubic identity. For fixed \(b\in(0,1)\), divide the rational formula by \(r^2\) and take \(r\downarrow0\). If \(r,b\to0\) jointly, the numerator bracket is \(4b^2+r+O((r+b)(b^2+r))\), while \(\Delta=4+O(r+b)\); this proves the uniform joint asymptotic and all crossover regimes claimed above. The exact fixed-\(b\) ratio of reshuffling to iid error is \(2rb^2/[(1+b)(1+b^2)]+o(r)\) for \(0<b<1\), while at \(b=0\) it is \(r^2/2+o(r^2)\).

## Verification
Run `python verification/check.py` with dependencies in `verification/requirements.txt`. The symbolic checker verifies the full covariance matrix in the Lyapunov equation, the iid comparator, exact zero-momentum and asymptotic identities, and the square-root crossover. It independently enumerates every sign path for six complete epochs at each of five exact-rational parameter pairs (30 path-moment comparisons), and compares five directly iterated numerical covariance matrices with the symbolic solution. Expected output is retained in `verification/observed-output.txt`. Enumeration and floating-point checks are corroboration; the infinite-time and limiting arguments follow from the Schur stability proof and exact identities.

## Relationship to prior work
Qiu and Milzarek (original 2024 preprint, subsequently revised) study the actual random-reshuffling heavy-ball algorithm and prove broad nonconvex complexity and last-iterate results. Their accessible analysis includes weighted without-replacement sampling estimates and constant-stepsize complexity bounds; those do not supply the scalar, exact completed-epoch invariant covariance or its changing powers of the stepsize as momentum vanishes. Tran, Tran-Dinh, and Nguyen (2024) analyze an **epoch-anchored** shuffling momentum scheme, a different recurrence. Mishchenko, Khaled, and Richtárik (2020) provide quantitative no-momentum random-reshuffling bounds. Wang and collaborators (2023/2024) study small-learning-rate momentum under independently sampled gradient noise, not correlated without-replacement epochs. Related no-momentum comparisons, including the 2020 work *Random Reshuffling is Not Always Better*, concern different sampling/optimization regimes. Domingo-Enrich (2022) analyzes stationary variances of shuffling SGD with momentum through power spectra. Its accessible numerical reproduction script averages squared error over all individual iterations, mixing the two epoch phases. The exact phase-specific claims here are not implied by that all-step average alone. The full paper text was not accessible for a decisive comparison, and a broader phase-resolved formula there remains a material originality risk. The shared underlying discrete Lyapunov method is classical and is not claimed as new; the mathematical content here is the exact model-specific covariance comparison and nonuniform momentum/stepsize transition.

## Limitations
This is a two-component, one-dimensional, equal-curvature strongly convex example. It does not imply a universal limitation for every finite-sum objective or every definition of momentum, nor does it establish any finite-time advantage of one sampler. The phase-specific floor is not the mean over all inner iterates. These constant-step stationary quantities should not be confused with convergence under diminishing stepsizes. Deriving a simple formula from a general discrete Lyapunov framework is possible once the special epoch recurrence is recognized; an equivalent formulation in older switching or Markov-jump linear-systems literature is an unresolved originality risk. Scientific claims do not include independent validation.

## References
- J. Qiu and A. Milzarek, *Random Reshuffling with Momentum for Nonconvex Problems: Iteration Complexity and Last Iterate Convergence*, arXiv:2404.18452, first made public 2024-04-29; later revisions include B. Ma. https://arxiv.org/abs/2404.18452
- T. H. Tran, Q. Tran-Dinh, and L. M. Nguyen, *Shuffling Momentum Gradient Algorithm for Convex Optimization*, arXiv:2403.03180 (2024). https://arxiv.org/abs/2403.03180
- K. Mishchenko, A. Khaled, and P. Richtárik, *Random Reshuffling: Simple Analysis with Vast Improvements*, arXiv:2006.05988 (2020). https://arxiv.org/abs/2006.05988
- R. Wang et al., *The Marginal Value of Momentum for Small Learning Rate SGD*, arXiv:2307.15196 (2023; updated 2024). https://arxiv.org/abs/2307.15196
- C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632 (2022). https://arxiv.org/abs/2206.00632
- *Random Reshuffling is Not Always Better*, NeurIPS (2020). https://proceedings.neurips.cc/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf
