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

Proved binary scaling P_(2^k d)=P_d via t(2^k q+s)=t(q) xor t(s), and global complement closure via adding a new high leading bit. For odd d, a 192-state carry+parity transducer tracks x+jd for j=1,2,3, with carry bounds c_j<=j. Higher zero bits of d plus guessed bits of starting n are handled by exact reverse reachability, not finite prefixes. Independently reimplemented both transitions and subset determinization without using the source verifier: precisely 195 reachable subsets after initial odd bit, with output masks 0x6e (5), 0xf7 (6), 0xff (184); zero cycles and all one-bit edges establish A only d=1, B only d=3, C all other odd d. Corresponding relative-mask sizes 5,7,8; complement gives 10,14,16. Checker addresses all unbounded input words because finite reachable graph is exhausted. Supplemental finite prefix computations are not infinite proof.

## originality

PASS

Joshi--Rust's automata theorem gives length>=4 monochromatic arithmetic progressions for each difference with odd part>1, but no nonmonochromatic four-word spectrum. Aedo et al. study maximum monochromatic runs and their arithmetic scaling, while Avgustinovich--Fon-Der-Flaass--Frid study union-over-d arithmetical complexity. The fixed-difference 14-versus-16 separation at d odd-part3 is not implied by any of these statements. The 2003 primary complete work remains unread.

## value

PASS

It resolves a natural fixed-step factor-spectrum invariant of the canonical automatic sequence for **every** d and includes a subtle exceptional odd part 3. The 195-state exact certificate is a substantive all-input classification useful for automatic-sequence factors, not an arbitrary small sampled table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
