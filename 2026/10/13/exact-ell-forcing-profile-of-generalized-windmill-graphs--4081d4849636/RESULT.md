# Exact \(\ell\)-forcing profile of generalized windmill graphs
## Finding
Let \(r\ge2\), \(m\ge2\), and \(1\le \ell\le rm\). Define the generalized windmill
\[
W_{r,m}=K_1\vee rK_m,
\]
with center \(c\) and pairwise disjoint peripheral cliques \(B_1,\ldots,B_r\), each of size \(m\). Under the \(\ell\)-forcing rule, a black vertex with at most \(\ell\) white neighbors colors all of those white neighbors black.

For an initial black set \(S\), put \(w_i=|B_i\setminus S|\) and \(f=|\{i:w_i=m\}|\). Then \(S\) is \(\ell\)-forcing if and only if the following conditions hold.

For \(1\le\ell<m\):
- if \(c\in S\), then \(w_i\le\ell\) for every \(i\);
- if \(c\notin S\), then \(w_i\le\ell\) for every \(i\), and \(w_j\le\ell-1\) for at least one \(j\).

For \(m\le\ell\le rm\):
- if \(c\in S\), then \(f\le\lfloor\ell/m\rfloor\);
- if \(c\notin S\), then \(f\le\lfloor\ell/m\rfloor\) and at least one peripheral vertex is initially black.

