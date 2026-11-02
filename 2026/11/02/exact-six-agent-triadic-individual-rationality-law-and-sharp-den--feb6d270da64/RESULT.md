# Exact six-agent triadic individual-rationality law and sharp dense obstruction boundary

## Finding

In the first balanced market with two three-person coalitions, feasibility and multiplicity can be determined exactly under independently random signed pair preferences. For each integer \(z\in\{0,\ldots,10\}\), let \(a_{j,z}\) count labeled undirected friendship graphs on six vertices that have exactly \(j\) friendly edges and exactly \(z\) individually rational (IR) partitions into two unordered triples. The complete \(16\)-by-\(11\) table is in `artifacts/multiplicity_coefficients.csv`. For \(0\le p\le1\), independent friendship edges with common probability \(p\) give

\[
\Pr_p(Z=z)=\sum_{j=0}^{15}a_{j,z}p^j(1-p)^{15-j}.
\]

At \(p=1/2\), the count vector for \(z=0,1,\ldots,10\) is

\[
(7020,6520,5400,4860,2460,2592,1740,1260,360,480,76).
\]

Thus the exact feasibility probability is \(\Pr_{1/2}(Z>0)=6437/8192\). The separate coefficient vector for the feasibility event \(Z>0\), indexed by friendly-edge count \(j=0,\ldots,15\), is

\[
(0,0,0,0,90,870,3130,5610,6165,4945,2997,1365,455,105,15,1).
\]

There is also a sharp dense structural boundary: whenever a six-agent friendship graph has at least eight edges, it admits an IR two-triple partition **if and only if** its minimum degree is positive. At seven friendly edges, the IR-infeasible graphs with positive minimum degree comprise exactly two isomorphism types: \(K_4\sqcup K_2\), with 15 labeled realizations, and the graph with one universal vertex whose five leaves span two independent edges, with 90 labeled realizations. Both have seven friendship edges, so the threshold cannot be decreased.

As analytical checks on the full multiplicity law,

\[
\mathbb E_p[Z]=10(3p^2-2p^3)^2,
\]

and

\[
\Pr_p(Z=10)=p^{15}+15(1-p)p^{14}+45(1-p)^2p^{13}+15(1-p)^3p^{12}.
\]

## Assumptions and scope

There are six labeled agents \(N=\{0,1,2,3,4,5\}\). Every unordered pair is symmetric and either friendly (value \(+1\) to each other) or hostile (value \(-1\) to each other). For any coalition \(T\) containing agent \(i\), utility is the sum of that agent's pair values to the other members of \(T\); a singleton has utility zero. A partition is IR if each agent's utility is nonnegative. Exactly two **unlabeled**, disjoint, size-three coalitions must cover all agents. Friendship edges are drawn independently with probability \(p\), without assumptions about strategic stability stronger than individual rationality. The deterministic statement concerns arbitrary signed instances, not random graphs only.

## Proof

**Triple characterization.** For any triple \(T\), each agent compares the signs of its two incident pairs. Its utility is nonnegative exactly when at least one pair is friendly. Thus all three agents are IR exactly when the friendship graph induced on \(T\) has at least two edges, equivalently is connected (a path or triangle). Consequently an IR allocation exists precisely when the friendship graph admits a spanning partition into two connected triples. Existence is equivalent to the existence of a \(P_3\)-factor, although the number \(Z\) counts *vertex partitions*, not distinct spanning path subgraphs.

**Exact finite counting proof.** There are \(\binom62=15\) possible undirected friendship edges, giving exactly \(2^{15}=32768\) signed profiles. Every unordered partition into two triples has a unique block containing vertex \(0\); choose its other two members from the remaining five. Hence there are exactly \(\binom52=10\) possible partitions. Fix the 15 edge coordinates in lexicographic pair order and enumerate every integer mask from zero through \(32767\). For each partition, test whether each of its two triples has at least two friendly edges. Record \(a_{j,z}\), where \(j\) is the mask popcount and \(z\) the number of successful partitions. This exhausts every labeled profile exactly once; each \(a_{j,z}\) is therefore an exact integer, not an estimate. The complete finite proof is executable as `artifacts/verify.py` and its coefficients are recorded separately. The checker performs a second, reachability-based connectivity test of every triple independently of the edge-count criterion.

**Dense boundary, necessity.** An isolated agent has no friends and cannot receive nonnegative utility from either of its possible three-person coalitions, so isolation prevents IR.

**Dense boundary, sufficiency.** Suppose a six-vertex graph has at least eight edges and no isolates. If a vertex \(v\) has degree five, then among its five other vertices there are at least three edges, which contain a connected triple. Its complement is a triple containing the universal vertex and is connected. If \(v\) has degree four, let \(y\) be its unique nonneighbor and \(A\) its four neighbors. Since \(y\) is not isolated, it has at least one neighbor in \(A\). If it has at least two, these two with \(y\) form a connected triple, and the remaining two of \(A\) with \(v\) form another. Otherwise let \(a\) be the unique neighbor of \(y\). If \(a\) is adjacent to another member of \(A\), use the connected triple consisting of \(y,a\), and that member. If not, an eight-edge graph forces at least two edges among the remaining three members of \(A\): four edges touch \(v\), one touches \(y\), and none joins \(a\) to the other members of \(A\). Those remaining three form a connected triple, and the complement \(\{v,a,y\}\) is a connected path. Thus maximum degree at least four is handled.

