# Hilbert regularization separates intrinsic parts of mixed \(\ell_p\) norms

## Finding
For every integer \(n\ge2\), every \(1<p<\infty\), and every \(a\ge0\), define a real norm on \(\mathbb R^n\) by
\[
N_{p,a}(x)=\|x\|_p+a\|x\|_2.
\]
Two norms \(N_{p,a}\) and \(N_{q,b}\) belong to the same intrinsic part of the cone of all equivalent norms on \(\mathbb R^n\) **if and only if** one of the following disjoint conditions holds:

1. \(1<p=q<2\), with arbitrary \(a,b\ge0\).
2. \(2<p=q<\infty\), with \(a=b=0\).
3. \(p,q\ge2\), with \((p=2\text{ or }a>0)\) and \((q=2\text{ or }b>0)\).

In particular, all super-Hilbert norms with even an arbitrarily small positive additive Euclidean term lie in one intrinsic part with the Euclidean norm. No such perturbation unites two distinct sub-Hilbert exponents. The completely unregularized super-Hilbert exponents remain in mutually different parts.

There is also a quantitative boundary law. Fix \(p>2\), \(b>0\), and \(0<a<b\). Write \(d_{\mathrm{int}}\) for the intrinsic Hilbert projective metric on the cone of equivalent norms. Then
\[
\log\frac{b(1+a)}{a(1+b)}
\le d_{\mathrm{int}}([N_{p,a}],[N_{p,b}])
\le \log\frac ba.
\]
In particular,
\[
\lim_{a\downarrow0}\frac{d_{\mathrm{int}}([N_{p,a}],[N_{p,b}])}{\log(1/a)}=1,
\]
although \(N_{p,a}\to N_{p,0}\) uniformly on the Euclidean unit sphere and in the ordinary symmetric logarithmic norm metric. The endpoint \(N_{p,0}\) lies at infinite intrinsic distance from \(N_{p,b}\).

## Assumptions and scope
All spaces and norms are **real**, and \(n\ge2\) is finite. The intrinsic order is that induced by the cone \(\mathcal N(\mathbb R^n)\cup\{0\}\) of all equivalent norms: \(P\preceq Q\) when \(Q-P\) is either zero or a norm. The intrinsic Hilbert distance is infinite between distinct parts. For a norm \(R\), its triangular defect is
\[
\Delta_R(x,y)=R(x)+R(y)-R(x+y)\qquad(x,y\in\mathbb R^n).
\]
We use the established intrinsic-part criterion that two equivalent norms lie in the same part exactly when their defects are bounded above and below by positive multiples of each other. This criterion is Theorem 4.6 in the initiating paper cited below, not claimed as new here.

