# Exact weight-three 2-cover-free families

## Result

Let \(F_3(v)\) be the maximum size of a family \(\mathcal F\subseteq { [v]\choose 3}\) such that no member of \(\mathcal F\) is contained in the union of two other distinct members. Equivalently, \(F_3(v)\) is the maximum number of columns in a binary 2-disjunct matrix with \(v\) rows when every column has weight exactly \(3\).

Then
\[
F_3(3)=1,\qquad F_3(4)=2,\qquad F_3(5)=3,
\]
and for every \(v\ge 6\),
\[
\boxed{F_3(v)=D(v,3,2),}
\]
where \(D(v,3,2)\) is the maximum size of a \(2\)-\((v,3,1)\) packing (a partial Steiner triple system). Consequently,
\[
F_3(v)=
\begin{cases}
\dfrac{v(v-1)}6,&v\equiv1,3\pmod6,\\[4pt]
\dfrac{v(v-2)}6,&v\equiv0,2\pmod6,\\[4pt]
\dfrac{v^2-2v-2}6,&v\equiv4\pmod6,\\[4pt]
\dfrac{v^2-v-8}6,&v\equiv5\pmod6,
\end{cases}
\qquad (v\ge6).
\]

There is also an extremal-structure statement:

> For every \(v\ge7\), every maximum 3-uniform 2-cover-free family is linear: no pair of points occurs in two blocks. Hence the maximum families are exactly the maximum \(2\)-\((v,3,1)\) packings.

The threshold \(v\ge7\) is sharp. On six points the four triples
\[
\{1,2,3\},\{1,2,4\},\{1,2,5\},\{1,2,6\}
\]
form a maximum 2-cover-free family but are not linear.

## Context

Erdős, Frankl and Füredi introduced the uniform extremal problem in 1982. For \(k=3\), their general theorem gives
\[
F_3(v)\le \frac{\binom v2}{3},
\]
with equality precisely when a Steiner triple system exists; they stated only the asymptotic consequence \(F_3(v)=v^2/6+O(v)\) in general. The exact maximum \(D(v,3,2)\) of partial Steiner triple systems is classical and was determined by Schönheim; a modern explicit table appears in Bailey and Burgess.

The design-to-CFF direction is standard: a \(2\)-\((v,k,1)\) packing with \(k\ge3\) yields a 2-cover-free family. A 2026 survey of cover-free families explicitly records this construction. The point here is the reverse extremal mechanism at weight three: repeated pairs force degree-one leaves so strongly that, from \(v=6\) onward, allowing non-linear triple systems cannot improve on the packing number; from \(v=7\) onward it cannot even occur in an extremal family.

## Proof

Call a family *linear* if any two of its triples meet in at most one point.

### Lemma 1: repeated-pair deletion

Suppose a pair \(\{x,y\}\) is contained in \(s\ge2\) members
\[
\{x,y,z_1\},\ldots,\{x,y,z_s\}
\]
of a 3-uniform 2-cover-free family \(\mathcal F\). Then every \(z_i\) has degree exactly one in \(\mathcal F\).

Indeed, if \(z_i\) belonged to another block \(C\ne\{x,y,z_i\}\), choose \(j\ne i\). Then
\[
\{x,y,z_i\}\subseteq \{x,y,z_j\}\cup C,
\]
contradicting 2-cover-freeness.

Therefore deleting the \(s\) points \(z_1,\ldots,z_s\) deletes exactly these \(s\) blocks and leaves a 3-uniform 2-cover-free family on \(v-s\) points. Thus every non-linear family with such a repeated pair satisfies
\[
|\mathcal F|\le s+F_3(v-s). \tag{1}
\]

### Lemma 2: linear families are precisely packing candidates

If \(\mathcal F\) is linear, it is a \(2\)-\((v,3,1)\) packing, so
\[
|\mathcal F|\le D(v,3,2).
\]

Conversely, every \(2\)-\((v,3,1)\) packing is 2-cover-free. If distinct triples \(A,B,C\) satisfied \(A\subseteq B\cup C\), then linearity gives
\[
|A\cap B|\le1,\qquad |A\cap C|\le1,
\]
so \(B\cup C\) could cover at most two points of the three-point set \(A\), a contradiction. Hence
\[
F_3(v)\ge D(v,3,2). \tag{2}
\]

### Small cases

For \(v=3\), clearly \(F_3(3)=1\). For \(v=4\), any two distinct triples have union all four points, so any third triple would be covered; hence \(F_3(4)=2\). For \(v=5\), the three triples \(\{1,2,3\},\{1,2,4\},\{1,2,5\}\) show \(F_3(5)\ge3\). A linear family has at most \(D(5,3,2)=2\), while Lemma 1 bounds a non-linear family by at most \(3\), so \(F_3(5)=3\).

