# Automorphism-orbit classification of local Rota–Baxter operators on the three-dimensional nilpotent evolution chain
## Finding
Let \(k\) be an algebraically closed field of characteristic zero, and let \(E\) be the evolution algebra with natural basis \(e_1,e_2,e_3\) and multiplication
\[
e_1^2=e_2,\qquad e_2^2=e_3,\qquad e_3^2=0,\qquad e_i e_j=0\ \text{for}\ i\ne j.
\]
Write
\[
T=T(d_1,d_2;r_1,r_2,r_3)
\]
for the linear map
\[
T(e_1)=d_1e_1+r_1e_3,\qquad T(e_2)=d_2e_2+r_2e_3,\qquad T(e_3)=r_3e_3.
\]
The recent local Rota–Baxter classification implies that the weight-zero local Rota–Baxter operators on \(E\) are exactly those maps for which
\[
(d_1,d_2)\in \{(0,0)\}\cup\{(0,2\alpha):\alpha\in k^\times\}\cup\{(4\alpha,2\alpha):\alpha\in k^\times\},
\]
with \(r_1,r_2,r_3\in k\) arbitrary.

Up to conjugation by \(\operatorname{Aut}(E)\), these operators admit the following complete and nonredundant classification for each fixed invariant triple \((d_1,d_2,r_3)\).

If \(r_3\ne d_1\), there are exactly two conjugacy classes, represented by
\[
T(d_1,d_2;0,0,r_3),\qquad T(d_1,d_2;0,1,r_3).
\]
They are distinguished by whether \(r_2=0\).

If \(r_3=d_1\), there are three isolated classes, represented by
\[
T(d_1,d_2;0,0,d_1),\qquad T(d_1,d_2;1,0,d_1),\qquad T(d_1,d_2;0,1,d_1),
\]
and a one-parameter family represented uniquely by
\[
T(d_1,d_2;\Delta^2,\Delta,d_1),\qquad \Delta\in k^\times.
\]
For an operator with \(r_1r_2\ne0\), the parameter is the conjugacy invariant
\[
\Delta=\frac{r_1^2}{r_2^3}.
\]
Thus the raw parameter space of local operators collapses generically to two symmetry classes for fixed diagonal data, while a genuine one-dimensional modulus survives exactly on the resonance hypersurface \(r_3=d_1\).

## Assumptions and scope
The field is algebraically closed of characteristic zero. Algebraic closedness is used only to normalize a nonzero \(r_1\) by a cube root or a nonzero \(r_2\) by a square root on the coordinate axes. The both-nonzero resonant normal form uses no root extraction. The statement concerns conjugation by algebra automorphisms of \(E\), not arbitrary similarity in \(\operatorname{GL}(E)\).

The local Rota–Baxter classification itself is taken from Qaralleh, Mukhamedov and Khakimov, arXiv:2606.22623v1, Example 4.1 and Theorem 3.4. The present finding is the subsequent orbit classification under the intrinsic algebra automorphism group.

## Proof
Every algebra automorphism is determined by the image of \(e_1\), because \(e_2=e_1^2\) and \(e_3=e_2^2\). Write
\[
\phi(e_1)=ae_1+be_2+ce_3.
\]
Then
\[
\phi(e_2)=a^2e_2+b^2e_3,\qquad \phi(e_3)=a^4e_3.
\]
Invertibility forces \(a\ne0\). Since \(e_1e_2=0\), multiplicativity also gives
\[
0=\phi(e_1)\phi(e_2)=ba^2e_3,
\]
so \(b=0\). Conversely every map
\[
\phi_{a,c}(e_1)=ae_1+ce_3,\qquad \phi_{a,c}(e_2)=a^2e_2,\qquad \phi_{a,c}(e_3)=a^4e_3,
\]
with \(a\in k^\times\) and \(c\in k\), is an automorphism. Hence these are all automorphisms of \(E\).

