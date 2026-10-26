# Five observations are the sharp cutoff for stable miscoordination under heterogeneous sampling

## Finding

In the one-population, symmetric, two-action sampling-best-response coordination game of Arigapudi, Heller and Schreiber, with favorable tie-breaking as specified below, the **smallest possible maximum sample size** permitting an asymptotically stable interior population state is **five**, among all payoff ratios \(u>1\) and all finite distributions of positive integer sample sizes. In particular, no distribution supported on \(\{1,2,3,4\}\) has an asymptotically stable interior stationary state.

This cutoff is attained without any agents sampling more than five opponents. For every payoff ratio \(1<u<3/2\), let a proportion \(\alpha\in[0,1]\) of revising agents observe two opponents and the remaining proportion \(1-\alpha\) observe five. Set
\[
\alpha_c=\frac{7\sqrt7}{18+7\sqrt7}=\frac{343-126\sqrt7}{19}\approx0.507122884519.
\]
There is an asymptotically stable interior stationary state **if and only if**
\[
\boxed{\frac12<\alpha<\alpha_c.}
\]
Precisely in this interval there are two interior stationary states \(0<p_s<p_u<1\): \(p_s\) is asymptotically stable, \(p_u\) is unstable, and the pure state \(p=1\) remains asymptotically stable. Every trajectory beginning in \((0,p_u)\) converges to \(p_s\), and every trajectory beginning in \((p_u,1]\) converges to \(1\). The endpoints \(0,1\) and the separator \(p_u\) are stationary. At the critical value \(\alpha=\alpha_c\), the two interior states merge into a non-asymptotically-stable double root.

Thus a narrow, explicit population-composition interval permits persistent mixing when the largest observational sample has size five, whereas every mixture of sample sizes at most four rules it out for all \(u>1\). “Miscoordination” means that an interior state assigns positive mass to both actions, so randomly matched agents sometimes choose different actions. It does not assert that the interior state is a Nash equilibrium of the underlying complete-information stage game.

## Assumptions and scope

There is a unit mass of agents repeatedly matched in a symmetric coordination game. The payoff is \(u>1\) to each player for mutual play of action \(a\), payoff \(1\) for mutual play of \(b\), and payoff \(0\) for mismatched play. At independent unit-rate revision opportunities, each agent draws a sample size \(k\ge1\) from a fixed distribution \(\theta\), observes \(k\) independent draws from the current population, and best responds to the empirical action frequencies. A payoff tie is resolved in favor of \(a\). No endogenization or learning of the sample-size distribution is assumed.

Write \(p(t)\in[0,1]\) for the mass playing \(a\), and
\[
F_{k,m}(p)=\sum_{j=m}^k\binom{k}{j}p^j(1-p)^{k-j},\qquad m_k=\left\lceil\frac{k}{1+u}\right\rceil.
\]
The deterministic mean-field equation is
\[
\dot p=w(p)-p,\qquad w(p)=\sum_{k\ge1}\theta(k)F_{k,m_k}(p).
\]
The sum is finite. Both pure states are stationary, and the vector field is a polynomial, hence solutions are unique and remain in \([0,1]\). An interior stationary state is asymptotically stable in the standard two-sided Lyapunov/attraction sense relative to \([0,1]\).

## Proof

**Step 1: exact low-sample response polynomials.** For \(k\le4\) and \(u>1\), favorable tie-breaking produces thresholds \(m_1=m_2=1\),
\[
m_3=\begin{cases}2,&1<u<2,\\1,&u\ge2,\end{cases}\qquad
m_4=\begin{cases}2,&1<u<3,\\1,&u\ge3.\end{cases}
\]
For each nontrivial sample, define \(h_{k,m}\) by
\[
F_{k,m}(p)-p=p(1-p)h_{k,m}(p).
\]
Direct binomial expansion gives the complete relevant table:
\[
\begin{aligned}
h_{1,1}(p)&=0,&h_{2,1}(p)&=1,\\
h_{3,2}(p)&=2p-1,&h_{3,1}(p)&=2-p,\\
h_{4,2}(p)&=-3p^2+5p-1,&h_{4,1}(p)&=3-3p+p^2.
\end{aligned}
\]
If \(1<u<3\), the polynomial
\[
h(p)=\sum_{k=1}^4\theta(k)h_{k,m_k}(p)
\]
is concave on \([0,1]\): its only quadratic term is \(-3\theta(4)p^2\). Moreover, \(h(1)=1-\theta(1)\). If \(\theta(1)<1\), concavity and \(h(1)>0\) imply that \(h\) cannot cross from positive to negative as \(p\) increases through an interior zero. Indeed, for any \(p_0<1\) with \(h(p_0)=0\), the chord inequality gives \(h(q)\ge(q-p_0)h(1)/(1-p_0)>0\) for all \(p_0<q<1\). Since \(\dot p=p(1-p)h(p)\), no interior stationary point attracts from both sides. If \(\theta(1)=1\), then \(\dot p\equiv0\), and no individual interior state is asymptotically attracting. For \(u\ge3\), all \(h_{k,m_k}(p)\) for \(k=2,3,4\) are strictly positive on \((0,1)\), so again there is no asymptotically stable interior state. This proves the universal four-observation exclusion, including \(u=2\) and \(u=3\).

