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

The two available path counts from vacant class sizes u,v are choose(u,2)v and u choose(v,2). Equal-rate clocks choose proportionally, which gives the stated two-count recurrence. The required type counts a−t and 2t−a prove feasibility; any such schedule has positive probability. Subtracting adjacent recurrences gives the stated positive-coefficient difference recursion. For t≤a<floor(3t/2), the earlier difference at a−2 is strictly positive (including at the support entrance), and the one at a−1 is nonnegative, including the preceding odd central tie. The t=2 base and symmetry give exactly the listed maxima. The extreme profile iterates the factor (2t−1)/(3t−2), while the inward ratio satisfies r_t=[t+2(t−1)r_(t−1)]/(2t−1), r_1=1, yielding (t+2)/3. Summing gives S_t/S_(t−1)=(3t−1)/(3t−2); both gamma identities and the edge asymptotic follow. Normalization gives the urn as stated, including its mixed symmetric initial state. Its centered increments are ±1/2 with conditional mean C_k/(3k+2), proving the exact variance recurrence. The even-moment recurrence has homogeneous growth k^(2r/3), below the forced order k^r, and forces successive Gaussian moment constants by the factor (2r−1)·3/4. Uniform moment bounds and Gaussian determinacy justify the weak limit, not pointwise probabilities. Independently written exact code agreed with all 26 positive labeled bipartitions through t=4, checked the stated profile identities through t=80 and matched independent normalized urn propagation through t=41. The uploaded verifier was inspected, not executed.

## originality

PASS

Credit the distinct exact perfect-cover composition analysis: the strict optimizer, evaluated edge and first inward layer, and identification of its normalized finite law. Do not credit the two-count jump mechanism as distinct from the same-model jamming record, or the Gaussian limit as an independent urn theorem. The inspected general Eulerian theorem already implies the Gaussian limit once the adsorption coefficients are identified; it does not supply that model-specific identification or the evaluated edge and optimizer. No exact prior coverage of that residual analysis was established in the bounded comparison.

## value

PASS

Perfect occupation is a practical and sharply defined endpoint of a natural irreversible matching process. For a fixed total size, the finite analysis answers which bipartitions maximize it, quantifies how rare success is at the feasibility edge and the exact gain from moving one site inward, and explains the distribution of favorable compositions. Those results are useful independently of the known general Gaussian machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
