# Parity-selective power propagation times of minimum prism monitoring sets

## Finding
For every integer \(n\ge 7\), let \(Y_n=C_n\square K_2\) be the labeled \(n\)-gonal prism. Let \(\mathcal P_n\) be the family of all minimum-cardinality power-dominating vertex sets, and let \(\operatorname{ppt}(Y_n;S)\) count synchronous observation rounds **including** the initial closed-neighborhood observation. The complete latency enumerator of minimum placements is
\[
\Phi_n(z)=\sum_{S\in\mathcal P_n}z^{\operatorname{ppt}(Y_n;S)}=
\begin{cases}
3n\,z^{(n-1)/2}+8n\,z^{(n+1)/2},&n\text{ odd},\\
9n\,z^{n/2}+2n\,z^{n/2+1},&n\text{ even}.
\end{cases}
\]
Thus \(\gamma_P(Y_n)=2\), exactly \(11n\) minimum sets exist, and their propagation times are exactly \(\lfloor n/2\rfloor\) and \(\lfloor n/2\rfloor+1\). The number attaining the fastest time is \(3n\) for odd \(n\) but \(9n\) for even \(n\). The slower counts are respectively \(8n\) and \(2n\).

More precisely, write the prism vertices as \(a_i,b_i\) for \(i\in\mathbb Z/n\mathbb Z\), with cycle edges in each rail and rungs \(a_ib_i\). Two seeds form a minimum power-dominating set exactly when they lie in the same rail with cyclic separation \(d\in\{1,2,3\}\), or in opposite rails with separation \(d\in\{0,1,2\}\) (this eligibility criterion is prior work [2]). When \(n\) is odd, the fastest placements are precisely the opposite-rail pairs with \(d=0\) or \(d=2\). When \(n\) is even, the slowest placements are precisely the same-rail pairs with \(d=2\); every other eligible pair is fastest.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled by the displayed rail/column coordinates. The cycle has \(n\ge7\) columns. For a seed set \(S\), let \(O_1(S)=N[S]\) and for each integer \(t\ge1\) define
\[
O_{t+1}(S)=O_t(S)\cup\bigl\{w\notin O_t(S):\exists v\in O_t(S),\ N(v)\setminus O_t(S)=\{w\}\bigr\}.
\]
A set is power dominating if \(O_t(S)=V(Y_n)\) for some finite \(t\). Its power propagation time is the least such \(t\ge1\). All eligible forces fire simultaneously, based on the previous round, not in an arbitrarily chosen serial order. The domination round counts as one; if it is instead counted as zero, subtract one from every displayed exponent.

## Proof
**Minimum seeds and eligibility.** A singleton \(\{a_i\}\) initially observes only \(a_{i-1},a_i,a_{i+1},b_i\). Every observed boundary vertex has zero or at least two unobserved neighbors, so no force is possible for \(n\ge7\); the same holds by symmetry for \(\{b_i\}\). Girish and Somasundaram [2, Lemma 2] prove, for prisms of order at least five, that a pair is power dominating if and only if its two vertices have graph distance at most three. In the two-rail coordinate system, same-rail distance is cyclic separation \(d\), while opposite-rail distance is \(1+d\). This establishes the six eligible pair types listed in the finding and \(\gamma_P(Y_n)=2\). For each of the three same-rail separations there are \(2n\) unordered pairs; for opposite rails there are \(n\), \(2n\), and \(2n\) pairs at separations zero, one, and two. Therefore \(|\mathcal P_n|=11n\).

**Finite local bases.** Choose the first seed to be \(a_0\) using the rail-exchange, reflection, and rotation symmetries. Express columns temporarily as integer indices before reducing modulo \(n\). The following table specifies each seed-pair representative, the number \(q\) of forcing rounds *after* the domination round, and the integer interval \([\ell,r]\) such that the observed set \(O_{1+q}\) is **exactly** the union of the two full rails over those columns:

| Pair type | Seeds | \(q\) | \([\ell,r]\) | Interval length |
| --- | --- | ---: | --- | ---: |
| same, \(d=1\) | \(a_0,a_1\) | 1 | \([-1,2]\) | 4 |
| same, \(d=2\) | \(a_0,a_2\) | 2 | \([-1,3]\) | 5 |
| same, \(d=3\) | \(a_0,a_3\) | 2 | \([-1,4]\) | 6 |
| opposite, \(d=0\) | \(a_0,b_0\) | 0 | \([-1,1]\) | 3 |
| opposite, \(d=1\) | \(a_0,b_1\) | 1 | \([-1,2]\) | 4 |
| opposite, \(d=2\) | \(a_0,b_2\) | 1 | \([-1,3]\) | 5 |

