# Sharp ladder bounds for rectangular clauses with sparse fibers

## Finding
Let \(X,Y\) be arbitrary sets. Suppose a binary relation has a decomposition
\[
R=F\cup\bigcup_{h=1}^{r}(A_h\times B_h),
\qquad \sup_{x\in X}|F_x|\le s,
\]
where \(r,s\) are nonnegative integers and \(F_x=\{y\in Y:(x,y)\in F\}\). Write \(\ell(R)\) for the supremum of the heights of half-graphs in \(R\), with a half-graph of height \(t\) consisting of distinct elements \(x_0,\ldots,x_{t-1}\) and \(y_0,\ldots,y_{t-1}\) such that \(R(x_i,y_j)\) holds exactly when \(i\le j\).

Then
\[
\boxed{\ell(R)\le (r+1)(s+1)-1.}
\]
The bound is sharp simultaneously for every \(r,s\), even among stable quantifier-free semilinear relations on \(\mathbb R^2\) for which the exceptional relation \(F\) is the union of \(s\) graphs of affine maps. Equivalently, the least number of complete bipartite rectangles needed to cover the height-\(t\) half-graph while leaving at most \(s\) uncovered neighbors per left vertex is
\[
\boxed{\left\lfloor\frac{t}{s+1}\right\rfloor.}
\]

**Extremal rigidity.** If a relation attains height \(t=(r+1)(s+1)-1>0\) in such a decomposition, every representation using at most \(r\) rectangles has precisely \(r\) nonempty rectangles on the selected half-graph. Each of them determines a canonical cut, and these cuts, in increasing order, are forced to be exactly \(c_k=k(s+1)-1\) for \(1\le k\le r\). In fact, the maximum selected row index and minimum selected column index of the \(k\)-th rectangle both equal \(c_k\). For \(r=0\), the assertion about rectangles is vacuous.

## Assumptions and scope
No definability, cardinality, or order assumptions on \(X\) or \(Y\) are required for the upper bound and rigidity statement. Rectangles may overlap and may initially be empty. Fibers of \(F\) are uniformly bounded in cardinality by \(s\); no bound on right fibers is used. The ladder convention includes the diagonal: the selected incidence matrix has entries \(1\) exactly at positions \(i\le j\). The maximum is finite by the upper bound, except that an empty class contains no positive-height witness, for which we adopt height zero.

The sharpness construction below uses parameters and ordinary nonstrict linear inequalities, hence is semilinear in the language of ordered vector spaces over \(\mathbb R\). It does not assert a quantitative bound for every stable semilinear relation in terms of its original formula length.

## Proof
**1. Every rectangle on a half-graph is dominated by one cut.** Restrict a putative height-\(t\) witness to its \(t\) selected rows and columns. For a nonempty rectangular component set \(I=\{i:x_i\in A_h\}\) and \(J=\{j:y_j\in B_h\}\), both nonempty. Because the rectangle is contained in \(R\) and the witness has no edges at \(i>j\), we have \(a=\max I\le b=\min J\). Choose any integer \(c\) with \(a\le c\le b\). Every selected edge of this rectangle lies in the canonical cut rectangle
\[
C_c=\{(i,j):0\le i\le c\le j<t\}.
\]
Ignore components that have no selected cells. The selected edges of all rectangular components are thus covered by \(k\le r\) canonical cut rectangles, with repeated cuts discarded.

**2. Gap obstruction.** Sort the distinct cuts \(c_1<\cdots<c_k\). The indices \(0,\ldots,t-1\) not used as cuts form \(k+1\) consecutive gaps (possibly empty) with lengths \(g_0,\ldots,g_k\) and
\[
\sum_{h=0}^k g_h=t-k.
\]
For any nonempty gap, let \(i\) be its first index. The \(g_h\) selected columns indexed by that gap all satisfy \(j\ge i\). They are edges of the half-graph, yet no canonical cut lies in \([i,j]\). Consequently they belong to no selected rectangular component and all lie in \(F_{x_i}\). Hence each \(g_h\le s\). Summing yields
\[
t-k\le (k+1)s,
\qquad t\le k+(k+1)s\le r+(r+1)s.
\]
This proves the universal bound, without assuming distinctness of the rectangles before selecting cuts.

