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

For
\[
q\in\mathbb R,
\]
the exact power-weight test is
\[
y^q\in\mathcal B_2
\quad\Longleftrightarrow\quad
|q|<\alpha+1.
\]
This follows directly from the integrability of
\[
y^{\alpha+q}
\quad\text{and}\quad
y^{\alpha-q}
\]
on
\[
(0,L).
\]

After translating and dilating the pole, the symbol may be taken as
\[
b(z)=(z+i)^{-r}.
\]
For a Carleson box of length
\[
L,
\]
the denominator of the weighted oscillation quotient for
\[
\nu=y^s
\]
is comparable to
\[
L^{\alpha+s+2}.
\]

On boxes short compared with their distance scale
\[
R
\]
from the pole,
\[
|b'(z)|
\lesssim
R^{-r-1}
\]
and therefore
\[
\mathcal O_s(I)
\lesssim
L^{1-s}R^{-r-1}.
\]
This is uniformly bounded when
\[
s\le1
\quad\text{and}\quad
r+s\ge0.
\]

On the complementary boxes,
\[
\int_{Q_I}|b|\,dA_\alpha
\lesssim
\begin{cases}
L^{\alpha+2-r},&r<\alpha+2,\\
\log(2+L),&r=\alpha+2,\\
1,&r>\alpha+2.
\end{cases}
\]
After division by the denominator, the same conditions give uniform boundedness.

For necessity at small scale, use
\[
I_L=[0,L]
\]
and
\[
L\downarrow0.
\]
The nonzero derivative of
\[
(z+i)^{-r}
\]
at the origin gives
\[
\mathcal O_s(I_L)
\sim
cL^{1-s}
\]
with
\[
c>0.
\]
Thus bounded mean oscillation forces
\[
s\le1,
\]
and vanishing mean oscillation forces
\[
s<1.
\]

For necessity at infinity, use
\[
I_L=[L,2L]
\]
and
\[
L\to\infty.
\]
Scaling by
\[
z=Lw
\]
gives the nonconstant limiting profile
\[
w^{-r},
\]
hence
\[
\mathcal O_s(I_L)
\sim
c'L^{-r-s}
\]
with
\[
c'>0.
\]
Thus bounded mean oscillation forces
\[
s\ge-r,
\]
and vanishing mean oscillation forces
\[
s>-r.
\]

Therefore
\[
b\in\operatorname{BMOA}_{y^s}
\quad\Longleftrightarrow\quad
-r\le s\le1,
\]
and
\[
b\in\operatorname{VMOA}_{y^s}
\quad\Longleftrightarrow\quad
-r<s<1.
\]

The cited analytic-symbol Bergman commutator theorems then give the operator conclusions. No numerical experiment, truncated search, or finite enumeration is used as proof.
