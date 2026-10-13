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

The proof is algebraic and local. The order-four action has no nontrivial stabilizers outside the two four-point coordinate-line sets. At those points its tangent weights are respectively \((-1,-1)\) and \((1,1)\) modulo \(4\), so every quotient singularity is \(\frac14(1,1)\).

On \(Y W\ne0\), the function-field computation is
\[
t^4(r^4+1)+F_4(z,1)=0,
\]
with \(r,z\) invariant and \(t\mapsto it\). Thus the quotient field is \(\mathbb C(r,z)\). The standard scalar cyclic-quotient resolution extends the pair-ratio map, and the proof identifies its positive-dimensional fibers exactly with the sixteen invariant lines.

The bundled `verify.py` checks the complete intersection-lattice calculation on \(\operatorname{Bl}_{16}(\mathbf P^1\times\mathbf P^1)\): eight boundary curves of square \(-4\), sixteen grid exceptional curves of square \(-1\), the claimed incidences, \(D=-2K\), \(K^2=-8\), \(\rho=18\), and \(e=20\). The emptiness of \(|-K|\) is proved symbolically by the degree-two restriction argument on each of four vertical fibers, not by sampling.

No claim is made about quotient models outside the stated smooth two-outer-Galois-point family.
