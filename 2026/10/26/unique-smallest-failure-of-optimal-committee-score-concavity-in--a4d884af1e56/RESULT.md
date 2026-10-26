# Unique smallest failure of optimal committee-score concavity in approval coverage

## Finding

For an unweighted approval election with \(n\) voters and \(m\) candidates, let \(S_c\subseteq[n]\) be the voters approving candidate \(c\), and let
\[
M(k)=\max_{W\subseteq[m],\,|W|=k}\left|\bigcup_{c\in W}S_c\right|,\qquad 0\le k\le m.
\]
This is the approval Chamberlin–Courant (maximum-coverage) optimal score. Discrete concavity means \(2M(k)\ge M(k-1)+M(k+1)\) for every interior cardinality.

**Sharp boundary and classification.** Every such profile has a concave \(M\) if \(n\le5\), regardless of the number of candidates, or if \(m\le3\), regardless of the number of voters. With \(n=6\) and \(m=4\), nonconcavity occurs **if and only if**, up to voter and candidate relabeling, the four candidate supporter sets are three disjoint pairs partitioning the six voters and a three-person transversal containing exactly one voter from each pair. Its exact score profile is
\[
(M(0),M(1),M(2),M(3),M(4))=(0,3,4,6,6).
\]
The unique isomorphism class contains exactly \(120\) different candidate-unlabeled families on six labeled voters and \(2880\) fully labeled election profiles. Every one is **voter-deletion critical for voter intervals**: deleting any single voter produces a voter ordering in which all four supporter sets are intervals.

## Assumptions and scope

All voters have unit weight. Approval ballots may be empty, and different candidates may have equal supporter sets or no supporters. Candidates themselves are distinct; committees contain exactly \(k\) candidates. A voter contributes one unit of score if at least one approved candidate is selected and contributes zero otherwise. The theorem characterizes the first possible failure simultaneously by the number of voters and by the number of candidates; it does not claim concavity for other Thiele scoring rules outside the voter-interval domain.

## Proof

Write \(d_j=M(j)-M(j-1)\). All these increments are nonnegative integers. Let \(s=M(1)\) and \(U=\left|\bigcup_{c=1}^m S_c\right|\). If \(M(j)<U\), then \(d_{j+1}\ge1\): from any optimal size-\(j\) committee, some remaining candidate reaches an uncovered voter, and adding it increases coverage. Consequently, once an increment is zero, all later increments are zero. Also \(d_1=s\) and \(d_2\le s\), since every pair covers at most \(2s\). No violation can occur at \(k=1\).

**At most three candidates.** The only nontrivial case is \(m=3\) and \(k=2\). Choose a candidate \(a\) with \(|S_a|=M(1)\), and call the others \(b,c\). Coverage is submodular, so
\[
|S_a\cup S_b|+|S_a\cup S_c|\ge |S_a|+|S_a\cup S_b\cup S_c|=M(1)+M(3).
\]
Each pair score is at most \(M(2)\), proving \(2M(2)\ge M(1)+M(3)\). This also handles repeated or empty supporter sets.

**At most five voters, any number of candidates.** Suppose a first concavity violation occurs at \(k\), so \(d_{k+1}\ge d_k+1\). The observation above implies all \(d_2,\ldots,d_k\ge1\), and \(d_{k+1}\ge2\). Thus
\[
n\ge M(k+1)\ge s+(k-1)+2=s+k+1.
\]
If \(k\ge3\) and \(n\le5\), then \(s\le1\). When \(s\le1\), every nonempty supporter set is a singleton, so \(M(j)=\min\{j,U\}\), which is concave. Hence \(k=2\) is the only possible violating cardinality. Then \(n\ge s+3\). For \(n\le5\), again \(s\le2\), and \(s=1\) is impossible. With \(s=2\), integer margins force \(M(2)=3\) and \(M(3)\ge5\). But if three sets each have size at most two and their union has at least five elements, some pair has union of at least four elements: their total sizes are at most six, so at most one element can be counted twice, and two of the sets are disjoint size-two sets (or the union-size-five case with a singleton has such a pair). This contradicts \(M(2)=3\). Therefore no such profile exists.

**Six voters and four candidates.** There can be no violation at \(k=1\). If one occurs at \(k=3\), the above bound gives \(s\le2\); \(s\le1\) is excluded. Thus \(s=2\), and the integer increments must be exactly \((2,1,1,2)\), giving \(M(3)=4\) and \(M(4)=6\). In the union of all four sets, removing any one of them leaves a union of at most four. Each set therefore has at least two private voters not belonging to the other three. Four sets cannot have at least eight mutually distinct private voters among six voters. Hence \(k=3\) is impossible.

