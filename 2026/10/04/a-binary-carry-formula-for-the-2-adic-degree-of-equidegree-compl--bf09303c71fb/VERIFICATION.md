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
The source formula used is the equidegree specialization of the singular-complete-intersection discriminant degree:
\[
\deg_i\Delta=\binom{N+1}{c}d^{c-1}(d-1)^{N-c+1},
\]
together with \(\deg\Delta=\sum_i\deg_i\Delta\).

The proof then uses only exact integer identities. In particular,
\[
c\binom{N+1}{c}=(N+1)\binom{N}{c-1}
\]
and Legendre's formula identify \(\nu_2\binom{N}{c-1}\) with the number of binary carries in adding \(c-1\) and \(N-c+1\).

The bundled checker verifies 204120 triples with \(1\le N\le80\), \(1\le c\le N\), and \(2\le d\le64\). For every triple it compares the direct integer valuation of the closed degree formula with the carry formula, verifies the odd-degree classification, and checks the universal divisibility by \(4\) for \(c\ge2\). The sharp witness \((N,c,d)=(2,2,2)\) is checked separately.

The finite replay is not used as an infinite proof. The symbolic derivation covers all stated parameters.
