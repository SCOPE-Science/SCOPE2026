# Euclidean inball centers and universal facet contacts of partial alternating-sign-matrix polytopes

## Finding

For integers \(m,n\ge2\), let \(\mathcal A_{m,n}\subset\mathbb R^{m\times n}\) be the convex hull of the \(m\)-by-\(n\) partial alternating sign matrices, equipped with the Frobenius (entrywise Euclidean) metric. Put \(L=\max\{m,n\}\) and
\[
\rho=\frac1{L+\sqrt L}.
\]
The exact radius of a largest inscribed Euclidean ball is \(\rho\). The constant matrix with every entry \(\rho\) is an incenter.

The **complete** set \(\mathcal I_{m,n}\) of centers of balls of this radius is the set of real matrices \(C=(c_{ij})\) satisfying
\[
\rho\sqrt j\le\sum_{t=1}^j c_{it}\le1-\rho\sqrt j\quad(1\le i\le m,1\le j\le n),
\]
\[
\rho\sqrt i\le\sum_{s=1}^i c_{sj}\le1-\rho\sqrt i\quad(1\le i\le m,1\le j\le n).
\]
In this description the following equalities are automatic and describe the entire affine hull:

* If \(m<n\), \(c_{1j}=\rho\) for every \(j\); there are no further affine equalities.
* If \(m>n\), \(c_{i1}=\rho\) for every \(i\); there are no further affine equalities.
* If \(m=n\), the first row **and** first column consist entirely of \(\rho\); there are no further affine equalities.

In particular,
\[
\dim\operatorname{aff}\mathcal I_{m,n}=
\begin{cases}
mn-\max\{m,n\},&m\ne n,\\
(n-1)^2,&m=n.
\end{cases}
\]
For \(m,n\ge2\), no largest inscribed ball has a unique center.

There is also an exact facet-contact distinction. If \(m<n\), exactly \(n+1\) facets are tangent to **every** maximum-radius ball: the \(n\) nonnegativity facets \(c_{1j}\ge0\) and the first-row total-sum upper facet. If \(m>n\), the transpose gives exactly \(m+1\) universally tangent facets. If \(m=n\), exactly \(2n+1\) facets are universally tangent: the \(2n-1\) distinct nonnegativity facets in the first row or column and the two corresponding total-sum upper facets. Generic centers in the relative interior of \(\mathcal I_{m,n}\) have no other tangent facets.

At the constant center \(C=\rho\mathbf1\), the number of tangent facets is \(2m+n-1\) when \(m<n\), its transpose when \(m>n\), and \(4n-1\) when \(m=n\). Thus equal-radius balls have different contact patterns within the same polytope.

## Assumptions and scope

A partial alternating sign matrix is an integral \(m\)-by-\(n\) matrix whose every initial row sum and every initial column sum belongs to \(\{0,1\}\). The convex hull is full-dimensional for \(m,n\ge2\). Its exact real halfspace description is the requirement that all those initial sums lie between zero and one (Heuer–Striker, Theorem 4.6); their Theorem 4.8 identifies which of these inequalities are actual facets. Here distance, inball and tangency all refer to the standard unweighted Frobenius metric, **not** the metric of a projection or affine realization. A tangent facet means its supporting hyperplane is at distance equal to the inradius from the selected center.

## Proof

**1. Ball containment as shifted prefix bounds.** A row-prefix functional involving \(j\) entries has Frobenius-normal length \(\sqrt j\); a column-prefix functional involving \(i\) entries has length \(\sqrt i\). A closed radius-\(r\) ball centered at \(C\) lies in the Heuer–Striker halfspace system if and only if its row-prefix values belong to \([r\sqrt j,1-r\sqrt j]\) and its column-prefix values belong to \([r\sqrt i,1-r\sqrt i]\). Since the system defines \(\mathcal A_{m,n}\) exactly, this is necessary and sufficient even for inequalities that are redundant as facets.

**2. Sharp bound and attainment.** Assume \(m\le n\), the other case following by transposition. The first row's \(n\) individual entries satisfy \(c_{1j}\ge r\): each is a length-one column prefix. Its full row sum satisfies \(\sum_{j=1}^n c_{1j}\le1-r\sqrt n\). Thus \((n+\sqrt n)r\le1\). Conversely, at \(C=\rho\mathbf1\) every prefix of length \(k\le n\) equals \(k\rho\), which lies between \(\rho\sqrt k\) and \(1-\rho\sqrt k\): use \(k\ge\sqrt k\) and \(k+\sqrt k\le n+\sqrt n\). This proves the radius formula in all dimensions.

