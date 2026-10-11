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

The proof has three symbolic checkpoints.

1. For odd \(p\), the covering-kernel order \(4\) is a unit in \(\mathbf F_p\), and the source exterior-pair criterion applies to both quotients.

2. The group algebras satisfy
\[
\mathbf F_p[C_4]\cong\mathbf F_p[t]/(t^4-1).
\]
The factor \(t^2+1\) splits exactly for \(p\equiv1\pmod4\). Thus \(\mathbf F_p[C_4]\cong\mathbf F_p^4\) in that case and \(\mathbf F_p[C_4]\cong\mathbf F_p\times\mathbf F_p\times\mathbf F_{p^2}\) for \(p\equiv3\pmod4\). In contrast, \(\mathbf F_p[C_2\times C_2]\cong\mathbf F_p^4\) for every odd \(p\). Corollary 9.3 of arXiv:2610.04164v1 then yields the BV conclusion.

3. A common simply connected semisimple cover containing both a \(C_4\) and a \(C_2\times C_2\) central subgroup has rank at least \(4\): rank \(3\) is the first rank supporting an order-\(4\) central element, realized by \(\mathrm{SU}(4)\), but its centre is cyclic; one additional even-centred simple factor has rank at least \(1\). The product \(\mathrm{SU}(4)\times\mathrm{SU}(2)\) attains rank \(4\).

No finite experiment is used as an infinite proof. Characteristic \(2\) and minimality without the common-cover hypothesis remain outside the claim.
