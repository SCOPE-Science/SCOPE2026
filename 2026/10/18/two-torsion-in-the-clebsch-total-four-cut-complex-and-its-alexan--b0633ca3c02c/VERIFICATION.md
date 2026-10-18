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

# Reproduction of the integral Clebsch cut-complex calculation

Run `python3 verify.py`. This uses only Python's standard library. Its complete captured output is in `verify_output.txt`. A successful run ends with `VERIFY_OK`.

The verifier constructs the explicit degree-five graph on \(\{0,\dots,15\}\), enumerates all independent four-sets, and builds both the total four-cut complex and the simplicial complex of subsets with independence number at most three. It checks their Alexander-dual equivalence on all \(2^{16}\) masks.

For the total four-cut complex it independently checks \(52{,}915\) augmented faces, \(26{,}434\) matched pairs, and every one of \(392{,}720\) directed face-poset incidences for acyclicity; its unmatched dimensions and integral boundary matrices are printed. For the Alexander dual the corresponding counts are \(12{,}621\) faces, \(6{,}287\) pairs and \(70{,}368\) incidences. Signed Morse coefficients are computed recursively from the actual incidence signs, not inferred from a finite-field rank.

For an independently implemented consistency check, run `python3 verify_mod2.py`. It computes the independence number of every vertex mask by memoized recurrence, reconstructs the dual without enumerating independent four-sets, and calculates the ranks of the unreduced original simplicial boundary matrices over the two-element field. The recorded output is in `verify_mod2_output.txt`, ending in `MOD2_VERIFY_OK`; the nonzero reduced Betti numbers are \(45,1,1\) in dimensions five, six and seven.

The two integral Morse differentials have nonzero entries only in the respective maps between dimensions seven and six, with absolute value two. The direct reduced chain complexes prove the stated integral homology, including torsion. Connectivity follows from the discrete-Morse CW reductions with no positive-dimensional cells below the stated thresholds.

Limits: no integral cellular attaching-map calculation beyond chain degrees is claimed, and no independent mathematical audit has been performed. No finite computation is used to infer a theorem for an infinite graph family.
