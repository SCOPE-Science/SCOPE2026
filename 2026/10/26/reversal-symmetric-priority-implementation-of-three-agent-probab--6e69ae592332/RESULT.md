# Reversal-symmetric priority implementation of three-agent probabilistic serial

## Finding

Fix a square, strict, one-sided house-allocation market with \(n\in\{2,3\}\) agents and \(n\) indivisible objects. Let \(P^{\mathrm{PS}}\) be the assignment matrix of probabilistic serial (PS). There is an explicit **preference-profile-dependent, reversal-symmetric** probability distribution on serial-dictatorship priority orders whose induced assignment matrix is exactly \(P^{\mathrm{PS}}\). Consequently this particular decomposition of PS is decomposition-envy-free (Dec-EF), and every realized assignment is Pareto efficient.

For \(n=3\), use this complete rule. If two agents have the same first-choice object, their full rankings differ, and the third agent has another first choice, assign probability \(1/4\) to each of the four priority orders with the third agent **first or last** and probability zero to the two other orders. In every other three-agent profile, assign probability \(1/6\) to each of the six orders. With two agents, use either priority order with probability \(1/2\).

Exactly \(72\) of the \(6^3=216\) labeled strict three-agent profiles use the four-order rule, in two isomorphism classes (\(36\) profiles each) under independent agent and object relabeling; on all remaining \(144\), uniform random priority itself equals PS. The four-order rule differs from uniform random priority precisely in these \(72\) profiles. At any such profile, two agents' marginal lotteries differ from uniform-priority lotteries by total-variation distance \(1/12\) each and the third agrees.

The positive statement is **sharp in number of agents within the reversal-symmetric serial-dictatorship representation class**: a four-agent counterexample is already in Kawase, Suksompong, Sumita and Yokoi (2026), Example 5. That negative example is prior work, not a new theorem here. The present finding is the explicit complete three-agent positive construction and its exact profile classification.

## Assumptions and scope

Preferences are strict permutations of the \(n\) objects; each object has one seat. In serial dictatorship, agents, in the selected priority order, irrevocably take their highest-ranked available object. In PS, every agent simultaneously consumes her currently best available object at unit speed, switching when capacity is exhausted, until each has one unit. A **priority law** is reversal-symmetric if each permutation \(\sigma\) and its reverse \(\sigma^{\mathrm{rev}}\) have equal probabilities. A decomposition is Dec-EF if for every ordered pair of distinct agents \((i,j)\), the probability that agent \(i\) strictly prefers the realized object of \(j\) to her own is at most \(1/2\).

The claim concerns exact *assignment-matrix implementation* using a possibly profile-dependent lottery on priority orders. It does not claim that the resulting mechanism is strategyproof, nor does it claim that all SD-envy-free matrices can be represented through such priority laws. The source's four-agent counterexample limits this particular representation, not Dec-EF decomposability in general.

## Proof

**Reversal symmetry implies Dec-EF.** Fix two distinct agents \(i,j\). Whenever \(i\) precedes \(j\) in serial dictatorship, \(i\)'s chosen object is at least as preferred by \(i\) as \(j\)'s subsequently chosen object. Reversal pairs each priority where \(i\) precedes \(j\) with one where \(j\) precedes \(i\) of identical probability. Hence the probability that \(i\) envies \(j\) is at most \(1/2\). In particular, the proposed rule, which is uniform on a reversal-closed set of four or six orders, has Dec-EF.

**Exact PS equality for three agents.** Each profile can be relabeled using arbitrary permutations of the three agents and three objects. The following is a complete table of orbit representatives, sizes, and exact PS matrices. Here `012` means \(a\succ b\succ c\), `021` means \(a\succ c\succ b\), etc.; the three codes in the first column are the respective agents' rankings. Rows and columns of the displayed matrices are in the listed agent and object order. `4` means the four-order rule above; `6` means uniform priority. Every displayed matrix is also the expected serial-dictatorship assignment under its indicated priority law.

| Preference profile | Orbit size | Orders | Exact common assignment matrix (rows separated by semicolons) |
| --- | ---: | ---: | --- |
| `012 012 012` | 6 | 6 | \((1/3,1/3,1/3);(1/3,1/3,1/3);(1/3,1/3,1/3)\) |
| `012 012 021` | 18 | 6 | \((1/3,1/2,1/6);(1/3,1/2,1/6);(1/3,0,2/3)\) |
| `012 012 102` | 18 | 6 | \((1/2,1/6,1/3);(1/2,1/6,1/3);(0,2/3,1/3)\) |
| `012 012 120` | 18 | 6 | \((1/2,1/6,1/3);(1/2,1/6,1/3);(0,2/3,1/3)\) |
| `012 012 201` | 18 | 6 | \((1/2,1/2,0);(1/2,1/2,0);(0,0,1)\) |
| `012 012 210` | 18 | 6 | \((1/2,1/2,0);(1/2,1/2,0);(0,0,1)\) |
| `012 021 102` | 36 | 4 | \((1/2,1/4,1/4);(1/2,0,1/2);(0,3/4,1/4)\) |
| `012 021 120` | 36 | 4 | \((1/2,1/4,1/4);(1/2,0,1/2);(0,3/4,1/4)\) |
| `012 102 201` | 36 | 6 | \((1,0,0);(0,1,0);(0,0,1)\) |
| `012 120 201` | 12 | 6 | \((1,0,0);(0,1,0);(0,0,1)\) |

