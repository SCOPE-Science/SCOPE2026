# Exact minimal-Roman census of graph joins

## Finding
Let \(G\) and \(H\) be **arbitrary nonempty finite simple graphs** on disjoint vertex sets, of orders \(n\) and \(m\), respectively. They need not be connected. Their *join* \(G\vee H\) is obtained by inserting every edge between their vertex sets. A Roman dominating function (RDF) is a map \(f:V(X)\to\{0,1,2\}\) such that every vertex of label \(0\) has a neighbor of label \(2\). It is *pointwise minimal* if no different RDF can be obtained by decreasing any of its labels. Define the bivariate minimal-RDF polynomial
\[
\mathcal R_X(s,z)=\sum_{f\text{ pointwise-minimal RDF of }X}s^{|f^{-1}(2)|}z^{\sum_{v\in V(X)}f(v)}.
\]
Write \(i(X)\) for the number of isolated vertices, and \(p(X)\) for the number of **nonuniversal** vertices, i.e. vertices of degree strictly smaller than \(|V(X)|-1\). A single-vertex graph has \(i=1\) and \(p=0\) under these definitions. Then
\[
\boxed{\begin{aligned}
\mathcal R_{G\vee H}(s,z)
={}&\mathcal R_G(s,z)+\mathcal R_H(s,z)-z^n-z^m+z^{n+m}\\
&+i(G)s z^{n+1}+i(H)s z^{m+1}+p(G)p(H)s^2z^4.
\end{aligned}}
\]
This is an equality of polynomials, including overlapping degrees. It determines **every joint coefficient** recording the number of label-\(2\) vertices and the total weight for all finite graph joins. In particular, the number \(c(X)=\mathcal R_X(1,1)\) of pointwise-minimal RDFs satisfies
\[
\boxed{c(G\vee H)=c(G)+c(H)-1+i(G)+i(H)+p(G)p(H).}
\]

For example, both factors of \(K_{2,3}\) are edgeless, so
\[
\mathcal R_{K_{2,3}}(s,z)=z^5+2sz^3+3sz^4+6s^2z^4.
\]
The formula also yields a polynomial-time coefficient recurrence for *cographs* supplied with a recursive disjoint-union/join decomposition: at a disjoint union the bivariate polynomials multiply; at a join they obey the displayed identity. The required auxiliary quantities \(n,i,p\) are maintained by addition and the elementary rules in the proof.

## Assumptions and scope
All graphs are undirected, finite, loopless and simple, with named vertices. Both factors are nonempty; neither connectivity nor absence of isolated vertices is assumed. Universal means degree equal to order minus one, so the unique vertex of \(K_1\) is universal and isolated. Functions are counted with named vertex assignments, not modulo automorphisms. The polynomial concerns the *standard* Roman RDF feasibility rule and *pointwise* minimality with \(0<1<2\). It is **not** the polynomial of all feasible RDFs, nor a polynomial of minimum-weight RDFs only.

## Proof
**Canonical-label lemma.** Fix a finite graph \(X\) and a prospective nonempty set \(S\) of vertices carrying label \(2\). Any pointwise-minimal RDF with this exact \(S\) necessarily assigns label \(0\) to every vertex of \(N_X(S)\setminus S\) and label \(1\) to every vertex of \(V(X)\setminus N_X[S]\). Indeed, a label \(1\) at a neighbor of \(S\) could be lowered to \(0\), while a vertex not adjacent to any member of \(S\) cannot carry \(0\). Thus the labels are uniquely determined by \(S\). The resulting canonical RDF is pointwise minimal **if and only if** every \(v\in S\) has a zero-labeled neighbor \(w\) satisfying \(N_X(w)\cap S=\{v\}\). Necessity follows by lowering a label \(2\) to \(1\) when there is no such witness; sufficiency follows because every label \(1\) is outside \(N_X(S)\) and each label \(2\) has an indispensable private zero. When \(S=\varnothing\), the unique minimal RDF is the all-ones function, of weight \(|V(X)|\).

Apply the lemma to \(X=G\vee H\). Partition the functions by the intersection of \(S=f^{-1}(2)\) with the two shores.

**No label \(2\).** The sole function is all ones, contributing \(z^{n+m}\).

**Labels \(2\) only in \(G\).** Every vertex in \(H\) is zero. If \(|S|\ge2\), no vertex of \(H\) can be a private zero for any member of \(S\), because it sees all members of \(S\). The function is minimal precisely when its restriction to \(G\) is a minimal RDF. If \(S=\{v\}\), a vertex of \(H\) always provides a private zero. Hence *every* such singleton is minimal in the join; on \(G\) itself the singleton is minimal precisely when \(v\) has positive degree. The additional cases are the \(i(G)\) isolates of \(G\). Their canonical labels on \(G\) consist of one \(2\) and \(n-1\) ones and have weight \(n+1\). The complete contribution is therefore \(\mathcal R_G(s,z)-z^n+i(G)sz^{n+1}\). The symmetric case contributes \(\mathcal R_H(s,z)-z^m+i(H)sz^{m+1}\).

