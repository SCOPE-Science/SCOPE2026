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

Exactly h numerator generators give the entire integer interval from ah to (a+3)h, so quotient membership is the union of I_h. The nested offset intervals have h+1 offsets if 3|h and h otherwise; the chosen interval [-A,B] first spans all x residues, dropping the larger duplicate endpoint only for x≡0. Earliest arrival of each offset is q(t). To exclude any better representative from later intervals, min I_(q0+1)−max I_q0 is respectively 0,1,0 in the three residue classes for both r, and later lower endpoints strictly increase. I_1={x} and later lower endpoints exceed x. The genus check is Σ q(t)−A: use Σ_{j=1}^L 3j=3L(L+1)/2 and Σ ceil(3j/2)=[3L(L+1)+2ceil(L/2)]/4 with L=A or B as appropriate. The larger of the two endpoint values minus x yields each F entry. For PF, the quoted generator edges remove all but the two terminal branches: for r=1 keep −A, B and B−1 only if B is even; for r=2 keep −A, B if B>0 and −A+1 only if A is even. To check domination it suffices to compare these candidates, since any element not maximal is below a maximal one. For r=1, the positive pairwise differences are {1}, {2,x−1,x+1}, and {3x−1} in x mod 3 order. Only the last belongs to T, taking −A to B. For r=2 they are {x−1,x+2,2x+1} when x≡0 and x≥6 (only {x−1} at x=3), {x−1,2x−2} for x≡1, and {x+1} for x≡2. None belongs to T using the displayed generators (the smallest nonmultiplicity generator is 2x−1). This proves precisely the PF sets and small type exception. Independently, original-generator additive dynamic programming followed by direct gap/PF testing agreed for x=3..75 in both families (/workspace/replay/independent_checks.py, semigroups, 146 pairs). This test uses no proposed quotient generating set for membership, finds x consecutive members to certify the conductor bound, and is finite.

## originality

PASS

Both interval-semigroup theory and the general quotient-generator theorem apply, so neither the interval description nor the four-generator presentations are credited as novel. The contribution is the explicit evaluation of the Apéry staircase and all three invariants, especially the complete pseudo-Frobenius spectrum and its small exception. The inspected closed formulas are for genuinely different ranges or families. This is a bounded statement-level comparison.

## value

PASS

This is an infinite, naturally motivated nondivisible subfamily of a published quotient problem. In particular the pseudo-Frobenius classification goes beyond calculating a largest gap: it captures every semigroup-order maximal gap and explains why the types vary across this natural residue split, including the boundary exception. The interval model and generator lists alone would not warrant the value decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
