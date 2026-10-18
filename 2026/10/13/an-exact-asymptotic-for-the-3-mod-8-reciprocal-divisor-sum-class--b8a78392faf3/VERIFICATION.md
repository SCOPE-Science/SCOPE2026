---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The published class has unique p (the only prime at odd exponent), so no multiplicity overcount. Terms exponent>=5 satisfy sum_{p,j>=1}sqrt(X/p^(4j+1))=O(sqrt(X)) by convergent p^-5/2 series. In the e=1 layer dropping p∤k adds only O(sqrt X) pairs by k=p*l, sum_p sqrt(X/p^3). The main sum M(X)=sum_{odd k<=sqrt(X/3)} pi(X/k^2;8,3). For fixed k the progression PNT yields (log X/X)*pi(X/k^2;8,3)->1/(4k^2). Split k<=X^(1/4): Chebyshev bound pi(y)<<y/log y gives uniform C/k^2 bound since y>=sqrt X; k>X^(1/4): pi(y)<=y yields O(log X*X^(-1/4)). Dominated convergence gives 1/4 sum_odd k^-2=(1/4)(pi^2/8)=pi^2/32. Error O(sqrt X) is o(X/log X). Independent exact prime/square enumeration at X=200000 gave 6160 members (11 in e>=5 layers); finite counts are not proof of the asymptotic.

## originality

PASS

Best-of-knowledge PASS. An equivalent result under either quadratic-form or squarefree-kernel terminology would need the X/log X order and constant. The natural density-zero statement alone allows many rates and cannot give it. The later assertion implies the old zero-density result, not vice versa. Even though the proof uses well-known prime-distribution methods, extracting the sharp constant is a new natural quantitative fact not mechanically contained in a table. Residual priority/access caveats explicitly included; no search absence alone is interpreted as novelty.

## value

PASS

Turns an explicitly known natural density-zero arithmetic class into an exact quantitative distribution law with constant, resolving a worthwhile missing scale for an OEIS-indexed residue class of the reciprocal divisor-sum generating series. The X/log X first-order term is not determined by the older density-zero theorem or a finite table; this is an independently useful natural exact enumeration asymptotic, even without settling the full reciprocal-set positive-density conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
