---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

From the explicit poset relations, every linear extension is a product of disjoint allowed adjacent swaps; these are exactly matchings, with the descent number equal to matching cardinality. The Stanley binomial expansion gives Omega(t)=sum_k m_k binom(t+n-1-k,n). Differentiation yields [t]Omega=(1/n!)sum_k(-1)^k m_k k!(n-1-k)!. Removing one distinguished edge from a (k+1)-matching proves (k+1)m_{k+1}<=(n-1-k)m_k, and hence the alternating magnitudes decrease. All induced subposets (in particular ideals/filters) reindex within the same family, so Ferroni–Morales–Panova Theorem 3.4 applies to all coefficients. Shifting t->t+1 gives strict Ehrhart positivity. Independent permutation enumeration and direct matching-polynomial comparison checked 127 (n,E) cases through n=7, with 896 factorial-scaled coefficients and exact zero-linear cases (2,1),(3,3); this is corroboration, not the universal proof.

## originality

PASS

Theorem 3.4 in Ferroni–Morales–Panova is a hereditary reduction, not a universal width-two positivity statement; their Section 7.1 explicitly conjectures width-two positivity, while their proven skew cell poset and fence cases are different definitions. The result constructs the required missing positive linear coefficient for the path-incomparability family, so it is not simply an application absent a new check.

## value

PASS

The proof supplies a natural hereditary all-dimensional width-two class, including the complement zig-zag example within a live conjectural framework, with an explicit path matching certificate overcoming known finite checks. It does not purport to solve the entire width-two conjecture; deriving all coefficients from a genuinely new linear-term inequality makes this more than a textbook restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
