# Sharp direct-versus-iterative Horn bases for precedence constraints of finite linear orders

## Finding
For every integer \(n\ge 3\), let \(V=[n]\), \(E=\{(a,b):a,b\in V,\ a\ne b\}\), and let the objects be all strict linear orders on \(V\). A comparison attribute \((a,b)\) holds in an object if \(a\) precedes \(b\). Define \(c(S)\) as the common attributes of all orders satisfying every comparison in \(S\), taking the intersection of no objects to be \(E\). An implication means \(A\to B\), with a nonempty, possibly multi-attribute conclusion; one *simultaneous round* adds all conclusions whose premises lie in the input at the start of that round.

The globally minimum number of nontrivial implications whose iterated application generates \(c\) is
\[
I_n=n(n-1)(n-2)+\binom n2.
\]
A basis attaining this number uses one rule for each directed two-edge path and one for each directed two-cycle. Its exact worst-case number of simultaneous rounds to reach closure is
\[
L_n=\left\lceil\log_2(n-1)\right\rceil.
\]
The minimum number of implications in any *simultaneously direct* (one-round) basis is
\[
D_n=\sum_{\ell=2}^{n-1}\frac{n!}{(n-\ell-1)!}
+\sum_{\ell=2}^{n-1}\frac{n!}{\ell(n-\ell)!}.
\]
A minimum direct basis has one premise for each simple directed path of length at least two, and one premise for each simple directed cycle using fewer than \(n\) vertices. Directed Hamiltonian cycles need no separate direct rule. In particular, \(D_n=(e+o(1))n!\), whereas \(I_n\sim n^3\). For \(n=3,4,5\), respectively, \((I_n,D_n,L_n)=(9,9,1),(30,62,2),(70,360,2)\).

## Assumptions and scope
All orders are strict, complete, and transitive, on the fixed labeled ground set \(V\). The attributes are *oriented* comparisons, so \((a,b)\) and \((b,a)\) are different attributes. No loops are included. Inference is the simultaneous, order-independent operation \(\pi_\Sigma(S)=S\cup\bigcup_{A\to B\in\Sigma,\ A\subseteq S}B\). Rules with a conclusion already contained in their premise can be discarded. Rule counts use multi-conclusion implications and count distinct premises once; they are not counts of unit Horn clauses, ordered-direct sequences, or execution time.

## Proof
**Closure lemma.** Interpret \(S\subseteq E\) as a directed graph. If it is acyclic, its linear extensions are exactly the permitted objects. The intersection of all those orders is its strict reachability relation \(R(S)\): a directed path forces its endpoints to be ordered, while, if there is no path from \(a\) to \(b\), adding \(b\to a\) leaves a directed acyclic graph (otherwise there would be a path from \(a\) to \(b\)), and a topological order then witnesses that \(a\to b\) is not forced. If \(S\) contains a directed cycle, it has no linear extension, so \(c(S)=E\).

**Minimum unrestricted basis.** For every triple of distinct vertices \(a,b,c\), use \(\{(a,b),(b,c)\}\to\{(a,c)\}\). For every unordered pair \(\{a,b\}\), use \(\{(a,b),(b,a)\}\to E\). Repeatedly applying the first rules computes reachability; if a directed cycle occurs, it generates a directed two-cycle, activating the second rules. Thus the displayed \(I_n\) rules suffice. Conversely, from an input consisting of precisely \(a\to b\) and \(b\to c\), no proper subset forces any new attribute, while its closure adds \(a\to c\). Any complete implication basis must therefore have a rule with exactly this two-edge premise to make its first nontrivial inference. Similarly, the input consisting of the two opposite arrows \(a\to b\) and \(b\to a\) must have a rule with exactly this premise: its closure is \(E\), which strictly contains the input for \(n\ge3\), while no proper subset forces anything new. These distinct indispensable premises yield the lower bound \(I_n\).

**Minimum one-round basis.** For each simple directed path \(P=(v_0,\ldots,v_\ell)\) with \(2\le\ell\le n-1\), include the implication with premise its \(\ell\) consecutive arcs and conclusion all forward pairs along the path. For each simple directed cycle on \(2\le\ell\le n-1\) vertices, include the implication from its arc set to \(E\). If \(S\) is acyclic, each element of \(c(S)\setminus S\) has a simple witnessing path and is supplied in one round. If \(S\) has a directed cycle missing at least one vertex, its cycle rule supplies \(E\). Otherwise \(S\) contains a directed Hamiltonian cycle, and every ordered pair is an arc or the endpoints of a proper forward subpath of that cycle; all of \(E\) appears in one round without a Hamiltonian-cycle rule.

