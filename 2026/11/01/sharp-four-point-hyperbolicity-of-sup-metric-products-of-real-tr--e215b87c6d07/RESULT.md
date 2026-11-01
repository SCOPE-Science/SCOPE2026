# Sharp four-point hyperbolicity of sup-metric products of real trees

## Finding

**Theorem.** Let \(k\ge2\) be finite and let \(T_1,\ldots,T_k\) be nonempty real trees, possibly unbounded or singleton. Let \(D_1\ge D_2\ge\cdots\ge D_k\) be their diameters, ordered in \([0,\infty]\), and put
\[
X=\prod_{i=1}^k T_i,\qquad d_\infty(x,y)=\max_{1\le i\le k}d_{T_i}(x_i,y_i).
\]
For the **four-point** hyperbolicity constant (defined below),
\[
\boxed{\delta_4(X,d_\infty)=\frac{D_2}{2},}
\]
where infinite diameter gives infinite constant. In particular, the product is four-point Gromov hyperbolic if and only if at most one factor is unbounded. Neither the number of factors beyond two nor their branching changes the sharp constant once the two largest diameters are fixed.

**General upper-bound lemma.** If \((T,d_T)\) has four-point constant zero and \((Y,d_Y)\) is any metric space with finite diameter \(D\), then
\[
\delta_4(T\times Y,\max\{d_T,d_Y\})\le D/2.
\]
The theorem is sharp because two nontrivial real-tree factors contain suitably long geodesic segments.

## Assumptions and scope

For any metric space \((M,d)\) and any four (not necessarily distinct) points \(x_1,x_2,x_3,x_4\), let
\[
S_1=d(x_1,x_2)+d(x_3,x_4),\quad S_2=d(x_1,x_3)+d(x_2,x_4),\quad S_3=d(x_1,x_4)+d(x_2,x_3).
\]
Arrange them in descending order \(S_{(1)}\ge S_{(2)}\ge S_{(3)}\), and define \(\delta_4(M)=\frac12\sup(S_{(1)}-S_{(2)})\). This normalization is the standard four-point normalization. It is **not** a claim about an equal numerical value for the Rips thin-geodesic-triangle constant. A real tree is geodesic and has \(\delta_4=0\). The product metric here is the coordinatewise maximum, **not** the shortest-path metric of a Cartesian graph product and **not** the sum (\(\ell_1\)) metric.

The diameter is a supremum: neither compactness nor existence of diametral endpoints is assumed. The number of factors is finite. Singleton factors have diameter zero. When at least two factors are unbounded, \(D_2=\infty\) and both sides of the theorem are interpreted as infinite.

## Proof

**1. Four-point upper bound for a zero-hyperbolic factor and one bounded factor.** Fix arbitrary four points \((t_i,y_i)\in T\times Y\), indexed by \(i=1,2,3,4\), and set \(a_{ij}=d_T(t_i,t_j)\), \(b_{ij}=d_Y(y_i,y_j)\), and \(c_{ij}=\max(a_{ij},b_{ij})\). Then \(0\le b_{ij}\le D\), \(a_{ij}\le c_{ij}\le\max(a_{ij},D)\). Since \(T\) is zero-hyperbolic, among the three sums of pairs of \(a_{ij}\), the largest two are equal. Call their common value \(A\); the remaining sum is at most \(A\).

Suppose first that \(A>D\). Consider any of the three pairings and write the two \(a\)-distances in it as \(u,v\), so \(u+v\le A\). If both \(u,v<D\), the corresponding \(c\)-sum is at most \(2D\le A+D\). Otherwise at least one is at least \(D\), so
\[
\max(u,D)+\max(v,D)\le u+v+D\le A+D.
\]
Thus **every** pairing sum for \(c\) is at most \(A+D\). On the other hand, each of the two maximal pairings for \(a\) has \(c\)-sum at least \(A\). Hence the second-largest \(c\)-pairing sum is at least \(A\). The largest minus second-largest is therefore at most \(D\).

Suppose instead that \(A\le D\). Every \(a_{ij}\) lies in a pairing whose sum is at most \(A\), hence \(a_{ij}\le D\). Therefore all six \(c_{ij}\le D\). Let \(S_{(1)}\ge S_{(2)}\ge S_{(3)}\) be the three sums for \(c\). The triangle inequalities yield \(S_{(1)}\le S_{(2)}+S_{(3)}\) (if the largest is \(c_{12}+c_{34}\), combine \(c_{12}\le c_{13}+c_{23}\) and \(c_{34}\le c_{14}+c_{24}\), and similarly under relabeling). Therefore \(S_{(2)}\ge S_{(1)}/2\), while \(S_{(1)}\le2D\). Consequently
\[
S_{(1)}-S_{(2)}\le S_{(1)}/2\le D.
\]
In both cases the four-point defect is at most \(D/2\), establishing the upper-bound lemma. The case \(D=0\) follows directly too.

