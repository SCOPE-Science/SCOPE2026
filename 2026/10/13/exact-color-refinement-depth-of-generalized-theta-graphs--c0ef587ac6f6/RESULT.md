# Exact color-refinement depth of generalized theta graphs

## Finding
Let \(d\ge3\), and let
\[
\Theta(\ell_1,\ldots,\ell_d),\qquad \ell_i\ge2,
\]
be the simple generalized theta graph obtained from two branch vertices \(u,v\) by joining them with \(d\) internally vertex-disjoint paths whose edge lengths are \(\ell_1,\ldots,\ell_d\). Equivalently, this is a subdivision of \(K_{2,d}\). Start ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round \(s\) for which rounds \(s\) and \(s+1\) induce the same vertex partition.

Put
\[
L=\max_i\ell_i
\]
and let \(S\) be the second-largest *distinct* value among the \(\ell_i\), with \(S=0\) when all path lengths are equal. Then
\[
\boxed{\operatorname{Stab}\bigl(\Theta(\ell_1,\ldots,\ell_d)\bigr)
      =\max\left\{\left\lfloor\frac L2\right\rfloor,S\right\}.}
\]

There is a stronger exact round description. If \(x\) is an internal vertex on a path of length \(\ell\), at distance \(i\) from one branch vertex and \(\ell-i\) from the other, define
\[
P_r(x)=\left\{\min(i,r),\,\min(\ell-i,r)\right\},
\]
as an unordered pair. For every \(r\ge1\), the two branch vertices form one color class, and two internal vertices have the same round-\(r\) color if and only if their clipped pairs \(P_r\) are equal.

For fixed \(d\) and order \(n\), this also gives the exact extremum over the whole family:
\[
\boxed{\max_{\substack{|V(\Theta)|=n\\\Theta\text{ has }d\text{ paths}}}
       \operatorname{Stab}(\Theta)
       =\left\lfloor\frac{n-d+1}{2}\right\rfloor}
       \qquad(n\ge d+2).
\]

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. Round \(0\) is the uniform coloring. At each later round, a vertex is recolored by its previous color together with the multiset of previous colors of its neighbors.

The restriction \(\ell_i\ge2\) makes \(\Theta(\ell_1,\ldots,\ell_d)\) precisely a simple subdivision of \(K_{2,d}\). The two branch vertices have degree \(d\), and all internal vertices have degree \(2\). The order is
\[
n=2+\sum_{i=1}^d(\ell_i-1)=\sum_{i=1}^d\ell_i-d+2.
\]

## Proof
The automorphism reversing every \(u\)-\(v\) path exchanges \(u\) and \(v\), so the two branch vertices have the same color in every round. Since \(d\ge3\), their degree-\(d\) color is already different in round \(1\) from the common degree-\(2\) color of all internal vertices.

We first prove the clipped-pair description by induction on \(r\). For \(r=1\), every internal vertex has
\[
P_1=\{1,1\},
\]
and all internal vertices have the same degree-\(2\) color, so the claim holds.

Assume the statement holds at round \(r\). Consider an internal vertex \(x\) whose two distances to the branch vertices along its path are \(a\) and \(b\). Its round-\((r+1)\) color consists of its round-\(r\) color and the multiset of the round-\(r\) colors of its two neighbors. By the induction hypothesis, all internal neighbor colors are encoded injectively by their clipped pairs, while a branch neighbor has the common branch color, which is distinct from every internal color.

The unordered pair
\[
\{\min(a,r+1),\min(b,r+1)\}
\]
determines the old clipped pair at level \(r\) and the multiset of the two neighbor clipped pairs (with a branch marker when a coordinate is \(1\)). Conversely, if two level-\((r+1)\) clipped pairs differ, then either their level-\(r\) clipped pairs already differ, or one of the coordinates that was clipped at \(r\) is exposed at the next step; in the latter case the corresponding neighbor has a different level-\(r\) clipped pair. Thus equality of round-\((r+1)\) colors is exactly equality of \(P_{r+1}\). This completes the induction.

It remains to determine when this clipped-pair partition stops changing. For a single path of length \(\ell\), if
\[
r<\left\lfloor\frac{\ell}{2}\right\rfloor,
\]
then two non-reflection-equivalent internal positions still have the same clipped pair at round \(r\) but are separated later. Hence stabilization requires
\[
r\ge\left\lfloor\frac L2\right\rfloor.
\]
Once \(r\ge\lfloor\ell/2\rfloor\), the clipped pair distinguishes every position on that path up to reversal.

There is a second obstruction coming from distinct path lengths. Let \(a<b\). For every \(r<a\), the first internal vertices on the two paths have the same clipped pair
\[
\{1,r\},
\]
but at round \(a\) the shorter path gives \(\{1,a-1\}\), while the longer one gives \(\{1,a\}\). Therefore the coloring cannot be stable before round \(a\). Taking \(a\) over all nonmaximal distinct path lengths gives the lower bound \(r\ge S\).

