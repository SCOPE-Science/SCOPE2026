---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Disjoint specified cycles under Ewens have factorial moments equal to the product of powers of theta/j times (n)_h times the ratio of rising Ewens normalizations for n-h and n; the latter combined factor tends to one at fixed h. This yields independent short-cycle Poisson counts, with O_P(1) short-cycle vertices whose marks disappear. Hanf locality for the degree-two relational graph reduces any fixed sentence to finitely many neighborhood counts capped at a fixed threshold. A long-cycle word with j positive marks has mean asymptotic to n p_n^j; the overlapping distinct windows for this fixed word are incompatible or require at least j+1 marks, giving conditional variance at most n p_n^j+O(n p_n^(j+1)). Thus zero or infinite scales imply disappearance or saturation. The all-unmarked path type saturates; intermediate-length unmarked cycles with the same path type do not affect that conclusion. At the unique possible finite positive k, use maximal clusters joined by gaps at most H>2r. Discard cycles up to a fixed cutoff larger than the support of such clusters, with loss O_P(1) and negligible marks. For t prospective cluster starts and fixed gap types, the widely separated choices number n^t(1+o_P(1)) given the permutation, and have marking probability p_n^(kt)(1+O(p_n)); the O(n^(t-1)) close choices have probability at most p_n^(kt) if feasible, since distinct realized maximal clusters cannot share a marked vertex. Thus mixed factorial moments give independent Poisson(lambda) gap-type counts conditionally in probability, hence independently of fixed Ewens counts in the limit. Expected chains of k+1 distinct marks with all gaps at most H are O(n p_n^(k+1))=o(1); this also excludes longer wraparound clusters, while shorter cycles with potential wrap ambiguity were discarded. Every critical word then comes from one cluster with a fixed computable multiplicity; counts need not be independent at the rooted-type level. The finite truncated Hanf profile has a limiting distribution and determines sentence truth; Poisson inputs can themselves be capped at the threshold for the linear contributions. For necessity, consecutive distinct k-runs agree with the unit-gap clusters at finite positive scale except on the negligible events above (choose the cutoff for that k), so their existence tends to 1-exp(-lambda) jointly with short unmarked cycles. At scale zero use the first-moment bound, and at infinity disjoint k-blocks cover all but O_P(log n) vertices using the Ewens cycle-count expectation. Thus the run sentence detects the extended limit injectively on every convergent subsequence; compactness gives necessity without monotonicity. The fixed-point probability is 1-exp(-theta), excluding a zero–one law. A separate finite enumeration reproduced 24 exact run-mean cases at theta=1,2, n<=5, p=1/3 and feasible k<=3; this corroborates only the finite identity. The frozen checker was inspected but not executed.

## originality

PASS

Best-of-knowledge pass for the exact iff law in the directed Ewens successor language with arbitrary vanishing mark sequence, together with the critical Poisson vector independent of the Ewens cycle background. Sparse unary thresholds, bounded-degree locality and Bernoulli run Poisson limits have substantive antecedents; those methods and the unmarked baseline are not claimed as new.

## value

PASS

This is a natural complete logical convergence criterion, including oscillatory and boundary regimes rather than only regularly varying scales. It identifies the finite cluster variables needed to compute sentence limits and separates correlated critical rooted counts from independent Ewens cycle counts; neither a single run calculation nor random-permutation locality alone supplies that description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
