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
The proof is analytic. The checker performs only finite consistency checks and numerical evaluation; those computations are not substitutes for the Gaussian rotational-symmetry argument or the permutation-counting proof.

`verify.py` performs four checks:

1. For \(n=6\), it exhaustively enumerates all \(6!\) permutations of the balanced residual direction and verifies the exact three-point multiplicities.
2. For a small finite-\(m\) case, it exhaustively enumerates every sequence of three-point randomized outcomes and confirms the binomial-tail formula.
3. It directly evaluates the reported \(n=20\), \(m=1000\), \(\alpha=0.05\) null size.
4. It checks numerically that the complete-randomization limit approaches \(1/2\) with increasing \(n\).

The checker does not establish literature originality, does not test alternative residual constructions, and does not certify a worst-case statement over all designs.

Run `python3 verify.py`. The expected first line is `VERIFY_OK`.
