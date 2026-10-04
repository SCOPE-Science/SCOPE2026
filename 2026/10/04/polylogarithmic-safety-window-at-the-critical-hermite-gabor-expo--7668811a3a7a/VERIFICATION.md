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

The verification is analytic and tracks the primary source's displayed inequalities directly.

Set
\[
\eta_n=\beta\frac{\log\log n}{\log n},
\qquad
\delta_n=\eta_n/2,
\qquad
p_n=1-\eta_n/4,
\qquad
t_n=2/3-\eta_n/4.
\]
Then the source's parameter constraint is satisfied with margin
\[
p_n+t_n-\left(\frac53-2(\eta_n-\delta_n)\right)
=
\frac{\eta_n}{2}>0.
\]

The principal exponents in the source's finite-layer estimate become
\[
-\eta_n/8,\quad
-\eta_n/4,\quad
-1/6-\eta_n/2,\quad
-\eta_n/2,
\]
and the delicate-layer exponents become
\[
-1/6-9\eta_n/8,\quad
-\eta_n/2,\quad
-1/6-\eta_n/2
\]
with one additional factor \(\log n\) in the last term. Therefore the whole non-tail contribution is
\[
O_\beta((\log n)^{-\beta/8}).
\]

For the tail, the source parameter is
\[
\varepsilon_n=2/3-\eta_n.
\]
Its explicit final tail estimate applies once
\[
\pi n^{-\varepsilon_n}<0.1
\]
and
\[
\exp\!\left(-\frac{\pi}{4}n^{1-\varepsilon_n}\right)<1/2.
\]
These hold because
\[
n^{-\varepsilon_n}=n^{-2/3}(\log n)^\beta\to0
\]
and
\[
n^{1-\varepsilon_n}=n^{1/3}(\log n)^\beta\to\infty.
\]

Finally, Janssen's representation and the unitary norm of every time-frequency shift give
\[
\|ab\,S_{n,a,b}-I\|
\le
\sum_{(k,l)\ne(0,0)}
\left|V_{h_n}h_n\left(\frac{k}{b},\frac{l}{a}\right)\right|.
\]
This proves the stated operator-norm and frame-bound estimates.

No finite computation, numerical fit, or truncation is used as evidence.
