# Classification of maximal nilpotent-free subspaces of two-by-two finite-field matrices

## Finding
For each prime power \(q\), there are exactly
\[
\frac{q^2(q-1)}2
\]
three-dimensional subspaces of \(M_2(\mathbb F_q)\) whose only nilpotent element is zero. They are precisely the hyperplanes
\[
H_C=\{X\in M_2(\mathbb F_q):\operatorname{tr}(CX)=0\}
\]
for projective matrices \([C]\) with irreducible quadratic characteristic polynomial. Their simultaneous classification under conjugation by \(\operatorname{GL}_2(\mathbb F_q)\) is as follows.

For even \(q\), there are \(q/2\) orbits, each of size \(q(q-1)\), represented by companions \(C_d\) of \(T^2+T+d\) where \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(d)=1\).

For odd \(q\), there are \((q+1)/2\) orbits: one orbit of size \(q(q-1)/2\) for trace-zero \(C\) with irreducible \(T^2+d\), and \((q-1)/2\) orbits of size \(q(q-1)\), represented by companions of \(T^2-T+d\) with \(1-4d\) nonsquare. The number of \(d\) in the latter family is \((q-1)/2\).

## Assumptions and scope
All subspaces are linear over \(\mathbb F_q\), contain the zero matrix, and are compared under **conjugation** \(H\mapsto GHG^{-1}\), not arbitrary left-right equivalence. A matrix is nilpotent if some positive power is zero. The field cardinality \(q\ge2\) is an arbitrary prime power; no odd-characteristic assumption is imposed. The **absolute trace** is \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(d)=\sum_{j=0}^{f-1}d^{2^j}\) when \(q=2^f\). Any hyperplane has the form \(H_C\) uniquely up to replacing nonzero \(C\) by a nonzero scalar multiple. Dimension three is maximal for the nilpotent-free property because the full four-dimensional matrix algebra contains nonzero nilpotents.

## Proof
**Step 1 (universal criterion).** Over any field \(F\), the trace pairing \((C,X)\mapsto\operatorname{tr}(CX)\) on \(M_2(F)\) is nondegenerate, so every hyperplane is \(H_C\) for a nonzero \(C\), unique up to \(F^\times\). Every nonzero nilpotent \(N\in M_2(F)\) has rank one and factors as \(N=v\varphi\) for \(0\ne v\in F^2\) and \(0\ne\varphi\in(F^2)^*\) with \(\varphi(v)=0\). Then
\[
\operatorname{tr}(CN)=\varphi(Cv).
\]
If this is zero, both \(v\) and \(Cv\) lie in the one-dimensional kernel of \(\varphi\), and \(v\) is an eigenvector of \(C\). Conversely, if \(Cv=\lambda v\), choosing any nonzero \(\varphi\) annihilating \(v\) yields a nonzero square-zero \(N=v\varphi\in H_C\). Thus \(H_C\) has no nonzero nilpotent element if and only if \(C\) has no eigenvector over \(F\), equivalently its degree-two characteristic polynomial is irreducible over \(F\).

**Step 2 (exact count).** Over \(\mathbb F_q\), the number of monic irreducible quadratics is \((q^2-q)/2\), obtained by pairing the \(q^2-q\) elements of \(\mathbb F_{q^2}\setminus\mathbb F_q\) into Frobenius-conjugate pairs. All matrices with a fixed irreducible quadratic characteristic polynomial are similar, and their centralizer in \(\operatorname{GL}_2(\mathbb F_q)\) has size \(q^2-1\), the unit group of \(\mathbb F_{q^2}\). As \(\lvert\operatorname{GL}_2(\mathbb F_q)\rvert=(q^2-1)q(q-1)\), there are \(q(q-1)\) matrices per polynomial, hence \(q^2(q-1)^2/2\) matrices with irreducible characteristic polynomial. Each projective class \([C]\) has exactly \(q-1\) nonzero scalar representatives. Therefore the number of good hyperplanes is \(q^2(q-1)/2\).

