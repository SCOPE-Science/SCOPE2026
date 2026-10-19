# Two parity-dependent stabilization thresholds for near-extremal sum-free exchange graphs

## Finding
For a positive integer \(n\), write \([a,b]=\{a,a+1,\ldots,b\}\) and let \(k=\lceil n/2\rceil-1\). Let \(\mathcal E_n\) be the graph whose vertices are the \(k\)-element sum-free subsets of \([1,n]\); two vertices are adjacent when their symmetric difference has size two. A set is sum-free if it contains no \(x,y,z\) with \(x+y=z\), including the possibility \(x=y\).

For every odd \(n=2m+1\) with \(m\ge7\), \(\mathcal E_n\) has precisely two connected components, of orders \(m+1\) and \(m+3\), and
\[|V(\mathcal E_n)|=2m+4,\qquad |E(\mathcal E_n)|=m(m+1)+5.\]
For every even \(n=2m\) with \(m\ge10\), it has precisely two components, of orders \(m\) and \(2m+2\), and
\[|V(\mathcal E_n)|=3m+2,\qquad |E(\mathcal E_n)|=m(m-1)+\binom{m-1}{2}+2(m-1)+9.\]
In both cases one component is a complete graph consisting of all \(k\)-subsets of the odd numbers; the other is explicitly classified below, including every edge. The parity thresholds are sharp for eventual two-component stabilization: at \(n=13\) and \(n=18\), respectively, there are four components, not two.

## Assumptions and scope
Only ordinary sum-freeness in positive integers is considered, with repeated addends forbidden as above. This is not sum-freeness modulo \(n\), nor inclusion-maximality. The exchange move is a single removal and a single insertion at fixed size \(k\); one must remain sum-free after each move. The theorem concerns all odd \(n\ge15\) and all even \(n\ge20\). The maximum possible cardinality in \([1,n]\) is \(\lceil n/2\rceil\): if \(M\) is the maximum element of a nonempty sum-free \(A\), then \(A\) and the \(|A|-1\) positive differences \(M-a\) for \(a\in A\setminus\{M\}\) are disjoint subsets of \([1,M]\), whence \(2|A|-1\le M\). The odd-number set attains the bound.

## Proof
**Structural reduction.** We use Deshouillers–Freiman–Sós–Temkin, Theorem 1.1 [1]: if a sum-free set \(A\) with largest member \(M\) satisfies \(|A|>0.4M+0.8\), then either every member is odd or \(\min(A)\ge |A|\). This theorem is an existing structural input, not a result proved here. In the odd case \(k=m\) and \(m>0.4(2m+1)+0.8\) for \(m\ge7\). In the even case \(k=m-1\) and \(m-1>0.4(2m)+0.8\) for \(m\ge10\). Since \(M\le n\), this reduction applies to every vertex in the asserted ranges.

**Odd case.** Put \(n=2m+1\). The all-odd vertices are all ways of omitting one from the \(m+1\) odd integers; they form \(K_{m+1}\). Every non-odd vertex has minimum at least \(m\). Define
\[U_t=[m+1,2m+1]\setminus\{t\}\quad (m+1\le t\le2m+1),\]
\[A_0=[m,2m-1],\qquad A_1=\{m\}\cup[m+2,2m-1]\cup\{2m+1\}.\]
If the minimum exceeds \(m\), the vertex is one of the \(U_t\). If it equals \(m\), exactly two elements of \([m,2m+1]\) are omitted; \(2m\) is forbidden by \(m+m=2m\). Depending on whether \(m+1\) is present, the second omission is \(2m+1\) or \(m+1\), giving exactly \(A_0,A_1\). Every listed set is directly sum-free, so no candidates were lost. The \(U_t\) induce \(K_{m+1}\). The remaining five edges are
\[A_0A_1,\quad A_0U_{2m},\quad A_0U_{2m+1},\quad A_1U_{m+1},\quad A_1U_{2m}.\]
All edge assertions follow by checking that intersecting \(k\)-sets differ in one member exactly when the intersection has \(k-1\) elements. These edges make the non-odd induced graph connected, of order \(m+3\), and give the stated count. No all-odd vertex can be adjacent to a non-odd vertex: the latter is contained in \([m,2m+1]\), which has at most \(\lceil(m+2)/2\rceil<m-1\) odd elements when \(m\ge7\), whereas a swap adjacency to an all-odd \(m\)-set would require \(m-1\) common odd elements.

