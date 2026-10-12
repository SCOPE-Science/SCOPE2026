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

# Exact witness and weighted-output verification

The package contains `witnesses.json` and `verify.py`, both complete standalone UTF-8 files. Run `python3 verify.py` in their shared directory. Python's standard library is the only dependency. Each witness triple lists the *one-based* coordinates of three ones, not raw bit strings.

For every witness, the checker constructs its binary word, deletes each coordinate in turn, and adds the resulting length-\(n-1\) tuple to a set. It requires pairwise disjoint sets across the whole 32-word or 37-word code. It also performs an independent deletion computation by shifting one-support indices relative to each deleted coordinate and compares both methods.

For both blocklengths it exhaustively traverses all \({n\choose3}\) possible transmitted weight-three words (364 at length 14; 455 at length 15). At each it checks the physical and index-based deletion sets coincide and that the explicit dual weight \(u_m\) has total coverage at least three. The checker sums every nonzero integer dual weight directly, obtaining 96 and 111, so the fractional objective bounds are exactly 32 and 37. The proof in `RESULT.md` explains the exhaustive coverage inequality by three cases, independently of this finite replay.

Expected concluding line: `VERIFY_OK max3(14)=32 max3(15)=37`.

No computation asserts uniqueness, exhaustive enumeration of *codebooks*, or anything about other lengths. This is reproducible finite mathematical checking, not an independent external audit.
