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

The included `verify_tonn_10_4_1234.py` is a standalone standard-library replay. It reconstructs \(\mathrm{Tonn}^{10,4}(1,2,3,4)\) directly from the published facet formula, deduplicates the maximal-simplex candidates, enumerates every nonempty face, builds every Hasse cover, constructs the stated element matching, and verifies acyclicity by a complete topological-sort test.

The replay checks the exact face vector \((10,45,100,60)\), \(215\) nonempty faces, \(630\) Hasse covers, \(103\) Morse pairs, and the complete critical-cell set. It then constructs all simplicial boundary matrices with integer incidence signs and computes their ranks over \(\mathbb Q\) by exact `Fraction` elimination, obtaining \((9,36,58)\) and Betti vector \((1,0,6,2)\). A successful execution terminates with `VERIFY_OK`.

The script establishes a finite certificate for this one complex. It does not prove a classification of all nongeneric generalized Tonnetze. The final wedge decomposition additionally uses standard discrete Morse theory and the Hurewicz isomorphism \(\pi_2\cong H_2\) for the simply connected \(2\)-skeleton \(\bigvee^6S^2\).
