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

# Finite-state verification

Run `python3 verify.py` in a directory containing `CERTIFICATE.csv`. Both files are included with the result.

The script computes exactly, using Python integers, all 24 nonzero residue-pair states at depths 0 through 40. It checks the simultaneous certificate \(S_{28}=S_{16}\), \(H_{28}=H_{16}+4\), and \(J_{28}=J_{16}-4\) for **every state**. It verifies the twelve listed initial extrema and all eight transitions needed to extend the recurrence to \(r\geq8\), then compares 16384 ordinary Stern prefixes against an independently computed binary-block prefix algorithm and checks \(D(2190712)=-6\) and \(D(8693112)=12\).

The universal depth extension is mathematical induction using the exact three prefix recurrences, not an inference from a large finite search. The certificate is a deterministic, small, independently reproducible finite calculation; its results do not amount to an external mathematical audit. A separate review of the proof and literature priority remains unperformed.
