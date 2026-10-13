# A sharp refresh-run moment clock for Gaussian iterative Hessian sketches

## Finding

The number of consecutive iterations that reuse a Gaussian Hessian sketch, rather than the marginal distribution of a sketch, controls the existence of unconditional error moments. A Bernoulli refresh rule with any strictly positive chance of reuse gives an exact finite-horizon moment cutoff, even when every such algorithm converges exponentially fast almost surely.

**Theorem (refresh-run moment clock and almost-sure invariance).** Fix integers \(n\ge2\) and \(\ell>4\). Let \(A=e_1\in\mathbb R^{n\times1}\), \(b=0\), \(x_0\in\mathbb R\setminus\{0\}\), and \(f(x)=\frac12\|Ax-b\|_2^2=\frac12 x^2\). Take the deterministic step size \(\eta=(\ell-4)/\ell\). Every fresh sketch \(S\in\mathbb R^{\ell\times n}\) has independent \(N(0,1/\ell)\) entries, so its scalar sketched Hessian \(W=A^{\mathsf T}S^{\mathsf T}SA\) has law \(\chi^2_\ell/\ell\). The exact iterative Hessian sketch update is
\[
 x_{t+1}=\bigl(1-\eta/W_t\bigr)x_t,\qquad t=0,1,\ldots.
\]
Draw \(W_0\) freshly. Before each subsequent iteration, independently refresh to a new \(W_t\) with probability \(p\in(0,1]\), otherwise retain \(W_{t-1}\). All refresh indicators and all fresh Gaussian sketches are independent. For every real \(q>0\) and integer \(k\ge1\), the following conditions are necessary and sufficient:
\[
\begin{aligned}
 0<p<1:&\quad \mathbb E|x_k|^q<\infty\ \Longleftrightarrow\ \ell>2qk,\\
 p=1:&\quad \mathbb E|x_k|^q<\infty\ \Longleftrightarrow\ \ell>2q.
\end{aligned}
\]
For every \(p\in(0,1]\), independently of its numerical value, the almost-sure exponential error rate exists and equals the same finite number
\[
 \lim_{k\to\infty}\frac1k\log\frac{|x_k|}{|x_0|}
 =\lambda_{\ell,\eta}:=\mathbb E\log|1-\eta/W|<0,
 \qquad W\sim\chi^2_\ell/\ell.
\]
The fully refreshed iteration has the exact mean-square behavior
\[
 \mathbb E|x_k|^2=|x_0|^2\left(\frac{2}{\ell-2}\right)^k\quad(p=1),
\]
while every \(0<p<1\) has \(\mathbb E|x_k|^2=\infty\) for all integers \(k\ge\lceil\ell/4\rceil\). Thus positive-probability sketch persistence can destroy every sufficiently late mean-square statistic without changing the almost-sure Lyapunov exponent.

**Exact bounded-reuse comparison.** If the sketch is instead refreshed deterministically every \(B\ge1\) updates, independently between blocks, then for every \(q>0\) and \(k\ge1\),
\[
 \mathbb E|x_k|^q<\infty\quad\Longleftrightarrow\quad\ell>2q\min\{B,k\},
\]
and the almost-sure Lyapunov exponent remains \(\lambda_{\ell,\eta}<0\). Hence a bounded refresh interval \(B\) has all finite-horizon second moments exactly when \(\ell>4B\), whereas any Bernoulli refresh rule allowing arbitrarily long unrefreshed runs fails this property for every finite \(\ell\).

In particular, at \(\ell=6\) and \(\eta=1/3\), the fully refreshed procedure has \(\mathbb E|x_1|^2=|x_0|^2/2\) and \(\mathbb E|x_2|^2=|x_0|^2/4\). For **every** \(0<p<1\), the first moment remains \(\mathbb E|x_1|^2=|x_0|^2/2\), but the second-iterate mean square is already infinite.

## Assumptions and scope

All randomness is mathematical, and all updates use exact real arithmetic. The least-squares matrix is a rank-one column with unit Euclidean norm; it is full column rank, with an arbitrary ambient row dimension \(n\ge2\). The objective gradient \(\nabla f(x)=x\) is exact and not sketched. Only the Hessian preconditioner is sketched. An independent Gaussian \(\ell\times n\) test matrix produces each fresh Hessian. The first sketch is independent of the deterministic, nonzero \(x_0\), and the refresh rule does not depend on sketch values or iterates. The study concerns unconditional expectation over both sketch values and refresh decisions. At any individual finite sample realization, the iterates are finite almost surely.

