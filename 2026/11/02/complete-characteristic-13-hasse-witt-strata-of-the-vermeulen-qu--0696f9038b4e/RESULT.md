# Complete characteristic-13 Hasse–Witt strata of the Vermeulen quartic pencil

## Finding
Let \(k=\overline{\mathbb F}_{13}\). For \(u\in k\setminus\{0,1\}\), consider the smooth genus-three plane quartic
\[
V_u:\quad uX^4+Y^4-Z^4-2X^2Y^2-4XYZ^2=0.
\]
Define polynomials over \(\mathbb F_{13}\)
\[
 B(u)=6u^3+u^2+u+6=6(u+1)(u^2-3u+1),
 \qquad T(u)=-6u^3-4u^2-u-1=-6(u+6)(u^2-u+4).
\]
In a standard monomial basis of \(H^1(V_u,\mathcal O_{V_u})\), its Frobenius (Hasse–Witt) matrix is
\[
H(u)=\operatorname{diag}\bigl(u^3B(u),\,B(u),\,T(u)\bigr).
\]
The two cubic polynomials have no common root, all six roots are simple, and none is \(0\) or \(1\). Consequently the complete geometric arithmetic stratification is:

- At the three roots of \(B\): Jacobian \(13\)-rank \(1\) and \(a\)-number \(2\).
- At the three roots of \(T\): Jacobian \(13\)-rank \(2\) and \(a\)-number \(1\).
- At every other smooth parameter: Jacobian \(13\)-rank \(3\), \(a\)-number \(0\), and ordinary Jacobian.

Each nonordinary parameter lies in \(\mathbb F_{169}\). The only two rational parameters in \(\mathbb F_{13}\) are \(u=-1\) (rank \(1\)) and \(u=-6\) (rank \(2\)); the remaining four parameters form two Frobenius pairs. In particular the distinguished exceptional quartic \(V_{-1}\) has \(13\)-rank \(1\), but the other exceptional quartic in Pacini–Testa's characteristic-thirteen inflection-line analysis,
\[
K:\quad X^4+Y^4+Z^4+3(X^2Y^2+X^2Z^2+Y^2Z^2)=0,
\]
is ordinary: its Hasse–Witt matrix is \(11I_3\). No smooth member of this pencil has \(a\)-number \(3\).

## Assumptions and scope
Work over an algebraically closed field of characteristic exactly \(13\). All parameters \(u\neq0,1\) are included; the excluded parameters give singular plane quartics. Jacobian \(p\)-rank is \(\dim_{\mathbb F_p}\operatorname{Jac}(V_u)[p](\overline{k})\) expressed as the corresponding exponent; the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(V_u)[p])\). The complete classification concerns the explicitly embedded parameter pencil; different parameter values need not give distinct geometric isomorphism classes. The displayed secondary quartic \(K\) is included only as a motivated comparison, not as part of the pencil.

## Proof
**(1) Smoothness and genus.** Divide the three partial derivatives of the homogeneous defining quartic by \(4\), \(4\), and \(-4\), respectively. In characteristic \(13\) these equal
\[
 uX^3-XY^2-YZ^2,\qquad Y^3-X^2Y-XZ^2,\qquad Z(Z^2+2XY).
\]
If a common projective zero has \(Z=0\), then \(u\in\{0,1\}\) by separating \(XY=0\) from \(XY\neq0\). If \(Z\neq0\), the third equation forces \(Z^2=-2XY\), so \(X,Y\neq0\); the first two become \(X(uX^2+Y^2)=0\) and \(Y(Y^2+X^2)=0\), forcing \(u=1\). Conversely parameters \(0,1\) are singular. Therefore for \(u\neq0,1\) the canonical plane quartic is smooth and has genus \((4-1)(4-2)/2=3\).

**(2) Hasse–Witt coefficient extraction.** Write \(F=uX^4+Y^4-Z^4-2X^2Y^2-4XYZ^2\), and list the positive exponent vectors of sum \(4\):
\[
e_1=(2,1,1),\quad e_2=(1,2,1),\quad e_3=(1,1,2).
\]
Via the usual Čech monomial description of the cohomology of a smooth plane quartic, Frobenius on the basis indexed by these vectors has coefficient \(H_{ij}=[X^{13(e_j)_1-(e_i)_1}Y^{13(e_j)_2-(e_i)_2}Z^{13(e_j)_3-(e_i)_3}]F^{12}\). The basis convention (or its transpose) does not affect the diagonal formula. Applying the multinomial theorem to the five terms of \(F\), all six off-diagonal entries vanish, while
\[
H_{11}=6u^6+u^5+u^4+6u^3=u^3B(u),
\]
\[
H_{22}=6u^3+u^2+u+6=B(u),\qquad H_{33}=-6u^3-4u^2-u-1=T(u).
\]
Every coefficient equality is an identity in \(\mathbb F_{13}[u]\), not a finite list of parameter evaluations. It is independently reconstructed both by sparse multiplication of twelve copies of \(F\) and by direct multinomial enumeration in the supplied verifier.

