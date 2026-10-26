# A complete extremality criterion for two-term Artin–Schreier curves over \(\mathbb F_{p^4}\)

## Finding
For every odd prime \(p\), let \(E=\mathbb F_{p^4}\), \(F=\mathbb F_{p^2}\), and \(a,b\in E^\times\). Let \(C_{a,b}\) denote the smooth projective model of
\[
y^p-y=a x^{p+1}+b x^2.
\]
Set \(N=a^{p^2+1}\in F^\times\) and \(t=2b^p/a^{p+1}\in E^\times\). Then \(C_{a,b}\) attains **one of the two Hasse–Weil extremal point counts over \(E\)** if and only if
\[
\boxed{\ t^{p+1}=N^{-1}-N^{-p}\ }.
\]
In particular, this equality forces \(N\notin\mathbb F_p\). Exactly \(p(p^4-1)\) ordered pairs \((a,b)\in(E^\times)^2\) satisfy the criterion. Thus for every odd prime \(p\) there exist nonzero quadratic and Gold-term coefficients giving maximal or minimal genus-\(p(p-1)/2\) curves already over \(\mathbb F_{p^4}\).

## Assumptions and scope
Here “extremal” means either maximal or minimal, i.e.
\[
\# C_{a,b}(E)=p^4+1\pm(p-1)p^3.
\]
The curve has genus \(g=p(p-1)/2\), because its Artin–Schreier defining polynomial has degree \(p+1\), prime to \(p\). The result counts **ordered coefficient pairs**, not isomorphism classes, and does not assign each pair individually to the plus or minus sign. We assume \(p\) is odd and both coefficients are nonzero throughout.

