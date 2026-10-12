# Sharp four-candidate, three-voter boundary for Kemeny–maximin divergence
## Finding
Let \(P\) be a profile of complete strict rankings.

For distinct candidates \(x,y\), let
\[
n_P(x,y)
\]
be the number of voters who rank \(x\) above \(y\).

A linear order \(\pi\) receives Kemeny agreement score
\[
S_P(\pi)=\sum_{x\succ_\pi y} n_P(x,y).
\]
The **Kemeny winner set** \(K(P)\) consists of the candidates appearing first in at least one linear order maximizing \(S_P\).

The **maximin score** of candidate \(x\) is
\[
m_P(x)=\min_{y\ne x} n_P(x,y),
\]
and the **maximin winner set** is
\[
M(P)=\operatorname*{arg\,max}_x m_P(x).
\]

Published three-candidate results imply
\[
K(P)=M(P)
\]
for every profile on three candidates.

The first possible disagreement is exactly four candidates and three voters.

For four candidates, the two correspondences agree on all
\[
24
\]
one-voter profiles and all
\[
24^2=576
\]
two-voter profiles.

With three voters, among all
\[
24^3=13824
\]
labeled profiles, exactly
\[
1056
\]
have different winner sets. Hence the exact impartial-culture incidence is
\[
\frac{1056}{13824}=\frac{11}{144}.
\]

Every first-layer disagreement has the same direction:
\[
K(P)\subsetneq M(P).
\]

The full three-voter winner-set-size census is
\[
\begin{array}{c|r}
(|K(P)|,|M(P)|,\text{relation}) & \text{profiles}\\ \hline
(1,1,\text{equal}) & 12288\\
(3,3,\text{equal}) & 480\\
(1,3,\text{strict containment}) & 144\\
(1,4,\text{strict containment}) & 576\\
(3,4,\text{strict containment}) & 336.
\end{array}
\]

Thus maximin never refines Kemeny on this first layer, and there is no nonnested overlap or disjointness.

Up to simultaneous relabeling of the four candidates and the three voters, the \(1056\) divergent profiles form exactly eight isomorphism classes. Seven have full orbit size
\[
4!\,3!=144,
\]
while one has orbit size
\[
48,
\]
equivalently stabilizer order \(3\).

Using candidates \(A,B,C,D\), canonical representatives are:

