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

# Verification

The included standalone `verify.py` is an exact executable finite certificate with no third-party dependencies. From the explicitly listed graph edges it enumerates all sixty-five thousand five hundred thirty-five nonempty vertex subsets, checks equivalence of forbidden-three-path recognition and induced-component recognition, and reconstructs the entire face poset.

It then reproduces the stated vertex-pivot face pairing, verifies all matched pairs are valid disjoint Hasse covers, and topologically sorts the *entire* directed Hasse graph after reversing matched edges. The absence of any remaining directed vertices certifies acyclicity and the exact list of four critical cells. It additionally reduces all simplicial boundary matrices over \(\mathbb F_2\) as a separate consistency check.

The stored verification output is an actual completed execution of the embedded program, ending `VERIFY_OK`; successful replay should reproduce the same output. The integral homotopy conclusion uses discrete Morse theory and the critical CW dimensions, not a finite-dimensional mod-two inference. No independent audit, formal proof-assistant check or external replication is claimed.
