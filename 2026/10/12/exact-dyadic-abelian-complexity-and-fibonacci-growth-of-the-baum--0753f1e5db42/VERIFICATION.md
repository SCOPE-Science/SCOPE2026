---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Four-letter substitution sigma(A)=AB, sigma(B)=CB, sigma(C)=BD, sigma(D)=DD with coding A/B to 1 and C/D to 0 yields recurrences of the binary-digit Baum--Sweet definition. At every level, D_k is zero and A_k=B_k+C_k coordinatewise; therefore each aligned block is coordinatewise bounded by A_k. Each length-2^k shifted window is a suffix and prefix of adjacent aligned blocks and is dominated by a cyclic rotation of A_k, proving the sharp maximum. Block weights satisfy Fibonacci recursion with initial 1,2; arbitrarily long D blocks and one-step window changes give complete interval spectra. Monotonicity sandwiches all n between dyadic scales to prove growth. An independently written digit-word/window enumeration checked dyadic maxima through k=12 and complete spectra through k=9, but the all-n proof is symbolic.

## originality

PASS

The Merta source contains the digit recurrences and infinite zero runs, while Cicalese--Liptak--Rossi establish general abelian-complexity / prefix-normal relationships. Neither materially inspected primary paper states the coordinatewise four-block domination of all shifted Baum--Sweet factors, exact Fibonacci dyadic spectra or this exponent. A general complexity-computability algorithm is weaker than a closed exact formula.

## value

PASS

The word is a classical automatic sequence, and abelian complexity is a standard natural combinatorial invariant. An explicit infinitely long dyadic spectrum and global noninteger exponent answer a substantive structure question, not a rediscovery of the Fibonacci one-count of prefixes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
