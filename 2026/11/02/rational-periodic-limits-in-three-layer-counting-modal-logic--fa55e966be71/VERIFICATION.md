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

# Verification and reproducibility

The exact finite probability of a uniquely largest one of \(m\) independent fair binomial counts is computed as a finite sum of integer binomial coefficients. The event \(m\#B_m-\#\top+r=0\) has a binomial mass function on the admissible residue and probability exactly zero outside it. Independent subtrees yield the amplification formula \(1-(1-e)^n\).

The local central-limit step in the mathematical proof uses an independent check of a positive asymptotic variance: \(u_m(n)\to1/m\), with fixed \(m\ge2\), hence \(u_m(n)(1-u_m(n))\to(m-1)/m^2>0\). The equality target differs from the mean by only \(O(\sqrt n)\). The tie correction comes from pairwise co-maxima; triple ties contribute only \(O(n^{-1})\). No finite computation is substituted for these asymptotic arguments.

Run the standalone test with `python3 checker.py` in a standard Python 3 installation; no extra packages or data files are required. Its direct enumerations include 5,276 base assignments, 266,508 middle-level assignments and 65,536 full depth-three assignments, plus 656 independent output-gate assignments and two numerical large-size checks. The observed output is:

```
ALL_CHECKS_OK {'plurality_assignments': 5276, 'middle_assignments': 266508, 'root_assignments': 65536, 'root_gate_assignments': 656, 'asymptotic_parameter_checks': 2}
```

This is a self-review mathematical and computational review. The independent audit channel has not been performed. Residual scientific limits: the statement is restricted to complete uniformly branching trees, independent fair labels, fixed modulus, and rational target profiles; it is not a full convergence-law classification.
