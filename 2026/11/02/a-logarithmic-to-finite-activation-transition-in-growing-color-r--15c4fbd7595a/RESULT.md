# A logarithmic-to-finite activation transition in growing-color reinforced trees

## Finding

**Theorem.** Start with one vertex of urn weight one. At integer time \(t\ge1\), choose one of the existing \(t\) vertices with probability proportional to its current weight; increase the chosen weight by \(c t^\alpha\), where \(c>0\) and \(\alpha>0\); and then add a new child of the chosen vertex, with urn weight one. Let \(I_n\) be the number of vertices having at least one child after \(n\) steps, and let \(\mu_n=\mathbb E I_n\). Let \(\tau\) be the last time at which the chosen parent had no previous child, with \(\tau=1\) if no such choice occurs after the first step.

1. If \(0<\alpha<1\), then almost surely
   \[
   \frac{I_n}{n^{1-\alpha}}\longrightarrow \frac{\alpha+1}{c(1-\alpha)},
   \]
   and
   \[
   \frac{I_n-\mu_n}{\sqrt{\mu_n}}\Longrightarrow N(0,1),\qquad
   \operatorname{Var}(I_n)\sim\mu_n\sim \frac{\alpha+1}{c(1-\alpha)}n^{1-\alpha}.
   \]
2. If \(\alpha=1\), then almost surely \(I_n/\log n\to2/c\), and the same centered normal limit holds with
   \[
   \mu_n=\frac2c\log n+O(1),\qquad
   \operatorname{Var}(I_n)\sim\frac2c\log n.
   \]
3. If \(\alpha>1\), then \(I_n\uparrow I_\infty<\infty\) almost surely. The probability that *only the initial vertex ever becomes a parent* is strictly positive and exactly
   \[
   \Pr(I_\infty=1)=\prod_{t=2}^\infty\left(1-\frac{t-1}{t+c\sum_{j=1}^{t-1}j^\alpha}\right).
   \]
   The last activation has the sharp heavy tail
   \[
   \Pr(\tau>n)\sim\frac{\alpha+1}{c(\alpha-1)}\,n^{1-\alpha}.
   \]
   In particular, for any real \(s>0\), \(\mathbb E\tau^s<\infty\) if and only if \(s<\alpha-1\).

For \(0<\alpha\le1\), infinitely many distinct vertices become parents almost surely and the probability of an eternal star is zero. Thus \(\alpha=1\) is the sharp boundary between indefinitely increasing and almost surely finite numbers of activated parent vertices.

## Assumptions and scope

All weights are positive real numbers and every step uses the current urn weights *before* the new vertex is inserted. The attachment graph is rooted at the initial vertex; parenthood refers to having at least one child and ignores any initial graphical self-loop convention. The exponent \(\alpha\) and coefficient \(c\) are fixed as the number of steps tends to infinity. The random variables of interest are the count of vertices selected at least once as parents and the last time a previously unselected vertex is first selected. No claim about a unique maximal-degree vertex or the number of infinite-degree vertices is made.

## Proof

**Exact reduction.** Set
\[
S_{t-1}=t+c\sum_{j=1}^{t-1}j^\alpha.
\]
Exactly \(t-I_{t-1}\) of the \(t\) living vertices have never been chosen as parents. Each still has weight exactly one: its weight can increase only when it is chosen. Therefore, if \(Y_t\) is the indicator that time \(t\) chooses a hitherto childless vertex, then
\[
I_0=0,\quad I_t=I_{t-1}+Y_t,\quad
p_t:=\Pr(Y_t=1\mid\mathcal F_{t-1})=\frac{t-I_{t-1}}{S_{t-1}}.
\]
These are exact identities for the full urn process. With \(q_t=t/S_{t-1}\), the deterministic growth law is
\[
S_{t-1}\sim\frac{c}{\alpha+1}t^{\alpha+1},\qquad
q_t\sim\frac{\alpha+1}{c}t^{-\alpha}.
\]
Writing \(\mu_t=\mathbb E I_t\) and \(v_t=\operatorname{Var}(I_t)\) gives exact recursions
\[
\mu_t=\left(1-\frac1{S_{t-1}}\right)\mu_{t-1}+\frac{t}{S_{t-1}},
\]
\[
 b_t=\frac{t-\mu_{t-1}}{S_{t-1}},\qquad
 v_t=\left(1-\frac2{S_{t-1}}\right)v_{t-1}+b_t(1-b_t),
\]
with \(\mu_0=v_0=0\). The variance identity follows from \(\operatorname{Cov}(I_{t-1},Y_t)=-v_{t-1}/S_{t-1}\) and the fact that the unconditional variable \(Y_t\) is Bernoulli with mean \(b_t\).

