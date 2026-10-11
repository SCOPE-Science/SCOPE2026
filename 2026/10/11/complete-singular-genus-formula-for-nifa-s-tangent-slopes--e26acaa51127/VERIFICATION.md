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

The proof was checked at the level of the exact source statements and its integer boundary cases.

For the lower bound, Nifa's circle-action construction gives the images of \(\mu\) and the central trefoil element \(h\); substituting \(\lambda=h\mu^{-6}\) shows that \(\lambda^m\) is conjugate to a rigid translation of size \(|m|(N-1)/N\). The strict Eisenbud--Hirsch--Neumann inequality then gives the least possible number of commutators.

For the upper bound, write \(|m|=Na+r\). The published case \(r=0\) is Nifa's Theorem 6.5. For \(r>0\), the boundary monodromy is chosen with cycle type \(N^a r^1\). Its parity exponent is \(A=a(N-1)+r-1\), so the minimal parity correction \(\varepsilon\in\{0,1\}\) gives a connected branched cover with
\[
2-2g-(a+1)=-(Na+r)-\varepsilon.
\]
Hence
\[
g=1+\left\lceil\frac{A}{2}\right\rceil,
\]
which agrees with the circle-action lower bound. Centrality of \(\lambda^N\) combines the degree-\(N\) boundary components with the residual degree-\(r\) component to give \(\lambda^{Na+r}\).

The low degrees \(D=2,3,4\) satisfy the needed elementary fact that every even permutation in \(S_D\) is a product of two \(D\)-cycles; the degree-one longitude is already one commutator in the source.

The bundled standard-library checker verifies the residue formula, compact floor form, strict translation threshold, the central-power specialization, and the covering-genus arithmetic for representative ranges. Its output is recorded in the result package. Finite checking is not used as proof of the universal group-theoretic or covering statements.

No independent audit has been performed.
