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

The analytic proof is self-contained in `RESULT.md`. The standalone `verify.py` implements Clifford monomials by exact bit masks and phases in \(\{1,i,-1,-i\}\). It was executed from the packaged working path and returned:

`VERIFY_OK N=4:full_product=-I:sector_dim=2^0 N=8:full_product=+I:sector_dim=2^7 N=12:full_product=-I:sector_dim=2^22 N=16:full_product=+I:sector_dim=2^45`

For those four values it exhaustively checks all subsets of the first \(N-1\) corrected stars, verifies that their Majorana support is the corresponding cut, verifies that no nonempty subset has empty support, verifies pairwise commutation and involutivity, and verifies scalarity of the full-star product. The alternating sign shown for the full product is specific to the verifier's lexicographic edge/star ordering and is not part of the theorem.

The finite replay is not an exhaustive proof for arbitrary \(N\). The all-\(N\) proof rests on parity of \((N-1)(N-2)/2\), connectivity of \(K_N\), the primary source's tracelessness proposition, and the character-projector trace calculation. No spectrum inside an individual symmetry sector is computed or certified here.
