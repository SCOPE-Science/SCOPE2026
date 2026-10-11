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

Run `python3 verify.py` with Python 3 (standard library only). The script recomputes the rational candidate minima from the rank description and checks the center-of-contact-orbits inequality, ties and exact radius values for \(3{,}600\) pairs \(1\le m,n\le60\). For \(m\le5,n\le6\), it explicitly generates all rank-orbit vertices (\(1{,}352\) total instances across pairs) and independently evaluates their rational squared distances, including equality versus strict inequality for each contact orbit. It tests the sharp full-rank-only phase and sample cubical asymptotics.

The independently reproducible certificate for the general theorem is the exact proof in `RESULT.md`: the adjacent rank-quadratic differences, interval minimization and contact-barycenter squared-distance identity. Finite checks do not prove assertions for every parameter pair. This is not independent mathematical auditing or priority certification.
