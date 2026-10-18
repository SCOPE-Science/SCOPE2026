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

# Verification notes

The exact recurrence for full blocks is \(F_k(r)=F_{k-1}(r)-F_{k-1}(r-(-1)^{k-1})\) on the cyclic residues. For even blocks it reduces to a nonnegative tridiagonal recurrence after conjugation by residue-distance signs. The proof explicitly treats the exceptional pair \(h,-h\) and proves all-prefix interval containment, which is needed to infer an infinite all-prefix assertion.

Execute `python check_newman.py` with Python 3.8 or later. It independently builds binary alternating-digit sums and signed prefix counts for all odd moduli \(3\) through \(31\), all prefixes below \(2^{12}\), and verifies complete-block vectors through length \(119\) for selected moduli. The documented exact run passed all assertions. These finite computations do not replace the general symbolic proof.

Remaining scientific limits: no quantitative lower bound, no zero classification for nonzero residues, and no treatment of even moduli. The originality comparison is best knowledge, not an exhaustive all-literature certificate. Independent audit has not been performed.
