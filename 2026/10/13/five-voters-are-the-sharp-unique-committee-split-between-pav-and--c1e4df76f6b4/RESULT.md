# Five voters are the sharp unique-committee split between PAV and approval Chamberlin–Courant
## Finding
Consider approval-based committee elections with exactly three candidates
\[
C=\{A,B,C\}
\]
and target committee size
\[
k=2.
\]
Each voter may submit any approval set \(A_i\subseteq C\), including the empty set or all three candidates.

Under Proportional Approval Voting (PAV), a voter who approves \(j\) members of a committee contributes
\[
r(j)=\sum_{t=1}^{j}\frac1t,
\]
so for \(k=2\) the possible contributions are \(0,1,3/2\). Under approval Chamberlin–Courant (CC), a voter contributes \(1\) exactly when the committee contains at least one approved candidate.

If both rules have unique winning committees and those committees are different, then the election has at least \(5\) voters.

The lower bound is sharp. Up to candidate relabeling, the unique anonymous five-voter conflict profile is
\[
3\times\{A,B\},\qquad 1\times\{A\},\qquad 1\times\{C\}.
\]
For the three committees \(\{A,B\},\{A,C\},\{B,C\}\), respectively, the PAV scores are
\[
\frac{11}{2},\quad 5,\quad 4,
\]
so PAV uniquely selects \(\{A,B\}\). The CC coverage scores are
\[
4,\quad 5,\quad 4,
\]
so CC uniquely selects \(\{A,C\}\).

There are exactly \(6\) anonymous labeled-candidate profiles at this boundary, all in one candidate-relabeling orbit. Each has ballot multiplicities \(3,1,1\), and therefore has
\[
\frac{5!}{3!}=20
\]
labeled-voter realizations. Hence exactly
\[
6\cdot20=120
\]
of the
\[
8^5=32768
\]
labeled five-voter approval profiles have different unique PAV and CC winning committees. The unconditional incidence is
\[
\frac{120}{32768}=\frac{15}{4096}.
\]

Exactly \(11970\) labeled five-voter profiles have a unique winner under each rule. Conditional on that resolute domain, the disagreement incidence is therefore
\[
\frac{120}{11970}=\frac4{399}.
\]

At the anonymous level there are \(\binom{12}{7}=792\) five-voter profiles over the eight ballot types, so the boundary incidence there is
\[
\frac6{792}=\frac1{132}.
\]

## Assumptions and scope
The result concerns the exact optimizing versions of PAV and approval CC, with all tied maximizing committees retained when discussing winner correspondences. The sharp boundary statement is specifically about profiles for which both rules have a unique winning committee.

Approval ballots are unrestricted subsets of the three-candidate set. Empty ballots and ballots approving all three candidates are included in the finite domain.

The theorem fixes three candidates and committee size two, and varies the number of voters. It does not claim that five voters is a universal boundary when the number of candidates or the committee size changes.

Winner correspondences can differ through ties with fewer than five voters. The theorem isolates the first point where the two rules make different unambiguous committee choices.

## Proof
Write
\[
a,b,c
\]
for the numbers of singleton ballots \(\{A\},\{B\},\{C\}\), and write
\[
x,y,z
\]
for the numbers of doubleton ballots \(\{A,B\},\{A,C\},\{B,C\}\). Empty ballots and full ballots contribute equally to all three committees under each rule, so they can be ignored in score differences.

Any two distinct size-two committees on three candidates share one candidate. Therefore, after relabeling candidates, every putative unique conflict can be normalized so that PAV uniquely selects \(\{A,B\}\) while CC uniquely selects \(\{A,C\}\).

For CC, a size-two committee fails to cover only empty ballots and singleton ballots for the omitted candidate. Thus, apart from the common empty-ballot term, the three coverage scores are
\[
n-c,\qquad n-b,\qquad n-a.
\]
For \(\{A,C\}\) to be the unique CC winner we must have
\[
b<a\quad\text{and}\quad b<c.
\]
Hence
\[
a\ge b+1,\qquad c\ge b+1.
\]

The PAV scores, after dropping the common full-ballot contribution, are
\[
\begin{aligned}
P_{AB}&=a+b+\frac32x+y+z,\\
P_{AC}&=a+c+x+\frac32y+z,\\
P_{BC}&=b+c+x+y+\frac32z.
\end{aligned}
\]
The strict inequality \(P_{AB}>P_{AC}\) gives
\[
b-c+\frac{x-y}{2}>0,
\]
so
\[
x-y>2(c-b).
\]
Because \(c-b\ge1\) and the counts are integers,
\[
x-y\ge3,
\]
and therefore \(x\ge3\).