For \(v=6\), a linear family has at most \(D(6,3,2)=4\). In the non-linear case, (1) with \(s=2,3,4\) gives respectively
\[
2+F_3(4)=4,\qquad 3+F_3(3)=4,\qquad 4+F_3(2)=4.
\]
A \(2\)-\((6,3,1)\) packing with four blocks exists, so \(F_3(6)=4=D(6,3,2)\).

### Induction for \(v\ge7\)

Use the classical exact packing formula displayed above. A direct check of its six residue classes gives, for every \(t\ge6\),
\[
D(t+1,3,2)\ge D(t,3,2)+1,\qquad
D(t+2,3,2)\ge D(t,3,2)+3. \tag{3}
\]

Assume the theorem for all smaller orders and let \(\mathcal F\) be a non-linear family on \(v\ge7\) points. Choose a repeated pair of codegree \(s\ge2\), and set \(m=v-s\). Necessarily \(m\ge2\).

If \(m\le5\), the small values above give \(F_3(m)\le m-2\), so (1) yields
\[
|\mathcal F|\le s+m-2=v-2.
\]
The exact packing formula gives \(D(v,3,2)>v-2\) for every \(v\ge7\).

If \(m\ge6\), induction and (1) give
\[
|\mathcal F|\le s+D(m,3,2).
\]
Because \(s\ge2\), (3) implies
\[
D(m+s,3,2)\ge D(m,3,2)+3+(s-2)
>D(m,3,2)+s.
\]
Hence every non-linear family has size strictly below \(D(v,3,2)\). Together with (2), this proves
\[
F_3(v)=D(v,3,2)
\]
and also proves that every extremal family is linear for \(v\ge7\).

## Consequences

The 1982 upper bound \(\lfloor v(v-1)/6\rfloor\) is therefore sharpened to the exact answer in every residue class. In particular, the deficit from that simple pair-count upper bound is not an artifact of restricting to packings: for \(v\ge6\), non-linear 3-uniform 2-cover-free families cannot recover the missing blocks.

In group-testing language, the exact maximum number of items represented by constant-column-weight-three binary 2-disjunct matrices with \(v\) tests is the table above. For \(v\ge7\), every optimal such matrix has the property that every pair of rows occurs together in at most one column.

## Verification

An exact integer-programming check independently optimizes the defining 2-cover-free constraints for \(3\le v\le9\). It returns
\[
1,2,3,4,7,8,12
\]
for \(v=3,4,5,6,7,8,9\), respectively, matching the theorem. The script and its output are included in `artifacts/`.

The computation is only a finite sanity check; the theorem for all \(v\) is proved above.

## Limitations and originality

The result is specific to 3-uniform families and two covering blocks. The repeated-pair deletion lemma uses both features essentially and does not by itself extend to higher uniformity or larger disjunctness.

Originality is claimed only to the best of our knowledge. The 1982 Erdős--Frankl--Füredi paper was checked directly and gives the general upper bound plus the asymptotic \(k=3\) statement, not the exact all-\(v\) formula above. The 2026 Idalino--Moura paper explicitly records the packing-to-2-CFF construction but not the converse extremal theorem. Searches also checked later CFF/superimposed-code terminology and recent sparse-disjunct-matrix work. The full text of Li--van Rees--Wei (2006) and Yu--Wang--Ji (2025) was not fully inspected; their accessible abstracts indicate different emphases, but they remain the most relevant residual sources that could contain an equivalent special-case statement. Because the argument is short and uses classical ingredients, unlocated prior appearance under extremal-set, superimposed-code, or packing terminology remains a substantive residual risk.

## References

1. P. Erdős, P. Frankl, Z. Füredi, *Families of Finite Sets in Which No Set Is Covered by the Union of Two Others*, Journal of Combinatorial Theory, Series A 33 (1982), 158--166. https://doi.org/10.1016/0097-3165(82)90004-8
2. J. Schönheim, *On maximal systems of k-tuples*, Studia Scientiarum Mathematicarum Hungarica 1 (1966), 363--368.
3. R. F. Bailey, A. C. Burgess, *Generalized packing designs*, Discrete Mathematics 313 (2013), 1167--1190. https://doi.org/10.1016/j.disc.2011.11.039
4. P. C. Li, G. H. J. van Rees, R. Wei, *Constructions of 2-cover-free families and related separating hash families*, Journal of Combinatorial Designs 14 (2006), 423--440. https://doi.org/10.1002/jcd.20109
5. T. B. Idalino, L. Moura, *Cover-free families on hypergraphs and combinatorial group testing*, Journal of Combinatorial Optimization 51 (2026), article 55. https://doi.org/10.1007/s10878-026-01429-0
6. L. Yu, X. Wang, L. Ji, *Constructions of Optimal Sparse r-Disjunct Matrices via Packings*, Journal of Combinatorial Designs 33 (2025), 287--299. https://doi.org/10.1002/jcd.21986
