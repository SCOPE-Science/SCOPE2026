# Scientific review of the mixed-involution universality enumerator

## Correctness — PASS

A greedy arch is the shortest prefix seeing all symbols; terminal missing-letter witnesses show its count is the exact subsequence-universality index. For a word fixed by an involutive antimorphism, opposite greedy-arch families leave a central remainder; the presence or absence of all letters there determines whether the full index is odd or even. For mixed involutions, the even center must already contain every fixed letter, while the odd center can supply one omitted fixed letter. Enumerating proper-support remainder alphabets with those two conditions yields the explicit series \(E\) and \(O\), and summing arch counts proves the claimed rational function. Least-degree coefficients give the stated extremal lengths and numbers. Two standalone, independently structured exhaustive programs passed; their tests do not replace the proof.

## Originality — PASS, qualified

Barker et al. (arXiv:2003.04629, Proposition 15) provide ordinary-palindrome universality criteria and arch machinery. Adamson (arXiv:2304.04583) counts unrestricted universal words algorithmically. Mahalingam et al. (DOI:10.1016/j.ic.2021.104863) investigate Watson–Crick palindrome conjugates rather than the subsequence-universality distribution. Existing exact descriptions of the two pure involution cases are acknowledged as prior coverage and excluded from the new theorem's parameter domain. The mixed case has both fixed letters and transposed pairs, producing new explicit support polynomials and all-length coefficients not implied by simply specializing either pure case. A more general unpublished or unindexed formula could still cover this case; no negative novelty claim is inferred merely from failed searches.

## Mathematical value — PASS

The orbit structure of involutions has three natural regimes: identity, fixed-point-free, and mixed. This closes the mixed regime with a complete length/index distribution, not a single numerical example. The odd-center effect creates a sharp \(f-1\) excess for the shortest odd-order universal word and an exact number of extremizers. These facts matter for constructing and enumerating symmetric subsequence-rich words when some alphabet letters are self-complementary and other letters occur in complementary pairs. The work does not assert an error-correcting code or biochemical stability.

## Residual limitations

The comparison does not establish absolute priority against every unindexed source. The result counts indexed finite words under a specified involution; cyclic, unlabeled, and physical-molecular versions are different questions. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
