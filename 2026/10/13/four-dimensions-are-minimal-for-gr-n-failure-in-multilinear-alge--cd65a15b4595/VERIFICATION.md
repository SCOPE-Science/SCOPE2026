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

For the basis \((a,b,c,d)\), the only nonzero products are
\[
b^2=a,\qquad bc=b,\qquad cb=c,\qquad c^2=d,\qquad ab=d.
\]
The first four displayed products are the four basis vectors, hence \(A^2=A\).

For \(x=\alpha a+\beta b+\gamma c+\delta d\),
\[
xb=\beta a+\gamma c+\alpha d,
\]
so the annihilator is exactly \(kd\). Modulo \(kd\),
\[
xb\equiv\beta a+\gamma c,\quad xc\equiv\beta b,\quad
bx\equiv\beta a+\gamma b,\quad cx\equiv\beta c,
\]
so the second center is exactly \(ka\oplus kd\). Since \(ab=d\ne0\), \(a\) is not central.

The lower bound is symbolic: a strict second center yields a perfect quotient by the annihilator that has nonzero annihilator. Such a quotient cannot have dimension at most \(2\), because after choosing a complement to a nonzero annihilator line, all products span at most one dimension. Therefore the quotient has dimension at least \(3\), and the original algebra has dimension at least \(4\).

`check_grun.py` replays the table identities and verifies them over several finite fields. `verification_output.txt` ends with `CHECK_OK`. The all-fields theorem rests on the symbolic proof, not finite enumeration.