**3. All mandatory equalities.** For \(m<n\), equality in the bound from Step 2 forces each of the first-row entries to equal \(\rho\). For \(m=n\), the same argument applied after transposition forces the entire first column to equal \(\rho\) as well. For \(m>n\), only the first column is similarly forced. By Step 1 the shifted prefix inequalities are necessary and sufficient to characterize all such centers.

**4. No hidden affine equations.** It suffices to give a feasible point that makes every shifted prefix inequality *strict* except those forced in Step 3. Suppose \(m<n\), and choose sufficiently small \(\varepsilon>0\). Keep the first row equal to \(\rho\). In every remaining row put \(\rho+\varepsilon\) in column one and \(\rho-2\varepsilon\) in every later column. A row prefix of length \(j\) in a later row becomes \(j\rho+(3-2j)\varepsilon\). At \(j=1\) the lower inequality is strict; at \(j=n\) the upper inequality is strict because \(3-2n<0\); at intermediate lengths both have positive slack for small \(\varepsilon\). Column prefixes of length \(i\ge2\) become \(i\rho+(i-1)\varepsilon\) in column one and \(i\rho-2(i-1)\varepsilon\) in other columns. Since \(i\le m<n\), all such inequalities had strictly positive slack at \(\varepsilon=0\) and remain strict for sufficiently small \(\varepsilon\). The only remaining tight inequalities are those defining the first-row equalities and its total upper bound.

When \(m=n\), keep the first row and first column equal to \(\rho\), and put \(\rho-\varepsilon\) in all entries with both indices at least two. Every later row prefix of length \(j\ge2\) is \(j\rho-(j-1)\varepsilon\), and similarly for columns. All these bounds are strict for small positive \(\varepsilon\): at full length the upper bound becomes strict, and at other lengths there was a positive gap before perturbation. Transpose the rectangular construction for \(m>n\). These strict relative-interior witnesses prove the claimed affine-hull dimensions.

**5. Universally tangent facets.** In the rectangular case, the forced first-row coordinates put the \(n\) individual nonnegativity facets at distance \(\rho\), and their total upper facet at the same distance. In the square case the first-column counterparts contribute another \(n\) individual facets (with one shared at entry \((1,1)\)) and one upper facet. Heuer–Striker's irredundant facet list confirms that these are distinct facets and that every other facet is strict at the witnesses of Step 4. This proves exact universal contact counts and the generic contact statement. At the constant center, the other first-column individual lower facets and all row total upper facets (plus column total upper facets in the square case) are tangent; the remaining proper-prefix inequalities have strictly larger distances. Counting distinct facets proves the final counts.

## Verification

The standalone checker `check_pasm_incenters.py` uses 70-digit decimal arithmetic to test the constructive witnesses, the complete shifted inequalities, and their active labels for all \(1521\) shapes with \(2\le m,n\le40\). It reports \(45682\) active labeled inequalities; a duplicated label at \((1,1)\) corresponds to one geometric facet. The proof above, not this finite check, establishes the universal theorem. The optimal-radius linear-program calculations for low-dimensional shapes provided an additional diagnostic but are not needed by the statement or certificate.

## Relationship to prior work

Heuer and Striker introduced these polytopes and proved the row/column-prefix halfspace description and irredundant facet list (arXiv:2012.09901, first posted 2020-12-17, Theorems 4.6 and 4.8). Their results are the starting point; they do not state an exact Euclidean inradius, characterize its full center locus, or classify universally tangent facets. Heuer, Solhjem and Striker later studied special faces and their order/flow-polytope realizations (arXiv:2403.02204, first posted 2024-03-04), not the full-polytope Frobenius incenter locus. Work on partial-permutation matching polytopes and partial permutohedra concerns different convex bodies, which cannot imply the stated geometry without proving a metric-preserving identification.

## Limitations

The theorem uses the standard Frobenius metric and the full-dimensional polytope with \(m,n\ge2\); it does not address Euclidean geometry of special faces or arbitrary affine projections. The classification determines the exact incenter polytope by inequalities, its affine hull, and its common facet contacts; it does not enumerate all vertices or all individual tangent-facet patterns of that incenter polytope. The literature comparison is limited to the identified primary sources and accessible indexed findings, and cannot exclude an unindexed equivalent theorem. Independent mathematical validation has not been performed.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first posted 2020-12-17), in particular Theorems 4.6 and 4.8. https://arxiv.org/abs/2012.09901
2. D. Heuer, S. Solhjem and J. Striker, *On ν faces of partial alternating sign matrix polytopes*, arXiv:2403.02204 (first posted 2024-03-04), in particular Theorems 3.2 and 4.5. https://arxiv.org/abs/2403.02204
