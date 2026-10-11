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

The proof was reconstructed from the exact scalar recurrences in the primary source. In the fixed-diagonal sector, the off-diagonal coordinate obeys
\[
t_{k+1}-t_*=
\left(1-\frac{c_0}{c}\right)(t_k-t_*),
\]
so every nonfixed point in that sector has exact root rate \(|1-c_0/c|\).

For a normalized diagonal perturbation, the source gives
\[
p_k=p_0^{(1-1/c)^k}.
\]
For \(p_0\ne1\) and \(1-1/c\ne0\), Taylor expansion of the exponential at zero gives a nonzero leading term proportional to \((1-1/c)^k\), proving the lower bound \(|1-1/c|\). The source's arbitrary-initial theorem supplies the matching maximum upper bound.

The scalar minimax problem was checked by setting \(s=1/c\). On the admissible interval, the maximum of \(|1-s|\) and \(|1-c_0s|\) has its unique equioscillation point at \(s=2/(1+c_0)\), giving the stated parameter and rate. The special case \(c_0=1\) gives rate \(0\) at \(c=1\) directly from the source upper bound.

No finite computation is used as proof. The verification does not address transient constants, variable relaxation schedules, or dimensions above two.
