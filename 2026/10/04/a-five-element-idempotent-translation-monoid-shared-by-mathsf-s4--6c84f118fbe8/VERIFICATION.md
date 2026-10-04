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

The proof reduces the full table to two semantic identities.

For a finite reflexive-transitive frame, the published operator
\[
\gamma(p)=\Diamond\Box\Diamond p
\]
is inverse image along the relation \(R'\) that keeps exactly edges whose target is maximal. In \(\mathsf{Grz}\), \(\Diamond\Box p\) is equivalent to \(\gamma(p)\).

The first critical check is that evaluating \(\gamma\) on \((W,R')\) again gives the ordinary diamond for \(R'\). The second is that evaluating \(\gamma\) after adding the identity relation, corresponding to \(p\vee g\), still gives that same \(R'\)-diamond. These prove
\[
g\star g=g,\qquad h\star g=g.
\]
Every other entry follows from preservation of \(p,\bot,\vee\), from \(e=\Diamond p\) being the identity translation, and from \(h=p\vee g\).

The bundled `verify.py` independently enumerates all reflexive-transitive relations on up to four labelled points and all valuations of \(p\). For \(\mathsf{Grz}\) it restricts to antisymmetric reflexive-transitive frames. It reconstructs translation syntax, evaluates every one of the twenty-five products, and checks the displayed common table. It prints `VERIFY_OK`.

## Limits

The finite checker corroborates rather than proves the unbounded result. The proof uses finite completeness. No claim is made for translations with parameters or for complete additivity on arbitrary infinite \(\mathsf{S4}\)-frames.
