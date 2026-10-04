# Exact finite-sample risk inflation in two-item synthetic BTL augmentation
## Finding
For a fully observed two-item Bradley--Terry--Luce comparison, the sufficient statistic is a Bernoulli win count. Let \(m\ge 1\) comparisons be added at every round. Write \(p_\star\in[0,1]\) for the real win probability, let \(S_0\sim\operatorname{Binomial}(m,p_\star)\), and define \(P_1=S_0/m\). At each synthetic round \(t\ge1\), conditionally on the accumulated data, generate \(S_t\sim\operatorname{Binomial}(m,P_t)\) and refit on all data, so
\[
P_{t+1}=\frac{tP_t+S_t/m}{t+1}.
\]
Then for every \(t\ge1\),
\[
\mathbb E[(P_t-p_\star)^2]=p_\star(1-p_\star)\left[1-\prod_{k=1}^t\left(1-\frac{1}{mk^2}\right)\right].
\]
Moreover, conditionally on \(P_1=x\),
\[
\mathbb E[P_t\mid P_1=x]=x,
\qquad
\operatorname{Var}(P_t\mid P_1=x)=x(1-x)\left[1-\prod_{k=2}^t\left(1-\frac{1}{mk^2}\right)\right].
\]
Thus the accumulated synthetic rounds do not self-correct the realized first-round estimate; they add a precisely quantifiable amount of dispersion.

The bounded martingale converges almost surely and in \(L^2\) to \(P_\infty\), with
\[
\mathbb E[(P_\infty-p_\star)^2]
=p_\star(1-p_\star)\left[1-\frac{\sin(\pi/\sqrt m)}{\pi/\sqrt m}\right].
\]
Relative to the real-only MLE risk \(p_\star(1-p_\star)/m\), the exact infinite-round inflation is
\[
R_m=m\left[1-\frac{\sin(\pi/\sqrt m)}{\pi/\sqrt m}\right]
<\frac{\pi^2}{6},
\]
and
\[
R_m=\frac{\pi^2}{6}-\frac{\pi^4}{120m}+O(m^{-2}).
\]
The known \(\pi^2/6\) augmentation constant therefore appears as the large-\(m\) limit of an exact finite-sample Bernoulli/BTL formula, rather than only as a square-summability upper bound or a fixed-generation asymptotic variance.

## Assumptions and scope
The result concerns the two-item, fully observed specialization of the iterative accumulated-data BTL construction: the comparison edge is always present and each round contributes the same number \(m\) of independent pairwise outcomes. The parameter is written as the win probability \(P_t\), which is the natural closure of the two-item logistic parameterization. If one insists on finite log-odds, the argument applies pathwise whenever the initial real batch contains at least one win and one loss; such a batch keeps every accumulated empirical probability strictly between zero and one. The closed parameterization also includes the two degenerate initial batches, where the recursion remains mathematically well defined.

The claim is about estimation error in the win-probability parameter. It does not assert an exact finite-sample law for the log-odds score, for more than two items, for sparse random comparison graphs, or for unequal batch sizes.

## Proof
Let \(\mathcal F_t\) contain the real batch and the first \(t-1\) synthetic batches, so \(P_t\) is \(\mathcal F_t\)-measurable. Because \(\mathbb E[S_t/m\mid\mathcal F_t]=P_t\),
\[
\mathbb E[P_{t+1}\mid\mathcal F_t]=P_t.
\]
Hence \((P_t)\) is a bounded martingale. Its conditional variance increment is
\[
\operatorname{Var}(P_{t+1}\mid\mathcal F_t)
=\frac{P_t(1-P_t)}{m(t+1)^2}.
\]
Since the conditional mean is \(P_t\), the identity \(\mathbb E[X(1-X)]=\mu(1-\mu)-\operatorname{Var}(X)\), applied conditionally, gives
\[
\mathbb E[P_{t+1}(1-P_{t+1})\mid\mathcal F_t]
=P_t(1-P_t)\left(1-\frac{1}{m(t+1)^2}\right).
\]
Writing \(h_t=\mathbb E[P_t(1-P_t)]\), the real first round has
\[
h_1=p_\star(1-p_\star)\left(1-\frac1m\right),
\]
so induction yields
\[
h_t=p_\star(1-p_\star)\prod_{k=1}^t\left(1-\frac{1}{mk^2}\right).
\]
The martingale has \(\mathbb E[P_t]=p_\star\), and therefore
\[
\operatorname{Var}(P_t)=p_\star(1-p_\star)-h_t,
\]
which proves the finite-round MSE formula. Starting instead from a fixed \(P_1=x\) removes the \(k=1\) factor and gives the conditional variance formula.

