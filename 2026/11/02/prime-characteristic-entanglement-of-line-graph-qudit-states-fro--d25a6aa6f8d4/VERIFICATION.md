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

# Reproducibility and verification

The proof is given in `RESULT.md`; the computation is corroborative, not an infinite proof. Run `python3 check.py` from this directory. Python 3.8+ is sufficient for finite-field checks; NumPy is needed only for the optional direct density-matrix eigenspectrum comparisons. The exact recorded output of the complete test environment is in `CHECK_OUTPUT.txt`.

The checker independently forms (a) the direct cross-adjacency matrix of the line graph for each edge partition and prime, and (b) connected components with the characteristic-dependent alternating vectors and their overlap matrix. Gaussian elimination over the specified prime field is performed on both. It checks all three-way edge assignments (absent, first part, second part) through five base vertices (179,427 graph/partition/prime tests), plus 20,000 seeded random six-to-fifteen-vertex comparisons over four primes. It also checks the complete-graph Hamilton path formula for n=4,...,31 over four primes (112 comparisons); n=4 is only a numerical check and is not included in the theorem's n>=5 corollary.

For ten small graph-state cases, the checker also directly constructs the amplitudes with generalized controlled-phase phases, traces out the complementary subsystem, and computes eigenvalues using NumPy. Its largest recorded absolute difference from the stated flat spectrum was 2.22e-16. This is floating-point corroboration for those examples and does not verify all dimensions.

The nonstandard critical proof checks are the exact unsigned-incidence product for *simple* base graphs, the component-kernel classification in prime characteristic including isolated vertices and odd cycles, and the dimension formula for pairing two incidence images. The boundary cases are zero-edge parts and disconnected graphs. These steps are proved algebraically in `RESULT.md`, not inferred from finite tests. The work has not undergone independent scientific audit.
