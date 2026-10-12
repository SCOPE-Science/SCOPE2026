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
# Reproduction and proof boundaries

Run `python verify.py` with Python 3 and SymPy installed. This constructs adjacency matrices for \(P_3\) and \(P_4\), reconstructs all seven spectral idempotents from their eigenvalues, verifies idempotence, orthogonality and completeness, and checks exact rational-surd identities giving expected mixing \(J_3/3\), \(J_4/4\), and all 144 entries of \(J_{12}/12\). It also checks that the relevant numbers of distinct positive gaps are two and four, providing a direct basis for the fifteen-dimensional coefficient-space support bound.

Expected exact output:

`VERIFY_OK idempotents=7 exact_factor_rows=7 exact_product_entries=144 nonzero_gap_counts=2,4 caratheodory_support_bound=15`

Optionally run `python verify.py --numerical` if NumPy and SciPy are installed. This also checks the Cartesian mixing identity against five full twelve-dimensional matrix exponentials and solves a finite linear program over 300 sampled observation times using a fixed random seed; in one execution it returned a fifteen-positive-weight approximate solution with matrix residual \(2.77\times10^{-11}\). This numerical witness **does not prove** that exact times or weights have been found.

The exact finite physical-time assertion is established by the rational independence and Kronecker density arguments together with the relative-interior lemma, followed by Carathéodory. Neither finite random sampling nor projector identities alone establish that topological step. This proof gives no bound on the magnitudes of realizing times and no constructive exact arithmetic representation for their weights.
