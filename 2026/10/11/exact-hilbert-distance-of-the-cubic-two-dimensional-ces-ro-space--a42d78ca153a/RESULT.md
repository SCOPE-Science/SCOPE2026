# Exact Hilbert distance of the cubic two-dimensional Cesàro space
## Finding
For the real Cesàro plane \(X=\mathrm{ces}_3^{(2)}=(\mathbb R^2,N)\), with
\[
N(u,v)=\left(|u|^3+\left(\frac{|u|+|v|}{2}\right)^3\right)^{1/3},
\]
put \(a=9^{2/3}\) and let \(\tau>0\) be the unique solution of
\[
a(1+\tau)^2=\tau\bigl((1+\tau)^2+8\bigr).
\]
Then the exact Euclidean Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)
=\left(\frac{(8+(1+\tau)^3)^{2/3}}{a+\tau^2}\right)^{1/2}
=1.13999212435921634517891658558\ldots.
\]
More precisely, the explicit Hilbert norm
\[
H(u,v)=\frac12\sqrt{a u^2+v^2}
\]
satisfies the globally sharp two-sided estimate
\[
H(z)\le N(z)\le d_{\mathrm{BM}}(X,\ell_2^2)H(z)\qquad(z\in\mathbb R^2).
\]
No other (possibly tilted) positive definite quadratic form achieves a smaller distortion. The upper comparison is sharp at \((\pm1,\pm\tau)\); the lower comparison is sharp precisely on the two coordinate axes. Consequently the universal inequality \(C_{\mathrm{NJ}}(X)\le d_{\mathrm{BM}}(X,\ell_2^2)^2\) is sharp for this coordinate-asymmetric absolute norm.

## Assumptions and scope
The scalar field is real. The two-dimensional Cesàro norm is
\[
N(u,v)=\left(|u|^3+\left(\frac{|u|+|v|}{2}\right)^3\right)^{1/3}.
\]
The Euclidean Banach--Mazur distance is the infimum of \(\sqrt{\beta/\alpha}\) over all positive definite quadratic forms \(Q\) and constants \(0<\alpha\le\beta\) with \(\alpha Q(z)\le N(z)^2\le\beta Q(z)\) for every \(z\). The candidate quadratic form is
\[
H(u,v)^2=\frac{a u^2+v^2}{4},\qquad a=9^{2/3}=3^{4/3}.
\]

## Proof
**Lower comparison.** By absolute symmetry and homogeneity, for nonzero first coordinate it suffices to set \(z=(1,t)\) with \(t\ge0\). Then
\[
4N(1,t)^2=\bigl(8+(1+t)^3\bigr)^{2/3},\qquad 4H(1,t)^2=a+t^2.
\]
The required inequality \(H(1,t)^2\le N(1,t)^2\), after cubing, is
\[
\bigl(9+3t+3t^2+t^3\bigr)^2-(a+t^2)^3\ge0.
\]
Using \(a^3=81\), its left side is exactly
\[
54t+(63-3a^2)t^2+36t^3+(15-3a)t^4+6t^5.
\]
All coefficients are strictly positive: \(a<5\), since \(81<125\), and \(a^2<21\), since \(6561<9261\). Thus \(H(1,t)\le N(1,t)\), with equality only at \(t=0\). At the other axis, \(N(0,v)=|v|/2=H(0,v)\). This proves \(H\le N\), with equality exactly on the coordinate axes.

**Upper comparison.** For \(t\ge0\), define
\[
R(t)=\frac{N(1,t)^2}{H(1,t)^2}
=\frac{\bigl(8+(1+t)^3\bigr)^{2/3}}{a+t^2}.
\]
Its derivative has the sign of
\[
a-\phi(t),\qquad \phi(t)=t\left(1+\frac8{(1+t)^2}\right).
\]
Indeed this follows by differentiating \(\log R\) and clearing positive denominators. Direct differentiation gives
\[
\phi'(t)=1+\frac{8(1-t)}{(1+t)^3}\ge\frac{19}{27}>0
\qquad(t\ge0),
\]
with equality in the bound at \(t=2\). Since \(\phi(0)=0\) and \(\phi(t)\to\infty\), there is a unique \(\tau>0\) with \(\phi(\tau)=a\). The ratio \(R\) rises strictly on \([0,\tau]\), then falls strictly for \(t>\tau\). Its endpoint values are \(R(0)=1\) and \(\lim_{t\to\infty}R(t)=1\). Therefore \(R(\tau)\) is the unique maximum and
\[
H(z)\le N(z)\le\sqrt{R(\tau)}H(z)
\]
for every \(z\), with upper equality exactly on the four rays \((\pm1,\pm\tau)\).

