---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For every b>=2,m>=1 the underlying probability space has b^m equiprobable leaves, with E_k conditional expectation by first-k prefix. The alternating difference transform T=Σ_{k=1}^m (-1)^{k-1}(E_k-E_{k-1}) has exact kernel depending only on longest-common-prefix length r. Summation by parts gives K_r=(b-1-2b(-b)^r)/(b+1) for r<m and K_m=(b-1)(1+(-1)^{m-1}b^m)/(b+1). Each K_r nonzero with explicit parity sign; the shell mass (b-1)b^{-r-1} and diagonal b^{-m} produce the exact row absolute sum 2(b-1)m/(b+1)+2(b-1)(1-(-1/b)^m)/(b+1)^2. Every row shares the norm and its sign function achieves it; self-adjoint duality gives same L1 norm. Orthogonal martingale differences give L2 norm 1. Direct independent rational conditional-expectation matrices checked for b=2..4 and m=1..4; symbolic sign/geometric series prove the full infinite-parameter statement.

## originality

PASS

Best-of-knowledge, after implication-aware prior/source comparisons: The exact all-branching sharp formula is a narrow, motivated endpoint refinement not obtained from the inspected prior theorems; full specialist older-literature priority remains provisional.

## value

PASS

This gives the sharp finite-depth endpoint cost of a completely natural alternating Haar/martingale multiplier on homogeneous b-ary trees, including all extremizing sign patterns and branching-dependent logarithmic amplification in the number of leaves despite L2 norm one. Such an exact endpoint benchmark is useful for martingale inequalities and shows why interior Lp/weighted bounds do not pin down L∞.

The dated certificate retains the supplied scientific assessment, sources and limitations.
