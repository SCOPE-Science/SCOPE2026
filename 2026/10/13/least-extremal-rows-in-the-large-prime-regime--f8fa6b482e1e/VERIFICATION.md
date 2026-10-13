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
# Verification

The proof was checked at the level of definitions, quantifiers, boundary conditions, and carry counts. In the regime \(p>m\), one necessarily has \(p\ge3\), the next multiple \(T=p+s\) satisfies \(1\le s<m\), and every selected \(k\) satisfies \(s<k<p\). Kummer's residue form therefore gives exactly one borrow at the \(p\)-boundary and none above it. Earlier admissible rows are strictly below \(p\), so their binomial coefficients have zero \(p\)-adic valuation.

The global upper bound was separately reconstructed for an arbitrary admissible multiplier using the leading base-\(p\) digit split, with an explicit selected witness in each of the three cases. No infinite conclusion relies on finite enumeration.

The standalone `verify.py` checker uses only exact integer arithmetic and the Legendre formula for binomial valuations. It checked 5,250 pairs with \(2\le m\le80\) and prime \(m<p\le401\), covering 53,641 selected coefficients at predicted target rows and 48,391 earlier admissible rows. On a smaller subrange it also verifies exact divisibility by direct binomial coefficients. Replay output:

`VERIFY_OK cases=5250 target_coefficients=53641 lower_rows=48391 m_max=80 p_max=401`

The computation is a regression check, not a substitute for the proof. The originality assessment is limited to inspected literature and search results; it does not certify historical uniqueness.
