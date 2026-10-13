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

# Verification details

Run the included standalone Python 3 script with `python3 artifacts/verify.py` from the package root. The script has no nonstandard dependencies. It computes exact covariance using the avoid-one-part-size recurrence, compares this with direct enumeration of all separator strings for integers \(1\le n\le12\), checks finite signs over \(6\le n\le64\), and checks the explicitly stated asymptotic profile numerically for \(n=50,100,200,500\). The tolerance bounds are stated in the code and the computed errors are printed.

The proof's critical nonstandard ingredient is Theorem 1 of Arratia, Goldstein and Gordon (1989), whose Poisson void inequality was read from the publicly accessible complete paper and used with \(b_3=0\). The separator-pattern intersections, size-window error sums, finite identities and lattice Fourier integral were independently reconstructed in the mathematical argument. A finite computation cannot verify the infinite limit or nonconstancy by itself, nor does any such computation certify priority in the literature.

The displayed asymptotic is an analytic claim for all positive integers. No external independent audit or validation is represented.
