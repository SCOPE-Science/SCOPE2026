# Exact directional width law of the cube and its first spherical-cap transition

## Finding

Let \(d\ge3\) be an integer and \(U\) a direction distributed uniformly with respect to surface measure on \(S^{d-1}\). The length of the orthogonal projection of the unit-edge cube \(Q_d=[-1/2,1/2]^d\) onto the line spanned by \(U\) is \(W_d=\sum_{i=1}^d|U_i|\). Put \(H_d(s)=\mathbb P\{W_d\ge s\}\), whose support lies in \([1,\sqrt d]\). Write \(\mathcal I_z(a,b)\) for the regularized incomplete beta function.

**All dimensions, exactly above the first face crossing.** For every integer \(d\ge3\) and \(\sqrt{d-1}\le s\le\sqrt d\),
\[
H_d(s)=2^{d-1}\mathcal I_{1-s^2/d}\left(\frac{d-1}{2},\frac12\right).
\]
The expression on the right defines the *unrestricted diagonal-cap estimate* \(H_d^{\mathrm{cap}}(s)\) also for lower values of \(s\). At the sharp first transition \(q=\sqrt{d-1}\), its overcount has the asymptotic law
\[
H_d(q-\varepsilon)-H_d^{\mathrm{cap}}(q-\varepsilon)
=-\frac{2^d}{\pi}\left(\frac{2}{q}\right)^{(d-2)/2}
\varepsilon^{d/2}+o(\varepsilon^{d/2}),\qquad \varepsilon\downarrow0.
\]
Moreover, if \(\sqrt{d-2}<s<\sqrt{d-1}\), the correction is *exactly* the sum of the \(d\) individually excluded spherical segments within each octant; no pairwise excluded-segment overlap is possible in this interval.

**Complete three-dimensional distribution.** For \(1<s<\sqrt2\) define
\[
\alpha(s)=\arccos\left(\frac{s}{\sqrt{2(3-s^2)}}\right),\qquad
\gamma(s)=\arccos\left(\frac1{\sqrt{3-s^2}}\right).
\]
Then the full survival function of the unit cube is
\[
H_3(s)=\begin{cases}
1,&s\le1,\\
4\left(1-\frac{s}{\sqrt3}\right)-\frac{12}{\pi}
\left(\gamma(s)-\frac{s}{\sqrt3}\alpha(s)\right),&1<s<\sqrt2,\\
4\left(1-\frac{s}{\sqrt3}\right),&\sqrt2\le s<\sqrt3,\\
0,&s\ge\sqrt3.
\end{cases}
\]
Its probability density, extended by zero outside its support, is
\[
f_3(s)=\begin{cases}
\frac4{\sqrt3}\left(1-\frac3\pi\alpha(s)\right),&1<s<\sqrt2,\\
\frac4{\sqrt3},&\sqrt2<s<\sqrt3.
\end{cases}
\]
Thus the **upper tail is exactly uniform** on \([\sqrt2,\sqrt3]\) conditional on exceeding \(\sqrt2\). The density is continuous at \(\sqrt2\), but its derivative diverges from below, with the threshold correction of order \((\sqrt2-s)^{3/2}\).

## Assumptions and scope

The cube's edge length is one, the width is a *one-dimensional* orthogonal projection length (not two-dimensional shadow area), and the direction has normalized rotation-invariant spherical law. Boundaries of orthants, having surface measure zero, do not affect the distribution. The arbitrary-dimensional statement concerns the first transition and the exact high-width tail; it does not provide the entire lower-tail distribution for every \(d>3\). The stated density is a property only of dimension three. No statistical independence among the absolute spherical coordinates is assumed.

For convenience, the surface area of the unit \(k\)-sphere is \(|S^k|=2\pi^{(k+1)/2}/\Gamma((k+1)/2)\). The regularized incomplete beta function is \(\mathcal I_z(a,b)=B_z(a,b)/B(a,b)\) for \(0\le z\le1\).

