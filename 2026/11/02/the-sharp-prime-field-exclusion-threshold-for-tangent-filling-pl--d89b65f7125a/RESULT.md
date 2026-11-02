# The sharp prime-field exclusion threshold for tangent-filling plane cubics

## Finding
Let \(p\) be prime and let \(C\subset\mathbf P^2_{\mathbf F_p}\) be an irreducible plane cubic. Call \(C\) **tangent-filling** if every point of \(\mathbf P^2(\mathbf F_p)\) lies on a tangent line at some smooth \(\mathbf F_p\)-point of \(C\). Then:

**Theorem.** For every prime \(p\ge11\), no irreducible plane cubic over \(\mathbf F_p\) is tangent-filling. The prime threshold is sharp: over \(\mathbf F_7\), the geometrically smooth cubic
\[
X^2Y+XZ^2+2Y^2Z=0
\]
is tangent-filling.

The new part is the uniform nonexistence statement, which closes the primes \(11\) and \(13\) not settled by the explicit \(p\ge17\) range of Asgarli–Ghioca's degree-three bound. The characteristic-seven cubic is included solely as a checked sharpness witness, not as an original construction.

## Assumptions and scope
Throughout, fields are exactly the prime fields \(\mathbf F_p\), not their nonprime extensions. Irreducible means irreducible over the stated ground field; geometrically reducible but ground-field irreducible cubics are included. Smooth, singular, and nonsplit cubics are treated separately. ``Coverage'' counts ambient projective \(\mathbf F_p\)-points on the union of *rational tangent lines at smooth rational curve points*, not tangent lines over an extension field.

