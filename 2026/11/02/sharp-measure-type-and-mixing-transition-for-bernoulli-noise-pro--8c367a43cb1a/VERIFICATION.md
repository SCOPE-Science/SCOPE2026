---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each exact soft-threshold branch f± is q-Lipschitz with 0<q=1−ah<1, so backward coupling ensures a unique invariant law. Its images of I=[−B,B] overlap and cover I iff q≥1/2. For q<1/2 both branches are affine with strong separation, giving a nonatomic Cantor law of dimension log2/(−log q). At q=1/2 they halve I, giving exact uniform measure. For q>1/2 an arbitrary small plateau preimage can be hit by a common finite sign word from all x∈I, using a cylinder of diameter ≤2Bq^n; the uniform atom minorization yields TV geometric contraction. Stationarity and propagation of a reset atom give a dense countable purely atomic support. Finite-support laws from a deterministic start are TV singular to the nonatomic invariant laws. Independently checked exact rational endpoint geometry and a five-sign global reset word.

## originality

PASS

General random forward-backward invariant-measure results and classical two-branch IFS Cantor dimension theory are established mathematics. Their inspected statements do not give this explicit noisy-proximal trichotomy, including a dense full-support atomic invariant law and uniform Doeblin TV mixing at all smaller steps. Priority remains best-of-knowledge and exact-special-case IFS literature may contain equivalent statements.

## value

PASS

The measure-type transition exposes a concrete failure mode for inferring stationary density or total-variation mixing from weak convergence of fixed-step stochastic optimization. The dense purely atomic law alongside exact uniform/Cantor transition is a motivated structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
