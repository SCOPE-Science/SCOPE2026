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

# Reproduction and limits

Use Python 3 with the standard library. Run `python3 verify.py` in the directory containing the embedded research files. A successful run reports `PASS: 51565 exact rational assertions; n=2..10; varied tree topologies and edge signs.`

The test program derives the covariance by unique path products, derives the inverse precision separately by edge contributions, checks their exact product is identity, checks the signed edge-sum-of-squares PSD decomposition coefficient by coefficient, verifies the null vector and the explicit sampling weights, and cross-checks both paths and stars for equal-magnitude edge correlations. It includes a heterogeneous signed five-vertex example.

The finite checks validate concrete identities; they do not exhaust the infinite set of trees and real edge correlations. For all-dimensional correctness, use the constructive sign vector, diagonal PSD equivalence, sum-of-squares identity, and uniqueness proof in RESULT.md. The literature comparison is not an independently certified originality guarantee. Independent mathematical audit has not been performed.
