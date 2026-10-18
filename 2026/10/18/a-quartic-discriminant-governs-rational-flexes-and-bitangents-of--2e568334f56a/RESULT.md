# A quartic discriminant governs rational flexes and bitangents of plane-filling curves

## Finding
For every odd prime power \(q\), let \(k\in\mathbf F_q\) be such that \(t^7+kt^3-1\) has no root in \(\mathbf F_q\). On the plane-filling curve \(C_{k,q}\) below, every rational point is smooth. Let \(F\) be the number of rational points whose rational tangent has local contact multiplicity three, and let \(B\) be the number of rational lines tangent at two distinct rational points. Define a quartic in the *dual* projective plane by
\[
D_k:\quad a^3b+b^3c+ac^3+k(b^4+abc^2)=0.
\]
Then
\[
F=\#D_k(\mathbf F_q),\qquad B=\frac{q^2+q+1-\#D_k(\mathbf F_q)}{2}.
\]
Indeed, the numbers of rational lines tangent to \(C_{k,q}\) at zero, one, and two distinct rational points are precisely \(B,F,B\), respectively, and there are no rational lines tangent at three rational points. If \(D_k\) is geometrically smooth, its genus is three, giving the nontrivial uniform estimates
\[
|F-(q+1)|\le6\sqrt q,\qquad |B-q^2/2|\le3\sqrt q.
\]
This last implication is *conditional on smoothness of \(D_k\)*; the exact counting formulas require no such additional condition.

## Assumptions and scope
Write \(\mathbf F_q\) for a field of odd cardinality \(q\). The curve is the degree-\(q+3\) plane curve
\[
C_{k,q}:\ X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0.
\]
Every point of \(\mathbf P^2(\mathbf F_q)\) lies on \(C_{k,q}\). The cited source proves that the condition on \(t^7+kt^3-1\) is exactly the condition that every one of these points be smooth. No geometric smoothness over the algebraic closure is assumed for \(C_{k,q}\), and the theorem does not settle the source's corresponding conjecture. A *rational bitangent line* here is a rational line tangent at two distinct **rational** smooth points, even if other geometric tangencies exist. A *rational flex* is a rational point where its unique rational tangent meets the curve to order at least three; the proof shows this order is exactly three.

## Proof
Let \(L\) be any rational line with equation \(aX+bY+cZ=0\), and choose independent vectors \(U,V\in\mathbf F_q^3\) spanning its underlying two-dimensional vector space. Write a general point of \(L\) as \(sU+tV\). Since \(U,V\) have rational coordinates, the binomial \(X^qY-XY^q\), restricted to \(L\), equals \((U_XV_Y-U_YV_X)(s^qt-st^q)\). The other two Frobenius binomials similarly have coefficients \(U_YV_Z-U_ZV_Y\) and \(U_ZV_X-U_XV_Z\). These three coefficients form the cross product \(U\times V=\lambda(a,b,c)\) for some \(\lambda\in\mathbf F_q^\times\). Thus, *as an identity of binary forms*,
\[
C_{k,q}|_L=\lambda(s^qt-st^q)Q_L(s,t),
\]
where \(Q_L\) is the restriction of the ternary quadratic
\[
Q_{a,b,c}(X,Y,Z)=(c+kb)X^2+aY^2+bZ^2
\]
to \(L\). The factor \(s^qt-st^q\) has the \(q+1\) distinct points of \(\mathbf P^1(\mathbf F_q)\) as its simple zeros.

**Nonvanishing of the residual quadratic.** We verify that \(Q_L\) is never identically zero. Write \(\alpha=c+kb\), \(\beta=a\), \(\gamma=b\). If all three diagonal coefficients are nonzero, the quadratic form has rank three and cannot vanish on a two-dimensional subspace. If precisely two are nonzero, a two-dimensional totally isotropic subspace of this rank-two ternary quadratic must contain its radical axis. In the cases of radical \(X\), \(Y\), and \(Z\), respectively, the nonzero corresponding coefficient of the line equation is \(a\), \(b\), and \(c\); so this axis is *not* contained in \(L\). If precisely one of \(\alpha,\beta,\gamma\) is nonzero, the three cases force, respectively, the rational lines \(Z=0\), \(X=0\), or \(Y+kZ=0\); the resulting restrictions are nonzero scalar multiples of \(X^2\), \(Y^2\), or \(Z^2\). This exhausts the possibilities: \(Q_L\not\equiv0\) for every rational line.

