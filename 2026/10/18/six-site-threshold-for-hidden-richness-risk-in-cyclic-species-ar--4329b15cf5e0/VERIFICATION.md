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

# Reproduction and boundaries

Run `python verify.py` from the directory containing `verify.py` and `certificate.json`. Its sole output is a stable, single-line JSON object; it must match the UTF-8 contents of `certificate.json` after removing the final line feed. Both files are standalone and require no network connection or third-party packages.

The code enumerates all restricted-growth words of lengths one through five (a bijective encoding of set partitions of labeled sites), computes the complete distribution of richness over uniformly shifted cyclic windows for every length, and confirms that no mean curve appears with two distinct distribution signatures. The enumerated totals are exactly the first five Bell numbers, \(1,2,5,15,52\). There is also a direct mathematical small-site proof in `RESULT.md`.

At six sites it checks that the circular labels `BACAAA` and `BAACAA` have exactly matching species-specific detection probabilities for all depths, but length-three richness histograms \((1,4,1)\) and \((0,6,0)\) over richness values \(1,2,3\), respectively, yielding variance difference \(1/3\).

For \(6\le N\le40\), all separations \(2\le s\le N-2\) and sample lengths \(2\le m\le N\), it confirms via direct window enumeration the exact three-point probability formula and variance formula, each across \(18{,}970\) cases. It also verifies the half-window extremal range for \(6\le N\le60\). No floating-point decisions are used.

These checks are corroborations. The proof for every \(N\) is the two-site window-intersection identity and its half-window bound; the finite table cannot alone establish an infinite statement. Neither source inspection nor the included checker constitutes independent scientific certification. Inaccessible or as-yet-unrecognized mathematical prior work remains possible.
