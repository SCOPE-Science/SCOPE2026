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

The proof is analytic and has four critical steps.

1. For a strictly positive \(T\)-periodic solution, integrate the third delay equation over one full period. Periodicity gives
\[
\int_0^T\frac{x_2(t-\tau_2)x_3(t-\tau_2)}{v+p x_2(t-\tau_2)+q x_3(t-\tau_2)}\,dt
=
\int_0^T\frac{x_2(t)x_3(t)}{v+p x_2(t)+q x_3(t)}\,dt.
\]
2. Normalize by \(\int_0^T x_3(t)\,dt>0\). This creates a probability weight proportional to top-predator density and gives the exact weighted stationary identity used in the proof.
3. The comparison
\[
\frac{u}{v+pu+qz}<\frac{u}{v+pu}
\]
is strict for \(u,z,q>0\), and \(u/(v+pu)\) is strictly concave because its second derivative is \(-2pv/(v+pu)^3\). Jensen therefore yields the strict threshold. The algebraic difference is
\[
\frac{M}{v+pM}-\frac e\eta
=
\frac{(\eta-pe)M-ve}{\eta(v+pM)}.
\]
4. Only when \(\tau_2=0\) does division by the current positive \(x_3(t)\) directly give a periodic logarithmic derivative and hence the ordinary-time mean identity. No such unweighted claim is made for general positive \(\tau_2\).

The supplementary `verify.py` uses exact rational arithmetic to replay the threshold rearrangement and to check that the source's printed numerical parameter values give
\[
\frac{ve}{\eta-pe}=\frac{155}{493}.
\]
It is a consistency check, not an infinite-dimensional proof of periodic-orbit existence.