**Even case.** Put \(n=2m\). All-odd \((m-1)\)-sets are one-omission subsets of the \(m\) odd integers and form \(K_m\). Every other vertex has minimum at least \(m-1\). Define
\[U_t=[m+1,2m]\setminus\{t\}\quad(m+1\le t\le2m),\]
\[V_s=[m,2m-1]\setminus\{s\}\quad(m+1\le s\le2m-1),\]
\[W_0=[m-1,2m-3],\]
\[W_1=\{m-1\}\cup[m+1,2m-3]\cup\{2m-1\},\]
\[W_2=\{m-1\}\cup[m+2,2m-3]\cup\{2m-1,2m\}.\]
If the minimum exceeds \(m\), one omission from \([m+1,2m]\) gives \(U_t\). If the minimum is \(m\), then \(2m\) is forbidden by doubling, leaving one omission from \([m+1,2m-1]\), hence \(V_s\). If the minimum is \(m-1\), the element \(2m-2\) is forbidden by doubling. Of the remaining two omissions, including \(m\) forces both \(2m-1\) and \(2m\) to be omitted, giving \(W_0\). Omitting \(m\) instead forces at least one of \(m+1,2m\) to be omitted (their sum with \(m-1\) would be \(2m\)), giving \(W_1\) or \(W_2\). The displayed families are all sum-free and have \(m-1\) elements.

Inside the non-odd family, the \(U_t\) induce \(K_m\), and the \(V_s\) induce \(K_{m-1}\). Cross edges \(U_tV_s\) exist exactly when \(t=s\) or \(t=2m\), for \(m+1\le s\le2m-1\), giving \(2(m-1)\) edges. The remaining nine edges, and no others, are
\[W_0W_1,\ W_1W_2,\ W_0V_{2m-2},\ W_0V_{2m-1},\ W_1V_{2m-2},\]
\[W_1U_{2m-2},\ W_1U_{2m},\ W_2U_{m+1},\ W_2U_{2m-2}.\]
These are verified by \((m-2)\)-element intersections. The \(U\)-to-\(V\) edges connect the two cliques and every \(W\) attaches, so this component has order \(2m+2\); summing the indicated edge classes proves the formula. As in the odd case, there are no cross edges to the all-odd clique: a non-odd set lies in \([m-1,2m]\), having at most \(\lceil(m+2)/2\rceil<m-2\) odd elements for \(m\ge10\), whereas a one-swap neighbor of an all-odd \((m-1)\)-set would share \(m-2\) odd elements.

**Boundary sharpness.** A finite exhaustive enumeration, using the algorithm in `verify_exhaustive.py`, yields four components of sizes \((9,7,1,1)\) at \(n=13\) and four of sizes \((20,9,1,1)\) at \(n=18\). These are precisely the preceding odd and even parameter values, so neither eventual two-component range can be extended one step backward in its parity class.

## Verification
`verify_exhaustive.py` independently enumerates every admissible fixed-cardinality subset by Schur-triple-avoiding backtracking, constructs all one-swap edges and connected components for \(13\le n\le29\), and checks the formulas throughout the asserted range. It includes the two boundary counterchecks. `verify_symbolic_families.py` constructs the displayed families directly, verifies each set has the right size and is sum-free, independently computes all pairwise intersections and components for all odd \(15\le n<100\) and even \(20\le n\le100\), and verifies the formulas. Both output `VERIFY_OK`; recorded outputs accompany the programs. The infinite parameter claims do not rely on finite extrapolation: they follow from the structural theorem and the displayed symbolic case analysis.

## Relationship to prior work
Freiman [2] and Deshouillers–Freiman–Sós–Temkin [1] supply strong structural information about dense sum-free sets, used here explicitly as a premise. In particular [1, Theorem 1.1] yields the dichotomy essential to the proof. Alon–Balogh–Morris–Samotij [3] count fixed-size sum-free subsets asymptotically and study their large-scale structure, but do not classify the graph of fixed-cardinality one-swap moves. The present contribution is the complete **exchange graph**, including exactly which configurations can reach one another, the clique-and-attachment descriptions, exact edge counts and sharp parity thresholds. A structural description of the individual sets is not by itself a reachability theorem.

## Limitations
The range excludes smaller \(n\), whose graphs can have more components. No claim is made about different exchange rules, other cardinalities or sum-freeness in groups. The proof relies on the previously established strong structural theorem [1], not an independent proof of that theorem. The 1992 and 1999 papers have verified publication years but no verified day-precise first public release dates; the bibliographic day used in machine metadata is the verified public arXiv submission of source [3], not an assertion that the subject was first studied then. Global publication uniqueness remains subject to overlooked or unindexed work; in particular, a characterization obtained implicitly elsewhere could cover portions of this classification.

## References
[1] J.-M. Deshouillers, G. A. Freiman, V. Sós, M. Temkin, *On the structure of sum-free sets, 2*, Astérisque 258 (1999), 149–161, Theorem 1.1, DOI: 10.24033/ast.443, https://numdam.org/item/AST_1999__258__149_0/.

[2] G. A. Freiman, *On the structure and the number of sum-free sets*, Astérisque 209 (1992), 195–201, https://numdam.org/article/AST_1992__209__195_0.pdf.

[3] N. Alon, J. Balogh, R. Morris, W. Samotij, *A refinement of the Cameron–Erdős conjecture*, arXiv:1202.5200v1 (first submitted 2012-02-23), https://arxiv.org/abs/1202.5200.
