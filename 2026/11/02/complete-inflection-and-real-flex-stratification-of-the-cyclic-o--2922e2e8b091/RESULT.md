# Complete inflection and real-flex stratification of the cyclic octic pencil

## Finding
Let \(\lambda\in\mathbb C\setminus\{-2,2\}\), and let \(C_\lambda\subset\mathbb P^2_{\mathbb C}\) be the smooth octic
\[
F_\lambda(X,Y,Z)=Z^8+X^8+\lambda X^4Y^4+Y^8=0.
\]
Write \(Q_\lambda=X^8+\lambda X^4Y^4+Y^8\) and
\[
R_\lambda=6\lambda(X^8+Y^8)+(28-\lambda^2)X^4Y^4.
\]
Let \(B_\lambda\) be the reduced divisor on \(C_\lambda\) cut out by \(Z=0\), and \(A_\lambda\) the reduced divisor cut out by \(XY=0\). Thus \(\deg B_\lambda=8\) and \(\deg A_\lambda=16\), with disjoint supports. The **complete flex divisor** of the plane embedding—equivalently the ramification divisor of the complete linear series \(\mathcal O_{C_\lambda}(1)\)—has the scheme-theoretic expression
\[
\boxed{\operatorname{Flex}(C_\lambda)=6B_\lambda+2A_\lambda+\operatorname{div}_{C_\lambda}(R_\lambda).}
\]
Here a point where its multiplicity is \(w\) has tangent contact order exactly \(w+2\). The following cases exhaust all smooth members of the pencil:

1. **General parameter**, \(\lambda\notin\{0,-2,2,-14,14\}\): exactly eight points of tangent contact order eight, sixteen of contact order four, and sixty-four ordinary flexes of contact order three. There are \(88\) distinct flex points.
2. **Octahedral parameters**, \(\lambda=14\) or \(\lambda=-14\): exactly eight points of contact order eight and forty-eight of contact order four, with no ordinary flexes. There are \(56\) distinct flex points.
3. **Fermat parameter**, \(\lambda=0\): exactly twenty-four points of contact order eight and no other flexes.

In every case the weighted total is \(144=3\cdot8\cdot(8-2)\), as required for a smooth plane octic.

**Real refinement.** If \(\lambda\in\mathbb R\setminus\{-2,2\}\), then \(C_\lambda(\mathbb R)=\varnothing\) for \(\lambda>-2\). For \(\lambda<-2\), its real locus consists of exactly two ovals, and there are exactly four real flexes, all of contact order eight: two on each oval. In particular none of the residual ordinary or contact-four flexes is real.

## Assumptions and scope
Everything is over characteristic zero and concerns the indicated projective embedding, not arbitrary embeddings of the abstract curve. A flex is a smooth point where the tangent line has intersection multiplicity at least three; a hyperflex of order eight has tangent contact eight. The term *flex divisor* includes multiplicity equal to contact order minus two. Parameters \(\lambda=\pm2\) are excluded because the defining curve is singular. The assertion about real ovals concerns the real form given by the displayed homogeneous equation.

## Proof
**1. Smoothness and cyclic covering.** Set \(u=(X/Y)^4\) on the chart \(Y\ne0\). The degree-eight binary form factors through \(u^2+\lambda u+1\), whose discriminant is \(\lambda^2-4\). Neither coordinate direction is a zero. Thus \(Q_\lambda\) has eight simple projective zeros precisely when \(\lambda^2\ne4\). Since \(F_Z=8Z^7\), a singularity must lie on \(Z=0\) over a multiple zero of \(Q_\lambda\); therefore the curve is smooth for exactly the stated parameters. Projection \([X:Y:Z]\mapsto[X:Y]\) has degree eight, is unramified away from \(B_\lambda\), and has total ramification index eight at each of the eight points of \(B_\lambda\).

**2. Scheme-theoretic Hessian.** Taking second derivatives gives
\[
\det\bigl(F_{\lambda,ij}\bigr)_{i,j=X,Y,Z}
=6272X^2Y^2Z^6\bigl[6\lambda(X^8+Y^8)+(28-\lambda^2)X^4Y^4\bigr].
\]
In characteristic zero, the intersection of the projective Hessian with a smooth plane curve is precisely its flex divisor, with local multiplicity contact order minus two. Neither \(Z=0\) nor \(X=0\) nor \(Y=0\) is a component of the smooth curve. Their reduced restrictions are disjoint and have eight and sixteen distinct points respectively; for example \(X=0\) imposes \(Y^8+Z^8=0\). This proves the divisor identity, including its scheme structure and degree \(48+32+64=144\).

**3. The residual degree-eight form.** If \(\lambda\ne0\), the equation \(R_\lambda=0\) in \(u=(X/Y)^4\) is
\[
6\lambda u^2+(28-\lambda^2)u+6\lambda=0,
\]
with discriminant
\[
\Delta_R=(\lambda^2-4)(\lambda^2-196).
\]
The constant term is nonzero. At a zero of \(Q_\lambda\), reduction modulo \(u^2+\lambda u+1\) gives
\[
R_\lambda\equiv 7(4-\lambda^2)u\pmod{u^2+\lambda u+1},
\]
which does not vanish for a smooth parameter. Thus the residual support is disjoint from \(B_\lambda\); it is also disjoint from \(A_\lambda\) when \(\lambda\ne0\). If \(\lambda\notin\{0,\pm2,\pm14\}\), the two nonzero roots of the quadratic are distinct. Each has four distinct fourth roots, and each such base direction has eight distinct points above it. Therefore the residual divisor consists of \(64\) reduced points, each of flex weight one. Combining with the weights six on \(B_\lambda\) and two on \(A_\lambda\) proves the general count and contact orders.

