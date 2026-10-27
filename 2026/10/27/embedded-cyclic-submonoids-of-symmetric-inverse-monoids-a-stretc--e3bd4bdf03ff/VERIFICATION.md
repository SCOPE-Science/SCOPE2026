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

# Verification instructions and limits

Execute the included standalone `CHECKER.py` using a standard Python 3 interpreter. It constructs all partial injections, composes their powers inside the ambient monoid, enumerates distinct cyclic submonoid subsets through rank five, and independently computes the rational totient-weighted formula through rank six. Expected terminal marker: `ALL_PARTIAL_CYCLIC_FINITE_CHECKS_PASSED`.

Re-derive the all-size argument from the generator-multiplicity lemma, the directed path/cycle decomposition, and the uniform random-permutation largest-cycle bound. In particular, a map with a nontrivial directed path has a unique generator of its embedded cyclic submonoid, while locally permutational maps of period \(p\) have \(\varphi(p)\) generators. For the asymptotic constant, check the Laguerre–Bessel coefficient comparison and the saddle-point integral in the proof. The script is finite verification only; it does not check the limiting distributions or prove novelty.

Related comparison documents: Lipscomb, DOI `10.1007/BF02573166` (only abstract accessible); Elliott–Levine–Mitchell, arXiv:`2303.12387`, full HTML text. Prior independent mathematical audit: not performed.
