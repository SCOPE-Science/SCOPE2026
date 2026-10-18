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

# Reproducibility

Run `python3 checker.py` using Python 3.10 or newer; no additional packages are needed. The program uses direct q-ary enumeration, computes the parity of every word, constructs the actual adjacent-swap graph separately for each content vector, and finds a maximum matching by Kuhn augmenting paths. It checks that graph independence number (vertex count minus maximum matching size) equals the claimed constant-composition formula, and checks global summation independently.

The tested ranges are every \(n=1,\ldots,9\) for \(q=2\); every \(n=1,\ldots,7\) for \(q=3\); and every \(n=1,\ldots,5\) for \(q=4\). The successful expected terminator is `ALL_ADJACENT_SWAP_CAPACITY_CHECKS_PASSED`. The infinite range is justified by the mathematical involution proof, not finite computation. The program deliberately does not attempt error correction, nonadjacent swaps or simultaneous multiple swaps.