**Labels \(2\) in both shores.** Write \(S_G=S\cap V(G)\) and \(S_H=S\cap V(H)\). Every zero in \(H\) sees all of \(S_G\), and every zero in \(G\) sees all of \(S_H\). A private zero for a label-\(2\) vertex in \(G\) must lie in \(H\) (a zero in \(G\) sees a member of \(S_H\)). Consequently \(|S_G|=1\); symmetrically \(|S_H|=1\). Write \(S_G=\{g\}\) and \(S_H=\{h\}\). All remaining vertices are zero. The vertex \(g\) has a private zero exactly when \(h\) has a nonneighbor distinct from itself within \(H\), and \(h\) has a private zero exactly when \(g\) has a nonneighbor in \(G\). These are exactly the conditions that \(g\) and \(h\) are nonuniversal. There are \(p(G)p(H)\) choices, each containing two labels \(2\) and having weight \(4\). This yields the term \(p(G)p(H)s^2z^4\).

The four cases are disjoint and exhaustive. Summing their contributions proves the polynomial identity; evaluation at \(s=z=1\) gives the counting formula.

**Cograph consequence.** The RDF condition and pointwise minimality are componentwise on a disjoint union, whence \(\mathcal R_{G\sqcup H}=\mathcal R_G\mathcal R_H\). For nonempty factors, disjoint union has \(i(G\sqcup H)=i(G)+i(H)\) and \(p(G\sqcup H)=n+m\); join has \(i(G\vee H)=0\) and \(p(G\vee H)=p(G)+p(H)\). Starting from \(\mathcal R_{K_1}(s,z)=z\), these recurrences calculate all coefficients along a cograph construction tree using polynomially many integer operations on polynomials of polynomial degree. This is a computational consequence of the join identity, not a separate assumption.

## Verification
The accompanying standalone `verify.py` independently constructs arbitrary labeled graph pairs, constructs their joins, checks every labeling directly against the Roman condition, then tests pointwise minimality by every strict single-coordinate decrease. It compares the complete bivariate coefficient dictionaries with the displayed formula without using the canonical-label lemma to enumerate the left side. The provided test suite covers every pair of labeled graphs on shores of orders \(1\) through \(3\), plus 160 deterministic larger cases with shores of orders up to \(4\), including disconnected graphs, isolated vertices, and universal vertices. Successful execution prints

`VERIFY_OK join_pairs=281 direct_join_assignments=331245`

This computation is finite corroboration; the proof above establishes the theorem for every pair of nonempty finite simple graphs.

## Relationship to prior work
Abu-Khzam, Fernau, and Mann established a general private-neighbor characterization for pointwise-minimal Roman dominating functions and polynomial-delay enumeration (first public preprint 2022-04-10). Their characterization supplies useful general background, but their examined statements do not give this exact join decomposition, its nonuniversal-pair correction, or the bivariate identity. Their subsequent *Roman Census* work provides algorithms on split, cobipartite, interval, chordal, and forest graph classes and explicit path counts, not an arbitrary two-factor join formula. A separately published exact polynomial for **all feasible** Roman dominating functions of complete multipartite graphs concerns a different enumerated class; a bound on minimum weight or a formula for every feasible labeling does not yield the pointwise-minimal join identity without an additional privacy analysis. These distinctions are statements about the cited results, not claims of exhaustive publication priority.

## Limitations
The theorem requires a complete join, not an arbitrary graph product or partial edge join. Pointwise minimality is essential. The formula is symbolic in the factor enumerators; computing them for arbitrary input graphs may remain computationally difficult. The cograph consequence assumes an available decomposition. A pre-existing equivalent or stronger result outside the examined literature may exist; no independent review or publication-priority certification has been performed.

## References
1. F. N. Abu-Khzam, H. Fernau, K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765, first public preprint 2022-04-10; later *Algorithmica* 86 (2024), 1862–1887, DOI: 10.1007/s00453-024-01211-w.
2. F. N. Abu-Khzam, H. Fernau, K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261 (2022); MFCS 2023, LIPIcs 272, 6:1–6:15.
3. *Roman domination polynomial of complete multipartite graphs*, published mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-roman-domination-polynomial-of-complete-multipartite-graphs--fa4c41b40973 (a formula for all feasible RDFs rather than pointwise-minimal RDFs).
