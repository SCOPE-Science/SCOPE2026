# Review: exact length-five non-overlapping codes

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof starts from the exact SQN characterization of maximum non-overlapping codes. For n=5, left-right symmetry reduces the first partition sizes to a <= b. Eliminating the recursive constraints leaves two scalar branches because the objective is affine first in x4 and then in x3. In the regime a <= b/3, the relevant concave quadratic is increasing throughout its feasible interval and has unique maximum at x2=ab, forcing the simple AB^4 construction. In the complementary regime, the two branches are bounded by 81 q^5 / 1024; the optimized simple construction exceeds that bound for all q >= 4 except q=7, while equality at q=4 and q=8 has equality conditions that again force the simple construction. The q=7 residue is checked exactly over the three possible first-part sizes. Direct SQN evaluation gives the stated q=2 and q=3 exceptions.

The algebraic reductions were checked separately, including the vertex formula and the derivative signs. A standalone finite verification reconstructs the SQN objective and confirms the theorem on a substantial finite range; this is supporting evidence rather than a substitute for the general proof.

The classification follows from equality conditions, not just cardinality: for q >= 4 the optimal SQN size vector is unique up to left-right reversal and recursively forces L2=L1R1, L3=L2R1, L4=L3R1, hence AB^4 or B^4A. Proposition 11 of Stanovnik--Moškon--Mraz then gives N(q,5)=2 binom(q,a).

## Originality — PASS, to the best of our knowledge

Blackburn (2015) proves exact maximum sizes through length three and conjectures that his k=n-1 construction is maximum for every fixed length once q is sufficiently large. Stanovnik--Moškon--Mraz (2024) give the exact SQN formulation, prove the length-four case, and report finite computations for larger lengths; their paper states that no simple formula was available for larger codeword length and notes that the Blackburn construction can fail at length five. Their 2025 constrained-code follow-up still cites those finite unrestricted computations rather than an all-q length-five theorem.

Searches under non-overlapping codes and the synonymous terms cross-bifix-free, mutually uncorrelated, strongly regular, and strong comma-free, together with exact length-five notation and formula variants, did not locate the all-q formula for S(q,5), the q=4 sharp threshold for Blackburn's construction, or the classification and count of all maximum codes. Recent 2025--2026 work located in adjacent overlap-free variants studies restricted or generalized overlap conditions rather than this exact unrestricted extremal problem.

Residual risk remains that an older synchronization paper, thesis, or differently indexed source contains the same n=5 consequence without exposing it in searchable terminology. Originality is therefore asserted only to the best of our knowledge.

## Value — PASS

Length five is the first codeword length beyond the previously proved exact length-four formula in the modern SQN framework. The result replaces finite parameter computations by a closed formula for every alphabet size, proves Blackburn's structural conjecture at n=5 with a sharp threshold, and determines every maximum code and their exact number for q >= 4. The proof also isolates why the small q=2,3 behavior is exceptional.

## Scientific limitations

The result is restricted to length five and depends on the previously proved SQN characterization. It does not resolve length six or higher. The theorem gives only the maximum cardinalities at q=2,3, not a classification or count of all maximum codes at those two exceptional alphabets. Literature coverage is broad but cannot exclude an obscure equivalent formulation.
