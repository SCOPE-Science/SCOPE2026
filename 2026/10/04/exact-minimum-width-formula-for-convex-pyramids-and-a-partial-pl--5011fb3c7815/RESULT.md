# Exact minimum-width formula for convex pyramids and a partial-plank consequence
## Finding
Let \(d\ge2\). Let \(B\) be a compact convex body with nonempty relative interior in an affine hyperplane \(H\subset\mathbb R^d\), let \(v\notin H\), and put \(K=\operatorname{conv}(B\cup\{v\})\). Let \(p\) be the orthogonal projection of \(v\) to \(H\) and let \(h=\operatorname{dist}(v,H)\).

If \(p\notin B\), then \(w(K)<h\). If \(p\in B\), translate \(p\) to the origin in the direction space \(L=H-p\), write \(C=B-p\), and define the support number
\[
a(e)=h_C(e)=\max_{x\in C}\langle x,e\rangle,\qquad e\in S(L).
\]
Then
\[
w(K)=\min\left\{h,\ \min_{e\in S(L)}\frac{h\,[a(e)+a(-e)]}{\sqrt{h^2+a(e)^2}}\right\}.
\]
Equivalently, after identifying \(e\) and \(-e\), the nonvertical candidate associated with that unoriented line is
\[
\frac{h\,[a(e)+a(-e)]}{\sqrt{h^2+\max\{a(e)^2,a(-e)^2\}}}.
\]
Hence the base altitude is a minimum width, \(w(K)=h\), exactly when \(p\in B\) and
\[
[a(e)+a(-e)]^2\ge h^2+\max\{a(e)^2,a(-e)^2\}
\]
for every unit \(e\in L\).

As an application, suppose this criterion holds and \(0<W<h\). For every finite family of planks \(P_i\) with total width at most \(W\),
\[
\operatorname{vol}_d\!\left(K\cap\bigcup_iP_i\right)
\le
\left[1-\left(1-\frac Wh\right)^d\right]\operatorname{vol}_d(K),
\]
and equality is attained by one width-\(W\) plank parallel and adjacent to the base.

## Assumptions and scope
The base may be any \((d-1)\)-dimensional compact convex body, not necessarily a polytope. The formula is Euclidean and uses the ordinary support function and Euclidean width. No smoothness, symmetry, or strict convexity is assumed. The partial-plank consequence is relevant in dimensions \(d\ge3\), since Bakaev--Polyanskii already prove the one-plank statement for every planar convex body.

The source paper studies optimal partial plank coverings and, in its discussion, proves the conjectured one-plank optimum for simplices having a facet altitude equal to the minimum width. The formula above resolves exactly when the analogous base altitude condition holds for an arbitrary convex pyramid.

## Proof
Choose a unit normal \(n\) to \(H\) pointing from \(H\) toward \(v\), translate \(p\) to the origin, and identify
\[
B=C\times\{0\},\qquad v=hn.
\]
First suppose \(p\notin B\). Strong separation of the origin from the compact convex set \(C\) gives a unit \(e\in L\) for which \(h_C(-e)<0\). For sufficiently small \(r>0\), put
\[
u_r=re+\sqrt{1-r^2}\,n.
\]
The apex supports \(K\) in direction \(u_r\), while the base supports it in direction \(-u_r\). Thus
\[
w_K(u_r)=h\sqrt{1-r^2}+r h_C(-e)<h
\]
for all sufficiently small positive \(r\). Therefore \(w(K)<h\).

