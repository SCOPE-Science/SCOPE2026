---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Read actual RESULT.md blob 4eda4d6d72cd258edb7d1a11b81b58d1d3fb322c, verify.py blob fdaecde505a72430578ac46011a710498c2a46e3, and certificate metadata. The unique path forces F_j(p)=Σπ_i p^{|i−j|}. For n=4, six independent algebraic gap factorizations reduce to five monotone/linear residues and one monotonic equation 1/p+1+p (strictly decreasing for 0<p<1); no pair can switch from positive to negative back to positive. For n<4 pad zero source weights only within this proof. For five vertices, independent symbolic expansion verifies all four displayed F2−Fj factorizations; the first three stay positive and only F2−F1 changes twice at (5±√5)/10. Exact rational calculations verify unique winners at p=1/5,1/2,4/5 as 2,1,2. On longer paths, new zero-mass vertices score p^{j−4}F4<F4 at those three probabilities, and sufficiently small positive perturbations preserve all strict finite gaps. Thus all quantified cases follow analytically, not by finite path enumeration.

## originality

PASS

Qualified PASS: this is weighted decay centrality with source-specific vertex masses, not the unweighted decay centrality for which path rankings are stable in Hurajová–Gago–Madaras. Leskovec et al. study general outbreak sensor optimization and Holme a distinct temporal SIR detection metric, while the inspected scope of Tsakas is general decay centrality without this sharp weighted minimal reentrance threshold. A hidden weighted path-ranking theorem remains possible.

## value

PASS

The smallest path order allowing return of a previously uniquely optimal detector as transmission increases is a natural sharp qualitative boundary for epidemic sensing/weighted decay centrality. A complete no-reentry theorem below five and an exact double-crossover witness above establish a meaningful new failure mode for ranking stability; no general network or multiple-monitor claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
