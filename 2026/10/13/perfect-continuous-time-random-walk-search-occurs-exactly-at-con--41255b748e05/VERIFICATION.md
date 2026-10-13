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
# Verification of the perfect-search cone classification

The unrestricted theorem is proved in `RESULT.md`; numerical evidence is not used to infer global necessity. The identities requiring exact checking are the normalized transition-return moment
\[
\|P e_w\|_d^2=\frac1{d_w}\sum_{v\sim w}\frac1{d_v},
\]
the equality in the chain
\[
\frac1{d_w}\sum_{v\sim w}\frac1{d_v}\ge\frac{d_w}{\sum_{v\sim w}d_v}\ge\frac{d_w}{2m-d_w},
\]
and the cone reduced-Hamiltonian square
\[
\left[\frac1{k+2}\begin{pmatrix}-1&-\sqrt{k+1}\\-\sqrt{k+1}&1\end{pmatrix}\right]^2=\frac{I}{k+2}.
\]

Run `python3 verify.py` with Python's standard library. The code iterates every connected labeled simple graph of orders two through six; it computes the exact rational equality defect for every marked vertex, proves a matching empirical criterion on this **finite** test set, and checks the two-state identities for base degrees zero through twelve. Its expected output is `VERIFY_OK connected_labeled_graphs=27475 orders=2..6 cone_blocks=13 exact_fractions=true`.

The finite census is not exhaustive over all graph orders, and the trigonometric sample is not a substitute for a universal theorem. Global sufficiency/necessity follows from the analytic moment and Cauchy–Schwarz argument. This verification does not provide independent scientific validation or third-party replication.
