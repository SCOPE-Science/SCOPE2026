---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For M=I−h(H+K), M−=M^T, Frobenius averaging over the two RR orders and four IID draws yields difference (1/4)||MM^T−M^TM||_F². Direct commutator calculation MM^T−M^TM=−2h²[H,K] with ||[H,K]||_F²=2||AC−CB||_F² proves the exact nonnegative formula for arbitrary d_x,d_y. A Rayleigh contraction bound 1−2hm+h²||H+K||² proves nonnormal pairs can be strictly stable. The scalar planar four-product expansion yields 4h³δω²(by²−ax²), and exact rational witness with A=3,B=1,C=1,h=1/8 gives gaps −5/1024 and +7/1024, sum 1/512. Independently evaluated actual products numerically at three choices and both basis directions; these checks are nonexhaustive. A sentence saying “averaging two basis starts” must be read with the explicit covariance-I normalization: unscaled uniform basis choice would halve the trace, whereas the precise theorem and subsequent proof correctly sum basis contributions.

## originality

PASS

Best-of-knowledge comparison of mathematically equivalent statements and possible stronger coverage, including Resultary semantic search, relevant published repository search, and primary literature readings. An adjoint pair of update matrices M and M^T yields a squared normality defect as the exact order-sampling gap. Prior PSD matrix-product inequalities apply to symmetric positive factors, unlike nonsymmetric GDA coupled maps; those inequalities cannot be substituted to deduce the reversed sign. Das et al. give K-epoch convergence bounds with step-size choices that may depend on K and n; those estimates do not order the two exact expected squared distances after one fixed two-step epoch. No stronger one-epoch theorem covering this opposite-coupling class was found in the searched material. Residual priority risks are recorded rather than treating negative searches as novelty proofs.

## value

PASS

The exact two-evaluation reversal is a motivated counterexample to unqualified random-reshuffling superiority on strongly convex–concave games, including stable components; the sharp commutator defect and initial-direction cone characterize when the reversal occurs. Although the trace lemma is elementary, its model-specific implication is not simply a textbook substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