It remains to consider maximum degree at most three. Eight edges force degree sequence either \((1,3,3,3,3,3)\) or \((2,2,3,3,3,3)\); nine edges force a cubic graph. A cubic graph on six vertices is Hamiltonian by Dirac's theorem. In the first eight-edge case, let \(x\) be the leaf and \(a\) its neighbor. The five-vertex graph after removing \(x\) is \(K_5\) minus a three-edge graph comprising a two-edge path centered at \(a\) and a disjoint edge. Writing those three missing edges as \(au,av,wt\), the original graph has the spanning path \(x,a,w,u,t,v\). In the second eight-edge case, let \(a,b\) be the degree-two vertices. If they are not adjacent, adding their missing edge yields a cubic six-vertex graph and hence a Hamiltonian cycle; deleting that added edge, if the cycle uses it, leaves a spanning path in the original graph. If \(a,b\) are adjacent, the four degree-three vertices induce \(K_4\) minus one edge. Such a graph has a Hamiltonian path beginning at any prescribed vertex, so prepend \(b,a\) and continue from \(a\)'s other neighbor through those four vertices. Every spanning six-vertex path splits into two disjoint connected triples. Hence all eight-or-more-edge, isolate-free cases admit IR.

**Sharpness and obstruction classification.** The graphs \(K_4\sqcup K_2\) and a universal vertex with a matching of size two among its five leaves both have exactly seven friendship edges and no isolates, but neither admits a partition into two connected triples. Exhaustive classification of all seven-edge signed profiles with positive minimum degree finds precisely their two disjoint permutation orbits, of sizes \(15\) and \(90\), respectively. The included verifier constructs both orbits directly and checks equality against the complete seven-edge obstruction set.

**Two analytic multiplicity checks.** For each fixed partition, a three-vertex friendship graph is connected with probability \(3p^2-2p^3\), independently for its two blocks. Summing ten indicator variables gives \(\mathbb E_p[Z]=10(3p^2-2p^3)^2\). All ten partitions are IR precisely when the hostility graph has maximum degree at most one: a hostile wedge can be put into some triple, making that triple non-IR, whereas if no hostile wedge exists, every triple is IR. Thus hostile edges form a matching. Counting matchings of sizes zero through three on six labeled vertices gives multiplicities \(1,15,45,15\), proving the stated formula for \(\Pr_p(Z=10)\).

## Verification

Execute `python3 artifacts/verify.py` using only the Python standard library. It exhausts all 32,768 labeled graphs and all ten partitions, compares the edge-count test against a separately implemented connectivity test, checks the 16 edge-count totals against \(\binom{15}{j}\), checks every coefficient in the CSV, verifies the 11 multiplicity totals, tests the eight-edge threshold and the two seven-edge obstruction orbits, and checks the exact all-ten-partitions matching counts. An additional graph-atlas analysis over 156 unlabeled six-vertex graphs, weighted by automorphism orbit sizes, independently reproduced the same 16 edge-layer feasibility coefficients. The general dense-boundary proof above does not depend on finite experiments; the complete finite distribution does depend on transparent exhaustive enumeration.

## Relationship to prior work

Fioravantes, Gahlawat, Melissinos, and Schierreich (arXiv:2603.21826v1, public March 23, 2026) study existence complexity for constrained individually rational additively separable and fractional hedonic games. Their full accessible manuscript establishes hardness and algorithmic classifications, rather than the exact six-agent probability and multiplicity law stated here. Schierreich and Schlotter (arXiv:2608.14461v1, public August 14, 2026) study constrained individual rationality for friend-, enemy-, and neutral-oriented preferences, including balanced size-three coalitions and complexity hardness. With only friends and enemies, their friend-oriented IR condition for triples coincides with the one here; this is a relevant overlapping model, but the accessible abstract and detailed synopsis do not establish this exact finite distribution. Kaneko, Kelmans, and Nishimura (2001) study three-vertex path packings and factors, so the graph interpretation of feasibility is classical. The new claim is the exact six-agent distribution and sharp dense six-vertex obstruction layer, **not** the graph-factor equivalence, general computational decidability, or complexity hardness.

## Limitations

The probability law assumes independently sampled, identically distributed, symmetric friendship edges with values exactly \(\pm1\), and the population is exactly six; it does not give a closed formula for larger populations or other dependency distributions. The dense edge threshold concerns six agents only. Individual rationality is weaker than Nash, individual, or core stability. A finite exhaustive computation proves a finite integer table when the enumeration covers all inputs, but does not imply an analogous infinite-population theorem. The complete text of arXiv:2608.14461 and the 2001 path-packing article could not be inspected; an equivalent or stronger exact small-order statement in inaccessible or unindexed work remains a priority risk. No independent expert audit has been performed.

## References

1. F. Fioravantes, H. Gahlawat, N. Melissinos, and Š. Schierreich, *Individual Rationality in Constrained Hedonic Games: Additively Separable and Fractional Preferences*, arXiv:2603.21826v1 (public March 23, 2026), https://arxiv.org/abs/2603.21826.
2. Š. Schierreich and I. Schlotter, *Individual Rationality in Constrained Hedonic Games: Friends, Enemies, and Neutrals*, arXiv:2608.14461v1 (public August 14, 2026), https://arxiv.org/abs/2608.14461.
3. A. Kaneko, A. Kelmans, and T. Nishimura, *On Packing 3-Vertex Paths in a Graph*, Journal of Graph Theory 36 (2001), 175–197, DOI 10.1002/1097-0118(200104)36:4<175::AID-JGT1005>3.0.CO;2-T.
