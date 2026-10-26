# Unbounded multiplicity of local reset-rate optima in a Brownian search

## Finding
For **every integer** \(N\ge 1\), a one-dimensional Brownian search with exactly \(N\) positive resetting locations can have **at least \(N\) distinct strict local minima** of its mean first-passage time as a function of the single total Poisson resetting rate. The same objective then has at least \(N-1\) strict local maxima separating these minima.

An explicit construction works at every \(N\): with diffusion coefficient \(D=1\), absorbing target at \(0\), and initial position \(1\), choose
\[
 a_j=1000^j,\qquad p_j=\frac{a_j}{\sum_{i=0}^{N-1}a_i},\qquad 0\le j<N.
\]
At each Poisson resetting event, independently choose location \(a_j\) with probability \(p_j\). If \(M_N(r)\) denotes the mean absorption time at total rate \(r>0\), then for each \(0\le j<N\), the interval
\[
 I_j=\left(\frac{1}{4a_j^2},\frac{4}{a_j^2}\right)
\]
contains a strict local minimizer of \(M_N\). These \(N\) intervals are pairwise disjoint. Between consecutive intervals there is at least one strict local maximum. This is an **existence theorem for local optima**; it does not assert that the \(N\) minima have equal height or are all global optima.

## Assumptions and scope
The process is standard one-dimensional Brownian diffusion \(dX_t=\sqrt{2}\,dB_t\) on \((0,\infty)\), absorbed on first reaching \(0\). It begins at \(X_0=1\), and while unabsorbed is reset instantaneously at Poisson rate \(r>0\). Each reset independently selects one of the \(N\) sites \(a_j\) using fixed probabilities \(p_j\); these probabilities do not vary with \(r\). Brownian paths and reset choices are mutually independent. The result holds for every finite integer \(N\ge1\), including arbitrarily large \(N\), but makes no claim about a single infinite-site measure. Rescaling physical time replaces \(r\) by \(r/D\) for any desired constant diffusivity \(D>0\).

## Proof
**1. First-passage renewal transform.** For free Brownian motion started at \(x>0\), the Laplace transform of its first-hitting-time distribution is \(e^{-x\sqrt{s}}\). Therefore its survival transform is \(q_0(s\mid x)=(1-e^{-x\sqrt{s}})/s\). The first-reset decomposition, followed by a Laplace transform, gives the survival transform of the reset process,
\[
 q_r(s)=\frac{q_0(s+r\mid1)}{1-r\sum_{j=0}^{N-1}p_j q_0(s+r\mid a_j)}
 =\frac{1-e^{-\sqrt{s+r}}}{s+r\sum_{j=0}^{N-1}p_j e^{-a_j\sqrt{s+r}}}.
\]
Its value at \(s=0\) is finite and equals the mean absorption time. Put \(u=\sqrt r\), \(W=\sum_{j=0}^{N-1}a_j\). Then
\[
 F_N(u):=M_N(u^2)=\frac{W(1-e^{-u})}{u^2\sum_{j=0}^{N-1}a_j e^{-a_j u}},\qquad u>0.
\]
This is a positive nonconstant real-analytic function.