Bounded martingale convergence gives an almost-sure and \(L^2\) limit. Euler's sine product
\[
\frac{\sin(\pi z)}{\pi z}=\prod_{k=1}^\infty\left(1-\frac{z^2}{k^2}\right)
\]
with \(z=1/\sqrt m\) gives the displayed limiting MSE. Finally, \(\sin x>x-x^3/6\) for \(x>0\), so \(R_m<\pi^2/6\). Expanding \(\sin x/x\) at \(x=0\) gives
\[
R_m=\frac{\pi^2}{6}-\frac{\pi^4}{120m}+O(m^{-2}).
\]

## Verification
The standalone script `verify.py` performs exact-rational state propagation for several finite \((m,t)\) pairs, checks the martingale mean and the exact variance product both unconditionally and conditionally on an initial MLE, and numerically checks the Euler-product limit and the strict \(\pi^2/6\) bound. It terminates with `VERIFY_OK` when all checks pass.

## Relationship to prior work
Jin and Yu, arXiv:2609.32987, introduce the recent BTL accumulation setting used here: each round adds fresh comparisons generated from the current fitted BTL model, and the next MLE uses all accumulated rounds. Their theory gives high-dimensional nonasymptotic rates and asymptotic normality, not this two-item exact finite-sample risk identity.

Gerstgrasser et al., arXiv:2404.01413, obtain an exact \(\sum_{k\le t}k^{-2}\) test-error law for an accumulated linear-regression model. Dey and Donoho, arXiv:2410.22812, show that the same \(\pi^2/6\) pathway is asymptotically universal across a broad exponential-family/AAL class: for fixed generation and large per-generation sample size, the asymptotic variance inflation is \(\sum_{k\le t}k^{-2}\). Barzilai and Shamir, arXiv:2505.19046, establish nonasymptotic consistency bounds for general iterative MLE and use the same square-summability mechanism in concentration arguments.

The present statement does not re-claim square summability or the \(\pi^2/6\) asymptotic constant. Its content is the exact Bernoulli/BTL finite-sample product law, its exact infinite-round sine-product value, the strict finite-\(m\) correction, and the conditional no-self-correction identity.

## Limitations
The exact product is special to the two-item Bernoulli sufficient statistic with equal batch sizes. It does not by itself control score-space error near probabilities zero or one, and it does not extend automatically to coupled multi-item BTL likelihoods or random missing comparison edges. The supporting general exponential-family literature is asymptotic or bound-based; the new finite-sample calculation should be viewed as a sharp benchmark rather than a general replacement for those results.

## References
Y. Jin and M. Yu, “Maximum Likelihood Estimation for Entity Ranking under Iterative Synthetic Data Augmentation,” arXiv:2609.32987, first public version 2026-09-26.

M. Gerstgrasser et al., “Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data,” arXiv:2404.01413.

A. Dey and D. Donoho, “Universality of the \(\pi^2/6\) Pathway in Avoiding Model Collapse,” arXiv:2410.22812.

D. Barzilai and O. Shamir, “When Models Don't Collapse: On the Consistency of Iterative MLE,” arXiv:2505.19046.
