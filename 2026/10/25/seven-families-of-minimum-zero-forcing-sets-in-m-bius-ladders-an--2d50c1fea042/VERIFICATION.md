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

# Reproducibility and limits

Run `python3 exhaustive.py` and `python3 template_certificate.py` with standard Python 3; neither needs third-party packages. Each has assertions that fail on conflicting counts or graph structures. The corresponding execution records are `exhaustive_output.txt` and `template_output.txt`.

The first script exhausts every four-element subset of each labelled Möbius ladder for \(6\le n\le14\), constructs the token-jumping graph exactly and checks full connectivity. It also exhausts all triples for \(6\le n\le10\). The second computes translated template overlap counts using the at-most-sixteen shifts per ordered template pair; it tests \(6\le n\le13\). Affine congruence stability for \(n\ge13\) is proved in RESULT.md, providing the infinite step. An independent construction of the circular ladder gives the integer closed-walk traces for the finite nonisomorphism witness. All claims beyond those finite test ranges rely on the detailed symbolic arguments, not an asserted exhaustive search of infinitely many sizes.

No external independent audit, expert certification, or formal proof-assistant verification has been performed. Absolute novelty is not certified.
