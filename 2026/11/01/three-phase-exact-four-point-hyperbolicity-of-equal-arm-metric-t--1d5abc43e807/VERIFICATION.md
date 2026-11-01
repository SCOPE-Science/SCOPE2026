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

# Exact rational verification

Execute `python theta_verify.py` next to `theta_dual_certificates.json.gz` using Python 3. No solver, network connection, NumPy, or third-party packages are required to verify the proof certificate.

The checker reconstructs each of the nine unordered arm-assignment types, three closed real length-parameter intervals, three possible leading pair sums, and all affine alternatives for the two competitors. For each of the 2,685 linear programs, it regenerates the complete matrix of rational coordinate, order, length, distance, and epigraph inequalities. It then checks each compressed dual vector has nonnegative rational entries, sums exactly to the objective vector for the variable \(w\), and has a nonpositive total bound. The proof converts these finitely many verified rational identities into a universal statement over all real quadruple coordinates and all real \(0<t\le1\); no finite sample is interpreted as an infinite proof.

Observed checker output:

```
PASS: 2685 exact rational LP dual certificates; complete continuous parameter domain
No floating-point tolerance used in the certificate check.
```

Lower-bound witnesses are explicit in `RESULT.md` and can be checked directly from the two-pole shortest-path formulas. This verification is a self-review consistency review, not an external mathematical audit. Historical-priority uncertainty is discussed in `REVIEW.md` and `AUDIT.json`.
