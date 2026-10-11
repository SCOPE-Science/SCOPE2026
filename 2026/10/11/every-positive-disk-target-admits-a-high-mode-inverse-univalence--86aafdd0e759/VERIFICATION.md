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

Fix
\[
n\ge2.
\]
For
\[
f_{a,n}(z)=z+az^n
\]
the transformed function is
\[
F(z)=z+\Omega_naz^n.
\]
Writing
\[
c=\Omega_na,
\]
one obtains exactly
\[
\frac{zF'(z)}{F(z)}-1
=
\frac{(n-1)cz^{n-1}}
{1+cz^{n-1}}.
\]

If
\[
t=|c|>1,
\]
then \(F\) has a nonzero zero in the unit disk, so the defining logarithmic derivative is not analytic there. If
\[
t=1,
\]
its modulus is unbounded toward the corresponding boundary direction. Thus membership requires
\[
t<1.
\]
For such \(t\),
\[
w=cz^{n-1}
\]
ranges over
\[
|w|<t,
\]
and the exact supremum is
\[
\sup_{|w|<t}
\left|
\frac{(n-1)w}{1+w}
\right|
=
\frac{(n-1)t}{1-t}.
\]
Therefore membership in the disk target is equivalent to
\[
t
\le
\frac{\delta}{n-1+\delta},
\]
or
\[
|a|
\le
\frac{\delta}
{\Omega_n(n-1+\delta)}.
\]

For the original function,
\[
f'_{a,n}(z)=1+naz^{n-1}.
\]
An interior critical point exists exactly when
\[
|a|>\frac1n.
\]
The logarithmic derivative is
\[
\frac{zf'_{a,n}(z)}
{f_{a,n}(z)}
=
\frac{1+nu}{1+u},
\qquad
u=az^{n-1},
\]
and
\[
\operatorname{Re}
\frac{1+nu}{1+u}
=
\frac{
1+n|u|^2+(n+1)\operatorname{Re}u
}{
|1+u|^2
}.
\]
At fixed
\[
|u|,
\]
the numerator is minimized on the negative real ray. At the boundary radius
\[
|a|,
\]
it becomes
\[
(1-|a|)(1-n|a|).
\]
Thus starlikeness holds exactly when
\[
|a|\le1/n.
\]

Comparing the exact membership and starlikeness thresholds gives
\[
\delta
\le
\delta_n
=
\frac{\Omega_n(n-1)}
{n-\Omega_n}
\]
as the necessary-and-sufficient condition that every member of the \(n\)-th monomial slice retain original starlikeness.

Finally,
\[
\frac{\delta_n}{\Omega_n}
=
\frac{n-1}{n-\Omega_n}
\longrightarrow1,
\]
while
\[
\Omega_n
\sim
(n-1)^{-(\lambda/2+\mu)}.
\]
Hence
\[
\delta_n\to0.
\]
For every fixed positive
\[
\delta,
\]
a sufficiently high mode satisfies
\[
\delta>\delta_n,
\]
and then the interval
\[
1/n<|a|\le
\delta/[\Omega_n(n-1+\delta)]
\]
is nonempty. Every coefficient chosen from it gives a class member with an interior critical point.

All inequalities are exact. No finite experiment is used to infer an infinite-dimensional or asymptotic conclusion.
