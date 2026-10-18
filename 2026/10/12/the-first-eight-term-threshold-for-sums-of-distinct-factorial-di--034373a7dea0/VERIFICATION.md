---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The subset-of-divisors recurrence follows by disjoint include/exclude cases and remains exact when sums>N are masked. Independently reimplemented at-most-j integer bitsets, a different recurrence initialization from source exact-j layers; checked every integer 0..n! for n=1..12, all 792 divisors of 12!, and first/largest unrepresented numbers. Independent recomputation produced h=(1,1,2,3,4,5,5,6,7,7,7,8), with exactly 175 misses at seven terms, first 475785157 and last 479001547; all 479001601 totals represented by at most eight distinct divisors. The source artifact lists 175 integers and the displayed eight-term witness sums to the first. This is an exhaustive finite result, NOT an inference about later factorials.

## originality

PASS

The exact invariant h(n!) is explicitly studied by Hughes and older Yokota, so only the 1..12 finite transition and exact 175-element layer count are in scope. Hughes abstract describes h(n!) asymptotics, and full Tenenbaum–Yokota 1990 Lemma 4 has an unspecified large-k cutoff, not a 12! optimum. A high-overlap Yokota 1992/1995 text could conceal finite tables and remains an identified unresolved priority risk, but lack of access alone does not falsify this novel best-of-knowledge result.

## value

PASS

The first point where a natural cardinality-constrained invariant h(n!) reaches eight is a meaningful exact finite cutoff for the factorial divisor-covering problem posed by Erdős and investigated by Hughes. A complete 1..12 profile, thin 175-member extremal layer and reproducible exact certificate provide concrete benchmarks and potential structure for later bounds, despite not proving a general formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
