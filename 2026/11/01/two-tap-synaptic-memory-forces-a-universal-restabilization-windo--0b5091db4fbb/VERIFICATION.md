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

# Verification notes

The standalone standard-library Python script `check_stability.py` was run successfully. It recomputed all three critical-delay residuals and derivative signs for each of five \((a,b)\) pairs, checked the order of the first three crossings against other candidate families, and verified 80 further candidate imaginary-axis characteristic identities, as well as a concrete macroscopic equilibrium example. Its output was:

```
PASS: five parameter pairs, first three crossings/order/direction, sample physical theta-neuron case, and complete candidate families
a=4, b=2; critical two-tap delays: 0.9366419641387634 1.5707963267948966 1.8732839282775269
first Dirac critical mean delay: 1.282549830161864
```

Independent numerical root searches at shorter-tap delays \(0.5,1.2,1.7,2.0\) for \((a,b)=(4,2)\) found positive-real-part characteristic roots at \(1.2\) and \(2.0\) but none at \(0.5\) or \(1.7\). These grid-started root searches are illustrative, not exhaustive. The universal result follows from the analytic proof's complete imaginary-axis classification, transversality, and argument-principle root count. No nonlinear Hopf coefficient or full delay-axis stability diagram was computed.

The 2026 preprint was inspected in accessible full text (relevant main sections and appendix). The 2024 directly relevant two-commensurate-delay article was available only as an abstract/first-page preview, leaving an explicit literature-priority uncertainty. This limitation is not evidence of noncoverage.
