# A sharp type-blindness threshold for three-site mixed-cost committees

## Finding

Let \(X=\{v_0,v_1,v_2\}\) be three **distinct** points in any metric space, with one equally weighted agent at each point. Exactly two distinct sites must be selected as facilities, and the available facility sites are exactly \(X\). Every agent independently has one of two cost types: average distance to the two selected facilities, or maximum distance to them. Social cost is the sum of the three individual costs. The locations are known, but the type assignment need not be known.

Write the three pairwise distances, in nondecreasing order, as \(0<p\le r\le q\), where the triangle inequality requires \(q\le p+r\). There exists a **single facility pair minimizing social cost simultaneously for all eight type assignments** if and only if

\[
\boxed{3p\le q+r.}
\]

When the inequality holds, **any pair at distance \(p\)** is universally optimal. When it fails, no universally optimal pair exists; although every shortest-distance pair optimizes both homogeneous objectives (all-average and all-maximum), a mixed type profile defeats each such pair.

In particular, for three distinct collinear sites, one may always select the two sites separated by the smaller adjacent gap, independently of types. This collinear type-blind optimality does not extend to four sites on the line: at sites \(0,1,3,4\), all-average agents uniquely prefer the facility pair \(\{1,3\}\), whereas all-maximum agents prefer exactly \(\{0,1\}\) and \(\{3,4\}\).

## Assumptions and scope

There are precisely three agent-site pairs, one per distinct site, with unit social weights. The facility set is fixed to those three sites, and the decision is an unordered set of exactly two **distinct** facilities. The two cost types are

\[
S_i(F)=\frac12\sum_{v\in F}d(v_i,v),\qquad
M_i(F)=\max_{v\in F}d(v_i,v).
\]

A type profile \(t=(t_0,t_1,t_2)\in\{0,1\}^3\) specifies \(S_i\) at \(t_i=0\) and \(M_i\) at \(t_i=1\). Define \(C_t(F)=\sum_{i=0}^2[(1-t_i)S_i(F)+t_iM_i(F)]\). A pair \(F\) is called *universally optimal* when \(C_t(F)=\min_{|F'|=2}C_t(F')\) for every \(t\in\{0,1\}^3\), allowing ties.

Relabel sites so that \(d(v_0,v_1)=p\), \(d(v_1,v_2)=r\), and \(d(v_0,v_2)=q\). Put \(A=\{v_0,v_1\}\), \(B=\{v_1,v_2\}\), and \(C=\{v_0,v_2\}\). This relabeling is always possible for a triangle, including distance ties.

## Proof

For an all-average profile, twice the social cost for \(A,B,C\), respectively, is

\[
2C_{000}(A)=2p+q+r,\quad
2C_{000}(B)=p+q+2r,\quad
2C_{000}(C)=p+r+2q.
\]

Changing agent \(i\) from average type to maximum type adds half of the following quantity to the cost:

| Pair | Agent \(0\) | Agent \(1\) | Agent \(2\) |
|---|---:|---:|---:|
| \(A\) | \(p\) | \(p\) | \(q-r\) |
| \(B\) | \(q-p\) | \(r\) | \(r\) |
| \(C\) | \(q\) | \(r-p\) | \(q\) |

These are exact identities, since the maximum of two nonnegative distances minus their mean equals half their absolute difference. Therefore, for every type vector \(t\),

\[
\begin{aligned}
2(C_t(A)-C_t(B))
  &=(p-r)+(2p-q)t_0+(p-r)t_1+(q-2r)t_2,\\
2(C_t(A)-C_t(C))
  &=(p-q)+(p-q)t_0+(2p-r)t_1-rt_2.
\end{aligned}
\]

Because \(p\le r\le q\le p+r\le2r\), the coefficients of \(t_1,t_2\) in the first line and those of \(t_0,t_2\) in the second are nonpositive. Maximizing the two differences independently over all eight type profiles gives

\[
\begin{aligned}
\max_t 2(C_t(A)-C_t(B))&=p-r+\max\{0,2p-q\},\\
\max_t 2(C_t(A)-C_t(C))&=p-q+\max\{0,2p-r\}.
\end{aligned}
\]

Both quantities are nonpositive exactly when \(3p\le q+r\): if the expression in braces is positive, the relevant inequality becomes \(3p\le q+r\); if it is zero, the other inequalities follow from the distance ordering. Consequently, \(A\) minimizes \(C_t\) for *all* type profiles exactly in this parameter region. Relabeling proves the same statement for every shortest pair.

Conversely, when \(3p>q+r\), the all-average optimum must be a shortest pair (the displayed all-average costs strictly increase with the chosen edge length). For any selected shortest pair \(A\), relabel its endpoints as above and take the type profile \(t=(1,0,0)\). Since \(3p>q+r\) also implies \(2p>q\), the first difference identity becomes