The scalar case deliberately isolates inverse-sketch tail behavior from matrix noncommutativity. The selected \(\eta=(\ell-4)/\ell\) is the exact mean-square-optimal constant step for independent scalar Gaussian sketches, not an adaptive line search or a conditional step-size safeguard. The moment equivalences hold for all real \(q>0\) at the stated \(\eta>0\). In fact their tail proof applies to any fixed positive step size, but no universal almost-sure contraction is claimed for such other steps.

## Proof

**1. Scalar reduction and inverse moments.** As \(A=e_1\), the sketch Hessian is
\[
 W=\sum_{j=1}^{\ell}S_{j1}^{2}=\frac1\ell\sum_{j=1}^{\ell}Z_j^2,
\]
with independent standard Gaussians \(Z_j\). Its density on \((0,\infty)\) is
\[
 h_\ell(w)=\frac{(\ell/2)^{\ell/2}}{\Gamma(\ell/2)}w^{\ell/2-1}e^{-\ell w/2}.
\]
For any \(r>0\) and \(\eta>0\), the only divergent endpoint of \(\mathbb E|1-\eta/W|^r\) can be \(w\downarrow0\), where the integrand is asymptotic to \(\eta^r w^{-r}\). Consequently
\[
 \mathbb E|1-\eta/W|^r<\infty\quad\Longleftrightarrow\quad r<\ell/2.
\]
At equality the integrand-density product is asymptotic to a positive multiple of \(1/w\), so divergence includes the boundary. The neighborhood of \(w=\eta\) causes no singularity, and the gamma density controls infinity. For positive integers \(j<\ell/2\), integration gives
\[
 \mathbb EW^{-j}=\frac{\ell^j}{\prod_{a=1}^j(\ell-2a)}.
\]

**2. Conditional refresh partitions.** Set \(M(w)=1-\eta/w\). Conditional on any prescribed pattern of refreshes among the \(k-1\) possible opportunities, the \(k\) iteration factors split into independent blocks of lengths \(r_1,\ldots,r_m\ge1\), with \(\sum r_i=k\). The absolute error power then factors exactly as
\[
 \mathbb E[|x_k|^q\mid r_1,\ldots,r_m]=|x_0|^q\prod_{i=1}^{m}\mathbb E|M(W)|^{qr_i},
\]
where all factors are nonnegative, and the identity remains valid in the extended nonnegative reals. By Step 1 this conditional moment is finite precisely when \(\ell>2q\max_i r_i\). If \(p=1\), all block lengths equal one, yielding its criterion. If \(0<p<1\), the all-retention pattern has probability \((1-p)^{k-1}>0\), has a block of length \(k\), and forces divergence when \(\ell\le2qk\). Conversely \(\ell>2qk\) makes the moments finite for all possible blocks; there are finitely many patterns at each fixed \(k\), so their mixture is finite. This proves both equivalences and the precise equality cases.

For deterministic periodic refresh with block size \(B\), the first block through iteration \(k\) has length \(\min\{B,k\}\), and no other block is longer. The same factorization establishes the periodic criterion for every \(k\), and in particular a uniform-in-horizon integrability condition \(\ell>2qB\).

**3. Exact mean-square decay under full refresh.** At \(\ell>4\), the first two inverse moments are \(\mathbb EW^{-1}=\ell/(\ell-2)\) and \(\mathbb EW^{-2}=\ell^2/((\ell-2)(\ell-4))\). Therefore the one-step expected squared multiplier is
\[
 \rho(\eta)=1-\frac{2\eta\ell}{\ell-2}+\frac{\eta^2\ell^2}{(\ell-2)(\ell-4)}.
\]
This strictly convex quadratic is minimized at \(\eta=(\ell-4)/\ell\), where \(\rho=2/(\ell-2)<1\). Full independence now gives the exact \(k\)-step formula. The \(\ell=6\) two-step example follows from Steps 1–2; no approximation or Monte Carlo extrapolation is involved.

