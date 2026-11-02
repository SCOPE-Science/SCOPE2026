# Translation symmetries and the complete Newton stratification of characteristic-two quartic Picard covers

## Finding
Let \(k=\overline{\mathbb F}_2\). For each monic quartic \(f(X)=X^4+aX^3+bX^2+cX+d\) with \(\Delta=c^2+abc+a^2d\ne0\), let \(C_f\) be the smooth projective completion of \(Y^3=f(X)\). The Jacobian has \(2\)-rank \(0\) if \(a=0\), and \(2\)-rank \(2\) if \(a\ne0\); \(2\)-rank \(1\) never occurs. Every member has \(a\)-number exactly \(1\). The Newton slopes of its Jacobian are \((1/2)^6\) when \(a=0\), and \(0^2,(1/2)^2,1^2\) when \(a\ne0\).

The exceptional locus \(a=0\) is equivalently the locus where \(C_f\) has a nontrivial automorphism of the form \((X,Y)\mapsto(X+t,Y)\). In that case the four roots of \(T^4+bT^2+cT\) form a translation subgroup \((\mathbb Z/2)^2\); the three nontrivial involution quotients are supersingular elliptic curves and their product is isogenous to \(\operatorname{Jac}(C_f)\). For every \(q=2^m\), the numbers of smooth *monic coefficient quadruples*, as opposed to isomorphism classes, over \(\mathbb F_q\) are \(q^2(q-1)\) on the supersingular locus and \(q^2(q-1)^2\) on the \(2\)-rank-two locus.

