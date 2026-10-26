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

# Reproduction guide and limits

The standalone `verify.py` requires Python 3.8 or later and only its standard library. From a directory containing the script, run `python3 verify.py` and require the final `VERIFY_OK` report. The program constructs all seven Fano lines as the nonzero triples in \(\mathbb F_2^3\) summing to zero. It builds and checks all fourteen incidence-graph neighbor sets.

It separately tests every initial vertex set of size at most five, all 3,003 six-subsets, and all 784 pairs of noncollinear point triples and nonconcurrent line triples; the two characterizations agree as complete sets. An independent sequential application of the zero-forcing rule agrees with the simultaneous bit-mask implementation for every six-subset. The program also constructs 168 linear collineations and the other 168 automorphisms from a Fano point–line polarity and checks each against all graph neighborhoods. It compares the successful and rejected orbit classifications and the complete induced-shape and propagation tables. Finally it enumerates every one-site exchange of the 700 optimum sets and computes shortest-path distances from every set, including the entire 244,650-pair distribution.

These are complete computations over explicit finite domains, not statistical sampling. The correctness argument uses the monotonicity and termination of the legal forcing rule, the Fano incidence definition, group invariance of the relevant parameters, and exhaustive bounded loops. The included checker is not an external or independent certification; no independent audit has been performed. The result does not establish an analogous formula for projective planes of arbitrary order or any claim concerning positive-semidefinite zero forcing.
