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

For real coefficients the primary theorem gives
\[
p_-(\mathcal H)<q
\quad\Longleftrightarrow\quad
\omega\in RH_{q'/2}.
\]

For
\[
-n<\beta<0,
\]
the power weight satisfies
\[
|x|^\beta\in RH_s
\quad\Longleftrightarrow\quad
\beta s>-n.
\]
With
\[
s=\frac{q'}2,
\]
this is exactly
\[
q>\frac{2n}{2n+\beta}.
\]

The same threshold is independently obtained from
\[
\mu_{q'}\text{ locally finite}
\quad\Longleftrightarrow\quad
\frac{\beta q'}2>-n.
\]
Thus
\[
p_-(\mathcal H)=\frac{2n}{2n+\beta}
\]
for negative \(\beta\).

For nonnegative \(\beta<n\), the source records
\[
|x|^\beta\in RH_\infty,
\]
and therefore
\[
p_-(\mathcal H)=1.
\]

For negative \(\beta\), the conjugate critical exponent is
\[
p_\beta'=-\frac{2n}{\beta}.
\]
The source duality corollary therefore gives the reverse inequality for
\[
2\le p<-\frac{2n}{\beta}.
\]

Finally,
\[
\frac{2n}{2n+\beta}
=
\frac{2(n+2)}{n+4}
\]
if and only if
\[
\beta=-\frac{n^2}{n+2}.
\]
At this value,
\[
\beta\left(1+\frac2n\right)=-n,
\]
so the endpoint reverse-Hölder power is not locally integrable.

The packaged symbolic checker replays these algebraic equivalences. The reverse-Hölder membership proof and the operator-theoretic implications are contained in RESULT.md.
