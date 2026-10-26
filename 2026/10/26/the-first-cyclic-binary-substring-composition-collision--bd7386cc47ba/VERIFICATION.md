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

# Reproduction of the cyclic window-spectrum classification

From the directory containing the two accompanying files run:

```sh
python3 verify.py
```

The script uses only the Python standard library and performs an exhaustive search through all \(2^n\) binary words at each of the twelve lengths \(1\le n\le12\). It independently computes cyclic spectra through direct modular-bit summation and through rolling sums of strings; it also constructs minimal representatives using two distinct approaches. All results are checked by exact integer tuple equality rather than probabilistic fingerprints. It verifies the \(224\)-versus-\(223\) count, unique class of size two, no collisions at shorter lengths, the \(23\) homometric pairs, and the complete contents of `homometric_pairs_n12.csv`. For each canonical bracelet it also checks the finite-difference moment identity linking window histograms to autocorrelation. The terminal success marker is `VERIFY_OK`.

The CSV has three columns: the two lexicographically least dihedral representatives of each distinct homometric pair of length twelve, and the first window length distinguishing that pair; `0` denotes the one pair not distinguished by any window length. Histograms for window lengths exceeding half the blocklength are recovered exactly by complementing each window inside the circle, not omitted as an approximation.

The script tests powers of the witness words only through exponent five; the argument for every positive power is the symbolic window-periodicity proof in `RESULT.md`. The exhaustive finite classification is an algorithmic proof conditional on the provided code being executed correctly on an ordinary Python interpreter. The code does not certify any statement concerning arbitrary non-multiple lengths above twelve. Independent scientific validation was not performed.