**Optimality among every Euclidean pullback.** Let any positive quadratic form \(Q\) and \(0<\alpha\le\beta\) satisfy \(\alpha Q(z)\le N(z)^2\le\beta Q(z)\). Set \(x=(1,0)\), \(y=(0,\tau)\). Since the Cesàro norm is absolute, \(N(x+y)=N(x-y)=N(1,\tau)\). The quadratic parallelogram law and the sandwich yield
\[
2N(1,\tau)^2\le\beta\bigl(Q(x+y)+Q(x-y)\bigr)
=2\beta\bigl(Q(x)+Q(y)\bigr)
\le \frac{2\beta}{\alpha}\bigl(N(x)^2+N(y)^2\bigr).
\]
But \(N(x)^2=a/4\), \(N(y)^2=\tau^2/4\), and \(N(1,\tau)^2=\bigl(8+(1+\tau)^3\bigr)^{2/3}/4\). Hence
\[
\frac{\beta}{\alpha}\ge R(\tau).
\]
Our explicit \(H\) attains equality in this universal bound; consequently the Euclidean Banach--Mazur distance is exactly \(\sqrt{R(\tau)}\). This argument considers arbitrary tilted ellipses, not merely diagonal ones.

## Verification
The stationarity equation is \(a(1+\tau)^2=\tau((1+\tau)^2+8)\), and \(\phi\) is strictly increasing, so there is no ambiguous root selection. With 60-digit arithmetic one obtains
\[
\tau=2.7667398800787011390685370499587174985707872620\ldots,
\]
\[
R(\tau)=1.29958204360103898476109693949458365272517\ldots,
\]
and
\[
\sqrt{R(\tau)}=1.13999212435921634517891658558988654198026\ldots.
\]
These decimals merely check exact definitions, and are not used to prove the inequalities or global optimality. All polynomial coefficients and derivative signs are explicit.

## Relationship to prior work
Maligranda, Petrot, and Suantai study the finite-dimensional Cesàro norms and their James constants; their 2006 full text defines the same norm but does not calculate an Euclidean Banach--Mazur distance. Saejung's later two-dimensional Cesàro calculations concern James and von Neumann--Jordan constants, principally for lower exponents, rather than optimal ellipses. Zuo's open 2012 Ptolemy paper treats absolute normalized planes and gives a concrete Cesàro example at exponent two; its complete searchable body does not establish this cubic Banach--Mazur value.

The known cubic Cesàro Ptolemy and von Neumann--Jordan constants take the same scalar value \(R(\tau)\). That equality does not automatically imply a sharp Euclidean upper sandwich: \(C_{\mathrm{NJ}}\le d_{\mathrm{BM}}^2\) is generally only a lower bound. The new contribution is the explicit matching global Hilbert sandwich and a proof that no off-axis ellipse is better. An indexed exact Euclidean distance for the distinct quadratic Cesàro plane does not cover the present cubic norm.

## Limitations
The theorem addresses the real two-coordinate Cesàro space with exponent three; it does not determine the Banach--Mazur distance for general Cesàro exponent or higher dimension. The claim gives an explicit sharp ellipsoid but makes no assertion that this optimal ellipsoid is unique. The complete body of Saejung's 2010 paper was not available in the checked route; its abstract indicates other invariants, but possible unexposed exact comparisons remain a bibliographic residual risk. The cited 2006 paper is used with its verified first online date; day-level dates are not extrapolated from later journal indexing.

## References
1. L. Maligranda, N. Petrot, and S. Suantai, “On the James constant and B-convexity of Cesàro and Cesàro--Orlicz sequence spaces,” *Journal of Mathematical Analysis and Applications* (2006), DOI 10.1016/j.jmaa.2006.02.085; first publicly online 2006-04-17.
2. S. Saejung, “Another look at Cesàro sequence spaces,” *Journal of Mathematical Analysis and Applications* (2010), DOI 10.1016/j.jmaa.2010.01.029.
3. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107; primary MSC 46B20.
