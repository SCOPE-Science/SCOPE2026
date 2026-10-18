---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The infinite proof splits N into r=1,2,3 coprime prime-power blocks. r=1 gives (M-1)N=2; r=2 gives M=2 then (A-1)(B-1)=3, whose sole candidate blocks (2,4) are not coprime; r=3 bounds sigma*/N <=12/5 and N>=30, hence M=2. The linear equation C(AB-A-B-1)=AB+A+B+2 forces (for A=2) B-3|13 with B=4 or16 noncoprime; for A=3 an even denominator divides 13, impossible; and for A>=4,B>=5, monotone D(A,B)=AB^2-2AB-B^2-2B-A-2>=19 forces C<B, contradicting order. An independent factorization enumeration of 2<=N<=40000 found only N=2. This finite check supplements, not proves, the unbounded case.

## originality

PASS

Best-of-knowledge: the minus-sign small-support obstruction is not implied by the inspected plus-sign Lehmer analogues or Yamada large-support estimates. The congruence reformulation was compared; a generic bound on M does not eliminate M=2 for three factors.

## value

PASS

The low-support barrier is motivated by the open unitary near-perfect/Lehmer-type minus-one equation. Exact elimination of all nontrivial three-factor candidates is an unbounded necessary structure theorem, not just a finite search or a renamed classical opposite-sign result; it sharply relocates any hypothetical counterexample to omega>=4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
