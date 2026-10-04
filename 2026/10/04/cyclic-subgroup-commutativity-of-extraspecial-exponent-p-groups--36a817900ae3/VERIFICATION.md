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
The universal proof uses the extraspecial commutator form
\[
B:G/Z(G)\times G/Z(G)\to\mathbf F_p.
\]

Critical checks:
- every nonidentity cyclic subgroup has order \(p\);
- there are \(pN+2\) cyclic subgroups in total;
- the unique nontrivial central cyclic subgroup is \(Z(G)\);
- every projective point of \(G/Z(G)\) has exactly \(p\) noncentral cyclic-subgroup lifts;
- two noncentral cyclic subgroups permute exactly when their quotient lines are orthogonal;
- a line in a \(2n\)-dimensional symplectic space has
  \[
  R=(p^{2n-1}-1)/(p-1)
  \]
  orthogonal projective points;
- the ordered commuting-pair count is
  \[
  p^2NR+4pN+4.
  \]

The packaged checker `artifacts/verify.py` constructs finite Heisenberg groups for
\[
(p,n)=(3,1),(3,2),(5,1),(5,2),
\]
enumerates cyclic subgroups directly from multiplication, tests every ordered pair for permutability, and verifies the closed formula and the published \(n=1\) specialization.

It returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.
