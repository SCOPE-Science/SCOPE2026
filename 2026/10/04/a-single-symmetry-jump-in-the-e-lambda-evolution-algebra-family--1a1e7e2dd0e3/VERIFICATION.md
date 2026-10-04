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

The verification is symbolic and uses the basis
\[
u=e_1+e_3,\qquad v=e_2+e_3,\qquad w=e_3.
\]
The multiplication table is
\[
u^2=0,\quad uv=u,\quad v^2=-u+\lambda v,\quad uw=u,\quad vw=u,\quad w^2=u.
\]

Any automorphism preserves \(E_\lambda^2=\operatorname{span}_K\{u,v\}\). Its square-zero locus is \(Ku\), so an automorphism must have
\[
\phi(u)=\alpha u,\qquad \phi(v)=\beta u+v.
\]
The relation \(v^2=-u+\lambda v\) gives
\[
\alpha=1+(\lambda-2)\beta.
\]
Writing \(\phi(w)=pu+qv+cw\), the relations \(uw=u\) and \(vw=u\) give
\[
q=0,\qquad c=1,\qquad p=\alpha-\beta-1.
\]
The relation \(w^2=u\) then gives \(2p+1=\alpha\), hence
\[
(4-\lambda)\beta=0.
\]

Therefore \(\lambda\ne4\) forces the identity. For \(\lambda=4\),
\[
\phi_\beta(u)=(1+2\beta)u,\qquad
\phi_\beta(v)=v+\beta u,\qquad
\phi_\beta(w)=w+\beta u.
\]
Its determinant is \(1+2\beta\), and direct substitution preserves all six basis products. Composition satisfies
\[
1+2(\beta+\gamma+2\beta\gamma)=(1+2\beta)(1+2\gamma),
\]
which identifies the automorphism group with \(K^\times\).

No finite experiment is used as a proof, and no claim is made about automorphism group schemes or semilinear automorphisms.
