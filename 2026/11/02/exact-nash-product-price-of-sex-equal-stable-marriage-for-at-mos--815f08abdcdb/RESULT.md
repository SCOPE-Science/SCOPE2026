# Exact Nash-product price of sex-equal stable marriage for at most three pairs

## Finding

In a classical complete, strict, balanced stable-marriage instance with \(n\) participants on each side, write \(r_a(M)\) for the zero-based rank (best rank zero) assigned to participant \(a\) by a stable perfect matching \(M\). Following the positive rank-utility model, define
\[
u_a(M)=n-r_a(M),\qquad P(M)=\prod_a u_a(M).
\]
The two-sided aggregate-rank disparity is
\[
\Delta(M)=\left|\sum_{m}r_m(M)-\sum_{w}r_w(M)\right|.
\]
With \(\mathcal S(I)\) denoting all stable matchings, define
\[
P_*(I)=\max_{M\in\mathcal S(I)}P(M),\qquad
P_{\mathrm{SE}}(I)=\max_{\substack{M\in\mathcal S(I)\\\Delta(M)=\min_{N\in\mathcal S(I)}\Delta(N)}}P(M).
\]
The second definition uses the best Nash product **among all sex-equal optima**: no unfavorable tie-breaking is assumed.

**Theorem.** Every instance with \(n\le2\) satisfies \(P_*(I)=P_{\mathrm{SE}}(I)\). For \(n=3\),
\[
\boxed{\max_I\frac{P_*(I)}{P_{\mathrm{SE}}(I)}=\frac94.}
\]
In fact the complete ratio distribution over the \(6^6=46{,}656\) labeled three-pair preference profiles is

| Nash-product ratio | Profiles | Full-label-and-side-swap orbits |
|---|---:|---:|
| \(1\) | 44136 | 634 |
| \(9/8\) | 504 | 7 |
| \(3/2\) | 1728 | 24 |
| \(2\) | 144 | 2 |
| \(9/4\) | 144 | 2 |

Thus exactly \(2520\) profiles have a genuine Nash-product penalty from requiring minimum rank disparity. The sharp class consists of two symmetry orbits of \(72\) profiles each. The corresponding geometric-mean Nash-welfare ratio is \((9/4)^{1/6}\), not \(9/4\); the latter is a **product ratio**.

## Assumptions and scope

All members of either side strictly rank all members of the opposite side; each agent is assigned exactly one partner. Stability is absence of a blocking man-woman pair who strictly prefer each other to their assigned partners. The theorem covers every labeled profile for \(n\in\{1,2,3\}\), and no larger market. All computations use exact positive integer Nash products and exact rational ratios. Both objectives are optimized only over stable perfect matchings, with all ties retained before selecting the highest Nash product among minimum-disparity matchings.

## Proof

For \(n=1\), there is a single matching. For \(n=2\), if there are two stable matchings, both agents on one side strictly favor one and both agents on the other side favor the other (the proposer-optimal and receiver-optimal endpoints). Thus in the two matchings the side rank sums are \((0,2)\) and \((2,0)\); both have disparity \(2\) and Nash product \(4\). If there is only one stable matching both optima coincide. This proves the first assertion.

The remaining assertions admit a complete, finite exhaustive proof using the two standalone standard-library programs included with this result. A three-person strict preference order is one of the six permutations of three labels, so the six distinct preference lists on both sides give exactly
\[
(3!)^{6}=46656
\]
labeled profiles. The first program enumerates these profiles with no sampling, omission, or pruning. For each profile it enumerates all \(3!=6\) possible perfect matchings and rejects a matching if and only if some unmatched pair \((i,j)\) meets the two strict-rank inequalities
\[
r_{m_i}(w_j)<r_{m_i}(M(m_i)),\qquad
r_{w_j}(m_i)<r_{w_j}(M(w_j)).
\]
For each remaining stable matching it calculates the two integer side rank sums and \(P\); it then takes the minimum \(\Delta\), the maximum \(P\) overall, and the maximum \(P\) restricted to that minimum \(\Delta\). Their exact ratio is classified using reduced integer fractions. The exhaustive count is exactly the table above, including \(144\) maximizers with ratio \(9/4\) and zero profiles with a larger ratio. It independently reproduces the established marginal counts \((34080,11484,1092)\) of instances with one, two, or three stable matchings.

