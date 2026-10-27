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

# Reproduction and evidence

Run `python verify_cube_expectation.py` using Python 3 and its standard library. It enumerates every source word in six rational source laws with \(q\in\{2,3,4\}\), computes all distinct nonempty scattered cubes by testing all possible roots, weights each input by its exact source probability, and compares every resulting mean with coefficients independently constructed from \(T(z)/((1-z)(1-T(z)))\).

Observed execution: `VERIFY_OK exact_source_words=115024 probability_vectors=6 max_length=12 rational_coefficients=True stationary_saddle_checks=5 alphabet_support_comparisons=199`.

Source distributions and maximum lengths: fair binary (12), biased binary (11), uniform ternary (9), biased ternary (9), uniform quaternary (7), biased quaternary (7). In addition the verifier checks strict integer-power rational inequalities used for \(m=4\), the support-size formula through \(m=199\), and five stationary-pair derivative relations. These are finite cross-checks; the infinity of word lengths, all admissible probabilities, global maximization and singularity asymptotics are proved analytically in `RESULT.md`, not certified by enumeration.

The precise claim concerns distinct cube **strings**, not multiple embeddings of a cube within one source string. The input alphabet and positive probabilities are fixed in the asymptotic statement. No independent audit has been performed.