## Assumptions and scope
All geometric statements concern smooth projective curves over the algebraic closure in characteristic two. The parameter space consists of ordered monic quartic coefficient quadruples \((a,b,c,d)\), not a coarse moduli space. The cover \(C_f\to\mathbb P^1_X\) has degree three, hence is tame. Its five branch points are the four distinct roots of \(f\) and infinity, so Riemann–Hurwitz gives genus three. The smoothness criterion follows from \(f'(X)=aX^2+c\): the resultant with \(f\) vanishes exactly when \(\Delta=c^2+abc+a^2d\) does.

## Proof
**Cartier computation.** A basis of holomorphic differentials is \(\omega_0=dX/Y^2\), \(\omega_1=X\,dX/Y^2\), \(\omega_2=dX/Y\). At the unique point above infinity their valuations are respectively \(4,1,0\), hence they are holomorphic; they form a basis by genus three. Cartier in characteristic two satisfies \(\mathcal C(h^2\eta)=h\mathcal C(\eta)\), \(\mathcal C(dX)=0\), and \(\mathcal C(X\,dX)=dX\). Since \(Y^3=f(X)\), the identities \(Y^{-1}=f(X)Y^{-4}\) and \(Y^{-4}=(Y^{-2})^2\) imply
\[
\mathcal C(\omega_0)=0,\qquad
\mathcal C(\omega_1)=\omega_2,\qquad
\mathcal C(\omega_2)=c^{1/2}\omega_0+a^{1/2}\omega_1.
\]
Thus the Cartier matrix in the displayed basis is
\[
\begin{pmatrix}0&0&c^{1/2}\\0&0&a^{1/2}\\0&1&0\end{pmatrix}.
\]
Because \(\Delta\ne0\) excludes \((a,c)=(0,0)\), this matrix always has rank two. Therefore the kernel is one-dimensional and the \(a\)-number is exactly one. If \(a=0\), Cartier is nilpotent of index at most three. If \(a\ne0\), its induced semilinear map on the quotient by \(k\omega_0\) is invertible, so its stable rank is two. The stable rank of Cartier equals the geometric \(2\)-rank, proving the dichotomy and excluding rank one. In genus three, \(2\)-rank two leaves a height-two factor of slopes \((1/2,1/2)\), giving the stated generic Newton polygon.

**Translation criterion and elliptic splitting.** For \(t\ne0\), the coefficient of \(X^2\) in \(f(X+t)-f(X)\) is \(at\), so translation invariance forces \(a=0\). Conversely, for \(a=0\) smoothness forces \(c\ne0\), and the additive separable polynomial \(L(T)=T^4+bT^2+cT\) has four distinct roots. Each root gives an automorphism \((X,Y)\mapsto(X+t,Y)\), and these roots form a two-dimensional \(\mathbb F_2\)-vector space.

For a nonzero root \(t\), put \(U=X^2+tX\). Since \(t^3+bt+c=0\), direct expansion gives
\[
X^4+bX^2+cX=U^2+(b+t^2)U,
\qquad b+t^2=c/t\ne0.
\]
The quotient by the corresponding involution therefore has affine equation \(Y^3=U^2+(c/t)U+d\). After scaling and shifting \(U\), this is an elliptic curve of characteristic-two model \(V^2+V=W^3\), which has \(j=0\) and is supersingular. The quotient by the entire translation group has function field \(k(Y)\), since \(L(X)=Y^3+d\), and hence genus zero. For \(\ell\ne2\), the group-algebra idempotents decompose \(H^1_{\acute et}(C_f,\mathbb Q_\ell)\) into the three nontrivial characters, each of dimension two as seen from the three elliptic quotients. Pullback from the three quotients gives an isomorphism on \(\ell\)-adic first cohomology, hence an isogeny of their product with \(\operatorname{Jac}(C_f)\). Therefore the latter is supersingular, with all six Newton slopes \(1/2\). This also independently establishes the rank-zero case.

**Exact marked-model counts.** For \(a=0\), smoothness is simply \(c\ne0\), leaving \(q\) choices each for \(b,d\). This gives \(q^2(q-1)\). For each \(a\ne0\) and \(b,c\), exactly one value \(d=(c^2+abc)/a^2\) is singular, giving \((q-1)q^2(q-1)=q^2(q-1)^2\) remaining tuples. Every finite extension is covered.

## Verification
The standalone dependency-free script `verify_picard.py` verifies exact characteristic-two field arithmetic for \(\mathbb F_2\) and \(\mathbb F_4\), enumerating all monic coefficient quadruples and computing the semilinear Cartier stable ranks. It also verifies the elliptic quotient identity for all admissible \((b,c,t)\) over fields of orders \(2,4,8,16\), and records sample point counts over four extensions. All checks end with `VERIFY_OK`; the complete execution output is in `verification_output.txt`. These finite computations corroborate the algebraic proof and do not replace its universal quantifiers.

## Relationship to prior work
The cyclic trigonal/Picard model and Cartier-operator theory are classical. Estrada-Sarlabous (1991) explicitly discusses ordinary and supersingular Jacobians of Picard curves via Hasse–Witt matrices; only its abstract was accessible, so potential overlap with the rank criterion remains a priority risk. Lario–Somoza (2014) studies the particular CM member \(Y^3=X^4-X\), not the full characteristic-two parameter space or its translation-group geometry. Published analyses of cyclic covers over characteristic greater than three do not imply a characteristic-two classification. The claim here is the joint geometric translation criterion, elliptic-quotient isogeny, and full Newton/Cartier stratification with exact finite-field marked-model counts, not the general Cartier formalism or the special curve's known arithmetic.

## Limitations
No classification of isomorphism classes, integral endomorphism rings, or polarizations of the isogeny is claimed. The isogeny is not asserted to preserve a principal polarization. Arithmetic descent of the three individual elliptic quotients may require adjoining roots of the separable additive polynomial. The full 1991 Estrada-Sarlabous article was not available for comparison, so historical priority is provisional. The self-review is not an independent audit.

## References
1. J. Estrada-Sarlabous, *On the Jacobian Varieties of Picard Curves Defined over Fields of Characteristic \(p>0\)*, Mathematische Nachrichten 152 (1991), 329–340, DOI: 10.1002/mana.19911520125. Abstract accessed; full text unavailable.
2. J.-C. Lario and A. Somoza, *The Sato-Tate conjecture for a Picard curve with Complex Multiplication*, arXiv:1409.6020, first public 2014-09-21, especially the model \(Y^3=X^4-X\).
3. Stöhr and Voloch, *Weierstrass points and curves over finite fields*, Proc. London Math. Soc. (3) 52 (1986), 1–19; background Cartier techniques.
