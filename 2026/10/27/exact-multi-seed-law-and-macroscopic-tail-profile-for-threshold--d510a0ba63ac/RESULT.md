# Exact multi-seed law and macroscopic-tail profile for threshold cascades

## Finding

Consider a fully mixed population of \(N\) agents with \(s\) fixed initial seeds and independent thresholds uniform on \(\{1,\ldots,N\}\) for all other agents, each activating permanently when the active count reaches its threshold. For every pair of integers \(1\le s\le k\le N\), the final active count \(K_{N,s}\) satisfies
\[
\Pr(K_{N,s}=k)=\binom{N-s}{k-s}\frac{s\,k^{k-s-1}}{N^{k-s}}\left(1-\frac{k}{N}\right)^{N-k},
\]
with \(0^0=1\); in particular, \(\Pr(K_{N,s}=N)=s/N\). Moreover, for fixed \(s\) and \(\epsilon\in(0,1)\),
\[
\sqrt N\,\Pr(K_{N,s}\ge\lceil\epsilon N\rceil)\longrightarrow s\sqrt{\frac{2}{\pi}}\sqrt{\frac{1-\epsilon}{\epsilon}},
\]
and, conditional on that event, \(K_{N,s}/N\) converges in distribution to the density \(\frac{\sqrt{\epsilon}}{2\sqrt{1-\epsilon}}x^{-3/2}(1-x)^{-1/2}\) on \((\epsilon,1)\).

This is a fully mixed, single-movement threshold process. The exact finite-population law applies to every seed count \(s\) and every terminal size \(k\), while the tail limit is for a fixed number of seeds and a fixed macroscopic cutoff \(\epsilon\in(0,1)\).

## Assumptions and scope

There are \(N\) agents. Exactly \(s\) are initially active and remain active forever. Each of the other \(N-s\) agents independently receives a threshold \(T_i\) uniformly from \(\{1,\ldots,N\}\). At each synchronous update, every inactive agent becomes active if its threshold is no larger than the current active count. Let \(K_{N,s}\) be the eventual active count. Monotonicity and finiteness ensure termination. The same terminal set is obtained by sequentially activating eligible agents in any order, because eligibility depends only on the active count.

The exact law below is valid for all integers \(N\ge1\) and \(1\le s\le k\le N\). The asymptotic statement assumes that \(s\) is fixed as \(N\to\infty\); it does not claim uniformity when \(s\) grows with \(N\), when \(\epsilon\) approaches zero, or at the endpoint \(\epsilon=1\).

## Proof

**1. Count the threshold vectors that can recruit a specified set.** Fix a candidate final set of size \(k\) containing the \(s\) seeds. Put \(m=k-s\). The thresholds of its \(m\) nonseeds must all be at most \(k-1\), and after sorting them as \(t_{(1)}\le\cdots\le t_{(m)}\), they must satisfy
\[
t_{(j)}\le s+j-1,\qquad 1\le j\le m.
\]
These conditions are necessary and sufficient for the set to be recruited: the \(j\)-th smallest threshold can be met once the seeds and the preceding \(j-1\) recruits are active. The number of length-\(m\) parking functions with \(q=k-1\) spaces is \((q-m+1)(q+1)^{m-1}\). Here \(q-m+1=s\) and \(q+1=k\), so the number of admissible threshold vectors is exactly \(s k^{k-s-1}\). For \(m=0\), the empty vector is counted once, consistent with \(s k^{-1}=1\) at \(k=s\).

For completeness, the generalized parking-function count follows from circular parking: place \(m\) cars and \(q+1\) spaces on a circle. Every preference vector parks all cars. By rotational symmetry, each fixed space is empty in a fraction \((q+1-m)/(q+1)\) of all \((q+1)^m\) preference vectors. The vectors leaving a specified space empty are exactly the linear parking functions on the other \(q\) spaces. Their count is therefore \((q+1-m)(q+1)^{m-1}\), as used above.

**2. Obtain the exact probability mass function.** There are \(\binom{N-s}{k-s}\) choices for the recruited nonseeds. Their admissible threshold vectors have probability \(s k^{k-s-1}/N^{k-s}\). Each of the remaining \(N-k\) agents must have threshold greater than \(k\), an independent event of probability \((1-k/N)^{N-k}\). These conditions are disjoint across the chosen final set, so multiplication gives the displayed exact law. At \(k=N\), it reduces to \(s/N\).

**3. Reduce the macroscopic tail to the one-seed case.** Write \((a)_r=a(a-1)\cdots(a-r+1)\), with \((a)_0=1\). Dividing the exact mass for \(s\) seeds by the one-seed mass gives, for \(k\ge s\),
\[
\frac{\Pr(K_{N,s}=k)}{\Pr(K_{N,1}=k)}
=s\frac{N^{s-1}}{(N-1)_{s-1}}\frac{(k-1)_{s-1}}{k^{s-1}}.
\]
For fixed \(s\), this ratio tends to \(s\) uniformly over \(k\ge\lceil\epsilon N\rceil\). Thus the tail constant and the conditional macroscopic-size law are \(s\) times the one-seed tail before conditioning, and unchanged after conditioning.

