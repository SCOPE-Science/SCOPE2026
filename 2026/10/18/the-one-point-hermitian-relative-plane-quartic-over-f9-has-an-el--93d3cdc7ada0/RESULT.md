# The one-point Hermitian-relative plane quartic over \(\mathbb F_9\) has an elliptic-cube Jacobian

## Finding
Let \(\eta\in\mathbb F_9\) satisfy \(\eta^2=-1\), and let \(C\) be the smooth projective plane curve
\[
C:\quad X^4+\eta Y^4+Y^3Z+YZ^3=0.
\]
Its Hasse–Weil zeta function over \(\mathbb F_9\) has numerator
\[
L_C(T)=(1-3T+9T^2)^3
=1-9T+54T^2-189T^3+486T^4-729T^5+729T^6.
\]
In particular \(\#\operatorname{Jac}(C)(\mathbb F_9)=L_C(1)=343\). If \(E/\mathbb F_3\) is the elliptic curve \(v^2=u^3-u+1\), then
\[
\operatorname{Jac}(C)\sim_{\mathbb F_9}
  (E\times_{\mathbb F_3}\mathbb F_9)^3.
\]
This is an isogeny of unpolarized abelian varieties, not a polarization-preserving isomorphism.

## Assumptions and scope
All equations are interpreted over finite fields of characteristic three. The element \(\eta\) is either root of \(U^2+1\) in \(\mathbb F_9\); the two choices are conjugate under the \(\mathbb F_3\)-Frobenius and have the same zeta function. The homogeneous quartic has derivatives \(F_X=X^3\), \(F_Y=\eta Y^3+Z^3\), and \(F_Z=Y^3\), whose common projective zero locus is empty. Thus \(C\) is smooth and geometrically integral, with genus \(3\) by the smooth plane quartic genus formula. The curve is the \(q=9\) member of the one-rational-point Hermitian-relative family of Homma and Kim.

## Proof
For \(m\in\{1,2,3\}\), let \(K_m=\mathbb F_{3^{2m}}\), containing the chosen \(\mathbb F_9\). In the affine chart \(Z=1\), the curve equation is \(x^4=-\eta y^4-y^3-y\). Define \(r_m(a)=\#\{x\in K_m:x^4=a\}\). Exact field arithmetic yields
\[
\begin{array}{c|rrr}
 m&\text{affine points}&\text{points at infinity}&N_m\cr
 1&1&0&1\cr
 2&105&4&109\cr
 3&892&0&892
\end{array}
\]
The affine count is precisely \(\sum_{y\in K_m}r_m(-\eta y^4-y^3-y)\). At infinity \(Y\ne0\), and there are exactly \(r_m(-\eta)\) points \([x:1:0]\). The point \([1:0:0]\) is never on the curve. No singular points or branch corrections arise because this is the original smooth projective plane model. Every sum above is a finite exhaustive sum over \(9\), \(81\), or \(729\) field elements; the attached verifier constructs the fields from explicitly checked irreducible polynomials and implements both this count and direct projective enumeration.

Write \(q=9\), let \(\alpha_1,\ldots,\alpha_6\) be the reciprocal roots, and put \(s_m=\sum_j\alpha_j^m=q^m+1-N_m\). The values are \(s_1=9\), \(s_2=-27\), and \(s_3=-162\). Newton's identities for \(L_C(T)=\sum_{i=0}^{6}a_iT^i\) give
\[
a_1=-9,\qquad a_2=54,\qquad a_3=-189.
\]
The genus-three Weil functional equation \(a_{6-i}=q^{3-i}a_i\) for \(0\le i\le3\) gives \(a_4=486\), \(a_5=-729\), and \(a_6=729\). Direct integer multiplication factors this polynomial as asserted. The standard Jacobian point-count formula is \(\#\operatorname{Jac}(C)(\mathbb F_9)=L_C(1)=343\).

The elliptic curve \(E:\ v^2=u^3-u+1\) is nonsingular in characteristic three because the derivative of its right-hand side is \(-1\). For each \(u\in\mathbb F_3\), the right-hand side is \(1\), so there are two affine points for each of three values of \(u\), plus infinity: \(\#E(\mathbb F_3)=7\). Its Frobenius trace over \(\mathbb F_3\) is therefore \(-3\). Under base change to \(\mathbb F_9\), the trace is \((-3)^2-2\cdot3=3\), so its Weil numerator is \(1-3T+9T^2\). The equality of characteristic Frobenius polynomials proves the \(\mathbb F_9\)-isogeny via the finite-field isogeny theorem.

## Verification
Run \(`python3 verify_curve.py`\). The script uses only the Python standard library. It first checks irreducibility of the defining field polynomials by division by all monic factors of degree at most half the extension degree, then performs both root-frequency and independently looped projective counts; all six counts agree. It checks the initial and reciprocal Weil coefficients, the exact cube, the Jacobian point count, and the elliptic traces. Its terminating message is `VERIFICATION_OK`. The complete finite-field computations are certificates of the three point counts; the genus-three functional equation, Newton identities, and finite-field isogeny theorem extend them to the full zeta numerator and isogeny class.

## Relationship to prior work
Homma and Kim's 2026 Theorem 1.1 classifies the Hermitian-relative curves with only one rational point, and gives exactly this normal form. Their result establishes \(N_1=1\), not the full extension-degree counts or this Weil polynomial. The 2010 work of Meagher and Top studies twists and their Frobenius actions on genus-three Jacobians; its specific Dyck–Fermat quartic twist tables (Proposition 18) assume characteristic at least five, so do not state the characteristic-three calculation here. Earlier tables of maximal genus-three point counts study a different extremal invariant. Those authors' results and the standard zeta/isogeny theorems are explicitly credited; only this model's exact zeta and isogeny identification are claimed as new.

## Limitations
The theorem concerns the specified \(\mathbb F_9\)-model (and its Frobenius-conjugate coefficient), not every Hermitian-relative curve or all genus-three quartics. It gives an isogeny class, not an explicit kernel, minimal isogeny degree, or polarizations. The field-enumeration checks are finite and exhaustive only for the three extension degrees stated; the infinite extension-count consequence depends on the classical Weil functional equation. An unindexed earlier computation of this specific Frobenius polynomial remains possible.

## References
- Masaaki Homma and Seon Jeong Kim, *Rational points and inflexions on Hermitian-relative curves*, arXiv:2610.09672 (submitted October 7, 2026), Theorem 1.1; accessible proceedings manuscript: https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_17.pdf .
- Stephen Meagher and Jaap Top, *Twists of genus three curves over finite fields*, 2010, especially Sections 3 and 7, https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf .
- Jaap Top, *Curves of genus 3 over small finite fields*, Indagationes Mathematicae 14 (2003), 275–283.
- A. Weil, the zeta functional equation for curves over finite fields; J. Tate, the finite-field isogeny theorem for abelian varieties.
