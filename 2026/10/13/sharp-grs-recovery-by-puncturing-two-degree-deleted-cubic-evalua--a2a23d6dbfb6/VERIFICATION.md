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

# Verification scope

The proof is the five-step all-field polynomial and conic argument in RESULT.md; the bundled `verify.py` is an exact **finite** regression check rather than a substitute for that proof. It uses only Python 3 standard-library integer arithmetic and Gaussian elimination modulo small primes, with no floating-point tolerances or external data.

The script independently reconstructs both generator-column families and verifies every triple-column determinant in all tested MDS sets. For each surviving set of at least five coordinates it evaluates all six quadratic monomials on the generator columns and computes their rank. Rank below six is the conic criterion. It separately computes \(e_1\) or \(e_5\) and asserts agreement with the theorem. It checks the incidence restriction that no two eligible six-sets share five evaluation points.

Four seven-point examples exercise both outcomes for each family: \(r=1\), \(S=\{0,1,2,3,4,5,6\}\) over \(\mathbb F_{19}\) and \(\mathbb F_{23}\), with respectively one and zero GRS six-subsets; and \(r=2\), \(S=\{1,4,5,10,13,16,18\}\) over \(\mathbb F_{19}\) and \(S=\{0,1,2,3,4,7,11\}\) over \(\mathbb F_{17}\), likewise one and zero. For the first example the script checks the explicit conic \(XY+14XZ+18Y^2+4YZ+Z^2=0\) at all six relevant columns and checks they form an arc.

The exhaustive small-field study over \(\mathbb F_{11}\) and \(\mathbb F_{13}\) inspects all evaluation subsets of sizes five, six and seven, discarding precisely those failing the MDS triple test. The counts (GRS subsets, all MDS subsets), ordered by length five, six, seven, are: \(q=11,r=1\): \((112,112),(7,7),(0,0)\); \(q=11,r=2\): \((212,212),(5,77),(0,5)\); \(q=13,r=1\): \((432,432),(36,108),(0,0)\); \(q=13,r=2\): \((639,639),(24,360),(0,72)\). This exhaustiveness applies only to those finite prime fields, not to all finite fields.

To reproduce from the complete package, extract `verify.py` and run `python3 verify.py` (no arguments). The expected terminal success marker is `VERIFY_OK`. No independent audit is asserted.
