# The complete four-agent random-priority matching-lottery spectrum

## Finding
Consider four labeled agents and four labeled indivisible objects. Each agent reports a **complete strict ranking** of the four objects. Random serial dictatorship (RSD, also called random priority) chooses each of the \(24\) agent orders with probability \(1/24\); in the selected order each agent takes the most-preferred available object. Every realized assignment is a perfect matching.

For a preference profile \(R\) and perfect matching \(\mu\), let
\[
 c_R(\mu)=\#\{\sigma\in S_4:\text{serial dictatorship under order }\sigma\text{ produces }\mu\}.
\]
The **matching-lottery signature** \(\lambda(R)\) is the weakly decreasing tuple of all positive integers \(c_R(\mu)\). It is a partition of \(24\); dividing the entries by \(24\) gives the multiset of positive probabilities of distinct deterministic matchings in the RSD lottery. In particular \(K(R)=|\lambda(R)|\) counts its ex-post matching support, *not* the number of nonzero agent-object probabilities in its marginal assignment matrix.

**Exact finite classification.** As \(R\) varies through all \(24^4=331{,}776\) labeled complete strict profiles, there are exactly **57 distinct matching-lottery signatures**. The file `spectrum.csv` is the complete, exact list, with for every signature the number of labeled profiles that realize it; no signatures outside this file occur. In particular, the possible positive support sizes are exactly
\[
\boxed{\{1,2,3,4,5,6,7,8,9,10,11,12,14,16,18,24\}}.
\]
Thus support sizes \(13,15,17,19,20,21,22,23\) are impossible. The full support-size distribution is:

| \(K\) | Labeled profiles | \(K\) | Labeled profiles |
|---:|---:|---:|---:|
| 1 | 31,104 | 2 | 20,736 |
| 3 | 20,736 | 4 | 53,856 |
| 5 | 48,384 | 6 | 40,032 |
| 7 | 45,504 | 8 | 26,568 |
| 9 | 12,672 | 10 | 15,120 |
| 11 | 6,336 | 12 | 5,880 |
| 14 | 4,032 | 16 | 216 |
| 18 | 576 | 24 | 24 |

For uniformly sampled labeled complete strict profiles, the exact first two moments are
\[
\boxed{\mathbb E[K]=\frac{1597}{288},\qquad
\operatorname{Var}(K)=\frac{684839}{82944}}.
\]
Support size \(1\) occurs precisely when all four first choices differ; this gives \(4!\,6^4=31{,}104\) profiles. Support size \(24\) occurs precisely when all four full rankings agree, giving exactly \(4!=24\) labeled profiles. Concrete realizations for every permitted support size appear in `support_witnesses.csv`.

## Assumptions and scope
The market is balanced: exactly four agents and four objects, every object is acceptable to every agent, all individual rankings are strict, and agent priorities are uniformly sampled over all \(24\) permutations. Agents and objects are labeled. The results are matching-level: two priority orders are counted as different realizations of the same outcome when they generate the same complete deterministic allocation, and distinct matchings are never merged just because they induce the same marginal lottery probabilities.

The strings in `spectrum.csv` encode multiplicity tuples by semicolon-separated descending positive integers, e.g. `24` is the one-outcome lottery and `1;1;...;1` (24 ones) is uniform over all \(24\) matchings. The second CSV column counts labeled profiles. `support_histogram.csv` aggregates those rows by the number of positive entries. In `support_witnesses.csv`, `ranking_indices` are four semicolon-separated zero-based indices in lexicographic `itertools.permutations(range(4))` order; index \(0\) represents the rank list \((0,1,2,3)\). All files have complete standalone contents.

## Proof
**1. Exhaustive reduction by object relabeling.** Let \(\mathcal P=S_4\) denote the \(24\) strict rankings of the four objects, represented as permutations listing most-preferred first. Every profile belongs to \(\mathcal P^4\). For each such profile there is a **unique** object permutation carrying the first agent's ranking to \((0,1,2,3)\). Object relabeling bijects priority-induced perfect matchings and hence preserves the tuple of their positive multiplicities. The entire labeled domain consequently decomposes into \(24^3=13{,}824\) normalized profiles, each with exactly \(24\) labeled object-relabelings. This normalization does not permute or identify agents.

