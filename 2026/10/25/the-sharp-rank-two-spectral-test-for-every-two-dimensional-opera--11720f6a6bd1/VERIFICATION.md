---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The central nonscalar-compression lemma is checked directly: take x,y with Ax,Ay independent and a bounded V with VAU=I2. If all admissible VBU are scalar, varying V by coordinate functionals vanishing on ran(AU) forces Bx,By to lie in span(Ax,Ay), and their scalar compression makes both Bx=cAx and By=cAy. Varying x,y with overlapping pairs yields one c globally; for any z in ker A, compare x+z and x, giving Bz=0. Thus B=cA contradicts independence. For a nonscalar 2x2 M, choose an explicit traceless involution H with tr(HM)!=0, then T=UHV has rank2. PQ/QP yields the nonzero spectrum of H(λI+µM), with trace µtr(HM)!=0 if µ!=0 and eigenvalues ±λ if µ=0. This proves strict positivity, uniform over the compact parameter sphere. Rank-one T gives a nonzero C in trace-kernel of V, making CT²=0; if all C rank<=1 the same holds for any T. Independently exhaustively tested the H matrix identities for 78 small-entry nonscalar matrices. Verified finite tests are not proof of the Banach-space lemma.

## originality

PASS

Aznay–Chabbabi 2026 Lemma 3.2 gives some finite-rank common right multiplier for complex infinite-dimensional pencils, via adding to a rank-two seed, but does not bound the rank of the final detector. The submitted optimal exactly-two rank and real-field extension are additional; zero-trace obstruction is already known from that paper. Separate classical spectral-radius multiplier papers consider one operator at a time, not a fixed common detector.

## value

PASS

The exact minimal complexity of a common spectral test is a direct and natural refinement of an existence lemma used in product-nilpotence preserver theory. A rank-two universal detector is optimal, valid independent of the Banach dimension, and accompanied by a crisp impossibility boundary, giving an explicit useful finite-dimensional compression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