**Step 2: the first attainable case.** Fix \(1<u<3/2\). A two-agent sample selects \(a\) if at least one sampled agent plays \(a\), whereas a five-agent sample requires at least three \(a\)'s. Therefore
\[
F_{2,1}(p)=2p-p^2,\qquad F_{5,3}(p)=10p^3-15p^4+6p^5.
\]
With \(\theta(2)=\alpha\), \(\theta(5)=1-\alpha\), a direct factorization is
\[
\dot p=p(1-p)H_\alpha(p),\qquad
H_\alpha(p)=2\alpha-1-(1-\alpha)\Phi(p),
\]
where \(\Phi(p)=6p^3-9p^2+p\). Differentiation gives
\[
\Phi'(p)=18p^2-18p+1,
\quad p_-=\frac{3-\sqrt7}{6},\quad p_+=\frac{3+\sqrt7}{6}.
\]
The function \(\Phi\) increases from \(0\) to its unique maximum \(M=\Phi(p_-)=7\sqrt7/18-1>0\), then decreases until \(p_+\), and increases to \(\Phi(1)=-2\). Its only positive zero in \((0,1)\), apart from \(0\), is \((9-\sqrt{57})/12\), which lies strictly between \(p_-\) and \(p_+\).

For \(\alpha>1/2\), both \(H_\alpha(0)=2\alpha-1\) and \(H_\alpha(1)=1\) are positive. The function \(H_\alpha\) has an interior minimum at \(p_-\) and is negative there precisely when
\[
2\alpha-1<(1-\alpha)M
\quad\Longleftrightarrow\quad
\alpha<\frac{1+M}{2+M}=\alpha_c.
\]
When this strict inequality holds, monotonicity of \(\Phi\) on either side of \(p_-\) and its sign beyond its positive zero show there are exactly two interior zeros, both below \((9-\sqrt{57})/12\). As \(p\) increases, the sign pattern of \(\dot p\) is \(+,-,+\) across the three open subintervals delimited by the zeros. The first root is attracting from both sides, the second repelling, and \(1\) attracting. Uniqueness of solutions in one dimension yields the stated basins.

For \(\alpha\ge\alpha_c\), \(H_\alpha\ge0\) on \([0,1]\), with only a nonnegative double-zero at \(p_-\) when equality holds; hence no interior point attracts from both sides. For \(\alpha\le1/2\), \(H_\alpha\) is negative just to the right of \(0\), is increasing on \((p_-,p_+)\), and is strictly positive at \(p_+\) and \(1\). It therefore has exactly one interior sign change, from negative to positive, which is repelling. This completes the if-and-only-if assertion and proves that five is the smallest attainable maximum sample size.

## Verification

The accompanying standard-library Python program `check_sampling.py` verifies, by exact rational arithmetic, the five low-sample binomial factorization identities, the two-versus-five factorization, the two strict stationary-point brackets at \(\alpha=503/1000\), and rational-squared comparisons enclosing the critical mixing proportion. Polynomial identities of degree at most five are checked at six distinct rational points, which is sufficient to establish those identities exactly. The four-sample concavity argument and cubic root-count argument are the analytical proof; their infinite quantifiers do not follow from the program's finite checks.

For the rational witness \(\alpha=503/1000\), the stable stationary point belongs to \((137/10000,138/10000)\) and the unstable stationary point belongs to \((1059/10000,1060/10000)\); both brackets are certified by exact sign evaluations. One can run the program with `python check_sampling.py`, with no third-party dependencies.

## Relationship to prior work

Arigapudi, Heller and Schreiber formulate the precise one-population sampling dynamics, prove that homogeneous sample sizes do not permit stable interior miscoordination (their Theorem 1), and prove that heterogeneity with sufficiently large samples can create stable interior states (their Theorem 2). They compare these results to earlier equilibrium-selection conditions of Oyama, Sandholm and Tercieux. Their results do not supply a sharp maximum-sample cutoff or the exact first-attainable two-versus-five mixture interval derived here. In particular, their broad heterogeneity-existence statement does not itself imply that five observations are sufficient or that four are impossible.

Oyama, Sandholm and Tercieux prove sufficient dominance-based global-selection conditions for random sample sizes, not the two-sided interior-stability minimality and exact saddle-node window here. The subsequent study by Izquierdo and Izquierdo focuses on the stability of pure equilibria and inference protocols; its section on mixed sample sizes does not state this finite minimality result.

## Limitations

The theorem concerns the deterministic infinite-population sampling-best-response flow, the symmetric two-action payoff matrix specified above, fixed sample-size distributions and tie-breaking in favor of \(a\). The universal exclusion is proved only for \(u>1\), and the explicit five-observation witness is proved for \(1<u<3/2\). Nothing here classifies alternative inference procedures, heterogeneous payoffs, more actions, finite-population stochastic fluctuations, endogenous sample sizes or the global dynamics of all larger-sample distributions. The equilibrium is stable in population dynamics, not necessarily a Nash equilibrium of the original game. No claim of independent validation or exhaustive bibliographic completeness is made.

## References

1. S. Arigapudi, Y. Heller, A. Schreiber, *Heterogeneous Noise and Stable Miscoordination*, arXiv:2305.10301, first posted 17 May 2023; full author text and appendices, version 2, 25 January 2025. https://arxiv.org/html/2305.10301v2
2. D. Oyama, W. H. Sandholm, O. Tercieux, *Sampling Best Response Dynamics and Deterministic Equilibrium Selection*, *Theoretical Economics* 10 (2015), 243–281, DOI:10.3982/TE1405. https://www.oyama.e.u-tokyo.ac.jp/papers/sBRD.140328.pdf
3. S. S. Izquierdo and L. R. Izquierdo, *Statistical Inference in Games: Stability of Pure Equilibria*, open author manuscript, sections 1 and 3.6. https://www.segis.izqui.org/files/Izquierdo_Statistical_Inference_Stability.pdf
