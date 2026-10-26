# A unibranch \(2,7\) cusp on the characteristic-seven Klein quartic

## Finding
Let \(C\) be the special fiber in characteristic \(7\) of the classical Klein plane quartic, with its displayed integral model:
\[
C:\quad X^3Y+Y^3Z+Z^3X=0\quad\subset\mathbf P^2_{\mathbf F_7}.
\]
The curve is geometrically integral and has exactly one geometric singularity, \(P=[1:2:4]\). This is a unibranch cusp of Puiseux semigroup \(\langle2,7\rangle\), with \(\delta_P=3\). Its normalization is \(\mathbf P^1_{\mathbf F_7}\), and for every integer \(m\ge1\),
\[
\#C(\mathbf F_{7^m})=7^m+1,\qquad Z(C/\mathbf F_7,T)=\frac1{(1-T)(1-7T)}.
\]
This computes the point counts of the *singular displayed model*, not the potentially good reduction of a different integral or stable model.

## Assumptions and scope
Everything is over \(k=\overline{\mathbf F}_7\) for geometric claims, and over \(\mathbf F_7\) for rationality. The equation and projective coordinates are fixed. The arithmetic genus of a geometrically integral plane quartic is \(3\). The normalization is the unique smooth projective curve finite and birational over \(C\).

## Proof
Write \(F=X^3Y+Y^3Z+Z^3X\). The three partial derivatives in characteristic \(7\) are
\[
F_X=3X^2Y+Z^3,\quad F_Y=X^3+3Y^2Z,\quad F_Z=Y^3+3Z^2X.
\]
No projective common zero of the derivatives has a zero coordinate: if any of \(X,Y,Z\) is zero then the three equations force them all to vanish. Scale \(X=1\). From \(F_Y=0\), \(Z=2/Y^2\). From \(F_X=0\), \(3Y^7+1=0\), i.e. \(Y^7=2\). Frobenius is injective on \(k\), so \(Y=2\) and \(Z=4\). Direct substitution shows \(F(P)=F_X(P)=F_Y(P)=F_Z(P)=0\). Thus \(P\) is the only geometric singular point.

On the chart \(X=1\) put \(Y=2+u\) and
\[
Z=4+3u+3u^2+5u^3+h.
\]
Expanding modulo \(7\) gives the exact local equation
\[
 h^3+(u^3+2u^2+2u-2)h^2+(-2u^6-u^5-2u^4)h-u^9+u^8+3u^7=0.
\]
The \(h^2\)-coefficient is a unit in \(k[[u]]\); the \(h\)-coefficient has order \(4\) and the constant coefficient has order \(7\). The Weierstrass preparation theorem writes the left side as a unit times a monic quadratic \(h^2+a(u)h+b(u)\), where \(\operatorname{ord}_u a\ge4\) and \(\operatorname{ord}_u b=7\). Because \(2\) is invertible, completing the square gives \(v^2=u^7w(u)\) with \(w(0)\ne0\). Taking a formal square root of the unit \(w(u)\) gives an analytic equation \(v^2=u^7\). This is one geometric branch with numerical semigroup \(\langle2,7\rangle\) and delta invariant \((2-1)(7-1)/2=3\).

The curve is reduced at \(P\), since the completed local equation defines an integral domain; it is reduced everywhere else because it is smooth there. Any two distinct positive-degree projective components would meet by Bezout, and their meeting would produce a singular point with at least two branches. The only singularity is unibranch, so \(C\) is geometrically integral. The genus formula gives \(g(\widetilde C)=3-3=0\). The unique point of the normalization above \(P\) is \(\mathbf F_7\)-rational (uniqueness and geometric rationality). Consequently the genus-zero normalization is \(\mathbf P^1_{\mathbf F_7}\).

Normalization is an isomorphism off \(P\), and exactly one geometric point lies above \(P\). Therefore normalization is bijective on the points of every finite extension \(\mathbf F_{7^m}\), yielding the point-count formula for all \(m\ge1\) and its stated zeta function.

## Verification
The supplied Python 3 script `verify.py` uses exact finite-field arithmetic and independently enumerates all projective points and singularities over \(\mathbf F_7\) and \(\mathbf F_{49}\). Running `python3 verify.py` yields `FIELD 7 POINTS 8 EXPECTED 8 SING [(1, 2, 4)]`, `FIELD 49 POINTS 50 EXPECTED 50 SING [(1, 2, 4)]`, and `VERIFY_OK`. The computations corroborate, but do not replace, the proof of the uniform formula.

## Relationship to prior work
Dolgachev and Martin state that the classical Klein plane quartic becomes singular in characteristic \(7\), in their treatment of automorphisms of del Pezzo surfaces (Lemma 4.5 and Remark 5.7). Their cited result does not give the local analytic type, normalization, and every-extension point counts asserted here. Elkies discusses characteristic-seven arithmetic of the Klein quartic in a broader setting; full access to that relevant paper was unavailable for comparison. The literature on potentially good or hyperelliptic stable reduction addresses a different model and must not be mistaken for a point count on this naive plane special fiber.

## Limitations
This is the fixed coordinate model reduced modulo \(7\); no assertion is made about the stable reduction of the smooth generic fiber or models after ramified base change. The singularity is described by its completed geometric local ring, not by a claim of characteristic-independent ADE classification. Independent validation has not been performed. A full comparison with Elkies's 1999 treatment is still a literature risk.

## References
- I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170 (first publicly posted 2023-03-28), Section 4.2 and Remark 5.7, https://arxiv.org/html/2303.16170v2.
- N. D. Elkies, *The Klein quartic in number theory*, in *The Eightfold Way* (1999), pp. 51–102, https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b.
- R. van Bommel, J. Docking, R. Lercier and E. Lorenzo García, *Reduction of plane quartics and Dixmier–Ohno invariants*, arXiv:2401.13902 (2024), https://arxiv.org/abs/2401.13902.
