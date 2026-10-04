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

The analytic proof is self-contained in `RESULT.md`. The bundled `verify.py` checks, with exact rational arithmetic, the scalar identities that make the biased regular-simplex distribution have mean \(\theta\) and isotropic covariance \((1-\|\theta\|^2)I/d\). It tests several dimensions and rational interior radii, including the five-parameter case.

The critical non-computational steps were also checked directly: the SLD equation reduces to a two-equation Clifford calculation; positivity follows because each effect has scalar part equal to the Euclidean norm of its spin-factor vector part; the Fisher matrix is the transported simplex covariance; and outcome minimality follows from the zero-mean score relation, which forces \(\operatorname{rank}F\le m-1\) for \(m\) positive-probability outcomes.

The recent primary source was inspected at theorem/construction level for the exact normalized Fisher region and its randomized spectral realization. The broad 2026 support-size theorem, pure-state Fisher-symmetry literature, and the known arbitrary-mixed-qubit special case were separately compared. No independent audit has been performed.

Limits: the verifier does not prove the theorem by enumeration, does not test boundary states, and does not certify novelty. Those points are addressed by the analytic proof and literature comparison, respectively.
