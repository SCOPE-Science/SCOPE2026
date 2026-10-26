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

# Verification and limits

Run `python verification/check.py` with Python 3 and NumPy. The script evaluates explicit \(2\times2\) antiunitaries \((\alpha I+\sqrt{1-\alpha^2}J)C\) for five overlap levels and six \(q\)-moduli; it samples 10,000 unit vectors at each of 30 parameter pairs, checks the phase-extremal lower/upper envelopes against the claimed radii, and confirms that observed extrema approach those exact endpoints. Three exact rational identities exercise the \(3\)-\(4\)-\(5\) threshold examples. The script reports its total number of assertions.

The proof in `RESULT.md` establishes all dimensions and all real parameter values. Finite sampling is neither exhaustive over the complex sphere nor a proof about infinite Hilbert spaces. The infinite-dimensional open disk is established by the explicit direct-sum construction and a strict weighted-average argument; no finite machine computation can verify nonattainment. Endpoint comparisons and strict inequalities are proved symbolically, rather than inferred from tolerances.

Scientific publication-priority uncertainty remains, particularly for inaccessible or unindexed literature. No independent scientific audit or external validation is claimed.