## Proof
**(1) Extremality is equivalent to a two-dimensional polar radical.** Define the quadratic form on the four-dimensional \(\mathbb F_p\)-space \(E\) by
\[
Q(x)=\operatorname{Tr}_{E/\mathbb F_p}(a x^{p+1}+b x^2).
\]
For each \(x\in E\), the equation \(y^p-y=a x^{p+1}+b x^2\) has \(p\) solutions in \(E\) precisely when \(Q(x)=0\), and no solutions otherwise. Hence \(\#C_{a,b}(E)=1+p\#Q^{-1}(0)\). The trace pairing is nondegenerate, and polarizing gives
\[
B(x,z)=\operatorname{Tr}_{E/\mathbb F_p}\bigl(x(az^p+a^{p^3}z^{p^3}+2bz)\bigr).
\]
Its radical is the zero set of the additive polynomial \(L(z)=az^p+a^{p^3}z^{p^3}+2bz\). Raising to the \(p\)-th power preserves the root set in \(E\) and yields
\[
H(z)=az+2b^p z^p+a^p z^{p^2}.
\]
As \(H\) has nonzero linear coefficient and degree \(p^2\), its \(\mathbb F_p\)-kernel has dimension at most two. Thus \(Q\) has rank two, three, or four. A quadratic form of rank two in four variables over odd \(\mathbb F_p\) has \(p^3\pm(p-1)p^2\) zeros, whereas rank three has \(p^3\) zeros and rank four has \(p^3\pm(p-1)p\) zeros. These values follow by diagonalizing its nondegenerate quotient and counting square classes. Consequently, equality in the Hasse–Weil bound occurs **exactly when** \(\dim_{\mathbb F_p}\ker H=2\).

**(2) Coefficient comparison for complete splitting.** The separable additive polynomial \(H\) has \(p^2\) distinct roots in \(E\) precisely when an additive quadratic-degree-in-Frobenius polynomial \(K(z)=dz+ez^p+fz^{p^2}\) satisfies
\[
K(H(z))=z^{p^4}-z.
\]
For the forward direction, take the linearized subspace polynomial of the image \(H(E)\) and normalize its leading coefficient; the composition is the monic degree-\(p^4\) polynomial vanishing on all of \(E\). The converse follows because this composition identity makes every \(E\)-root of \(H\) and the induced image dimensions compatible, or directly because \(H\) then right-divides \(z^{p^4}-z\) and is separable of degree \(p^2\). (More explicitly, any additive right divisor of this separable polynomial has all its roots in \(E\).)

In the identity, comparison of coefficients of \(z\), \(z^p\), and \(z^{p^4}\) determines
\[
d=-a^{-1},\qquad e=t=\frac{2b^p}{a^{p+1}},\qquad f=a^{-p^3}.
\]
The two remaining intermediate coefficients give
\[
t^{p^2}=-t,
\qquad
-a^{p-1}+t\,(2b^p)^p+a^{p^2-p^3}=0.
\]
Dividing the latter equality by \(a^{p^2+p}\) is equivalent to
\[
t^{p+1}=a^{-p^2-1}-a^{-p^3-p}=N^{-1}-N^{-p}.
\]
Therefore splitting implies the asserted criterion. Conversely, if this criterion holds, \(w=N^{-1}-N^{-p}=t^{p+1}\) is nonzero, and \(w^p=-w\) since \(N\in F\). It follows that \(w^{p-1}=-1\), hence
\[
t^{p^2-1}=(t^{p+1})^{p-1}=-1,
\]
which supplies the other intermediate coefficient equation \(t^{p^2}=-t\). All five coefficients of \(K\circ H\) therefore agree with \(z^{p^4}-z\). This proves the equivalence.

**(3) Exact coefficient-pair count and existence.** The norm map \(E^\times\to F^\times\), \(a\mapsto N=a^{p^2+1}\), is surjective with kernel of size \(p^2+1\). The right side \(w=N^{-1}-N^{-p}\) vanishes precisely when \(N\in\mathbb F_p^\times\). For every other \(N\), \(w^p=-w\), hence \(w^{p-1}=-1\). As \(p\) is odd,
\[
w^{(p^4-1)/(p+1)}=(w^{p-1})^{p^2+1}=1.
\]
The cyclicity of \(E^\times\) implies that \(t^{p+1}=w\) has exactly \(p+1\) nonzero solutions. Each pair \((a,t)\) determines exactly one \(b\in E^\times\), since \(b^p=t a^{p+1}/2\) and Frobenius is bijective. There are \(p^2-p\) allowed norms \(N\), so the total is
\[
(p^2-p)(p^2+1)(p+1)=p(p^4-1).
\]
This number is positive for every odd prime. The proof is complete.

## Verification
Run `python verify.py` using Python 3; it has no third-party dependencies. The program constructs \(\mathbb F_{3^4}\) and \(\mathbb F_{5^4}\) by explicit polynomial arithmetic, exhaustively enumerates all \(6400\) and \(389376\) nonzero ordered coefficient pairs, independently computes the polar-matrix rank and the criterion, and checks their exact agreement. The observed extremal counts are \(240\) for \(p=3\) and \(3120\) for \(p=5\), agreeing with the general formula. A direct point-count calculation confirms one extremal witness for each prime. Finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work
Almeida Filho, Tafazolian and Vieira (2026, arXiv:2610.17476, §10, Question 10.4) ask when the predicted field-size threshold for maximal/minimal van der Geer–van der Vlugt curves with nonzero \(x^2\) term can be attained. Their explicitly exhibited small cases do not include a uniform construction for all odd primes with \(h=1\). The theorem above supplies such a construction **and a complete coefficient criterion and exact model count** over \(\mathbb F_{p^4}\). The general kernel/splitting viewpoint is established in prior work, especially Ito–Tatematsu–Tsushima (arXiv:2412.00902), and is not claimed as new. Anbar–Meidl's earlier quadratic-form approach treats in particular coefficient regimes restricted to the prime field, rather than the unrestricted two-coefficient \(\mathbb F_{p^4}\)-parameter space counted here. The specific explicit identity and count were not identified in the checked sources. This is not a proof of priority over every possible unindexed source.

## Limitations
No isomorphism-class enumeration, separate count of maximal versus minimal pairs, characteristic-two extension, or result for \(h>1\) is asserted. The classification is for *models with specified coefficients* and not for geometric isomorphism classes. Its proof is mathematical and is not an independently audited certification.

## References
- G. B. Almeida Filho, S. Tafazolian, and S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (first public October 12, 2026), especially §10 and Question 10.4.
- T. Ito, R. Tatematsu, and T. Tsushima, *Criteria of maximality and minimality of van der Geer–van der Vlugt curves*, arXiv:2412.00902v2 (original preprint December 1, 2024), especially Proposition 4.12.
- I. Bouw and collaborators, *Zeta functions of a class of Artin–Schreier curves with many automorphisms*, arXiv:1410.7031, quadratic-form and additive-polynomial background.
- N. Anbar and W. Meidl, *Quadratic functions and maximal Artin–Schreier curves*, Finite Fields Appl. 30 (2014), relevant prime-field-coefficient criteria.
