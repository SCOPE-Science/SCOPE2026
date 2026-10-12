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

The proof is analytic. The critical chain is:

1. Set \(n=m+1\) and identify
\[
I_u(r,n-r+1)=\Pr\{\operatorname{Bin}(n,u)\ge r\}.
\]

2. Use the tail-sum identity to obtain
\[
C_m(u,v)=\frac1n\mathbb E[\min(J_u,J_v)].
\]

3. For \(u\le v\),
\[
M(u,v)-C_m(u,v)=\frac1n\mathbb E[(J_u-J_v)_+],
\]
which is nonincreasing in \(v\). Symmetry reduces the global maximum to the diagonal.

4. On the diagonal,
\[
M(p,p)-C_m(p,p)=\frac{\mathbb E|J-K|}{2n}.
\]
The difference is a lazy symmetric random walk whose activation probability is \(2p(1-p)\). Conditional expected absolute displacement is nondecreasing in the number of active steps, so the maximum occurs at \(p=1/2\).

5. At \(p=1/2\),
\[
J-K\stackrel d=B_{2n}-n,
\]
and direct telescoping gives
\[
\mathbb E|B_{2n}-n|=n\binom{2n}{n}/4^n.
\]

The standalone script `verify.py` checks the center identity and the telescoping identity in exact arithmetic through \(n=120\), and performs deterministic grid checks for \(n\le8\). It also checks the central-binomial asymptotic numerically at a large \(n\).

Expected successful terminal line:
`VERIFY_OK exact_n=120 grid_n=8 asymptotic_ratio=0.999987500101`.

Finite verification does not establish the theorem; it only replays consequences of the analytic proof.
