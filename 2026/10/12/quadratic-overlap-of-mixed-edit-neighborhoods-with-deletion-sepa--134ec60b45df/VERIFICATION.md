---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The explicit four residue classes n=4r+c (c=4,5,6,7) yield centers u_c0110v_c and u_c1001v_c. A shared one-deletion output would require a one-symbol shift across all four differing positions, impossible because 0110 has consecutive 11, so deletion sets are disjoint. For the mixed edit balls, the six-bit nondeterministic scanner recognizes zero-operation, substitution and a single adjacent shift; determinized pair scanner has exactly 64 states. A direct independently implemented output-set enumerator checked deletion separation and overlap floor(n²/4)+4 for n=4..22. Separately independently reconstructed compiled C++ matrix DP checked all 4099 terms in each residue class (CERTIFICATE_OK c=4,5,6,7). With X_r=P^r K_c R_c^r in dimension 64×64, Cayley–Hamilton gives a scalar recurrence of order <=4096; adding the cubic annihilator of a quadratic target gives order <=4099. Exact integer first-4099-term equality therefore proves the claimed overlap for all n>=4, not extrapolation from small cases. The 64-bit bound follows from bounded one-edit scripts from any finite-state boundary state; the verification passed without overflow evidence.

## originality

PASS

Sala et al. Section V-B indeed defines exactly the composed I_t(D_t) channel and gives alternating-center distance-one, uncoded lower bounds, so that direct same-model prior is explicitly credited. Here the centers have no common one-deletion shadow (distance two in fixed-length Levenshtein), and a new exact quadratic overlap holds for all n. Their Section V-B does not analyze this deletion-correcting pair in inspected full text; single edit alternatives, individual fixed-length balls, and cross insertion-vs-deletion balls are different channel models.

## value

PASS

The distinct-trace budget under composed deletion/insertion corruption is a natural adversarial reconstruction invariant. A deletion-correcting two-codeword constraint fundamentally removes the easier alternating distance-one witness. An explicit all-length quadratic overlap and exact recurrence certificate supply a nontrivial lower bound even under that structural code condition, and are potentially relevant to trace-count limits. This is an existence bound, not claimed to be extremal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
