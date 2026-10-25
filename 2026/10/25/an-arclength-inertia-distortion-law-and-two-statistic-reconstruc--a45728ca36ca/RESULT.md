# An arclength-inertia distortion law and two-statistic reconstruction of ellipses

## Finding
Let \(X,Y,Z\) be independent points sampled uniformly by **arclength** on the boundary of an arbitrary nondegenerate Euclidean ellipse, whose (unoriented) semiaxes are \(a\ge b>0\). Put
\[
D=\mathbb E\|X-Y\|^2,\qquad H=\mathbb E\big[\operatorname{area}(XYZ)^2\big],\qquad \eta=\frac{32H}{3D^2}.
\]
Then \((D,H)\) determines \((a,b)\) uniquely, including circles. More precisely, if \(\lambda_+\ge\lambda_->0\) are the two roots of
\[
z^2-\frac D2 z+\frac{2H}{3}=0,
\]
then the ratio \(h=\lambda_-/\lambda_+\) strictly increases with \(s=b^2/a^2\), from zero to one, and satisfies the global strict geometric distortion bounds
\[
 s<h<\sqrt{s}\qquad(0<s<1).
\]
For the circle \(s=h=1\). The normalized three-point statistic \(\eta=4h/(1+h)^2\) therefore determines the aspect ratio without the overall scale. At the circular endpoint, with \(t=1-s\),
\[
t=\frac83\sqrt{1-\eta}+O(1-\eta),\qquad \eta\uparrow1.
\]
Thus the best possible local Hölder exponent for recovering \(t\) from \(\eta\) at a circle is \(1/2\).

## Assumptions and scope
Points are independently distributed according to normalized Euclidean arclength on one and the same ellipse. The triangle area is its ordinary unsigned Euclidean area. Only semiaxes up to interchange and rigid motions can be inferred from isometry-invariant statistics. The theorem concerns genuine ellipses \(b>0\); the zero-minor-axis case is a limit, not an included ellipse. It does **not** assert that the marginal law of a single chord length is sufficient.

## Proof
Parametrize the ellipse by \((a\sin\theta,b\cos\theta)\), let \(t=1-b^2/a^2\), and set \(U=\sin^2\theta\). The Euclidean arclength element is \(a\sqrt{1-tU}\,d\theta\). Denote expectation under the corresponding normalized measure by \(\mathbb E_t\) and put \(A(t)=\mathbb E_t U\). Symmetry implies the covariance matrix \(\Sigma\) has eigenvalues
\[
 \lambda_+=a^2 A(t),\qquad \lambda_-=a^2(1-t)(1-A(t)).
\]
Here the first is indeed the larger: this follows below from the strict ratio inequality. Independence and centering imply
\[
\mathbb E\|X-Y\|^2=2\operatorname{tr}\Sigma.
\]
Expanding the determinant of two differences of three independent centered planar vectors yields
\[
\mathbb E\det(Y-X,Z-X)^2=6\det\Sigma,
\]
since the three squared cross-products each contribute \(2\det\Sigma\) and all mixed expectations vanish. Hence \(H=3\det\Sigma/2\), establishing the displayed quadratic for the eigenvalues.

It remains to prove strict monotonicity, not merely rely on the known elliptic-integral formulas for the moments. For \(0\le t<1\) the arclength-weighted law of \(U\) has density proportional to \(\sqrt{1-tu}/\sqrt{u(1-u)}\) on \((0,1)\). Differentiating the normalized integral gives
\[
 A'(t)=-\frac12\operatorname{Cov}_t\left(U,\frac{U}{1-tU}\right).
\]
The covariance is positive because both displayed functions of \(U\) are strictly increasing. For \(G=U/(1-tU)\ge0\), \(0\le U\le1\), and \(s=1-t>0\),
\[
\begin{aligned}
\operatorname{Cov}_t(U,G)&=\mathbb E_t[UG]-A\mathbb E_t G\\
&\le(1-A)\mathbb E_t[UG]\\
&\le\frac{A(1-A)}s.
\end{aligned}
\]
The first inequality uses \(UG\le G\), and the second uses \(UG=U^2/(1-tU)\le U/s\). Both are strict for \(0<t<1\) under the non-atomic law. Consequently
\[
-\frac{A(1-A)}{2s}<A'(t)<0.
\]
Define \(h(t)=s(1-A(t))/A(t)\). Since \(A(0)=1/2\), one has \(h(0)=1\), while
\[
-\frac1s<\frac{d}{dt}\log h(t)=-\frac1s-\frac{A'(t)}{A(t)(1-A(t))}<-\frac1{2s}.
\]
This proves strict decrease. Integrating from zero to \(t\), using \(\int_0^t du/(1-u)=-\log s\), gives \(s<h(t)<\sqrt s\). As \(t\uparrow1\), dominated convergence gives \(A(t)\to1/3\), hence \(h(t)\to0\). Thus the ratio maps \([0,1)\) bijectively onto \((0,1]\). The covariance eigenvalues recover \(h\), and the unique solution of its defining integral recovers \(t\), followed by
\[
 a=\sqrt{\lambda_+/A(t)},\qquad b=a\sqrt{1-t}.
\]
Finally, \(U\) has the arcsine law at \(t=0\), with \(\mathbb E_0U=1/2\) and \(\operatorname{Var}_0U=1/8\). Hence \(A'(0)=-1/16\), \(h(t)=1-3t/4+O(t^2)\), and \(1-\eta=(1-h)^2/(1+h)^2=9t^2/64+O(t^3)\). Inversion proves the stated \(8/3\) coefficient and optimality: a larger Hölder exponent would contradict this asymptotic along noncircular ellipses approaching a circle.

## Verification
The accompanying independent computational cross-check (`check_ellipse.py`) evaluates the defining arclength integrals by composite Simpson quadrature, checks the exact pair/triple identities, verifies the global bounds and inverse recovery at multiple aspect ratios, and checks the circular asymptotic. Its finite numerical tests are not used as proofs of monotonicity or universal quantifiers; those are established by the covariance inequality above. Run with `python3 check_ellipse.py` using Python's standard library.

## Relationship to prior work
The principal moments of inertia of an arclength-uniform elliptical wire are classical elliptic integrals. Nick Lord, *The moment of inertia of an elliptical wire* (Mathematical Gazette 98, 2014; online 2015), and J. Tatum's *Ellipses and Ellipsoids* both give forward computations of the wire's principal inertias. The added statement tested here is global strict inversion from two rotation-invariant random-point statistics with the quantitative distortion sandwich and the local sharp inverse exponent. Earlier forward formulas are acknowledged and not claimed new.

## Limitations
The optimal numerical constants for a global two-sided Lipschitz inverse away from circles are not determined. The fractional-Hölder statement concerns the parameter \(t=1-b^2/a^2\) inferred from the scale-free pair/triple statistic \(\eta\), not recovery from the full observed coordinates. There is unresolved historical-priority risk because the complete Lord article was inaccessible for comparison; its forward formulas could contain additional inverse remarks. No independent external validation has been performed.

## References
- N. Lord, “98.08 The moment of inertia of an elliptical wire,” *Mathematical Gazette* **98** (2014), 121–125. DOI: 10.1017/S0025557200000796; online date January 23, 2015.
- J. B. Tatum, “2.20: Ellipses and Ellipsoids,” *Classical Mechanics*, University of Victoria / Physics LibreTexts, section 2.20; full accessible web exposition of elliptical-hoop principal inertia integrals.
