# Six pairs are the sharp boundary for compatibility of minimum-regret and minimum-rank-gap stable marriage

## Finding

**Sharp compatibility theorem.** In every complete, strict, balanced one-to-one stable-marriage instance with \(1\le n\le 5\) men and \(n\) women, there is a stable matching simultaneously minimizing the maximum individual partner rank (minimum regret) and the range of individual partner ranks (minimum rank gap). This is sharp: at \(n=6\), there is an instance where the two sets of optimal stable matchings are disjoint singletons. The quantitative witness has minimum rank gap \(2\), attained at worst rank \(5\), and minimum regret \(4\), attained at rank gap \(3\).

## Assumptions and scope

There are \(n\) men and \(n\) women, and every agent strictly ranks all \(n\) agents of the opposite side. Every matching is a bijection and every agent is matched. A pair outside a matching blocks it when both endpoints strictly prefer each other to their assigned partners. A stable matching has no blocking pair. For a stable matching \(M\), let \(r_a(M)\in\{1,\ldots,n\}\) be the one-based position of agent \(a\)'s partner on that agent's list, and set
\[
R(M)=\max_a r_a(M),\qquad L(M)=\min_a r_a(M),\qquad G(M)=R(M)-L(M).
\]
The two criteria separately minimize \(R\) and \(G\) over all stable matchings. The difference utility-gap criterion of Sheng and Yokoi specializes to \(G\) for the utilities \(v_a=-r_a\). The result concerns strictly ranked, *complete* lists, two equally sized sides, no ties, and a single partner per agent.

## Proof

**Lemma (rank-incidence bound).** For every stable matching \(M\),
\[
\sum_a(r_a(M)-1)\le n(n-1),\qquad L(M)\le\left\lfloor\frac{n+1}{2}\right\rfloor.
\]
For any agent \(a\), precisely \(r_a(M)-1\) opposite-side agents precede the assigned partner. Count all such directed preferred-partner incidences. Every unmatched man–woman pair contributes at most one incidence: if both directions occurred, the pair would block \(M\). There are exactly \(n(n-1)\) unmatched pairs. Thus the sum bound holds. Each of \(2n\) summands is at least \(L(M)-1\), so \(2n(L(M)-1)\le n(n-1)\), yielding the asserted bound.

**Compatibility for \(n\le5\).** For \(n\le4\), the lemma ensures \(L(M)\le2\) in every stable matching. The same is true at \(n=5\) unless a stable matching \(M_0\) has \(L(M_0)=3\). In that exceptional case all ten agents have rank exactly \(3\): the ten rank-offsets are each at least \(2\), whereas the lemma caps their sum at \(20\). Consequently \(G(M_0)=0\), its global minimum, and \(R(M_0)=3\). There cannot be any stable matching \(N\) with \(R(N)\le2\): every pair in \(N\setminus M_0\) would consist of two agents strictly preferring their new partners to their rank-three partners in \(M_0\), so it would block \(M_0\). Hence \(M_0\) also minimizes \(R\).

It remains to consider instances where every stable matching has \(L(M)\le2\). Write \(q=\min_{M\text{ stable}}R(M)\), and choose among the stable matchings with \(R=q\) one, \(M_*\), that minimizes \(G\). Since \(L(M_*)\ge1\), \(G(M_*)\le q-1\). Every stable \(N\) with \(R(N)>q\) has \(R(N)\ge q+1\) and \(L(N)\le2\), whence \(G(N)\ge q-1\ge G(M_*)\). By the choice of \(M_*\) among \(R=q\) matchings, it minimizes \(G\) globally and simultaneously minimizes \(R\). This proves the universal assertion for every \(n\le5\).

**Sharp six-pair construction.** Label both sides \(0,1,2,3,4,5\). Each row gives the complete opposite-side preference list, in *decreasing preference* order; all entries are zero-based identifiers, while utility ranks are one-based.

Men's lists:

| Man | Women, most to least preferred |
|---|---|
| 0 | 3, 5, 0, 1, 2, 4 |
| 1 | 4, 2, 1, 0, 3, 5 |
| 2 | 3, 5, 2, 1, 0, 4 |
| 3 | 0, 4, 3, 2, 5, 1 |
| 4 | 1, 2, 4, 0, 3, 5 |
| 5 | 2, 4, 5, 3, 1, 0 |

