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
# Verification

Fix an integer \(r\ge1\) and a proper lovely pair \(P\preccurlyeq R\) of real closed fields. Choose \(t\in R\setminus P\). Since \(P\) is real closed and elementary, \(t\) is transcendental over \(P\), so
\[
a_i=t^i\quad(0\le i<r)
\]
are \(P\)-linearly independent.

For each \(i<r\), put
\[
H_i=\sum_{j\ne i}Pa_j.
\]
Membership in \(H_i\) is first-order definable in the pair language using the finitely many parameters \(a_j\). Choose distinct \(c_m\in P\), \(m<\omega\), and use the row
\[
x-c_ma_i\in H_i.
\]
Two formulas from one row are inconsistent because their difference would put a nonzero \(P\)-multiple of \(a_i\) in the span of the other \(a_j\). Every choice of one formula from each row is realized by
\[
x=\sum_{i<r}c_{m_i}a_i.
\]
Thus there is an inp-pattern of depth \(r\) in one object variable. As the dense-pair theory is NIP, burden and dp-rank agree, giving \(\operatorname{dp-rk}(x=x)\ge r\).

For a fixed \(k\ge1\), RCF has unary dp-rank \(1\), while its lovely-pair theory has unary dp-rank exceeding \(k\). Kim Theorem 10.33 preserves every member of \(\mathfrak D^h_{n\text{-var}}\) between a geometric theory and its lovely-pair expansion. Therefore the class of complete NIP theories with \(\operatorname{dp-rk}(x=x)\le k\) is not a member of that framework.

## Limits

No infinite-depth inp-pattern is claimed. No failure of strong dependence is claimed. No computation or finite experiment is used.