At each rational point of \(L\), the Frobenius factor has multiplicity one. Consequently, the local intersection multiplicity of \(C_{k,q}\) with \(L\) is one plus the multiplicity of that point as a root of \(Q_L\). Since all rational points are smooth, \(L\) is tangent at such a point exactly when \(Q_L\) vanishes there. A nonzero binary quadratic has at most two distinct roots on \(\mathbf P^1(\mathbf F_q)\): two simple roots correspond to a rational bitangent line; one double root corresponds to a flex line of exact contact three; and no rational roots correspond to no rational tangencies.

It remains to recognize *which* lines carry double roots. In odd characteristic, the binary quadratic has a double projective root exactly when its discriminant vanishes. Set \(D=\operatorname{diag}(c+kb,a,b)\). If the symmetric matrix of the restriction is \([U,V]^T D[U,V]\), the Cauchy–Binet adjugate identity gives
\[
\det([U,V]^TD[U,V])=(U\times V)^T\operatorname{adj}(D)(U\times V)
=\lambda^2\bigl(a^3b+b^3c+ac^3+k(b^4+abc^2)\bigr).
\]
The binary discriminant is \(-4\) times this determinant. Since \(\lambda\ne0\) and the characteristic is odd, precisely the lines lying on \(D_k(\mathbf F_q)\) have a double root of \(Q_L\). Such a double root lies over \(\mathbf F_q\), so each such line has one rational flex contact. We have proved \(F=\#D_k(\mathbf F_q)\).

Put \(N=q^2+q+1\), and write \(E\) for the number of rational lines tangent at zero rational points. The plane-filling curve has exactly \(N\) rational points, each with one unique rational tangent, whence incidence counting gives \(2B+F=N\). The dual plane has exactly \(N\) rational lines, whence \(E+F+B=N\). Subtraction yields \(E=B\) and the stated formula for \(B\). If \(D_k\) is geometrically smooth, the plane-degree/genus formula gives genus three and the Hasse–Weil bound gives the two estimates.

## Verification
The accompanying standalone file `verify_tangent_quartic.py` computes tangent directions directly from the cubic expressions for the partial derivatives at rational points, independently counts fibers of the tangent map, and compares them against a separate residual-quadratic test and the zero locus of \(D_k\). It also symbolically checks the quartic adjugate identity. For the seven explicitly tested prime fields, its outputs are:

| \(q\) | \(k\) | Rational flexes \(F\) | Rational bitangents \(B\) | Untangent rational lines \(E\) |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 2 | 5 | 4 | 4 |
| 5 | 4 | 5 | 13 | 13 |
| 7 | 1 | 11 | 23 | 23 |
| 11 | 1 | 9 | 62 | 62 |
| 13 | 1 | 15 | 84 | 84 |
| 17 | 4 | 15 | 146 | 146 |
| 19 | 1 | 21 | 180 | 180 |

SymPy Gröbner calculations on all three standard affine charts independently verify geometric smoothness of each of these seven companion quartics. The quartic specializes at \(k=0\) to the classical Klein quartic \(a^3b+b^3c+ac^3=0\), smooth in odd characteristics other than seven; \(k=0\) itself **does not** satisfy the rational-smoothness hypothesis on \(C_{k,q}\). In characteristic seven the quartic at \(k=1\) is geometrically smooth, as witnessed by the same exact Gröbner chart checks. Hence the companion quartic family has a smooth member over every odd characteristic. These computations confirm benchmark instances; the uniform counting theorem is proved algebraically above, not extrapolated from finite experiments.

## Relationship to prior work
Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, Theorem 1.2, introduce exactly the degree-\(q+3\) family and characterize rational smoothness by \(t^7+kt^3-1\). Proposition 3.3 excludes rational line components. Sections 1–4 investigate smoothness, point counts for parameter incidence, and generalizations, but do not state a dual-plane quartic or a flex/bitangent census. The same authors' *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v2, discusses tangent coverage and related counting questions, not the residual quadratic discriminant for this plane-filling family. Related earlier minimum-degree filling curves have degree \(q+2\) and different equations. The new exact quartic equality is not a direct numerical corollary of these works: it uses the line-restriction factorization and adjugate computation to identify a genus-three invariant controlling every rational tangent fiber.

## Limitations
Originality is assessed against the identified literature and available mathematical research records; poorly indexed classical or equivalent results remain possible. The theorem does not count tangencies at nonrational points, does not prove \(C_{k,q}\) geometrically smooth, and does not give the genus-three Hasse estimates where \(D_k\) is singular. Only odd-characteristic fields are covered. The seven finite tests and exact quartic checks are corroboration rather than a proof for all prime powers.

## References
1. Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (first public July 6, 2023), https://arxiv.org/html/2307.03072v1.
2. Shamil Asgarli and Dragos Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v2 (2023), https://arxiv.org/html/2302.13420v2.