**The divergent regime.** Put \(\Lambda_n=\sum_{t=1}^n q_t\) and \(\xi_t=Y_t-p_t\). For \(0<\alpha\le1\), \(\Lambda_n\to\infty\), with
\[
\Lambda_n\sim\begin{cases}
\dfrac{\alpha+1}{c(1-\alpha)}n^{1-\alpha},&0<\alpha<1,\\
\dfrac2c\log n,&\alpha=1.
\end{cases}
\]
Since \(\mu_{t-1}\le\Lambda_{t-1}\),
\[
0\le\Lambda_n-\mu_n=\sum_{t=1}^n\frac{\mu_{t-1}}{S_{t-1}}
\le\sum_{t=1}^n q_t\frac{\Lambda_{t-1}}t=o(\Lambda_n),
\]
where the last step is the weighted Cesàro lemma, using \(\Lambda_{t-1}/t\to0\). At the endpoint \(\alpha=1\), this correction is bounded because \(\sum_t (\log t)/t^2<\infty\), and the harmonic asymptotic for \(q_t\) has a bounded remainder.

Let \(M_n=\sum_{t\le n}\xi_t\). Its conditional quadratic variation is bounded by \(\Lambda_n\). The convergent series \(\sum_t q_t/\Lambda_t^2<\infty\) implies \(M_n/\Lambda_n\to0\) almost surely by martingale convergence and Kronecker's lemma. As
\[
I_n=\Lambda_n-\sum_{t\le n}\frac{I_{t-1}}{S_{t-1}}+M_n\le\Lambda_n+M_n,
\]
we have \(I_n=O(\Lambda_n)\) almost surely, and hence \(\sum_{t\le n}I_{t-1}/S_{t-1}=o(\Lambda_n)\) by the same weighted Cesàro argument. This proves the almost-sure limits.

For the central limit theorem, center \(E_n=I_n-\mu_n\). The exact recursion yields
\[
E_n=\sum_{t=1}^n a_{t,n}\xi_t,\qquad
a_{t,n}=\prod_{j=t+1}^n\left(1-\frac1{S_{j-1}}\right).
\]
Since \(\sum_j 1/S_{j-1}<\infty\) for every \(\alpha>0\), the weights are in \([0,1]\) and approach one uniformly on late time intervals. Furthermore,
\[
0\le \Lambda_n-\sum_{t\le n}p_t(1-p_t)
\le\sum_{t\le n}\frac{I_{t-1}}{S_{t-1}}+\sum_{t\le n}q_t^2.
\]
The expectation of the right side is \(o(\Lambda_n)\): use the preceding bound on \(\mu_{t-1}\) and \(q_t\to0\). The deterministic weights do not change the leading quadratic variation, because \(a_{t,n}\to1\) uniformly for all sufficiently late \(t\), and the early contribution is bounded as \(n\to\infty\). Thus the predictable quadratic variation of the normalized martingale array converges to one in probability. Its increments are bounded by \(1/\sqrt{\Lambda_n}\), so Lindeberg holds. The martingale central limit theorem proves \(E_n/\sqrt{\Lambda_n}\Rightarrow N(0,1)\). The same orthogonal-increment representation gives \(v_n/\Lambda_n\to1\), establishing the stated variance scale.

