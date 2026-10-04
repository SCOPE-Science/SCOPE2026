# Quasismooth anticanonical sections on the canonical non-terminal two-heavy boundary
## Finding
For every integer \(r\ge 2\), let \(X=\mathbb P(1^r,a,b)\) with \(1\le a\le b\), and suppose \(X\) is canonical but not terminal. A general anticanonical hypersurface of degree \(D=r+a+b\) is quasismooth if and only if \((a,b)=(c,c+r)\) for a positive divisor \(c\) of \(2r\) or \(2r-1\), or \((a,b)=(r,r)\), or \((a,b)=(2r-1,3r-2)\). Consequently exactly \(\tau(2r)+\tau(2r-1)+1\) of the \(3r\) canonical non-terminal boundary spaces admit a quasismooth anticanonical hypersurface, where \(\tau(n)\) is the number of positive divisors of \(n\).

## Assumptions and scope
Fix an integer \(r\ge 2\). Write \(X=\mathbb P(1^r,a,b)\) with \(1\le a\le b\), put \(d=b-a\), and take the complete anticanonical linear system, whose weighted degree is \(D=r+a+b\). The statement concerns ordinary well-formed weighted projective spaces and quasismooth hypersurfaces in the standard affine-cone sense.

The canonical-but-not-terminal locus is the boundary of the two strict inequalities governing terminality: it is the union of \(d=r\) and \(a=r+d\), subject to \(0\le d\le r\) and \(a\le r+d\). These two boundary segments contain exactly \(3r\) weight pairs.

## Proof
Use the coordinate-stratum quasismoothness criterion for the complete degree-\(D\) monomial system. Any coordinate subset containing one of the weight-one variables automatically has a supported monomial, namely a pure power of that variable. Thus only subsets supported on the two heavy coordinates can be nonautomatic.

First take the boundary segment \(d=r\), so \(b=a+r\). Then
\[
D=r+a+b=2b.
\]
Hence the monomial \(z^2\), where \(z\) has weight \(b\), is present. It handles the \(z\)-axis and the two-heavy coordinate stratum. The only remaining condition is the singleton stratum of the weight-\(a\) coordinate \(y\). The quasismoothness criterion says that one needs a monomial of one of the forms \(y^m\), \(x_i y^m\), or \(z y^m\). Their degree equations are respectively
\[
D=ma,\qquad D=ma+1,\qquad D=ma+b.
\]
Because \(D=2a+2r\), these are equivalent to
\[
a\mid 2r,\qquad a\mid (2r-1),\qquad a\mid r.
\]
The third condition is contained in the first. Therefore this boundary segment contributes exactly those pairs \((a,a+r)\) for which \(a\mid 2r\) or \(a\mid(2r-1)\). The two divisor sets intersect only at \(a=1\), so their number is \(	au(2r)+	au(2r-1)-1\).

Now take the other boundary segment \(a=r+d\), so \(b=r+2d\) with \(0\le d\le r\). Then
\[
D=r+a+b=3a,
\]
so \(y^3\) is present and handles the \(y\)-axis and the two-heavy stratum. The only remaining condition is at the weight-\(b\) coordinate. The analogous three degree equations reduce to
\[
b\mid(r-d),\qquad b\mid(r-d-1),\qquad b\mid r.
\]
Since \(b=r+2d\), these can occur only for \(d=0\), \(d=r-1\), or \(d=r\), giving respectively
\[
(r,r),\qquad (2r-1,3r-2),\qquad (2r,3r).
\]
The last pair is already on the first boundary segment, corresponding to the divisor \(2r\mid 2r\). Adding the two genuinely new pairs gives
\[
	au(2r)+	au(2r-1)+1.
\]
This also proves necessity, because if the relevant singleton condition fails then the coordinate-stratum criterion says that every degree-\(D\) polynomial has a singular punctured affine cone along a nonempty locus.

## Verification
The accompanying exact-arithmetic script enumerates every canonical non-terminal pair from the two inequality criteria for each \(2\le r\le150\). It independently applies the singleton monomial congruence tests above, compares the result with the explicit divisor description, verifies that the whole boundary has \(3r\) pairs, and checks the divisor-count formula. It prints `VERIFY_OK r=2..150`.

Weighted adjunction is compatible with the construction: \(D\) equals the sum of the ambient weights. Thus a well-formed quasismooth member has trivial canonical class. The pure heavy monomial on each boundary segment also prevents the entire heavy coordinate line from being forced into the hypersurface.

## Relationship to prior work
Chen, Chen, and Chen give the standard quasismooth weighted-complete-intersection framework, and the coordinate-stratum monomial criterion goes back to Iano-Fletcher. Kasprzyk develops the canonical and terminal weighted-projective-space criteria used to identify the two-heavy boundary. The present statement combines these ingredients on the all-dimensional family \(\mathbb P(1^r,a,b)\) and reduces the complete boundary problem to two divisor sets plus two exceptional points. Searches for the exact divisor formula and its equivalent boundary classification did not locate a prior statement.

## Limitations
The result is restricted to hypersurfaces in ordinary spaces \(\mathbb P(1^r,a,b)\). It does not classify higher-codimension weighted complete intersections, fake weighted projective spaces, or anticanonical hypersurfaces away from the canonical non-terminal boundary. The finite computation is a regression check, not a substitute for the all-dimensional proof.

## References
J.-J. Chen, J. A. Chen, and M. Chen, *On Quasismooth Weighted Complete Intersections*, arXiv:0908.1439 (first posted 2009-08-11).

A. M. Kasprzyk, *Classifying Terminal Weighted Projective Space*, arXiv:1304.3029 (first posted 2013-04-10).

A. R. Iano-Fletcher, *Working with Weighted Complete Intersections*, in *Explicit Birational Geometry of 3-Folds*, London Mathematical Society Lecture Note Series 281 (2000).
