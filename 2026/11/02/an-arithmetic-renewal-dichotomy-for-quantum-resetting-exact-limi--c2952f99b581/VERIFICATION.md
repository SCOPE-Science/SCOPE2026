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

The proof in `RESULT.md` is analytical and applies to every finite-dimensional unitary and all positive-integer interarrival distributions with finite mean. Its one non-elementary named input is the standard arithmetic renewal theorem for positive integer increments of gcd one and finite mean. The zero-free multiplier argument and operator commutator step are proved directly.

The accompanying `verify_periodic_reset.py` is a standalone standard-library check. Execute `python3 verify_periodic_reset.py`. It verifies finite-horizon renewal-age distributions for multiple finite-support clocks, exact normalization, multiple rational Fourier mixtures, convergence diagnostics, and the nonconstant two-phase qubit witness. The recorded replay reports **1212 finite diagnostics passed**, including the exact example trace-distance \(\sqrt2/3\). These calculations neither enumerate all clocks nor independently prove the renewal asymptotics.

The explicit qubit clock has support \(\{2,4\}\) with equal probabilities; the off-diagonal residue-zero and residue-one limits are \(1/6\) and \(-i/6\). Their trace-norm separation is \(\sqrt2/3\). No external data, hidden setup or network dependencies are needed to run the checker. The result has received a self-review; independent audit is not yet performed.