## Proof
**1. A uniform Euclidean comparison for defects.** For \(1<p<2\), put
\[
c_{p,n}=(p-1)n^{-(p-1)(1/p-1/2)}>0.
\]
For \(p>2\), put
\[
C_{p,n}=(p-1)n^{(p-1)(1/2-1/p)}<\infty.
\]
We first prove that for every \(x,y\in\mathbb R^n\),
\[
\Delta_{\|\cdot\|_p}(x,y)\ge c_{p,n}\Delta_{\|\cdot\|_2}(x,y)
\quad(1<p<2),
\]
and
\[
\Delta_{\|\cdot\|_p}(x,y)\le C_{p,n}\Delta_{\|\cdot\|_2}(x,y)
\quad(p>2).
\]
To prove this, let \(F_p(z)=\|z\|_p\), and use the Euclidean norm \(E(z)=\|z\|_2\). Whenever \(z\ne0\) has nonzero coordinates, direct differentiation gives the exact Hessian identity
\[
D^2F_p(z)[h,h]
=(p-1)F_p(z)^{1-p}
\min_{s\in\mathbb R}\sum_{i=1}^n|z_i|^{p-2}(h_i-sz_i)^2.
\]
The corresponding Euclidean Hessian is
\[
D^2E(z)[h,h]=E(z)^{-1}\min_{s\in\mathbb R}\|h-sz\|_2^2.
\]
If \(1<p<2\), then \(|z_i|^{p-2}\ge E(z)^{p-2}\) and \(F_p(z)\le n^{1/p-1/2}E(z)\); hence
\[
D^2F_p(z)[h,h]\ge c_{p,n}D^2E(z)[h,h].
\]
If \(p>2\), then \(|z_i|^{p-2}\le E(z)^{p-2}\) and \(F_p(z)\ge n^{1/p-1/2}E(z)\); hence
\[
D^2F_p(z)[h,h]\le C_{p,n}D^2E(z)[h,h].
\]
These inequalities imply, respectively, that \(F_p-c_{p,n}E\) and \(C_{p,n}E-F_p\) are convex. Indeed, along lines avoiding the origin, the derivatives are continuous and their almost-everywhere second derivatives are nonnegative; the isolated points where a coordinate vanishes cause no negative derivative jump (for \(p>1\), the first derivatives are continuous and the second derivatives are locally integrable). For lines through the origin, these differences are even and positively homogeneous along the line, and nonnegative: \(F_p\ge E\ge c_{p,n}E\) for \(p<2\), and \(C_{p,n}E\ge E\ge F_p\) for \(p>2\). Thus their derivatives also have nonnegative jumps at the origin. Their convexity proves the displayed triangular-defect comparisons by applying the triangle inequality to the convex homogeneous differences.

**2. Sufficiency of the three cases.** Since the defect is additive in the norm,
\[
\Delta_{N_{p,a}}=\Delta_{F_p}+a\Delta_E.
\]
For \(1<p<2\), Step 1 yields
\[
\Delta_{F_p}\le \Delta_{N_{p,a}}
\le(1+a/c_{p,n})\Delta_{F_p}.
\]
Therefore all choices of \(a\ge0\) for a fixed sub-Hilbert exponent \(p\) give comparable defects. For \(p>2\) and \(a>0\), Step 1 yields
\[
a\Delta_E\le \Delta_{N_{p,a}}
\le(C_{p,n}+a)\Delta_E.
\]
At \(p=2\), \(N_{2,a}=(1+a)E\). Thus every member of Case 3 has defects comparable to \(\Delta_E\). Case 2 compares a norm only with itself. The intrinsic-part criterion establishes sufficiency.

**3. Necessity and the precise boundary.** Let \(e_1,e_2\) be the first two coordinate vectors, and take \(x=e_1\), \(y=e_1+t e_2\) with \(t\to0\). The binomial expansion yields
\[
\Delta_{F_p}(x,y)
=\frac{1-2^{1-p}}{p}|t|^p+O(|t|^{2p}),
\qquad
\Delta_E(x,y)=\frac14t^2+O(t^4).
\]
The coefficient \((1-2^{1-p})/p\) is strictly positive for every \(p>1\). Hence the leading small-angle order of \(\Delta_{N_{p,a}}(x,y)\) is precisely
\[
\begin{cases}
|t|^p,&1<p<2\quad(\text{all }a\ge0),\\
|t|^p,&p>2,\ a=0,\\
t^2,&p=2\quad(\text{all }a\ge0),\text{ or }p>2,\ a>0.
\end{cases}
\]
If two defects are uniformly comparable, their leading powers at this family of pairs must agree. These powers coincide only within the three classes stated above. Conversely, Step 2 already proved that every pair within each class has comparable defects. This completes the classification.