## Proof

**1. Diagonal spherical caps.** Let \(v=(1,\dots,1)/\sqrt d\). In the positive orthant the width is \(W_d=\sqrt d\langle U,v\rangle\). Its superlevel set is the cap \(\langle U,v\rangle\ge s/\sqrt d\), intersected with the orthant. The \(2^d\) orthants contribute equally. Set \(\theta=\arccos(s/\sqrt d)\). The spherical distance of the cap's center \(v\) from each coordinate face \(U_i=0\) is \(\delta=\arcsin(1/\sqrt d)\). Thus the cap lies entirely inside its orthant precisely when \(\theta\le\delta\), equivalently \(s\ge\sqrt{d-1}\). For a uniform spherical direction, the unrestricted cap fraction is
\[
\frac{|S^{d-2}|}{|S^{d-1}|}\int_0^\theta(\sin t)^{d-2}\,dt
=\frac12\mathcal I_{\sin^2\theta}\left(\frac{d-1}2,\frac12\right).
\]
Multiplication by \(2^d\) proves the exact high-width expression.

**2. Why the first face corrections have no overlaps.** If two specified coordinates are nonpositive, then \(\sum_iU_i\le\sum_{j\notin\{i,k\}}U_j\le\sqrt{d-2}\), by Cauchy--Schwarz. Therefore the parts of an unrestricted diagonal cap that lie beyond two different coordinate faces have empty intersection for \(s>\sqrt{d-2}\). The inclusion--exclusion formula consequently truncates exactly after its one-face terms on \(\sqrt{d-2}<s<\sqrt{d-1}\).

