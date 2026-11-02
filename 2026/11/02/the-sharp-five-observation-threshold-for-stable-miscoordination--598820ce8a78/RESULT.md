# The sharp five-observation threshold for stable miscoordination in heterogeneous sampling dynamics

## Finding

For one-population sampling best-response dynamics in a symmetric two-action coordination game with diagonal payoffs \(u>1\) and \(1\), zero off-diagonal payoffs, and no sample-payoff ties for observation sizes at most four, **no distribution supported on observation sizes \(1,2,3,4\) admits an asymptotically stable interior population state**. This is sharp: for every \(1<u<3/2\), mixing sample sizes two and five produces exactly two interior equilibria, one attracting and one repelling, if and only if the fraction \(q\) of size-two observers satisfies

\[
\frac12<q<q_*:=\frac{343-126\sqrt7}{19}=0.507122884519\ldots.
\]

At equality, the two interior equilibria merge at a non-attracting (from both sides) double root. Consequently five is the least possible *maximum sample size* for asymptotically stable interior miscoordination in the stated generic, payoff-favored-action setting. The threshold is exact, rather than a large-sample sufficiency condition.

## Assumptions and scope

Consider a continuum of agents repeatedly randomly matched to play the two-action game with payoffs \(u\) for simultaneous action \(a\), \(1\) for simultaneous action \(b\), and \(0\) for a mismatch. The proportion currently choosing \(a\) is \(p\in[0,1]\). A revising agent independently samples \(k\) actions and best responds to the sample; size \(k\) has probability \(\theta_k\). Replacement at unit rate yields the deterministic evolution

\[
\dot p=W(p)-p,\qquad
W(p)=\sum_k\theta_k\sum_{j=\lfloor k/(u+1)\rfloor+1}^{k}\binom{k}{j}p^j(1-p)^{k-j}.
\]

The displayed strict threshold is used only when no tie \(k/(u+1)\in\mathbb Z\) occurs among positively weighted sample sizes. For the nonexistence statement assume \(u>1\), \(u\notin\{2,3\}\), and \(\operatorname{supp}\theta\subseteq\{1,2,3,4\}\). For the sharp construction assume \(1<u<3/2\), \(\theta_2=q\), and \(\theta_5=1-q\), with all other weights zero. The word 'stable' means asymptotically stable for the scalar continuous-time flow; no claim about evolutionary stability of a Nash equilibrium is implied.

## Proof

**Step 1: Exhaust the possible small-sample drift shapes.** Write \(F_k(p)=\Pr[\mathrm{Bin}(k,p)>k/(u+1)]\) and \(R_k(p)=(F_k(p)-p)/(p(1-p))\), for \(0<p<1\). Direct binomial expansion gives the following complete table; \(R_1=0\) in every range:

| Payoff range | \(R_2\) | \(R_3\) | \(R_4\) |
|---|---|---|---|
| \(1<u<2\) | \(1\) | \(2p-1\) | \(-3p^2+5p-1\) |
| \(2<u<3\) | \(1\) | \(2-p\) | \(-3p^2+5p-1\) |
| \(u>3\) | \(1\) | \(2-p\) | \(p^2-3p+3\) |

The drift is \(p(1-p)R(p)\), with \(R=\sum_{k=1}^4\theta_kR_k\). For \(1<u<3\), \(R\) is concave because \(R''=-6\theta_4\le0\), while \(R(1)=\theta_2+\theta_3+\theta_4>0\) unless all agents use one observation. A concave function positive at its right endpoint cannot cross from positive to negative at an interior point: otherwise its later secant slopes, and therefore its terminal value, would be negative. Even a zero without crossing cannot attract trajectories from both sides. Hence no asymptotically stable interior equilibrium exists. For \(u>3\), each nonzero \(R_k\) is strictly positive on \((0,1)\), so the drift is strictly positive. If \(\theta_1=1\), the drift vanishes identically and no isolated state is asymptotically stable. These cases exhaust the specified nonexistence domain.

**Step 2: Exactly analyze a size-two/size-five population.** For \(1<u<3/2\), sample size two chooses \(a\) upon at least one observed \(a\), whereas sample size five requires at least three. Thus

\[
F_2(p)=2p-p^2,\qquad F_5(p)=10p^3-15p^4+6p^5.
\]

A direct factorization gives

\[
\dot p=p(1-p)Q_q(p),\qquad Q_q(p)=2q-1+(1-q)h(p),
\quad h(p)=-p+9p^2-6p^3.
\]