**(3) Frobenius strata.** The factorisations of \(B,T\) above hold in \(\mathbb F_{13}[u]\). The quadratic discriminants are \(5\) and \(11\), both nonsquares in \(\mathbb F_{13}\). Thus the two quadratics have four distinct \(\mathbb F_{169}\)-roots; the two linear roots are \(-1\) and \(-6\). Direct Euclidean arithmetic gives \(\gcd(B,T)=1\); neither vanishes at \(0\) or \(1\). Since \(u\neq0\), the Hasse–Witt matrix has rank \(1\) at roots of \(B\), rank \(2\) at roots of \(T\), and rank \(3\) otherwise. A one-step Hasse–Witt rank ordinarily only bounds the stable Frobenius rank. Here all matrices are *diagonal* in the same parameter-independent basis, so their Frobenius-twisted products have exactly the same zero positions; the stable rank and hence the Jacobian \(13\)-rank equal the one-step rank. Cartier–Hasse duality identifies the \(a\)-number with \(3-\operatorname{rank}(H)\). This proves every stratum assertion.

**(4) Companion inflection exception.** For \(K\), applying the same coefficient formula to
\(G=X^4+Y^4+Z^4+3X^2Y^2+3X^2Z^2+3Y^2Z^2\) gives \(H_K=\operatorname{diag}(11,11,11)\), so \(K\) is ordinary. The identification of \(K\) and \(V_{-1}\) as special characteristic-thirteen inflection-line cases is due to Pacini–Testa and is not a new claim here.

## Verification
Run the standalone standard-library-only program `python3 verify.py`. It multiplies \(F^{12}\) and \(G^{12}\) as sparse polynomials over \(\mathbb F_{13}[u,X,Y,Z]\), independently computes all nine entries by multinomial enumeration, checks the polynomial factorisations, exhaustively locates the six nonordinary parameters in \(\mathbb F_{169}=\mathbb F_{13}[\alpha]/(\alpha^2-5)\), and independently counts rational points on the projective curves for four parameters and on \(K\). It checks the congruence \(1-\#C(\mathbb F_{13})\equiv\operatorname{tr}(H)\pmod{13}\), yielding \(12,8,22,12\) for \(u=-1,7,2,4\), respectively, and \(20\) for \(K\). The exact symbolic calculations establish infinitely many geometric-parameter cases; isolated point counts alone would not.

## Relationship to prior work
Pacini and Testa (2013, arXiv:1301.1865, §2 and Remarks 2.2–2.3) supply the Vermeulen family, its smoothness range, and the two characteristic-thirteen inflection-line exceptions, but do not present an arithmetic \(p\)-rank stratification. Lercier, Ritzenthaler, Rovetta, and Sijsling (2014, arXiv:1403.0562, §§3–5) classify representative plane-quartic families and finite-field isomorphism/point-count data; the inspected discussion does not provide the displayed cohomological polynomial stratification over the algebraic closure. Ohashi, Kudo, and Harashita (2021, arXiv:2111.09777, Introduction and opening sections) study \(a\)-numbers in a different order-six automorphism family and mention decomposition of other symmetric families into elliptic factors; no identity equivalent to the present six-point parameter stratification was found in the inspected portions. The extraction of a Hasse–Witt matrix from coefficients of \(F^{p-1}\) is a standard method. This result does not claim novelty for that method, for the classical pencil, or for the inflection-line exceptions.

## Limitations
This theorem does not classify all genus-three quartics, assign a distinct isomorphism class to every parameter, determine complete Newton polygons away from the ordinary cases, or establish independent priority. A specialized older elliptic-quotient treatment of the same pencil might imply the Hasse strata under a different normalization; such literature remains a residual novelty risk. The proof is an exact algebraic calculation with a reproducible verifier, not a formal-machine or independent audit.

## References
1. M. Pacini and D. Testa, *Plane quartics with at least 8 hyperinflection points*, arXiv:1301.1865 (first posted 2013-01-09), §2.
2. R. Lercier, C. Ritzenthaler, F. Rovetta, and J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562 (first posted 2014-03-03), §§3–5.
3. R. Ohashi, M. Kudo, and S. Harashita, *The \(a\)-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (first posted 2021-11-18), Introduction.
4. K.-O. Stöhr and J. F. Voloch, *A formula for the Cartier operator on plane algebraic curves*, J. Reine Angew. Math. **377** (1987), 49–64 (background coefficient method).
