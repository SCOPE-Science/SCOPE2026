# Two exceptional separation-rank collapses for five-dimensional displaced spheroids

## Finding
For five-dimensional spheroids whose symmetry axis passes through the origin but whose centers may be displaced along that axis, the minimum number of angular-times-offset terms in a **local parallel-section-volume representation** is completely classified. There are two exceptional displacements for noncentered prolate spheroids: the focal displacement lowers the generic rank from five to three, and a displacement equal to the focal distance divided by \(\sqrt3\) lowers it to four. Every centered nonspherical spheroid has rank three; a centered ball has rank one. These are exact minimal ranks, rather than upper bounds obtained by expanding a polynomial.

Explicitly, fix \(e\in S^4\), \(a,b>0\), and \(s\in\mathbb R\) with \(|s|<a\), and set
\[
K=\left\{x\in\mathbb R^5:\frac{(\langle x,e\rangle-s)^2}{a^2}+\frac{\|x-\langle x,e\rangle e\|^2}{b^2}\le1\right\}.
\]
Let \(r(K)\) be the least nonnegative integer \(R\) for which \(A_K(u,t)=\sum_{j=1}^R f_j(u)g_j(t)\) on all \(u\in S^4\) and \(|t|<\varepsilon\), where \(A_K(u,t)\) is the four-dimensional volume of the section \(K\cap\{x:\langle x,u\rangle=t\}\). For any sufficiently small \(\varepsilon>0\),
\[
r(K)=\begin{cases}
1,&s=0,\ a=b,\\
3,&s=0,\ a\ne b,\\
3,&s\ne0,\ a^2=b^2+s^2,\\
4,&s\ne0,\ a^2=b^2+3s^2,\\
5,&s\ne0\text{ and neither preceding equality holds}.
\end{cases}
\]

## Assumptions and scope
The ambient Euclidean dimension is exactly five, the section dimension exactly four, and all directions \(u\) range over the full unit sphere. The symmetry-axis direction \(e\) is arbitrary. The condition \(|s|<a\) ensures the origin lies inside \(K\), hence every section at sufficiently small \(|t|\) is nonempty. The factors \(f_j\) and \(g_j\) may be completely arbitrary real-valued functions; no smoothness assumption is needed. The assertion does not concern all ellipsoids, nor section volumes outside a common interior offset interval.

## Proof
Put \(w=\langle u,e\rangle\), \(v=sw\), and \(q=b^2+(a^2-b^2)w^2>0\). The positive-definite squared-semiaxis matrix of \(K\) is \(M=b^2 I+(a^2-b^2)ee^{\mathsf T}\), whose determinant satisfies \(\sqrt{\det M}=ab^4\). By a linear map from the unit ball, the section-volume formula for dimension five is
\[
A_K(u,t)=\frac{\pi^2ab^4}{2\sqrt q}\left(1-\frac{(t-v)^2}{q}\right)^2
=\frac{\pi^2ab^4}{2q^{5/2}}(h+2vt-t^2)^2,
\]
where \(h=q-v^2=b^2+(a^2-b^2-s^2)w^2\). It holds uniformly for sufficiently small \(|t|\), since \(q-(t-v)^2>0\) there.

The polynomial in the last display has coefficient functions (in ascending powers of \(t\))
\[
P_0=h^2,\quad P_1=4hv,\quad P_2=4v^2-2h,\quad P_3=-4v,\quad P_4=1.
\]
Multiplication of all five by the same positive angular function does not change their linear-span dimension. Moreover, **the smallest separable rank equals that dimension**: one expansion in the monomial basis gives an upper bound, while any representation with \(R\) arbitrary offset factors forces its collection of angular coefficient functions to lie in an \(R\)-dimensional span. For the latter assertion, evaluate at five distinct offsets and invert the Vandermonde matrix; this expresses each coefficient function as a linear combination of the five section-value functions, all of which lie in the span of the \(R\) angular factors. This also proves independence of the chosen sufficiently small offset interval.

If \(s=0\), then \(v=0\) and the coefficient span is \(\operatorname{span}\{1,h,h^2\}\). It has dimension one when \(a=b\) and three otherwise, since \(h=b^2+(a^2-b^2)w^2\) then varies through an interval.

Now assume \(s\ne0\). Write \(B=b^2>0\), \(z=v=sw\), and \(\beta=(a^2-b^2-s^2)/s^2\), so \(h=B+\beta z^2\). The even and odd polynomial coefficient subspaces are disjoint. The odd coefficients span \(\{z, Bz+\beta z^3\}\), of dimension one when \(\beta=0\) and two otherwise. The even coefficients span \(\{1,-2B+(4-2\beta)z^2,(B+\beta z^2)^2\}\). This span has dimension two if \(\beta=0\) or \(\beta=2\), and three otherwise: in the generic case the last entry has a nonzero degree-four coefficient, while the second has a nonzero degree-two coefficient. Adding the independent parity dimensions gives respectively \(3\), \(4\), and \(5\). Finally \(\beta=0\) is exactly \(a^2=b^2+s^2\), and \(\beta=2\) exactly \(a^2=b^2+3s^2\). Both imply \(a>b\), so the special positions arise only for prolate spheroids. Every case is exhausted.

## Verification
The embedded `CHECK.py` uses exact symbolic polynomial algebra. It computes coefficient-matrix ranks for nine sample geometries spanning all five rank regimes, verifies the formal sectional-numerator identity, and checks the symbolic determinant \(32\beta^3(\beta-2)\) of the generic five-by-five coefficient matrix. Its output is reproducible with Python and SymPy by running `python CHECK.py`. The actual proof above handles all real admissible parameters; finitely many sampled ranks do not establish the universal theorem.

## Relationship to prior work
Fish, Ryabogin, Sun and Yaskin [1], Theorem 4.2, establish that a convex body in odd dimension with a locally separable parallel-section function must be an ellipsoid. Their result is an **existence/rigidity theorem** about finite separability, not a formula for the minimal count of separation terms within ellipsoids. This finding studies precisely that count for the full natural five-dimensional translated axial family and identifies two exceptional displacement surfaces. The earlier paper by Yaskin and Zawalski [2] concerns separably integrable symmetric bodies and related integrated section functions; its symmetry assumptions and statements do not imply the noncentral displacement stratification here. The general elementary ellipsoid-section formula is not claimed as new.

## Limitations
Only axially symmetric five-dimensional ellipsoids whose centers lie on the symmetry axis are classified. The method does not determine minimum ranks for arbitrary five-dimensional ellipsoids, other odd ambient dimensions, or offset intervals crossing the boundary of some sections. The theorem is analytically proved but has not undergone an independent expert audit. Although relevant indexed results and accessible primary sources were compared, earlier unindexed equivalent calculations cannot be excluded; historical priority is not certified.

## References
[1] A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1 (first posted 2026-10-07), https://arxiv.org/html/2610.10229v1, especially Section 4, Theorem 4.2.

[2] V. Yaskin and T. Zawalski, *On separably integrable symmetric convex bodies*, arXiv:2306.17127v1, https://arxiv.org/pdf/2306.17127.
