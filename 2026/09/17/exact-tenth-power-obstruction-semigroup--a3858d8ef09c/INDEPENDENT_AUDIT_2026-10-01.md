# Independent scientific audit — Exact tenth-power stable obstruction set via a numerical semigroup

Audit date: 2026-10-01 (UTC) UTC.

Disposition: **REPAIRED**.

## Correctness

**PASS** — The numerical-semigroup proof was reconstructed. Stable offsets are gaps of Gamma_k=<m to the k-th power-1>. For k=10, every generator reduces to 11T+C N_0 with T=<93,5368> and C=11 to the tenth-1, using Fermat modulo 11, the exact m=4 reduction, and the fact that all larger quotients exceed F(T)=493763. Since C is in T and C=-1 mod 11, the canonical residue decomposition N=rC+11z gives membership iff z is in T. This yields a_10=10C+11F(T)=259379677393 and b_10=11g(T)+5(C-1)=129689838697, with symmetry transferred from the two-generator symmetric semigroup T. Independent arithmetic reproduced the constants. The filed scientific theorem required one correction: the original text incorrectly called exponent 10 a case of Conjectures 10.1/10.2; the primary paper states those conjectures for power-of-two exponents.

## Originality

**PASS** — Benfield--Lippard compute through k<=9 and give only the lower bound |B10|>=129687123005. A separate published SCOPE record proves the general semigroup-gap reformulation and repairs Benfield--Lippard Theorem 10.7, but explicitly does not determine new large-exponent exact values. Resultary searches for the exact three generators and constants found only the audited exact-k=10 record. After removing the false conjecture-domain claim, the exact k=10 reduction and invariants remain best-of-knowledge original.

### Equivalent formulations

The exact claim was compared both in Waring-offset language and in numerical-semigroup language.

Searches: Resultary: exact tenth-power obstruction semigroup B10 1023 59048 25937424600; Resultary: stable Waring exceptions numerical semigroup gaps.

Evidence: A related SCOPE result gives the general gap-semigroup translation but not the exact k=10 generators or invariants.

### Broader coverage

Neither broader source implies the three-generator equality and exact Frobenius/genus values without the record's k=10 reduction.

Searches: Benfield--Lippard arXiv:2404.08193v2 Section 10; SCOPE stable-waring-exceptions-semigroup-correction--04e8548696c7.

Evidence: Benfield--Lippard give only a lower bound for B10; the SCOPE correction gives a general reformulation/lower-bound theorem but explicitly no exact new large-exponent values.

### Exact database or table

The closest exact table does not contain k=10, so there is no known-table recomputation coverage.

Searches: Benfield--Lippard Table 2; Resultary exact-number searches.

Evidence: Table 2 stops at k=9; Corollary 10.8 provides a lower bound for k=10 but not the exact set.

### Claim versus prior implication

The exact claim is not mechanically implied by the prior lower bound/general translation; however, the original assertion about Conjectures 10.1/10.2 was false and is removed in the repaired claim.

Searches: Benfield--Lippard Corollary 10.8; SCOPE semigroup-correction result.

Evidence: The lower bound and general gap translation leave substantial work: proving every m to the tenth-1 lies in the three-generated semigroup and evaluating its gaps exactly.

### Source inspections

- **Integers that are not the sum of positive powers** (https://arxiv.org/abs/2404.08193v2): Assessment: Conjectures 10.1 and 10.2 are for power-of-two exponents, so the filed exponent-10 attribution was incorrect; Corollary 10.8 gives only the lower bound 129687123005. Material read: PDF Section 10.1, including Table 2, Conjectures 10.1--10.5, Theorem 10.7 and Corollary 10.8; page 10 was visually inspected. Evidence: Conjectures 10.1 and 10.2 are explicitly indexed by powers of two; Corollary 10.8 states the lower bound for the tenth-power obstruction set as 129687123005.
- **Stable Waring exceptions as numerical-semigroup gaps: correcting Theorem 10.7 and extending its modular obstruction** (https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-stable-waring-exceptions-semigroup-correction--04e8548696c7): Assessment: covers the general gap-semigroup translation and modular lower bounds, but explicitly does not claim exact new large-exponent values. Material read: full RESULT.md through the connected repository source. Evidence: Its limitations say it does not claim exact values of |B-sub-k| for new large exponents.
- **The generalized Waring problem: A new property of positive integers** (https://doi.org/10.1007/BF02304770): Assessment: develops the generalized Waring framework and invariant exception sets, but does not give the exact exponent-10 three-generator semigroup or its Frobenius/genus values. Material read: complete five-page article, including Theorems 1--4 and the discussion of invariant finite exception sets. Evidence: The article states general existence and threshold results for G(m,r) and g(m,r), with explicit square examples; no exponent-10 exact obstruction calculation appears.

Checked sources: https://arxiv.org/abs/2404.08193v2; Resultary SCOPE stable-waring-exceptions-semigroup-correction--04e8548696c7; Resultary exact-number/generator searches; https://doi.org/10.1007/BF02304770 full text; record artifacts/verify.py and artifacts/verify-output.txt.

Residual risks: Search cannot exclude an unindexed exact k=10 computation.

## Scientific value

**PASS** — The corrected claim exactly determines the first stable obstruction set beyond the source paper's computed range k<=9, improves a published large lower bound to a full semigroup description, and computes its Frobenius number, genus and symmetry. The object and invariant are directly motivated by the source problem, so this remains valuable after the attribution repair.

## Final claim

The stabilized tenth-power offset obstruction set is exactly the positive gap set of <1023,59048,25937424600>, with Frobenius number 259379677393 and genus 129689838697; the semigroup is symmetric and satisfies a_10=2b_10-1. These exponent-10 symmetry identities are analogues of patterns studied by Benfield--Lippard, but exponent 10 is not a case of their Conjectures 10.1 or 10.2, which concern power-of-two exponents. The oddness statement is a genuine exponent-10 case of their Conjecture 10.4.

This audit is a scientific assessment of the claim and supplied evidence. It is not peer review, formal verification, or a guarantee of first discovery.
