---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- The source places \(\mathrm{Hoch}(1,n)\) in \(\sum_i x_i=\binom{n+2}{2}\).
- The source supplies tight subset-sum right-hand sides and an explicit formula for them.
- Specializing that formula to \(m=1\) gives \(z_J=\binom{a+c+1}{2}+b\).
- With \(k=a+b+c\), one has \(z_J\le\binom{k+1}{2}\).
- The projected normal to a \(k\)-subset hyperplane has squared norm \(k(N-k)/N\).
- The uniform center is therefore at distance at least \(\frac12\sqrt{Nk(N-k)}\) from every facet hyperplane.
- All singleton tight inequalities are \(x_i\ge1\), and summing their exact radius constraints gives the sharp upper bound.
- Equality forces every center coordinate to \((N+1)/2\).

`verify.py` checks the algebraic inequalities exactly for \(3\le N\le200\) over all abstract parameter triples allowed by the specialization. It does not assess originality and does not replace the source verification.