In the ordered basis \((e_1,e_2,e_3)\), direct multiplication gives
\[
\phi_{a,c}\,T(d_1,d_2;r_1,r_2,r_3)\,\phi_{a,c}^{-1}
=T\!\left(d_1,d_2;\ a^3r_1+\frac{c}{a}(d_1-r_3),\ a^2r_2,\ r_3\right).
\]
Therefore \(d_1,d_2,r_3\) are conjugacy invariants.

Suppose first that \(r_3\ne d_1\). For any chosen \(a\ne0\), choosing
\[
c=-\frac{a^4r_1}{d_1-r_3}
\]
kills the transformed \(r_1\). If \(r_2=0\), this gives the first representative. If \(r_2\ne0\), algebraic closedness supplies \(a\) with \(a^2r_2=1\), giving the second. Since zero versus nonzero of \(r_2\) is invariant under multiplication by \(a^2\), the two representatives are not conjugate.

Now suppose that \(r_3=d_1\). The parameter \(c\) drops out, and the action on \((r_1,r_2)\) is the weighted scaling
\[
(r_1,r_2)\longmapsto(a^3r_1,a^2r_2).
\]
The zero pattern of \((r_1,r_2)\) is invariant. Algebraic closedness gives the representatives \((1,0)\) and \((0,1)\) on the two nonzero axes. If \(r_1r_2\ne0\), then
\[
\Delta=\frac{r_1^2}{r_2^3}
\]
is invariant. Conversely, putting \(a=\Delta r_2/r_1\) sends \((r_1,r_2)\) to \((\Delta^2,\Delta)\), because
\[
a^3r_1=\Delta^2,\qquad a^2r_2=\Delta.
\]
Thus equal values of \(\Delta\) are sufficient as well as necessary for conjugacy in the both-nonzero resonant locus. This proves completeness and uniqueness of the listed representatives.

## Verification
The included `verify.py` checks the multiplication table, derives the displayed automorphism and inverse matrices, and verifies the conjugation formula by exact rational arithmetic on a deterministic family of parameter choices. It separately checks the nonresonant elimination formula and the resonant identity sending \((r_1,r_2)\) to \((\Delta^2,\Delta)\), together with invariance of \(r_1^2/r_2^3\). The replay output is stored in `verification_output.txt` and terminates with `CHECK_OK`.

These computations are consistency checks. Completeness over an algebraically closed field is proved symbolically above and is not inferred from finite enumeration.

## Relationship to prior work
Qaralleh, Mukhamedov and Khakimov classify the local weight-zero Rota–Baxter operators on nilpotent evolution algebras of maximal nilindex and, in their three-dimensional chain example, give exactly the three raw diagonal strata used here. Their paper also studies parameter-space dimensions and ordinary Rota–Baxter operators commuting with automorphisms, but document-wide searches found no conjugacy-orbit classification of local operators. The earlier paper arXiv:2601.08669v1 classifies ordinary Rota–Baxter operators on the same class of algebras, again without an orbit quotient by \(\operatorname{Aut}(E)\).

The present statement is not a restatement of the source parameterization: it identifies the intrinsic isomorphism classes of local operators under algebra automorphisms and detects the resonance \(r_3=d_1\) as the unique locus where a continuous modulus survives.

## Limitations
The normal forms on the two resonant coordinate axes use algebraic closedness. Over a general characteristic-zero field, those axes split further according to cube and square classes. The theorem treats only the three-dimensional chain algebra and weight zero. It does not classify local operators in higher dimension or in positive characteristic.

## References
1. I. Qaralleh, F. Mukhamedov, O. Khakimov, “Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex,” arXiv:2606.22623v1, first posted 2026-06-21. https://arxiv.org/abs/2606.22623
2. I. Qaralleh, F. Mukhamedov, O. Khakimov, “Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex,” arXiv:2601.08669v1, first posted 2026-01-13. https://arxiv.org/abs/2601.08669