Women's lists:

| Woman | Men, most to least preferred |
|---|---|
| 0 | 1, 2, 4, 5, 0, 3 |
| 1 | 0, 2, 3, 5, 1, 4 |
| 2 | 0, 3, 2, 1, 4, 5 |
| 3 | 1, 4, 3, 0, 2, 5 |
| 4 | 0, 2, 4, 1, 3, 5 |
| 5 | 1, 3, 5, 0, 2, 4 |

Specify a perfect matching as the six-tuple of women's identifiers assigned, in order, to men \(0,1,2,3,4,5\). Exhaustive evaluation of all \(6!=720\) perfect matchings yields **exactly seven stable matchings**, with the following complete scores:

| Matching | \(G\) | \(R\) |
|---|---:|---:|
| \((0,1,2,3,4,5)\) | 2 | 5 |
| \((0,4,2,3,1,5)\) | 5 | 6 |
| \((1,0,2,3,4,5)\) | 3 | 4 |
| \((1,0,4,2,3,5)\) | 5 | 6 |
| \((3,1,2,0,4,5)\) | 5 | 6 |
| \((3,4,2,0,1,5)\) | 5 | 6 |
| \((3,4,5,0,1,2)\) | 5 | 6 |

For the identity matching, the complete twelve-agent rank vector (men first, then women) is \((3,3,3,3,3,3,5,5,3,3,3,3)\), yielding \(G=2\) and \(R=5\). For \((1,0,2,3,4,5)\), it is \((4,4,3,3,3,3,1,1,3,3,3,3)\), yielding \(G=3\) and \(R=4\). The first is the *unique* rank-gap minimizer and the second is the *unique* minimum-regret matching. Thus no stable matching jointly optimizes the two criteria at six pairs.

## Verification

The standalone files `verify_witness.py` and `verify_independent.py` implement separate exhaustive checks of all \(720\) six-pair perfect matchings, using respectively direct preference-position tests and independent bitmask-based blocking-pair tests. Both confirm precisely the seven stable matchings displayed above, their exact score pairs, and disjoint singleton optimal sets. `verify_small.py` independently checks all \((3!)^6=46,656\) strict complete three-pair profiles and verifies the existence of a common optimizer in every profile. The universal \(n\le5\) statement is proved analytically above, **not inferred** from finite enumeration. To reproduce with Python 3: run `python verify_witness.py`, `python verify_independent.py`, and `python verify_small.py` in a directory containing the three scripts; each prints `PASS` upon successful assertions.

## Relationship to prior work

Sheng and Yokoi introduced minimum individual utility-gap stable matching and an optimization algorithm covering rank-gap as an explicit special case [1]. They also summarize the classical minimum-regret criterion; their studied optimization problems do not, in the inspected material, give this sharp *joint-compatibility* theorem for complete strict marriage markets. Cooper and Manlove [2] study *regret-equal* stable matchings, but their criterion compares the two sides' worst-off agents, **not** the maximum minus minimum rank over *all* individual agents. Their profile-based algorithms [3] optimize rank-maximal or generous objectives rather than the simultaneous \(R\)/\(G\) criterion. The earlier work establishes these foundational objectives, not an inference that implies the five-pair compatibility and six-pair sharpness stated here.

## Limitations

The proof gives no compatibility guarantee for \(n\ge6\); the witness proves failure *can* occur, not that it must. The universal half of the theorem assumes complete strict preference lists and does not automatically extend to incomplete acceptability, ties, capacities, or utility scales other than partner rank. The witness enumeration is fully finite and exact, but no independent external audit has been performed. Literature comparison establishes originality only to the best of the inspected sources and accessible records, not a proof of global priority.

## References

[1] Yao Sheng and Yu Yokoi, *Stable Matchings with Minimum Utility Gap*, arXiv:2607.07160, first publicly posted July 8, 2026, https://arxiv.org/abs/2607.07160 .

[2] Frances Cooper and David Manlove, *Algorithms for new types of fair stable matchings*, arXiv:2001.10875, https://arxiv.org/abs/2001.10875 .

[3] Frances Cooper and David Manlove, *Two-sided profile-based optimality in the stable marriage problem*, arXiv:1905.06626, https://arxiv.org/abs/1905.06626 .
