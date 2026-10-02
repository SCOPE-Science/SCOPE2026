---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

For the signed-K4 family obtained by subdividing the positive edge opposite the unique negative edge into a positive path of length n, the Zaslavsky signed chromatic polynomial satisfies q P_n(q)=(q-1)^2((q-1)^n(q^2-3q+3)+(-1)^n(2q-3)); consequently no P_n has a real zero above 2, while P_n(2)=0 for every odd n, so 2 is the sharp uniform barrier.

## Correctness — PASS

The transfer identity and sign proof were reconstructed algebraically. The key identity (q-1)(q^2-3q+3)-(2q-3)=q(q-2)^2 is exact. For even n both terms in S_n are positive for q>2; for odd n, (q-1)^n is at least q-1 and the key identity gives strict positivity. At q=2, S_n(2)=1+(-1)^n. The inspected verifier independently checks the closed form against direct signed-coloring counts for n<=4, exact recurrences and finite Sturm certificates, so the infinite statement rests on the symbolic proof rather than finite experiments.

## Originality — PASS

The closest inspected signed-chromatic literature computes signed Petersen graphs, signed complete graphs through five vertices, or signed book-graph families. None of those sources treats this one-edge subdivision family or states the closed form or sharp barrier 2. The published-corpus semantic search returned the present record as the only direct match for the exact family formula.

### Equivalent formulations

Those are different graph families and do not give the audited transfer formula.

### Broader coverage

A generic outer zero-free disc does not imply the exact real half-line (2,infinity) or the attained endpoint.

### Exact database or table comparison

No prior exact table or formula matching this family was located.

### Claim versus prior implication

The all-n recurrence and the sharp endpoint require additional structure beyond a fixed K4 computation.

## Value — PASS

A sharp all-n zero-free boundary for a canonical one-parameter deformation of the smallest unbalanced complete graph is a motivated structural statement about signed chromatic roots. The barrier is attained infinitely often, so the result is not merely a loose finite bound.

## Sources inspected

- Git tree/blobs: RESULT.md, fallback_table.json and complete verifier source. Checked the transfer recurrence, symbolic identities, finite checks and normalization.
- Beck et al., arXiv:1311.1760: abstract and scope. Covers signed Petersen graphs and signed complete graphs up to five vertices, not this subdivision family.
- Sehrawat-Bhattacharjya, arXiv:2206.08580: abstract and scope. Covers signed book graphs, a distinct family.

## Residual risks

- The literature search cannot exclude an obscure equivalent formula under switching-equivalent graph terminology, but no such source was found. The result is explicitly limited to Zaslavsky signed-chromatic normalization.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
