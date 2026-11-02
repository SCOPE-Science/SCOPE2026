---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Index a p-level graph-state stabilizer element by r in F_p^(m+n); a local Pauli operator is nonidentity precisely if (r_i,(Gamma r)_i)!=(0,0). In K_{m,n}, each side's adjacency value is the other side's sum, so the four mutually exclusive events (S_A,S_B) zero/nonzero yield exactly Z_m Z_n; p^(m-1) z^m N_n; p^(n-1) z^n N_m; and (p-1)^2 p^(m+n-2) z^(m+n). Finite-field character orthogonality supplies the correct Z_r and N_r, and the total at z=1 is p^(m+n). With m fixed, B-side coordinate support satisfies a binomial weak law even after conditioning on its sum (conditioning event has fixed positive probability). If S_A=0, the normalized weight tends to (p-1)/p, probability 1/p; if S_A!=0, B-side support is full, giving limit 1 with probability (p-1)/p. Independently enumerated all p^(m+n) stabilizer labels in 26 small (p,m,n) cases and matched every enumerator coefficient. This proves the stated finite formula analytically and the asymptotic via conditional law of large numbers, not via finite experiments.

## originality

PASS

Qualified best-of-knowledge PASS for the explicit K_{m,n} closed polynomial and its two-atom fixed-side limit. Miller et al. 2023 already give a fully general graph-theoretic representation for graph-state SLDs, including qudits, and formula (43) as an unevaluated sum over Pauli labels; this does contain the object abstractly and is fully credited. The primary PDF's exact-family section treats complete graph/GHZ, stars, cycles and Pusteblume; text search found no 'bipartite'. It does not exhibit the K_{m,n} explicit polynomial or its weak limit. The derivation is an elementary yet non-identical family-specific evaluation, not a new general SLD theorem. A possible coding-theory equivalent weight enumerator remains a priority risk.

## value

PASS

Complete bipartite qudit interaction graphs are canonical many-body stabilizer constructions. An explicit support enumerator for every prime local dimension and pair of part sizes is a natural exact invariant; the two-atom limit reveals a qualitative breakdown of typical single-binomial SLD concentration. It can serve as an exact benchmark for multipartite correlations without claiming by itself an entanglement threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
