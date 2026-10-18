---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For B in F2^{k x r} rank t, f_B(U)=BU^T+UB^T. Under invertible row P and column Q operations, U->P U Q^{-T} conjugates f_B, so kernel dimension only depends on t. In B0=[I_t 0;0 0] normal form, trailing k(r-t) entries free, lower (k-t)x t leading block zero, upper t x t leading block symmetric of dimension t(t+1)/2. Thus dim kernel=k(r-t)+t(t+1)/2, rank=t(2k-t-1)/2, and provided Proposition 5.3 favorable free-code shortest-embedding regime and a fixed G/residue B, affine lifts count 2^{dim kernel}. Ratio for t+1 versus t equals 2^{t+1-k}. Edge t=0 and t=min(k,r), k=1, r=0 formulas hold algebraically. This counts labeled generator extensions, not inequivalent codes.

## originality

PASS

An–Kim–Ling Proposition 5.3 explicitly parametrizes shortest quaternary lifts as an affine translate of this kernel, but the inspected primary article does not state its rank-only dimension, exact lift count, or monotonic search-size law. These are straightforward linear algebra consequences, so priority could exist as folklore or algebraic lemma; assessed claim is the quantitative lift-fiber formula, not the source parametrization.

## value

PASS

The originating embedding search explicitly enumerates candidates from the kernel and optimizes code parameters; a rank-only exact formula tells coding researchers search-branch cardinalities without elimination, monotonic change under rank, and the cost of fixed residue choices in a natural, actually used construction. This is an intrinsically useful uniform algorithmic invariant, not a random tiny instance or claim about monomial equivalences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
