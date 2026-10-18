# Four Weil spectra and a fifth-extension dichotomy among superspecial trigonal genus-five twists

## Finding
Let \(p\ge 11\) be prime with \(p\equiv 11\) or \(14\pmod {15}\), put \(q=p^2\), and let \(K=\mathbf F_q\). For every \(a,b\in K^\times\), let \(C_{a,b}\) be the smooth projective normalization of the geometrically integral plane quintic
\[
xy z^3+a x^5+b y^5=0.
\]
Fix a generator \(\gamma\) of \(K^\times\), put \(\zeta=\gamma^{(q-1)/15}\), and define the unique residue \(r\in\{0,\ldots,14\}\) by
\[
(a^4b)^{(q-1)/15}=\zeta^r.
\]
For \(u=pT\), the numerator of the Hasse--Weil zeta function of \(C_{a,b}/K\) is **exactly**
\[
L_{a,b}(T)=
\begin{cases}
(1+u)^{10}, & r=0,\\
1-u^5+u^{10}, & \gcd(r,15)=1,\\
(1+u^5)^2, & \gcd(r,15)=3,\\
(1-u+u^2)^5, & \gcd(r,15)=5.
\end{cases}
\]
There are precisely four distinct Weil polynomials, occurring for respectively \(1,8,4,2\) of the fifteen possible classes of \(a^4b\) modulo fifteenth powers. Each residue class is attained by exactly \((q-1)^2/15\) ordered coefficient pairs \((a,b)\). The Jacobians consequently exhibit four different \(K\)-isogeny types.

The base-field point counts are \(q+1+10p\), \(q+1\), \(q+1\), and \(q+1-5p\), respectively. The most distinctive phenomenon is that the twelve types satisfying \(\gcd(r,15)\in\{1,3\}\) have identical point counts \(q^n+1\) over **each** of \(\mathbf F_{q^n}\) for \(n=1,2,3,4\), although their Weil polynomials differ. At the first separating extension,
\[
\#C_{a,b}(\mathbf F_{q^5})=
\begin{cases}
q^5+1-5p^5,&\gcd(r,15)=1,\\
q^5+1+10p^5,&\gcd(r,15)=3.
\end{cases}
\]
Thus even four consecutive extension-field point counts do not determine the Jacobian isogeny class in this natural genus-five family.

## Assumptions and scope
The characteristic is prime to \(15\), and the specified congruences are essential for the maximality of the untwisted curve over \(K\). No statement is made about primes in other residue classes, non-diagonal deformations, or a complete classification of all \(K\)-forms of the underlying geometric curve. The fifteen classes refer to the image of the **specified diagonal coefficient family** in \(K^\times/(K^\times)^{15}\); they are not asserted to be fifteen distinct curve-isomorphism classes.

We use the convention
\[
Z(C/K,T)=\frac{L_C(T)}{(1-T)(1-qT)},\qquad
L_C(T)=\det(1-T\operatorname{Fr}_q\mid H^1_{\mathrm{et}}(C_{\bar K},\mathbf Q_\ell)),
\]
for \(\ell\ne p\). All equalities concern the smooth normalization, not the singular plane model's naive point count.

## Proof
**1. Normalization and genus.** On \(x\ne0\) set \(t=y/x\), \(w=z/x\), and \(v=tw\). The function field is
\[
v^3=-t^2(a+bt^5).
\]
The degree-three cyclic cover of the \(t\)-line is totally ramified at \(t=0\), at the five distinct geometric roots of \(a+bt^5\), and at infinity; there is no other ramification. These seven branch places are distinct because \(p\ne 3,5\) and \(a b\ne0\). Riemann--Hurwitz gives \(2g-2=-6+14=8\), hence \(g=5\). The cyclic cover is connected, so the plane quintic is geometrically integral.

