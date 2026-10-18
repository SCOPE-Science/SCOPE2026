# Arbitrarily long attracting opinion cycles with only three agents

## Finding

For every integer \(p\geq 2\), the scalar, synchronous set-based-confidence opinion model of Zabarianska and Proskurnikov admits a **locally attracting orbit of prime period \(p\)** with only three agents: two stubborn agents fixed at opinions \(0\) and \(1\), and one ordinary agent. The same confidence set is used to determine all ordinary-agent interactions, and it can be chosen **bounded, open, symmetric, and a finite union of intervals containing a neighborhood of zero**. The period-\(p\) return map has exact local multiplier \(2^{-p}\); in particular, each periodic orbit attracts a nonempty open interval of initial ordinary-agent opinions. The number three is minimal for a nonconstant periodic orbit under a symmetric self-confident rule.

One explicit choice, for every \(p\ge2\), is
\[
Q=2^p-1,\qquad \eta=\frac{1}{100Q},\qquad
u_j=\frac{2^{p-1-j}}{Q}\quad(0\le j<p),
\]
\[
C=\{0,u_0,\ldots,u_{p-2},1-u_{p-1}\},\qquad
\mathcal O_p=\bigcup_{c\in C}\big((c-\eta,c+\eta)\cup(-c-\eta,-c+\eta)\big).
\]
The ordinary-agent opinions \(u_0,u_1,\ldots,u_{p-1}\) form the desired prime-period orbit, with the first \(p-1\) steps influenced only by the stubborn opinion \(0\) and the last step influenced only by the stubborn opinion \(1\).

Thus **period length is not bounded by the agent count** in this general model, even when symmetry, openness, and a positive confidence neighborhood are retained. The construction varies the confidence set with \(p\); it does **not** assert that one fixed set realizes all periods.

## Assumptions and scope

There are exactly three scalar-opinion agents. The stubborn agents keep their respective opinions \(0\) and \(1\) at every discrete time, regardless of the opinions they might otherwise trust. The ordinary agent, with opinion \(x\in\mathbb R\), trusts itself and exactly those stubborn agents whose opinion difference belongs to a common set \(\mathcal O\subset\mathbb R\). It replaces its opinion by the equally weighted average of the opinions it trusts, including its own. For the symmetric set \(\mathcal O_p\) above, this is the map
\[
F_p(x)=\frac{x+b(x)}{1+a(x)+b(x)},\quad
 a(x)=\mathbf 1_{\{-x\in\mathcal O_p\}},\quad
 b(x)=\mathbf 1_{\{1-x\in\mathcal O_p\}}.
\]
This is precisely the deterministic SCOD update with stubborn agents described in the source, specialized to one opinion coordinate. No probabilistic sampling, asynchronous update, or weighted interactions are assumed. All intervals in \(\mathcal O_p\) are open; membership at their boundaries is defined by the displayed strict inequalities.

## Proof

**1. All inclusion and exclusion tests are strict.** Define the selected positive distances
\[
S=\{u_0,\ldots,u_{p-2},1-u_{p-1}\}
\]
and the excluded positive distances
\[
E=\{u_{p-1},1-u_0,\ldots,1-u_{p-2}\}.
\]
Every element of either set is an integer multiple of \(1/Q\). They are disjoint: \(u_{p-1}=1/Q\) differs from the positive powers-of-two numerators of the selected \(u_j\), and from \((Q-1)/Q\) because \(Q\ge3\). For \(0\le i,j\le p-2\), equality \(1-u_i=u_j\) would imply
\[
2^{p-1-i}+2^{p-1-j}=2^p-1,
\]
which is impossible because the left side is even and the right side is odd. Equality \(1-u_i=1-u_{p-1}\) would imply \(i=p-1\), also impossible. Moreover \(E\) is disjoint from zero. Since distinct elements of \(\{0\}\cup S\cup E\) are separated by at least \(1/Q\), and \(\eta<1/(2Q)\), every selected distance is in \(\mathcal O_p\) and every excluded distance is outside its closure. Symmetry supplies the same conclusions for negative differences. This remains true for \(p=2\), where two expressions for a selected center coincide.

**2. The exact itinerary.** At \(x=u_j\) with \(0\le j\le p-2\), the difference to \(0\) is selected and the difference to \(1\) is excluded. Consequently \(a(u_j)=1\), \(b(u_j)=0\), and
\[
F_p(u_j)=\frac{u_j}{2}=u_{j+1}.
\]
At \(x=u_{p-1}=1/Q\), only the stubborn opinion \(1\) is selected, giving
\[
F_p(u_{p-1})=\frac{u_{p-1}+1}{2}
=\frac{Q+1}{2Q}=\frac{2^{p-1}}{Q}=u_0.
\]
The \(p\) powers-of-two numerators are distinct, so this is a **prime** period-\(p\) orbit rather than a repeated shorter cycle.

