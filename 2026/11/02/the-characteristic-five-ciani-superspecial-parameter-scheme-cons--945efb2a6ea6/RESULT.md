# The characteristic-five Ciani superspecial parameter scheme consists of four quadratic points

## Finding

Let \(k=\mathbb F_5\) and let \(U\subset\mathbb A^3_k\) be the open parameter space of smooth normalized Ciani plane quartics
\[
C_{a,b,c}: X^4+Y^4+Z^4+aX^2Y^2+bY^2Z^2+cZ^2X^2=0.
\]
Define \(\mathcal S\subset U\) by the vanishing of the Hasse--Witt matrix of this family, with its natural determinantal scheme structure. Then there is an isomorphism of finite étale \(k\)-schemes
\[
\boxed{\mathcal S\simeq\coprod_{i=1}^{4}\operatorname{Spec}\mathbb F_{25}.}
\]
More explicitly, its eight geometric parameter triples are exactly
\[
(a,b,c)=(\varepsilon_1r,\varepsilon_2r,\varepsilon_3r),\qquad
r^2-2r-2=0,\qquad
\varepsilon_j\in\{1,-1\},\quad\varepsilon_1\varepsilon_2\varepsilon_3=1.
\]
Here the quadratic equation has two distinct roots in \(\mathbb F_{25}\), and \(\mathcal S(\mathbb F_5)=\varnothing\). Its zero-dimensional zeta function and extension-field point counts are
\[
Z(\mathcal S,T)=(1-T^2)^{-4},\qquad
\#\mathcal S(\mathbb F_{5^n})=\begin{cases}0&n\text{ odd},\\8&n\text{ even}.\end{cases}
\]
This is a classification of **marked normalized coefficient triples**, not a classification of geometric isomorphism classes of curves.

## Assumptions and scope

The base field has characteristic exactly five; geometric statements are over an algebraic closure. Parameters lie in the smooth locus \(U\), given by the nonvanishing of
\[
\Delta=(a^2-4)(b^2-4)(c^2-4)(a^2+b^2+c^2-abc-4).
\]
The Hasse--Witt zero scheme means the intersection of the zero loci of all entries of the Hasse--Witt matrix after choosing the standard basis of canonical differentials of a smooth plane quartic. The vanishing scheme is invariant under change of this basis. For genus three, full Hasse--Witt vanishing means \(a\)-number three, equivalently a superspecial Jacobian. No assertion is made about arbitrary non-Ciani quartics, other characteristics, or isomorphism-class counts.

## Proof

**1. Hasse--Witt coefficient formula.** For a smooth plane quartic \(F=0\), the Hasse--Witt entries can be read from coefficients of \(F^{p-1}\) indexed by the canonical adjunction basis \(X,Y,Z\). In characteristic five, all monomials of the Ciani polynomial have even exponents; therefore the six off-diagonal entries vanish by parity. The three diagonal entries are the coefficients of \(X^8Y^4Z^4\), \(X^4Y^8Z^4\), and \(X^4Y^4Z^8\) in \(F^4\). Direct multinomial extraction gives, in \(k[a,b,c]\),
\[
\begin{aligned}
H_X&=a^2c^2+2a^2-abc+b^2+2c^2+2,\\
H_Y&=a^2b^2+2a^2-abc+2b^2+c^2+2,\\
H_Z&=a^2-abc+b^2c^2+2b^2+2c^2+2.
\end{aligned}
\]
Thus \(\mathcal S=V(H_X,H_Y,H_Z)\cap U\) scheme-theoretically.

**2. Exhaust all geometric zeros on the smooth locus.** Subtracting the displayed equations yields
\[
\begin{aligned}
H_X-H_Y&=(a^2+1)(c^2-b^2),\\
H_Y-H_Z&=(b^2+1)(a^2-c^2),\\
H_Z-H_X&=(c^2+1)(b^2-a^2).
\end{aligned}
\]
Since \(\Delta\ne0\) implies \(a^2+1,b^2+1,c^2+1\ne0\) in characteristic five, every common zero satisfies \(a^2=b^2=c^2=s\). Put \(t=abc\). The Hasse equations then reduce to \(t=s^2+2\), while \(t^2=s^3\). Eliminating \(t\) gives
\[
(s+1)^2(s^2+2s-1)=0.
\]
The smoothness assumption excludes \(s=-1\). The remaining quadratic has two simple nonzero roots, and for each root there are exactly four sign triples satisfying the fixed product equation. Equivalently, pick a root \(r\) of \(r^2-2r-2\), so that \(r^3=s^2+2\), and take the four sign triples with product \(1\). These are all geometric solutions. Their smoothness follows because \(a^2+1=s+1\ne0\) and
\[
4+abc-a^2-b^2-c^2=(s+1)^2=2\ne0.
\]

