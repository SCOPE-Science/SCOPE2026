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
# Verification of signed-star reachable-colouring theorem

The included `verify.py` requires only Python 3 standard-library modules. Run it alongside this document with `python3 verify.py`. It starts with an all-unburned signed star and independently enumerates every admissible synchronous spread-then-ignition continuation, with signs on the centre-to-leaf edges and \(\pm1\) burned colours. States are deduplicated only after explicit simulation; the proof formulas are evaluated separately.

The successful evaluation covered each of the \(2^n\) signings for every \(1\le n\le7\), totaling \(254\) signed stars. For each signing, the program compared all reachable configurations literally against the one-reversed-leaf classification, compared complete yellow-count distributions with the claimed generating polynomial, and checked the plurality number. It separately computed the Hamming covering radius of the all-positive reachable code by enumerating all target words, and compared the minimum plurality over all signings with the radius identity.

The respective covering radii for \(n=1,2,3,4,5,6,7\) were \(1,1,1,1,2,2,3\), and the minimum pluralities over all signings were \(1,2,3,4,4,5,5\). The verifier concluded `VERIFY_OK` without discrepancies.

**Limit:** The program is an exhaustive check over those finite orders, not a proof for unrestricted \(n\). The general result is established by the centre/leaf first-ignition dichotomy and the exact target-word Hamming-distance maximization in `RESULT.md`. No independent external review has been carried out.
