---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Writing \(y=M_1\) and \(z=y+1=x(x+1)\), the simultaneous \(x\)- and \(x+1\)-valuation reduces on \(\mathbb F_2[y]\) to the \(z\)-valuation. For the normalized states \(B_n\), the submitted factorization gives an exact block transition \(B_n\mapsto B_{n+t}\) in exactly \(t\) odd steps, with all but the last block step having valuation one. The block index strictly increases, cannot pass the next power of two, and its two-adic valuation increases at block boundaries, so the total step count telescopes to the distance from \(n\) to that power of two. A fresh exact bit-polynomial implementation independently replayed every allowed starting index through \(R=8\), checking each block endpoint and intermediate valuation; the universal conclusion rests on the symbolic block proof.

## originality

PASS

The focal paper states this exact formula as Conjecture 3.1 after presenting computations; its full text contains examples but no proof. Fresh Resultary and web searches for the family, exponent window, and \(j+1\) sequence length did not locate a later proof or stronger theorem. Related polynomial-Collatz papers study general stopping/periodicity questions or different families and do not imply this exact block identity.

## value

PASS

The result proves a named, explicit conjecture about an infinite family in a current polynomial-Collatz paper and explains the exact length through a structural block transition rather than extending a finite census. This is a natural exact dynamical fact with clear mathematical motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
