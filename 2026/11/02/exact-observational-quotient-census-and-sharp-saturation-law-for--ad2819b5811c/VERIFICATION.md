---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Under exact tests T_l and single-agent S5, atomic profiles c and class support S give full formula equivalence iff pairs (S,c) agree: atoms recover c, modal exact tests recover S; box induction establishes converse. A block with support size s has EGF (e^z-1)^s, arbitrary set of such blocks exp((e^z-1)^s), and marking distinct realized supports yields product over s of [1+u^s(exp((e^z-1)^s)-1)]^{binom(m,s)}. Type families require sum|S|<=n; maximum M=m2^{m-1}. Missing singleton support coefficient ratio by saddle at W(n)/m gives exp(1-(n/W(n))^{1/m}) and for m=2 a nonvanishing saddle-displacement correction exp(-1/8). Higher supports and multi-singleton absences negligible at fixed m. Independent direct n<=5 enumerators m=2,3 matched and numerical m=2 coefficient ratios at n50,100,200,350 approached predicted prefactor; this is a sanity check, not proof of asymptotic.

## originality

PASS

Support-type semantics and multiplicity-insensitive bisimulation are already known from Ciardelli–Otto and prior finite Heyting modal quotient work, explicitly credited. The separate contribution is exact labelled bivariate census, type feasibility threshold, and sharp rare-event asymptotic with exceptional m=2 factor. Generic species and saddle methods are standard, but inspected modal texts did not contain these enumerative statements. Priority risk from colored set-partition literature remains.

## value

PASS

The natural S5 quotient under full exact tests has an exact distribution and saturation threshold, quantifying how model multiplicities collapse observationally; the rare-event constant e^{-1/8} is a substantive sharp boundary correction rather than a routine table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