**4. Logarithmic divergence at a regularization boundary.** Fix \(p>2\) and \(0<a<b\). For all pairs with \(\Delta_E(x,y)>0\), set \(u=\Delta_{F_p}(x,y)/\Delta_E(x,y)\ge0\). Then
\[
\frac{\Delta_{N_{p,b}}(x,y)}{\Delta_{N_{p,a}}(x,y)}
=\frac{u+b}{u+a}\le\frac ba.
\]
Along the pairs in Step 3, \(u\to0\), so the supremum of the defect ratio equals \(b/a\). The pointwise norm ratio likewise obeys
\[
1\le\frac{N_{p,b}(z)}{N_{p,a}(z)}\le\frac ba\qquad(z\ne0).
\]
The intrinsic Hilbert metric formula from the initiating paper now gives \(M_{\mathrm{int}}(N_{p,b}/N_{p,a})=b/a\), while its lower comparison constant satisfies
\[
1\le m_{\mathrm{int}}(N_{p,b}/N_{p,a})
\le\frac{N_{p,b}(e_1)}{N_{p,a}(e_1)}=\frac{1+b}{1+a}.
\]
Taking the logarithm of the quotient of optimal comparison constants gives the two asserted metric bounds. Dividing by \(\log(1/a)\) and letting \(a\downarrow0\) proves the limit. Norm convergence follows directly from \(N_{p,a}-N_{p,0}=aE\). Step 3 shows the unregularized endpoint is in a different intrinsic part, hence has infinite intrinsic distance.

## Verification
The inequalities in Step 1 come from an explicitly differentiated Hessian identity, finite-dimensional norm comparisons, and an integration of one-dimensional convexity. The small-angle coefficient in Step 3 comes from expanding \((1+u)^{1/p}\) at \(u=0\). The logarithmic bound uses the sharp supremum of defect ratios, not a numerical extrapolation. These analytic steps prove the all-vector and all-parameter statements.

An accompanying deterministic Python checker samples random pairs in dimensions two and three, checks both one-sided defect bounds for representative exponents on either side of two, and checks the leading small-angle power and metric-bound arithmetic. These finite numerical checks are stress tests only, not exhaustive proof of the infinite family of inequalities or of literature originality.

## Relationship to prior work
Acosta-Portilla, *Intrinsic Hilbert metrics on cones of equivalent norms* (arXiv:2609.28922v1), introduces the intrinsic norm-cone distance and proves the criterion and metric formula used here. Its Example 4.8 already demonstrates the non-comparability of the unperturbed Euclidean and \(\ell_4^2\) norms. The present result does **not** claim this example or the general criterion as new. Its contribution is the complete two-parameter intrinsic-part classification, the asymmetric Hilbert-regularization phase transition at exponent two, and the logarithmic approach to the infinite-distance boundary.

Related studies classify polyhedral norms by their triangle-equality patterns and compute exact intrinsic distances between Hilbertian renormings. Those concern, respectively, finite polyhedral norms and norms induced by inner products. Neither statement covers the non-Hilbert smooth mixed norms in the present theorem. Our proof identifies a different mechanism: two-sided defect comparability produced by quadratic curvature regularization and obstructed by a precise vanishing order on coordinate axes.

## Limitations
The classification concerns finite-dimensional **real** \(\ell_p\) norms with an **additive** Euclidean term. It does not establish analogous results on infinite-dimensional \(\ell_p\), general Orlicz norms, arbitrary smooth norms, or complex norm spaces. The logarithmic estimate gives the sharp leading divergence coefficient but does not determine the bounded additive correction or the exact distance for every \(a,b\). Independent scientific review has not been performed, and unindexed related literature is a residual historical-priority risk.

## References
1. J. R. Acosta-Portilla, *Intrinsic Hilbert metrics on cones of equivalent norms*, arXiv:2609.28922v1, first public 2026-09-24, especially Theorem 4.6, Example 4.8, Proposition 4.9, and Theorem 5.2.
2. *Polyhedral triangle-equality patterns determine intrinsic parts*, published research result, 2026-10-11, identifier `9351eabec91a` (finite polyhedral subclass).
3. *Equivalent Hilbert norms have intrinsic distance exactly three times the log distance*, published research result, 2026-10-04, identifier `6f2b4c5fbe28` (Hilbertian subclass).
