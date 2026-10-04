# Sharp continuum dimension in snowflaked \(p\)-Banach metrics
## Finding
Let \(0<p<1\) and let \(X\) be a nonzero real or complex \(p\)-Banach space whose continuous dual separates points. Equip \(X\) with the metric \(d_p(x,y)=\|x-y\|_X^p\). Then every nondegenerate connected subset \(K\subset X\) satisfies \(\dim_H(K,d_p)\ge 1/p\), and this bound is attained by every nontrivial affine line segment. Hence the minimum Hausdorff dimension of a nondegenerate connected subset of \((X,d_p)\) is exactly \(1/p\). The point-separation hypothesis is essential: in \(L_p[0,1]\), whose continuous dual does not separate points for \(0<p<1\), the indicator path \(t\mapsto \mathbf 1_{[0,t]}\) is an isometric copy of \([0,1]\) for the metric \(d_p\), so the corresponding minimum is exactly \(1\).

## Assumptions and scope
Fix \(0<p<1\). A \(p\)-Banach space is a complete quasi-normed vector space whose quasi-norm satisfies \(\|x+y\|_X^p\le \|x\|_X^p+\|y\|_X^p\). We use its canonical translation-invariant metric \(d_p(x,y)=\|x-y\|_X^p\). The continuous dual is assumed to separate points in the positive statement. Hausdorff dimension is always computed with respect to \(d_p\).

The statement concerns arbitrary nondegenerate connected subsets, not only curves or compact connected sets. It does not classify all equality cases, and it makes no claim about Assouad, packing, or topological dimension.

## Proof
Let \(K\subset X\) be connected and contain distinct points \(a,b\). Since the continuous dual separates points, there is a continuous linear functional \(x^*\) with \(x^*(a)\ne x^*(b)\). In the complex case, after multiplying by a unimodular scalar and taking the real part, we obtain a continuous real-linear functional \(f:X\to\mathbb R\) with \(f(a)\ne f(b)\). Continuity gives a constant \(C>0\) such that
\[
|f(x)-f(y)|\le C\|x-y\|_X=C\,d_p(x,y)^{1/p}
\]
for all \(x,y\in X\). Thus \(f|_K\) is Hölder with exponent \(1/p\).

Because \(K\) is connected, \(f(K)\subset\mathbb R\) is connected; because it contains the distinct values \(f(a)\) and \(f(b)\), it contains a nondegenerate interval. Hence \(\dim_H f(K)\ge1\).

For completeness, the needed Hölder dimension inequality follows directly from covers. If \(g:E\to Y\) satisfies \(d_Y(g(u),g(v))\le C d_E(u,v)^\beta\), then a cover \(E\subset\bigcup_i U_i\) yields \(\operatorname{diam} g(U_i)\le C(\operatorname{diam}U_i)^\beta\). Therefore, for every \(s>\dim_H E\), the \(s/\beta\)-dimensional Hausdorff content of \(g(E)\) tends to zero with the covering scale, so \(\dim_H g(E)\le \dim_H(E)/\beta\). Applying this with \(\beta=1/p\) gives
\[
1\le \dim_H f(K)\le p\,\dim_H K,
\]
and therefore \(\dim_H K\ge1/p\).

Sharpness is explicit. If \(v\ne0\), the affine segment \(L=\{a+tv:0\le t\le1\}\) satisfies
\[
d_p(a+sv,a+tv)=\|v\|_X^p|s-t|^p.
\]
Thus \(L\) is a constant rescaling of the snowflaked interval \(([0,1],|s-t|^p)\). The same covering definition gives \(\dim_H([0,1],|s-t|^p)=1/p\): replacing every Euclidean diameter \(r\) by \(r^p\) changes an exponent \(q\) in the Hausdorff sum to \(pq\). Hence every nontrivial affine segment has Hausdorff dimension exactly \(1/p\), so the lower bound is attained.

Finally, the dual-separation assumption cannot be removed. In \(L_p[0,1]\), define \(F(t)=\mathbf 1_{[0,t]}\). Then
\[
d_p(F(s),F(t))=\|F(s)-F(t)\|_p^p=|s-t|,
\]
so \(F([0,1])\) is an isometric copy of the ordinary unit interval and has Hausdorff dimension \(1\). Every nondegenerate connected metric space has Hausdorff dimension at least \(1\), since its one-dimensional Hausdorff content is at least its diameter. Thus the minimum there is exactly \(1\).

## Verification
The proof has no finite search or numerical component. The critical steps are: point separation produces a nonconstant scalar functional on each nondegenerate connected set; that functional is exactly \(1/p\)-Hölder for the metric \(d_p\); connected scalar images contain intervals; and Hausdorff dimension contracts under Hölder maps by the reciprocal Hölder exponent. Each step is stated with its quantifiers and the covering argument is included above.

The boundary example is independently checkable from the formula for the \(L_p\) quasi-norm: the indicator path has \(d_p\)-distance exactly \(|s-t|\). No unproved classification of equality cases is used.

## Relationship to prior work
Albiac, Ansorena, and Wald prove that if a \(p\)-Banach space has point separation, every Lipschitz map from an interval into \((X,d_p)\) is constant. Their proof passes to the Banach envelope and uses that a \(1/p\)-Hölder map into a Banach space has exponent greater than one. They also point out that the indicator path in \(L_p[0,1]\) is Lipschitz for \(d_p\), showing the necessity of point separation for their curve theorem.

The present result is a different, quantitative statement about all connected subsets: it identifies the exact minimum Hausdorff dimension \(1/p\), with affine segments as extremizers, and shows a sharp drop to \(1\) in the standard non-point-separating \(L_p\) model. Targeted searches for this connected-set Hausdorff-dimension formulation, its snowflake equivalent, and the exact \(1/p\) threshold found no covering statement. General snowflake and Hölder-dimension literature supplies related background but does not by itself state this \(p\)-Banach continuum invariant.

## Limitations
Point separation by the continuous dual is essential. The theorem gives the minimum Hausdorff dimension but does not classify all connected sets of dimension \(1/p\). It also does not assert analogous sharp minima for packing or Assouad dimension. Because the argument is short and uses standard Hausdorff-dimension facts, an equivalent observation may exist under different metric-geometry terminology even though the targeted searches did not locate one.

## References
1. F. Albiac, J. L. Ansorena, P. Wald, “Differentiability of Lipschitz curves in p-Banach spaces,” arXiv:2609.26992v1, first public 2026-09-22.
2. General background consulted for overlap comparison: “A characterisation of snowflakes via rectifiability” (2026), concerning metric snowflakes and rectifiability rather than the exact connected-subset invariant above.
3. General background consulted for overlap comparison: “Minimising Hausdorff dimension under Hölder equivalence” (2021), concerning Hölder-equivalent metrics rather than the exact \(p\)-Banach connected-set threshold above.