Define
\[
A_{m,\ell}(x)=\sum_{j=0}^{\ell}\binom mj x^{m-j}\qquad(\ell<m)
\]
and
\[
B_m(x)=(1+x)^m-1.
\]
The complete cardinality enumerator of \(\ell\)-forcing sets is
\[
\Phi_{r,m,\ell}(x)=
\begin{cases}
(1+x)A_{m,\ell}(x)^r-\binom m\ell^r x^{r(m-\ell)},&1\le\ell<m,\\
(1+x)\displaystyle\sum_{f=0}^{\lfloor\ell/m\rfloor}\binom rf B_m(x)^{r-f},&m\le\ell<rm,\\
(1+x)^{rm+1}-1,&\ell=rm.
\end{cases}
\]
Therefore
\[
F_\ell(W_{r,m})=
\begin{cases}
r(m-\ell)+1,&1\le\ell<m,\\
r-\lfloor\ell/m\rfloor,&m\le\ell<m(r-1),\\
1,&m(r-1)\le\ell\le rm.
\end{cases}
\]
The numbers of minimum \(\ell\)-forcing sets are, respectively,
\[
\binom m\ell^r+r\binom m{\ell-1}\binom m\ell^{r-1},
\]
\[
\binom r s m^{r-s}\quad\text{where }s=\lfloor\ell/m\rfloor,
\]
and
\[
rm+\mathbf 1_{\{\ell=rm\}}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The parameter range \(1\le\ell\le\Delta(W_{r,m})=rm\) matches the standard \(k\)-forcing convention in the foundational literature. The notation uses \(r\) for the number of blades and \(\ell\) for the forcing threshold to avoid overloading the letter \(k\).

The result concerns the full set profile, not only the minimum parameter. The specialization \(\ell=1\) is ordinary zero forcing. In particular, for the friendship graph \(W_{r,2}\), the scalar equality \(F_1(W_{r,2})=r+1\) is not asserted as new; it is consistent with existing zero-forcing treatments of friendship graphs and with cut-vertex methods.

## Proof
Fix an initial black set \(S\). A black peripheral vertex in blade \(B_i\) sees all white vertices of its own blade and possibly the center, but no vertex of another blade.

First suppose \(c\in S\). A nonfull blade \(B_i\) contains a black peripheral vertex, and such a vertex has exactly \(w_i\) white neighbors. Hence that blade can clear itself precisely when \(w_i\le\ell\). A full white blade has no black peripheral vertex and can only be colored by the center. After every self-clearable nonfull blade has cleared, the center sees exactly \(fm\) white neighbors in the full blades.

If \(\ell<m\), a full blade can never be cleared by the center, because it alone contributes \(m>\ell\) white neighbors. Thus success is equivalent to \(w_i\le\ell\) for every blade. If \(\ell\ge m\), every nonfull blade satisfies \(w_i\le m-1\le\ell\) and therefore clears itself. The process then succeeds exactly when \(fm\le\ell\), equivalently \(f\le\lfloor\ell/m\rfloor\).

Now suppose \(c\notin S\). A black peripheral vertex in \(B_i\) initially has \(w_i+1\) white neighbors: the \(w_i\) white vertices of its blade and the white center. Therefore a first force exists in blade \(B_i\) exactly when \(w_i+1\le\ell\). Such a force simultaneously colors the center and every remaining white vertex in that blade, after which the preceding center-black analysis applies.

When \(\ell<m\), no full blade can ever be resolved, so every \(w_i\le\ell\) is necessary. A first force exists exactly when at least one \(w_j\le\ell-1\). These conditions are also sufficient: that blade colors the center, and then every other blade has at most \(\ell\) whites and clears itself.

When \(\ell\ge m\), every nonfull blade can initiate, because \(w_i+1\le m\le\ell\). Thus the only additional requirement beyond \(f\le\lfloor\ell/m\rfloor\) is that at least one blade be nonfull, equivalently that at least one peripheral vertex be initially black. This proves the classification.

For \(\ell<m\), a blade with \(j\) white vertices contributes \(\binom mj x^{m-j}\), so the allowed blade polynomial is \(A_{m,\ell}(x)\). If the center is black, the contribution is \(xA_{m,\ell}(x)^r\). If the center is white, the same blade choices are allowed except the stalled case in which every blade has exactly \(\ell\) white vertices. Subtracting that case gives \(A_{m,\ell}(x)^r-\binom m\ell^r x^{r(m-\ell)}\), yielding the first polynomial formula.

For \(m\le\ell<rm\), any nonfull blade contributes \(B_m(x)=(1+x)^m-1\). If exactly \(f\) blades are full white, there are \(\binom rf\) choices for them and \(B_m(x)^{r-f}\) choices on the remaining blades. Since \(f\le\lfloor\ell/m\rfloor<r\), at least one nonfull blade is automatic; multiplying by \(1+x\) accounts for the two center states. At \(\ell=rm\), every nonempty set is \(\ell\)-forcing, giving \((1+x)^{rm+1}-1\).

The minimum-size formulas follow by taking the least exponent with nonzero coefficient. For \(\ell<m\), the center-black minimum leaves exactly \(\ell\) whites in every blade, while the center-white minimum leaves exactly \(\ell-1\) whites in one blade and exactly \(\ell\) in all others; both have size \(r(m-\ell)+1\). For \(m\le\ell<m(r-1)\), with \(s=\lfloor\ell/m\rfloor\), a minimum set leaves exactly \(s\) blades fully white and chooses exactly one black vertex in every other blade, giving size \(r-s\). Once \(\ell\ge m(r-1)\), any single peripheral vertex forces the graph; the center alone also works exactly at \(\ell=rm\). The counting formulas follow from these descriptions.

## Verification
A standalone exhaustive checker accompanies this result. It independently simulates the \(\ell\)-forcing process and compares it with the structural criterion, polynomial coefficients, minimum size, and minimum-set count for every parameter triple \(2\le r\le4\), \(2\le m\le4\), and \(1\le\ell\le rm\). The replayed package reports:

`VERIFY_OK parameter_pairs=81 subset_checks=2312832 polynomial_checks=81 minimum_checks=81 max_order=17`

The finite computation is a consistency check, not a substitute for the proof for arbitrary \(r,m,\ell\).

## Relationship to prior work
Amos, Caro, Davila, and Pepper introduced the \(k\)-forcing number in the form used here and proved general bounds and several special-family results. Their first public arXiv version is dated 23 January 2014. The searchable full text was inspected for the aliases “windmill,” “friendship,” “Dutch,” “cone,” and “clique”; none occurs as a same-object theorem. Their results include general bounds and the complete-graph formula, but do not imply the blade-by-blade classification above.

Row's cut-vertex method is relevant to the \(\ell=1\) specialization and can cover scalar zero-forcing information for cut-vertex constructions. That does not provide the all-\(\ell\), all-set characterization or cardinality enumerator proved here. A later propagation-number paper studies the least forcing threshold for singleton starts in several graph operations, including joins; that parameter can overlap the singleton threshold of the present theorem but is strictly weaker than the complete forcing-set profile.

A semantic search of published-result records found as the closest forcing result an exact classification for complete multipartite graphs. Generalized windmills \(K_1\vee rK_m\) with \(m\ge2\) and \(r\ge2\) are not complete multipartite graphs: each blade is a clique and different blades are anticomplete. Therefore that result does not imply the present one. The closest same-family published record concerns the general-position polynomial of generalized windmills, a different invariant.

## Limitations
The proof is specific to equal-sized clique blades sharing one universal articulation vertex. Unequal blade sizes require a weighted full-blade condition and are not claimed here. The result does not address connected, total, positive-semidefinite, or oriented variants of forcing. Literature search cannot rule out poorly indexed or unpublished equivalent results. The 2012 cut-vertex paper and the 2026 propagation-number paper were available only at abstract/metadata level during this review, so no claim is made that their inaccessible full texts contain no related special-case statement.

## References
1. D. Amos, Y. Caro, R. Davila, R. Pepper, “Upper bounds on the \(k\)-forcing number of a graph,” arXiv:1401.6206v1 (23 January 2014); Discrete Applied Mathematics 181 (2015), 1–10, DOI: 10.1016/j.dam.2014.08.029.
2. D. D. Row, “A technique for computing the zero forcing number of a graph with a cut-vertex,” Linear Algebra and its Applications 436 (2012), 4423–4432, DOI: 10.1016/j.laa.2011.05.012.
3. V. L. Banot, M. Baldado Jr., “On the propagation number of some graphs,” Far East Journal of Mathematical Sciences 143(2) (2026), 467–488, DOI: 10.17654/0972087126027.
