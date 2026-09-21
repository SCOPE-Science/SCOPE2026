# same-model review

**Overall: PASS under TBOK-v1.** This is a same-model review, not independent validation. The conclusion is qualified by the documented literature scope and access limitation below.

## Exact result audited

For every integer n >= 11 and every nonpath tree T of order n, one of A = S(2,2,n-5) and B = S(2,4,n-7) has strictly more zero forcing sets than T at one of the cardinalities 2, 3, n-4. Consequently there is no greatest nonpath tree under coefficientwise zero forcing polynomial order. The finite quotient poset of tree polynomials has at least two coatoms below the path.

## Correctness: PASS

The proof uses the published hanging-path concatenation inequality of Menon-Singh, Proposition 3.13, to dominate every nonpath tree by a three-leaf spider while preserving the vertex count. Each merge removes exactly one leaf; the process stops before becoming a path. A greatest element would therefore have to dominate all spiders, and the explicit witness argument in RESULT.md is stronger than this observation.

The arm-state enumeration checks both initial colors of the center. An inactive arm contains neither a leaf nor adjacent chosen vertices. It can finish after the center is blue without using a center force exactly when its first vertex was chosen. Thus at least two arms must be independently completable, and when the center starts white at least one must be active. Subtracting the cases with no active arm proves the full generating identity, not just a numerical pattern. Extracting coefficients gives the known z2 = 9 - 2t and the needed z3 = 13n - 66 + 2r for arms at least two. Boundary cases of arm length two are explicitly included.

For n >= 11, z2 first rules out every spider with a length-one arm. Among the remaining spiders, z3 is uniquely maximized, up to arm permutation, by A. A has a four-vertex fort, whereas B has no fort of size at most four. The latter is proved separately according as the center lies inside or outside the fort. This gives the strict inequality at n-4 and completes the universal quantifiers. No claim that A or B itself is maximal is needed.

Reproducible computation was actually run: `python3 artifacts/spider_check.py`. Complete coefficient vectors were checked on all 41 spiders of orders 4-12. Every initial set was tested both by forcing closure and by independently enumerated forts followed by a subset-containment computation. The path formula from Boyer et al., Proposition 5, was compared with computed values at every cardinality for orders 2-12. Witnesses A/B were additionally checked at orders 11-15; exact outputs appear in RESULT.md. These finite checks support the analytic proof and are not substituted for it.

## Originality: PASS within the stated scope

The problem was formulated before candidate-originality screening, after inspecting Menon-Singh's transformation and their Section 4 poset question. The gap is our restricted inference about nonpath trees, not an author's explicit identical conjecture.

### Equivalent and stronger coverage checked

The coefficientwise assertion was translated into (i) absence of a universal second-best or runner-up tree, (ii) nonuniqueness of a maximal element after removing the path in the finite quotient poset, equivalently multiple coatoms in the tree subposet, and (iii) absence of a simultaneous optimizer of uniform-k zero forcing probabilities. Division by binomial(n,k) eliminates the probability normalization. The high-coefficient comparison was also translated into the presence or absence of forts of size at most four. Counts of inclusion-minimal forcing sets and counts of minimal forts were distinguished from counts of all fixed-cardinality forcing sets. Independent Bernoulli sampling is not asserted equivalent to coefficientwise order.

Recorded searches include initial exact-target, spider, polynomial extremal, and nonpath-tree directions. Final searches used maximal trees, second tree, spiders, coatoms, maximum number of forcing sets, and nonpath forcing probability. Search misses are not treated as evidence of noncoverage; primary sources and implications were checked as follows.

The closest transformation is Menon-Singh, Proposition 3.13 and its injection proof (retrieval, offsets 20500-27000). It reduces trees to spiders but cannot compare three-arm spiders without leaving the nonpath class. Section 4, offsets 28900-30000, asks about the poset and coatoms without resolving this restricted case.

Boyer et al., Theorem 22, Claim 4 (retrieval, offsets 44600-46500), already provides z2 = 9 - 2t. The zero-length omission in the stated range for t does not justify a novelty claim: their count applies to t = 0 too. Their argument distinguishes spiders from cycles, not from each other. All spiders with arms at least two remain tied under this count. The present z3 computation breaks this tie and supplies the particular extremizer that conflicts with the fort criterion.

The closest broader graph-class extremal result inspected is German, *The Path-Extremal Conjecture for Zero Forcing*, Theorem 1 (distance-hereditary graphs) and Theorem 2 (conditional split-decomposition extension), with proofs, retrieval, offsets 14500-38000. Specialization gives the path bound but no optimizer after removing the path. Neither the conclusion nor its leaf/twin induction gives the required comparison among nonpath trees.

The final audit followed the fort reformulation to Becker et al., *On the number of minimal forts of a graph*, Theorem 17 and proof (retrieval, offsets 28200-32400), and Nguyen-Kenter, *On the Number of Zero Forcing Minimal Forts on Trees*, Theorem 1 and Lemma 4 with proof (retrieval, offsets 0-6500 and 16500-21900). Becker's structural proof can supply the small-fort part of our argument. Nguyen-Kenter bounds the total number of minimal forts and characterizes individual minimal forts in all trees. Neither total counts nor these individual-set descriptions imply the required low-coefficient optimization by parameter substitution. Counting fixed-cardinality transversals of all forts and identifying the incompatible extremizers remains necessary. Theorem 17's proof does not perform that optimization. We credit the fort component as standard rather than treating it as a second new theorem.

*Minimal Zero Forcing Sets*, arXiv:2204.01810v2, Propositions 2-3 and proofs (retrieval, offsets 7800-12800), gives spider examples with polynomial versus exponential counts of inclusion-minimal sets. Its constructions do not compare the fixed-cardinality forcing polynomials or settle the runner-up question.

The actual residual is the sharp z3 dependence on the number of length-two arms, used after the known z2 restriction, and the deduction that this uniquely forced candidate loses at n-4. This is not inferred from search failure or from the general path conjecture being open.

## Value: PASS

This is a modest structural extremal result. It answers a natural restricted part of the published poset question for every order at least 11 and explains why the path maximum has no universal successor within trees. A fixed pair of competitors and only three cardinalities give a certificate against every proposed runner-up. The result combines a sharp low-cardinality optimization with a conflicting high-cardinality obstruction, rather than merely giving two incomparable examples (which alone would not rule out a greatest element).

Limitations: it does not classify all coatoms, prove the two displayed spiders maximal, settle arbitrary-graph path extremality, establish the smallest possible threshold, or prove any analogous statement for Bernoulli forcing probability. No algorithmic speedup or direct engineering application is claimed. The separate known lemmas are not claimed as original.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

**ACCESS_LIMITATION:** Baoxin Li, Yahan Cao and Shengjin Ji (2025), *The Extremal Results for Forcing Problem of Trees*, DOI https://doi.org/10.1007/s00373-025-02925-6. This is the most plausible inaccessible source because it studies tree forcing extrema. Full text was not obtained through available channels. A publisher PDF location was identified, but its full text remained unavailable.

Available snippets refer to minimum-cardinality forcing, connected forcing and total forcing extrema, not an asserted matching counting theorem. The possibility of a relevant theorem in the unread text remains unverified. There is possible topical relevance, but no concrete unresolved evidence asserting the present conclusion or a stronger counting result. This is an access limitation, not verified noncoverage. The PASS is permitted under TBOK-v1 on that basis, with the mathematical correctness and value assessments separately passing. Any later equivalent or stronger source would require revising the originality verdict.

## Recorded review qualifications

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.
