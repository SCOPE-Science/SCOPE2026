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

Run `python3 verify_majority.py` using Python 3. The exact-rational tests need only its standard library; SciPy, when installed, adds numerical large-size hypergeometric-tail tests.

The executed verifier passed 1,764 exact formula-versus-absorbing-chain comparisons across 36 odd graph-size pairs; 144 complete first-update ordering enumerations; and 820 finite exact symmetry checks. Optional SciPy computations additionally compared the critical-window limit against six finite-network hypergeometric tails and checked three off-critical parameter families at two sizes each.

For proof completeness, the important mathematical reductions are: (i) common partwise majorities imply deterministic absorption, (ii) initially opposing majorities remain fixed until one of two first-ring thresholds and so reduce to independent exponential first updates, (iii) the first \(r+s-1\) clock ranks yield a hypergeometric tail, and (iv) exponential order-statistic spacings and a Lyapunov central limit argument give the claimed critical normal law. Finite experiments corroborate the finite combinatorics, but are not used to establish infinite-family truth or publication priority.

Limits: the result concerns odd part sizes, equal-rate asynchronous clocks, full initial public visibility, and the specified interior scaling window. A specialist prior result could still entail the theorem; literature checks are not an independent novelty certificate.
