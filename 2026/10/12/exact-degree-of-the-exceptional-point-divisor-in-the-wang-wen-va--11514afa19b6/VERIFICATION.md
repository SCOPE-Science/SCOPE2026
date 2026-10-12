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

The claim is proved symbolically; no finite computation or numerical experiment is needed.

The source-side checks are:

1. The initiating paper assumes \(V^G=0\) and \(\rho|_{Z(G)}=1\), defines the associated bundle \(E_\rho(P)\), and proves that a general pair \((P,x)\) satisfies
   \[
   H^0(C,E_\rho(P)((g-1)x))
   =
   H^1(C,E_\rho(P)((g-1)x))
   =
   0.
   \]
2. The same paper explicitly interprets this as proper finite intersection, for general \(P\), between the curve
   \[
   x\mapsto\mathcal O_C((g-1)x)
   \]
   and the generalized theta divisor.
3. The determinant character of \(\rho\) is trivial under the source hypotheses, hence \(E_\rho(P)\) has degree \(0\) and trivial determinant.
4. Classical generalized-theta theory gives class \(r\Theta\) for the proper theta divisor of a rank-\(r\) degree-zero bundle in this setting.
5. After identifying \(\operatorname{Pic}^{g-1}(C)\) with \(J(C)\), the curve map is \([g-1]\circ j\). The principal polarization satisfies
   \[
   [g-1]^*\Theta\equiv(g-1)^2\Theta.
   \]
6. Poincaré's formula
   \[
   [j(C)]=\frac{\Theta^{g-1}}{(g-1)!}
   \]
   and
   \[
   \int_{J(C)}\frac{\Theta^g}{g!}=1
   \]
   give
   \[
   \deg j^*\Theta=g.
   \]
   Therefore
   \[
   \deg\alpha^*\Theta_E=r\,g\,(g-1)^2.
   \]

Riemann--Roch gives \(\chi(E_\rho(P)((g-1)x))=0\), so the nonvanishing loci for \(H^0\) and \(H^1\) coincide.

The proof establishes the total scheme-theoretic multiplicity only. It does not establish reducedness of the exceptional-point divisor.