**3. Reduced scheme structure.** Let \(J\) be the three-by-three Jacobian matrix of \(H_X,H_Y,H_Z\) with respect to \(a,b,c\). Direct differentiation at any listed point gives
\[
\det J=1-r\ne0.
\]
For example, on the diagonal \((r,r,r)\), the determinant before reduction is \(4r^3(r^2+1)^2(4r^2-3r+10)\), which reduces to \(1-r\) modulo \(r^2-2r-2\). Even-sign changes of the coefficients give the same determinant. The Jacobian criterion therefore makes the eight zeros reduced and étale over \(k\); no hidden multiplicities remain.

**4. Frobenius descent.** In \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-3)\), the roots are \(r=1+u\) and \(r'=1-u=r^5\). Frobenius preserves each of the four sign patterns and exchanges \(r\) with \(r'\). Hence there are four geometric orbits of length two, proving the asserted scheme decomposition and zeta function.

## Verification

The standalone `verify.py` uses only the Python standard library. It reconstructs the three diagonal Hasse polynomials independently by enumerating all \(6^4\) ordered monomial selections in \(F^4\), evaluates the smooth Hasse zeros exhaustively among all \(25^3\) parameter triples over \(\mathbb F_{25}\), checks the predicted eight points, verifies their Jacobian determinants, and confirms the four quadratic Frobenius orbits. It also directly enumerates all \(651\) projective points of \(\mathbb P^2(\mathbb F_{25})\) for each of the eight plane curves and finds \(56\) rational points in every case, consistent with maximality. Its run output is supplied in `verification_output.txt` and ends with `VERIFY_OK`. The finite-field enumerations are checks, not the proof that no geometric points exist over larger fields; that completeness is supplied by Step 2.

## Relationship to prior work

The Ciani family and its significance as a plane-quartic automorphism stratum are classical. Lercier--Ritzenthaler--Rovetta--Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields* (first arXiv version, March 3, 2014), study the normalized family and its sign symmetries, but their representative-family theorem explicitly assumes characteristic at least seven and does not give this characteristic-five superspecial determinantal scheme. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type* (first arXiv version, January 31, 2022), proves that superspecial normalized parameters lie in the quadratic finite field and gives a general maximal/minimal criterion; that field-bound statement does **not** enumerate the eight triples, prove transversality, or determine the four quadratic closed points. The current result does not claim novelty for that bound, the elliptic-quotient theory, or the abstract existence of superspecial genus-three curves.

Prior genus-three superspecial isomorphism-class enumerations and explicit Ciani elliptic-quotient criteria provide substantial background; counting isomorphism classes is not logically equivalent to the marked coefficient-scheme calculation. The historical-priority comparison remains qualified because the full Brock dissertation on superspecial curves of genera two and three was not available for direct textual inspection. No complete parameter-scheme evaluation identical to the claim was identified in the accessible primary materials and mathematical-record searches.

## Limitations

The result treats only the normalized three-parameter Ciani equation in characteristic five. It does not say that the eight marked models represent eight distinct geometric curves, nor does it classify their twists or the entire superspecial genus-three moduli stack. The scheme structure used is the explicit Hasse--Witt zero locus on the smooth coefficient space; moduli-quotient scheme structures may differ. The direct projective point counts concern \(\mathbb F_{25}\), not every extension. Priority is not certified by a failed search; independent mathematical and historical review has not been performed.

## References

1. R. Lercier, C. Ritzenthaler, F. Rovetta, and J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562 (first version March 3, 2014), especially Sections 3 and 5.
2. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996 (first version January 31, 2022), Sections 2--4.
3. B. W. Brock, *Superspecial Curves of Genera Two and Three*, doctoral dissertation (1993); bibliographic background, full text not inspected.