**2. Explicit finite evaluation.** For every normalized profile \(R=((0,1,2,3),R_2,R_3,R_4)\), run all \(24\) priority orders. For each order, assign the first still-unassigned object in each agent's ranking, record the resulting four-coordinate matching, and count identical matching outcomes. Sort the positive counts decreasingly and add \(24\) to that signature's labeled frequency. Equivalently, the exhaustive integer recurrence is
\[
 H(\lambda)=24\sum_{(R_2,R_3,R_4)\in\mathcal P^3}
 \mathbf 1\{\operatorname{sort}_{\downarrow}(\{c_R(\mu):c_R(\mu)>0\})=\lambda\}.
\]
Here the multiset inside the sort contains the **positive values** of the counts \(c_R(\mu)\). The finite loop has exactly \(24^3\cdot24=331{,}776\) normalized profile/order evaluations; no sampling, extrapolation, approximate floating-point arithmetic or unbounded search is involved.

`verify.py` implements this recurrence and **also** calculates the same matching counter for each of the \(13{,}824\) normalized profiles by a separate recursive remaining-agent/remaining-object choice tree. It checks equality of the full matching counters before aggregating. `verify_full.cpp` evaluates all \(24^4=331{,}776\) labeled profiles directly, using a different implementation of the assignment calculation, and independently computes the complete signature-frequency table. Its output agrees exactly, row for row, with `spectrum.csv`. Therefore every row of that table is an exhaustive integer count over the specified domain, and the lack of any other row is an exhaustive nonexistence statement.

**3. Extraction of the claimed spectrum and moments.** The supplied 57-row CSV consists of exactly the distinct nonzero keys \(\lambda\) in \(H\). The row frequencies sum to \(331{,}776\). Grouping them by tuple length gives exactly the 16 positive support-frequency pairs in the displayed table and exactly the forbidden support sizes. The independently generated `support_histogram.csv` agrees with this aggregation. Summing \(K\) and \(K^2\) with these integral frequencies, dividing by \(331{,}776\), and subtracting the square of the mean yields \(1597/288\) and \(684839/82944\), respectively. The verifier uses rational arithmetic to confirm both fractions.

**4. Structural endpoints.** If four agents have distinct first choices, every order gives all agents their respective first choices and \(K=1\). Conversely, if two agents share a first choice, prioritizing one before the other versus reversing them changes the winner of that contested first object, hence produces at least two different matchings. Counting bijective assignments of top choices and independent orders of the remaining three objects gives \(4!\,6^4\). If all four complete rankings coincide, each priority order assigns its first actor the first-ranked object, its second actor the second-ranked object, and so forth; all \(24\) matchings occur exactly once. The finite exhaustive table shows these are the only \(24\)-support profiles: its 24 labeled occurrences correspond to the single normalized all-identical profile.

**5. Interpretation as a Pareto frontier (known structural equivalence).** Every RSD outcome is Pareto optimal, since a priority order can be followed through to reject a proposed improvement at its first affected agent. Conversely, for a Pareto-optimal perfect matching \(\mu\), draw an edge from the owner of object \(o\) to agent \(i\) whenever \(i\) ranks \(o\) above \(\mu(i)\). A directed cycle would give a Pareto-improving reassignment, so the graph is acyclic. Processing agents in a topological order makes every object preferred by each agent to \(\mu(i)\) already occupied; serial dictatorship therefore produces \(\mu\). This equivalence is classical and is not claimed as a contribution. It means the new support-size census also counts the number of Pareto-optimal perfect matchings at each four-by-four strict profile. `verify_pareto.py` independently checks this statement by comparing all \(24\) possible deterministic assignments under direct Pareto dominance to the RSD support at each of the \(13{,}824\) canonical profiles.

## Verification
All three scripts use exact integer enumeration, and `verify.py` uses `fractions.Fraction` for moment checks. No data file from another record is required.

From the directory containing the embedded files, run:

