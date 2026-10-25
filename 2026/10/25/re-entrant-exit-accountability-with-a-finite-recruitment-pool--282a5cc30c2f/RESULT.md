# Re-entrant exit accountability with a finite recruitment pool

## Finding
For a finite population of \(n\ge2\) agents, a one-delegate exploitation decision under probabilistic exit and delayed outsider recruitment has the exact accountability threshold
\[
 F_m=\frac{\alpha\kappa t}{m(m-1)\bigl(1-t+t[1-(1-p)^{n-m}]\bigr)},\qquad t=\delta^L.
\]
The center weakly prefers not to exploit exactly when \(d\le F_m\). For every \(n\ge3\) and \(p\in(0,1]\), **some positive exploitation gain \(d\)** is deterred at the grand constituency size \(n\) but not at size \(n-1\) if and only if
\[
 t>\frac{2}{2+(n-2)p}.
\]
The exact nonempty interval realizing that reversal is
\[
 \frac{\alpha\kappa t}{(n-1)(n-2)(1-t+tp)}<d\le
 \frac{\alpha\kappa t}{n(n-1)(1-t)}.
\]
Hence an accountability set that is downward closed under permanent member loss can become non-downward-closed when a **finite outside recruitment pool** may refill a vacancy. This is a statement about a specified one-shot deviation, not a general game-equilibrium assertion.

## Assumptions and scope
There are \(n\ge2\) persistent agents, and one existing center has a constituency of size \(m\in\{2,\ldots,n\}\), including itself. The center pays \(c(m)=\kappa/m\) in each reached operational round for \(\kappa>0\). Every epoch has \(L\ge1\) rounds; continuation after each round occurs independently with probability \(0<\delta<1\), giving an epoch-survival factor \(t=\delta^L\). The center decides once at the epoch start whether to exploit **one** delegate for a transfer of \(d>0\) in every reached round. If the epoch ends and play continues, exploitation causes that delegate to depart with conditional probability \(\alpha\in(0,1]\). The departure does not affect continuation and the departed delegate is permanently ineligible for reentry into this same center's constituency.

If an exploited delegate departs, the vacancy persists for at least one complete subsequent epoch at size \(m-1\). At the **end** of each complete vacant epoch, every agent outside the initial constituency (of whom there are \(n-m\)) independently submits an application with probability \(p\in[0,1]\). If at least one submits, exactly one is admitted, restoring size \(m\) from the start of the next epoch; otherwise recruitment is independently repeated. An outsider remains eligible to retry while outside. The center has no other turnover or deviations in this comparison; continuation payoffs after full restoration are identical under both initial actions. These are exogenous recruitment commitments, not strategic joining equilibria. The parameter \(\alpha\) is conditional on reaching the governance transition. Define \(\rho_m=1-(1-p)^{n-m}\), with \(\rho_n=0\) also at \(p=1\) (the empty outsider pool).

## Proof
Put \(A=\sum_{j=0}^{L-1}\delta^j=(1-\delta^L)/(1-\delta)>0\) and let \(D(m)=c(m-1)-c(m)=\kappa/[m(m-1)]\). Conditional on a vacancy at the **start** of an epoch, let \(Q_m\) denote the center's expected excess discounted organizational cost until the vacancy is filled (or play terminates). During the first vacant epoch it incurs \(A D(m)\). The cost persists into another vacant epoch precisely if the interaction survives that epoch and no outsider applies, with probability-and-discount factor \(t(1-\rho_m)\). Therefore
\[
 Q_m=A D(m)+t(1-\rho_m)Q_m,
 \qquad Q_m=\frac{A D(m)}{1-t(1-\rho_m)}.
\]
Since \(0<t<1\), the denominator is strictly positive even when \(\rho_m=0\); the Bellman equation is the convergent nonnegative geometric sum, not merely a formal rearrangement.

Exploitation transfers \(dA\) to the center over its initial locked-in epoch. The only difference in subsequent payoffs is that a vacancy begins at the next epoch with factor \(\alpha t\). Thus the **non-exploit minus exploit** value is
\[
 \alpha tQ_m-dA
 = A\left(\frac{\alpha tD(m)}{1-t+t\rho_m}-d\right).
\]
Because \(A>0\), deterrence is equivalent to the stated exact \(d\le F_m\). For \(p=0\), \(\rho_m=0\), recovering the permanent-loss benchmark \(\alpha tD(m)\ge d(1-t)\).

