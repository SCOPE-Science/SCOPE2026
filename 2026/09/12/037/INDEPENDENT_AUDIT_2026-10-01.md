# Independent mathematical audit — SCOPE-20260912-037

**Audit date (UTC):** 2026-10-01 (UTC)  
**Disposition:** passed

## Final claim reviewed

Countable inequality rank in OrdMon: non-reflexive coinserter comparison failure with finite presentability via lambda_2 and lambda_3

## Correctness — PASS

For C the generated order has only the diagonal and pairs a^n b <= b a^n because every generator bottom starts with a and every top starts with b, so no nontrivial generator chain can continue. The same first-letter barrier applies to the tuple generators defining D. Thus p=(a^2 b,a) and q=(b a^2,a) satisfy p<=q componentwise in T(C), while p is neither q nor a D-generator bottom because its second coordinate a is not a^n b; hence p not<=q in D. Separately, lambda_{m+n} follows from lambda_n in left context a^m and lambda_m in right context a^n, so lambda_2 and lambda_3 derive every lambda_n for n>=2. A fresh independent recursion checked these derivations through n=100; the global proof is the semigroup decomposition by 2 and 3, not the finite test.

## Originality — PASS

The primary ordered-algebra source proves preservation of reflexive coinserters/sifted colimits by strongly finitary monads and identifies the ordered-monoid word monad, but it does not cover arbitrary non-reflexive coinserters. The explicit comparison-map failure therefore sits exactly outside the theorem’s hypotheses. No prior source located gives the stated mismatch pair or the simultaneous finite-presentation collapse.

### Equivalent formulations
Reasoning: The Pos comparison failure is genuinely about the non-reflexive coinserter; it is not a relabeling of the reflexive theorem.

Searches:
- Resultary ordered monoid non-reflexive coinserter query
- Adamek-Dostal-Velebil ordered-algebra monads

Evidence:
- No inspected source states the same countable inequation family, mismatch pair or comparison order.

### Broader coverage
Reasoning: Prior broader machinery explains why no contradiction arises but does not imply either the explicit failure or the lambda_2/lambda_3 collapse.

Searches:
- arXiv:2011.13839v2 strongly finitary ordered monads
- finitely presentable algebras for finitary monads

Evidence:
- The main theorem covers reflexive coinserters, not this non-reflexive diagram.

### Exact database or table
Reasoning: No exact database/table coverage was found.

Searches:
- Resultary exact semantic query for a^n b <= b a^n

Evidence:
- Resultary returned the same SCOPE record and an unrelated path-swap presentation, not this result.

### Claim versus prior implication
Reasoning: The final claim is outside, rather than a corollary of, the prior implication.

Searches:
- Theorem-level comparison with arXiv:2011.13839v2

Evidence:
- The prior preservation theorem expressly uses reflexive coinserters; the present pair has no common section.

### Source inspections

- **A Categorical View of Varieties of Ordered Algebras** (arXiv:2011.13839v2). Trigger: closest theorem on strongly finitary ordered monads and coinserter preservation. Material read: primary full text around the equivalence theorem, reflexive-coinserter hypothesis and the free ordered-monoid word monad example. Method: full-text PDF inspection. Assessment: covers reflexive/sifted coinserters but not the record’s non-reflexive diagram. Evidence: The preservation theorem is stated with reflexive coinserters; the word monad T(X)=X* with pointwise order is explicitly among the standard examples.

### Checked sources

- Resultary semantic search
- Adamek-Dostal-Velebil arXiv:2011.13839v2 primary full text
- related finite-presentation literature cited by the record

### Residual risks

- An unindexed example could use the same inequation family; none was located.

## Scientific value — PASS

The result isolates a clean boundary of a standard categorical preservation theorem: the free ordered-monoid monad is strongly finitary yet fails on a concrete non-reflexive coinserter, while the associated countable inequational presentation unexpectedly collapses to two relations. This is a reusable structural example rather than an arbitrary finite computation.

## Limitations

- The bounded computational cross-check is not the proof; the global first-letter and additive derivations are the evidence.
- An unindexed source could contain the same explicit non-reflexive example; none was located.

The finding is accepted on all three scientific axes. No change to `RESULT.md` or `SLOGAN.txt` is proposed.