**3. Sharp semilinear construction.** Fix \(r,s\ge0\), put \(t=(r+1)(s+1)-1\), and set \(c_k=k(s+1)-1\) for \(1\le k\le r\). On \(\mathbb R\times\mathbb R\), define
\[
R_{r,s}(x,y)\ \quad\Longleftrightarrow
\bigvee_{k=1}^r(x\le c_k\ \wedge\ y\ge c_k)
\quad\vee\quad
\bigvee_{h=0}^{s-1}(y=x+h).
\]
An empty disjunction is false. The first terms are \(r\) rectangles; the second are \(s\) affine graphs with at most \(s\) points in every left fiber. Select \(x_i=y_i=i\) for \(0\le i<t\). If \(i>j\), no clause is true. If \(i\le j\) and some cut \(c_k\) lies in \([i,j]\), a rectangle makes the pair true. Otherwise \(i,j\) belong to the same cut-free gap of at most \(s\) indices, so \(0\le j-i\le s-1\) and an affine-graph clause makes the pair true. Thus the selected incidence matrix is exactly the height-\(t\) half-graph. Every component is stable, directly because a rectangle has no half-graph of height two and an \(s\)-left-sparse relation has no half-graph of height \(s+1\); the established bound also gives stability of their finite union. The construction is semilinear.

**4. Exact covering budget.** For a given \(t\ge0\) and permitted residual degree \(s\), the upper-bound argument rearranges to \(r\ge\lfloor t/(s+1)\rfloor\). Conversely select every \((s+1)\)-st index as a cut, beginning at \(s\), provided it is smaller than \(t\). There are precisely \(\lfloor t/(s+1)\rfloor\) such cuts, and every cut-free gap has length at most \(s\). Cover by the corresponding canonical rectangles and assign every remaining edge to the residual relation. Its left degree is at most \(s\), proving equality.

**5. Rigidity at equality.** Suppose \(t=r+(r+1)s>0\). In Step 2, strict monotonicity of \(k+(k+1)s\) forces \(k=r\) and every one of the \(r+1\) gaps to have length \(s\). This uniquely fixes the cuts at \(c_k=k(s+1)-1\). Because *any* choice of a cut between \(a=\max I\) and \(b=\min J\) of each nonempty selected rectangle is valid, and every such choice must yield the unique optimal cut set, we must have \(a=b=c_k\) for each rectangle, after relabeling. Empty rectangles or duplicate cuts would yield fewer than \(r\) cuts, contradicting equality. This proves rigidity.

## Verification
Execute `python3 checker.py` with Python 3 and no external dependencies. The checker independently enumerates the canonical cut-cover problem for \(108\) small parameter cases, compares it with arbitrary rectangular covers in \(12\) small cases, verifies forced extremal cut locations in \(13\) cases, and checks \(2600\) incidence-matrix cells from explicit sharpness constructions. Expected terminal output:

```text
ALL_CHECKS_OK canonical_cases=108 arbitrary_cases=12 rigidity_cases=13 witness_cells=2600
```

Finite checking is independent corroboration, not proof for unbounded parameters. The proof is Steps 1–5 and does not rely on software, finite enumeration, or an external mathematical certificate.

## Relationship to prior work
Girón, *On stable semilinear sets in ordered vector spaces* (2026), Theorem 4.8, characterizes stable semilinear relations as finite unions of special stable sets. Hoffmann, Tran, and Ye, *Stable formulas in ordered structures*, establish earlier qualitative decomposition and closure principles. Both explain why rectangles and affine graphs are natural stable building blocks; neither inspected theorem provides the quantitative sharp joint clause-budget/left-degree tradeoff or its equality rigidity. Pinto, *Biclique Covers and Partitions* (2014), investigates biclique cover and local cover parameters but not the mixed half-graph exact tradeoff; its basic biclique-cover viewpoint encompasses the degenerate case \(s=0\). The novelty assertion concerns the mixed budget for positive parameters and its rigidity, not the individual elementary endpoint bounds.

## Limitations
The bound depends on having a representation with \(r\) genuine rectangles and a uniformly \(s\)-left-sparse remainder. General special stable sets need not have that form with controlled \(r,s\). In particular the theorem is not an algorithm to extract these budgets from arbitrary semilinear formulas. The exact ladder bound is a finite combinatorial statement, not an independence or publication-priority certificate. Although published related sources were examined for statement-level implication, equivalent older results concerning mixed covers of Ferrers matrices or row-sparse residuals could exist; independent expert review has not been performed.

## References
1. M. Girón, *On stable semilinear sets in ordered vector spaces*, arXiv:2610.26335, first posted 19 October 2026, https://arxiv.org/abs/2610.26335.
2. D. M. Hoffmann, C.-M. Tran, J. Ye, *Stable formulas in ordered structures*, arXiv:2004.10953, https://arxiv.org/abs/2004.10953.
3. T. Pinto, *Biclique Covers and Partitions*, Electronic Journal of Combinatorics 21(1), #P1.19 (2014), https://doi.org/10.37236/3595.
