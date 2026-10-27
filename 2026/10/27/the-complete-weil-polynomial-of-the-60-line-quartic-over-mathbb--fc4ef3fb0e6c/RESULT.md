# The complete Weil polynomial of the 60-line quartic over \(\mathbb F_4\)

## Finding

Let \(e_j\) denote the elementary symmetric polynomial of degree \(j\) in the five homogeneous coordinates \(x_1,\ldots,x_5\). Choose a primitive fifth root \(\alpha\) in \(\mathbb F_{16}\), with \(\alpha^4+\alpha^3+\alpha^2+\alpha+1=0\), and put \(\mu=1+\alpha^2+\alpha^3\in\mathbb F_4\). For the smooth quartic K3 surface
\[
S=\{e_1=0,\;e_4+\mu e_2^2=0\}\subset\mathbb P^4_{\mathbb F_4},
\]
the characteristic polynomial of geometric degree-four Frobenius on second \(\ell\)-adic cohomology, for any prime \(\ell\ne2\), is
\[
\boxed{P_2(X)=(X-4)^{10}(X+4)^{10}(X^2-3X+16).}
\]
Equivalently, the complete Hasse--Weil zeta function is
\[
\boxed{Z(S/\mathbb F_4,T)=\frac{1}{(1-T)(1-16T)(1-4T)^{10}(1+4T)^{10}(1-3T+16T^2)}.}
\]
In particular, \(\#S(\mathbb F_4)=20\) and \(\#S(\mathbb F_{16})=554\). The remaining two Frobenius eigenvalues have sum \(3\), product \(16\), and discriminant \(-55\). The formula determines the number of rational points over every finite extension of \(\mathbb F_4\).

## Assumptions and scope

The base field is precisely \(\mathbb F_4\); the quartic uses the specific nontrivial cube root \(\mu=1+\alpha^2+\alpha^3\). All statements concern the smooth geometric surface, not the reducible union of its lines. The smoothness, 60-line equations, and rank-20 Néron--Severi span are established in the cited 2015 source (Section 8). Fix \(\ell\ne2\); the standard K3 cohomological trace formula has \(\dim H^2=22\) and vanishing odd cohomology. The arithmetic Frobenius action on line classes and geometric Frobenius have identical characteristic polynomials here because their permutation is an involution.

## Proof

**1. Algebraic 20-dimensional part.** Rams and Schütt give one line \(L\) by
\[
 e_1=0,\quad x_3+x_2+(\alpha^3+\alpha+1)x_1=0,\quad
 x_4+(\alpha^3+\alpha^2+\alpha+1)x_2+\alpha x_1=0.
\]
Its \(S_5\)-orbit comprises 60 distinct lines and spans the full geometric Néron--Severi group of rank 20. Parameterizing the source line by \(x_1=s\), \(x_2=t\) gives the two five-vectors
\[
(1,0,c,\alpha,1+c+\alpha),\qquad(0,1,1,d,d),
\]
where \(c=1+\alpha+\alpha^3\) and \(d=1+\alpha+\alpha^2+\alpha^3\); in characteristic two the last component of the second vector is \(d\). (The equality \(1+1+d=d\) is used.)

Enumerate all 120 coordinate permutations and reduce their two-dimensional spans by finite-field row reduction, obtaining exactly 60 distinct lines. Form the \(60\)-by-\(60\) intersection matrix \(G\) with diagonal \(-2\), entry \(1\) for a meeting pair and \(0\) otherwise; for smooth quartics these are the actual line-class intersection numbers. Coordinatewise fourth powers induce a permutation matrix \(P\) of the 60 lines, satisfying \(P^2=I\). Exact row reduction modulo the prime \(1000003\) gives
\[
 \operatorname{rank}_{\mathbb F_{1000003}}G(I+P)=10,
 \qquad\operatorname{rank}_{\mathbb F_{1000003}}G(I-P)=10.
\]
Each modular rank is a lower bound for the corresponding rational rank. The two images are disjoint eigenspaces and their sum lies in the rank-20 rational Néron--Severi span (nondegeneracy of the intersection form); therefore both rational dimensions equal \(10\). Thus Frobenius on algebraic \(H^2\) has eigenvalue \(4\) ten times and \(-4\) ten times. Its first two traces are \(0\) and \(320\).

**2. Complete finite-field point counts.** Represent \(\mathbb F_{16}\) as \(\mathbb F_2[a]/(a^4+a^3+a^2+a+1)\), with \(a\) representing \(\alpha\), and identify \(\mathbb F_4=\{0,1,\mu,1+\mu}\). For any \(q\in\{4,16}\), every nonzero five-vector satisfying \(e_1=0\) is uniquely \((u,v,w,z,u+v+w+z)\), with \((u,v,w,z)\in\mathbb F_q^4\setminus\{0}\). Exhaustively test \(e_4+\mu e_2^2=0\) on these \(q^4-1\) vectors and divide the count by \(q-1\). The exact nonzero affine counts are \(60\) and \(8310\), respectively; hence
\[
 \#S(\mathbb F_4)=60/3=20,\qquad\#S(\mathbb F_{16})=8310/15=554.
\]
Every case is enumerated in the accompanying standalone verifier; no random trials or sampled cases enter these counts.

**3. Remaining two eigenvalues.** By the Grothendieck--Lefschetz trace formula,
\[
 \#S(\mathbb F_{4^n})=1+4^{2n}+\operatorname{Tr}(F^n\mid H^2).
\]
The algebraic contribution to \(\operatorname{Tr}F\) is \(0\) and to \(\operatorname{Tr}F^2\) is \(320\). Denote the two residual eigenvalues by \(\lambda,\lambda'\). The two point counts give
\[
 \lambda+\lambda'=20-17=3,\qquad
 \lambda^2+\lambda'^2=554-257-320=-23.
\]
Thus \(2\lambda\lambda'=3^2-(-23)=32\), so \(\lambda\lambda'=16\). The residual polynomial is \(X^2-3X+16\), proving the full cohomological and zeta identities.

## Verification

Execute `python3 VERIFY.py` with Python's standard library. It reconstructs the 60 lines from the cited equations; checks the source line lies on the quartic by exact homogeneous-polynomial restriction; computes the Frobenius permutation and the two rank certificates; and exhausts all projective points over \(\mathbb F_4\) and \(\mathbb F_{16}\). A successful run prints `VERIFY_OK`. The reported pair \((20,554)\) is exhaustive for the two named fields. The implication for every extension is an algebraic consequence of the 22-dimensional K3 cohomology and its proven Frobenius polynomial, not of numerical extrapolation.

## Relationship to prior work

Rams--Schütt (arXiv:1512.01358; earliest public 2015-12-04) provide the explicit \(S_5\)-symmetric quartic, 60 lines, line equations, smoothness and the rank-20 Néron--Severi span (Section 8); these inputs are not new. Degtyarev (arXiv:1604.05836) classifies large characteristic-two line configurations and describes the 60-line case; the complex classification of Degtyarev--Itenberg--Sertöz (arXiv:1601.04238) is not a finite-field Frobenius calculation. The additional result here is the exact arithmetic Frobenius factor and complete zeta function of this particular \(\mathbb F_4\)-model. Neither line counts, the Néron--Severi discriminant nor the geometric line configuration alone supplies its two-dimensional Frobenius trace.

## Limitations

The statement is about one marked \(\mathbb F_4\)-form; it does not classify zeta functions of all characteristic-two quartics with 60 lines, or prove a universal modularity theorem. The zeta computation depends on the published smoothness and rank-20 spanning statements, together with the fully reproducible exact finite-field and matrix calculations. An identical arithmetic evaluation in specialized or later literature cannot be excluded from the available source inspections.

## References

- S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358, first posted 2015-12-04, Section 8. https://arxiv.org/abs/1512.01358
- A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836, first posted 2016-04-20, Section 8, Remark 8.10. https://arxiv.org/abs/1604.05836
- A. Degtyarev, I. Itenberg and A. S. Sertöz, *Lines on quartic surfaces*, arXiv:1601.04238, first posted 2016-01-17. https://arxiv.org/abs/1601.04238
