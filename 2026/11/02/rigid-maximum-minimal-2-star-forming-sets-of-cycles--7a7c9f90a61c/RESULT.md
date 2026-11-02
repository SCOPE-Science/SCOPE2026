# Rigid maximum minimal 2-star-forming sets of cycles

## Finding
For every integer \(n\ge3\),
\[
\mathrm{SF}_2(C_n)=\left\lfloor\frac{2n}{3}\right\rfloor.
\]
When \(3\mid n\), every inclusion-minimal 2-star-forming vertex set \(S\) of maximum size is, in characteristic-word notation with vertices indexed in cyclic order, a rotation of \((110)^{n/3}\) or, only when \(6\mid n\), a rotation of \((111100)^{n/6}\). Conversely, all these sets are optimal. The exact number of distinct labelled optimal sets is
\[
\begin{cases}3,&n\equiv3\pmod6,\\9,&n\equiv0\pmod6.\end{cases}
\]
The additional six configurations for multiples of six are not 2-independent: their induced subgraph contains a run of four vertices and therefore a three-vertex path. The numerical optimum alone does not distinguish these configurations from maximum dissociation sets.

## Assumptions and scope
Let \(C_n\) be the finite simple cycle with labelled vertices \(0,1,\ldots,n-1\), indexed modulo \(n\), and \(n\ge3\). A vertex set \(S\) is **2-star-forming** if, for every \(v\notin S\), the subgraph \(C_n[S\cup\{v\}]\) contains a copy (not necessarily an induced copy) of \(K_{1,2}\) that contains \(v\). It is **inclusion-minimal** if no proper subset has the same property. It suffices to test deletions of one vertex because star-forming is monotone under enlarging \(S\). The number \(\mathrm{SF}_2(C_n)\) is the largest size of an inclusion-minimal 2-star-forming set. A **2-independent** set induces maximum degree at most one. Characteristic words distinguish cyclically labelled vertex subsets; rotations are distinct unless the word is periodic.

## Proof
**Local test.** For a cyclic binary occupancy sequence \(x_i=\mathbf1_{\{i\in S\}}\), an omitted vertex \(i\) lies in an eligible three-vertex path precisely when
\[
(x_{i-2}x_{i-1})\lor(x_{i-1}x_{i+1})\lor(x_{i+1}x_{i+2})=1.
\]
The terms correspond to \(i\) being an endpoint on either side or the central vertex. When a selected vertex \(i\) is removed, only eligibility tests for formerly omitted vertices within cyclic distance at most two can change. Hence for \(n\ge9\), 2-star-forming plus minimality can be decided at \(i\) from the nine bits \(x_{i-4},\dots,x_{i+4}\): if \(x_i=0\) require the displayed local test; if \(x_i=1\), set this central bit to zero and require at least one of the five local tests centered at \(i-2,\dots,i+2\) to fail. The standalone verifier implements this predicate as `permitted(bits)`; all 512 possible windows are considered.

**Finite-state inequality, all orders.** Interpret the nine bits as an integer \(b\) in \(\{0,\ldots,511\}\), with \(x_{i-4}\) the least significant bit. For each permitted window introduce a directed arc from the eight-bit state \(u=b\bmod256\) to \(v=\lfloor b/2\rfloor\), weighted by \(w=3x_i-2\). Exactly 332 of the 512 candidate arcs are permitted. The explicit 256-entry integer height vector \(h\), indexed by state \(0\) through state \(255\), is the string `POTENTIAL` in the included `verify.py`, with every character a digit between zero and four. Exact exhaustive integer checking yields
\[
w(u,v)\le h(v)-h(u)\qquad\text{for each of the 332 arcs.}\]
The verifier constructs the arcs from the local predicate without a stored edge table, reconstructs the stated height vector literally, and checks every inequality by integer comparison. Thus for every cyclic admissible word of length \(n\ge9\), its successive overlapping eight-bit states form a closed directed walk, and summing the inequalities gives
\[
3|S|-2n\le0.
\]