**The summable regime and last-activation tail.** If \(\alpha>1\), then \(\sum_t q_t<\infty\); in particular \(\mathbb E I_\infty\le\sum_t q_t<\infty\), implying \(I_\infty<\infty\) almost surely. Let \(H_n=\sum_{t>n}Y_t\). Because \(\sup_t\mathbb E I_t<\infty\),
\[
\mathbb E H_n=\sum_{t>n}q_t-\sum_{t>n}\frac{\mathbb E I_{t-1}}{S_{t-1}}
\sim\frac{\alpha+1}{c(\alpha-1)}n^{1-\alpha},
\]
where the second sum is \(O(n^{-\alpha})\). For \(s<t\),
\[
\Pr(Y_s=Y_t=1)=\mathbb E(Y_s p_t)\le q_t\mathbb E Y_s\le q_s q_t.
\]
Consequently the sum of all pair probabilities with \(s,t>n\) is at most \((\sum_{t>n}q_t)^2/2=o(\mathbb E H_n)\). First- and second-order Bonferroni inequalities show \(\Pr(\tau>n)=\Pr(H_n\ge1)\sim\mathbb E H_n\). The power-moment criterion follows by tail integration. Finally, the event \(I_\infty=1\) means every choice after the deterministic first step selects the initial vertex. Conditional on surviving as a star through time \(t-1\), the initial vertex has all the urn weight except that of the \(t-1\) unselected leaves, giving the displayed infinite product. It is strictly positive exactly when \(\sum_t (t-1)/S_{t-1}<\infty\), namely when \(\alpha>1\).

## Verification

The standalone file `checker.py` independently enumerates full labeled urn-weight histories and compares their exact rational parent-count distributions against the reduced one-dimensional chain. It additionally validates the exact mean and variance recurrences and evaluates the asymptotic scales numerically in several parameter regimes. The code is finite evidence supporting the algebraic reduction; the almost-sure, Gaussian and tail statements are established by the arguments above, not by numerical extrapolation.

## Relationship to prior work

Singh, Alajaji and Gharesifard introduced the expanding-color reinforcement tree and gave marginal distributions for the draw count of each individual color. These marginals in principle determine expected activation counts by summation but do not determine the joint fluctuation law, the last-activation tail or the full activation transition. Time-dependent two-color urn monopolies (Sidorova) and degree-superlinear attachment condensation (Sethuraman and Venkataramani) concern different processes; neither supplies the deterministic-new-color, time-power-reinforced parent-activation theorem. Time-dependent triggering-urn novelty counts (Bellina, De Marzo and Loreto) add colors conditionally on first occurrences rather than at every draw. The result here concerns deterministic color immigration and first-use counts, not a reparameterization of that triggering rule.

## Limitations

The theorem requires a fixed positive polynomial reinforcement exponent and one fresh color of initial weight one at every step. It does not cover feedback weights that depend nonlinearly on current degree, conditional color creation, random reinforcement, or changing exponents. The finite-active-vertex statement does not imply a unique hub or monopoly by a particular vertex. Broader historical priority beyond the inspected literature is not independently certified.

## References

1. S. Singh, F. Alajaji and B. Gharesifard, *Generating Preferential Attachment Graphs via a Pólya Urn with Expanding Colors*, first public preprint 2023-08-20, arXiv:2308.10197, https://arxiv.org/abs/2308.10197.
2. N. Sidorova, *Time-dependent Pólya urn*, first public preprint 2018-07-12, arXiv:1807.04844, https://arxiv.org/abs/1807.04844.
3. S. Sethuraman and S. C. Venkataramani, *On the growth of a superlinear preferential attachment scheme*, first public preprint 2017-04-19, arXiv:1704.05568, https://arxiv.org/abs/1704.05568.
4. W. M. Ruszel and D. Thacker, *Positive Reinforced Generalized Time-Dependent Pólya Urns via Stochastic Approximation*, Journal of Theoretical Probability (2024), https://doi.org/10.1007/s10959-024-01366-w.
5. A. Bellina, G. De Marzo and V. Loreto, *Full spectrum of novelties in time-dependent urn models*, Physical Review Research (2025), https://doi.org/10.1103/PhysRevResearch.7.023127.
