---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For an unrestricted partition, independently choose the odd-part subpartition of total a=(n+d)/2 and the halved even-part partition of total t=(n-d)/4. This is an exact bijection N_n(d)=Q(a)p(t) when both are nonnegative integers and zero otherwise; hence d=n (mod 4). Applying classical p(t) and Q(a) asymptotics uniformly on fixed |d|<=K n^{3/4} yields the exponent -pi d^2/(4 sqrt(6) n^{3/2}) and prefactor 2/(6^{1/4} n^{3/4}); Taylor remainder O_K(n^{-1/2}), prefactor relative error O_K(n^{-1/4}). Lattice spacing four and tightness yield CLT with variance 2 sqrt(6)/pi. For 4|n, exact balance Q(n/2)p(n/4) and its asymptotic follow. Independently enumerated all partitions for n=0..17 and confirmed the bijection; finite cases do not prove asymptotics.

## originality

PASS

Andrews–Ghosh Dastidar studies SOME(n) signed aggregate and congruences, not partition-level local distributions. Craig–Li alternates by part position, not size parity; Bringmann et al focus numbers of parts rather than total weight. Published weighted-representation partition claims concern different combinatorial objects. The exact Qp factorization is elementary and explicitly not new; novelty is at most the uniform local probability asymptotic.

## value

PASS

The total odd-minus-even PART WEIGHT is a genuine arithmetic statistic studied through aggregate signed sums. Its local partition-level Gaussian law, variance scale n^{3/4}, lattice-four support, and exact-balance rarity n^{-3/4} are a useful, non-obvious probability description, even though the generating-function factorization is classical and not claimed original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