| ballots | \(K(P)\) | \(M(P)\) | orbit |
|---|---|---|---:|
| `ABCD`, `BCAD`, `DCAB` | \(\{A,B,C\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BCDA`, `CDAB` | \(\{B\}\) | \(\{A,B,C\}\) | \(144\) |
| `ABCD`, `BCDA`, `DACB` | \(\{A\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BCDA`, `DCAB` | \(\{B\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BDAC`, `CDAB` | \(\{A\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BDAC`, `DCAB` | \(\{A,B,D\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BDCA`, `CDAB` | \(\{B\}\) | \(\{A,B,C,D\}\) | \(144\) |
| `ABCD`, `BDCA`, `DACB` | \(\{A,B,D\}\) | \(\{A,B,C,D\}\) | \(48\) |

Consequently, four candidates are the smallest candidate set on which the two correspondences can differ, and three voters are the smallest electorate size realizing that difference with four candidates.

## Assumptions and scope
Ballots are complete strict rankings. Kemeny is treated as a choice correspondence: every candidate topping at least one maximum-agreement ranking is selected. Maximin uses raw pairwise support; with a fixed electorate size this is equivalent to minimizing the largest opposing support.

The lower candidate bound is a published theorem: for exactly three candidates, Kemeny and maximin are identical correspondences for every profile.

The voter lower bound at four candidates is established by complete enumeration of every one-voter and two-voter profile.

The result does not concern margin-only variants that change tie conventions, truncated ballots, weak orders, or electorates with more than three voters.

## Proof
For four candidates, there are
\[
4!=24
\]
possible strict ballots. The verifier exhausts all profiles with one, two, and three labeled voters.

For Kemeny, two exact implementations are compared.

The first enumerates all \(24\) candidate rankings and maximizes the pairwise agreement score \(S_P\).

The second minimizes total Kendall inversion distance from the candidate ranking to the voters' ballots. For every ranking \(\pi\),
\[
S_P(\pi)+D_P(\pi)=6|P|,
\]
because four candidates have exactly six unordered pairs. Thus the two objectives are complementary, and the two implementations agree profile by profile.

For maximin, the first implementation computes
\[
m_P(x)=\min_{y\ne x}n_P(x,y).
\]
The second computes the largest opposing support against \(x\),
\[
o_P(x)=\max_{y\ne x}n_P(y,x).
\]
Since
\[
n_P(x,y)+n_P(y,x)=|P|,
\]
one has
\[
m_P(x)+o_P(x)=|P|,
\]
so maximizing \(m_P\) is exactly minimizing \(o_P\). The two implementations again agree on every profile.

All \(24\) one-voter and \(576\) two-voter profiles have identical Kemeny and maximin winner sets.

For three voters the exact relation histogram is
\[
12768
\]
equal profiles and
\[
1056
\]
strict containments
\[
K(P)\subsetneq M(P).
\]
The three strict size cells sum to
\[
144+576+336=1056.
\]

To quotient by symmetry, the verifier applies every permutation of the four candidate labels and every permutation of the three voters. It maps each profile to a canonical representative and obtains exactly eight divergent orbits. Seven have \(144\) labeled profiles and one has \(48\), summing to
\[
7\cdot144+48=1056.
\]

The published three-candidate equivalence theorem supplies the candidate lower bound, while the complete one- and two-voter enumeration supplies the electorate lower bound.

## Verification
The embedded `verify_kemeny_maximin_first_layer.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- all \(24\) four-candidate one-voter profiles;
- all \(576\) four-candidate two-voter profiles;
- all \(13824\) four-candidate three-voter profiles;
- pairwise-score Kemeny against independent total-Kendall-distance Kemeny;
- support-form maximin against independent opposition-form maximin;
- the exact equality count \(12768\);
- the exact divergent count \(1056\);
- exact probability \(11/144\);
- strict containment \(K(P)\subsetneq M(P)\) for every divergence;
- exact strict size counts \(144,576,336\);
- exactly eight divergent isomorphism classes;
- seven orbit sizes \(144\) and one orbit size \(48\);
- all eight displayed canonical representatives and winner sets.

Run:

`python3 verify_kemeny_maximin_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Courtin, Mbih, and Moyouwou define their “Condorcet function” as the maximin rule and define Kemeny by maximum pairwise agreement. Their three-candidate analysis proves equality of the relevant score orderings and concludes that maximin and Kemeny always select the same winner in the three-candidate case.

Brandt, Dong, and Peters give a modern correspondence-level treatment: in their Hasse diagram of three-candidate Condorcet extensions, maximin and Kemeny occur at the same node, meaning the rules are identical for all three-candidate profiles. They explicitly cite the Courtin result for this equivalence.

Courtin, Mbih, and Moyouwou also note that these equivalences cease to hold once there are more than three alternatives. That qualitative statement does not determine the smallest electorate needed at four candidates, the exact incidence, the one-sided containment, or the symmetry quotient.

The contribution here is the complete first post-equivalence layer: two voters still never separate the rules at four candidates; three voters do so on exactly \(11/144\) of labeled profiles; every disagreement is a Kemeny refinement of maximin; and the whole divergent layer consists of eight symmetry classes.

Targeted searches using the canonical rule names, the four-candidate/three-voter parameter pair, the exact count \(1056\), the fraction \(11/144\), and isomorphism language did not locate an equivalent published census.

## Limitations
The theorem classifies only the sharp first layer. It gives no frequency formula for larger electorates or candidate sets.

The oldest inspected working paper is dated September 2012, but its exact release day was not established. The metadata uses \(2012\)-\(10\)-\(06\), the earliest day-resolved public indexing record verified for that working paper, rather than inventing a September day.

The originality search cannot rule out an unindexed teaching computation, software test corpus, thesis appendix, or unpublished enumeration containing the same finite census.

## References
1. S. Courtin, B. Mbih, and I. Moyouwou, “Are Condorcet procedures so bad according to the reinforcement axiom?”, THEMA Working Paper 2012-37, September 2012; later *Social Choice and Welfare* 42 (2014), 927–940. DOI: 10.1007/s00355-013-0758-7.
2. F. Brandt, C. Dong, and D. Peters, “Condorcet-Consistent Choice Among Three Candidates,” arXiv:2411.19857, first submitted 29 November 2024; later *Games and Economic Behavior* 153 (2025), 113–130.
3. J. G. Kemeny, “Mathematics without numbers,” *Daedalus* 88 (1959), 577–591.