**2. Apply the bound to the product.** Assume \(D_2<\infty\). Sort the factors so \(T_1\) has diameter \(D_1\), and aggregate the remaining factors into \(Y=\prod_{i=2}^k T_i\) with its maximum metric. Then \(\operatorname{diam}Y=\max_{i\ge2}D_i=D_2\), even when diameters are not attained. The first part applied to \(T_1\times Y\) gives \(\delta_4(X)\le D_2/2\).

**3. Matching lower bound.** If \(0<D_2<\infty\), fix any \(0<L<D_2\). By the supremum definition of diameter and the real-tree geodesic property, both \(T_1\) and \(T_2\) contain isometric copies of the segment \([0,L]\). Fix all remaining factor coordinates. Their product contains an isometric copy of the supremum-metric square \([0,L]^2\). The four compass points
\[
(0,L/2),\qquad(L/2,0),\qquad(L/2,L),\qquad(L,L/2)
\]
have pairing sums \(2L,L,L\): opposite points are distance \(L\) and adjacent points distance \(L/2\). Their defect is \(L/2\). Since \(L\uparrow D_2\) is arbitrary, \(\delta_4(X)\ge D_2/2\). If \(D_2=0\), all factors beyond the first are singletons and the product is a real tree, hence \(\delta_4=0\). If \(D_2=\infty\), the same square construction works for every \(L>0\), forcing \(\delta_4=\infty\). This completes the proof.

**4. Sharp consequence.** In particular, \(k\) unit segments with the maximum product metric have \(\delta_4=1/2\) for every \(k\ge2\). By contrast, the cited \(\ell_1\)-product partition formula yields \(\lfloor k/2\rfloor\) for the same family under the *different* sum metric.

## Verification

The independent-of-proof, standard-library-only program `verify.py` enumerates every four-point configuration from nine finite test spaces: six half-unit- or unit-spaced products of intervals, and three products of branching metric stars. It performs all comparisons as exact rational arithmetic and checks the proposed values in every case. A direct execution of the included program completed successfully with 14,680,587 exhaustive finite-quartet comparisons. These are finite consistency checks, not a proof over arbitrary real trees; the argument above supplies that proof, including unbounded cases.

## Relationship to prior work

Michel, Soria-Lorente and Vilaire [1], publicly posted October 16, 2026, treat the shortest-path geometry of Cartesian graph products and the **sum-metric** products of zero-hyperbolic metric spaces. Their \(\ell_1\) four-point formula involves optimal bipartitions of the factor diameters and grows with dimension for equal-length factors. Their stated results do not yield the present **maximum-metric** formula: changing from a sum metric to a maximum metric alters every pairwise distance and the four-point sums, and the two formulas disagree already for three equal unit segments. The same article supplies the relevant common four-point normalization. Searches also considered published four-point studies of polygonal chord metrics and work on other sup-product metric invariants; those address different underlying spaces or different invariants. The elementary pairwise-truncation argument, rather than a renaming of the \(\ell_1\) formula, gives the present result.

## Limitations

This theorem identifies the exact **four-point** constant, not automatically the exact geodesic-triangle thinness constant. The result is restricted to finite products of real trees equipped with the supremum metric; it does not assert the same equality for arbitrary hyperbolic factors, arbitrary normed product metrics or infinite products. The verification program checks finite test examples only. Searches of accessible indexed records and the cited primary paper did not reveal an equivalent previously published formula, but unindexed or inaccessible earlier literature could affect historical priority; no independent scientific audit has been performed.

## References

1. J. Michel, A. Soria-Lorente and J.-M. Vilaire, *Sharp Gromov Hyperbolicity Constants for Cartesian Products of Finitely Many Trees*, arXiv:2610.24253v1, publicly submitted 2026-10-16, https://arxiv.org/html/2610.24253v1 (especially §§2, 5, 7–8).
2. Mathematical Reviews and zbMATH, *Mathematics Subject Classification MSC2020*, https://mathscinet.ams.org/msnhtml/msc2020.pdf (51F30, Lipschitz and coarse geometry of metric spaces).
