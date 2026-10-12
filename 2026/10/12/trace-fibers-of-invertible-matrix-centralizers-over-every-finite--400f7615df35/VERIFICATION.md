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

# Verification of invertible-centralizer trace fibers

The included `verify.py` is a dependency-free direct census. It constructs a basis of \(\ker(X\mapsto AX-XA)\) using finite-field Gaussian elimination, independently loops over **all** centralizing matrices for the listed inputs, tests their invertibility, and counts each ordinary trace. In parallel, it evaluates the closed formula using the known elementary divisor multiplicities. Every comparison is exact integer arithmetic over \(\mathbb F_q\). The script terminates with `VERIFY_OK` only if all comparisons pass.

The checker was run for **45 selected similarity-type representatives** over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). It covers scalar representatives, single and multiple Jordan blocks (some block lengths divisible by the characteristic), multiple distinct eigenvalues, irreducible quadratic and cubic companion matrices, squared irreducible quadratic companions and mixed degree factors. For example, for the single length-two nilpotent block over \(\mathbb F_2\), the trace count is \((2,0)\); for the length-three nilpotent block over \(\mathbb F_3\), it is \((18,0,0)\); and for the single irreducible quadratic companion matrix over \(\mathbb F_4\), it is \((3,4,4,4)\).

Execute `python3 verify.py`. This tests finitely many representative cases, **not** every similarity class, arbitrary field size or dimension. The general infinite family is proved by the full algebraic argument in `RESULT.md`: quotient of the commuting endomorphism algebra, trace filtration, matrix Gauss sum, and additive Fourier inversion. No independent external audit has been performed.
