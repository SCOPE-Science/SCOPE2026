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

The trace on a Weyl basis element factors as χ(u) conjugate(η(a)) A_g(a,χ). These are distinct characters of the orbit index group, so the nonzero columns are independent, and the zero columns give the exact kernel for the trace pairing. That pairing is nondegenerate, so the measurement-map rank equals the projector-span dimension. For a outside D an overlap is impossible; for nonzero involution a the two ordered contributions of a pair cancel exactly when χ(a)=−1, which occurs for N/2 characters. For the integer window, at a=0 the doubled powers have distinct exponents; at fixed a≠0 only reversal can repeat an unordered-pair exponent, and that happens only at an involution. After combining the reversals, each surviving coefficient has modulus 1 or 2, with at most N distinct exponents. The sum of terms below the top exponent E is bounded by 2N B^{E−1}<B^E, so every nonforced coefficient is simultaneously nonzero. Finite polynomial zero loci then give the claimed positive-orthant genericity. For prescribed S, informational completeness is equivalent to D=G and odd N; the stated existence over all real windows uses full support for the odd direction. I independently row-reduced the full projector orbit after a roots-of-unity specialization modulo 1009 on eight cases: ranks 49,21,52,12 for the specified proper supports and 60,52,36,81 for the full supports on Z_8, Z_4×Z_2, (Z_2)^3, and (Z_3)^2. Nonzero minors modulo the prime give exact complex-rank lower bounds and the analytic result supplies the upper bounds.

## originality

PASS

The supported distinct contribution is the all-group, all-prescribed-support maximum over real amplitudes, including the exact support-dependent involution loss and one simultaneous integer witness. The Weyl rank equivalence, prime-rational proper supports, and fixed-window cyclic boxcar ranks are prior coverage. The distinct same-day records give exact ranks or kernels on specific supports/windows, including an actual binary-Sidon real special case, but not the all-support optimization. No equivalent general statement was substantiated in the bounded comparison; no priority is inferred merely from a date.

## value

PASS

For a natural structured measurement ensemble, the theorem gives both the exact best operator rank under arbitrary missing-site constraints and the directions that no real taper can observe. The different capacities at order eight distinguish group structure rather than only size; the odd-order criterion and sparse difference-cover case directly inform support design. The constructive witness validates the uniform boundary, even though its magnitudes make it unsuitable as a practical taper.

The dated certificate retains the supplied scientific assessment, sources and limitations.
