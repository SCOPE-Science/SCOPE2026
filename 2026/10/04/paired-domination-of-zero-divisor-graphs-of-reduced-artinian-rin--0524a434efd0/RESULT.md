# Paired domination of zero-divisor graphs of reduced Artinian rings

## Finding

Let \(R\) be a reduced commutative Artinian ring that is not a domain, and write \(r=|\operatorname{Min}(R)|\ge2\). For the standard zero-divisor graph \(\Gamma(R)\), whose vertices are the nonzero zero-divisors and whose distinct vertices are adjacent exactly when their product is zero, the paired-domination number is \[\gamma_{\mathrm{pr}}(\Gamma(R))=2\left\lceil\frac r2\right\rceil.\] Equivalently, if \(R\cong\prod_{i=1}^r F_i\) is its product decomposition into fields, then \(\gamma_{\mathrm{pr}}=r\) for even \(r\) and \(\gamma_{\mathrm{pr}}=r+1\) for odd \(r\).

This gives a complete paired-domination classification for reduced Artinian non-domains. The formula depends only on the number of minimal prime ideals, not on the cardinalities of the residue fields.

## Assumptions and scope

Let \(R\) be a reduced commutative Artinian ring with identity and suppose that \(R\) is not a domain. The Artinian reduced decomposition gives
\[
R\cong F_1\times\cdots\times F_r,
\]
where the \(F_i\) are fields and \(r=|\operatorname{Min}(R)|\ge2\).

The zero-divisor graph \(\Gamma(R)\) has as vertices the nonzero zero-divisors of \(R\). Distinct vertices \(x,y\) are adjacent exactly when \(xy=0\). A paired dominating set is a dominating set \(D\) such that the induced graph \(\Gamma(R)[D]\) has a perfect matching.

For \(x=(x_1,\ldots,x_r)\), define its support by
\[
\operatorname{supp}(x)=\{i:x_i\ne0\}.
\]
Because each factor is a field, the vertices of \(\Gamma(R)\) are exactly the elements with nonempty proper support, and
\[
x\sim y
\quad\Longleftrightarrow\quad
\operatorname{supp}(x)\cap\operatorname{supp}(y)=\varnothing.
\]

## Proof

For each nonempty proper subset \(S\subsetneq[r]\), let \(V_S\) be the set of graph vertices with support exactly \(S\).

First assume \(r\ge3\). For each \(i\in[r]\), choose a vertex \(y_i\in V_{[r]\setminus\{i\}}\). Let \(D\) be any dominating set. If \(y_i\in D\), then \(D\) meets \(V_{[r]\setminus\{i\}}\). If \(y_i\notin D\), then some member of \(D\) must be adjacent to \(y_i\), and its support must therefore be the singleton \(\{i\}\). Hence, for every \(i\),
\[
D\cap\left(V_{\{i\}}\cup V_{[r]\setminus\{i\}}\right)\ne\varnothing.
\]
For \(r\ge3\), these \(r\) unions are pairwise disjoint. Therefore every dominating set has at least \(r\) vertices. A paired dominating set has even cardinality, so
\[
\gamma_{\mathrm{pr}}(\Gamma(R))\ge 2\left\lceil\frac r2\right\rceil.
\]
For \(r=2\), every paired dominating set has at least two vertices, which is the same lower bound.

For the upper bound, choose for each \(i\) an element \(e_i\in R\) supported exactly on \(\{i\}\). The vertices
\[
e_1,\ldots,e_r
\]
form a clique because distinct singleton supports are disjoint. They dominate the whole graph: every nonempty proper support omits at least one index \(i\), and the corresponding \(e_i\) is adjacent to that vertex.

If \(r\) is even, the clique \(\{e_1,\ldots,e_r\}\) has a perfect matching, so it is a paired dominating set of size \(r\).

If \(r\ge3\) is odd, choose a vertex \(b\) supported on \(\{1,2\}\). Then
\[
\{e_1,\ldots,e_r,b\}
\]
is still dominating and has size \(r+1\). It has a perfect matching: pair \(b\) with \(e_3\), pair \(e_1\) with \(e_2\), and pair the remaining \(e_i\)'s arbitrarily. Thus the upper bound equals the lower bound.

When \(r=2\), \(e_1\) and \(e_2\) are adjacent and dominate every vertex, so the paired-domination number is \(2\).

Combining the cases proves
\[
\gamma_{\mathrm{pr}}(\Gamma(R))=2\left\lceil\frac r2\right\rceil.
\]

## Verification

The proof is symbolic. The accompanying `verify.py` independently constructs the actual direct products of small prime fields, enumerates their nonzero zero-divisors, builds adjacency from coordinatewise multiplication, and searches exactly for minimum paired dominating sets by testing domination together with perfect matchings.

The exact output is:

```text
VERIFY_OK
F2xF2 vertices=2 paired=2
F2xF3 vertices=3 paired=2
F3xF3 vertices=4 paired=2
F2xF2xF2 vertices=6 paired=4
F2xF2xF3 vertices=9 paired=4
F2xF3xF3 vertices=13 paired=4
F3xF3xF3 vertices=18 paired=4
F2xF2xF2xF2 vertices=14 paired=4
F2xF2xF2xF2xF2 vertices=30 paired=6
```

The tested rings include products with two through five field factors and mixed factor sizes. The largest checked graph has \(30\) vertices. These computations corroborate the theorem but are not used to prove the general statement.

## Relationship to prior work

Haynes and Slater introduced paired domination for general graphs in 1998. Jafari Rad, Jafari, and Mojdeh studied domination in zero-divisor graphs and, for commutative Artinian rings, calculated ordinary domination; for products of two rings they also treated total domination. Their paper defines the same standard zero-divisor graph and explicitly states domination, total domination, and connected domination as its domination parameters, but does not impose the perfect-matching condition of paired domination.

For a reduced Artinian ring, the field-product structure turns adjacency into disjointness of supports. The present result uses that support geometry to add the matching constraint and obtains the exact parity correction. Targeted searches for paired domination of zero-divisor graphs, products of fields, reduced Artinian rings, and minimal-prime formulations did not locate a prior statement of this formula.

## Limitations

The theorem is restricted to reduced commutative Artinian rings. Nilpotent elements in a nonreduced Artinian ring change the support-disjointness model, so the argument does not extend without additional structure.

The result determines the paired-domination number, not the complete family or polynomial of paired dominating sets. It also does not claim that the zero-divisor graph determines the individual field sizes.

A residual literature risk is that an unindexed algebraic-graph paper may have specialized paired domination to the same field-product graphs under different terminology.

## References

1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
2. N. Jafari Rad, S. H. Jafari, and D. A. Mojdeh, “On Domination in Zero-Divisor Graphs,” *Canadian Mathematical Bulletin* 56 (2013), 407–411. DOI: 10.4153/CMB-2011-156-1. Published electronically 3 August 2011.
3. D. F. Anderson and P. S. Livingston, “The Zero-Divisor Graph of a Commutative Ring,” *Journal of Algebra* 217 (1999), 434–447. DOI: 10.1006/jabr.1998.7840.
