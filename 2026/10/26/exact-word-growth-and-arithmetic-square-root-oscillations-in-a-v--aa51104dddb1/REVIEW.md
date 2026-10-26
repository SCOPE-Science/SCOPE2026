# Self-review

**Finding reviewed:** Exact word growth and arithmetic square-root oscillations in a valuation-parity spacing shift.

## Correctness — PASS

For binary spacing words whose every two occupied sites have odd 2-adic separation valuation, an even/odd index splitting is exhaustive: occupied sites must occupy one parity, and after division by two the target valuation parity flips. The complementary even-valuation language permits independent choices in the two parity classes. This proves the coupled all-length word-count recursions, including the duplicated empty-word adjustment. At fourfold lengths they imply exactly \(p(4n)=2p(n)^2-1\), giving the claimed Chebyshev iterates and distinct normalized logarithmic limits. Monotonicity transfers square-root growth to every length. The binary-residue-tree sparsity bound gives a uniformly vanishing density of ones and hence the unique invariant probability. Periodic-point and nonsofic arguments cover all configurations. An independently coded finite mask enumerator checked both recursion branches to length 18, plus fourfold and exact integer iterative identities; these checks do not replace the infinite proof.

## Originality — PASS (qualified by search coverage)

Actual search and primary-text comparisons addressed spacing-shift entropy, hereditary dynamics, hierarchical 2-adic spacing, and the exact displayed integer subsequences. Ahmadi Dastjerdi–Dabbaghian Amiri (arXiv:1110.6144) and Kwietniak (arXiv:1111.0190) establish general zero-entropy/hereditary implications rather than this exact word-count recursion and nonconstant square-root normalization. Banks–Nguyen–Oprocha–Stanley–Trotta, *Dynamics of spacing shifts*, discusses different lacunary allowed-difference examples and their dynamical properties. OEIS A002812 and A001601 already record the integer iteration values: numerical uniqueness is expressly disclaimed. No inspected source proves this same 2-adic all-pairs word-count identity, nor a stronger classification that implies it. A prior result couched as independent sets in hierarchical valuation graphs could still cover the theorem; this is a residual priority risk, not a claim of independent certification.

## Mathematical value — PASS

The parity of a difference's 2-adic valuation provides a natural recursive pairwise-spacing constraint, sharply distinct from ordinary successive-gap shifts. Its exact coupled recursions reveal intermediate growth \(\exp(\Theta(\sqrt n))\), zero entropy with unique invariant measure, and a genuinely nonconvergent normalized square-root complexity law with exact algebraic constants. The coupled structural and asymptotic classification is not merely a table recomputation; the independently known Chebyshev sequences serve as explicit solutions of a newly identified symbolic recurrence. It offers a reproducible representative of a natural hierarchical spacing class and distinguishes its full finite-block information from entropy alone.

## Limits and closest literature

The accumulation set across *all* lengths is not determined, and the classification is restricted to prime two and the two valuation parities. The generic hereditary/proximal implications are not claimed to be new. The strongest outstanding originality risk is an unindexed equivalent hierarchical graph/independent-set enumeration. Earlier relevant primary articles and exact OEIS sequences are acknowledged in the finding's references.

Self-review: passed. Independent audit: not yet performed.