**4. Evaluate the one-seed tail.** For \(s=1\), the exact law in Fontanari (2026) gives
\[
k\Pr(K_{N,1}=k)=B_{N,k}:=\binom Nk\left(\frac{k}{N}\right)^k\left(1-\frac{k}{N}\right)^{N-k}.
\]
For \(x=k/N\) in a compact subinterval of \((0,1)\), Stirling's formula yields uniformly
\[
\Pr(K_{N,1}=k)=\frac{1+o(1)}{\sqrt{2\pi}\,N^{3/2}x^{3/2}\sqrt{1-x}}.
\]
The Riemann sum over \(x\in[\epsilon,1-\delta]\), multiplied by \(\sqrt N\), tends to
\[
\frac{1}{\sqrt{2\pi}}\int_{\epsilon}^{1-\delta}\frac{dx}{x^{3/2}\sqrt{1-x}}.
\]
The omitted endpoint is controlled by the standard binomial-mass bound \(B_{N,k}\le C/\sqrt{N x(1-x)}\) for \(1\le k<N\): the contribution from \(k>(1-\delta)N\) is at most \(C_\epsilon\sqrt{\delta/N}\), while \(\Pr(K_{N,1}=N)=1/N\). Letting \(\delta\downarrow0\) gives
\[
\int_{\epsilon}^{1}\frac{dx}{x^{3/2}\sqrt{1-x}}=2\sqrt{\frac{1-\epsilon}{\epsilon}}.
\]
This proves the stated tail constant for one seed and hence for every fixed \(s\). Applying the same Riemann-sum argument with a bounded continuous test function proves the conditional weak limit. The normalizing integral is \(2\sqrt{(1-\epsilon)/\epsilon}\), so the displayed density integrates to one. There is no limiting atom at \(x=1\), since the full-cascade probability is \(s/N\) while the conditioning event has order \(N^{-1/2}\).

## Verification

The included standard-library verifier checks exact normalization of the formula with rational arithmetic, compares it with exhaustive threshold-vector enumeration for all seed counts through population size seven, and checks the predicted tail coefficient numerically at several cutoffs. These finite checks corroborate the derivation; the infinite-\(N\) tail law follows from the Stirling/Riemann-sum argument above, not from numerical fitting.

## Relationship to prior work

Fontanari's 2026 paper gives an exact final-size distribution for the same fully mixed threshold model with **one** initial instigator and derives the critical mean active fraction. Its stated initial condition is one instigator; the multi-seed law here changes that condition and requires a generalized parking-function count. The paper's exact one-seed mass does not itself state the all-\(s\) formula or the fixed-\(s\) macroscopic-tail coefficient and conditional density.

The accessible abstract and summary of Karampourniotis et al. describe multiple initiators in networked threshold contagion, emphasizing average cascade size and threshold heterogeneity, rather than an exact finite-population law for a fully mixed single movement with discrete uniform thresholds. The full primary text was not inspected line-by-line, so an equivalent complete-graph special case cannot be ruled out from the inspected materials alone. Ishikawa and Fontanari study competition among multiple groups, a different process with different state variables. The generalized parking-function count is a standard combinatorial ingredient; novelty is not claimed for that count itself, but for the exact multi-seed threshold law and its finite-population macroscopic-tail consequence in this model.

## Limitations

The result assumes complete mixing, a single irreversible movement, independent discrete-uniform thresholds for nonseeds, and a fixed seed count in the tail limit. It does not cover network topology, correlated thresholds, heterogeneous threshold laws, or a seed count that grows with population size. The tail theorem applies only to fixed \(\epsilon\in(0,1)\); the microscopic regime \(\epsilon\downarrow0\) and the exact endpoint \(\epsilon=1\) have different asymptotics. A targeted literature and database search found no exact match, but absence from an index is not proof of universal novelty; an unindexed multi-seed treatment remains a residual priority risk. The full text of the 2015 multiple-initiator article was not inspected line-by-line, so an equivalent complete-graph special case in that article remains possible. No independent audit has been performed.

## References

1. J. F. Fontanari, “Exact Solution of Granovetter’s Threshold Model for a Finite Population,” arXiv:2606.25921v1, first public 2026-06-24; *Mathematics* 14(14), 2620 (2026), DOI: 10.3390/math14142620. Primary source for the one-seed exact law and critical mean scaling.
2. M. Granovetter, “Threshold models of collective behavior,” *American Journal of Sociology* 83 (1978), 1420–1443. Foundational threshold-cascade model.
3. P. D. Karampourniotis, S. Sreenivasan, B. K. Szymanski, and G. Korniss, “The Impact of Heterogeneous Thresholds on Social Contagion with Multiple Initiators,” *PLOS ONE* 10(11) (2015), e0143020, DOI: 10.1371/journal.pone.0143020.
4. B. Y. S. Ishikawa and J. F. Fontanari, “Competitive Social Mobilization in Threshold Models of Collective Action,” arXiv:2601.18682v1 (2026), journal reference *Physica A* 695 (2026), 131642.
5. The generalized parking-function count used in the proof is established by the circular-parking argument included above; no novelty claim is made for that combinatorial identity.
