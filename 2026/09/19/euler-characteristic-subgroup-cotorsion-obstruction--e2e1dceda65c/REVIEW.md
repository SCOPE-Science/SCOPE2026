# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness: PASS

The proof was checked at the category, ideal, orthogonality, approximation, and object-obstruction stages.

The category \(\mathcal A_B=\{X:\chi(X)\in B\}\) is extension closed because Euler characteristic is additive, and weak idempotent completeness follows because the Euler characteristic of a split complement is a difference of two elements of \(B\). Contractible complexes have Euler characteristic zero, so the standard cone sequences provide enough projectives and injectives for every subgroup \(B\le\mathbb Z\).

The key uniform device is the pair of correction stalks \(R_-(r)\) and \(R_+(r)\), supported respectively in degrees \(\le0\) and \(\ge2\), with arbitrary prescribed Euler characteristic \(r\). They allow every low- or high-support cohomology piece to be enlarged to Euler characteristic zero. This proves the object-ideal equalities without any divisibility assumption on \(B\).

The extension bifunctor is the usual degreewise-split one:
\[
\operatorname{Ext}^1(X,Y)\cong\bigoplus_n\operatorname{Hom}_k(H^n(X),H^{n+1}(Y)).
\]
The consecutive-stalk test objects \(S^{n+1}(k)\oplus S^{n+2}(k)\) and \(S^{m-1}(k)\oplus S^{m-2}(k)\) have Euler characteristic zero, so the reverse ideal-orthogonality inclusions work uniformly for all \(B\).

Completeness of the ideal pair was checked using explicit correction-stalk cone sequences. In the precover construction, the kernel \(U[-1]\oplus R_+(\chi(U))\) has Euler characteristic zero and high support; in the dual construction, the cokernel \(V[1]\oplus R_-(\chi(V))\) has Euler characteristic zero and low support. The maps satisfy the defining cohomology-vanishing conditions for the two ideals.

For object approximations, the long exact sequence forces the middle object's cohomology to be exactly \(H^{\le0}(A)\) or \(H^{\ge2}(A)\), proving necessity of the subgroup conditions. The ordinary undistorted cone sequences prove sufficiency. The witnesses \(S^0(k)\oplus S^1(k)\) and \(S^1(k)\oplus S^2(k)\) have total Euler characteristic zero but truncated Euler characteristic one, so they obstruct both sides for every proper subgroup \(B<\mathbb Z\). Since every proper subgroup of \(\mathbb Z\) omits \(1\), the dichotomy is sharp.

## Originality: PASS

Originality is qualified to the best of our knowledge. Ren--Wang, arXiv:2609.18681v1, was inspected in the sections defining the Frobenius category, object ideals, special ideal approximations, parity obstruction, and idempotent completion. It treats the even-total-cohomology case, equivalently \(B=2\mathbb Z\), and does not state a congruence/subgroup family or the completeness-if-and-only-if-\(B=\mathbb Z\) theorem.

Wang--Wang--Zhu, arXiv:2609.14382v1, was also inspected. Its counterexample is built from a half-space \(\lambda\ge0\) for an exact-additive integer-valued function and is explicitly not weakly idempotent complete; it does not imply the subgroup construction here.

Targeted searches for combinations of Euler characteristic, congruence/subgroup conditions, ideal cotorsion pairs, and object completeness located the recent parity paper and general cotorsion literature, but no equivalent subgroup-parametrized theorem. General ideal approximation theory and standard facts about bounded complexes are treated as prior art.

The main residual risk is implicit coverage in older exact-category or \(K_0\)-theoretic literature under more abstract language. This risk is meaningful because the extension becomes short once the correction-stalk mechanism is identified. No concrete prior theorem subsuming the result was found. No specific inaccessible source emerged as a likely source of the exact statement.

## Value: PASS

The result identifies the parity example as one point in a complete subgroup family and isolates the actual mechanism: membership of truncated Euler characteristics in an additive subgroup of \(K_0(\operatorname{vect}_k)\cong\mathbb Z\). It provides a sharp classification within this family: complete ideal cotorsion pairs occur for every subgroup, whereas object completeness occurs only for the full subgroup \(\mathbb Z\).

The extension is not merely the replacement of “even” by “divisible by \(m\)”: for \(m>2\), total cohomology dimension is not exact-additive modulo \(m\), while Euler characteristic is. The theorem also includes the infinite-index subgroup \(B=\{0\}\), for which no fixed-multiplicity doubling argument suffices. The explicit correction-stalk construction gives a uniform mechanism across all subgroups.

## Scope and limitations

The theorem concerns the specific Frobenius exact categories cut out inside bounded finite-dimensional complexes by subgroups of the integer Euler characteristic. It does not claim that every additive invariant or every exact category admits the same construction, nor does it settle completeness descent in arbitrary idempotent-complete or abelian exact categories.

No independent validation, formal verification, or exhaustive-literature guarantee is asserted.
