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

# Verification of the duration comparison

The exact proof identifies first-infection generations with directed live-edge distances, bounds the vaccinated maximum by \(n-2\), and establishes that a positive delay forces the original last-infection generation to be at least two. An explicit directed graph family attains the resulting \(n-4\) upper bound for every \(n\ge5\).

The attached `verify.py` is a standalone Python standard-library program. It reconstructs the expected-duration difference by summing over the complete set of 64 live-edge configurations of the five-person graph, rather than taking the displayed expectation formulas as input. It checks the resulting exact polynomial coefficient vector \((0,-1,-1,0,3,1,-1)\), corresponding to powers zero through six of \(p\). It independently exhausts all directed graphs with at most four vertices, demonstrates the sharp construction for \(5\le n\le60\), tests 999 rational probability values, and brackets the critical root between the rational numbers \(83659/100000\) and \(83660/100000\).

Command: `python verify.py`. Expected output begins `PASS:`.

**Limits of verification:** Finite exhaustive checks cover only graphs through four vertices; the all-size theorem is justified by the analytical upper bound and explicit constructions. The root uniqueness follows from exact strict concavity, not a numerical solver. Neither the code nor the proof establishes a network-independent stochastic threshold for arbitrary five-person graphs. Independent audit has not been performed.
