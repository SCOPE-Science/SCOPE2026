---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Write rank-one T=uv*, ||v||=1, a=v*u, s=|a|², L=||u||². T²=aT and defining 2-partial-isometry identity reduce exactly to L(2−s)=1 (0≤s<2). Orthogonal component b=u−av has ||b||²=(s−1)²/(2−s). S=vw* with w=2u−La v and w*u=1 gives idempotents ST=P=vv* and TS=Q=uw*. For same positive bounded invertible G, two remaining Penrose equations are GP=PG and GQ=Q*G; these imply Gv=gv, Gu=cw, yielding g=c(2−L) when a≠0 and Gb=2cb. Therefore positivity requires L<2 (the a=0 exception automatically has L=1/2). G₀=(2−L)P+2(I−P) suffices; for a,b nonzero its forced eigenvalues give sharp cond 2/(2−L)=2(2−s)/(3−2s), while s=0,1 admit G=I. Endpoint s=3/2 gives explicit 2×2 T and S with (TS)(ST)=0 but (ST)(TS)≠0, forbidding any common orthogonal-projection metric. Independent sample s=1.2 yields cond=8/3 and correct Hermiticity; endpoint exact commutator contradiction. Proof works in infinite dimension; script finite tests are not infinite proof.

## originality

PASS

Source Aouichaoui–Buchała–Garcia 2026 Lemma 2.8 already proves reflexivity of the canonical generalized inverse and asks in Question 6 whether a single equivalent inner product can make it Moore–Penrose. The assigned rank-one theorem supplies a threshold, explicit boundary negative witness, and optimal metric distortion; this is not entailed by generalized reflexivity or failure in original metric. Resultary Moore–Penrose triple-transfer findings concern finite-field involution anisotropy, not these complex Hilbert operators. Full text of the 2026 paper was inaccessible after OA and authorized institutional attempts; its abstract and accessible mathematical setup were inspected. Priority and possible later answers are residual risks, not fabricated negative coverage.

## value

PASS

Answers a motivated open equivalent-inner-product question negatively already in rank one and gives the exact positive region with a quantified minimal condition-number divergence. The same Hilbert metric requirement and exceptions s=0,1 are essential, not a mere notation change. Exact threshold and distortion are useful even without general higher-rank classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
