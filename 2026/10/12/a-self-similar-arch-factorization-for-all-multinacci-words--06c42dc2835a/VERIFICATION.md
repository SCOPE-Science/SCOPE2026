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

# Verification instructions and scope

Run `python3 verify.py` with Python 3.9 or newer, using only the standard library. The program reconstructs the substitution \(\sigma_m\), computes its \((m-1)\)-fold letter images and the proposed arches, and checks image lengths, the sole terminal rare-letter property, and arch completeness for \(2\le m\le8\). It then compares the explicitly coded infinite-word factorization with a long substituted prefix, compares all greedy arch endpoints with exactly the locations of \(m-1\), and verifies the arch-gap coding for all available gaps within the first 15,000 symbols for each parameter. It also checks the all-prefix count identity, independently tests the defining scattered-subsequence condition on short prefixes, and verifies six substitution-length identities per alphabet size. The program prints `VERIFY_OK` on success, with counts by alphabet size.

The finite histogram need not exhibit every allowed arch length for large \(m\), since rare coding letters may not appear within the finite sample; the program properly checks that observed gaps belong to the proved set. Infinitely many occurrences of every type and the exact limiting frequencies are justified by primitivity, not a finite census. No independent audit, formal proof certification, or computational proof of the infinite theorem is claimed.
