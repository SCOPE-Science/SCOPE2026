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

# Reproducibility and mathematical limits

Execute `python3 verify.py` in a directory containing the extracted source. This uses the Python standard library only.

The program generates all integer-valued root-normalized potentials with the first upper-layer height fixed at zero and edge increments bounded by one, filters each candidate by all clique/matching inequalities, and tests spanning connectivity of tight edges by exact union-find operations. It compares the output with the claimed closed facet formula for \(n=2,3,4,5,6\) (with \(n=2\) only a boundary consistency check outside the theorem statement).

It separately computes the action of every simultaneous column permutation, optional layer interchange, and optional global negation for \(n=3,4,5\). It checks all images are facet potentials, decomposes the entire enumerated set into disjoint exact orbits, checks the orbit counts and gives the orbit-size multisets. The program terminates with `ALL EXACT CHECKS PASSED` when all assertions hold.

This is not exhaustive verification of all infinitely many dimensions, nor a computer-assisted proof of the analytic orbit-sum identities; those are justified in RESULT.md. The reference inspection and originality assessment are not an independent bibliographic certification.
