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
# Reproducible finite checks

Run the standalone standard-library Python program from the directory containing this file:

```
python3 verify_type_a_rips.py
```

It terminates with `TYPE_A_RIPS_CHECKS_OK` when all assertions pass. `verification_output.txt` records the actual run. For \(n=4,5,6\), it enumerates every face of the \(\sqrt2\)- and \(2\)-scale complexes (all subsets of the proven maximal source, target, or disjoint-source-target cliques), builds exact signed incidence only modulo two for homology ranks, and computes every mod-two boundary rank. The observed reduced first Betti ranks are \(5,11,19\), while the middle-stage reduced homology is respectively one-dimensional in degrees \(2,3,4\). It enumerates all 24 and 120 coordinate permutations for \(n=4,5\), evaluates oriented fixed-simplex Lefschetz traces, and compares the characters \(1-(f^2-3f+1)\) and \(1+(-1)^{n-2}\operatorname{sgn}(\sigma)\). Exact coordinate distances are recomputed for each parameter and found to have squared values \(2,4,6,8\). The antipodal-pair join description is checked structurally; the full high-dimensional simplicial chain complex at the penultimate scale is not enumerated.

The proof for all integers \(n\ge4\) is independent of and logically stronger than these finite computations: its essential uniform certificates are the row-column nerve, the two order maps \(\Phi,\Psi\) with \(\Phi\Psi=\mathrm{id}\le\Psi\Phi\), the explicit polyhedral homeomorphism to the standard representation sphere, and the antipodal-pair join with exterior-square orientation character. The code is a finite consistency check, not an infinite-dimensional certification. Integral torsion-freeness follows from the topological identifications, not from a finite-field rank check. There has been no independent external validation.
