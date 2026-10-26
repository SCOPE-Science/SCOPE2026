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
# Reproducibility

Execute `python verify.py` with Python's standard library. The script builds the ten-vertex witness by the exact edge list described in the proof and computes the combinatorial Laplacian, its fourth matrix power, and exact rational inverses of the two implicit-step matrices.

It checks diameter exactly three, \((L^4)_{uv}=4\), the two short analytic bounding tables, and strict negativity of the chosen completed transition entry at \(h=1/75,1/100,1/200,1/1000\). It also checks the exact midpoint-count identity on 2,499 deterministic random distance-three pairs, along with the appropriate order bounds for graphs with at most ten vertices. See `verify_output.txt` for the reproduced output.

The proof's universal claim is analytic: the graph identity, monotonic one-bridge reduction, and complete integer maximization replace any supposed enumeration of all graphs. Numerical or finite random checks cannot establish an infinite universal theorem or novelty.