At the two largest allowable sizes, \(\rho_n=0\) and \(\rho_{n-1}=p\). Hence
\[
 F_n=\frac{\alpha\kappa t}{n(n-1)(1-t)},\qquad
 F_{n-1}=\frac{\alpha\kappa t}{(n-1)(n-2)(1-t+tp)}.
\]
The desired strict reversal occurs exactly when \(F_{n-1}<d\le F_n\), so such a \(d>0\) exists exactly when \(F_n>F_{n-1}\). All denominators are positive; cancelling them gives
\[
 (n-2)tp>2(1-t),\qquad\text{equivalently}\qquad t>\frac{2}{2+(n-2)p}.
\]
At equality the interval is empty. If \(p=0\), the reversal is impossible. For the smallest allowable population \(n=2\), there is only one nontrivial size, so no adjacent-size reversal is possible.

For an exact witness take \(n=3\), \(L=1\), \(\delta=3/4\), \(p=1\), \(\alpha=\kappa=1\), \(d=2/5\). Then \(F_2=3/8<2/5<F_3=1/2\). The non-exploit minus exploit values, normalized by \(A=1\), are \(-1/40\) for size two and \(+1/10\) for size three. If a delegation cost \(\ell=1/4\) is separately charged to delegates, both sizes are individually viable absent exploitation: \(c(1)-c(2)=1/2\ge\ell\) and \(c(1)-c(3)=2/3\ge\ell\). Thus the reversal is not an artifact of delegating below the fixed-cost participation threshold.

## Verification
The standalone `check_recruitment.py` uses only Python standard-library exact fractions. It confirms Bellman identities, finite-geometric-sum plus exact tail, deterrence thresholds and the sharp adjacent-size equivalence across 15,840 rational parameter combinations; it identifies 260 strict-reversal witness parameter combinations on the tested grid. It also verifies the exact three-agent witness values and the two participation inequalities. Run `python3 check_recruitment.py` from the extracted file directory. This finite computation checks examples and formulas but **does not prove the universal quantified theorem**; that follows from the preceding Bellman and inequality arguments.

## Relationship to prior work
Mukhopadhyay, Filos-Ratsikas and Danassis (2026, arXiv:2610.21746v1, Sections 3.2, 4.1 and 6) analyze exit-based accountability under no replacement over the continuation horizon; their fixed-cost condition is \(\alpha t D(m)\ge d(1-t)\), and accountability is downward closed. Their simulations allow subsequent recruitment, and their discussion notes that replacement shortens the punishment, but the inspected analytical proposition does **not** give this finite-outsider recruitment Bellman law or the sharp grand-size re-entrance threshold. The present result changes the continuation technology, not the original theorem. Joshi (2024 online publication, 2025 journal volume) analyzes repeated club formation with size-dependent member preferences and fear of exclusion; it does not model this center's exploitation versus probabilistic vacancy cost under automatic outsider applications. These are comparison claims limited to the inspected primary texts, not declarations of exhaustive publication priority.

## Limitations
The exploited delegate is excluded from this center indefinitely; if that same delegate may apply again, the grand-constituency vacancy will not necessarily be permanent and the displayed boundary changes. The original outsiders apply exogenously and independently with stationary probability; in a strategic recruitment game the hazard could depend on group size, wages, outside options, or other constituencies. The result tests a single contemplated exploited delegate and does not show equilibrium behavior, enforcement of applicant commitments, deterrence of simultaneous multi-delegate exploitation, or optimal social welfare. Existence of a strict reversal is robust under small changes of parameters satisfying the strict inequalities; this does not imply a global nonmonotonicity pattern for all sizes or a quantitative prediction about observed institutions. Unindexed analogous renewal models pose a residual priority risk.

## References
1. A. Mukhopadhyay, A. Filos-Ratsikas, and P. Danassis, *The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance*, arXiv:2610.21746v1, originally submitted 2026-10-15. https://arxiv.org/html/2610.21746v1
2. P. Joshi, *Fear of exclusion: the dynamics of club formation*, *Theory and Decision* 98 (2025), 249–276, first online publication 2024-11-19, doi:10.1007/s11238-024-10010-2. https://link.springer.com/article/10.1007/s11238-024-10010-2
