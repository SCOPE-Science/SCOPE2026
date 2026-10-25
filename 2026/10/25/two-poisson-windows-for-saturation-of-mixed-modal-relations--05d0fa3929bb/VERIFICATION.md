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

Run `python3 check_mixed_modal.py` using Python 3 standard library only.

The checker separately computes Boolean compositions by row-wise union and by explicit existential quantification. It exhaustively checks the equivalence between the universal-valuation modal mixed axiom and the two composition inclusions for every reflexive triple on one, two or three worlds. Every valuation is tested. It also checks the exact expected hole counts at edge probability \(p=1/2\) by rational arithmetic.

Verified enumerations: for two worlds, \(16\) pairs of base relations allow \(25\) third-relation expansions with hole distribution \(\{0:9,1:6,2:1\}\). For three worlds, \(4096\) pairs allow \(11006\) expansions and hole distribution \(\{0:2342,1:576,2:786,3:280,4:93,5:18,6:1\}\). The checker prints `MIXED_MODAL_CRITICAL_WINDOW_CHECK_OK` on success.

The asymptotic Poisson claims are not experimentally certified. They rely on the explicit uniform external-intermediate witness estimate and the factorial-moment proof in RESULT.md. Independent audit has not been performed.