**2. A maximal untwisted model.** For \(a=b=1\), the normalized curve \(C_{1,1}\) is maximal over \(\mathbf F_{p^2}\) for precisely the stated prime classes; this is Kudo's theorem [1, Theorem 1.2], proved there using Hermitian coverings. In particular its ten Frobenius eigenvalues all equal \(-p\), since their moduli equal \(p\) and the Hasse--Weil upper bound is attained. Frobenius on the first étale cohomology is semisimple, and the geometric automorphisms below commute with \(\operatorname{Fr}_q\).

**3. The order-fifteen character.** On the untwisted superelliptic model \(v^3=-t^2(1+t^5)\), choose \(\xi=\zeta\), the primitive fifteenth root fixed above. The automorphism
\[
g:(t,v)\longmapsto(\xi^3t,\xi^2v)
\]
has order \(15\). To calculate its characters, consider \(t^i\,dt/v^j\) for \(j\in\{1,2\}\). Its orders at \(t=0\), at infinity, and at each nonzero branch point are respectively
\[
3i+2-2j,\qquad -3i-4+7j,\qquad 2-j.
\]
The five regular monomials are
\[
\frac{dt}{v},\quad\frac{t\,dt}{v},\quad
\frac{t\,dt}{v^2},\quad\frac{t^2dt}{v^2},\quad\frac{t^3dt}{v^2}.
\]
They are independent and, since the genus is five, form a basis of regular differentials. Their respective \(g\)-weights modulo \(15\), from \(3(i+1)-2j\), are \(1,4,2,5,8\). By Serre duality and tame comparison for a finite-order automorphism prime to the characteristic, the ten weights in first étale cohomology are
\[
\mathcal E=\{1,2,4,5,7,8,10,11,13,14\}.
\]
Thus \(\mathcal E\) consists of all eight units modulo \(15\), together with the two primitive third-root exponents \(5,10\). One may also obtain the tame comparison by lifting this Kummer cover, whose seven branch places remain distinct, to characteristic zero and applying smooth proper base change.

**4. Coefficient descent.** Let \(\sigma\) be a geometric fifteenth root of \(a^4b\), and put \(\rho=a/\sigma^3\). Then \(\rho^5=a/b\); the substitution \(t=\rho T\), \(w=\sigma W\) identifies the original curve with the untwisted equation \(TW^3+1+T^5=0\) over the algebraic closure. Because \(a^4b\) has residue exponent \(r\),
\[
\sigma^q/\sigma=\xi^r,\qquad \rho^q/\rho=\xi^{-3r}.
\]
In the coordinates \((T,V=TW)\), the descent cocycle is \(g^{-r}\). It follows that the Frobenius eigenvalues on the twist are \(-p\xi^{rk}\) for \(k\in\mathcal E\), up to simultaneous inversion of all the character labels (which leaves the product invariant). Therefore
\[
L_{a,b}(T)=\prod_{k\in\mathcal E}(1+p\xi^{rk}T).
\]

**5. Four factorizations and frequencies.** The primitive fifteenth-root characters contribute \(\Phi_{15}(-u)\), and the remaining two contribute \(\Phi_3(-u)\), where \(\Phi_m\) is the \(m\)-th cyclotomic polynomial. Multiplication by \(r\) on the weights gives
\[
\begin{array}{c|c|c}
\gcd(r,15)&\text{cyclotomic product}&L(T)\\\hline
15&(1+u)^{10}&(1+u)^{10}\\
1&\Phi_{15}(-u)\Phi_3(-u)&1-u^5+u^{10}\\
3&(1+u)^2\Phi_5(-u)^2&(1+u^5)^2\\
5&\Phi_3(-u)^5&(1-u+u^2)^5
\end{array}
\]
The four displayed polynomials are pairwise distinct. Their residue-class multiplicities follow from the numbers of residues modulo \(15\) with gcd \(15,1,3,5\). Finally, the map \((a,b)\mapsto a^4b\) is surjective on \(K^\times\), with \(q-1\) ordered preimages of each value; every coset contains \((q-1)/15\) elements. This proves the exact coefficient frequencies.

