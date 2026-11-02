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
# Exact verification

Run `python3 HEAWOOD_CHECK.py` (Python 3.9+; standard library only). The program reconstructs the graph from a dot-product Fano-plane incidence rule, enumerates signed cubical boundaries, checks \(d_1d_2=0\), and verifies chain ranks over \(\mathbb F_2\) and \(\mathbb F_3\). It then performs explicit unimodular row/column operations obtaining \(153\) unit factors and a residual rank-one matrix of gcd \(2\). This determines the complete Smith form and the integral groups.

The same program verifies that the graph first homology is the entire image of the configuration-to-graph chain map, generates all \(336\) collineations and point-line dualities, checks their automorphism property, computes signed cellular fixed-point traces, groups the conjugacy classes, verifies both irreducible-character orthogonality identities, and confirms three rational quotient Betti vectors.

Expected final line prefix: `HEAWOOD_2CONFIG_FULL_336_CHARACTER_AND_INTEGRAL_SMITH_OK`.

The checker has been executed on the exact extracted package file. All computations are finite and exhaustive; the transfer to the continuous configuration space uses the cited finite-model theorem. This check does not assert an integral isotypic splitting, a cup-product calculation, or independent external validation.