**3. Sharp first-crossing coefficient.** Let \(q=\sqrt{d-1}\), \(s=q-\varepsilon\), and fix one face. Parameterize the sphere by \(x=U_1<0\) and \((U_2,\dots,U_d)=\sqrt{1-x^2}\,\omega\), where \(\omega\in S^{d-2}\). The face-excess region is
\[
x+q\sqrt{1-x^2}\langle\omega,v'\rangle\ge q-\varepsilon,
\qquad v'=(1,\dots,1)/q.
\]
Here \(x\in[-\varepsilon+O(\varepsilon^2),0]\). Its angular aperture \(\phi(x,\varepsilon)\), centered at \(v'\), obeys uniformly on the shrinking interval
\[
\phi(x,\varepsilon)^2=\frac2q(\varepsilon+x)+O(\varepsilon^2)
\]
(the error may be interpreted via the nonnegative positive-part near the lower endpoint). Since the surface element is \((1-x^2)^{(d-3)/2}\,dx\,d\sigma_{d-2}(\omega)\), integration of the small \((d-2)\)-dimensional spherical cap gives the **one-face segment area**
\[
\operatorname{Seg}_d(\varepsilon)
=\frac{|S^{d-3}|}{d-2}\left(\frac2q\right)^{(d-2)/2}
\frac2d\varepsilon^{d/2}+o(\varepsilon^{d/2}).
\]
This follows rigorously by rescaling \(x=\varepsilon y\), using the expansion \(\int_0^z\sin^{d-3}t\,dt=z^{d-2}/(d-2)+O(z^d)\), and dominated convergence over \(-1\le y\le0\). The total probability correction is \(-2^d d\operatorname{Seg}_d(\varepsilon)/|S^{d-1}|\). Finally \(|S^{d-3}|/|S^{d-1}|=(d-2)/(2\pi)\), yielding precisely the announced constant. Since it is nonzero, \(s=q\) is a genuine transition in the analytic form of the distribution.

**4. Exact spherical segments for three dimensions.** For \(d=3\), \(\delta=\arcsin(1/\sqrt3)\) and \(\theta=\arccos(s/\sqrt3)\). A spherical circular cap of radius \(\theta\) cut beyond a great-circle face at distance \(\delta\) has segment area
\[
2\left[\arccos\left(\frac{\sin\delta}{\sin\theta}\right)
-\cos\theta\,\arccos\left(\frac{\tan\delta}{\tan\theta}\right)\right].
\]
To derive this, observe that the cap boundary and the great circle intersect in two points. Integrating the longitude arc lengths around the cap axis, or equivalently applying the spherical Gauss--Bonnet formula to the resulting circular segment, gives the two corner angles \(\arccos(\sin\delta/\sin\theta)\) and \(\arccos(\tan\delta/\tan\theta)\), with the boundary geodesic-curvature contribution \(-2\cos\theta\) times the latter. The formula vanishes at tangency \(\theta=\delta\) and approaches the correct hemisphere segment area at \(\theta=\pi/2\). Substituting \(s\) gives \(2(\gamma(s)-s\alpha(s)/\sqrt3)\).

There are three pairwise disjoint such face segments per octant for \(1<s<\sqrt2\). The cap's area is \(2\pi(1-s/\sqrt3)\), so multiplication by \(8/(4\pi)\) yields the asserted complete survival function. Direct differentiation, using
\[
\frac{d}{ds}\left[\gamma(s)-\frac{s}{\sqrt3}\alpha(s)\right]
=-\frac1{\sqrt3}\alpha(s),
\]
produces the stated density. Endpoint substitution proves normalization and continuity, including \(H_3(1)=1\) and \(H_3(\sqrt3)=0\). On the upper interval the density is constant; differentiating the explicit lower formula shows the sharp non-smooth transition. This completes the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. It implements the closed-form three-dimensional survival function and density, computes a separate one-dimensional polar integral using the octant geometry, checks near-tangency coefficients in dimensions three through five using nested angular quadrature, checks spherical caps in dimensions three, four, five and seven, and compares with generated uniform spherical directions. Its expected success marker is `VERIFY_OK`. These finite checks test the formulas but do not replace the preceding proof.

As independent normalization checks, \(\mathbb E W_3=3/2\) and \(\mathbb E W_3^2=1+4/\pi\), agreeing with the earlier moment calculations in the cited literature. No empirical assertion is used to establish a universal identity.

## Relationship to prior work

Kabluchko, Litvak, and Zaporozhets (arXiv:1511.08479, first circulated November 2015; historical MSC2010 primary 52A23) obtained general higher-moment identities and high-dimensional distributional limits for projection lengths of regular polytopes, including the cube. Those identities determine the distribution implicitly because its support is compact. They are stronger concerning availability of *all moments*, but their inspected formulas do not give the elementary piecewise three-dimensional density or the sharp first coordinate-face correction. The present calculation instead explicitly inverts the geometric superlevel event, for the full three-dimensional law and the first high-dimensional transition.

Finch (arXiv:1110.0671, first circulated October 2011) calculated the cube's mean-square width and discussed the undetermined density. Paouris, Pivovarov, and Zinn (arXiv:1210.7012) developed asymptotic Gaussian results for random projections of high-dimensional cubes, rather than the fixed three-dimensional elementary density. These works and other spherical-cap inclusion--exclusion principles motivate, but are not claimed to be rediscovered by, the present result.

## Limitations

The general-dimensional result stops at the first cap-overlap transition and does not classify the progressively overlapping lower tails in dimensions at least four. The formula is for rotation-invariant directions and unit-edge cubes; rectangular boxes require separate parameters. Finite code checks cannot certify the identities independently of their mathematical proofs. All preexisting moment results are acknowledged; a previously unnoticed equivalent closed-density derivation in broader literature remains possible. No independent external scientific audit has been performed.

## References

1. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (first public version November 26, 2015), especially the higher-moment formulas and distributional limit results; https://arxiv.org/abs/1511.08479.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671 (first public version October 4, 2011); https://arxiv.org/abs/1110.0671.
3. G. Paouris, P. Pivovarov, J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012 (first public version October 25, 2012); https://arxiv.org/abs/1210.7012.
