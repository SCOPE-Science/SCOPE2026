---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The exact parity-conditioned increment law for r(q+1)-r(q) follows from the trailing-ones carry. Splitting n=2^kq+a and averaging over the two high-block parities yields P_k=(2+sum_{1<=a<2^k}(G_even(d+hprime)+G_odd(d-h)))/2^(k+1). For k>=4 classify a by v2(a): interior weights W0=W1=37/8 and Wj=8-27/2^(j+2) for j>=2, with two explicitly handled boundary valuation classes. The finite geometric sum is exactly 83*2^(k-6) for T_k and gives P=83/128. Short k direct exact residue evaluation gives listed initial fractions. The infinite limit follows from truncating long carry runs, whose omitted density tends to zero, not from the finite checker.

## originality

PASS

The genuinely uniform evaluation P_k=83/128 for every k>=4 is not explicitly given in the inspected all-shift recursive prior source. The earlier work supplies general computational recurrences and a central-limit statement depending on many 1-runs, but its recurrence does not itself display or establish uniform stabilization for this one-run family; the novel content is the nontrivial all-k summation.

## value

PASS

The adjacent-11 analogue of a Cusick-type sign-bias problem is a motivated digital-arithmetic question. The infinite family 2^k−1 stays outside the many-run central-limit regime; an exact rational density independent of k from k=4 gives a substantive arithmetic stabilization, rather than an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
