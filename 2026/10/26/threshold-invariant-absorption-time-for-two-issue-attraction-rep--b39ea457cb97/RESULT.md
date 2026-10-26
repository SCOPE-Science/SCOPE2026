# Threshold-invariant absorption time for two-issue attraction–repulsion dynamics

## Finding

In a finite, two-issue model with both copying of friends and opposition to enemies, the *entire distribution* of the time to consensus or complementary-pair polarization is independent of the friend/enemy threshold, despite the fact that the kind of terminal configuration can change. This exact invariance comes from a Markovian reduction to the parity of the two-bit opinion string.

Let \(N\ge2\). If initially \(a\) of the \(N\) people have even parity (strings \(00\) or \(11\)), and the remaining people have odd parity (strings \(01\) or \(10\)), then after each attempted update the number \(A_t\) of even-parity people obeys
\[
\Pr(A_{t+1}=i+1\mid A_t=i)=\Pr(A_{t+1}=i-1\mid A_t=i)=p_i:=\frac{i(N-i)}{2N^2},\qquad 0<i<N.
\]
The remaining probability is a self-loop. States \(0\) and \(N\) are absorbing. The *physical* absorption time \(T\), measured in individual attempted updates including unsuccessful discussions and self-selection, has
\[
\Pr(A_T=N\mid A_0=a)=\frac aN,
\qquad
\mathbb E[T\mid A_0=a]=2N\sum_{j=1}^{a}(H_{N-j}-H_{j-1}),
\]
where \(H_m=\sum_{r=1}^{m}1/r\) for positive integers \(m\) and \(H_0=0\). The sum is zero for \(a=0\) and \(a=N\). Its full distribution is specified by the transient \((N-1)\)-square matrix \(Q\) with \(Q_{ii}=1-2p_i\), \(Q_{i,i-1}=Q_{i,i+1}=p_i\) (when the column is transient): for every integer \(t\ge0\) and \(1\le a<N\),
\[
\Pr(T>t\mid A_0=a)=(Q^t\mathbf 1)_a.
\]
For \(a/N\to x\in(0,1)\), the expected number of updates is \(2N^2[-x\log x-(1-x)\log(1-x)]+o(N^2)\). Thus this two-issue model never exhibits exponential expected absorption time under the stated generic thresholds.

## Assumptions and scope

Each agent holds one of four two-bit strings. Issue weights satisfy \(w_1,w_2>0\) and \(w_1+w_2=1\). The similarity of two strings is the sum of weights of the issues on which they agree. Fix the same lower and upper threshold, \(\alpha_e=\alpha_f=\alpha\), with \(0<\alpha<1\) and \(\alpha\notin\{w_1,w_2\}\). Noise is zero. Each elementary update independently samples a uniformly random focal agent and uniformly random target agent, allowing self-selection, and independently samples either issue with probability \(1/2\). The focal agent adopts the target's bit on that issue if similarity exceeds \(\alpha\), adopts the opposite of the target's bit if similarity is below \(\alpha\), and otherwise remains unchanged. Only one focal bit can change per update.

A terminal consensus means everybody holds the same two-bit string. A terminal complementary-pair polarization means that all occupied strings belong to a pair \(\{s,\bar s\}\), possibly with just one member occupied. In this two-issue setting these are precisely the configurations with all agents of one parity. The probability formula refers to the *identity of the surviving complementary pair*, not to the probability of strict two-type polarization; the latter generally depends on \(\alpha\).

If instead the target is sampled uniformly among the other \(N-1\) agents, each transient transition rate is multiplied by \(N/(N-1)\): replace \(p_i\) by \(i(N-i)/(2N(N-1))\) and multiply all mean absorption times by \((N-1)/N\). The resulting family-fixation probabilities are unchanged.

## Proof

**Parity reduction.** The even-parity strings are \(00,11\) and the odd-parity strings are \(01,10\). A pair of strings of the same parity is either identical or complementary. Identical strings have similarity \(1\) and copying changes no bit; complementary strings have similarity \(0\), so opposition changes no bit. Hence interactions between two agents of the same parity cannot change either opinion, for every \(0<\alpha<1\).

Two strings of opposite parity differ at exactly one issue and agree at the other. Their similarity is therefore either \(w_1\) or \(w_2\). By the strict genericity assumption, they are friends or enemies, not neutral. If they are friends, the focal individual changes exactly when the differing issue is discussed, which has probability \(1/2\); this flips the focal parity to that of the target. If they are enemies, the focal changes exactly when the agreeing issue is discussed, again with probability \(1/2\); this also flips its parity to the target's parity. This dichotomy is exhaustive and has no dependence on either weight or threshold.

When there are \(i\) even-parity agents, an odd focal with an even target is selected with probability \(i(N-i)/N^2\); a change occurs with probability \(1/2\). The reverse ordered selection has the same probability. Therefore both birth and death probabilities equal \(p_i=i(N-i)/(2N^2)\), regardless of the detailed configuration of the four types. This proves *strong lumpability* and the displayed transition matrix.