**3. An attracting open basin and exact multiplier.** Let \(|h|<\eta/2\). The membership decisions of each stubborn agent remain unchanged whenever \(|x-u_j|<\eta/2\), because selected tests lie at the centers of open confidence intervals and excluded tests have distance at least \(1/Q-\eta>\eta\) from those intervals. On each such neighborhood the map is affine with slope \(1/2\). Inductively, for every integer \(t\ge0\),
\[
F_p^{\,t}(u_0+h)=u_{t\bmod p}+2^{-t}h.
\]
In particular \(F_p^p\) fixes \(u_0\), has derivative \(2^{-p}\) on its neighborhood, and attracts that entire open neighborhood. Since there is a strict positive margin at every selection boundary, the attracting periodic itinerary also persists under sufficiently small changes of the confidence-interval endpoints and stubborn anchor opinions (with the period orbit shifted continuously): its \(p\)-step affine map remains a contraction.

**4. Sharpness of the three-agent threshold.** With one agent all opinions are fixed. With two agents and a symmetric confidence set containing zero, if both are ordinary then either they do not trust each other and are fixed, or they trust reciprocally and agree after one simultaneous averaging update. If one is stubborn, the other is either fixed or moves halfway toward that stubborn opinion; its distance to the stubborn opinion never increases and strictly decreases at any nontrivial update, precluding a nonconstant periodic orbit. If both are stubborn, both are fixed. Hence no system with fewer than three agents in this symmetric self-confident class has a nonconstant periodic orbit. The construction above attains the threshold.

## Verification

The standalone standard-library script `verify_periods.py` reconstructs the confidence set from exact fractions, evaluates the actual three-agent averaging rule, checks all \(p\) adjacency decisions and transition identities, and tests exact geometric phase contraction under two nearby rational perturbations. It passed for every integer \(2\le p\le40\), including \(312\) perturbed full laps. The mathematical proof above, not the finite computation, establishes the infinite family for all \(p\ge2\).

To reproduce: execute `python3 verify_periods.py` using Python 3 and no external dependencies. The certificate is a finite stress test of the construction, not a computer-assisted proof of unbounded period length.

## Relationship to prior work

Zabarianska and Proskurnikov introduced the symmetric set-confidence dynamics with stubborn agents and gave a **three-agent, prime-period-three** oscillation (their Example 4). Their Theorem 1 proves convergence when all stubborn agents have the same opinion; it does not apply to two stubborn agents with different opinions. Their concluding questions ask when stubborn agents induce oscillations. The present theorem retains the source's averaging convention and builds a sharply minimal **locally attracting cycle for every prescribed period**, with explicit integer-rational parameters and a stable symbolic itinerary. This is not implied by the existence of one period-three orbit. The initial construction is motivated by that open oscillation question.

Glass and Glass studied competing stubborn groups in a standard distance-threshold HK model, with a different (interval) confidence geometry and an emphasis on group influence, not unbounded attracting periods. General mixed HK systems and piecewise-affine contractions provide adjacent frameworks; the present statement is about the exact symmetric, open, finite-union SCOD confidence relation and the sharp three-agent realization. Indexed mathematical findings queried by model, period, confidence geometry, and aliases did not identify a theorem implying this conclusion; the absence of a match is not a proof of historical uniqueness.

## Limitations

The confidence set depends on \(p\) and becomes more finely resolved as \(p\) increases (the guaranteed margin is of order \(2^{-p}\)). The theorem concerns local attraction, not global attraction or simultaneous existence of all periods for one fixed confidence set. It does not classify all admissible confidence sets, all itineraries, or the maximal possible number of distinct attractors. It does not imply recurrent behavior for homogeneous stubborn opinions, a standard connected confidence interval, or arbitrary noisy/asynchronous variants. Coverage by unindexed specialist literature is not ruled out.

## References

1. I. Zabarianska and A. V. Proskurnikov, *Opinion Dynamics with Set-Based Confidence: Convergence Criteria and Periodic Solutions*, arXiv:2408.01753, first posted 2024-08-03; IEEE Control Systems Letters **8** (2024), 2373–2378, DOI 10.1109/LCSYS.2024.3479275. Model (1)–(2), Example 4, Theorem 1, and Section V.
2. C. A. Glass and D. H. Glass, *Social Influence of Competing Groups and Leaders in Opinion Dynamics*, Computational Economics **58** (2021), 799–823, first online 2020-09-19, DOI 10.1007/s10614-020-10049-7.
3. H.-L. Li, *Mixed Hegselmann–Krause Dynamics*, arXiv:2010.03050, first posted 2020-10-06. Background abstract on heterogeneous stubbornness; full manuscript not available during the present comparison.
