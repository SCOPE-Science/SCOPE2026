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

The algebraic proof is self-contained in `RESULT.md`. It establishes the affine reciprocal transformation, the attracting positive four-cycle, the four-coordinate strict majorization for every real \(r>1\) and \(0<L<H\), and the resulting population mean/extremum comparisons. The symbolic partial-sum gaps explicitly exhibit the strict sign conditions.

The complete standalone `verify.py` uses Python standard-library exact fractions. Executing `python verify.py` produces `41615 exact-rational assertions passed across 640 parameter triples.` This checks the recurrence, cycles, six schedule permutations, majorization, extremal and mean comparisons, higher convex powers and the exact rational illustrative example. Testing a finite rational grid is not a proof for all real-valued parameters and is not described as one.

Independently checkable sample: growth factor \(r=2\); capacities \(L=1/3\) and \(H=1\). The grouped orbit multiset is \(\{5/7,5/9,5/11,5/13\}\), the alternating one \(\{3/5,3/5,3/7,3/7\}\). The strict arithmetic-mean gap is exactly \(584/45045\), and the grouped minimum is \(5/13<3/7\).

The literature comparison addresses the *statement* of strict inverse-biomass convex order and simultaneous mean/trough conflict, not the already established recurrence or periodic solution. General historical novelty and external replication have not been independently validated. Full texts of two plausible later works were unavailable, so the priority evidence is bounded accordingly.
