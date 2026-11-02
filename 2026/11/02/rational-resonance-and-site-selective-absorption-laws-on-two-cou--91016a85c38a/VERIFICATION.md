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

# Verification of the rational-resonance capture theorem

The proof is independent of the finite checks. Its decisive analytic points are (i) Walsh diagonalization of the two-rate coordinate-flip Hamiltonian, (ii) exact dissipative projector characterization of eventual absorption, (iii) counting edges in primitive-step lines across the spectral rectangle, (iv) Krawtchouk character sums for sitewise projections, and (v) sign rigidity for full-capture corners. Every parameter in the claimed theorem is quantified and includes both minimum block sizes and all positive coupling and sink rates.

Run the accompanying scientific checkers as follows:

```
python3 check_resonances.py
python3 check_evolution.py
```

`check_resonances.py` evaluates \(a,b\in\{1,2,3,4\}\), nine specified coupling choices (including a generic no-collision case), and every starting vertex. The rational formula is checked against a separately assembled full Walsh projector. It also tests the predicted bright dimension and number of full-capture sites. `check_evolution.py` independently propagates the non-Hermitian Hamiltonian on finite examples and compares long-time capture with the spectral prediction. Numerical tolerances and all tested cases are explicit in their source code. The actual output of both packaged scripts is included in `CHECKS.txt`.

The finite-time evolution tests do not establish exact asymptotic convergence numerically: the proof uses finite-dimensional dissipativity. No claim is made about any independent audit or validation beyond these tests and self-review. An inaccessible specialized historical theorem could affect priority, not the finite computations reported here.
