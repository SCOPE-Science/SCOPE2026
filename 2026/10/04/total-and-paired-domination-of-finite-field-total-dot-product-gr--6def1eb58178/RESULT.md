# Total and paired domination of finite-field total dot product graphs

## Finding

Let \(\mathbb F_q\) be a finite field and let \(n\ge3\). For the total dot product graph \(TD(\mathbb F_q,n)\) on the nonzero vectors of \(\mathbb F_q^n\), with distinct vectors adjacent exactly when their dot product is zero, the total domination number and paired domination number are \[\gamma_t(TD(\mathbb F_q,n))=q+1,\] and \[\gamma_{\mathrm{pr}}(TD(\mathbb F_q,n))=\begin{cases}q+1,&q\text{ odd},\\q+2,&q\text{ even}.\end{cases}\] Thus the paired-domination number is independent of \(n\) for \(n\ge3\), and it differs from total domination exactly in even characteristic.

For comparison with the known ordinary domination number, Mollahajiaghaei proved
\[
\gamma(TD(\mathbb F_q,n))=
\begin{cases}
2,&q=2\text{ and }n=3,\\
q+1,&\text{otherwise},
\end{cases}
\]
for \(n>1\). Hence the exceptional binary three-dimensional graph has the strict chain
\[
\gamma=2<\gamma_t=3<\gamma_{\mathrm{pr}}=4,
\]
while for even \(q>2\) one has \(\gamma=\gamma_t=q+1<\gamma_{\mathrm{pr}}=q+2\), and for odd \(q\) all three values are \(q+1\).

## Assumptions and scope

Let \(V=\mathbb F_q^n\) with the standard nondegenerate bilinear form
\[
B(x,y)=x\cdot y=\sum_{i=1}^n x_i y_i.
\]
The graph \(TD(\mathbb F_q,n)\) has vertex set \(V\setminus\{0\}\), and two distinct vertices are adjacent exactly when \(B(x,y)=0\).

