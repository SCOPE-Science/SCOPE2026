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

The general proof was checked directly from multiplicative orders. If \(u\) is primitive in \(\mathbb F_{p^{ln}}\), then \(\operatorname{ord}(u)=p^{ln}-1\). A relation \(u^{p^d}=u\) with \(0<d<ln\) would force \(p^{ln}-1\mid p^d-1\), which is impossible. Hence the \(p\)-Frobenius orbit has exactly \(ln\) elements, so a basis consisting of all of them forces \(D(1,b)\) to equal the ambient field.

The exact finite example was replayed from the accompanying `verify.py`. It constructs \(\mathbb F_{64}\) as \(\mathbb F_2[g]/(g^6+g+1)\), verifies that \(g\) has multiplicative order \(63\), verifies \(b=g^{34}\) and \(1+b=g^{31}\) lie in \(gH\) for \(H=\langle g^3\rangle\), evaluates the Dickson multiplication for every field element, and obtains exactly four solutions. Those solutions are independently identified as the roots of \(d^4=d\), hence as \(\mathbb F_4\). Every nonzero solution has order dividing \(3\), so none is primitive in \(\mathbb F_{64}\).

The source-side hypotheses were also checked: \((4,3)\) is a Dickson pair, \(n>2\), \(b\neq0\), \(1+b\neq0\), and the coset parameters are \(s=t=1\), so \(\mu=1\) and \(\mathbb F_{p^{l\mu}}=\mathbb F_4\).

Limits: this verifies the claim only under Definition 25 exactly as printed. The plausible repaired definition, with primitivity relative to \(\mathbb F_{p^{l\mu}}\), has a different meaning and yields the equivalence stated in the result. No independent audit has been performed.