At \(k=2\), a violation means \(d_3\ge d_2+1\) with \(d_2\ge1\). If \(s\ge4\), then \(M(3)\ge s+3\ge7\), impossible. If \(s=2\), then necessarily \(d_2=1\) and \(M(3)\ge5\), again impossible by the three-size-two-sets argument above. Thus \(s=3\). The six-voter bound forces \(d_2=1\), \(d_3=2\), hence \((M(1),M(2),M(3))=(3,4,6)\).

Choose an optimal triple covering all six voters. Deleting any one of its three candidates leaves a pair covering at most four voters, so each of the three sets has at least two private voters within the triple. Since there are only six voters, they are three disjoint two-element sets covering all six. The fourth candidate must cover three voters because \(M(1)=3\). Since its union with each pair has cardinality at most four, it must intersect every pair. It contains exactly one voter from each, so it is a transversal. Conversely, for three disjoint pairs and such a transversal, the four maximum coverage scores are \(3,4,6,6\) after \(M(0)=0\); the sole strict inequality is \(2M(2)=8<9=M(1)+M(3)\). This proves the complete classification.

There are \(6!/(2!^3 3!)=15\) partitions of six labeled voters into three unlabeled pairs and \(2^3=8\) transversals per partition, for \(120\) distinct families. The triple of size-three voters uniquely identifies the transversal candidate, so candidate labeling multiplies by \(4!=24\), giving \(2880\).

**Voter-deletion criticality.** Write the pairs as \(\{x_i,y_i\}\), \(i=1,2,3\), with transversal \(\{x_1,x_2,x_3\}\). The original profile is not voter-interval: if the three transversal voters occupy consecutive positions, the middle \(x_i\) has both adjacent positions occupied by other transversal voters, leaving no adjacent position for its private partner \(y_i\) while retaining that pair as a consecutive interval. If \(y_2\) is deleted, the voter ordering \((y_1,x_1,x_2,x_3,y_3)\) makes every surviving supporter set consecutive. If \(x_2\) is deleted, the ordering \((y_1,x_1,x_3,y_3,y_2)\) does so. Permuting the three pairs covers deletion of any of the six voters. The claim follows.

## Verification

The standalone `verify.py` exhaustively checks all multisets of four candidate supporter sets on each labeled universe with \(1\le n\le6\), including empty and repeated sets. It checks all three discrete-concavity inequalities; finds no violations for \(n\le5\); and finds exactly \(120\) violations at \(n=6\), every one matching the stated transversal form and score profile. It checks the canonical witness's lack of a voter-interval ordering and interval realizability after each of the six single-voter deletions. A successful run prints `PASS` for each assertion group. These finite checks are not used as a substitute for the all-\(m\) analytic argument.

## Relationship to prior work

Manurangsi and Sornat, arXiv:2604.05953v1 (7 April 2026), Section 3, Theorem 5 and Corollary 9, prove a general concavity theorem on voter-interval profiles for generalized Thiele rules. Their result covers the **positive** concavity guarantee on the interval domain; it does not imply this exact **negative boundary and uniqueness classification** beyond the domain. Approval Chamberlin–Courant is the unit-coverage member of the Thiele family. Classical maximum-coverage and concave-coverage optimization literature supplies the definition and algorithms, not an identified derivation of the precise six-voter/four-candidate classification. The one-isomorphism-type conclusion is based on the direct proof above and should not be interpreted as a claim that no earlier equivalent construction exists.

## Limitations

The statements are for **unweighted coverage** only, not arbitrary Thiele scoring sequences or weighted voters. The minimality theorem concerns cardinality nonconcavity and separate bounds on voter and candidate counts, not a classification of all failure configurations at larger sizes. Historical priority remains subject to broader inspection of set-system, submodular-optimization and consecutive-ones literature. Independent mathematical audit has not been performed.

## References

1. Pasin Manurangsi and Krzysztof Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences*, arXiv:2604.05953v1, 7 April 2026, Section 3, Theorem 5 and Corollary 9. https://arxiv.org/pdf/2604.05953
2. Siddharth Barman, Omar Fawzi and Paul Fermé, *Tight Approximation Guarantees for Concave Coverage Problems*, arXiv:2010.00970, 2020. https://arxiv.org/abs/2010.00970
