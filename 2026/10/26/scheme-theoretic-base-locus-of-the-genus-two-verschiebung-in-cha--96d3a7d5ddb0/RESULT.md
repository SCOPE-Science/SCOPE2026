# Scheme-theoretic base locus of the genus-two Verschiebung in characteristic two

## Finding

For an ordinary smooth genus-two curve \(X\) over an algebraically closed field \(k\) of characteristic \(2\), the scheme-theoretic base locus of the Frobenius-pullback (Verschiebung) map \(V:\mathcal M_{X_1}\dashrightarrow\mathcal M_X\) on moduli spaces of semistable rank-two bundles with trivial determinant is supported at \((1:1:1:1)\) in theta coordinates and has local ring \(k[a,b]/(a^2,b^2)\); in particular, it is a length-\(4\) local complete intersection with Hilbert function \((1,2,1)\).

## Assumptions and scope

Let \(k\) be algebraically closed of characteristic \(2\), and let \(X/k\) be a smooth ordinary curve of genus \(2\). Write \(X_1\) for the Frobenius twist and \(\mathcal M_X\) for the coarse moduli space of semistable rank-two vector bundles with trivial determinant. In genus two, the theta-coordinate identification gives \(\mathcal M_X\cong\mathbb P^3\). The claim concerns the scheme cut out by the four coordinate quadrics defining the Frobenius-pullback rational map, not merely the set of bundles whose pullbacks are unstable.

For an ordinary genus-two curve in characteristic two, the no-vanishing-theta-null condition used in the coordinate construction holds; the constants multiplying the four quadrics are nonzero and do not change their generated ideal.

## Proof

Use theta coordinates \(x_{00},x_{01},x_{10},x_{11}\). Up to nonzero scalar factors, the four coordinate quadrics are

\[
P_0=x_{00}^2+x_{01}^2+x_{10}^2+x_{11}^2,
\]
\[
P_{01}=x_{00}x_{01}+x_{10}x_{11},\quad
P_{10}=x_{00}x_{10}+x_{01}x_{11},\quad
P_{11}=x_{00}x_{11}+x_{01}x_{10}.
\]

Their common projective zero is unique. Indeed, in characteristic two, \(P_0=(x_{00}+x_{01}+x_{10}+x_{11})^2\), so at a geometric zero the sum of the four coordinates is zero. Adding the equations \(P_{01}=P_{10}=0\) gives \((x_{01}+x_{10})^2=0\); adding \(P_{01}=P_{11}=0\) gives \((x_{00}+x_{10})^2=0\). Over a field these imply \(x_{00}=x_{01}=x_{10}\), and the sum relation then gives \(x_{11}=x_{00}\). The common zero is therefore \((1:1:1:1)\).

Work on the affine chart \(x_{00}=1\) around this point and put \(x_{01}=1+a\), \(x_{10}=1+b\), \(x_{11}=1+c\), and \(s=a+b+c\). The base ideal becomes

\[
J=(s^2,\ s+bc,\ s+ac,\ s+ab)\subset k[a,b,c]_{(a,b,c)}.
\]

In the quotient, the last three relations give \(s=ab=ac=bc\). Multiplying \(s=ab\) by \(a\), and using \(ab=ac\), yields \(a^2=a^2b\); since \(1+b\) is a unit in the local ring, \(a^2=0\). The same argument gives \(b^2=c^2=0\). From \(s=ab\) we then obtain \(c=a+b+ab\). Conversely, these relations imply all four generators of \(J\) vanish. Thus the local ideal is

\[
J=(c+a+b+ab,\ a^2,\ b^2),
\]

and the local ring of the base scheme is isomorphic to \(k[a,b]/(a^2,b^2)\). Its basis is \(1,a,b,ab\), so its length is \(4\). Its maximal ideal has successive graded dimensions \(1,2,1\) and cube zero. The displayed three generators form a regular sequence in the three-dimensional affine chart, proving the local-complete-intersection assertion.

## Verification

The local-ideal reduction is explicit above. The accompanying dependency-free checker verifies the four quadratic relations in the quotient algebra \(k[a,b]/(a^2,b^2)\); it is a finite consistency check, while the proof establishes the isomorphism and length. The result is restricted to ordinary genus-two curves in characteristic two.

## Relationship to prior work

Laszlo and Pauly give the quadratic coordinate formulas and identify the unique geometric base point for the ordinary characteristic-two genus-two case, but do not state its local Artin ring. Lange and Pauly compute the scheme-theoretic base locus as a local complete intersection for genus two in characteristic \(p>2\); their theorem excludes \(p=2\). Osserman's published abstract likewise states its genus-two degree result for \(p>2\). Laszlo and Pauly's later treatment of characteristic two addresses a nonordinary genus-two case, along with characteristic three, rather than this ordinary characteristic-two local scheme. The present claim supplies the local scheme type in the excluded ordinary characteristic-two case; the length agrees with the numerical value obtained by substituting \(p=2\) into the formula stated under the stricter \(p>2\) hypothesis, but that substitution alone is not a proof.

## Limitations

The statement does not cover nonordinary curves in characteristic two, curves of other genera, or the case of odd characteristic. It identifies the scheme defined by the displayed coordinate ideal; no independent audit has been performed. A full-text comparison with Osserman's article was unavailable, so that source remains a limited-access priority risk.

## References

1. Y. Laszlo and C. Pauly, *The action of the Frobenius map on rank 2 vector bundles in characteristic 2*, arXiv:math/0005044 (first public version 2000-05-04), especially Proposition 3.1 and Proposition 6.1.
2. Y. Laszlo and C. Pauly, *The Frobenius map, rank 2 vector bundles and Kummer's quartic surface in characteristic 2 and 3*, arXiv:math/0203175 (first public version 2002-03-18).
3. H. Lange and C. Pauly, *On Frobenius-destabilized rank-2 vector bundles over curves*, arXiv:math/0309456 (first public version 2003-09-29), published in *Commentarii Mathematici Helvetici* 83 (2008), 179–209.
4. B. Osserman, *The generalized Verschiebung map for curves of genus 2*, *Mathematische Annalen* 336 (2006), 963–986, DOI 10.1007/s00208-006-0026-6.