**4. Almost-sure rate under Bernoulli and periodic refresh.** For \(p>0\), \((W_t)\) is a stationary ergodic Markov chain with invariant law \(\chi^2_\ell/\ell\), because at each transition an independent reset occurs with positive probability. The function \(g(w)=\log|1-\eta/w|\) is integrable: it has only logarithmic singularities near \(w=0\) and \(w=\eta\), and it decays at infinity. As \(M(W_t)\ne0\) almost surely, the ergodic theorem gives
\[
 k^{-1}\log|x_k/x_0|=k^{-1}\sum_{t=0}^{k-1}g(W_t)\longrightarrow\mathbb Eg(W)
\]
almost surely. Jensen's inequality and Step 3 show
\[
 \mathbb Eg(W)=\tfrac12\mathbb E\log|M(W)|^2\le\tfrac12\log\mathbb E|M(W)|^2
 =\tfrac12\log\frac2{\ell-2}<0.
\]
The limit is therefore finite and negative and cannot depend on \(p\). Under periodic refresh, apply the strong law to independent complete blocks, each contributing \(B g(W)\); the remainder is at most \(B-1\) terms and vanishes after division by \(k\), yielding the same exponent. This completes the proof.

## Verification

The accompanying standalone `verify.py` uses only Python's standard-library `fractions` and `math`. It reconstructs the inverse chi-square moment formula, forms exact rational even-power block moments, checks the first- and second-moment identities, and verifies across \(\ell=5,\ldots,28\), horizons up to eight, and block partitions that the algebra matches the analytically established cutoff. The verifier returns 1,275 successful exact-rational tests. This finite sweep is a cross-check, not the proof of the all-parameter theorem; in particular, nonintegrability and almost-sure ergodicity are established analytically in the proof above. Run `python verify.py` from a directory containing that standalone file.

## Relationship to prior work

Pilanci and Wainwright introduced the iterative Hessian sketch with independently sampled sketches and high-probability solution-error analysis [1]. Lacotte and Pilanci explicitly distinguished a single fixed preconditioner from independent fresh preconditioners, giving an exact expected-error formula and optimal steps for the latter, including inverse-sketch moments [2, Section 4 and Theorem 4.1]. Wang, Ouyang and Xu considered iterative double sketching with nested or sequentially related sketches and asymptotic conditional prediction-error guarantees [3]. These works supply the optimization setting, not the stated Bernoulli-retention versus deterministic capped-refresh moment trichotomy and its independent-of-refresh almost-sure exponent. The existing fresh-sketch mean-rate formula is credited, not claimed as new.

The novelty claim is limited to the exact joint refresh-run/moment cutoff, its sharp boundary, and coexistence with the same almost-sure rate for all positive Bernoulli refresh probabilities, with periodic bounded-reuse as a precise integrability comparison. Prior work on inverse-Wishart tails and repeated-sketch moments is related, and undiscovered equivalent specializations remain a residual priority risk.

## Limitations

No assertion is made that a practical floating-point implementation encounters literal infinite measured error, or that typical realizations are numerically unstable. No high-dimensional matrix or nonlinear objective convergence theorem, or advantage in elapsed runtime, follows. The known IID rate is not presented as novel. Adaptive, data-dependent, or robust/truncated preconditioners can invalidate the specific tail clock. The exact boundary concerns scalar Gaussian sketches with full inverse preconditioning and a fixed positive step; it does not apply automatically to bounded-spectrum embeddings, safeguarded line searches, or regularized inverse Hessians. The calculation does not replace independent mathematical validation or a comprehensive priority examination.

## References

[1] M. Pilanci and M. J. Wainwright, *Iterative Hessian Sketch: Fast and Accurate Solution Approximation for Constrained Least-Squares*, JMLR 17 (2016), 1–38. https://jmlr.org/papers/v17/14-460.html

[2] J. Lacotte and M. Pilanci, *Faster Least Squares Optimization*, arXiv:1911.02675, first posted 2019-11-06, Section 3 (fixed sketch) and Section 4 (independently refreshed sketches). https://arxiv.org/abs/1911.02675

[3] R. Wang, Y. Ouyang and W. Xu, *Iterative Double Sketching for Faster Least-Squares Optimization*, ICML/PMLR 162 (2022), 22935–22963. https://proceedings.mlr.press/v162/wang22t.html
