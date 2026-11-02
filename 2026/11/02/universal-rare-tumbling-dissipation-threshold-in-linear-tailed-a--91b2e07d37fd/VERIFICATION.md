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

# Reproducibility and verification

The complete analytical proof is in `RESULT.md`; finite numerical checks independently stress-test its definitions and constants. With NumPy and SciPy installed, run:

```
python verification.py
```

The script executed successfully and reported **PASS: 99 deterministic checks**. It computes the two negative roots of the known one-cusp stationary cubic, recovers their density weights by symmetry and normalization, and checks the entropy identity \(\mathcal E=(v^2-b^2)/T+2bP(0)\). For \((b,T)=(1,0.7)\), the small-flip checks at \(r=0.00032\) include \(v=0.45\), \(v=0.8\), \(v=1\), \(v=1.3\), \(v=1.5\), and \(v=2.2\), covering both sides of and exactly the threshold. The code also constructs an independent finite-volume generator with thermal diffusion, orientation flips and spatial upwinding for single-cusp, bistable and asymmetric compact-interior force examples, and checks that their finite-rate results remain consistent with the theory.

The finite-volume systems have reflecting outer boundaries and finite spatial resolution; they do **not** establish any \(r\downarrow0\) limit. The infinite-domain, continuous-state and singular-limit conclusions follow from the proof's Foster–Lyapunov, frozen-invariant-measure and compact-escape arguments. These checks are not independent scientific review or external certification.
