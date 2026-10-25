# Scientific review: rare symmetry of commutative idempotent magmas

## Correctness — PASS

The exact formula for a fixed permutation is the orbit-product count over unordered pairs, with each orbit of length \(\ell\) contributing \(|\operatorname{Fix}(\sigma^\ell)|\). A transposition gives exactly \(p_n=n^{-(n-2)}(1-2/n)^{\binom{n-2}{2}+1}\). The support deficit \(D(\sigma)\ge k(2n-k-2)/4\) gives a uniform bound on all non-transpositions. Outside that bound, more than one transposition cannot coexist in an automorphism group. This establishes the explicit finite-\(n\) error, the sharp asymptotic constant, and the conditional full automorphism-group type. The standalone checker exhausts all tables for \(n=3,4\) and verifies permutation orbit identities up to \(n=7\). Finite checking is not used as an infinite proof.

## Originality — PASS within examined coverage

Bergman and Szendrei (arXiv:1901.06316, Lemma 5.4) show generic asymmetry, but their inspected full text does not establish the sharp rare-symmetry rate, exact transposition contribution, or the conditional one-transposition group law. Tureček (arXiv:2305.00269, Theorems 4 and 10) develops exact Burnside counts for unrestricted magmas. OEIS A030257 and A030259 list related exact small-order isomorphism class counts; these are known and credited. Indexed mathematical-result searches for equivalent random automorphism and transposition-event formulations did not yield the asserted combined limit. The full Cardó paper arXiv:2312.02863 could not be examined, leaving a material but not decisive priority risk. Novelty is not asserted with exhaustive certainty.

## Mathematical value — PASS

A sharp rate for exceptional symmetry refines the known qualitative rigidity statement in a natural, unrestricted commutative-idempotent variety. The complete conditional stabilizer classification distinguishes one isolated transposition from every other symmetry type, and the same proof quantifies the first correction to unlabelled enumeration. Neither correctness nor computation alone motivates the result: its value lies in resolving this structural rare-event question.

## Limits and literature risk

The result supplies asymptotics rather than exact arbitrary-order labeled counts and gives no structural census of extremely rare larger automorphism groups. Full-document comparison with arXiv:2312.02863 remains unresolved. All other comparison assertions refer only to inspected material, not unseen portions of papers.

Self-review: passed. Independent audit: not yet performed.
