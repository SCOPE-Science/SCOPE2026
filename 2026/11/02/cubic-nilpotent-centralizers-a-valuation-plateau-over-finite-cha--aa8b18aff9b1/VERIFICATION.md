---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Cayley-Hamilton for a primitive matrix U over R_m yields U^3=(tau^2-delta)U-tau delta I; unit minor of (I,U) makes this equivalent to delta=tau^2 and tau^3=0. Exactly q^2-1 nonzero nilpotent residue matrices; q^{m-ceil(m/3)} traces and q^{2(m-1)} fixed-trace/determinant lifts yield P_m=(q^2-1)q^{3m-2-ceil(m/3)}. At entry valuation v<c, lifting each of four coordinates by 2v levels gives q^{8v}P_{s-3v}, independent of v. At >=c cubes vanish automatically. Verified separately for small Z/p^s rings with direct matrix multiplication; extension fields and all s established by proof, not finite experiment. For s=1 cubic equals square nilpotence and c=1; zero/deep block handled.

## originality

PASS

Qualified PASS for the simultaneous all-length finite-chain-ring count and flat exact entry-valuation strata; general Drazin-index enumeration could cover total nilpotency-index count, but the inspected sources do not establish or imply the complete plateau. Explicit priority risk remains because Brawley 1982 primary full text was not accessible.

## value

PASS

Counts a natural bounded-index nilpotent locus within centralizers of two equal Jordan blocks, with structural arithmetic invariance across shallow radical levels. This is an all-residue-size/all-length classification including mixed characteristic and index-exact-three by subtraction, not a small isolated numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
