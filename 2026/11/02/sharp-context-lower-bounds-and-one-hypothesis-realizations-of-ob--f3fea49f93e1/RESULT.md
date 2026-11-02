# Sharp context lower bounds and one-hypothesis realizations of observation contracts

## Finding
Let \(X\) be a finite set of binary source variables and let \(\mathcal H\subseteq 2^X\) be a **nonempty inclusion antichain of nonempty sets**, with \(m=|\mathcal H|\). In the contextual Horn-abduction semantics recalled below, write \(\kappa(\mathcal H)\) for the minimum number of possible contexts among **all** finite acyclic Horn instances with canonical observation contract \(\mathcal H\), allowing any finite hypothesis vocabulary. Define the private-coordinate rank
\[
\rho(\mathcal H)=\max\bigl\{|\mathcal F|:\mathcal F\subseteq\mathcal H,\ \forall e\in\mathcal F\ \exists v_e\in e\setminus\bigcup(\mathcal F\setminus\{e\})\bigr\}.
\]
Then
\[
\boxed{1+\rho(\mathcal H)\le\kappa(\mathcal H)\le m+1.}
\]
The upper bound has a realization with **one hypothesis atom**, and one is the minimum possible number of hypothesis atoms for a nonempty contract without an empty edge. If every edge has a private coordinate relative to all of \(\mathcal H\), then
\[
\boxed{\kappa(\mathcal H)=m+1.}
\]
In that equality case, any minimal-context realization has a spanning tree of pairwise-distinct obstruction-witness pairs, one labelled by each contract edge. For **pairwise disjoint** nonempty edges, every labelled tree supplies an optimal one-hypothesis realization.

## Assumptions and scope
A finite contextual abduction instance is \((X,H,T,g,C)\). Here \(H\) is a finite set of hypothesis atoms, \(C\) is a nonempty subset of \(\{0,1\}^X\), and \(T\) is a Horn theory with heads among derived atoms or an integrity symbol \(\bot\); source and hypothesis atoms are never heads. At context \(c\), the source facts are \(F_c=\{x^{c(x)}:x\in X\}\). A hypothesis subset \(S\subseteq H\) is valid when the least Horn closure of \(F_c\cup S\) contains the manifestation \(g\) but not \(\bot\). Write \(E_c\) for its family of valid hypothesis subsets. A nonempty \(D\subseteq C\) is a *minimal obstruction* if \(\bigcap_{c\in D}E_c=\varnothing\) while every proper nonempty subfamily has nonempty intersection (the empty intersection is \(2^H\)). The span \(\operatorname{span}(D)\) is the set of coordinates not constant on \(D\). The canonical observation contract consists of the inclusion-minimal sets among the spans of minimal obstructions. This is the precise semantics of Yang's Theorem 1 and Theorem 2.

All claims concern finite \(X\), nonempty edge collections, nonempty edges, possible contexts rather than all binary assignments, and the **minimum** number of contexts. No optimality claim is made for general intersecting hypergraphs without the private-coordinate property.

## Proof
**1. Lower bound.** Choose any private-coordinate subfamily \(\mathcal F\subseteq\mathcal H\) of size \(r\), with one coordinate \(v_e\) private to each \(e\in\mathcal F\). Because every contract edge is an actual inclusion-minimal obstruction span, choose for each \(e\) a minimal obstruction \(D_e\) with \(\operatorname{span}(D_e)=e\). Some \(c_e,d_e\in D_e\) differ at \(v_e\). Regard context assignments as vectors over \(\mathbb F_2\) and set \(z_e=c_e+d_e\). On the \(r\) coordinates indexed by the private coordinates \(v_f\), these difference vectors are the \(r\) standard unit vectors: \(z_e(v_e)=1\), and for \(f\ne e\), \(z_e(v_f)=0\) since \(v_f\notin e\). Thus the vectors \(\{z_e:e\in\mathcal F\}\) are linearly independent. All are differences of vectors in \(C\); their span has dimension at most \(|C|-1\), since differences from one fixed context span all pairwise differences. Hence \(|C|\ge r+1\). Maximizing over \(\mathcal F\) proves the left inequality for **every** Horn theory and every number of hypothesis atoms.

**2. One-hypothesis realization.** Put \(H=\{h\}\), set \(c_0=0^X\), and for each \(e\in\mathcal H\) let \(c_e\) be its incidence vector. Since edges are distinct and nonempty, \(C=\{c_0\}\cup\{c_e:e\in\mathcal H\}\) has exactly \(m+1\) distinct contexts. Let \(T\) consist of precisely
\[
 g\leftarrow F_{c_0},\qquad \bot\leftarrow h,F_{c_0},\qquad g\leftarrow h,F_{c_e}\quad(e\in\mathcal H).
\]
A notation \(g\leftarrow h,F_{c_e}\) means the single rule whose body includes \(h\) and every source literal in the full assignment \(F_{c_e}\). Full context guards match no different binary context. All heads are \(g\) or \(\bot\), so the dependency digraph is acyclic. At \(c_0\), exactly \(\varnothing\) is valid; at every \(c_e\), exactly \(\{h\}\) is valid. The minimal obstructions therefore are precisely the \(m\) pairs \(\{c_0,c_e\}\). Their spans equal \(e\); because \(\mathcal H\) is an antichain, the canonical contract is exactly \(\mathcal H\). There are \(m+2\) Horn rules and their overall input size is \(O((m+1)(|X|+1))\).

