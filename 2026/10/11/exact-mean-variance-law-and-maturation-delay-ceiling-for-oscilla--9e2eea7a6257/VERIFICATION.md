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

The bundled `verify.py` uses SymPy to replay the algebra in the proof from the printed interaction term
\[
G(n,p)=\frac{(1+\alpha p)n}{1+h_1(1+\alpha p)n}.
\]
It verifies that the prey loss equals \(G(n,p)p\), that combining the integrated predator and prey balances gives
\[
\bar p=\sigma e^{-\beta\tau}\left(\bar n-\frac{\overline{n^2}}{\kappa}\right),
\]
and that rewriting \(\overline{n^2}=\bar n^2+\operatorname{Var}(n)\) produces the displayed variance defect.

It also verifies symbolically that the fixed-prey loss function
\[
\Phi(p)=\frac{p(1+\alpha p)}{1+h_1n_0(1+\alpha p)}
\]
has derivative numerator
\[
(1+h_1n_0)(1+2\alpha p)+h_1n_0\alpha^2p^2,
\]
which is positive for the stated positive parameters, and that
\[
\frac1{h_1}-G(n,p)=\frac1{h_1[1+h_1(1+\alpha p)n]}>0.
\]
The stored checker output is `VERIFY_OK`.

The delay-shift step is analytic: for every \(T\)-periodic integrable function \(q\),
\[
\int_0^T q(t-\tau)\,dt=\int_0^T q(t)\,dt
\]
for arbitrary real \(\tau\). No finite numerical experiment is used to infer an infinite-time conclusion.

The verification establishes only the stated necessary conditions for strictly positive nonconstant periodic solutions. It does not establish that such a cycle exists, nor its stability, uniqueness, basin, Hopf direction, or any claim about nonperiodic recurrent dynamics.
