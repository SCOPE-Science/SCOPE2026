# A length-two binary counterexample to the static-code extension corollary
## Finding

Corollary 3.1.5 of Fakieh and Nauman states that if \(V\) is an \(M\)-static right \(R\)-module, \(C\) is an \(M\)-static code of length \(n\) over \(V\), and \(f:C\to V^n\) is an embedding, then \(f\) is an isomorphic isometry and is the restriction of a monomial transformation.

The statement fails over the smallest field with a length-two coordinate-line code. Let
\[
R=M=V=\mathbb F_2,\qquad n=2,
\]
and let
\[
C=\{(0,0),(1,0)\}\subset V^2.
\]
Define
\[
f:C\longrightarrow V^2,\qquad f(a,0)=(a,a).
\]
Then \(V\) and \(C\) are \(M\)-static, and \(f\) is an injective \(\mathbb F_2\)-linear map. However,
\[
\operatorname{wt}(1,0)=1,\qquad \operatorname{wt}(f(1,0))=\operatorname{wt}(1,1)=2.
\]
Thus \(f\) is not a Hamming isometry. Every monomial transformation preserves Hamming weight, so no monomial transformation of \(V^2\) can restrict to \(f\). Both conclusions of Corollary 3.1.5 therefore fail under its stated hypotheses.

The same paper later invokes Corollary 3.1.5 in the proof of Theorem 3.3.2. The counterexample consequently invalidates that proof route as written. It does **not** prove that the conclusion of Theorem 3.3.2 is false by every possible argument.

## Assumptions and scope

The alphabet is the binary field \(\mathbb F_2\), used as the ring \(R\), the module \(M\), and the alphabet module \(V\). The endomorphism ring is
\[
D=\operatorname{End}_R(M)\cong\mathbb F_2.
\]
An embedding is taken in the ordinary module-theoretic sense of an injective linear homomorphism, consistent with the source's use of isometry as a separate conclusion. Hamming weight is the number of nonzero coordinates. A monomial transformation permutes coordinates and applies coordinate automorphisms, hence preserves zero versus nonzero in each coordinate and therefore preserves Hamming weight.

The code \(C\) is already coordinate-split: its first coordinate component is \(\mathbb F_2\) and its second is \(0\). Thus the counterexample also satisfies the coordinate-decomposition convention made immediately before Proposition 3.1.2 in the source.

## Proof

For \(R=M=V=\mathbb F_2\),
\[
\operatorname{Hom}_R(M,V)\cong\mathbb F_2,\qquad D\cong\mathbb F_2,
\]
and the defining evaluation map for staticity is
\[
\operatorname{Hom}_R(M,V)\otimes_D M\longrightarrow V,
\qquad a\otimes b\longmapsto ab.
\]
This is an isomorphism, so \(V\) is \(M\)-static. The code \(C\) is one-dimensional over \(\mathbb F_2\), hence isomorphic to \(M\) as an \(R\)-module; applying the same evaluation calculation gives
\[
\operatorname{Hom}_R(M,C)\otimes_D M\cong C.
\]
Therefore \(C\) is \(M\)-static independently of any proposition in the target paper.

The map \(f(a,0)=(a,a)\) is linear. Since its nonzero input maps to \((1,1)\neq(0,0)\), it is injective. But its unique nonzero input has weight \(1\) while its image has weight \(2\). This disproves conclusion (i) of Corollary 3.1.5.

Conclusion (ii) fails as well. Over \(\mathbb F_2\), the only nonzero scalar is \(1\), so the length-two monomial group consists only of the two coordinate permutations. The monomial orbit of \((1,0)\) is
\[
\{(1,0),(0,1)\},
\]
which does not contain \((1,1)\). More generally, the weight mismatch already rules out any monomial extension.

## Verification

The standalone script `artifacts/verify.py` exhausts all three linear embeddings of the one-dimensional code \(C\) into \(\mathbb F_2^2\). Two send the generator to a weight-one vector and are restrictions of coordinate permutations; the third sends it to \((1,1)\), changes the weight, and is not extendable by a monomial map. It also checks linearity and injectivity directly. Running

`python3 artifacts/verify.py`

returns `VERIFY_OK`.

No finite computation is used as a substitute for the proof: the staticity calculation, the weight change, and monomial weight preservation give a complete symbolic argument.

## Relationship to prior work

The target article defines \(M\)-static codes through the Hom--tensor evaluation map, states in Corollary 3.1.5 that every embedding under the stated staticity hypotheses is automatically an isometry and a monomial restriction, and later cites that corollary in the proof of Theorem 3.3.2.

The classical MacWilliams extension theorem does not cover or rescue that statement. Its premise is that the map is already a Hamming isometry; under that premise it asserts extendability to a monomial transformation over a finite field. Here the displayed embedding is deliberately not an isometry, so the classical theorem is inapplicable rather than contradicted.

Exact-title, corollary-number, counterexample, correction, corrigendum, and Morita-invariance searches located the target paper and standard extension-theorem literature but no prior published correction or the same binary counterexample. Semantic searches for static/adstatic codes and monomial extension likewise returned no same-object result. Search failure is not a proof of novelty; it is combined here with direct inspection of the most relevant full texts.

## Limitations

The finding refutes Corollary 3.1.5 under the ordinary meaning of an embedding as an injective module homomorphism. If a revised statement assumes at the outset that \(f\) is a Hamming isometry, this counterexample no longer applies; that is precisely the hypothesis used in standard extension theorems.

The counterexample shows that the proof of Theorem 3.3.2 is not valid insofar as it invokes Corollary 3.1.5. No claim is made here that the conclusion of Theorem 3.3.2 is false or that it cannot be proved under additional hypotheses.

The earliest verified public date used here is the publisher's online date, March 7, 2025. Exact-title searches did not locate an earlier public preprint; an unindexed earlier dissemination remains a bibliographic residual risk.

## References

1. Wafaa M. Fakieh and S. Khalid Nauman, *Static Codes and Monomial Transformations*, JP Journal of Algebra, Number Theory and Applications 64(2) (2025), 181--197, DOI 10.17654/0972555525011.
2. Marcus Greferath, Thomas Honold, Cathy Mc Fadden, Jay A. Wood, and Jens Zumbrägel, *MacWilliams' Extension Theorem for bi-invariant weights over finite principal ideal rings*, Journal of Combinatorial Theory, Series A 125 (2014), 177--193, DOI 10.1016/j.jcta.2014.03.005.
