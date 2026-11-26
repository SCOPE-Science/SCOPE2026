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

Depressing the cubic is unique since 3 is invertible. For each depressed slope A the constants B and B+v−us run as an independent pair because u≠0, giving the exact autocorrelation sum over A. For A≠0 the discriminant factors as −27 times a translate of B² by a nonzero constant; the two-factor quadratic character count gives sum −χ_q(−3). A zero discriminant then gives two distinct rational roots: the double root is unique, hence rational, the simple root is rational, and a triple root would force A=0. For nonzero discriminants the parity of Frobenius on the three roots gives one rational root exactly for nonsquare discriminants. Counting all pairs (B,x) gives q and eliminates the repeated-root count, yielding m(A)=(q−χ_q(−3))/3. For A=0 the cube-map calculation gives m(0)=0 or 2(q−1)/3 as claimed. Exactly A=0 and A=−u differ from the generic product, and −3 is a square exactly when there is a nontrivial cube root of unity. The resulting expressions agree, and are positive at the smallest permitted q=5 and above. Independently evaluated root-avoiding constants by Horner evaluation in eight fields, including genuine quadratic extensions, and verified 526 shift cases; the counts at q=5,7,25,49 were 12,36,1728,13056. Replay: `python3 /workspace/branches/frozen_replay.py 5`.

## originality

PASS

The supported distinct claim is the exact count for a nonconstant linear difference over the full specified odd prime-power domain, not the twin-polynomial formulation, the main term, or arithmetic of a single cubic. The strongest accessible exact cubic literature counts constant differences and the literature covering the target differences gives only asymptotics. The exact local analogues inspected have different shifts, invariants, coefficient objects, or characteristic. The 2002 chapter remains an explicit priority risk, not a verified match.

## value

PASS

This is the exact first nonconstant shift family in the intensively studied cubic twin-prime count. It quantifies an arithmetic contrast: the exact answer is uniform in the two shift coefficients, with only a quadratic-character correction to the constant-coefficient-independent main terms, whereas the exact scalar shift can fluctuate with the scalar cube class and elliptic traces. The exact finite-field law, including extension fields, is useful as a benchmark for conjectures and computations on short polynomial correlations and is not supplied by asymptotics or a generic positivity statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
