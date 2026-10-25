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

# Reproducibility and limits

The finite input is the complex of pairwise-intersecting families of triples on six points with transversal number at most two. The source `verify_morse.py` uses only Python 3 standard-library features and makes no network requests. Run it in the same directory as this document with `python3 verify_morse.py`. Its exact output is captured in `verify_morse_output.txt`.

The script verifies 54,870 nonempty faces, 27,398 matched pairs, all 358,760 directed face-cover relations, and the acyclicity of the complete directed Hasse graph. It constructs integer critical-cell boundary matrices, checks the chain condition, and reduces the matrices by explicitly implemented determinant-one-or-negative-one row and column operations. It confirms 13 unit Smith invariants in dimension six, six in dimension seven, and a zero boundary from dimension eight.

A second separately implemented script, `independent_mod2.py`, enumerates faces by a recursive clique generator and calculates ranks of every mod-two boundary matrix directly, without reference to the Morse matching. Run it with `python3 independent_mod2.py`; compare with `independent_mod2_output.txt`. Its mod-two homology is in degrees five and eight with ranks 29 and six. This is a cross-check of the input complex and integer reduction, not a substitute for the integer Smith calculation.

The infinite parts of the argument consist solely of standard topological steps: the star cluster is contractible, the published concentration map retracts the larger complex, the nullhomotopic inclusion gives the wedge with a suspension, and integral acyclic Morse matching preserves chain homology. The finite computations are exhaustive for the auxiliary six-point complex and do not assert a homotopy type or torsion statement at higher parameters. No independent audit has been performed.