**2. A logarithmic derivative.** Define \(h(u)=u/(e^u-1)\) and \(\mu_N(u)=\big(\sum_j a_j^2e^{-a_j u}\big)/\big(\sum_j a_j e^{-a_j u}\big)\). Direct logarithmic differentiation gives the exact identity
\[
 \frac{uF_N'(u)}{F_N(u)}=h(u)-2+u\mu_N(u).
\]
For \(j\in\{0,\ldots,N-1\}\) and \(c\in\{1/2,2\}\), take \(u=c/a_j\). With \(t_i=a_i/a_j=1000^{i-j}\), write
\[
 R_{j,N}(c)=\frac{\sum_{i=0}^{N-1}t_i^2e^{-ct_i}}{\sum_{i=0}^{N-1}t_i e^{-ct_i}},
 \qquad \frac{uF_N'(u)}{F_N(u)}=h(c/a_j)-2+cR_{j,N}(c).
\]

**3. Uniform dominance estimate, valid for every \(N\).** The \(i=j\) term in the denominator of \(R_{j,N}(c)\) is exactly \(e^{-c}\). For \(i<j\), \(t_i\le1/1000\), hence \(|t_i^2-t_i|e^{-ct_i}\le t_i\). For \(i>j\), \(t_i\ge1000\), hence \(|t_i^2-t_i|e^{-ct_i}\le t_i^2e^{-ct_i}\). Consequently,
\[
 |R_{j,N}(c)-1|\le e^c\left(\sum_{m\ge1}1000^{-m}
 +\sum_{m\ge1}1000^{2m}e^{-c1000^m}\right).
\]
Because \(c\ge1/2\), consecutive terms of the second series have ratio at most \(1000^2e^{-(1000-1)1000/2}<1/2\). Hence that series is at most \(2\cdot1000^2e^{-500}\). Using \(e^2<8\) gives the explicit bound
\[
 |R_{j,N}(c)-1|\le e^2\left(\frac1{999}+2\cdot 1000^2e^{-500}\right)<\frac1{100}.
\]
The estimate is uniform in \(j\) and \(N\); no infinite numerical enumeration is used.

**4. Forced alternating derivative signs.** The elementary function \(h\) is strictly decreasing on \((0,\infty)\), with \(0<h(u)<1\). At \(u=1/(2a_j)\), the estimate above yields
\[
 \frac{uF_N'(u)}{F_N(u)}<1-2+\tfrac12(1.01)=-0.495<0.
\]
At \(u=2/a_j\), since \(a_j\ge1\), one has \(h(2/a_j)\ge h(2)=2/(e^2-1)>2/7\), so
\[
 \frac{uF_N'(u)}{F_N(u)}>\frac27-2+2(0.99)>0.
\]
Thus \(F_N\) decreases at the left endpoint and increases at the right endpoint of every interval \((1/(2a_j),2/a_j)\). It achieves an interior local minimum in each closed interval. Since \(F_N\) is nonconstant and real-analytic, at least one such minimum is strict. Distinct intervals are disjoint, because
\[
 \frac{2}{a_{j+1}}=\frac{2}{1000a_j}<\frac{1}{2a_j}.
\]
For each consecutive pair of these intervals, the derivative is positive at the right endpoint of the smaller-\(u\) interval and negative at the left endpoint of the larger-\(u\) interval. The same extreme-value and analyticity argument supplies a strict intervening maximum. Finally, \(r=u^2\) is strictly increasing for \(u>0\), preserving all local extrema and taking \((1/(2a_j),2/a_j)\) to \(I_j\). This proves the claim for all \(N\ge1\).

## Verification
The accompanying standalone Python checker evaluates the normalized logarithmic derivative, verifies the uniform numerical inequalities for \(1\le N\le20\), brackets one derivative zero in each predicted interval, checks their separation, and compares the analytic derivative against centered finite differences of the independently computed log-mean. It reports **1,287 passed assertions**. The proof above, not this finite check, proves the universal quantifier in \(N\).

## Relationship to prior work
Julián-Salgado, Dagdug, and Boyer derive the two-site Brownian resetting mean and its metastable two-minimum regimes, and note that the mean extends to \(N\) sites. That known renewal formula is used as an antecedent here; the new statement is the explicit **unbounded lower bound on the number of distinct local minima**, established by a uniform all-\(N\) separation argument. Besga and collaborators previously observe a metastable local optimum for a Gaussian-distributed reset position, a different distribution and a one-well metastability scenario. Méndez, Flaquer-Galmés, and Campos analyze mean and variance for distributed reset positions but do not establish this all-\(N\) multiplicity theorem. A broader published theorem could still imply the same construction; originality has not been independently audited.

## Limitations
The construction uses exponentially spaced reset locations and increasing weights; it establishes existence of arbitrarily many **local** extrema, not equal-height global minimizers or a full classification of all extrema for a fixed \(N\). It does not optimize over the site locations or probabilities, and does not treat finite-speed returns, position-dependent diffusion, or other restart-time laws. Numerical checks are finite and serve only as reproducibility evidence. No claim of exhaustive scholarly priority is made.

## References
1. P. Julián-Salgado, L. Dagdug, and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897, first submitted 2023-11-20, https://arxiv.org/abs/2311.11897 .
2. B. Besga et al., *Optimal mean first-passage time for a Brownian searcher subjected to resetting: experimental and theoretical results*, arXiv:2004.11311, first submitted 2020-04-21, https://arxiv.org/abs/2004.11311 .
3. V. Méndez, R. Flaquer-Galmés, and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, first submitted 2024-01-02, https://arxiv.org/abs/2401.01125 .