Conversely, suppose
\[
r\ge \max\left\{\left\lfloor\frac L2\right\rfloor,S\right\}.
\]
Within any one path, the clipped pair already determines the exact unordered distance pair \(\{i,\ell-i\}\), hence the position up to path reversal. For two paths of different lengths \(a<b\), the shorter length satisfies \(a\le S\le r\). Every clipped pair on the shorter path has both coordinates strictly below \(r\), so its coordinate sum is exactly \(a\). It cannot equal a clipped pair from the longer path: if the latter is unclipped its sum is \(b\ne a\), and if it is clipped it contains the coordinate \(r\). Thus no further color class can split. This proves
\[
\operatorname{Stab}(\Theta)=
\max\left\{\left\lfloor\frac L2\right\rfloor,S\right\}.
\]

For the fixed-order extremum, write
\[
\sum_i\ell_i=n+d-2.
\]
Since the other \(d-1\) path lengths are at least \(2\),
\[
L\le n-d,
\]
and therefore
\[
\left\lfloor\frac L2\right\rfloor
\le \left\lfloor\frac{n-d}{2}\right\rfloor.
\]
If there are at least two distinct lengths and \(S=s\), then some length is at least \(s+1\), while the remaining \(d-2\) lengths are at least \(2\). Hence
\[
n+d-2=\sum_i\ell_i
\ge s+(s+1)+2(d-2),
\]
so
\[
S\le\left\lfloor\frac{n-d+1}{2}\right\rfloor.
\]
If all lengths are equal, \(S=0\), so the same upper bound is immediate.

The bound is attained. For \(n=d+2\), take all path lengths equal to \(2\). For \(n\ge d+3\), set \(d-2\) path lengths equal to \(2\), put
\[
R=n-d+2,
\qquad
a=\left\lfloor\frac{R-1}{2}\right\rfloor,
\qquad
b=R-a,
\]
and use the remaining two lengths \(a,b\). Then \(a\ge2\), the order is \(n\), and the second-largest distinct length is \(a\); the depth formula gives
\[
\operatorname{Stab}=\left\lfloor\frac{n-d+1}{2}\right\rfloor.
\]
This proves the extremal formula.

## Verification
The accompanying `verify.py` implements color refinement directly, without external packages. It exhaustively checks every nondecreasing length tuple with
\[
3\le d\le7,\qquad 2\le\ell_i\le10.
\]
For each graph it verifies both the closed-form depth and the complete clipped-pair partition at every round through stabilization. This covers \(11{,}385\) generalized theta graphs and \(77{,}660\) round-level partition comparisons.

It also groups the exhaustive data by \((d,n)\) and verifies the fixed-order extremal formula for every \(3\le d\le7\) and \(d+2\le n\le d+10\), where the length cutoff \(10\) is automatically exhaustive. The checker returns:

`VERIFY_OK depth_checks=11385 partition_checks=77660 order_checks=45 d=3..7 lengths=2..10`

The computation is corroborative; the proof above establishes both formulas for all allowed parameters.

## Relationship to prior work
Krebs and Verbitsky established the precise relationship between color-refinement rounds and truncated universal covers and used it to prove near-linear lower bounds on stabilization depth for general graphs. That framework supplies the standard local-information interpretation behind the clipped-distance argument here, but the inspected paper does not give a generalized-theta formula.

Kiefer and McKay later proved that the trivial \(n-1\) upper bound on the iteration number is tight for unrestricted graphs. More recent work of Kiefer and de Mel classifies low-degree graphs attaining the longest possible refinement behavior. These results concern unrestricted extremal behavior rather than the exact iteration law for subdivisions of \(K_{2,d}\).

Targeted searches using the terms “theta graph”, “generalized theta graph”, “subdivision of \(K_{2,d}\)”, “color refinement”, “1-WL”, “Weisfeiler--Leman”, and “iteration number” did not locate the clipped-pair law or the formula above. The closest surfaced theta-graph results concerned unrelated invariants such as square coloring and configuration-space homology.

## Limitations
The theorem is restricted to generalized theta graphs in which every \(u\)-\(v\) path has length at least \(2\). It concerns ordinary one-dimensional color refinement from the uniform coloring, not higher-dimensional Weisfeiler--Leman refinement, arbitrary initial colors, graph-pair distinguishing depth, or logical defining depth.

The literature search was targeted rather than exhaustive. An unindexed family-specific computation could therefore remain undiscovered, although no equivalent statement was found in the inspected sources or semantic-search results.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015, DOI: 10.1109/LICS.2015.69.
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73.
3. S. Kiefer and T. D. de Mel, *A Classification of Long-Refinement Graphs for Colour Refinement*, arXiv:2510.20802, first posted 23 October 2025.
