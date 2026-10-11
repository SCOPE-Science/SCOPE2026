# Bond degree is the linking-number speed of the bonded-braid power family
## Finding
Let \(BB_n\) be the bonded braid monoid and let \(\Phi_p:BB_n\to B_n\), \(p\in\mathbb Z\), be the family introduced by Lambropoulou and Lorenzi. Suppose \(\beta\in BB_n\) has pure forgetful image \(\Phi_0(\beta)\in P_n\). Let \(d_B(\beta)\) be the bond degree: each braid generator has degree \(0\) and each bond generator has degree \(1\). The defining relations preserve this degree.

If \(d_B(\beta)>0\), then there is an intrinsic vector
\[
b(\beta)\in\mathbb N^{\binom n2},\qquad \sum_{i<j}b_{ij}(\beta)=d_B(\beta),
\]
such that, for every \(p\in\mathbb Z\),
\[
\lambda(\Phi_p(\beta))=\lambda(\Phi_0(\beta))+p\,b(\beta),
\]
where \(\lambda:P_n\to\mathbb Z^{\binom n2}\) is the pairwise-linking vector of the ordered oriented closure. Hence the total pairwise linking number \(T=\sum_{i<j}\operatorname{{lk}}_{ij}\) obeys
\[
T(\widehat{{\Phi_p(\beta)}})=T(\widehat{{\Phi_0(\beta)}})+p\,d_B(\beta).
\]
In particular, the oriented links \(\widehat{{\Phi_p(\beta)}}\) are pairwise non-isotopic as \(p\) ranges over distinct integers.

## Assumptions and scope
The conclusion concerns bonded braids whose forgetful braid is pure; therefore every \(\Phi_p(\beta)\) has trivial strand permutation and its standard closure has \(n\) canonically oriented components. Isotopy is orientation-preserving; no claim is made after independently reversing component orientations. The theorem requires positive bond degree. The statement uses the homomorphisms of Theorem 4.6 of Lambropoulou--Lorenzi and the standard Artin generators \(A_{ij}\) of \(P_n\).

## Proof
Theorem 4.6 sends braid generators identically and sends an overpassing bond \(b_{ij}\) to \(A_{ij}^{p}\). A threaded bond is sent to a pure conjugate
\[
C A_{ij}^{p} C^{-1},
\]
with \(C\in P_n\). Thus changing \(p\) never changes the permutation of a bonded-braid word. Since \(\Phi_0(\beta)\) is pure, so is every \(\Phi_p(\beta)\).

Artin's presentation of \(P_n\), reproduced in the source paper, abelianizes to the free abelian group on the classes of the \(A_{ij}\). Under standard closure, the class of \(A_{ij}\) contributes \(+1\) to the linking number of components \(i,j\) and \(0\) to all other pairs. Hence the abelianization is exactly the pairwise-linking map \(\lambda\).

Choose any word for \(\beta\). Group its ordinary braid letters into blocks and regard each bond image as a pure factor. Move the pure bond factors successively to the right across the ordinary braid blocks. Conjugation by a pure braid does not change abelianization; conjugation by an arbitrary braid only permutes the basis classes \([A_{ij}]\) according to its strand permutation. Therefore each bond contributes exactly \(p\) times one standard basis vector to the difference
\[
\lambda(\Phi_p(\beta))-\lambda(\Phi_0(\beta)).
\]
Summing over the \(d_B(\beta)\) bond factors gives
\[
\lambda(\Phi_p(\beta))-\lambda(\Phi_0(\beta))=p\,b(\beta)
\]
for a vector \(b(\beta)\) with nonnegative integral coordinates whose coordinate sum is exactly \(d_B(\beta)\). Because the left side is determined by \(\beta\), this vector is independent of the chosen word; equivalently
\[
b(\beta)=\lambda(\Phi_1(\beta))-\lambda(\Phi_0(\beta)).
\]
Summing coordinates yields the total-linking formula. If \(p\ne q\), then the two total pairwise linking numbers differ by \((p-q)d_B(\beta)\ne0\), so the oriented closures cannot be isotopic.

## Verification
The proof was checked directly against the defining bonded-braid presentation and Theorem 4.6: every defining relation preserves the number of bond letters, and every bond image has the form of a pure conjugate of \(A_{ij}^{p}\). The Artin presentation shows that its generators have independent abelianized classes. The closure of \(A_{ij}\) is a positive full twist of the indicated pair, so its linking-coordinate contribution is \(+1\). No finite experiment or unproved enumeration is used.

## Relationship to prior work
Lambropoulou--Lorenzi construct the surjective, noninjective homomorphisms \(\Phi_p\) and describe the image of every threaded bond, but their paper does not discuss linking numbers or pairwise-linking vectors. The present statement turns the parameter \(p\) into an exact classical-link invariant along every pure bonded-braid input of positive bond degree and proves that the resulting closures form an infinite family of distinct oriented links. Artin's classical pure-braid presentation supplies the abelianization used in the argument but contains no bonded-braid parameter family.

## Limitations
The result distinguishes oriented closures. It does not assert that the links remain distinct after arbitrary component-orientation reversals, mirroring, or forgetting orientation. It also does not classify the vector \(b(\beta)\) from the bonded-link isotopy class alone, nor does it claim that pairwise linking numbers classify the resulting links.

## References
1. S. Lambropoulou and L. B. Lorenzi, *On pure braids and bonded braids*, arXiv:2609.35340v1 (2026), especially Theorem 4.6 and the presentation of \(P_n\).
2. E. Artin, *Theory of braids*, Ann. of Math. (2) 48 (1947), 101--126.
