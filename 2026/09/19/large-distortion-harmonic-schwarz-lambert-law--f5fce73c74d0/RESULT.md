# Lambert-W large-distortion law for the harmonic Schwarz extremal

## Result

Let \(H\) be a real Hilbert space with \(\dim H\ge 2\). For \(K\ge1\), let \(M_K\) be the sharp centered pointwise-distortion constant from Knežević--Mateljević: the supremum of \(L_F(0)\) over harmonic maps
\[
F:\mathbb D\to\mathbb B_H,\qquad F(0)=0,\qquad
0<\ell_F(0)\le L_F(0)\le K\ell_F(0).
\]
Their extremal family is parameterized by the unique \(\tau_K\in(0,1]\) satisfying
\[
\frac{\alpha(\tau_K)}{\beta(\tau_K)}=K,
\]
where, for \(k=\sqrt{1-\tau^2}\),
\[
\alpha(\tau)=\frac4\pi\,
\frac{\mathbf E(k)-\tau^2\mathbf K(k)}{1-\tau^2},
\qquad
\beta(\tau)=\frac{4\tau}{\pi}\,
\frac{\mathbf K(k)-\mathbf E(k)}{1-\tau^2},
\qquad
M_K=\alpha(\tau_K).
\]

Define
\[
Y_K=-W_{-1}\!\left(-\frac{e}{4K}\right),
\]
where \(W_{-1}\) is the lower real branch of Lambert's \(W\)-function. Then, as \(K\to\infty\),
\[
\boxed{\;
\tau_K=\frac{1}{K\,Y_K}
\left(1+O\!\left(\frac{1}{K^2Y_K}\right)\right).
\;}
\]
Equivalently,
\[
\tau_K\sim \frac{1}{K\log K},
\]
since
\[
Y_K=\log\frac{4K}{e}+\log\log\frac{4K}{e}+o(1).
\]

The sharp constant approaches its unrestricted limit at the rate
\[
\boxed{\;
\frac4\pi-M_K
=
\frac{2}{\pi K^2Y_K}
\left(
1-\frac{1}{2Y_K}
+O\!\left(\frac{1}{K^2Y_K}\right)
\right).
\;}
\]
In particular,
\[
\boxed{\;
\frac4\pi-M_K\sim\frac{2}{\pi K^2\log K}.
\;}
\]

There is also a sharp rate for degeneration of the extremal boundary data. Write
\[
\Phi_\tau(e^{it})
=
\frac{\cos t\,e_1+\tau\sin t\,e_2}
{\sqrt{\cos^2t+\tau^2\sin^2t}},
\qquad
\Psi(e^{it})=\operatorname{sgn}(\cos t)e_1,
\]
with normalized Lebesgue measure on \(\mathbb T\). Then the exact identity
\[
\boxed{\;
\|\Phi_\tau-\Psi\|_{L^2(\mathbb T,H)}^2
=
2-\frac4\pi\,
\frac{\arccos\tau}{\sqrt{1-\tau^2}}
\;}
\]
holds for \(0<\tau<1\). Consequently,
\[
\boxed{\;
\|\Phi_{\tau_K}-\Psi\|_2
=
\frac{2}{\sqrt{\pi K Y_K}}\,(1+o(1))
\sim
\frac{2}{\sqrt{\pi K\log K}}.
\;}
\]
For each fixed \(0<r<1\), Poisson extension therefore gives the local-uniform estimate
\[
\sup_{|z|\le r}
|F_{\tau_K}(z)-P[\Psi](z)|
\le
\sqrt{\frac{1+r^2}{1-r^2}}\,
\|\Phi_{\tau_K}-\Psi\|_2
=
O_r\!\left((K\log K)^{-1/2}\right).
\]

## Context

Knežević and Mateljević determine \(M_K\), prove uniqueness of \(\tau_K\), identify all extremals, and show
\[
M_K\uparrow\frac4\pi,\qquad \tau_K\downarrow0
\quad(K\to\infty).
\]
They also prove almost-everywhere and \(L^2\) convergence of \(\Phi_{\tau_K}\) to \(\Psi\). At the opposite endpoint they give the expansion
\[
\tau_K=1-2(K-1)+O((K-1)^2),\qquad
M_K=1+\frac12(K-1)+O((K-1)^2)
\quad(K\downarrow1).
\]
The formulas above quantify the previously qualitative large-\(K\) endpoint. The logarithm comes from the singular \(k\uparrow1\) behavior of the complete elliptic integral \(\mathbf K(k)\); its inversion naturally produces the \(W_{-1}\) branch.

## Proof

Set
\[
L=L(\tau)=\log\frac4\tau.
\]
The standard complementary-modulus expansions of the complete elliptic integrals give, as \(\tau\downarrow0\),
\[
\mathbf K(\sqrt{1-\tau^2})
=
L+\frac{\tau^2}{4}(L-1)+O(\tau^4L),
\]
\[
\mathbf E(\sqrt{1-\tau^2})
=
1+\frac{\tau^2}{2}\left(L-\frac12\right)+O(\tau^4L).
\]
Substitution into the exact formulas for \(\alpha,\beta\) yields
\[
\alpha(\tau)
=
\frac4\pi
\left[
1+\tau^2\left(\frac34-\frac L2\right)
+O(\tau^4L)
\right],
\]
and
\[
\beta(\tau)
=
\frac{4\tau}{\pi}
\left[
L-1+\tau^2\left(\frac{3L}{4}-1\right)
+O(\tau^4L)
\right].
\]
Hence
\[
\frac{\alpha(\tau)}{\beta(\tau)}
=
\frac{1}{\tau(L-1)}
\left(1+O(\tau^2L)\right).
\tag{1}
\]

