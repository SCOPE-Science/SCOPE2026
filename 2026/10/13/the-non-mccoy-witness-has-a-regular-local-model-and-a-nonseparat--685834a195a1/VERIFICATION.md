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

The finding is verified by a direct symbolic reconstruction.

1. Zariski density of \(X\) and the infinite fibers \(\{p\}\times\mathbb N\) imply \(\iota(A)\cap D=0\).

2. Because every \(p\in X\) is nonzero, each coordinate idempotent \(\delta_{(p,j)}\) is a multiple in \(R\) of at least one of \(\iota(x),\iota(y),\iota(z)\). Hence \(D\subset I\).

3. Every finitely supported function \(d\) satisfies \(d=de_F\) for the finite-support characteristic idempotent \(e_F\) of its support. Thus \(D^2=D\).

4. Therefore \(I=D+\iota(\mathfrak m)\) and \(I^n=D+\iota(\mathfrak m^n)\) for every \(n\ge1\).

5. The projection \(\iota(f)+d\mapsto f\) has kernel \(D\), giving \(R/I^n\cong A/\mathfrak m^n\). Since \(\bigcap_{n\ge1}\mathfrak m^n=0\) in the polynomial ring, \(\bigcap_{n\ge1}I^n=D\).

6. Successive quotients identify \(\operatorname{gr}_I(R)\) with \(\operatorname{gr}_{\mathfrak m}(A)\cong k[x,y,z]\), and inverse limits give \(\widehat R^{\,I}\cong k[[x,y,z]]\) with kernel \(D\).

7. For \(d\in D\), the element \(1-e_{\operatorname{supp}(d)}\notin I\) kills \(d\), so \(D_I=0\). Localizing \(R/D\cong A\) at \(I/D\cong\mathfrak m\) gives \(R_I\cong A_{\mathfrak m}\).

No computational certificate is needed for these identities. The source's global statements \(I\subseteq Z(R)\) and \(\operatorname{Ann}_R(I)=0\) were checked in the primary full text. The result does not claim that other maximal ideals have the same filtration.
