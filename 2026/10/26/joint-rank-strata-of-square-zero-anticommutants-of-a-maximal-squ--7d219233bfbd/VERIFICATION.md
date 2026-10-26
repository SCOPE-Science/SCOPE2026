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

# Reproduction and checks

Run `python3 verify.py` with an ordinary Python 3 installation; no third-party packages or network access are required. The program independently forms the prescribed square-zero matrix and the candidate anticommutants, verifies the matrix identities directly, calculates both ranks by field row reduction, and checks every stratum count against Gaussian-binomial formulas.

**Completed checks:** for \((r,q)=(1,2),(1,3),(2,2),(2,3),(2,5),(3,2)\), exact totals respectively \(2,3,28,153,1225,1184\), with full stratum equality in each case. Separately, all \(2^{16}=65536\) matrices of size \(4\times4\) over \(\mathbb F_2\) were tested without the block parametrization; exactly \(28\) satisfied both relations, with the expected ranks. The script prints `VERIFY_OK_MAX_RANK_EXTERIOR_PAIR_JOINT_RANK` only after all assertions succeed.

**Mathematical dependencies:** count square-zero matrices of fixed rank via image/kernel flags and quotient isomorphisms; compute the centralizer dimension from length-one and length-two \(\mathbb F_q[z]\)-modules; show its induced action on \(\ker P/\operatorname{im}P\) is onto with constant fibers; and establish the product-rank identity by projection onto the second block. These prove the unrestricted theorem. Finite experiments do not establish it beyond tested parameters. The implementation's modular arithmetic is for **prime** field orders; the proof covers arbitrary prime powers.

**Limits:** The thesis listed as a historical-priority risk was not accessible in full text. Geometric dimensions rely on the standard smooth rank-stratum and nilpotent-orbit constructions; the executable checks validate finite cardinalities, not scheme-theoretic assertions. No independent mathematical audit has been performed.
