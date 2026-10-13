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

The source proves
\[
K_{C_n}\longleftrightarrow\mathsf T(n),
\]
where \(\mathsf T(n)\) is phase choice for arbitrary disjoint unions of directed \(n\)-cycles.

For \(d\mid n\), expand each \(d\)-cycle by a finite second coordinate. An \(n\)-phase has a unique zero, whose old coordinate gives a \(d\)-phase. Hence
\[
K_{C_n}\Longrightarrow K_{C_d}.
\]

For \(a,b\ge2\), quotient each \(ab\)-cycle by the orbits of its \(b\)-step successor. The quotient is a \(b\)-cycle. A \(b\)-phase selects one orbit, which is an \(a\)-cycle under the \(b\)-step successor. An \(a\)-phase then chooses an origin of the original \(ab\)-cycle. Hence
\[
K_{C_a}\wedge K_{C_b}\Longrightarrow K_{C_{ab}}.
\]

Prime-factor induction gives
\[
K_{C_n}\longleftrightarrow\bigwedge_{p\mid n}K_{C_p}.
\]

The source's prime separation result supplies the reverse nonimplications, and its Theorem 42 supplies
\[
\operatorname{AC}(N)\longleftrightarrow\bigwedge_{2\le i\le N}K_{C_i}.
\]
Substituting the prime-support classification gives the prime-only basis.

## Limits

The positive classification is a theorem of \(\mathsf{ZF}\).

The exact negative implication criterion uses the source's consistency-dependent separation.

No statement is made about arbitrary finite digraphs or arbitrary CSP templates.