\[
C_t(A)-C_t(B)=\frac{3p-q-r}{2}>0.
\]

Thus that pair fails under a mixed assignment, even if multiple shortest pairs tie. No nonshortest pair can be universal, because it is suboptimal for the all-average profile. This proves the equivalence, including all distance ties and the threshold equality.

For comparison, the all-maximum costs are \(C_{111}(A)=2p+q\), \(C_{111}(B)=2r+q\), and \(C_{111}(C)=2q+r\), so every shortest pair is optimal for both homogeneous types. The mixed-profile obstruction above is therefore genuinely caused by heterogeneous types, not merely by a disagreement between the two homogeneous optima.

For three collinear sites with positive adjacent gaps \(a,b\), the distance multiset is \(\{a,b,a+b\}\). Setting \(p=\min(a,b)\), \(r=\max(a,b)\), \(q=a+b\), one has \(q+r=p+2r\ge3p\); hence the closer adjacent pair is universally optimal.

The necessity is realized by the metric triangle \((p,r,q)=(3,4,4)\): the all-average and all-maximum profiles uniquely favor \(A\); with only agent \(0\) maximum-type, \(C_t(A)=17/2\) and \(C_t(B)=8\). On the four-point line \(\{0,1,3,4\}\), all-average cost is uniquely minimized by \(\{1,3\}\) at value \(6\), whereas all-maximum cost has minimum \(9\), attained only at \(\{0,1\}\) and \(\{3,4\}\); the all-maximum cost of \(\{1,3\}\) is \(10\). These are exact counterexamples to the indicated extensions.

## Verification

The standalone standard-library Python script `verify.py` checks all eight type vectors for every ordered integer metric triangle with \(1\le p\le r\le q\le44\), giving \(8{,}327\) distinct integer triangle triples, plus \(3{,}339\) seeded rational metric triples. It directly verifies both affine difference identities, the if-and-only-if condition, and both boundary examples. All checks passed. Execute using `python3 verify.py`.

The infinite family result is proved by the displayed symbolic identities and inequalities, **not** by bounded enumeration or randomized testing.

## Relationship to prior work

Gruszecki and Anshelevich, *Strategyproof Facility Location and Committee Selection with Mixed Max and Sum Agent Types* (arXiv:2606.26074, first submitted 2026-06-24), establish general type-independent approximation guarantees for arbitrary metrics and characterize an unrestricted collinear setting in which facilities may co-locate. This result instead obtains an exact **zero-loss criterion** when three distinct report sites are the only available facilities and selected facilities must be distinct. Their unrestricted median-co-location theorem does not imply the current constrained-site threshold.

Deligkas, Lotfi and Voudouris, *Agent-constrained truthful facility location games* (2025), analyze homogeneous sum and homogeneous max variants separately under strategic location reporting; they establish, in particular, the nearest-to-median structure for the homogeneous sum variant with three collinear agents. The classification here differs by requiring one pair to optimize **all heterogeneous type mixtures**, under known positions and a fixed site set.

Han and Anshelevich, *Compatibility of Max and Sum Objectives for Committee Selection and \(k\)-Facility Location* (arXiv:2507.17063, 2025), study simultaneous approximate optimization of homogeneous objective pairs. Even a pair optimal for both homogeneous social costs need not be optimal for heterogeneous mixtures: the metric \((3,4,4)\) exhibits this distinction. Their full text was not inspected, so an unrecognized specific small-instance corollary remains a literature risk.

## Limitations

This is a classification only for three distinct agent sites, exactly two distinct facilities, unit agent weights, and the two stated cost types. It does not claim strategyproofness with privately reported *locations*, general market-size type-blind optimality, or robustness to additional candidate sites. The classification answers existence of a universal optimum, not worst-case approximation when universal optimality fails. Independent audit has not been performed. An unindexed exact equivalent remains possible.

## References

1. Y. Gruszecki and E. Anshelevich. *Strategyproof Facility Location and Committee Selection with Mixed Max and Sum Agent Types*. arXiv:2606.26074 (2026-06-24). https://arxiv.org/abs/2606.26074 ; CC BY 4.0 author-uploaded full text: https://www.researchgate.net/publication/408048091_Strategyproof_Facility_Location_and_Committee_Selection_with_Mixed_Max_and_Sum_Agent_Types
2. A. Deligkas, M. Lotfi, and A. A. Voudouris. *Agent-constrained truthful facility location games*. *Journal of Combinatorial Optimization* 49, 24 (2025). https://doi.org/10.1007/s10878-025-01258-7 ; preprint arXiv:2405.05197 (2024).
3. Y. Han and E. Anshelevich. *Compatibility of Max and Sum Objectives for Committee Selection and \(k\)-Facility Location*. arXiv:2507.17063 (2025-07-22). https://arxiv.org/abs/2507.17063
