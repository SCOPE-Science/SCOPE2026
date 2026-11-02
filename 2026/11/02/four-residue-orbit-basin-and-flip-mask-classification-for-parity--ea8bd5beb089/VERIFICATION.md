---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

The theorem is a symbolic all-integer proof. The programs are finite checks intended to detect errors, not an assertion of an exhaustive search over all graph orders or an external audit.

1. Run `python3 check_linear.py` using Python 3; it regenerates all two-subset disjointness matrices, performs independent \(\mathbb F_2\) Gaussian elimination and verifies the four classes for \(5\le n\le17\). Compare with `check_linear.out`, which terminates with `LINEAR_VERIFY_OK`.
2. Build the independent C++ verifier with `c++ -O2 -std=c++17 check_states.cpp -o check_states`; run `./check_states`. It enumerates exactly \(2^{10}+2^{15}+2^{21}=2{,}130{,}944\) states over \(n=5,6,7\). Compare its exact counts to `check_states.out`, which terminates with `STATES_VERIFY_OK`.
3. Run `python3 check_flips.py` to enumerate allowed spatial two-cycle flip masks for every \(5\le n\le16\), using independent image-column construction and direct even-cut enumeration; compare `check_flips.out`, ending in `FLIPS_VERIFY_OK`.
4. The infinite-family proof is the incidence-matrix derivation in RESULT.md. Its only graph assumptions are \(KG(n,2)\) and \(n\ge5\); the software does not claim to verify all \(n\).

The C++ binary is intentionally omitted as a platform-dependent build product; the complete source is embedded. No external computational certificates or datasets are needed. The results were reviewed against the stated theorem by the self-review; independent audit is not performed.