**3. Necessity of one hypothesis.** With \(H=\varnothing\), the only potential hypothesis subset is \(\varnothing\). Every \(E_c\) is either \(\{\varnothing\}\) or empty. If one is empty, the singleton \(\{c\}\) is a minimal obstruction with **empty** span, making the canonical contract \(\{\varnothing\}\). Otherwise there is no obstruction and the contract is empty. Neither case is the assumed nonempty antichain of nonempty edges. Hence at least one hypothesis atom is required, and the construction above is optimal.

**4. Sharpness and witness trees.** If every edge of \(\mathcal H\) has a private coordinate relative to the whole collection, then \(\rho(\mathcal H)=m\), giving equality in the context bounds. In a realization with exactly \(m+1\) contexts, choose pairs \(\{c_e,d_e\}\) as in step 1. These are distinct undirected edges on vertex set \(C\), and their \(m\) binary difference vectors are linearly independent. They cannot contain a graph cycle: summing edge differences along any cycle gives zero in \(\mathbb F_2^X\). Thus the \(m\) witness edges form an acyclic graph on \(m+1\) vertices and hence a spanning tree.

For the optional constructive converse when the contract edges are **pairwise disjoint**, choose any tree with \(m+1\) vertices, label its edges bijectively by the members of \(\mathcal H\), root it, and assign each tree vertex the xor of incidence vectors along its root path. The resulting contexts are all distinct because edge labels have disjoint nonempty supports. Give each even-depth vertex only the valid explanation \(\varnothing\) and each odd-depth vertex only \(\{h\}\), using exact-guard Horn rules \(g\leftarrow F_c\) and \(\bot\leftarrow h,F_c\) for the former, and \(g\leftarrow h,F_c\) for the latter. Opposite-colour vertex pairs are precisely the minimal obstructions. Their spans are unions of contract edges along the unique connecting path, and adjacent pairs realize the individual edges. Taking inclusion-minimal spans recovers exactly \(\mathcal H\), using one hypothesis and the optimal \(m+1\) contexts. The tree statement is a family of constructions, **not** a completeness classification.

## Verification
A standalone Python checker, supplied as `checker.py`, evaluates the actual Horn closures in the one-hypothesis construction, computes minimal empty-intersection obstruction families and their spans, and tests the private-coordinate lower bound on exhaustive finite semantic tables. It also enumerates tree codes with disjoint supports. Its recorded output is `ALL_CHECKS_OK antichains=193 semantic_tables=52670 tree_models=3103`. These are finite regression checks only; the universal lower bound and representation claims follow from steps 1–4, not from enumeration. Run with `python checker.py` in Python 3 without third-party dependencies.

## Relationship to prior work
Yang, *Choosing What to Observe: Higher-Order Obstructions in Horn Abduction*, arXiv:2610.32805v1 (public 2026-10-23), Theorems 1–2, establishes the canonical obstruction-span contract, arbitrary hypergraph realizability, an upper bound of \(m+1\) contexts, and a construction using **two** hypothesis atoms. The current claim does not reassert its already-known realizability or context upper bound as new. Its additional statements are (i) an optimal **one-hypothesis** construction, (ii) a general private-coordinate **lower** bound on the number of contexts, (iii) exact optimality for private-coordinate contract families, and (iv) a necessary witness-tree structure and constructive tree family for matching contracts. The classic discernibility matrix/function literature of Skowron–Rauszer concerns pairwise decision-table distinctions and reducts, and is a plausible predecessor for graph-difference arguments; equivalence of its full closed chapter to this resource theorem could not be ruled out.

## Limitations
The context lower bound is not asserted optimal for arbitrary overlapping edges. The witness-tree condition applies only when all contract edges have globally private coordinates; the tree construction itself assumes disjoint edges. One-hypothesis optimality excludes the empty contract and the contract with the empty edge, which behave differently. Binary source contexts and context-guard rules are part of the model. The general proof does not rely on finite enumeration. The 1992 Skowron–Rauszer chapter was not available as full text during the literature check and remains an originality risk.

## References
1. Y. Yang, *Choosing What to Observe: Higher-Order Obstructions in Horn Abduction*, arXiv:2610.32805v1, first posted 2026-10-23, https://arxiv.org/html/2610.32805v1, especially Section 4 and Theorem 2.
2. A. Skowron and C. Rauszer, *The Discernibility Matrices and Functions in Information Systems*, in *Intelligent Decision Support*, 1992, pp. 331–362, DOI:10.1007/978-94-015-7975-9_21 (abstract and later citations inspected; full chapter inaccessible).
3. A. Pawlak, *Rough Sets*, International Journal of Computer & Information Sciences 11 (1982), 341–356, classical background on information discernibility (not needed for proof).