At the exceptional values, direct factorization yields
\[
R_{14}=84(X^4-Y^4)^2,\qquad
R_{-14}=-84(X^4+Y^4)^2.
\]
Each quartic has four simple non-coordinate roots, so its inverse image consists of \(4\cdot8=32\) distinct points, each of residual weight two. Together with \(16\) points of \(A_\lambda\) already of weight two, this gives \(48\) contact-four flexes. At \(\lambda=0\), one has \(R_0=28X^4Y^4\), so the residual divisor equals \(4A_0\); accordingly the \(16\) axis points also have weight six. The eight branch points have weight six throughout. The three cases are exhaustive: only \(0\) changes the support on the coordinate axes, and only \(\pm14\) makes the residual quadratic discriminant zero on the smooth locus.

**4. Real topology and flexes.** For \(\lambda>-2\), the inequality
\[
X^8+\lambda X^4Y^4+Y^8=(X^4-Y^4)^2+(\lambda+2)X^4Y^4>0
\]
holds whenever \((X,Y)\ne(0,0)\); the point \([0:0:1]\) is not on the curve. Since \(Z^8\ge0\), there are no real points. For \(\lambda<-2\), the two roots of \(u^2+\lambda u+1\) are strictly positive. In the chart \(Y=1\), \(x^8+\lambda x^4+1\le0\) on exactly two compact disjoint real intervals, one with positive \(x\), the other with negative \(x\). Over each interval, the two real branches \(z=\pm(-x^8-\lambda x^4-1)^{1/8}\) meet smoothly at the two endpoints, giving exactly one oval. Neither the chart at \(Y=0\) nor the excluded axis directions contribute real points.

The four endpoints (two on each oval) are exactly the four real branch points in \(B_\lambda\). To exclude all further real flexes, put \(t=-\lambda>2\) and \(u=x^4\ge0\). Then
\[
R_\lambda=-6t(u^2+1)+(28-t^2)u
\le-(t^2+12t-28)u\le0.
\]
The inequality is strict for every \(u\ge0\): for \(u>0\), use \(t^2+12t-28=(t+14)(t-2)>0\), and at \(u=0\) the term \(-6t\) is strictly negative. Hence the residual divisor has no real points. The axis divisor has none because \(Q_\lambda\) is positive at the coordinate directions. The four real branch points are consequently all the real flexes, each of weight six and contact eight.

## Verification
The accompanying `verify_flex_pencil.py` uses only exact integer and rational arithmetic from the Python standard library. It constructs the entire homogeneous Hessian as a sparse polynomial in \(X,Y,Z,\lambda\) and compares coefficients with the claimed factorization. It also checks the exact discriminant factorization, reduction modulo the branch quadratic, both exceptional residual factorizations, the flex-weight sums across integer test parameters, and sample real-sign inequalities. Running `python3 verify_flex_pencil.py` gives `VERIFY_OK`. These finite parameter tests are supplementary; the symbolic identities and divisor argument above prove the full complex and real claims.

## Relationship to prior work
Badr and Harui (arXiv:2603.26180, first public March 27, 2026) classify automorphism groups for smooth plane curves with a unique outer Galois point, including the octahedral degree-eight form \(X^8+14X^4Y^4+Y^8\). Their result identifies the exceptional symmetry, but does not give the complete flex divisor or its two discriminant walls. The octahedral binary invariant and its relation to the octahedral six-vertex form already appear in classical invariant theory, as explained in Elkies's 2021 course notes. The standard Hessian-flex identity and the general arithmetic study of superelliptic inflection (Cotterill et al.) are also prior tools. The result here is the evaluated parameter-uniform divisor, its exact collision classification, and the real topology/flex law; no novelty is claimed for Hessians, binary covariants or generic inflection theory themselves.

## Limitations
The theorem does not describe the complete singularity scheme of the dual plane curve, other plane models, singular pencil parameters, or positive-characteristic analogues. No historical-priority claim is absolute: an older specialized Hessian or flex calculation using different names could imply part of the classification. The proof and checks reported here are not an independent external validation.

## References
1. E. Badr and T. Harui, *Smooth plane curves with a unique outer Galois point and their automorphism groups*, arXiv:2603.26180, initially submitted 2026-03-27; https://arxiv.org/html/2603.26180v2 .
2. E. Cotterill, I. Darago, C. Garay López, C. Han and T. Shaska, *Arithmetic inflection of superelliptic curves*, arXiv:2110.04813 (2021); https://arxiv.org/abs/2110.04813 .
3. N. Elkies, *Math 263x: Computational Techniques in Number Theory and Algebraic Geometry*, course notes (2021), octahedral invariant discussion; https://people.math.harvard.edu/~elkies/M263.21/index.html .
4. Standard Hessian–inflection correspondence for smooth plane curves in characteristic zero, used with local intersection multiplicity.
