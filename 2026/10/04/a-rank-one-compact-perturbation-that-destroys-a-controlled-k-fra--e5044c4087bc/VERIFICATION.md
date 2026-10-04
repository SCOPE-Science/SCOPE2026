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

The counterexample can be replayed entirely from the displayed formulas.

Take \(H=\ell^2(\mathbb N)\), \(C=K=I\), \(F=(e_n)\), and \(G=(e_2,e_2,e_3,e_4,\ldots)\). For each coefficient vector \(c=(c_n)\),
\[
(T_F-T_G)c=c_1(e_1-e_2),
\]
so the difference has rank one. For the test vector \(e_1\),
\[
\sum_{n\ge1}|\langle e_1,g_n\rangle|^2=0,
\]
so \(G\) cannot have a positive lower frame bound.

For the restricted quantitative repair, if \(F\) has lower frame bound \(A\) and \(E=T_F-T_G\), then
\[
\|T_G^*f\|\ge(\sqrt A-\|E\|)\|f\|.
\]
Thus \(\|E\|<\sqrt A\) gives lower frame bound \((\sqrt A-\|E\|)^2\). This verification uses no numerical approximation.

Limits: no claim is made that this norm condition is necessary or optimal in general Hilbert \(C^*\)-modules. The literature comparison cannot exclude an unindexed prior observation.