Consequently the total number of voters satisfies
\[
n\ge a+c+x\ge(b+1)+(b+1)+3=2b+5\ge5.
\]
This proves the lower bound without enumeration.

If \(n=5\), every inequality above must be tight. Therefore
\[
b=0,
\qquad
a=c=1,
\qquad x=3,
\]
and all remaining ballot counts, including \(y,z\), the empty-ballot count, and the full-ballot count, are zero. This is exactly the displayed canonical profile. Direct substitution gives the stated PAV and CC scores, so it is indeed a conflict.

The profile has no nontrivial candidate relabeling stabilizer, hence its candidate orbit has size \(3!=6\). Its ballot multiplicities are \(3,1,1\), giving \(20\) voter-labelings per candidate-labeled anonymous profile and therefore \(120\) labeled profiles.

The remaining count \(11970\) of five-voter profiles on which both rules are unique is obtained by exhaustive exact enumeration in the verifier.

## Verification
The embedded `verify_pav_cc_unique_boundary.py` gives two independent finite replays.

First, it directly enumerates every labeled profile in \(\{0,1\}^{3n}\) for \(1\le n\le5\), computes each committee score ballot by ballot using exact rational arithmetic, and records both complete winner correspondences.

Second, it independently enumerates anonymous ballot-count vectors over the eight approval types, computes PAV in integer half-units and CC by aggregate coverage, and weights every anonymous profile by its exact multinomial number of voter-labelings.

The two methods agree on all labeled counts. They verify that the numbers of profiles with different unique committees for \(n=1,2,3,4,5\) are
\[
0,0,0,0,120.
\]
They also verify the five-voter counts \(6\) anonymous conflicts, \(120\) labeled conflicts, \(11970\) profiles with both committees unique, and a single candidate-relabeling orbit of the canonical \(3,1,1\) profile.

Run:

`python3 verify_pav_cc_unique_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Approval Chamberlin–Courant is a standard coverage objective: Skowron and Faliszewski formulate its approval variant as choosing a fixed-size committee that minimizes the number of voters approving no committee member, equivalently a maximum-coverage problem.

Aziz, Brill, Conitzer, Elkind, Freeman, and Walsh give the standard PAV definition, with harmonic marginal weights \((1,1/2,1/3,\ldots)\). The same paper observes that approval CC is the weighted-PAV endpoint with weight vector \((1,0,0,\ldots)\). Thus the present comparison is between two established members of the same approval-committee scoring framework.

Later work quantitatively studies tradeoffs among approval-based multiwinner objectives and uses CC as a representation or diversity benchmark. A recent paper also gives a three-candidate, two-seat CC example, showing that this very small committee geometry is used explicitly in the literature. None of the inspected sources states the exact first electorate size at which PAV and approval CC have different unique committees, the canonical \(3,1,1\) obstruction, or the \(120\)-profile census.

Targeted searches used the PAV and Chamberlin–Courant names, the weighted-Thiele formulations \((1,1/2)\) versus \((1,0)\), the exact five-voter and three-candidate restrictions, the canonical ballot pattern, and the exact counts \(120\) and \(15/4096\).

## Limitations
The boundary is for exactly three candidates and committee size two.

The finite-domain incidences count empty and full approval ballots because the domain is all eight approval subsets per voter. The canonical conflict itself uses neither type.

The theorem concerns unique winners. Set-valued PAV and CC correspondences can differ at smaller electorates through ties.

The exact five-voter conditional denominator \(11970\) is computationally enumerated; the sharp lower bound and canonical boundary classification have the independent analytic proof above.

An unindexed exercise, small-profile table, software example library, or historical note could contain the same minimal profile even though the targeted searches did not locate it.

## References
1. P. Skowron and P. Faliszewski, “Approximating the MaxCover Problem with Bounded Frequencies in FPT Time,” arXiv:1309.4405, first public version 17 September 2013.
2. H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, and T. Walsh, “Justified Representation in Approval-Based Committee Voting,” arXiv:1407.8269, first public version 31 July 2014.
3. M. Lackner and P. Skowron, “Utilitarian Welfare and Representation Guarantees of Approval-Based Multiwinner Rules,” arXiv:1801.01527, first public version 4 January 2018.
4. Z. Fitzsimmons, Z. R. Hassan, and E. Hemaspaandra, “On the Parallelizability of Approval-Based Committee Rules,” DOI 10.3233/FAIA251005, 2026.
