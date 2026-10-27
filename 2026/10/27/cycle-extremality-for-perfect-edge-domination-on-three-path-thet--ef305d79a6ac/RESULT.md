# Cycle extremality for perfect edge domination on three-path theta graphs

## Finding

For integers \(a,b,c\ge 2\), let \(\Theta(a,b,c)\) be the simple graph formed from three internally vertex-disjoint paths of respective edge lengths \(a,b,c\) between the same two vertices. Its number of vertices is \(N=a+b+c-1\). A *perfect edge dominating set* (PED-set) is a set \(P\) of edges such that every edge outside \(P\) has **exactly one adjacent edge** in \(P\); edges inside \(P\) are unrestricted. Let \(F(a,b,c)\) denote the number of PED-sets, and let \(C_N\) be their number for the cycle on \(N\) vertices.

**Theorem.** For all \(a,b,c\ge2\),
\[
F(a,b,c)\le C_{a+b+c-1},
\]
with **equality if and only if** \(a=b=c=2\), when \(\Theta(2,2,2)\cong K_{2,3}\) and both counts equal \(6\). Therefore every other three-path theta graph satisfies the strict cycle upper bound conjectured for connected graphs by Grippo–Lin–Moyano–Vera.

The proof gives a complete exact enumeration formula. Use pair-state order \((00,01,10,11)\) and the integer matrix
\[
T=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
For \(\ell\ge2\), endpoint totals \(A,B\in\{0,1,2,3\}\), and prescribed first/last edge indicators \(f,g\in\{0,1\}\), put
\[
P_{\ell}^{A,B}(f,g)
=\sum_{h,p\in\{0,1\}}
\mathbf1_{\{f=1\ \mathrm{or}\ A+h=1\}}
(T^{\ell-2})_{(f,h),(p,g)}
\mathbf1_{\{g=1\ \mathrm{or}\ B+p=1\}}.
\]
Here a subscript \((u,v)\) refers to the corresponding row/column pair state. Then, **for all the stated lengths**,
\[
\boxed{
F(a,b,c)=\sum_{\mathbf f,\mathbf g\in\{0,1\}^3}
\prod_{i=1}^{3}P_{\ell_i}^{\sum_j f_j,\sum_j g_j}(f_i,g_i),
\quad (\ell_1,\ell_2,\ell_3)=(a,b,c).
}
\]
The cycle comparator is \(C_N=\operatorname{tr}(T^N)\). These formulas require only exact powers of the displayed four-state integer matrix.

## Assumptions and scope

The three paths are edge-distinct and have no common internal vertices, and every path has at least two edges; these conditions ensure a simple theta graph, including \(K_{2,3}\) at the smallest parameters. Paths and their edges are fixed graph objects, not quotiented by symmetries. We count *all* PED edge subsets, including the full edge set, not just minimum-cardinality sets or dominating induced matchings. The cycle has the same number of vertices as the theta graph. All counts are exact nonnegative integers.

## Proof

**Local edge rule.** Record each edge's membership in \(P\) as a bit, \(1\) for membership. On one theta path let the consecutive bits be \(x_1,\ldots,x_\ell\). If an internal edge \(x_j\) is zero, its only adjacent edges are \(x_{j-1}\) and \(x_{j+1}\); hence its necessary and sufficient rule is
\[
x_j=0\quad\Longrightarrow\quad x_{j-1}+x_{j+1}=1\qquad(2\le j\le\ell-1).
\]
Let \(A\) (respectively \(B\)) be the total number of selected first (respectively last) edges of the three paths at the common initial (respectively terminal) vertex. The boundary rules for a path whose first bit is \(f\) and last bit is \(g\) are exactly
\[
f=0\Longrightarrow A+x_2=1,\qquad
 g=0\Longrightarrow B+x_{\ell-1}=1.
\]
A selected edge imposes no further restriction. These are all edge conditions, so they are jointly necessary and sufficient for a PED-set.

**Transfer enumeration.** A consecutive pair \((u,v)\) can be extended by a new bit \(w\) precisely when \(v=1\) or \(u+w=1\). In the indicated pair order this is exactly the displayed matrix \(T\). Thus its power \(T^{\ell-2}\) counts all sequences with fixed first and last pairs satisfying every interior zero-edge rule. Multiplying by the two endpoint indicators gives \(P_\ell^{A,B}(f,g)\). Summing independently over the three paths, while enforcing \(A=\sum_i f_i\) and \(B=\sum_i g_i\), proves the exact theta enumeration. For a cycle the same pair transition closes cyclically; a closed sequence of \(N\) transitions is in bijection with a cyclic edge-membership word, hence \(C_N=\operatorname{tr}(T^N)\) for \(N\ge3\).

**Common recurrence.** Exact multiplication gives
\[
T^4=T^3+T.
\]
Consequently, for any fixed boundary data and every \(\ell\ge6\),
\[
P_{\ell}^{A,B}(f,g)=P_{\ell-1}^{A,B}(f,g)+P_{\ell-3}^{A,B}(f,g).
\]
The sum/product formula therefore yields, whenever \(a\ge6\),
\[
F(a,b,c)=F(a-1,b,c)+F(a-3,b,c),
\]
and likewise in either other argument of length at least six. The cycle sequence satisfies \(C_3=4,C_4=5,C_5=6\) and \(C_N=C_{N-1}+C_{N-3}\) for \(N\ge6\), again directly from the matrix identity.

**Finite base and induction.** It suffices to check the unordered triples with all lengths in \(\{2,3,4,5\}\), because \(F\) is symmetric in its three arguments. The table lists the exact theta count and the nonnegative difference \(\Delta(a,b,c)=C_{a+b+c-1}-F(a,b,c)\). Each value is obtained by the displayed finite four-state formula and independently reproduced by enumerating every subset of the at most 15 graph edges.

| \((a,b,c)\) | \(F\) | \(\Delta\) | \((a,b,c)\) | \(F\) | \(\Delta\) |
|---|---:|---:|---|---:|---:|
| \((2,2,2)\) | 6 | 0 | \((2,2,3)\) | 4 | 6 |
| \((2,2,4)\) | 6 | 9 | \((2,2,5)\) | 12 | 9 |
| \((2,3,3)\) | 7 | 8 | \((2,3,4)\) | 8 | 13 |
| \((2,3,5)\) | 12 | 19 | \((2,4,4)\) | 12 | 19 |
| \((2,4,5)\) | 18 | 28 | \((2,5,5)\) | 30 | 37 |
| \((3,3,3)\) | 10 | 11 | \((3,3,4)\) | 13 | 18 |
| \((3,3,5)\) | 20 | 26 | \((3,4,4)\) | 19 | 27 |
| \((3,4,5)\) | 27 | 40 | \((3,5,5)\) | 39 | 59 |
| \((4,4,4)\) | 29 | 38 | \((4,4,5)\) | 41 | 57 |
| \((4,5,5)\) | 59 | 85 | \((5,5,5)\) | 89 | 122 |

Now induct on \(a+b+c\). For any triple outside this finite cube, at least one coordinate, say \(a\), is at least six. By the theta and cycle recurrences, the corresponding difference obeys
\[
\Delta(a,b,c)=\Delta(a-1,b,c)+\Delta(a-3,b,c).
\]
Both predecessor triples retain lengths at least two and have smaller sum; neither can be \((2,2,2)\), because their first coordinates are at least five and three. By induction both differences are strictly positive. The base table has one equality only, completing the proof for every triple of allowed positive integer lengths. \(\square\)

## Verification

The self-contained `verify_theta.py` uses only Python 3's standard library. Run `python3 verify_theta.py` in the package directory. It directly verifies the \(4\times4\) transfer identity, recomputes all twenty base triples using the transfer formula **and** an independent edge-subset predicate, checks additional small theta graphs by exhaustive enumeration, and tests the recurrences on a larger finite parameter range. The executable prints `VERIFY_OK` when all checks pass. The infinite theorem rests on the proved recurrence and induction, not on extrapolating these finite experiments.

## Relationship to prior work

Grippo, Lin, Moyano and Vera [1] introduce the PED-set counting framework used here, establish the cycle sequence and recurrence, give a linear-time enumeration algorithm on generalized series-parallel graphs (which include theta graphs), and pose the connected-graph cycle upper bound as Conjecture 5.1. That algorithm can compute individual theta instances; the present result adds the explicit all-length transfer formula and an **infinite-family proof** of their conjectured bound, with the exact equality case. The primary 2026 full-text HTML was inspected at its definitions and concluding conjecture, and searched for theta-specific statements without a match. The 2002 generalized series-parallel PED algorithm of Lu, Ko and Tang [2] is prior algorithmic coverage, not an identified proof of the exact extremal inequality. Grippo, Lin and Vera [3] study counting in \(P_6\)-free graphs, another computationally covered subclass; their reported result is not an all-theta cycle comparison. The relationship of PED-sets to perfect dominating sets of line graphs is a change of language, not a separate novelty claim.

## Limitations

The result covers only three internally disjoint paths, not arbitrary bicyclic, generalized series-parallel, or connected graphs. It does not prove the full cycle extremality conjecture. The general preexisting counting algorithm could in principle be specialized to give the numerical formula, so the substantive new point is its structural recurrence and rigorous extremal comparison. Independent validation and exhaustive historical-priority verification have not been performed; relevant older algorithmic full texts were not all obtained. The existence of a larger theorem in inaccessible literature is an outstanding priority risk, not ruled out by the searches.

## References

[1] L. N. Grippo, M. C. Lin, V. Moyano and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, first public 2026-07-04. https://arxiv.org/html/2607.03894

[2] C. L. Lu, M.-T. Ko and C. Y. Tang, *Perfect edge domination and efficient edge domination in graphs*, Discrete Applied Mathematics 119 (2002), 227–250. Cited and discussed by [1], Section 4.

[3] L. N. Grippo, M. C. Lin and C. Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v1, first public 2025-09-04. https://arxiv.org/abs/2509.04598