## Proof
**1. Reduction to maximal elliptic curves at \(p=11,13\).** Let \(C\) be a geometrically smooth plane cubic. Since \(p>3\), its Gauss map is separable, and its irreducible dual \(C^\vee\) has degree six. If the rational tangent lines covered the plane, their dual points would be a blocking set \(B\) in the dual projective plane. As a degree-six curve cannot contain \(p+1>6\) collinear rational points on a line unless it has a line component, \(B\) would be nontrivial. Blokhuis's lower bound for nontrivial blocking sets in prime order gives
\[
|B|\ge 3(p+1)/2.
\]
Distinct rational points on a smooth cubic have distinct tangents by Bézout: two tangency contacts on a line would contribute intersection multiplicity at least four. Thus \(|B|=\#C(\mathbf F_p)\). By Hasse's bound this number is at most \(p+1+\lfloor2\sqrt p\rfloor\). For \(p=11,13\), this equals respectively \(18,21\), exactly \(3(p+1)/2\). Hence a tangent-filling cubic would have to have respectively \(18\) or \(21\) rational points.

**2. Exhaustion of elliptic-curve isomorphism classes.** Every elliptic curve in characteristic \(p>3\) has a model \(E_{a,b}:y^2=x^3+ax+b\) with \(4a^3+27b^2\ne0\); replacing \((a,b)\) by \((u^4a,u^6b)\) gives the same curve. The exact character-sum enumeration
\[
\#E_{a,b}(\mathbf F_p)=p+1+\sum_{x\in\mathbf F_p}\chi(x^3+ax+b)
\]
(with \(\chi(0)=0\)) gives precisely five coefficient pairs attaining \(18\) over \(\mathbf F_{11}\), forming the single scaling class represented by \((a,b)=(1,3)\), and precisely two pairs attaining \(21\) over \(\mathbf F_{13}\), represented by \((a,b)=(0,4)\). The pairs are exactly:
\[
\begin{array}{c|l}
11 &(1,3),(3,1),(4,9),(5,5),(9,4)\\
13 &(0,4),(0,9).
\end{array}
\]
The attached first verifier enumerates all \(p^2\) possible pairs, checks nonzero discriminant, computes point counts, and verifies the scaling orbits. These are exhaustive finite calculations, not extrapolations.

**3. Exhaustion of plane embeddings.** Fix either representative elliptic curve \(E\) and an origin \(O\). All degree-three line bundles are \(\mathcal O_E(2O+T)\) with \(T\in E(\mathbf F_p)\). Translation by a rational point changes this class by a multiple of three. Consequently *every* smooth plane-cubic model of \(E\), up to an \(\mathbf F_p\)-projective transformation, occurs among representatives of \(E(\mathbf F_p)/3E(\mathbf F_p)\). Exact group-law calculations give three cosets in both characteristics. The models can be taken as the usual Weierstrass plane cubic for \(T=O\), and, for \(T=(r,s)\) with \(s\ne0\), the cubic
\[
(X-rZ)Y^2-2sYZ^2-(X^2+rXZ+(r^2+a)Z^2)Z=0.
\]
The latter follows from the rational change of variable \(Y=(y+s)/(x-r)\). The map is the embedding associated to \(|2O+T|\), hence a smooth plane cubic.

Representatives are \(O,(4,4),(7,1)\) for \((p,a,b)=(11,1,3)\), and \(O,(0,2),(0,11)\) for \((p,a,b)=(13,0,4)\). The exact tangent unions have sizes:

| Ground field | Points on each cubic | Ambient points covered by the three models | Total ambient points |
| --- | ---: | --- | ---: |
| \(\mathbf F_{11}\) | 18 | 114, 112, 112 | 133 |
| \(\mathbf F_{13}\) | 21 | 145, 156, 156 | 183 |

The two independent verifiers enumerate every rational point of \(\mathbf P^2(\mathbf F_p)\), evaluate each cubic and its gradient, form each rational tangent line, and count its union. Since each complete embedding coset misses at least 19 points over \(\mathbf F_{11}\) and at least 27 over \(\mathbf F_{13}\), no smooth cubic fills the plane.

**4. Singular and geometrically reducible cases.** If \(C\) is geometrically integral but singular, its normalization is a smooth genus-zero curve over \(\mathbf F_p\), hence \(\mathbf P^1\) (a finite field has no nontrivial genus-zero Severi–Brauer curve). The normalization contributes at most \(p+1\) rational points and the singular locus can contribute at most one further rational point, so \(\#C(\mathbf F_p)\le p+2<3(p+1)/2\) for \(p\ge11\). Such a curve cannot give the required nontrivial blocking set: its dual is irreducible of degree at most six and is not a line in characteristic \(p>3\). If \(C\) is irreducible over \(\mathbf F_p\) but geometrically reducible, its geometric components are three Frobenius-conjugate lines. Every rational point lies in their mutual intersection and is singular; there are no smooth rational points, so it is not tangent-filling.

**5. Larger primes and sharpness.** Asgarli–Ghioca, Theorem 1.1, proves nonexistence for every irreducible cubic when \(p\ge4(3-1)^2(3-2)^2=16\); these prime fields start at \(17\). This completes all \(p\ge11\). At \(p=7\), an exact incidence calculation shows the displayed witness has twelve distinct rational tangents whose union contains all \(57\) ambient rational plane points. To check geometric smoothness directly, its gradient is
\[
(2XY+Z^2,\ X^2+4YZ,\ 2XZ+2Y^2).
\]
Any common zero on a coordinate hyperplane must be zero. On \(XYZ\ne0\), scale \(X=1\); the last two equations give \(Z=-Y^2\) and \(Y^3=2\), while the first gives \(Y^3=5\), a contradiction in \(\mathbf F_7\). Thus no geometric singularity exists.

## Verification
Run `python3 verify_classification.py` (Python standard library) and `python3 verify_incidence.py` (independently structured standard-library computation). Both terminate with `EXACT_PRIME_CHECK_OK` or `INDEPENDENT_INCIDENCE_OK`. The geometric smoothness of the characteristic-seven witness is also checked by `python3 verify_smoothness.py` using SymPy over \(\mathbf F_7\), which reports `GEOMETRIC_SMOOTHNESS_OK`. The proof of the infinite statement relies on the published general theorem and the exact finite classification, not on finite experiments for larger primes. The independent incidence script uses six explicitly written models, while the classifying script constructs them from elliptic-group cosets.

## Relationship to prior work
Asgarli–Ghioca introduced tangent-filling plane curves and proved nonexistence for irreducible cubics over prime fields at least \(17\); their paper does not resolve the primes \(11\) and \(13\). Its question of the least degree of such a curve motivates settling the smallest degree in the remaining range. Their proof supplies the blocking-set reduction, and the new argument adds a complete elliptic-isomorphism and line-bundle-embedding calculation for the two remaining primes. Blokhuis's prime-order blocking-set lower bound is a known input, not claimed as new. The previously exhibited characteristic-seven curve is used for sharpness only. A later paper on covering points *of a plane curve* by lines treats a dual but different asymptotic covering problem and does not imply the two finite classifications.

## Limitations
The classification concerns prime fields, not all finite extensions; it does not settle minimum tangent-filling degree at \(\mathbf F_{11}\) or \(\mathbf F_{13}\) above degree three. The code verifies finite arithmetic and incidence, while the passage from the table to all plane embeddings uses the mathematical fact about degree-three line bundles on elliptic curves. The broad mathematical literature may contain an unindexed prior formulation; no global originality or independent certification is asserted.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first posted 2023-02-26), especially Theorem 1.1, Question 1.5 and Section 2. https://arxiv.org/html/2302.13420v2
2. A. Blokhuis, *On the size of a blocking set in PG(2,p)*, Combinatorica **14** (1994), 111–114 (prime-plane nontrivial blocking-set lower bound).
3. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean and E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042 (2026), a distinct covering problem. https://arxiv.org/abs/2610.13042
