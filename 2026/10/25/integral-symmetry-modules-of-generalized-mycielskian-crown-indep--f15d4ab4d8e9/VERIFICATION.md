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

# Verification and limits

The file `verify_crown.py` is a standalone Python 3 checker requiring only the standard library. Running `python3 verify_crown.py` produces `PASS 180 orbit-independence/equivariant-Euler checks` and `PASS 6 mod-two homology vectors` after displaying the six computed face and homology vectors.

The first test independently enumerates orbits of each graph automorphism associated with all conjugacy-class representatives in \(S_n\), for \(3\leq n\leq5\) and \(0\leq\ell\leq5\), with and without part exchange. It rejects vertex orbits that contain an edge and computes the signed independence polynomial of the remaining orbit graph using the deletion recurrence. Each answer is checked against the reduced Lefschetz character predicted by the theorem, including the exceptional two-degree case when \(3\mid\ell\). This gives exactly 180 comparisons.

The second test generates all independent sets, builds mod-two simplicial boundary matrices, and computes reduced homology ranks for \((n,\ell)=(3,0),(3,1),(3,2),(3,3),(4,0),(4,1)\). The nonzero reduced mod-two ranks are respectively \((\beta_0,\beta_1)=(1,2)\), \(\beta_2=2\), \(\beta_3=4\), \((\beta_4,\beta_5)=(4,8)\), \((\beta_0,\beta_1)=(1,3)\), and \(\beta_2=3\).

**Scope.** Finite calculations are checks only. Integral torsion-freeness, the general module description, the all-parameter character formula and the absence of other reduced homology groups are established by the fold and equivariant long-exact-sequence proof in `RESULT.md`, not by extrapolating from experiments. The script does not calculate the full integral chain representation or independently prove the fold lemma for unbounded parameters. No independent audit has been performed.