**Equality rigidity.** Equality requires every traversed arc to be tight. Exactly 242 arcs satisfy equality of the potential inequality. The verifier exhaustively constructs the tight directed graph and computes strongly connected components (by an explicit Tarjan traversal). All of its directed cycles are confined to exactly two nontrivial components, with respective state sets
\[
\{109,182,219\}\quad\text{and}\quad\{60,121,158,207,231,243\}.
\]
Each induced tight component is a simple directed cycle with one internal incoming and one internal outgoing arc at every state; their successive central-bit words are rotations of `110` and `111100`, respectively (the latter may appear as `110011` depending on starting state). No other tight directed cycle exists, because any directed closed walk stays within one strongly connected component. Consequently every \(n\ge9\) case attaining \(3|S|=2n\) is exactly one of those two periodic families, and the second requires \(6\mid n\).

**Small cases.** For \(3\le n\le8\), direct exhaustive enumeration of every vertex subset using the definition of an included \(K_{1,2}\) gives maxima \(2,2,3,4,4,5\), in order, equal to \(\lfloor2n/3\rfloor\). At \(n=3\), there are exactly three maximum minimal sets, namely the three rotations of `110`. At \(n=6\), there are exactly nine, namely the three rotations of `110110` and six rotations of `111100`. This completes the classification also for the exceptional short-cycle boundary.

**Attainment for all orders.** Every cycle has a 2-independent set of size \(\lfloor2n/3\rfloor\), obtained by repeating `110` and appending `0` or `10` for remainders one or two. These words contain no cyclic run of three selected vertices. They are maximal 2-independent sets, since their cardinality attains the elementary upper bound of at most two selected vertices per three consecutive positions. In any graph a maximal 2-independent set is a minimal 2-star-forming set: adding any omitted vertex creates a three-vertex path containing it, and deleting any selected vertex leaves that vertex outside every such path because the remaining induced degrees were at most one. Thus \(\mathrm{SF}_2(C_n)\ge\lfloor2n/3\rfloor\). Together with the finite-state upper bound and the short cases, equality holds for every \(n\ge3\). Counting the distinct rotations of the primitive periods three and six yields exactly three or nine labelled optimal sets in the divisible-by-three cases.

## Verification
Run the included standard-library Python program with `python3 verify.py`. It prints a `VERIFY_OK` line after checking the complete finite certificate (all 512 windows, 332 permitted arcs, 242 tight arcs, and the two cyclic SCCs), directly enumerating all vertex subsets for cycle lengths 3 through 14, verifying the claimed maximum and optimum multiplicity on those lengths, and comparing the independent path-enumeration predicate with the nine-window test on every subset for lengths 9 through 14. This is a reproducible finite certificate for the infinite closed-walk proof, not an extrapolation from finite cycle samples.

## Relationship to prior work
Chellali and Favaron introduced k-star-forming sets and the general inequality \(\beta_k(G)\le\mathrm{SF}_k(G)\) [1]. Bhattacharjee's October 2026 work [2] proves NP-completeness for the upper two-star-forming decision problem on bipartite graphs and addresses the equality with k-independence for chain graphs, without enumerating maximum minimal sets on cycles. Sahbi [3] treats related upper 2-star-forming questions on bipartite and chain graphs. The numerical lower bound from 2-independent sets and the star-forming definitions are previously known; the claim here is the complete cyclic extremal-word classification, exact multiplicity jump at lengths divisible by six, and sharp upper bound from a finite-state certificate. The exact theorem was not located in the inspected primary literature and mathematical-record searches; the full text of [3] was not available in the inspected access path, and historical priority has not been independently certified.

## Limitations
The full extremal-set classification and exact counts are asserted only for lengths divisible by three. For other lengths the maximum size is determined but the classification/count of all maximum minimal sets is not claimed. The theorem concerns simple labelled cycles and the standard non-induced-copy definition of 2-star-forming. It does not classify arbitrary minimal sets, general graphs of maximum degree two, or count modulo dihedral symmetry. The 256-state finite certificate is exact and reproducible but has not been independently audited.

## References
[1] M. Chellali and O. Favaron, *On k-star-forming Sets in Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 68 (2009), 205–214. https://combinatorialpress.com/article/jcmcc/Volume%20068/vol-068-paper%2014.pdf

[2] D. Bhattacharjee, *Upper k-star-forming sets and k-independence in bipartite graphs*, version of 23 October 2026, hexagon:2610.00498v1. https://hexagonmath.org/2610.00498v1

[3] R. Sahbi, *Upper k-Star-Forming Sets, k-Independence, and Upper Domination*, arXiv:2610.03785, October 2026. https://arxiv.org/abs/2610.03785
