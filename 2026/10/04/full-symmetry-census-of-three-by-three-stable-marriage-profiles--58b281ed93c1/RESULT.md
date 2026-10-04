# Full-symmetry census of three-by-three stable-marriage profiles
## Finding
Consider the strict stable-marriage problem with three agents on each side. Two preference profiles are identified when one can be obtained from the other by independently relabeling the two sides and, optionally, exchanging the two sides. The resulting symmetry group is
\[
(S_3\times S_3)\rtimes C_2,
\]
of order \(72\).

There are exactly \(669\) profile classes under this full symmetry. Their distribution by number of stable matchings is
\[
491\text{ classes with one stable matching},\qquad
161\text{ classes with two},\qquad
17\text{ classes with three}.
\]
The corresponding labeled-profile counts are \(34080\), \(11484\), and \(1092\), respectively.

The \(17\) classes attaining three stable matchings have a further exact symmetry stratification: \(14\) have orbit size \(72\), two have orbit size \(36\), and one has orbit size \(12\). Thus their stabilizer orders are \(1\), \(2\), and \(6\). A representative of the unique stabilizer-order-\(6\) class is the cyclic profile
\[
\begin{array}{c|c}
\text{left side} & \text{preference order on the right side}\\
0 & 0,1,2\\
1 & 1,2,0\\
2 & 2,0,1
\end{array}
\qquad
\begin{array}{c|c}
\text{right side} & \text{preference order on the left side}\\
0 & 1,2,0\\
1 & 2,0,1\\
2 & 0,1,2.
\end{array}
\]

## Assumptions and scope
Each of the six agents has a strict total order over the three agents on the opposite side. A matching is stable when it has no blocking pair. The quotient regards names as irrelevant and also regards exchanging the two sides as an isomorphism.

The result is a complete finite census for size three only. It does not claim a formula for arbitrary market size, nor does it cover ties, incomplete lists, capacities, or many-to-one matching.

## Proof
Each agent has \(3!=6\) strict preference lists, so there are exactly
\[
6^6=46656
\]
labeled profiles. For every profile the verifier checks all \(3!=6\) perfect matchings and every unmatched cross-pair, so the stable-matching count is exhaustive rather than sampled.

For the quotient calculation, the verifier uses two independent exact routes. First, it partitions the \(46656\) profiles into orbits using five generators: a transposition and a 3-cycle on each side, together with side exchange. These generate the full group \((S_3\times S_3)\rtimes C_2\). Stable-matching count is checked to be constant on every orbit. This route gives \(669\) total classes, split \(491,161,17\), and gives the orbit-size distribution stated above.

Second, independently of those orbit representatives, the verifier applies Burnside's lemma. For each of the \(72\) group elements it counts the fixed labeled profiles separately within the one-, two-, and three-stable strata. Dividing the three fixed-point sums by \(72\) again gives
\[
491,\quad161,\quad17.
\]
The two routes therefore agree exactly.

As a further consistency check, weighting each orbit class by its orbit size reconstructs the complete labeled distribution
\[
34080,\quad11484,\quad1092,
\]
which agrees with the published labeled census.

## Verification
Run

`python3 verify_stable_marriage_orbits.py`

The verifier uses only exact integer operations and exhaustive finite loops. It returns `VERIFY_OK`, independently reproduces the quotient counts via orbit generation and Burnside's lemma, reconstructs the published labeled totals, and verifies the unique orbit-size-\(12\) three-stable representative.

## Relationship to prior work
Gale and Shapley introduced the strict two-sided stability model and proved existence of a stable matching in 1962. A later complete labeled enumeration by Borodin and coauthors reports, for three agents per side, exactly \(34080\), \(11484\), and \(1092\) labeled profiles with one, two, and three stable matchings. That paper also explicitly discusses relabeling the two sides and exchanging them as natural symmetries, but its enumerated stable-matching table is labeled rather than quotiented by the full symmetry group.

The present contribution is the symmetry-reduced census and stabilizer stratification. Searches for the exact totals \(669\), \(491,161,17\), the full two-sided relabeling quotient, and the three-stable orbit-size distribution did not locate an equivalent published table.

## Limitations
The census is specific to three-by-three strict instances. Although the enumeration is exhaustive, absence from the searched literature does not rule out an unindexed computation, thesis, course note, or software table containing the same quotient counts.

## References
1. D. Gale and L. S. Shapley, “College Admissions and the Stability of Marriage,” *American Mathematical Monthly* 69(1) (1962), 9–15. DOI: 10.1080/00029890.1962.11989827.
2. M. Borodin, E. Chen, A. Duncan, T. Khovanova, B. Litchev, J. Liu, V. Moroz, M. Qian, R. Raghavan, G. Rastogi, and M. Voigt, “Sequences of the Stable Matching Problem,” arXiv:2201.00645v1, first submitted 2021-12-29.
