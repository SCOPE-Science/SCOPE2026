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

# Reproducibility and verification

Run `python3 checker.py` to compare three independently derived finite procedures: direct enumeration of length-\(n\) factors and their actual tortoise images, union-counting of triple-window starts and two-one-image positions, and evaluation of the claimed closed formula. The recorded output is `computation.txt`.

The completed checks cover \(1400\) direct finite-factor cells for \(2\le b\le8\), \(1\le n\le200\), and \(22648\) independent interval cells including the boundary positions of geometric scales for \(2\le b\le12\). They agreed in every tested cell. The direct method uses a long finite prefix; no assertion of exhaustive coverage over all infinite factors follows from that alone.

The all-length proof instead relies on injectivity of images with at least three ones, exact interval formulas for images with exactly two ones, disjointness of the active intervals, and elementary geometric inequalities for \(b\ge2\). No external proof assistant or independent audit was employed. Results for arbitrary increasing-gap words and higher tortoise iterates remain unproved.
