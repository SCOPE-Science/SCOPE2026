---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Cycle type bijects isomorphism classes with integer partitions under the stated uniform law. Deletion and inclusion–exclusion give exact tail and prescribed-multiplicity counts even when shifts exceed n, using p(k)=0 for k<0. For the ratio, the leading Rademacher term with x=n−1/24 and c=π√(2/3) is exp(c√x)/(4√3 x) times (1−1/(c√x)), up to exponentially subleading error; taking a fixed shift changes the main exponential by 1−ch/(2√n)+O_h(n^(-1)) and the prefactors by 1+O_h(n^(-1)). A prescribed multiplicity at length j therefore costs πj/√(6n)+O(n^(-1)), while the two-length mixed difference cancels both constant and linear-shift terms. Effective bounded-degree Hanf locality gives a radius ρ and saturation t. The Gaifman balls in cycles of length ≤2ρ+1 are the whole directed cycles and in larger cycles are identical directed paths, with the radius-zero loop case distinguished. Thus short-type counts are j a_j and the long-type count is the total number of vertices in longer cycles. If fewer than t such vertices occur, their parts come from a finite list and all other parts are bounded in size, giving only polynomially many partitions against exponential-in-√n p(n). At order n^(-1/2) only the finitely many isolated short-type deficiencies matter, each evaluated on its explicit representative. This yields the stated effective weighted integer sum and its sign, with all other events contributing O_φ(n^(-1)). Absence of any prescribed m-cycle realizes (0,m), negation realizes (1,−m), and constants cover m=0. Nonzero coefficient forces the claimed sharp rate.

## originality

PASS

The qualitative law for the exact unlabelled model is known. Judged only on the effective first correction, its quantization and attainable spectrum, and the O(n^(-1)) remainder: inspected close sources do not cover or imply that combined quantitative result. A fixed multiplicity cap has a different limiting local law even though it uses the same logical machinery. This is best-of-knowledge, without dating-based priority inferences.

## value

PASS

A qualitative zero–one law leaves open whether finite structures approach it slowly, rapidly, or in a sentence-dependent continuum of leading coefficients. The theorem instead determines the complete discrete first-correction spectrum, a computable test for whether the leading term vanishes, and the resulting improvement to O(n^(-1)). It identifies exactly which local defects control the rate in a canonical unlabelled model, rather than tabulating a few examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
