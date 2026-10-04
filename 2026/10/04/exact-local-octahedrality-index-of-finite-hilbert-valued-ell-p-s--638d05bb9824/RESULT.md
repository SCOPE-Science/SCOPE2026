# Exact local-octahedrality index of finite Hilbert-valued \(\ell_p\)-sums

## Finding
Let \(H\) be a real Hilbert space with \(\dim H\ge 2\), let \(n\ge 1\), and let \(1\le p<\infty\). Put \(X=\ell_p^n(H)\). For Hardtke's local-octahedrality index
\[
s(X)=\sup\{c\in[0,2]:\forall x\in S_X\;\forall\varepsilon>0\;\exists y\in S_X\;\min\{\|x+y\|,\|x-y\|\}\ge c-\varepsilon\},
\]
one has
\[
s(\ell_p^n(H))=
\begin{cases}
\left(1-\frac1n+\left(1+n^{-2/p}\right)^{p/2}\right)^{1/p},&1\le p\le2,\\
\sqrt2,&2\le p<\infty.
\end{cases}
\]
Thus the finite number of coordinates affects the exact index precisely below the Hilbert exponent. For \(1\le p<2\), these values increase to \(2^{1/p}\) as \(n\to\infty\); for \(p\ge2\), the value is already \(\sqrt2\) for every finite \(n\).

## Assumptions and scope
The scalar field is real. The Hilbert space may have arbitrary dimension at least two, finite or infinite. The integer \(n\) is finite and positive. The norm on \(\ell_p^n(H)\) is
\[
\|(x_1,\ldots,x_n)\|_p=\left(\sum_{i=1}^n\|x_i\|_H^p\right)^{1/p}.
\]
No assertion is made for complex Hilbert spaces, for \(p=\infty\), or for summands that are merely uniformly convex rather than Hilbert.

## Proof
Write \(a_i=\|x_i\|_H\) for \(x=(x_i)_{i=1}^n\in S_X\), so \(\sum_i a_i^p=1\).

Assume first that \(1\le p\le2\). Choose \(j\) with \(a_j\le n^{-1/p}\). Select a unit vector \(u\in H\) orthogonal to \(x_j\), and let \(y\in S_X\) be supported only at coordinate \(j\), with \(y_j=u\). Then
\[
\|x\pm y\|_p^p=1-a_j^p+(1+a_j^2)^{p/2}.
\]
The function
\[
f(a)=1-a^p+(1+a^2)^{p/2}
\]
is decreasing on \([0,1]\): for \(a>0\),
\[
f'(a)=pa\left((1+a^2)^{p/2-1}-a^{p-2}\right)\le0,
\]
and the endpoint \(a=0\) follows by continuity. Therefore
\[
\min\{\|x+y\|_p,\|x-y\|_p\}^p
\ge1-\frac1n+\left(1+n^{-2/p}\right)^{p/2}.
\]
This proves the lower bound.

For the matching upper bound, take a unit vector \(e\in H\), put \(a=n^{-1/p}\), and choose the balanced point \(x=(ae,\ldots,ae)\in S_X\). Let \(y=(y_i)\in S_X\), set \(b_i=\|y_i\|_H\), and write \(A_\pm=\|x\pm y\|_p\). Since \(t\mapsto t^{p/2}\) is concave,
\[
\frac{\|ae+y_i\|_H^p+\|ae-y_i\|_H^p}{2}\le(a^2+b_i^2)^{p/2}.
\]
Hence
\[
\min\{A_+,A_-\}^p\le\frac{A_+^p+A_-^p}{2}\le\sum_{i=1}^n(a^2+b_i^2)^{p/2}.
\]
Set \(c_i=b_i^p\), so \(c_i\ge0\) and \(\sum_i c_i=1\). With \(q=2/p\ge1\),
\[
(a^2+b_i^2)^{p/2}=(a^2+c_i^q)^{1/q}.
\]
The function \(c\mapsto(a^2+c^q)^{1/q}\) is convex on \([0,1]\). Therefore its symmetric sum over the simplex \(\sum_i c_i=1\) is bounded above by its value at a vertex:
\[
\sum_{i=1}^n(a^2+c_i^q)^{1/q}
\le(n-1)a^p+(a^2+1)^{p/2}
=1-\frac1n+\left(1+n^{-2/p}\right)^{p/2}.
\]
Thus every \(y\in S_X\) has one sign for which the distance from the balanced \(x\) is at most the claimed constant, proving equality for \(1\le p\le2\).

Now assume \(p\ge2\). For arbitrary \(x=(x_i)\in S_X\), choose for each nonzero \(x_i\) a unit vector orthogonal to \(x_i\), and let \(y_i\) have norm \(a_i\) in that orthogonal direction. Then \(y\in S_X\) and
\[
\|x\pm y\|_p^p=\sum_i(\sqrt2\,a_i)^p=2^{p/2},
\]
so both distances equal \(\sqrt2\). This gives the lower bound.

For the upper bound, fix \(x=(e,0,\ldots,0)\) with \(e\in S_H\). Given \(y=(y_i)\in S_X\), put \(b=\|y_1\|_H\) and choose a sign \(\sigma\in\{-1,1\}\) with \(\langle e,\sigma y_1\rangle\le0\). Then
\[
\|x+\sigma y\|_p^p\le(1+b^2)^{p/2}+1-b^p.
\]
With \(t=b^p\) and \(r=p/2\ge1\), the right-hand side is
\[
h(t)=(1+t^{1/r})^r+1-t.
\]
For \(0<t\le1\),
\[
h'(t)=(1+t^{1/r})^{r-1}t^{1/r-1}-1\ge0,
\]
so \(h(t)\le h(1)=2^r\). Hence one of \(\|x+y\|_p\) and \(\|x-y\|_p\) is at most \(\sqrt2\), which proves the upper bound and completes the proof.

## Verification
Every estimate is analytic. The two sharp witnesses are explicit: a least-norm coordinate with an orthogonal unit vector for the lower bound below \(p=2\), the balanced vector for its upper bound, coordinatewise orthogonal vectors for the lower bound above \(p=2\), and a one-coordinate vector for its upper bound. The endpoint \(p=2\) gives \(\sqrt2\) from both formulas. For \(n=1\), the first formula also gives \(\sqrt2\), agreeing with the Hilbert-space value.

## Relationship to prior work
Hardtke introduced the invariant \(s(X)\) in the setting of local octahedrality, proved that \(s(H)=\sqrt2\) for Hilbert spaces of dimension at least two, and obtained lower restrictions on summands of locally octahedral absolute sums. The inspected full text does not give the exact value of \(s(\ell_p^n(H))\) for finite \(n\), nor the finite-cardinality transition at \(p=2\). The present calculation is an exact finite-sum optimization rather than a qualitative inheritance statement.

## Limitations
The argument uses genuine Hilbert orthogonality and the exact parallelogram identity in each coordinate. It does not automatically extend to general uniformly convex summands. The originality comparison is limited by the possibility that an older geometric-constant paper may encode the same quantity under different terminology; no such equivalent statement was found in the inspected source or targeted searches.

## References
[1] Jan-David Hardtke, *Summands in locally almost square and locally octahedral spaces*, arXiv:1705.06610. First public version: 2017-05-18. Primary classification: 46B20.
