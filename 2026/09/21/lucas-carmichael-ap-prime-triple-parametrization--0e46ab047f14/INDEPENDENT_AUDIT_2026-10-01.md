# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** Let \(p<q<r\) be odd primes in arithmetic progression and suppose \(n=pqr\). Then \(n\) is Lucas–Carmichael in the sense \(s+1\mid n+1\) for every prime divisor \(s\mid n\) if and only if there are unique coprime integers \(u>v>0\) of opposite parity and an integer \(w>0\) with \(u^2-v^2\mid2v^2w-3\) such that \((p,q,r)=(uw(u-v)-1,u^2w-1,uw(u+v)-1)\). Each primitive shape lies on one admissible congruence ray; the classical \((6m-1,12m-1,18m-1)\) family is the \((u,v)=(2,1)\) ray.

## C — PASS

Writing \(q+1=h\) and common difference \(d\), the three Lucas–Carmichael divisibilities reduce exactly to \(h-d\mid d(2d-3)\), \(h\mid d^2\), and \(h+d\mid d(2d+3)\). With \(g=\gcd(h,d)\), \(h=gu\), \(d=gv\), coprimality forces \(g=uw\), hence \(h=u^2w\), \(d=uvw\). The outer conditions become divisibility of \(2v^2w-3\) by both \(u-v\) and \(u+v\); same parity is impossible, and opposite parity makes these two factors coprime, yielding the single modulus \(u^2-v^2\). Reversing the algebra gives the converse and uniqueness. The fixed-shape admissibility argument correctly treats primes dividing the modulus, primes outside it, and the parity restriction. The finite artifact checks are supplementary, not the proof.

Residual risk: No unconditional infinitude of prime values is proved; the ray-admissibility consequence is conditional on the prime-tuples conjecture as stated.

## O — PASS

The open Einsele–Paterson 2024 article was inspected through its full HTML section on Lucas–Carmichael numbers with three prime factors. It develops general counting bounds and normalized shifted-factor variables but contains no “arithmetic progression” occurrence and no audited AP iff parametrization. OEIS A290810 records the known special ray \(6m-1,12m-1,18m-1\), confirming that this ray is prior art rather than the full theorem. Resultary returned an earlier 2026-09-20 SCOPE theorem on a different primitive-gcd uniqueness question, not AP classification.

Residual risk: Older Guy/De Koninck references and obscure arithmetic-progression treatments were not exhaustively inspected in full.

### Equivalent formulations

**Searches:** Resultary: Lucas-Carmichael three prime factors arithmetic progression parametrization; Einsele–Paterson 2024 full-text search for “arithmetic progression” and three-prime Lucas–Carmichael; OEIS A290810

**Evidence:** Einsele–Paterson treat three-prime Lucas–Carmichael counting but do not mention arithmetic progression. A290810 gives only the special \((6m-1,12m-1,18m-1)\) ray.

**Reasoning:** No inspected source states an equivalent all-shape AP iff theorem.

### Broader coverage

**Searches:** Einsele–Paterson, DOI 10.1007/s10623-023-01347-w, section 5.3; Resultary earlier primitive three-prime uniqueness theorem

**Evidence:** Einsele–Paterson is broader over arbitrary three-prime Lucas–Carmichael numbers but proves counting bounds under extra symbol assumptions, not an AP structural classification. The earlier SCOPE result classifies the minimum shifted-factor gcd case, a different slice.

**Reasoning:** Broader ambient treatments do not imply the AP parametrization.

### Exact database or table

**Searches:** OEIS A290810 and A006972; Einsele–Paterson reference to a table of Lucas–Carmichael numbers up to \(4\cdot10^{10}\)

**Evidence:** A290810 explicitly records the \((6m-1)(12m-1)(18m-1)\) construction. A finite table of examples does not encode the unique \((u,v,w)\) structural theorem.

**Reasoning:** Known databases cover instances and the classical ray but not the general classification.

### Claim versus prior implication

**Searches:** A290810 special family; Einsele–Paterson normalized three-prime discussion

**Evidence:** The \((2,1)\) ray is a strict special case of the audited shape parametrization. General shifted-factor normalization does not impose the AP relation needed to derive the single congruence modulus.

**Reasoning:** The inspected prior results neither state nor mechanically imply the all-shape iff classification.

### Source inspections

- **Average case error estimates of the strong Lucas test** (https://doi.org/10.1007/s10623-023-01347-w): NOT_COVERING. Trigger: Highly relevant recent primary treatment of three-prime Lucas–Carmichael numbers. Material read: Full HTML section 5.3, including Theorems 18–19 and the three-prime normalization/counting discussion; exact search for “arithmetic progression” returned no occurrence. Method: Full-text primary-source inspection. Evidence: It studies general three-prime counting under symbol assumptions and does not state the AP parametrization.
- **OEIS A290810** (https://oeis.org/A290810): SPECIAL_CASE_PRIOR_ART. Trigger: Exact known parametric AP subfamily cited by the package. Material read: Sequence definition, comments, formula, and cross-references. Method: Exact database inspection. Evidence: It records primes \(6m-1,12m-1,18m-1\) and the resulting Lucas–Carmichael product, exactly the \((u,v)=(2,1)\) ray.
- **Uniqueness of the primitive three-prime Lucas-Carmichael number** (published Resultary record dated 2026-09-20): NOT_COVERING. Trigger: Nearest earlier SCOPE hit in the same number-theory family. Material read: Resultary title and summary. Method: Semantic database inspection. Evidence: It concerns the minimum common shifted-factor gcd, not prime factors in arithmetic progression.

### Residual risks

- Guy (2004, section A13), De Koninck (2008, Entry 399), or other older sources may contain related AP parametrizations that were not available for full inspection.

## V — PASS

Arithmetic progression is a natural structured slice of three-prime Lucas–Carmichael numbers. The theorem replaces an isolated classical parametric family by a complete unique shape/ray classification and connects every shape to an admissible prime-tuple problem. This is a natural exact classification rather than an arbitrary finite slice.

Residual risk: The result is conditional only for infinitude; the iff classification itself is unconditional.

## Overall disposition

**PASSED**
