# Review: exact length-three 2-traceability codes

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The upper bound is driven by a local fiber-privacy lemma. Its two contradiction steps were checked separately: (i) two members of a proper repeated fiber cannot repeat a second coordinate, and (ii) a symbol used by one member in either remaining coordinate cannot occur anywhere else in the code. The global count then uses only exact fiber identities: if `R_i` codewords lie in repeated fibers and there are `G_i` such fibers, coordinate `i` uses exactly `(n-R_i)+G_i` symbols. Privacy makes repeated-fiber memberships disjoint across coordinates. For `n>q`, every coordinate has a repeated fiber, so summing yields `3(n-q) <= n-3`, hence `n <= floor((3q-3)/2)`.

The constructions were checked directly against the definition for every parent set of size at most two and every descendant for `2 <= q <= 30`. The construction proof is uniform: every outsider has two private coordinates, while every two-parent descendant is within Hamming distance one of a parent.

## Originality — PASS, to the best of our knowledge

Blackburn--Etzion--Ng (2010) give the odd-q length-three construction of size `3(q-1)/2`. Owen--Ng (2015) reproduce it while stating that the best leading constant remained unknown, and their new exact work concerns length four. Chen--Chen (2023) is explicitly about optimal length-four 2-traceability codes. The 2019 overview by Kabatiansky and the 2026 Chang--Hsu paper were also checked for nearby coverage at the level available; the latter still describes traceability-code cardinalities as broadly unresolved and focuses its new upper bounds on strengths three and four.

Searches for `2-traceability`, `2-TA`, `length 3`, `M_TA(3,q,2)`, and formula variants did not locate the exact all-q expression, the even-q matching construction, or the fiber-privacy argument. A repository overlap search likewise found no SCOPE record on traceability codes.

Residual risk remains that an older paper, thesis, or survey gives the same short-length theorem under different terminology or as a special case not exposed by searchable metadata. This is why originality is claimed only to the best of our knowledge.

## Value — PASS

The result converts a long-standing explicit length-three lower construction into an exact capacity theorem, determines every alphabet size rather than an asymptotic order, supplies the missing even-alphabet optimum, and fixes the length-three leading constant at exactly `3/2`. The proof mechanism is elementary and reusable: proper repeated fibers force privacy in the complementary coordinates.

## Scientific limitations

The theorem is restricted to length three and strength two. It does not settle longer 2-traceability codes or higher-strength exact capacities. Direct finite verification supports only the constructions; the general upper bound rests on the written proof.
