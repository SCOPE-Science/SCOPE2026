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
# Verification record

The mathematical proof is in `RESULT.md`. The standalone `verify.py` has no non-standard dependencies and runs with `python3 verify.py`.

It constructs polynomial quotient fields, proves each quotient is a field by checking invertibility of every nonzero residue class, chooses \(\eta\in\mathbb F_{s^2}\setminus\mathbb F_s\), and counts solutions of the affine Artin--Schreier equation using the exact image of \(z\mapsto z^s+z\), adding the unique point at infinity. All 12 checked tuples of characteristic, subfield exponent, and extension degree passed: \((p,r,n)=(2,1,1),(2,1,2),(3,1,1),(3,1,2),(3,1,3),(3,1,4),(5,1,1),(5,1,2),(2,2,1),(2,2,2),(3,2,1),(3,2,2)\). In the tested cases, \(\#C(\mathbb F_{16})=1\) for \(s=4,n=1\) and \(\#C(\mathbb F_{256})=65\) for \(s=4,n=2\). For \(s=9\), the tested counts are \(1\) and \(7291\) at extension degrees one and two.

The checks independently verify only finite cases; no finite experiment is presented as exhaustive over all characteristics or extension degrees. The proof's three nontrivial ingredients are the maximal Hermitian Frobenius spectrum, vanishing of translation invariants from the quotient \(H/U\simeq\mathbb P^1\), and equal multiplicities supplied by norm-scaling automorphisms. Source-specific comparisons and the inaccessible chapter limitation are given in `REVIEW.md`.
