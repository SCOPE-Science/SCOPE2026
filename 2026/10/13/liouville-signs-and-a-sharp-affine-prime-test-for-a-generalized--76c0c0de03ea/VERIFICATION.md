---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The corrected RESULT keeps the positive-integer affine recurrence and exact polynomial. The difference of two floor sums changes each old term only at divisors of n, with increment c; subtracting the d=1 contribution gives s(n)=-1-c times the proper-divisor sum over d>1. Multiplying the convolution equation by mu and setting L=epsilon-mu gives s*(epsilon+tL)=epsilon+(t-1)L. L(1)=0 ensures coefficientwise finite inversion. Each squarefree factorization has the same sign, and inclusion-exclusion counts exactly the occupancy assignments with no empty slots. A prime of exponent E forces at least E slots and makes all E occupied, and K slots must all be prime, verifying the exact lowest and highest degrees and all signs. The already-covered prime threshold is correctly presented as a corollary: even K has positive sign, odd composite K>=3 has magnitude at least (c-1)^(K-1)>=4 for c>=3, and n=30 at c=1 and n=8 at c=2 give the failures. The frozen verifier and recorded output were inspected, not executed. Independent replay: python3 /workspace/branches/independent_probes.py 4; 648 exact floor versus first-factor calculations on 2<=n<=163 for c=1,2,3,4 with the two boundary counterexamples. This is bounded corroboration, not the proof.

## originality

PASS

The corrected files limit the distinct claim to the full signed polynomial for arbitrary exponent vectors, its explicit coefficient counts and sharp vanishing order. They credit the exact threshold overlap and acknowledge squarefree EGF, prime-power and constant-term coverage. No inspected statement supplies the mixed-exponent expansion or yields it by simple restriction of one of those special cases.

## value

PASS

The exact coefficients explain Liouville signs at every positive shifted slope and quantify how the Möbius zeros disappear: degree detects total prime multiplicity and order at slope one detects maximal prime multiplicity, with both coefficients known explicitly. This addresses the natural affine family on arbitrary exponent patterns, rather than offering only another proof of the threshold or claiming a faster prime test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