A total dominating set \(D\) requires every vertex, including every member of \(D\), to have a neighbor in \(D\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching; in particular every paired dominating set is total dominating.

The theorem is stated only for \(n\ge3\). Dimension two has additional dependence on the isotropy type of the standard quadratic form and is not claimed here.

## Proof

### The universal lower bound

For a nonzero vector \(d\), write
\[
H_d=d^\perp=\{v\in V:B(v,d)=0\}.
\]
If \(D\) is total dominating, then for every nonzero \(v\in V\) there is some \(d\in D\) with \(v\in H_d\). Since \(0\) lies in every \(H_d\), the hyperplanes \(H_d\), \(d\in D\), cover all of \(V\).

If \(k\le q\) hyperplanes are given, their union has size at most
\[
q^{n-1}+(k-1)(q^{n-1}-1)
\le
q^n-q+1
<q^n.
\]
Indeed, after the first hyperplane, each further one contributes at most \(q^{n-1}-1\) new points because it already contains \(0\). Therefore at least \(q+1\) hyperplanes are needed, and
\[
\gamma_t(TD(\mathbb F_q,n))\ge q+1.
\tag{1}
\]
Since paired domination has even cardinality,
\[
\gamma_{\mathrm{pr}}(TD(\mathbb F_q,n))
\ge
\begin{cases}
q+1,&q\text{ odd},\\
q+2,&q\text{ even}.
\end{cases}
\tag{2}
\]

### Odd characteristic

Assume \(q\) is odd. We first construct a two-dimensional anisotropic subspace \(W\le V\).

If \(-1\) is a nonsquare, take \(W=\langle e_1,e_2\rangle\); then \(x^2+y^2=0\) has no nonzero solution.

If \(-1\) is a square, choose a nonsquare \(a\in\mathbb F_q\). Every element of \(\mathbb F_q\) is a sum of two squares: the set of squares (including zero) and its translate by \(a\) both have size \((q+1)/2\), so they intersect. Choose \(u,v\) with \(u^2+v^2=a\), and set
\[
w=(0,u,v,0,\ldots,0).
\]
Then \(w\perp e_1\), \(B(w,w)=a\), and the form on \(W=\langle e_1,w\rangle\) is \(\operatorname{diag}(1,a)\). Since \(-a\) is a nonsquare, this \(W\) is anisotropic.

Let \(U=W^\perp\). Choose one nonzero representative \(d_L\) from each of the \(q+1\) projective lines \(L\le W\), and put
\[
D=\{d_L:L\in\mathbb P(W)\}.
\]
The hyperplanes \(d_L^\perp\) are exactly the \(q+1\) hyperplanes containing \(U\), so they cover \(V\). Hence \(D\) dominates.

Because \(W\) is anisotropic, the map
\[
L\longmapsto L^\perp\cap W
\]
is a fixed-point-free involution on the \(q+1\) projective lines of \(W\). Pair each \(d_L\) with the representative from its orthogonal line. These are graph edges and form a perfect matching. Thus \(D\) is paired dominating of size \(q+1\). Combined with (1) and (2),
\[
\gamma_t=\gamma_{\mathrm{pr}}=q+1
\qquad(q\text{ odd}).
\]

### Even characteristic: total domination

Assume \(q\) is even. Let
\[
r=e_1+e_2,
\qquad
s=e_3,
\qquad
W=\langle r,s\rangle.
\]
Then \(B(r,r)=B(r,s)=0\) and \(B(s,s)=1\), so the radical of the restricted form on \(W\) is the line \(\langle r\rangle\).

Again choose one representative from each of the \(q+1\) projective lines of \(W\). Their perpendicular hyperplanes cover \(V\), so the selected set dominates. Moreover the representative of \(\langle r\rangle\) is adjacent to every other selected representative. Hence every selected vertex has a selected neighbor, and the set is total dominating. With (1),
\[
\gamma_t=q+1.
\]

### Even characteristic: paired domination

Now use the nondegenerate plane
\[
W_0=\langle e_1,e_2\rangle.
\]
In characteristic two,
\[
B((x,y),(x,y))=x^2+y^2=(x+y)^2,
\]
so \(W_0\) has exactly one isotropic projective line,
\[
L_0=\langle e_1+e_2\rangle.
\]
The remaining \(q\) projective lines are paired by the fixed-point-free orthogonal-complement involution.

Choose one representative from every projective line of \(W_0\); as before, their perpendicular hyperplanes cover \(V\). Since \(n\ge3\), choose a nonzero
\[
z\in W_0^\perp.
\]
Pair \(z\) with the representative of \(L_0\), and pair the remaining \(q\) representatives by orthogonal complement. This gives a perfect matching on a dominating set of size \(q+2\). With (2),
\[
\gamma_{\mathrm{pr}}=q+2
\qquad(q\text{ even}).
\]

## Verification

The accompanying `verify.py` constructs the graph directly from the dot product over prime fields and tests total and paired domination from the graph definition.

It exhaustively determines both minima for
\[
(q,n)=(2,3),(2,4),(3,3),
\]
including all candidate subsets through the optimum. It also verifies an explicit paired-total witness of size \(6\) for \(TD(\mathbb F_5,3)\) and replays the numerical hyperplane-union inequality over a wider parameter grid.

Exact output:

```text
q=2,n=3: vertices=7, gamma_t=3, gamma_pr=4 exhaustive
q=2,n=4: vertices=15, gamma_t=3, gamma_pr=4 exhaustive
q=3,n=3: vertices=26, gamma_t=4, gamma_pr=4 exhaustive
q=5,n=3: explicit paired-total witness size=6 verified
hyperplane-union lower-bound arithmetic checked
VERIFY_OK
```

These calculations are corroborative. The proof for all prime powers and all \(n\ge3\) is the hyperplane-cover and two-plane argument above.

## Relationship to prior work

Badawi introduced the total dot product graph and proved its basic connectivity, diameter, and girth properties; the paper does not study domination parameters. Its publisher record gives online publication on 1 August 2014 and primary Mathematics Subject Classification \(13A15\).

Mollahajiaghaei then determined the ordinary domination number over finite fields. Theorem 3.2 of the 19 January 2016 preprint gives \(q+1\) except for \(TD(\mathbb F_2,3)\), whose ordinary domination number is \(2\). The paper defines only ordinary domination in the relevant section and does not treat total or paired domination. Thus the present theorem is not a restatement of that result: the binary exceptional graph rises from ordinary value \(2\) to total value \(3\) and paired value \(4\), while even fields in general exhibit a parity-forced paired gap.

Saleh and Megahed later studied ordinary domination for total dot product graphs over residue rings and unit dot product graphs. Their open full text contains no occurrence of “total domination” or “paired”, and its domination section explicitly uses the ordinary definition.

A separate earlier result in this collection concerns the paired-domination polynomial of the **unit** dot product graph on \(\mathbb F_q\times\mathbb F_q\). That graph has only unit-coordinate vertices and a different slope-component structure. The present graph contains every nonzero vector of \(\mathbb F_q^n\), works uniformly for all \(n\ge3\), and is governed by hyperplane covers; neither result implies the other.

## Limitations

The theorem does not cover \(n=2\), where the isotropy type of the standard two-dimensional form affects the available matching constructions.

The verification program exhausts only small prime-field instances; extension to arbitrary prime powers is proved algebraically, not computationally.

No claim is made about paired-domination polynomials, counting minimum sets, or domination variants beyond ordinary, total, and paired domination.

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188. Published online 1 August 2014.
2. M. Mollahajiaghaei, “Properties of the Dot Product Graph of a Commutative Ring,” arXiv:1601.05034v1, 19 January 2016.
3. D. Saleh and N. Megahed, “Dot product graphs and domination number,” *Journal of the Egyptian Mathematical Society* 28 (2020), Article 31. DOI: 10.1186/s42787-020-00092-6.
