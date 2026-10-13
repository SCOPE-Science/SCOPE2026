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

The symbolic proof reduces an exact two-cycle containing \(2^a\) to
\[
y+\varphi(y)=3\cdot2^{a-1}
\]
and then classifies all positive solutions by the odd part of \(y\) and the \(2\)-adic valuation of its totient.

`verify.py` performs a separate finite regression check. It computes \(\varphi(n)\) by a sieve and exhaustively tests all \(y\) in the possible range for \(1\le a\le18\). It then directly evaluates both arrows of every predicted two-cycle.

Recorded output:

`VERIFY_OK a_cases=18 equation_values=786429 cycle_cases=15`

The finite check does not certify the infinite theorem and is not used to replace any step of the proof. The remaining scientific limitation is literature coverage: targeted searches found no equivalent classification, but no finite search can prove global novelty.
