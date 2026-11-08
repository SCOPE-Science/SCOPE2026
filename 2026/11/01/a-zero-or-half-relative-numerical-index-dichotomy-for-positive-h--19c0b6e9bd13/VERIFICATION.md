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

Reconstructed the precise p_G seminorm and paired-vector v_G limits. Since (I−G)^2≤I−G², unit near-norming pairs have y−x→0; this yields the same near-norming-vector characterization of v_G. For compact injective D, near-norming unit sequences are precisely weak-null, hence p_G=||T||ess and v_G=w_ess(T). Finite-rank head/tail decompositions establish the Calkin norm and tail numerical-radius identities; classical w(S)≥||S||/2 and square-zero infinite-multiplicity partial isometry give sharp 1/2. D=0 reduces to ordinary w/||.||. With nonzero ker D and D≠0, a rank-one map from ker D to a positive spectral band gives p=1,v=0. With injective noncompact D, take infinite low- and high-defect spectral subspaces and a partial isometry low→high: p=1,v=0, including spectral-limit boundary. CHECK.py consists of finite spectral/quadratic diagnostics; it does not prove the infinite statement. No missing positive-contraction spectral case.

## originality

PASS

Best-of-knowledge originality passes for the joint v_G identification and exhaustive positive-contraction eta=0/1/2 phase diagram, not for classical numerical-radius inequalities or the previously published p_G essential-norm criterion.

## value

PASS

A complete, sharp index dichotomy for all positive norm-one infinite-dimensional Hilbert contractions gives the exact structural boundary between compact-injective defects and every other spectral regime; explicitly captures discontinuity for arbitrarily small finite-rank defects and distinguishes full norm from quotient seminorm. These are motivated nontrivial infinite-dimensional operator-geometry facts, not a routine finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
