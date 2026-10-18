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

Execute `python3 verify_cusp_code.py` using only the standard library. The script validates 128 possible shared-coordinate sign patterns, selects precisely 42 compatible with the proved allowed-weight condition, and checks the four projective support sets and exact enumerator \(1+6z^{12}+2z^{15}\). Its assertion message is `CUSPIDAL_17_CODE_AND_TOPOLOGY_COMBINATORICS_OK`.

Analytical checks: for a length-17 ternary code of minimum weight 12, the first three Griesmer summands are \(12+4+2=18\), giving the dimension bound. Euler computation: resolution 55, singular base 21, complement 4, degree-nine complement cover 36 and three points above each of 17 cusps contribute 51; hence \(e(Y)=87\). The canonical square is nine times the quintic canonical square 5, thus 45, and Noether gives \(\chi(\mathcal O_Y)=11\). The regularity of all four intermediate cyclic triple covers follows from Tan's Theorem 4.3.1, giving \(q(Y)=0\) by character decomposition and \(p_g(Y)=10\).

Proof obligations not automated: simple-connectedness of the resolved quintic, local identification of \(A_2\) discriminant linking and cusp code, normalizing the universal local cyclic cover to a smooth point, Tan's irregularity theorem and the existence of the particular 17-cusp family. These are supplied by cited mathematical sources and arguments in RESULT.md, not inferred from script output. No independent audit has been performed.
