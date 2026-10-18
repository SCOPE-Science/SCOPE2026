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

## Reproduction

Run `python3 verify.py` with Python 3 and no third-party packages. Expected last output line: `ALL_EXACT_CHECKS_PASS`. The verifier constructs six unweighted strongly regular graphs and checks all unordered vertex pairs to recover the strongly regular parameters. For each edge, it checks the integer identity \((kI-A)((h+1)I+A)b_e=Db_e\), the computed voltage drop \(2h/D\), the total-variation/coarea wing formula, and the cycle complement identity. It computes all exact endpoint column sums using `fractions.Fraction`; no random sampling is used. In particular the complete rook and Shrikhande tests examine 48 of 48 edge columns each.

A separate symbolic calculation formed each \(16\times16\) Laplacian \(L\), computed \(L^+=(L+J/16)^{-1}-J/16\) over rational numbers, and checked \(Q^2=Q\), \(C^2=C\), rank \(15\), and the four claimed exact column-sum maxima on \(48\times48\) matrices. The resulting values agree with the explicit proof. The general theorem relies on its algebraic proof rather than the finite examples.

## Scope of verification

The assertions concern only the Euclidean orthogonal cut and cycle projections of unweighted connected noncomplete strongly regular graphs considered as bounded operators on real finite-dimensional edge \(\ell_1\) and \(\ell_\infty\). The claim does not cover minimum projection constants, arbitrary weighted networks, or intermediate exponents. No independent scientific audit has been performed.
