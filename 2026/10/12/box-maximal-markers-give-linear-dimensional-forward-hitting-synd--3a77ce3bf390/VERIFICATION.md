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

The proof was reconstructed from the definitions rather than inferred from numerical experiments.

For the free \(\mathbb Z^n\)-model, define the conflict graph by coordinate displacement in \([-r,r]^n\setminus\{0\}\). Its degree is finite. The maximal-independent-set construction used in the motivating paper applies to this finite-range graph through the same \(O(\log^* N)\) LOCAL mechanism. Independence in this graph directly excludes every forbidden pair of forward shifts of coordinate size at most \(r\).

For any starting point, shift first by \((r,\ldots,r)\). Maximality supplies a marker within coordinate displacement at most \(r\) in each direction. Undoing the centering gives a forward displacement vector in \([0,2r]^n\), hence total length at most \(2nr\). This is the only quantitative estimate.

The finite-window labeling with this hitting budget then satisfies the hypotheses of the LOCAL equivalence and Borel transfer stated as Theorems 3.2 and 3.3 in Gao--Hu--Zou. No finite enumeration, probabilistic certificate, or unproved limiting argument is used.

Limits: the proof does not establish sharpness; it applies only to the free part and preserves the bounded-to-one assumptions. The full text of the related Shinko--Weilacher--Yu preprint was not independently inspected.