```sh
python3 verify.py
python3 verify_pareto.py
c++ -std=c++17 -O2 verify_full.cpp -o verify_full
./verify_full > full_output.csv
tail -n +2 spectrum.csv | diff - full_output.csv
```

Successful execution prints `VERIFY_OK` on the three code paths and an empty diff. The full C++ route checks all \(331{,}776\) labeled profiles; the Python route checks all \(13{,}824\) normalized profiles with two independently written matching-outcome procedures; the Pareto cross-check tests the complete \(24\)-matching frontier against RSD support for every normalized profile. `support_witnesses.csv` gives constructive profile witnesses for every allowed support size, verified by `verify.py`. The source programs, their input CSV tables and all necessary standard-library dependencies are supplied.

## Relationship to prior work
RSD and its uniform random-priority definition are classical; serial dictatorship's correspondence with Pareto-optimal matchings was proved in the house-allocation literature. Abraham--Cechlárová--Manlove--Mehlhorn (2004, Section 6) use the term *signature* for a topological priority order of a **single** Pareto-optimal matching, not the sorted **lottery multiplicities across all matchings** used here. Their uniqueness criterion implies the \(K=1\) endpoint but does not yield this four-agent lottery census. Abdulkadiroğlu--Sönmez's all-size equivalence of RSD with core-from-random-endowments is also prior, not a new assertion.

Basteck--Ehlers (first arXiv posting 27 August 2026, arXiv:2608.27261v1) investigate strategy-proofness and precise four-agent random-assignment *waste* bounds, often with unacceptable objects. Their full-paper four-agent arguments concern unassignment and marginal agent-object probabilities, rather than distinct perfect-matchings and their \(24\)-priority multiplicities for four fully acceptable objects. A related 2025 paper by the same authors focuses on incentive and welfare comparisons, not this complete outcome-lottery spectrum.

The previously published three-agent RSD matching-lottery classification gives five shapes on three agents. A distinct published four-agent census gives the incidence of ordinal inefficiency of **marginal** RSD random assignments, and an associated comparison with probabilistic serial. Neither result states the 57 four-agent *matching-level* shapes or the support-size gap, and neither's scalar incidence determines the complete frequency table here. Exhaustive literature and semantic-record searches did not identify an equivalent four-agent table; unindexed calculations remain a residual priority risk.

## Limitations
The conclusion is a complete **finite** theorem for four agents and four objects with strict, complete preferences, not a formula for arbitrary market sizes or incomplete/tied preference lists. The numerical classification is established by bounded exhaustive exact computation supported by independent implementations, not by a short symbolic characterization of all 57 possible partitions. The stated classical equivalences are not novel. Although the cited primary sources and a relevant research-record corpus were compared at the claim level, an unpublished or unindexed enumeration could duplicate the frequency tables. No independent external scientific audit is claimed.

## References
1. C. Basteck and L. Ehlers, *Strategy-Proof and Minimally Wasteful Random Assignment*, arXiv:2608.27261v1, public 27 August 2026. https://arxiv.org/abs/2608.27261.
2. C. Basteck and L. Ehlers, *On (Constrained) Efficiency of Strategy-Proof Random Assignment*, Econometrica 93 (2025), 569–595. DOI: 10.3982/ECTA22762.
3. D. J. Abraham, K. Cechlárová, D. F. Manlove and K. Mehlhorn, *Pareto optimality in house allocation problems*, ISAAC 2004, pp. 3–15. https://eprints.gla.ac.uk/1062/.
4. A. Abdulkadiroğlu and T. Sönmez, *Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems*, Econometrica 66 (1998), 689–701. DOI: 10.2307/2998580.
5. A. Bogomolnaia and H. Moulin, *A New Solution to the Random Assignment Problem*, Journal of Economic Theory 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710.
6. *Complete three-agent lottery-shape classification for random serial dictatorship*, public mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-complete-three-agent-lottery-shape-classification-for-random-ser--7ae5a1139952.
7. *Exact four-agent random-serial-dictatorship ordinal-inefficiency census*, public mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-four-agent-random-serial-dictatorship-ordinal-inefficiency--d63734f44c9c.
