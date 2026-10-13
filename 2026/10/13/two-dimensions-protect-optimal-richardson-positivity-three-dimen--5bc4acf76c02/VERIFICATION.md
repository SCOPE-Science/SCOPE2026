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

The universal two-dimensional statement is proved symbolically in `RESULT.md`: after writing the optimal Richardson matrix as \(T=[[\delta,\gamma],[\gamma,-\delta]]\), direct multiplication gives \(T^2=(\delta^2+\gamma^2)I\), and \(I+T\) is entrywise nonnegative. Pairing powers then proves every iterate is nonnegative.

`verify.py` replays the finite three-dimensional witness with exact rational arithmetic. It checks the characteristic polynomial at \(1\), \(9\), and \(11\), the optimal parameter \(1/6\), the Richardson matrix, the first three iterates for \(b=(0,1,0)^{\mathsf T}\), the negative value \(x^{(3)}_1=-1/108\), the exact solution, and the spectral-radius value \(5/6\). It also checks the coefficient identity underlying the two-dimensional square relation.

The checker is supplementary: finite execution does not establish the quantified two-dimensional theorem. No claim is made beyond the assumptions and scope stated in `RESULT.md`.