Let
\[
f(\tau)=\tau\left(\log\frac4\tau-1\right).
\]
Equation (1) at \(\tau=\tau_K\) gives
\[
Kf(\tau_K)=1+O(\tau_K^2L(\tau_K)).
\tag{2}
\]
The exact solution of \(f(\tau)=1/K\) tending to zero is
\[
\tau_0=\frac1{KY_K},
\qquad
Y_K=-W_{-1}\!\left(-\frac e{4K}\right),
\]
because \(Y_Ke^{-Y_K}=e/(4K)\). Since \(f\) is regularly varying at zero with index one, (2) first gives \(\tau_K/\tau_0\to1\). On the interval between \(\tau_K\) and \(\tau_0\),
\[
f'(\tau)=\log\frac4\tau-2\asymp Y_K.
\]
Applying the mean-value theorem to (2) then improves the comparison to
\[
\frac{\tau_K}{\tau_0}
=
1+O\!\left(\frac1{K^2Y_K}\right),
\]
which proves the stated optimizer asymptotic.

For the sharp constant,
\[
\frac4\pi-\alpha(\tau)
=
\frac{2}{\pi}\tau^2
\left(L-\frac32\right)
+O(\tau^4L).
\tag{3}
\]
At \(\tau=\tau_K\),
\[
L(\tau_K)
=
Y_K+1+O\!\left(\frac1{K^2Y_K}\right),
\]
and substituting the preceding expansion for \(\tau_K\) into (3) gives
\[
\frac4\pi-M_K
=
\frac{2}{\pi K^2Y_K}
\left(
1-\frac1{2Y_K}
+O\!\left(\frac1{K^2Y_K}\right)
\right).
\]

It remains to compute the boundary rate. Since both \(\Phi_\tau\) and \(\Psi\) have norm one almost everywhere,
\[
\|\Phi_\tau-\Psi\|_2^2
=
2-2\int_{\mathbb T}
\frac{|\cos t|}
{\sqrt{\cos^2t+\tau^2\sin^2t}}\,dm.
\]
By symmetry and \(u=\sin t\),
\[
\int_{\mathbb T}
\frac{|\cos t|}
{\sqrt{\cos^2t+\tau^2\sin^2t}}\,dm
=
\frac2\pi
\frac{\arccos\tau}{\sqrt{1-\tau^2}}.
\]
This proves the exact identity. Expanding at zero gives
\[
\|\Phi_\tau-\Psi\|_2^2
=
\frac{4}{\pi}\tau-\tau^2+O(\tau^3),
\]
and the asserted \(K\)-asymptotic follows from the formula for \(\tau_K\).

Finally, for \(h=\Phi_{\tau_K}-\Psi\), Cauchy--Schwarz against the Poisson kernel gives
\[
|P[h](re^{i\theta})|
\le \|P_r\|_2\|h\|_2,
\qquad
\|P_r\|_2^2=\frac{1+r^2}{1-r^2},
\]
which is the local-uniform corollary.

## Numerical check

The standalone script `artifacts/verify_asymptotics.py` solves the exact elliptic equation for \(\tau_K\) and compares it with the Lambert-\(W\) formulas. Representative ratios are:

| \(K\) | \(\tau_K/(1/(KY_K))\) | exact deficit / two-term deficit asymptotic |
|---:|---:|---:|
| \(10^2\) | 0.9999904340 | 0.9999847316 |
| \(10^3\) | 0.9999999357 | 0.9999998910 |
| \(10^4\) | 0.9999999995 | 0.9999999991 |

These computations are consistency checks only; the proof is analytic.

## Limitations

This result refines the centered unit-ball pointwise-distortion problem. It does not address prescribed nonzero values, does not impose or prove global quasiconformality, and does not replace the exact finite-\(K\) characterization of the source paper. The \(W\)-formula is asymptotic, not an exact closed form for \(\tau_K\). The local-uniform convergence estimate is for the specific normalized extremal family.

## References

1. M. Knežević and M. Mateljević, *Target Geometry in Prescribed-Value Schwarz Lemmas for Harmonic Maps*, arXiv:2609.19609v1 (2026), https://arxiv.org/abs/2609.19609.
2. NIST Digital Library of Mathematical Functions, §19.12, *Asymptotic Approximations for Legendre's Integrals*, https://dlmf.nist.gov/19.12.
3. R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, *On the Lambert W function*, Advances in Computational Mathematics 5 (1996), 329--359, https://doi.org/10.1007/BF02124750.
4. R. Wegmann, *Extremal problems for harmonic mappings from the unit disc to convex regions*, Journal of Computational and Applied Mathematics 46 (1993), 173--182, https://doi.org/10.1016/0377-0427(93)90293-K.
