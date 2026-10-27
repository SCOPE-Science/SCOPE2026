# Super domination polynomials of leaf coronas as Widom–Rowlinson partition functions

## Finding
Let \(H=(V,E)\) be any finite simple undirected graph with \(n=|V|\ge1\), and form its **one-leaf corona** \(W(H)=H\circ K_1\) by adjoining a private leaf \(v'\) to every \(v\in V\). Write \(c(J)\) for the number of connected components of a graph \(J\), with \(c(\varnothing)=0\). The complete super domination polynomial of \(W(H)\) is
\[
\boxed{\mathcal S_{W(H)}(z)=\sum_{U\subseteq V}2^{c(H[U])}z^{2n-|U|}.}
\]
Equivalently, its super dominating sets correspond weight-preservingly to homomorphisms from \(H\) into the reflexive three-vertex path \(P_3^\circ\), in which the middle state has weight \(z^2\) and the two endpoint states each have weight \(z\). Thus its total number of super dominating sets is precisely the two-species Widom–Rowlinson partition function:
\[
\mathcal S_{W(H)}(1)=\operatorname{hom}(H,P_3^\circ).
\]
As a complexity consequence, **counting all super dominating sets is \(\#\mathrm P\)-complete** even when the input graph is a one-leaf corona of a base graph of maximum degree at most three (hence a corona of maximum degree at most four).

For connected \(H\) with \(n\ge2\), its first coefficient above the minimum records vertex cuts:
\[
[z^{n+1}]\mathcal S_{W(H)}(z)
=\sum_{v\in V}2^{c(H-v)}\ge2n,
\]
and equality holds **if and only if \(H\) has no cut vertex**. At minimum size the previously known result \([z^n]\mathcal S_{W(H)}(z)=2^{c(H)}\) is recovered; this minimum-set formula is not asserted to be new.

## Assumptions and scope
All graphs are finite, simple and undirected. For \(D\subseteq V(G)\), write \(\overline D=V(G)\setminus D\). The set \(D\) is **super dominating** if for every \(u\in\overline D\) some \(w\in D\) has
\[
N_G(w)\cap\overline D=\{u\}.
\]
The polynomial \(\mathcal S_G(z)=\sum_{D\text{ super dominating}}z^{|D|}\) counts each selected vertex subset once, including the full vertex set. The corona includes the \(n\) original edges \(vv'\), one for each \(v\), together with every edge of \(H\); private leaves have degree one. The target \(P_3^\circ\) is a three-vertex path with a loop at each vertex and no edge between its two endpoints; loops are permitted in the fixed target only, not in \(H\) or \(W(H)\).

## Proof
**Step 1: classify every arm.** If \(D\) is super dominating in \(W(H)\), the pair \(\{v,v'\}\) must meet \(D\): if both vertices were omitted, the omitted leaf \(v'\) would have no selected neighbor. Hence each pair has exactly one of three possible selected states:

- state \(A\): both \(v,v'\) are selected;
- state \(B\): \(v\) is selected and \(v'\) omitted;
- state \(C\): \(v'\) is selected and \(v\) omitted.

If \(v\) has state \(C\), then the sole neighbor \(v'\) is selected, has no other neighbor, and super dominates the omitted core vertex \(v\). If \(v\) has state \(B\), the omitted leaf \(v'\) has only its selected core vertex \(v\) as a possible witness. This witness is valid exactly when \(v\) has no other omitted neighbor, i.e. exactly when no neighbor of \(v\) in \(H\) has state \(C\). There is no omitted vertex on a state-\(A\) arm. Thus the three-state assignment is admissible **if and only if** no edge of \(H\) joins states \(B\) and \(C\). These are precisely the homomorphisms \(H\to P_3^\circ\), where \(A\) is the middle vertex and \(B,C\) its endpoints. The selected size is \(2\) per \(A\) and \(1\) per \(B\) or \(C\).

**Step 2: sum over monochromatic components.** For an admissible state assignment put \(U=\{v:\text{the arm at }v\text{ is }B\text{ or }C\}\). Then every vertex in \(V\setminus U\) has state \(A\). The only restriction left is that every edge of \(H[U]\) has the same endpoint state \(B\) or \(C\) on both ends. Equivalently, each connected component of \(H[U]\) is entirely one state, with two independent choices per component. There are exactly \(2^{c(H[U])}\) assignments for fixed \(U\), each of weight \(z^{2(n-|U|)+|U|}=z^{2n-|U|}\). Summing yields the asserted polynomial. In particular, the least degree is \(n\) (achieved by \(U=V\)), its coefficient is \(2^{c(H)}\), and the top degree has coefficient one.

**Step 3: cuts in the next coefficient.** For connected \(H\) of order \(n\ge2\), the \(z^{n+1}\) term is obtained exactly by \(U=V\setminus\{v\}\) for some \(v\). It therefore has the displayed coefficient \(\sum_v 2^{c(H-v)}\). Every \(H-v\) is nonempty and has at least one component, giving \(2^{c(H-v)}\ge2\), with equality precisely when \(H-v\) is connected. All summands attain equality simultaneously exactly when \(H\) has no cut vertex.

**Step 4: counting complexity.** The map \(H\mapsto W(H)\) is computable in linear time relative to the graph encoding. The bijection in Step 1 gives the **exact equality**
\[
\#\{D:D\text{ super dominates }W(H)\}=\#\operatorname{Hom}(H,P_3^\circ).
\]
Dyer and Greenhill's fixed-target homomorphism-counting dichotomy places \(P_3^\circ\) on the \(\#\mathrm P\)-complete side: it is connected and neither a fully looped clique nor an unlooped complete bipartite graph. They additionally establish hardness for the Widom–Rowlinson target on input graphs of maximum degree three. Hence the polynomial-time map above is a parsimonious reduction yielding hardness even for coronas \(W(H)\) with \(\Delta(H)\le3\), for which \(\Delta(W(H))\le4\). Membership in \(\#\mathrm P\) follows by guessing a subset \(D\) and verifying the defining private-neighbor condition in polynomial time. This proves the \(\#\mathrm P\)-completeness assertion. The hardness theorem of Dyer and Greenhill is used as established prior literature, not reproved here.

## Verification
The included standalone `verify.py` independently constructs \(W(H)\) and checks every candidate subset against the original private-neighbor condition. It separately evaluates the component expansion and enumerates all admissible three-state assignments, comparing complete coefficient dictionaries. It checks all labeled graphs with \(1\le n\le4\) and 108 additional fixed-seed graphs of orders five through seven: **183 base graphs** total. It also checks the minimum coefficient and the cut-vertex equality on every connected case. Execution:

```
python3 verify.py
```

Expected output begins `PASS: 183 base graphs`. For a four-vertex path, the polynomial is \(2z^4+12z^5+18z^6+8z^7+z^8\); for a four-cycle it is \(2z^4+8z^5+16z^6+8z^7+z^8\). These finite calculations test implementation and boundary cases, **not** the infinite proof or the imported complexity theorem.

## Relationship to prior work
Klein, Rodríguez-Velázquez and Yi (arXiv:1705.00928, Section 3, Theorem 18) give the super domination **number** for ordinary coronas, including \(\gamma_{\mathrm{sp}}(H\circ K_1)=n\); they do not derive the full cardinality polynomial. Ghanbari, Jäger and Lehtilä (arXiv:2209.01795, first public 2022-09-05) count minimum sets for selected graph families and study the distinct **neighborhood corona** product; their conclusions propose counting super dominating sets of trees as a direction. A previously published result entitled “Minimum super dominating sets of one-leaf coronas” determines the minimum-set classification \(2^{c(H)}\) for arbitrary bases, which is explicitly recovered rather than reclaimed.

The Widom–Rowlinson homomorphism count, its induced-component formula at unit weights, and its \(\#\mathrm P\)-completeness are established prior mathematics: Dyer and Greenhill (2000) prove the complexity theorem. A published result on metric-space one-point extension types gives even a multivariate Widom–Rowlinson partition polynomial; the present formula is a specialization **on the spin-model side**. The retained claim here is the **new exact identification with all super dominating sets of the one-leaf corona**, its cut-vertex coefficient, and its consequence for counting on a strongly restricted class of graphs. Existing super domination polynomial results for particular tree families, and a general forest dynamic program, cover some acyclic bases but do not yield the arbitrary-base structural identification or the hardness statement.

## Limitations
The assertion concerns only the ordinary one-leaf corona, not arbitrary attached graphs or the neighborhood corona. The result transfers a known \(\#\mathrm P\)-hard partition function; it does not discover that spin model or prove the complexity dichotomy anew. A 2024 chapter by Kaidash, “Super Domination Polynomial of a Graph,” was available only as an abstract/preview; its exact list of computed graph families could not be checked, and overlap with unindexed or inaccessible work remains a priority risk. The proof and reproducible finite checks establish the mathematics stated here but do not constitute independent review.

## References
1. D. J. Klein, J. A. Rodríguez-Velázquez and E. Yi, “On the super domination number of graphs,” arXiv:1705.00928, publicly posted 2017-05-02, Section 3, Theorem 18. https://arxiv.org/abs/1705.00928
2. N. Ghanbari, G. Jäger and T. Lehtilä, “Super Domination: Graph Classes, Products and Enumeration,” arXiv:2209.01795v1, publicly posted 2022-09-05; Discrete Applied Mathematics 349 (2024), 8–24, DOI:10.1016/j.dam.2024.01.039. https://arxiv.org/abs/2209.01795
3. M. Dyer and C. Greenhill, “The complexity of counting graph homomorphisms,” Random Structures & Algorithms 17 (2000), 260–289, Theorems 1.1–1.2, with subsequent corrigendum. https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/dg00b.pdf
4. P. A. Kaidash, “Super Domination Polynomial of a Graph,” Mathematical Optimization Theory and Operations Research: Recent Trends (2024), pp. 85–95, DOI:10.1007/978-3-031-73365-9_6 (abstract available; full text not inspected).
5. “Minimum super dominating sets of one-leaf coronas,” published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-minimum-super-dominating-sets-of-one-leaf-coronas--304999ba8c77.
6. “Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space,” published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989.
