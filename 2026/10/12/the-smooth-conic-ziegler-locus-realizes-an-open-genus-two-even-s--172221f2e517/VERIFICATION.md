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

# Exact verification and limits

Run `python3 verify.py` from the directory containing this document and the script. The verifier constructs the smooth conic \(P(t)=[1:t:t^2]\) over \(\mathbb Q\) with \(t\in\{0,1,2,4,7,11\}\), enumerates every unordered \(3+3\) partition, computes all nine normalized rational cross-chords and all pairwise intersections in exact integer arithmetic, then checks for exactly six triple points and eighteen double points for every partition. It also exhausts all Möbius maps preserving this six-element branch set by their images on three fixed parameters, obtaining the identity alone. Exact expected output:

`VERIFY_OK six_points=6 partitions=10 distinct_arrangements=10 every_incidence=6x3+18x2 base_mobius_stabilizer=1 fiber=10`

The script verifies an exact **finite witness** of the nonempty incidence-open set and a fiber of cardinality ten. It is not a universal proof of the moduli isomorphism or of genus-two theta classification. Those statements rest on the geometric reconstruction and quotient-space argument in RESULT.md and on the classical theta correspondence in Lange--Ortega, arXiv:1309.6984, Sections 3 and 7. The theorem of Dimca--Sticlaru, arXiv:2312.11928, supplies the already-known value \(\operatorname{mdr}=5\) and non-\(2\)-formality for the smooth-conic arrangements. Neither independent validation nor compactification verification is asserted.
