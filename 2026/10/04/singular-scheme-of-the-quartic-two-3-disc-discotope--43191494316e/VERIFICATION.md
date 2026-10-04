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

Run `python verify_discotope.py` with Python and SymPy. The script uses exact symbolic arithmetic and prints `VERIFY_OK` on success.

It verifies the compact identity \(F=(a^2+b^2+pq)^2-4(a^2b^2+pq)\), the factorization of all four first derivatives, and containment of all ten reduced line components in the Jacobian zero set. It also verifies a Hessian \(3\times3\) minor
\[
-128t^2(t-1)^2(t+1)^2
\]
on a main line and a minor \(-512t^2\) on an isotropic line, proving rank three away from the five special points.

For the origin it checks the exact identity
\[
F=(a^2-b^2)^2-pq(4-2(a^2+b^2)-pq),
\]
whose unit factor yields the completed local form \(PQ-u^2v^2\). The script differentiates this normal form, obtaining singular ideal \((P,Q,uv^2,u^2v)\), and verifies by exact Gröbner reduction that \(uv\) survives modulo \((u^2v,uv^2)\) while \(u(uv)\), \(v(uv)\), and \((uv)^2\) vanish. Thus the reduced radical is \((P,Q,uv)\) and the nilradical quotient has \(\mathbb C\)-length one.

For a triple-branch point it checks
\[
F=u^2((v+2)^2+pq)+pq(v(v+4)+pq),
\]
where the first coefficient is a unit and \(v(v+4)+pq\) is a formal coordinate, yielding \(U^2+Vpq\). Its differentiated singular ideal is \((U,pq,Vq,Vp)\), a squarefree monomial ideal.

The script does not establish a literature-negative claim. Originality rests on primary-source inspection and targeted searches. Global exhaustiveness of the reduced singular-locus list is proved algebraically in `RESULT.md`, not inferred from finite sampling.