For necessity, start from precisely the edges of a simple path \(P\) of length \(\ell\ge2\). The comparison between its first and last vertices belongs to \(c(P)\setminus P\), but no proper subset of its arcs entails that comparison, by the closure lemma. Consequently a simultaneously direct basis must include a rule with premise exactly the arc set of \(P\). Likewise, start from precisely the arcs of a simple directed cycle \(C\) using fewer than \(n\) vertices. Its closure is \(E\), but every proper subset of its arcs is acyclic and cannot entail any comparison incident to a vertex outside \(C\). A direct basis therefore requires a rule with premise exactly \(C\). The listed path/cycle premises are distinct. There are \(n!/(n-\ell-1)!\) directed paths of length \(\ell\) and \(n!/(\ell(n-\ell)!)\) directed cycles on \(\ell\) vertices. This proves the exact \(D_n\).

**Sharp parallel depth.** Let \(\Sigma_I\) be the unrestricted basis above. At round \(t\), every oriented pair of distinct vertices joined in the initial graph by a directed walk of length at most \(2^t\) is present, by induction using midpoint decomposition. Write \(L=\lceil\log_2(n-1)\rceil\). If the initial graph is acyclic, all strict reachable pairs arise from paths of length at most \(n-1\), so closure is reached by round \(L\). For a cyclic graph, choose a simple directed cycle of length \(\ell\). If \(\ell=n\), its proper forward paths of length at most \(n-1\) supply all \(E\) by round \(L\). If \(\ell\le n-1\), by round \(L-1\) the two opposite comparisons between two almost-antipodal vertices on the cycle are present, since their forward cyclic distances are at most \(\lceil\ell/2\rceil\le 2^{L-1}\). The two-cycle rule supplies \(E\) at round \(L\). Conversely, from the \(n-1\) edges of a directed Hamiltonian path, no two-cycle rule fires, and each inferred comparison after \(t\) rounds spans a subpath of at most \(2^t\) original edges. Its first-to-last comparison needs \(2^t\ge n-1\). Thus \(L\) is exact.

**Asymptotics.** The path contribution is \(n!\sum_{j=0}^{n-3}1/j!=(e+o(1))n!\). Reindexing the cycle contribution gives \(n!\sum_{j=1}^{n-2}1/((n-j)j!)=o(n!)\), splitting the sum at \(j=n/2\). Hence \(D_n=(e+o(1))n!\).

## Verification
The included `verify.py` derives the model incidence matrix independently from all permutations, compares its common-attribute closure with both constructed bases, and asserts the exact cardinalities and depth claims. It exhaustively covers all \(2^6=64\) inputs for \(n=3\) and \(2^{12}=4096\) inputs for \(n=4\), as well as 1024 deterministic sampled inputs for \(n=5\). Separate directed Hamiltonian-cycle checks run for \(3\le n\le8\). These finite tests corroborate, but do not replace, the proofs for all integers \(n\ge3\).

## Relationship to prior work
Finite closure systems, direct implicational bases, and the tradeoff against iterative computation are classical; the works of Adaricheva–Nation–Rand and Baixeries–Napoli develop those general tools. The special objects here are pairwise precedence constraints realized across *all* strict linear orders, a different formal context from position-to-symbol permutation incidence. Generic basis theory does not supply the displayed exact premise counts or the sharp synchronous-depth formula without the directed-path/cycle analysis above. No claim is made that transitive closure, linear extensions, or the abstract existence of direct bases is new.

## Limitations
These formulas concern positive comparison attributes and multi-conclusion rules; allowing auxiliary attributes, ordered-in-place passes, or other encodings changes the minimization problem. No independent novelty certification or independent mathematical audit has been carried out. An equivalent presentation of the same special closure system under database dependency or order-constraint terminology is a residual priority risk.

## References
1. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229, first posted 2024-04-18, https://arxiv.org/abs/2404.12229.
2. K. Adaricheva, J. B. Nation, and R. Rand, *Ordered direct implicational basis of a finite closure system*, arXiv:1110.5805, https://arxiv.org/abs/1110.5805; Discrete Applied Mathematics 161 (2013), 707–723.
3. M. G. Rawson, A. Myers, R. Green, M. Robinson, and C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first posted 2023-07-21, https://arxiv.org/abs/2307.11681.
