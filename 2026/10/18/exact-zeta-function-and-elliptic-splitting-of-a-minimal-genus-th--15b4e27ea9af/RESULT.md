# Exact zeta function and elliptic splitting of a minimal genus-three Artin–Schreier curve

## Finding
For \(C/\mathbb F_3\) given by \(y^3-y=x^2+x+x^{-1}\) on \(x\ne0\), its complete Hasse–Weil numerator is
\[
P_C(T)=1+T+4T^2+9T^3+12T^4+9T^5+27T^6
=(1-T+3T^2)^2(1+3T+3T^2).
\]
Consequently \(\#\operatorname{Jac}(C)(\mathbb F_3)=63\); the Jacobian is \(\mathbb F_3\)-isogenous to the product of two ordinary elliptic factors and one supersingular elliptic factor.

## Assumptions and scope
All geometry is over characteristic \(3\). Let \(C\) mean the smooth projective model. The two pole orders of \(x^2+x+x^{-1}\) are \(2\) at infinity and \(1\) at zero. There are no auxiliary parameter restrictions. The pre-existing classification establishes that this particular curve has geometric automorphism group \(C_3\) and lies at the first possible genus for positive \(3\)-rank with no additional automorphisms; neither is claimed as new here.

## Proof
Homogenizing after multiplication by \(x\) gives the projective plane quartic
\[
XY^3-XYZ^2-X^3Z-X^2Z^2-Z^4=0.
\]
In its affine chart \(Z=1\), \(X=0\) is excluded and \(\partial F/\partial Y=-X\ne0\). At infinity the only two points are \([1:0:0]\) and \([0:1:0]\); at them, respectively, \(\partial F/\partial Z=-1\) and \(\partial F/\partial X=1\). Thus the projective quartic is smooth of genus \(3\), and both points at infinity are rational over every extension.

For every integer \(n\ge1\), the finite-field additive map \(y\mapsto y^3-y\) has kernel of size \(3\) and image exactly the trace-zero elements of \(\mathbb F_{3^n}\). Accordingly
\[
\#C(\mathbb F_{3^n})=2+3\#\{x\in\mathbb F_{3^n}^\times:\operatorname{Tr}_{\mathbb F_{3^n}/\mathbb F_3}(x^2+x+x^{-1})=0\}.
\]
Exact exhaustive computations in the explicitly defined fields \(\mathbb F_3\), \(\mathbb F_3[u]/(u^2+1)\), and \(\mathbb F_3[u]/(u^3+2u+1)\) give respectively \(1,5,14\) qualifying nonzero \(x\) and \(5,17,44\) rational points. For \(q=3\) the first three Frobenius power sums are consequently \(-1,-7,-16\). Newton identities determine the coefficients of degrees \(1,2,3\) of the zeta numerator as \(1,4,9\). The Weil functional equation of a genus-three curve gives \(c_{6-j}=3^{3-j}c_j\) for \(j=0,1,2\), yielding \(c_4=12\), \(c_5=9\), \(c_6=27\). The displayed polynomial factorization is an exact integer identity.

The elliptic Weil polynomials are \(1-T+3T^2\) and \(1+3T+3T^2\). Over \(\mathbb F_3\), corresponding curves are \(E_1:v^2=u^3+u^2+2\) (three rational points) and \(E_2:v^2=u^3+2u+1\) (seven rational points). Both are smooth elliptic curves. Their traces are \(1\) and \(-3\); the first is ordinary and the second supersingular. The Honda–Tate classification, or equivalently Tate's isogeny theorem with the determined Weil polynomials, gives \(\operatorname{Jac}(C)\sim_{\mathbb F_3}E_1^2\times E_2\). Finally \(P_C(1)=63\).

## Verification
Run \(\texttt{python3 verification.py}\) with the standard Python library. The program constructs five finite extension fields by irreducible polynomials (whose irreducibility it checks), counts points through the trace criterion, independently checks Newton sums through extension degree five, and verifies the factorization and elliptic-model point counts. The counts at degrees four and five, \(77\) and \(155\), are extra consistency checks; only degrees one through three plus the proven functional equation are required for the full infinite statement.

## Relationship to prior work
Tafazolian and Kazemifard (2026, Proposition 4.2) supply the geometric genus-three example and its automorphism rigidity, not its full zeta numerator. Auer and Top (2002) analyze a different, highly symmetric plane-quartic family with three mutually isogenous elliptic factors, not the mixed ordinary/supersingular splitting here. General methods for Artin–Schreier zeta computation do not, without this calculation, imply the particular factors or Jacobian order.

## Limitations
The result is for this explicit \(\mathbb F_3\)-model, not all its twists or every curve in the geometric family. The isogeny is over \(\mathbb F_3\), not an asserted isomorphism or a decomposition respecting polarization. Existing databases of abelian isogeny classes may contain the resulting polynomial without identifying this curve with it; an unindexed independent treatment of an equivalent quartic remains possible.

## References
1. A. Tafazolian and M. Kazemifard, *Artin–Schreier Curves of Prescribed p-Rank Without Extra Automorphisms*, arXiv:2610.13279 (first publicly available 2026-10-09), especially Proposition 4.2.
2. R. Auer and J. Top, *Some genus 3 curves with many points*, arXiv:math/0201320 (2002).
3. Standard Weil functional equation and Tate isogeny criterion for abelian varieties over finite fields.