A second, independently coded finite proof checks each orbit under all permutations of male and female labels and under exchange of the two sides. Every orbit size is computed by the set of its \(72\) transformations, and the entire labeled space is partitioned into \(669\) orbits. With a separate list-position blocking-pair test, one representative of each orbit is scored; weighting by orbit size reproduces all five counts. The two maximizing orbits have sizes \(72\) and \(72\). These independent enumerations agree and cover the full finite domain, not a sample.

For an explicit sharp witness use candidates \(A,B,C\), men \(1,2,3\), and strict preferences
\[
\begin{array}{lll}
 m_1:A\succ B\succ C,&m_2:A\succ B\succ C,&m_3:A\succ C\succ B,\\
 A:1\succ2\succ3,&B:3\succ1\succ2,&C:2\succ1\succ3.
\end{array}
\]
Exhaustive blocking-pair checks leave exactly two stable matchings. Giving the women matched to men \((1,2,3)\) in order, the first is \((A,B,C)\), with men's rank sum \(2\), women's rank sum \(4\), \(\Delta=2\), and \(P=36\). The second is \((A,C,B)\), with rank sums \(4\) and \(0\), \(\Delta=4\), and \(P=81\). Consequently the former is uniquely sex-equal optimal, the latter uniquely Nash optimal, and \(81/36=9/4\) proves attainability.

## Verification

Run from this file's directory with Python 3 and no external dependencies:

```bash
python3 verify_price.py
python3 verify_orbits.py
```

The first checker performs all \(46656\) three-pair profile evaluations, the \(16\) two-pair cases and the singleton case, verifies all five rational-frequency cells, checks the stable-matching multiplicities, and verifies the explicit witness. The second checker independently generates the \(669\) label/side-swap orbits, evaluates all their representatives with a separately written stability test, and reobtains the exact weighted ratio distribution. Both were run from these supplied code files with successful assertions and expected completion lines.

## Relationship to prior work

Desai, Rasheed, Ghalme, and Gujar (2026) introduce optimization of positive rank-induced Nash social welfare among stable matchings, discuss sex equality as a competing objective, give a polynomial-time Nash-optimization algorithm, and explicitly leave theoretical cross-objective guarantees to future work. That optimization algorithm does not by itself yield the exact worst-case ratio \(9/4\) or the complete small-market distribution.

Iwama, Miyazaki, and Yanagisawa (2010) study algorithms for minimizing sex-equality rank disparity, including additional egalitarian criteria; this is a different cost comparison. Borodin and coauthors (2024) enumerate several stable-marriage preference-profile statistics, including stable-matching multiplicities and egalitarian-cost distributions, but not the Nash-product price under sex-equal optimization. A published finite census entitled *Sharp first conflict between egalitarian and sex-equal stable marriage* gives \(2520\) disjoint egalitarian/sex-equal profiles at three pairs, but does not supply Nash-product ratios. The separate statement that Nash-optimal three-pair stable matchings are egalitarian-optimal does not itself determine the highest Nash product among sex-equal solutions.

## Limitations

This is an exhaustive finite-market theorem; no claim for \(n\ge4\), incomplete preferences, ties, unequal sides, or alternative cardinal utilities is made. A finite exact computation is an exhaustive proof only because both programs cover every profile and every possible matching in the stated finite domain. It cannot imply analogous infinite-market statements. The result's priority remains subject to independent assessment; other unpublished or unindexed tables could overlap. No independent scientific audit is claimed.

## References

1. P. Desai, M. Rasheed, G. Ghalme and S. Gujar, *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1, first submitted 2026-09-02. https://arxiv.org/abs/2609.02354
2. K. Iwama, S. Miyazaki and H. Yanagisawa, *Approximation Algorithms for the Sex-Equal Stable Marriage Problem*, ACM Transactions on Algorithms 7 (2010), article 2. DOI:10.1145/1868237.1868239.
3. M. Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, arXiv:2201.00645. https://arxiv.org/abs/2201.00645
4. *Sharp first conflict between egalitarian and sex-equal stable marriage*, public mathematical research record, identifier 8fdd6836ad87 (2026), in the published-finding corpus research corpus. https://github.com/Resultary/2026