Here is a direct verification, rather than an inference from numerical experiments. Initially, the top- and bottom-rail observed column sets in these six rows are respectively
\[
([-1,2],[0,1]),\quad([-1,3],\{0,2\}),\quad([-1,4],\{0,3\}),\quad
([-1,1],[-1,1]),\quad([-1,1],[0,2]),\quad([-1,2],[0,3]).
\]
The neighborhood rule first fills the missing bottom-rail columns \(\{-1,2\}\), \(\{1\}\), \(\{1,2\}\), no missing columns, \(\{-1\}\) in the bottom rail plus \(\{2\}\) in the top rail, and \(\{-1\}\) in the bottom plus \(\{3\}\) in the top, respectively. In the second and third rows, one further simultaneous forcing round fills the missing bottom-rail boundary columns \(\{-1,3\}\) and \(\{-1,4\}\), respectively. In every case the observed set at the stated round is exactly the complete interval in the table, with nothing observed outside. For \(n\ge7\), the indicated columns are distinct when needed, and the same local check applies at the shortest cycles.

**Propagation fronts and exact time.** Once an interval of \(L\ge2\) consecutive rungs is completely observed and nothing else is observed, in the next synchronous round exactly its two neighboring rungs become fully observed (or the unique remaining rung if the two frontiers coincide). Indeed, on each rail the two vertices at the endpoints of the observed interval each have exactly one unobserved neighbor in the outward direction, and no vertex outside the interval can act as a forcing vertex. Iterating, the first completion after the local base occurs at
\[
\operatorname{ppt}(Y_n;S)=1+q+\left\lceil\frac{n-L}{2}\right\rceil.
\]
The base table gives the successive times for the six types as
\[
\begin{array}{c|cccccc}
\text{type}&\text{same }1&\text{same }2&\text{same }3&\text{opposite }0&\text{opposite }1&\text{opposite }2\\\hline
\operatorname{ppt}&1+\lceil(n-2)/2\rceil&1+\lceil(n-1)/2\rceil&1+\lceil(n-2)/2\rceil&1+\lceil(n-3)/2\rceil&1+\lceil(n-2)/2\rceil&1+\lceil(n-3)/2\rceil.
\end{array}
\]
There can be no earlier completion: before these rounds at least one entire rung outside the explicitly tracked observed interval remains unseen. For odd \(n\), the opposite-rail types of separation zero and two finish at \(\lfloor n/2\rfloor\), while all others take one additional round. For even \(n\), only same-rail separation two needs the additional round. Applying the counts from the first paragraph yields \(\Phi_n(z)\), as claimed.

## Verification
The accompanying standalone Python 3 program `verify.py` independently constructs every labeled prism of order \(7\) through \(50\), examines every unordered pair of vertices, computes the synchronous closed-neighborhood and forcing rounds, checks eligibility, and checks every exact latency against the parity formulas. It additionally verifies the exact base-interval identities for all six representative configurations at each order and checks singleton failure. The executed program reported:

`VERIFY_OK n=7..50 all_unordered_pairs every_latency_and_nonforcing checked_pdpairs=13794 base_intervals=264 singleton_nonforcing=44`

The infinite statement is proved by the six local calculations, the outward-front induction, and the established two-seed eligibility criterion, not by the finite experiment alone. To reproduce, run `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Barrera and Ferrero [1] treated the power domination number in cylinders, tori, and generalized Petersen graphs, establishing prism minimum-size benchmarks. Girish and Somasundaram [2, Lemmas 1–2] establish the exact eligible distance-three seed-pair criterion and explain the outward observation mechanism. These results are **credited** rather than claimed as new; the number \(11n\) of eligible pairs follows directly from their criterion. Bozeman [3] studies power propagation times in general and supplies the conventional round-counting viewpoint, including exact formulas for paths and ordinary cycles. The present theorem instead distinguishes and counts the **synchronous completion times of every minimum pair** for all cycle prisms; those time-resolved and parity-dependent multiplicities are not stated in the inspected prior results. The frontier proof provides the additional timing analysis.

## Limitations
The assertion is restricted to \(n\ge7\), two-vertex *minimum* power-dominating sets, and the simultaneous forcing convention. It does not count larger monitoring sets, asynchronous forcing schedules, or weighted sensor placements. Earlier equivalent time-resolved enumerations under propagation-radius or bounded-time power-domination terminology remain a priority risk. The cited 2016 thesis chapter and the 2024 prism article were materially inspected, but exhaustive literature completeness and independent mathematical validation are not claimed.

## References
[1] R. Barrera and D. Ferrero, *Power domination in cylinders, tori, and generalized Petersen graphs*, Networks **58** (2011), 43–49. DOI: 10.1002/net.20413. Author-open PDF: https://cpb-us-e1.wpmucdn.com/wp.txstate.edu/dist/1/556/files/2015/03/BarreraFerrero.pdf.

[2] L. Girish and K. Somasundaram, *Bound for the k-Fault-Tolerant Power-Domination Number*, Symmetry **16** (2024), 781, Lemmas 1–2. DOI: 10.3390/sym16070781. Open full text: https://www.researchgate.net/publication/381630437_Bound_for_the_k-Fault-Tolerant_Power-Domination_Number.

[3] C. Bozeman, *On the power propagation time of a graph*, arXiv:1608.01189v1 (2016-08-03), including the corresponding chapter of the author's thesis (Chapter 3, §3.2). Open thesis: https://www.aimath.org/~hogben/Bozeman-thesis.pdf.
