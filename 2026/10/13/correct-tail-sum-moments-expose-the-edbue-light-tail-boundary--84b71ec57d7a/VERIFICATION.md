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
Let
\[
\lambda=-\log\theta,
\qquad
u_k=\frac{\theta^k}{1+\lambda k},
\qquad
G_k=(1-u_k)^\alpha.
\]
Then
\[
p_n=G_{n+1}-G_n
\]
and
\[
\Pr(X\ge k)=1-G_k.
\]

The source's asymptotic gives
\[
p_n
\sim
\frac{\alpha(1-\theta)}{\lambda}
\frac{\theta^n}{n}.
\]
Also,
\[
1-G_k
\sim
\frac{\alpha}{\lambda}
\frac{\theta^k}{k}.
\]
Hence the MGF series has the same convergence boundary as
\[
\sum_{n\ge1}\frac{(\theta e^t)^n}{n},
\]
namely
\[
t<-\log\theta.
\]

For positive integer \(r\),
\[
X^r
=
\sum_{k=1}^{X}
\{k^r-(k-1)^r\},
\]
so Tonelli's theorem gives the corrected raw-moment formula
\[
\mathbb E[X^r]
=
\sum_{k\ge1}
\{k^r-(k-1)^r\}(1-G_k).
\]

The source's Eq. (6.4) instead has summand
\[
\{(k-1)^r-k^r\}G_k
\sim-rk^{r-1},
\]
so it diverges.

The bundled checker evaluates exact \(G_k\) and PMF values, verifies both tail constants, compares direct and tail-sum moments, and contrasts MGF partial sums below and at the convergence boundary. Those computations are consistency checks only.
