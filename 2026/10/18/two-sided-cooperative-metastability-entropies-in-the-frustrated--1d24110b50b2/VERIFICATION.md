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

# Verification
Execute `python verify.py` in the directory containing this document. The script is pure Python 3 and uses only standard-library modules. It compares the exact rational Hamiltonian on labeled periodic rings with every possible single-spin and unordered two-spin simultaneous flip at lengths \(N=8,9,10,11,12,13,14\) for the coupling ratios \(\kappa=1/4,1/2,3/4\). It also checks the four rational values \(1/100,49/100,51/100,99/100\) for lengths eight through eleven, and independently enumerates the weighted cyclic domain compositions. The expected two-spin counts at lengths \(8,10,12,14\) are \((26,52,92,198)\), \((46,122,324,842)\), and \((28,60,190,406)\) in increasing frustration regime order.

The script checks that the characteristic root polynomials vanish numerically at roots obtained by bisection; it is not an infinite proof of singularity dominance. The complete infinite-family proof, including all separation cases for two-spin moves and positivity/aperiodicity of the generating functions, is given symbolically in RESULT.md. No independent audit or experimental validation is asserted.