**Step 3 (orbits).** Conjugation carries \(H_C\) to \(H_{GCG^{-1}}\). Hence \(H_C\) and \(H_D\) are conjugate exactly if \(D=\lambda GCG^{-1}\) for some \(\lambda\in\mathbb F_q^\times\), \(G\in\operatorname{GL}_2(\mathbb F_q)\). When \(\operatorname{tr}C\ne0\), a unique scalar makes this trace one. Thus distinct irreducible characteristic polynomials of trace-one matrices label different hyperplane orbits; every such orbit has size \(q(q-1)\), the size of one ordinary conjugacy class. For even \(q\), an irreducible quadratic must have nonzero trace coefficient because every element is a square. After normalization, its polynomial is \(T^2+T+d\); it is irreducible exactly when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(d)=1\), which holds for exactly \(q/2\) values of \(d\).

If \(q\) is odd, nonzero-trace irreducible polynomials normalize to \(T^2-T+d\), irreducible precisely if \(1-4d\) is a nonsquare; exactly \((q-1)/2\) parameters qualify. Trace-zero irreducible matrices have polynomial \(T^2+d\) with \(-d\) nonsquare. Scaling \(C\) rescales \(d\) by a square, so all trace-zero good hyperplanes lie in one conjugation orbit. Each such matrix is similar to \(-C\) (the characteristic polynomial is unchanged), and no other scalar multiple can be similar by comparing determinants. Consequently this hyperplane orbit has exactly half the matrices in the ordinary similarity class, namely \(q(q-1)/2\). The listed orbits account for the total count, in both characteristics. \(\square\)

## Verification
Run the standalone standard-library script `verify.py` using `python verify.py`. It independently enumerates all \(q^4\) matrices, all \((q^4-1)/(q-1)\) projective hyperplanes, all nilpotents, and all invertible conjugations for \(q=2,3,4,5\). It tests the nilpotent-free condition against irreducibility for every hyperplane and recovers the exact orbits. Expected terminal marker: `VERIFY_OK`. Finite exhaustive computation checks those four fields only; the preceding proof supplies the result for all prime powers.

## Relationship to prior work
Wigderson, *Duality for matrix space questions* (arXiv:2609.29177v1, September 24, 2026), Conjecture 8 on p. 5, asks for nilpotent-free spaces of dimension \(n^2-\binom n2\) over finite fields. For \(n=2\) this is three. The published dimension-two construction (published-finding corpus identifier below) proves existence for every field via a quadratic-extension twist, not the count of all extremizers nor their conjugation-orbit classification. For a distinct hyperplane property, de Seguins Pazzis, *Commutators from a Hyperplane of Matrices*, Electronic Journal of Linear Algebra 27 (2014), Proposition 1.5, classifies the **commutator image** of hyperplanes of \(M_2(F)\). That proposition does not test nilpotent avoidance or give these counts. The present result concerns the entire extremal locus and its conjugacy strata, not an improved extremal dimension.

## Limitations
The theorem is specifically about dimension-three linear subspaces of two-by-two matrices, and the specified conjugation group. It does not classify nilpotent-free subspaces of larger matrices or classify these hyperplanes under all linear changes of coordinates on the four-dimensional ambient matrix vector space. Irreducible-quadratic enumeration and projective-quadric geometry are classical; originality of the combined extremal matrix-space census is asserted only relative to the inspected sources, not guaranteed against all older literature.

## References
1. Yuval Wigderson, *Duality for matrix space questions*, arXiv:2609.29177v1 (first public September 24, 2026), Conjecture 8; https://arxiv.org/pdf/2609.29177v1 .
2. *The dimension-two finite-field case of the nilpotent-free duality conjecture*, published published-finding corpus record `2026/10/4/SCOPE-the-dimension-two-finite-field-case-of-the-nilpotent-free-dualit--894e9cc95146`.
3. Clément de Seguins Pazzis, *Commutators from a Hyperplane of Matrices*, Electronic Journal of Linear Algebra **27** (2014), 39–54; https://journals.uwyo.edu/index.php/ela/article/download/1331/1331/1331 .
