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

# Verification record

The proof uses a ten-arc, six-vertex restricted de Bruijn digraph. Its five-parameter circulation equations, the two disjoint parameter cones, the exhaustive list of six simple cycles, and the two disconnected-support families are displayed in `RESULT.md`; these are the mathematical reasons the generating function holds for arbitrary lengths.

Run the included standard-library-only script as follows:

```sh
python verify_dual_rll_fourgram.py
```

Its independently implemented checks construct all balanced nonnegative profiles from both parameterizations through length 44, compare each support-connectivity decision against the two claimed excluded families, match rational generating-function coefficients, build and re-read an Euler circuit for every feasible profile, and separately enumerate every labeled binary word through length 18 for complete set equality. Actual output from execution:

```text
VERIFY_OK literal_all_binary_n=1..18 exact_flow_profiles_n=1..44 euler_tours=12596 disconnected_support_classification=PASS gf_coefficients=PASS
profile_counts_n2..18= [1, 2, 2, 2, 5, 4, 7, 10, 11, 14, 22, 22, 29, 38, 43, 50, 67]
```

The code performs finite checks only; it does not independently certify the infinite theorem or establish publication priority. The exact quasipolynomial period follows from genuine primitive-third, primitive-fourth, and primitive-sixth-root poles in the reduced rational generating function, not from sampled coefficients.
