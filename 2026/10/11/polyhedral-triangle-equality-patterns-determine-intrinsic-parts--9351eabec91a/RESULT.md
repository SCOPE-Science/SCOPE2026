# Polyhedral triangle-equality patterns determine intrinsic parts
## Finding
Let \(X\) be a finite-dimensional real vector space and let \(p,q\) be polyhedral norms on \(X\). Then \(p\) and \(q\) belong to the same intrinsic part of the cone \(\mathcal N(X)\cup\{0\}\) if and only if their triangular defects have the same zero set: \[\Delta_p(x,y)=0\quad\Longleftrightarrow\quad\Delta_q(x,y)=0\qquad(x,y\in X).\] Equivalently, for polyhedral norms the triangle-equality relation alone determines intrinsic-part membership. In the nontrivial direction, equality of the zero sets forces constants \(a,b>0\) such that \(a\Delta_p\le\Delta_q\le b\Delta_p\) on \(X\times X\).

## Assumptions and scope
For a norm \(r\) on a finite-dimensional real vector space \(X\), write
\[
\Delta_r(x,y)=r(x)+r(y)-r(x+y).
\]
A polyhedral norm means that its unit ball is a centrally symmetric polytope. Equivalently, there is a finite set \(F_r\subset X^*\) such that
\[
r(x)=\max_{\varphi\in F_r}\varphi(x).
\]
The intrinsic part is the part for the order induced by the cone of equivalent norms. In finite dimension every norm on \(X\) is equivalent to every other one, so the ambient cone is unambiguous.

The theorem is specific to the polyhedral subclass. The focal source shows that equality of triangular-defect zero sets is not sufficient for arbitrary smooth norms: its \(\ell_2^2\) and \(\ell_4^2\) example has the same zero set but non-comparable defect decay.

## Proof
The necessity follows from the intrinsic-part criterion in arXiv:2609.28922v1, Theorem 4.6: if \(p\) and \(q\) lie in the same intrinsic part, then there are \(a,b>0\) with
\[
a\Delta_p(x,y)\le\Delta_q(x,y)\le b\Delta_p(x,y)
\]
for all \(x,y\), and hence their zero sets agree.

For the converse, suppose that \(\Delta_p\) and \(\Delta_q\) have the same zero set. Because \(p\) and \(q\) are polyhedral, each of the six functions
\[
p(x),\ p(y),\ p(x+y),\ q(x),\ q(y),\ q(x+y)
\]
is linear on every cone of a suitable finite common polyhedral conic subdivision of \(X\times X\). Therefore both \(\Delta_p\) and \(\Delta_q\) are linear on every cone of that subdivision.

Normalize by the compact set
\[
D=\{(x,y)\in X\times X:p(x)+p(y)=1\}.
\]
Intersecting the common conic subdivision with \(D\) gives finitely many compact polytopes \(P\), and on each such \(P\) both defects are nonnegative affine functions.

We use the following elementary polyhedral lemma. If \(P\) is a compact polytope and \(f,g:P\to[0,\infty)\) are affine with the same zero set, then there are constants \(a_P,b_P>0\) for which
\[
a_P f\le g\le b_P f
\]
on \(P\). Indeed, if both functions vanish identically there is nothing to prove. Otherwise, write a point as a convex combination of the vertices of \(P\). Nonnegativity makes the zero set of each affine function a face, so the same vertices have zero value for \(f\) and \(g\). On every remaining vertex \(v\), the ratio \(g(v)/f(v)\) is positive. Taking its minimum and maximum over those finitely many vertices and then averaging over any convex decomposition gives the displayed inequalities throughout \(P\).

Apply the lemma on every cell \(P\). The global zero-set hypothesis makes the two cellwise zero sets identical. Since there are only finitely many cells, the minimum of the positive constants \(a_P\) and the maximum of the finite constants \(b_P\) give global numbers \(a,b>0\) satisfying
\[
a\Delta_p\le\Delta_q\le b\Delta_p
\]
on \(D\). For \((x,y)\ne(0,0)\), scale both vectors by \(1/(p(x)+p(y))\). Positive homogeneity of triangular defects then extends the same inequalities to all of \(X\times X\); at \((0,0)\) they are trivial. Theorem 4.6 of the focal source now places \(p\) and \(q\) in the same intrinsic part.

## Verification
The proof is symbolic and finite. The only nonstandard external premise used for the final implication is the focal source's Theorem 4.6, which characterizes common intrinsic parts by uniform two-sided comparison of triangular defects; its Corollary 4.7 supplies the necessary zero-set implication. The full theorem, corollary, counterexample, finite-dimensional local criterion, and intrinsic-distance formula were inspected in the manuscript.

The new step was checked independently at the level of its finite-cell argument: on a common polyhedral cell, both defects are nonnegative affine functions; equality of their zero sets forces the same zero vertices, and ratios on the finitely many remaining vertices bound the ratio everywhere by convexity. Compact normalization and positive homogeneity then give global constants. No enumeration, numerical experiment, or asymptotic approximation is used as proof.

## Relationship to prior work
Acosta-Portilla's arXiv:2609.28922v1 proves the general uniform-comparability criterion and shows that equality of defect zero sets is necessary but not sufficient in general. Its Example 4.8 uses the smooth norms \(\ell_2^2\) and \(\ell_4^2\) to demonstrate the failure, while Proposition 4.9 says that in finite dimension zero-set equality becomes sufficient once local quantitative comparability is also assumed. The present theorem identifies a natural class in which that extra quantitative hypothesis is automatic: for polyhedral norms, finite piecewise-linearity converts equality of zero sets into global uniform comparability.

A related preprint, arXiv:2609.14035v1, studies finite polyhedral models of equivalent norms through the logarithmic distortion metric and finite fans. Its abstract and indexed metadata concern the ambient logarithmic metric rather than the intrinsic triangular-defect order. Full text was not available through the attempted retrieval routes during this check, so an equivalent statement hidden there remains a specific residual originality risk. Focused database and web searches for the zero-set converse, piecewise-linear defect comparability, and polyhedral intrinsic parts did not locate a covering statement.

## Limitations
The conclusion requires finite dimension and polyhedral norms. It does not extend to arbitrary strictly convex or smooth norms; the focal source gives an explicit failure. The theorem classifies intrinsic-part membership, not the exact intrinsic Hilbert distance inside a polyhedral part. It also does not claim that a coarse face-count or an unlabeled combinatorial type determines the part: the invariant used here is the full triangle-equality relation on pairs of vectors.

The literature is very recent. In particular, the related polyhedral-model preprint could not be inspected beyond its abstract and metadata, so that access gap is retained as a residual originality risk rather than treated as evidence of absence.

## References
1. J. R. Acosta-Portilla, *Intrinsic Hilbert metrics on cones of equivalent norms*, arXiv:2609.28922v1, first public 2026-09-24. Relevant items: Theorem 4.6, Corollary 4.7, Example 4.8, Proposition 4.9, and Theorem 5.2.
2. J. R. Acosta-Portilla, *Finite Polyhedral Models for the Space of Equivalent Norms*, arXiv:2609.14035v1, first public 2026-09-12. Abstract and indexed metadata inspected for overlap.
