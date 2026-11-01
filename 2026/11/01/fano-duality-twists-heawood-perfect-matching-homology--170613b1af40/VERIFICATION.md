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
# Verification of the rational Heawood duality character

Execute `python3 verify_heawood_perfect_duality.py` in the same directory using Python 3 standard library. The checked output is included as `verify_heawood_perfect_duality.output.txt`. The program verifies all \(24\) perfect matchings, all \(2201\) nonempty perfect-complex faces, all \(3461\) nonempty ordinary-matching faces, the \(1092\) discrete-Morse pairs and complete \(8736\)-incidence acyclicity, the six exact mod-two boundary ranks, all \(336\) graph automorphisms, and two independent signed character computations for each. The key assertion tested for each element is \(\chi_{\mathrm p}(g)=\varepsilon(g)\chi_{\mathrm ordinary}(g)\).

Exact character averaging produces zero fixed vectors under the full group and one fixed vector under its point–line-preserving subgroup. Forman's discrete-Morse theorem, chain-rank inequalities, rational character semisimplicity and finite-group rational transfer are explicit proof steps, not executable substitutions. The conclusion is neither an integral representation isomorphism nor a claim of quotient contractibility. The independent audit remains unperformed.
