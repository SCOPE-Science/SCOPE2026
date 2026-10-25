# Exact one-omission approximation frontier for product-gap facility location

## Finding
Let \(k\ge2\) and consider exactly \(k+1\) agents at distinct ordered locations \(x_0<x_1<\cdots<x_k\) on the real line. Write \(g_i=x_i-x_{i-1}>0\), \(1\le i\le k\), and \(m=\min_i g_i\). The product-gap mechanism samples a set of \(k\) reported locations with probability proportional to the product of its consecutive gaps, and opens a facility at each sampled location. Let \(C_k(g)\) be its expected sum of nearest-facility distances and \(\mathrm{OPT}_k(g)\) the smallest such sum over **all** placements of \(k\) real-valued facilities.

**Theorem (the one-omission frontier).** For every such \(k\) and every positive gap vector,
\[
\mathrm{OPT}_k(g)=m,\qquad
C_k(g)=\frac{k+1+\displaystyle\sum_{i=1}^{k-1}\frac{\min\{g_i,g_{i+1}\}}{\max\{g_i,g_{i+1}\}}}{2\displaystyle\sum_{i=1}^{k}g_i^{-1}}.
\]
Moreover,
\[
1\le\frac{C_k(g)}{\mathrm{OPT}_k(g)}<k-\frac12,
\qquad
\sup_{g_1,\ldots,g_k>0}\frac{C_k(g)}{\mathrm{OPT}_k(g)}=k-\frac12.
\]
The supremum is not attained at a finite distinct profile. The mechanism is exactly welfare-optimal, \(C_k(g)=m\), **if and only if** both end gaps equal \(m\) and every adjacent pair of gaps contains at least one gap equal to \(m\). In particular, its sharp one-omission ratio is \(3/2\) for two facilities and \(5/2\) for three facilities.

## Assumptions and scope
Agents have unit weight, report their real-line positions truthfully for welfare evaluation, and incur distance to the nearest open facility. The sampled \(k\)-set consists of agent reports, but \(\mathrm{OPT}_k\) allows arbitrary facility locations. Distinctness makes every sampled-set weight strictly positive. When the \(k+1\) reports contain at most \(k\) distinct positions, the mechanism's standard fallback covers all occupied positions and both expected cost and optimum are zero; the approximation *ratio* is then undefined, but the corresponding cost inequality is trivial. The approximation statement is independent of incentive properties: this mechanism is known to be strategyproof for \(k=2,3\), not for general \(k\ge4\).

## Proof
Set \(P=\prod_{i=1}^k g_i>0\). Exactly one agent is omitted by any sampled \(k\)-subset. Number agents from \(0\) to \(k\). Omitting the first report gives weight \(w_0=P/g_1\) and realized cost \(c_0=g_1\); omitting the last gives \(w_k=P/g_k\) and \(c_k=g_k\). For an interior omitted agent \(j\in\{1,\ldots,k-1\}\), the two adjacent gaps are merged, so
\[
w_j=P\frac{g_j+g_{j+1}}{g_jg_{j+1}}
=P(g_j^{-1}+g_{j+1}^{-1}),\qquad
c_j=\min\{g_j,g_{j+1}\}.
\]
Consequently the exact total weight and weighted social cost are
\[
W=\sum_{j=0}^k w_j=2P\sum_{i=1}^k g_i^{-1},\qquad
\sum_{j=0}^k w_jc_j=P\left(k+1+\sum_{i=1}^{k-1}\frac{\min\{g_i,g_{i+1}\}}{\max\{g_i,g_{i+1}\}}\right).
\]
Their quotient is the asserted expected-cost identity.

For the unrestricted optimum, any assignment of \(k+1\) agents to \(k\) facilities serves some two distinct agents at the same facility. The triangle inequality makes their combined service distance at least their mutual distance, which is at least \(m\). Conversely, placing facilities at every report except one endpoint of a closest neighboring pair costs exactly \(m\). Thus \(\mathrm{OPT}_k(g)=m\).

The lower bound \(C_k(g)\ge m\) follows since every realized facility set costs at least the optimum. Because all \(w_j>0\), equality holds precisely when every omission costs \(m\). The endpoint omission costs force \(g_1=g_k=m\); interior omission costs force \(\min\{g_j,g_{j+1}\}=m\) for all \(j\). These are exactly the stated isolated-long-gap conditions.

For the upper bound, choose an index \(j\) with \(g_j=m\), and choose either neighboring gap \(g_\ell\) (at least one exists because \(k\ge2\)). Put \(u=m/g_\ell\in(0,1]\). Of the \(k-1\) adjacent-gap ratios in the numerator, one is exactly \(u\) and every other is at most one. Moreover \(m\sum_i g_i^{-1}\ge1+u\). Therefore
\[
\frac{C_k(g)}m\le\frac{2k-1+u}{2(1+u)}
= k-\frac12-\frac{(k-1)u}{1+u}<k-\frac12.
\]
To show sharpness, choose \(g_1=1\) and \(g_2=\cdots=g_k=T>1\). Direct substitution gives
\[
\frac{C_k(g)}{m}=\frac{(2k-1)T+1}{2(T+k-1)}
\longrightarrow k-\frac12\qquad (T\to\infty).
\]
The construction retains strictly distinct reports for every finite \(T\), completing the proof.

## Verification
The standalone Python program `VERIFY.py` independently computes all subset weights and realized costs using exact rational arithmetic, and compares them with the closed formula, sharp inequality, and exact optimality classification. It passed 21,844 exact-rational assertions for \(2\le k\le6\) and all gap vectors with entries from \(\{1,2,3,4\}\), plus sharp-family identities at four scales. These finite computations are reproducibility checks, not a substitute for the quantified algebraic proof above. Run `python3 VERIFY.py` with Python 3 and no third-party packages.

## Relationship to prior work
Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633 (first submitted August 20, 2026), introduces the same gap-product sampling family and proves its global sharp \(2k\) ratio when the population size is unrestricted. Chan, Lin, and Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484 (first submitted August 23, 2026), call the rule **Gap-Product** and independently prove the global \(2k\) guarantee; their Section 5 bounds cost through a weighted-sum inequality. The present theorem instead determines the exact \(n=k+1\) ratio, the full positive-gap expectation formula, and precisely which distinct profiles are welfare-optimal. In this regime, the displayed general weighted-sum inequality of Chan et al. yields the weaker upper bound \(k\); it does not yield \(k-1/2\) without additional analysis. Aziz, Mackenzie, and Suzuki, arXiv:2608.16550, analyze a different random-anchor volume rule. The \(k=2\) specialization is also known as **Global Pair** or **Pairwise-Distance**. No novelty claim is made for the common mechanism itself or for the global \(2k\) theorem.

## Limitations
This is a sharp welfare statement only for the minimum nontrivial population \(n=k+1\) on a line. It says nothing about truthful incentives when \(k\ge4\), arbitrary metric spaces, weighted agents, or the worst case for \(n\ge k+2\). The upper bound is a strict finite-profile bound with a supremum, not an attained maximum. The complete text of the earlier Jia preprint could not be inspected, so priority against a finite-population result possibly appearing in its uninspected portions remains uncertain; independent scientific audit is not claimed.

## References
1. J. Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633, first submitted 2026-08-20.
2. H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first submitted 2026-08-23.
3. H. Aziz, S. Mackenzie, and M. Suzuki, *Anchoring for Truthfulness: The Random-Anchor Volume Mechanism for Multi-Facility Location*, arXiv:2608.16550, first submitted 2026-08-17.