Now suppose \(p\in B\). Then \(a(e)\ge0\) for every \(e\). Width is unchanged when the direction is negated, so every unit direction can be written, after a possible sign change, as
\[
u=re+\sqrt{1-r^2}\,n,\qquad e\in S(L),\quad 0\le r\le1.
\]
Put \(a=a(e)\) and \(b=a(-e)\). The support function of the convex hull is the maximum of the support functions of its two generators, hence
\[
h_K(u)=\max\{ra,h\sqrt{1-r^2}\},\qquad h_K(-u)=rb.
\]
Therefore
\[
w_K(u)=rb+\max\{ra,h\sqrt{1-r^2}\}.
\]
The two terms in the maximum agree at
\[
r_0=\frac{h}{\sqrt{h^2+a^2}}.
\]
For \(0\le r\le r_0\), the width equals
\[
f(r)=rb+h\sqrt{1-r^2},
\]
which is concave, so its minimum on this interval is attained at an endpoint. Those endpoint values are
\[
f(0)=h,\qquad f(r_0)=\frac{h(a+b)}{\sqrt{h^2+a^2}}.
\]
For \(r_0\le r\le1\), the width is \(r(a+b)\), which is nondecreasing. Thus, for this fixed oriented horizontal direction \(e\), the smallest width among all inclinations is exactly
\[
\min\left\{h,\frac{h(a+b)}{\sqrt{h^2+a^2}}\right\}.
\]
Taking the minimum over \(e\in S(L)\) proves the stated formula.

The vertical width equals \(h\). Hence it is globally minimal exactly when
\[
a(e)+a(-e)\ge\sqrt{h^2+a(e)^2}
\]
for every \(e\). Applying the same inequality to \(-e\) and combining the two gives the symmetric criterion
\[
[a(e)+a(-e)]^2\ge h^2+\max\{a(e)^2,a(-e)^2\}.
\]

Finally assume the criterion holds, so \(w(K)=h\), and let \(0<W<h\). Corollary 7 and Lemma 8 of Bakaev--Polyanskii imply that any family of planks of total width at most \(W\) leaves uncovered volume at least
\[
\left(1-\frac Wh\right)^d\operatorname{vol}_d(K).
\]
A single plank of width \(W\), parallel and adjacent to the base, removes exactly the bottom height \(W\). The remaining pyramid is homothetic to \(K\) about the apex with ratio \(1-W/h\), so its volume is exactly the lower bound. This proves optimality and the displayed covered-volume formula.

## Verification
The proof is analytic. Its only optimization is one-dimensional: on the branch before the base support overtakes the apex support, \(rb+h\sqrt{1-r^2}\) is concave and therefore minimized at an endpoint; on the other branch, \(r(a+b)\) is nondecreasing. The accompanying `verify.py` numerically compares the closed formula with a direct directional minimization for several nonsymmetric polygonal bases and checks the branch calculation over a grid. These finite checks are supplemental and are not used as an infinite-dimensional proof.

## Relationship to prior work
Bakaev and Polyanskii formulate the optimal partial-plank conjecture, prove it for Euclidean balls and all planar convex bodies, and derive a general Minkowski-subtraction lower bound. In their discussion they obtain the exact one-plank optimum for a special class of simplices under the hypothesis that one facet altitude already equals the minimum width. They do not give a criterion for that hypothesis, nor a minimum-width formula for general pyramids.

Averkov and Martini study minimum width in pyramids in connection with reduced bodies. Their paper uses antipodality and two-dimensional projections; its stated results concern non-reducedness and do not provide the support-function formula or altitude criterion above.

The partial-plank inequality in this finding is deliberately not presented as an independent strengthening of the Bakaev--Polyanskii machinery: once the new altitude criterion gives \(w(K)=h\), their Corollary 7 and Lemma 8 yield the lower bound, and pyramid homothety gives equality.

## Limitations
The result classifies when the base altitude is a minimum width and computes the minimum width when the apex projection lies in the base. When the apex projection lies outside the base, only the strict inequality \(w(K)<h\) is asserted here; no closed formula for \(w(K)\) is claimed in that case. The literature search cannot exclude an equivalent formula hidden in older general treatments of polytope width; the most directly relevant pyramid paper inspected did not contain it.

## References
1. E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483v1, 29 July 2026. Primary MSC 52A40.
2. G. Averkov and H. Martini, *On pyramids and reducedness*, Periodica Mathematica Hungarica 57 (2008), 117--120. DOI: 10.1007/s10998-008-8117-x.