**6. Extension counts and isogeny distinction.** The coefficient of \(T\) gives the claimed base-field point counts. Both middle polynomials have zero coefficients of \(T,T^2,T^3,T^4\), so Newton's identities give \(\#C(\mathbf F_{q^n})=q^n+1\) for \(1\le n\le4\). Their coefficients of \(T^5\) are respectively \(-p^5\) and \(2p^5\); Newton's identities give the stated opposite fifth-extension deviations. Equality of Jacobian isogeny classes over a finite field would force equality of Weil polynomials, so these four spectra represent distinct isogeny classes.

## Verification
Three dependency-free verification programs are supplied. Run `python3 verify_characters.py`, `python3 verify_counts.py`, then `g++ -O2 -std=c++17 verify_extensions.cpp -o verify_extensions && ./verify_extensions` from a directory containing these files. The first independently enumerates the five regular differential monomials using the three valuation inequalities, computes the ten weights, and multiplies their cyclotomic factors exactly in \(\mathbf Z[\xi]/(\Phi_{15}(\xi))\) for all fifteen residues. It compares the complete degree-ten coefficient vectors to the four displayed polynomials.

The second independently counts points on the normalized cyclic cover \(v^3=-t^2(a+bt^5)\) for all fifteen cosets over both \(\mathbf F_{121}\) and \(\mathbf F_{841}\), by explicit field arithmetic and enumeration of cubic residues; the two ramified points above \(0\) and infinity are counted separately. It does not use the character-product routine. The third program certifies irreducibility of its quartic modulus and independently counts every coefficient type over the quadratic extension of \(\mathbf F_{121}\), using a direct cubic-root table in \(\mathbf F_{11^4}\). All outputs appear in `CHECKS.txt`, and all three programs were executed successfully before packaging. Finite counts are consistency checks only; the general-prime and higher-extension assertions follow from the proof, not from extrapolation.

## Relationship to prior work
Kudo and Harashita [2] classified superspecial trigonal genus-five curves over selected small base fields and studied automorphisms; their \(\mathbf F_{11}\)-isomorphism classification and its \(\mathbf F_{121}\)-point counts do not tabulate the fifteen coefficient cosets over \(\mathbf F_{p^2}\) or their Weil polynomials. Kudo [1] proved the superspeciality of the coefficient family and maximality of its untwisted member, and his maximality theorem is explicitly used in step 2 rather than claimed anew. General Galois-cohomological twist and Frobenius methods are described by Meagher and Top [3] for other curves; the abstract method is not new. What is established here is the explicit full character computation and the resulting four-polynomial/fifth-extension classification for this named genus-five family.

## Limitations
These fifteen diagonal coefficient classes are not a classification of all forms or all trigonal genus-five curves. The theorem asserts distinct **isogeny** types, not distinct isomorphism types within each class. The cyclic-cover and maximality arguments require the stated prime congruences. The two finite examples do not constitute a proof for all primes or for the degree-five extension. No independent external validation has been performed; unindexed earlier explicit twist computations or a direct published specialization of general Jacobi-sum formulas remain possible priority risks.

## References
[1] Momonari Kudo, *A note on certain superspecial and maximal curves of genus 5*, first posted 2018-07-12, arXiv:1807.04394, especially Theorems 1.1--1.3 and Section 3. https://arxiv.org/abs/1807.04394

[2] Momonari Kudo and Shushi Harashita, *Superspecial trigonal curves of genus 5*, first posted 2018-04-30, arXiv:1804.11277, especially Theorem B and Section 5. https://arxiv.org/abs/1804.11277

[3] Stephen Meagher and Jaap Top, *Twists of genus three curves over finite fields*, 2010, Sections 1--3 (general Frobenius-on-twists framework; different curves). https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf
