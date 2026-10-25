---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: Write A=π(n²), h=π((n+1)²)−π(n²). For n≥100 every prime in the interval is coprime to six, hence h≤2 floor((2n+1)/6)+2≤(2n+7)/3. Rosser–Schoenfeld π(n²)>n²/(2log n) yields n log(1+h/A)<(4/3+14/(3n))log n≤1.38log n, while log A>2log n−log(2log n)>1.5log n for n≥100. Thus A^(n+1)>(A+h)^n. Independently sieved/trial-checked every integer through 10000 and verified all 97 exact integer-power inequalities for n=3..99; n=2 fails. Finite range is genuinely exhaustive and tail proven analytically.

## originality

PASS

PASS best of knowledge: Sun 2014 Conjecture 2.14(ii) states precisely this monotonicity as conjectural; OEIS A038107 still records it as a conjecture. A general prime-count lower bound and trivial modulo-six sieve are old, but no inspected source combines them into this all-n explicit proof. Search absence does not establish definitive priority.

## value

PASS

PASS: Full resolution of an explicitly formulated uniform prime-counting monotonicity conjecture with sharp starting index is a mathematical result; not merely a finite verification, since an unconditional analytic tail covers all remaining n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