The critical points of \(h\) are \(p_-=(3-\sqrt7)/6\) and \(p_+=(3+\sqrt7)/6\). The first is its unique minimum on \([0,1]\), of value \(h(p_-)=1-7\sqrt7/18\), and the second is its local maximum. Also \(Q_q(1)=1\), regardless of \(q\). Therefore \(Q_q\) is negative somewhere in \((0,1)\) while positive at both endpoints precisely when

\[
q>\tfrac12\quad\text{and}\quad
2q-1+(1-q)(1-7\sqrt7/18)<0,
\]

which simplifies to \(1/2<q<q_*\). In that interval \(Q_q\) has exactly two roots in \((0,1)\). Its signs are positive, negative, positive across those roots, yielding one locally attracting lower root, one repelling upper root, and attracting endpoint \(p=1\). The entire basin \((0,p_{\mathrm{upper}})\) tends to the attracting lower root except for that root's unstable endpoint \(p=0\); the interval \((p_{\mathrm{upper}},1]\) tends to \(p=1\). The boundary \(p=0\) is stationary but unstable. At \(q=q_*\), the two roots coincide at \(p_-\) and the drift has the same sign on both sides, so the double root is not asymptotically stable. When \(q\le1/2\), the drift has no positive-to-negative sign crossing, since \(Q_q(0)\le0\) and \(Q_q\) has a single local minimum followed by a maximum and stays positive through the right endpoint. When \(q>q_*\), its global minimum is positive, and no interior root exists. This proves the iff statement and sharp minimal maximum observation size.

For a concrete rational choice \(u=6/5\), \(q=101/200\), the attracting and repelling interior roots are respectively approximately \(0.0263335610975055\) and \(0.0925790678725357\).

## Verification

Run the standalone program `python check.py` with SymPy. It checks all twelve small-size polynomial identities for representative payoff values in the three exhaustive regions, the size-two/size-five drift factorization, the critical points and exact threshold, numerical locations and stability derivatives, and the exact drift signs at 999 rational points. The program reported `PASS 1021 symbolic/finite sign checks`. These computations reproduce finite identities and examples; the absence of attracting equilibria for every admissible distribution and the exact threshold for all parameter values are established by the preceding analytical proof, not by sampling.

## Relationship to prior work

Arigapudi, Heller and Schreiber's *Heterogeneous Noise and Stable Miscoordination* (first public arXiv version May 17, 2023) defines exactly the sampling best-response evolution above, proves that homogeneous sample sizes cannot stabilize an interior state, and proves existence of heterogeneous stable miscoordination for sufficiently large second sample sizes. Its analysis of Oyama, Sandholm and Tercieux (2015) discusses sufficient small-sample mass conditions and a large-sample two-group interval. The present result instead establishes the **least finite observation ceiling for any heterogeneous stable interior state** in the stated game family, and an **exact necessary-and-sufficient weight interval when the sizes are two and five**. The 2015 sampling-dynamics paper provides sufficient almost-global pure-equilibrium selection conditions, which are not equivalent to an exact finite support cutoff for attracting interior states. This comparison is a best-knowledge claim based on inspected texts and mathematical-record searches, not an assertion that all possible literature has been exhausted.

## Limitations

The universal nonexistence claim assumes \(u>1\) and excludes the sample-payoff ties at \(u=2\) and \(u=3\); tie-breaking behavior there is not classified. The two-size phase diagram applies to \(1<u<3/2\), not the entire payoff domain. The result concerns single-population deterministic revision, not finite-population stochastic evolution, arbitrary heterogeneous games, or two-population asymmetric environments. Exact roots at the transition can be semistable without satisfying two-sided asymptotic stability. A specialized equivalent classification not indexed in the inspected literature remains possible. No independent audit has been performed.

## References

1. S. Arigapudi, Y. Heller, A. Schreiber, *Heterogeneous Noise and Stable Miscoordination*, arXiv:2305.10301 (first public version 2023-05-17), https://arxiv.org/abs/2305.10301 . Full 2025 preprint inspected at https://arxiv.org/pdf/2305.10301 , Sections 2.1–2.6 and relevant statements in Section 3.
2. D. Oyama, W. H. Sandholm, O. Tercieux, *Sampling Best Response Dynamics and Deterministic Equilibrium Selection*, Theoretical Economics 10 (2015), 243–281, https://doi.org/10.3982/TE1405 . Author-hosted full preprint: https://www.oyama.e.u-tokyo.ac.jp/papers/sBRD.140328.pdf , especially Sections 3.2–3.3 and Observations 3.2–3.3.
