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

The rotation-invariant indicator gives diagonal matrix elements because the given basis vectors have distinct angular frequencies. With t=|z|² the angular integral against π⁻¹dA cancels the radial Jacobian, yielding the stated density. For P=(t−k)(t−k−1), the derivative numerator (k−t)P+tP′ equals both Q_k and (k+1)(t−k)²−t(t−k−1)², proving the annular boundary identity with the correct sign. The zeros at 0,k,k+1 and positive decay at infinity imply one critical point in each proposed interval; the cubic permits no more and forces simplicity. For m=k+1≥4 and 1<y<m, the reflected ratio of the polynomial factors is (y+1)/(y−1), giving the quoted half-log ratio. The strict atanh lower bounds reduce it to a value strictly above [1−v+(m−1)v²/(3m)]/y, v=y²/m; the discriminant is (4−m)/(3m), so the conclusion is strict even at m=4. For k=1 the comparison uses max_{0<z<1}(z−z³)/2=1/(3√3) and the value at 4. For k=2 the displayed factorization and e^x≥1+x bound the inner hump by 1/6, while the value at 6 is larger (e<137/50 and (137/50)^6<432). Thus the outer maximum strictly dominates. For 0<a<u_k the later solutions are one on the falling inner branch and two on the outer hump; for u_k≤a<k only the latter two remain. At a=k the other zero k+1 is the sole finite future solution. For k<a<v_k there is one solution on the rising negative branch, while from v_k through k+1 there are none. For k+1<a<w_k the falling outer branch gives one, and at or after w_k none. No future intersection is critical, and the zero at k+1 from a=k is simple. The included checker and recorded output were read, not executed: the 182 checks are symbolic at finitely many k and numerical at sampled radii; they do not certify the all-index or endpoint count.

## originality

PASS

Radial diagonalization, Laguerre densities and the exact one-boundary disk difference for the same space are covered. That disk identity immediately gives the annulus difference by subtraction. The supported distinct result is the strict all-index comparison of positive maxima and its consequence, the complete annular crossing classification with sharp three reversals. Neither the same-space disk result nor the inspected analytic-Fock annulus results cover that comparison or its classification.

## value

PASS

The metric is a natural spectral-order question for radial localization, and a pair that switches order three times at fixed inner radius is a substantive departure from disk ordering. The classification for all inner radii and all adjacent pairs in the first true-polyanalytic layer pinpoints the transition, including whether an apparent crossing can be tangential. Its key strict height comparison is not routine from the disk identity. The result is useful for testing annular order claims without asserting anything about all-mode maximizers or higher layers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