**Absorption and fixation.** In an even-only or odd-only population no update is possible by the same-parity argument. Conversely, when both parities are present, a cross-parity ordered pair has positive probability and one discussion issue causes a change. The resulting birth–death chain reaches one of its endpoints almost surely because the finite transient states have positive probabilities of proceeding toward an endpoint. Therefore the hitting time of the parity endpoints equals the stopping time at consensus or complementary-pair polarization. Since \(A_t\) is a bounded martingale, applying bounded optional stopping to \(A_{t\wedge T}\) and taking limits gives \(a=N\Pr(A_T=N)\).

**Exact time law.** Let \(u_i=\mathbb E[T\mid A_0=i]\), with \(u_0=u_N=0\). First-step conditioning gives
\[
p_i(u_{i+1}-2u_i+u_{i-1})=-1.
\]
Let \(d_i=u_i-u_{i-1}\). The proposed solution has \(d_i=2N(H_{N-i}-H_{i-1})\). Indeed
\[
d_{i+1}-d_i=-2N\left(\frac1i+\frac1{N-i}\right)=-\frac{2N^2}{i(N-i)}=-\frac1{p_i},
\]
and \(\sum_{i=1}^{N}d_i=0\) by reversing \(i\mapsto N+1-i\), enforcing the endpoint boundary conditions. Summing the differences from \(1\) to \(a\) proves the mean formula. Killing the chain upon visiting an endpoint gives the transient matrix \(Q\); standard finite-state path enumeration yields \(\Pr(T>t)=(Q^t\mathbf 1)_a\). The harmonic-number sum has the stated Riemann-sum/entropy asymptotic for interior initial fractions.

**The threshold changes the terminal *type* despite unchanged time.** For \(N=2\), start from strings \(00\) and \(01\). If \(0<\alpha<\min(w_1,w_2)\), the pair is friendly and its first successful discussion makes both agents identical (consensus). If \(\max(w_1,w_2)<\alpha<1\), the pair is antagonistic and the first successful discussion makes them complementary (polarization). In either case the first successful discussion has probability \(1/4\) on each attempted update with replacement, so the time to absorption is geometric with mean \(4\). Thus the invariance does not assert invariance of the terminal opinion-string distribution.

**Why the non-equality condition is genuine.** If \(\alpha=w_1\), choose two initially adjacent strings agreeing exactly on issue one. Their similarity is exactly the threshold, so neither attractive nor repulsive updating occurs. This mixed-parity population remains frozen despite \(A_t\notin\{0,N\}\). The excluded equality parameters genuinely invalidate the claimed hitting-time identification.

## Verification

The accompanying `verify.py` independently enumerates every ordered focal/target opinion-type pair and both issues, using exact rational arithmetic to implement the original friend/enemy rule. For all compositions of two through seven people, three weight splits, and the admissible values from five thresholds, it checks every projected transition probability against \(i(N-i)/(2N^2)\), with no reliance on the transformed chain when computing the original transitions. This yields 4,225 microstate checks. It additionally checks the harmonic-formula recurrence exactly for populations from two through forty-nine, tests the two-agent friendly/antagonistic distinction and the equality-threshold freezing boundary. Reproduce with `python verify.py`. These finite checks are not a substitute for the preceding all-population proof.

## Relationship to prior work

Mintz, Simonson, Wodarz, Fu and Komarova, *When minor issues matter: symmetries, pluralism, and polarization in similarity-based opinion dynamics* (2026, arXiv:2603.04939), introduce exactly this stochastic attraction–repulsion update and analyze its deterministic symmetries and simulated absorption outcomes. Their main text identifies consensus and antipodal polarization as absorbing configurations and reports threshold-sensitive convergence behavior in more complicated multivariate systems. The result proved here is a two-issue, finite-population **strong-lumpability and absorption-time invariance** statement; it is not merely their classification of terminal possibilities.

Pickering and Lim, *Solution of the voter model by spectral analysis* (2015, arXiv:1408.2130), give extensive exact analysis of the classical voter chain. The gambler's-ruin distribution and harmonic hitting-time recurrence, once the model-specific projection has been established, are classical; no originality is claimed for that general Markov-chain computation in isolation. The additional contribution here is the algebraic identification that *both attraction and repulsion, for every generic similarity threshold and heterogeneous two-issue weights*, give the **same** neutral parity chain and therefore exactly the same physical absorption-time law even when the terminal outcome type differs.

## Limitations

This is a finite-population result on two binary issues, complete mixing, independent uniform agent choices, uniform issue sampling, zero mutation/noise, and a common strict friend/enemy threshold. It does not extend unchanged to additional issues, unequal discussion probabilities, thresholds equal to a similarity weight, or a model in which target selection depends on opinion similarity. The full supplementary analysis of the motivating preprint was not independently checked; an unindexed equivalent statement or refinement in supplementary or other literature remains a residual priority risk. The result says nothing about real-world timescales beyond this idealized update rule.

## References

1. B. Mintz, D. Simonson, D. Wodarz, F. Fu, N. L. Komarova, *When minor issues matter: symmetries, pluralism, and polarization in similarity-based opinion dynamics*, arXiv:2603.04939v1, first publicly posted 2026-03-05, https://arxiv.org/abs/2603.04939.
2. W. Pickering, C. Lim, *Solution of the voter model by spectral analysis*, arXiv:1408.2130, *Physical Review E* 91, 012812 (2015), https://arxiv.org/abs/1408.2130.