All entries are exact rational numbers. To verify any row from the definitions, repeatedly find the agents' currently chosen objects, let \(k_o\) be the number eating object \(o\) and \(r_o\) its remaining capacity, advance the clock by \(\min_{o:k_o>0}r_o/k_o\), and allocate the corresponding fractions. Separately, run serial dictatorship for the four or six specified priority orders and average their deterministic permutation matrices. This gives the identical displayed matrix in each row; the embedded checker performs both calculations independently with fractions. The ten orbits are disjoint because each profile is canonically minimized over all \(3!\) agent and \(3!\) object relabelings, and their sizes add to \(216\); thus no profile is omitted. The \(n=2\) verification covers its four strict labeled profiles.

For a representative exceptional profile, \((a\succ b\succ c,\ a\succ c\succ b,\ b\succ a\succ c)\), the singleton-first-choice agent is the third agent. The allowed priorities are \((3,1,2),(3,2,1),(1,2,3),(2,1,3)\), each with weight \(1/4\). Direct serial dictatorship yields
\[
P^{\mathrm{PS}}=\begin{pmatrix}1/2&1/4&1/4\\1/2&0&1/2\\0&3/4&1/4\end{pmatrix}.
\]
In contrast, the ordinary uniform-priority matrix is
\[
P^{\mathrm{RP}}=\begin{pmatrix}1/2&1/6&1/3\\1/2&0&1/2\\0&5/6&1/6\end{pmatrix}.
\]
The two affected agents therefore have total variation \(\tfrac12(1/12+1/12)=1/12\), and the same occurs throughout the two exceptional relabeling classes. This proves both necessity of modifying **uniform** priority on these profiles and all exact profile counts. It does **not** establish minimal support among all possible reversal-symmetric implementations.

**Sharpness boundary credited to prior literature.** Example 5 of Kawase et al. has four preference orders \((abcd,abcd,acbd,cabd)\). PS assigns the third agent objects \(a,b\) with total probability \(1/3+1/12=5/12\), whereas among each reversal pair of serial-dictatorship priorities the third agent gets \(a\) or \(b\) in exactly one priority. Thus any reversal-symmetric priority law would give \(1/2\), an impossibility. The source already establishes this four-agent obstruction, so only the positive three-agent resolution is proposed as new.

## Verification

Run `python3 verify_ps_reversal_three.py` (Python 3 standard library only). The program checks each of the \(216\) labeled three-agent profiles and the four two-agent profiles. It computes PS by exact event-driven fractional consumption and the proposed serial-dictatorship mixture by exact averaging; it independently checks reversal symmetry and all ordered-pair Dec-EF inequalities, canonicalizes the complete profile space under relabeling, checks the \(72/144\) division and the two exceptional classes, and confirms the four-agent source obstruction by checking all twelve reversal pairs. The successful final output line is `ALL EXACT CHECKS PASSED`. The finite enumeration is exhaustive over the stated domain, not an extrapolation to larger populations.

## Relationship to prior work

Bogomolnaia and Moulin (2001) introduced probabilistic serial and random priority and established the stochastic-dominance fairness properties of PS. Hosseini, Larson and Cohen (2015) compare PS to uniformly random serial dictatorship, including examples of differing allocations. A previously published complete small-market census gives \(144\) equal and \(72\) nonidentical PS/uniform-RSD matrices for three agents; that exact baseline division is **not** claimed as new. Kawase et al. (2026) prove the stronger existence statement that *every* SD-envy-free matrix with at most three agents has **some** Dec-EF decomposition, and separately exhibit the four-agent failure of reversal-symmetric serial dictatorship. Their proof does not provide the present constructive priority-law realization of PS at three agents, its four-priority exception, or the complete priority-law case classification.

The new assertion is specifically that the **PS matrices**, rather than arbitrary SD-envy-free matrices, admit an implementation using only Pareto-efficient serial-dictatorship outcomes under a reversal-symmetric, explicitly computable priority law at all three-agent profiles. This is a strict implementation requirement not entailed by general EF-decomposability. Full-text comparisons and targeted mathematical-record queries did not reveal an equivalent formula; this is a bounded priority assessment, not a proof of historical uniqueness.

## Limitations

The exact constructive theorem is limited to square assignment, two or three agents, strict full rankings, fixed unit capacities, and reported preferences used to choose the priority lottery. It does not assert incentive compatibility, the impossibility of non-reversal-symmetric implementation at four agents, an optimal minimum number of used priority orders, or an analogous classification for larger markets. The four-agent obstruction is from cited prior work, and PS fairness from Bogomolnaia–Moulin is prior work. The finite proof is reproducible computational mathematics, not an independent formal verification. Unindexed or unpublished precedence remains possible.

## References

1. Y. Kawase, W. Suksompong, H. Sumita, Y. Yokoi, *Decomposition Envy-Freeness in Random Assignment*, arXiv:2604.16973, first public 18 April 2026, especially Proposition 1, Theorem 1, and Example 5. https://arxiv.org/html/2604.16973v1
2. A. Bogomolnaia, H. Moulin, *A New Solution to the Random Assignment Problem*, Journal of Economic Theory 100 (2001), 295–328, DOI: 10.1006/jeth.2000.2710.
3. H. Hosseini, K. Larson, R. Cohen, *Random Serial Dictatorship versus Probabilistic Serial Rule: A Tale of Two Random Mechanisms*, arXiv:1503.01488, first public 4 March 2015. https://arxiv.org/html/1503.01488v1
4. *Exact small-market stochastic-dominance census for probabilistic serial versus random serial dictatorship*, public research record: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-small-market-stochastic-dominance-census-for-probabilistic--67db019723a1
5. *Two preference types restore stochastic-dominance envy-freeness of random priority*, public research record: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-preference-types-restore-stochastic-dominance-envy-freeness--6e7d900d7fa1
