# Review of the rank-two code-distortion theorem

**Correctness — PASS.** The full proof reduces dimension-two weight distortion to permutations of projective directions, establishes that all these permutations occur for fields of orders two and three, uncrosses every permutation to an optimal sorted matching, and proves the sharp length bound including necessary and sufficient equality conditions. The field-four obstruction is certified by the even action of the 60-element projective group and explicit ten-column generator matrices. The verifier independently enumerates the finite cases specified in the finding and returns `VERIFY_OK`. Infinite-length claims rely on the explicit proof, not finite enumeration.

**Originality — PASS, with qualifications.** Bennett–Fox–Morrell (arXiv:2607.26261v1, 2026-07-28; LIPIcs APPROX/RANDOM 2026, DOI:10.4230/LIPIcs.APPROX/RANDOM.2026.24) develops the general problem and algorithms, without the specific rank-two sorted-weight formula, sharp bound, equality conditions, or length-ten quaternary obstruction located in its examined arguments. Searches for projective, rank-two, weight-spectrum, and distorted-code formulations did not locate a dominating earlier theorem. Standard projective-group and exchange arguments are known; an unindexed earlier reformulation, including relevant work on finite code equivalence, remains a real residual risk. Absence from searches is not a proof of novelty.

**Value — PASS.** This resolves a natural low-dimensional but nontrivial slice of a recently formalized hardness problem, yielding an exact efficient optimizer rather than a generic approximation and identifying the field transition where the weight spectrum stops determining distortion. The sharp distortion bound and equality classification apply at arbitrary block length, rather than a single enumerated instance.

The main scientific limitation is the restriction to two-dimensional codes and the lack of full coverage of all older projective-code-equivalence literature. Numerical checks are finite even where the proof is uniform.

Self-review: passed. Independent audit: not yet performed.
