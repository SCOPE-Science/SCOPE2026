# Strict concavity and logarithmic endpoint asymptotics of the harmonic distortion constant

## Result

Let \(H\) be a real Hilbert space with \(\dim H\ge 2\), and let \(M_K\) be the sharp constant from Knežević--Mateljević's pointwise-distortion problem:
\[
M_K=\sup L_F(0),
\]
where the supremum runs over harmonic maps \(F:\mathbb D\to \mathbb B_H\) satisfying
\[
F(0)=0,\qquad 0<\ell_F(0)\le L_F(0)\le K\ell_F(0).
\]
The source paper determines \(M_K\) through a unique parameter \(\tau_K\in(0,1]\), proves that \(M_K\) is strictly increasing, and proves
\[
M_1=1,\qquad M_K\longrightarrow \frac4\pi\quad(K\to\infty).
\]

The following quantitative strengthening holds.

### Theorem

For \(K>1\), the function \(K\mapsto M_K\) is \(C^\infty\), strictly increasing, and **strictly concave**. If \(\tau_K\) is the optimizing parameter, then
\[
\boxed{\;
M_K'=\frac{\tau_K M_K}{K(K+\tau_K)}.
\;}
\]
Moreover,
\[
\boxed{\;
M_K
=
1+\frac12(K-1)-\frac12(K-1)^2+O((K-1)^3)
\qquad(K\to1^+).
\;}
\]

At the opposite endpoint, put
\[
Y_K=-W_{-1}\!\left(-\frac{e}{4K}\right),
\]
where \(W_{-1}\) is the lower real branch of the Lambert \(W\)-function. For all sufficiently large \(K\), \(Y_K>1\) and
\[
Y_Ke^{-Y_K}=\frac{e}{4K}.
\]
Then
\[
\boxed{\;
\tau_K
=
\frac{1}{K Y_K}
\left(1+O\!\left(\frac{1}{K^2Y_K}\right)\right),
\;}
\]
and
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
\tau_K\sim\frac{1}{K\log K},
\qquad
\frac4\pi-M_K\sim\frac{2}{\pi K^2\log K}.
\;}
\]

The boundary extremals also have an exact quantitative degeneration law. With
\[
D_\tau(t)=\sqrt{\cos^2t+\tau^2\sin^2t},\qquad
\Phi_\tau(e^{it})
=
\frac{\cos t\,e_1+\tau\sin t\,e_2}{D_\tau(t)},
\]
and
\[
\Phi_0(e^{it})=\operatorname{sgn}(\cos t)e_1
\quad\text{a.e.},
\]
one has
\[
\boxed{\;
\|\Phi_\tau-\Phi_0\|_{L^2(\mathbb T)}^2
=
2-\frac4\pi
\frac{\arccos\tau}{\sqrt{1-\tau^2}}.
\;}
\]
Consequently,
\[
\boxed{\;
\|\Phi_{\tau_K}-\Phi_0\|_{L^2(\mathbb T)}
=
\frac{2}{\sqrt{\pi K Y_K}}
\left(1+O\!\left(\frac{1}{K Y_K}\right)\right)
\sim
\frac{2}{\sqrt{\pi K\log K}}.
\;}
\]
Thus the source paper's qualitative convergence of the extremal boundary functions to the two-valued endpoint has a sharp first-order rate.

## Proof

Write normalized arclength measure on \(\mathbb T\) as \(dm=dt/(2\pi)\), and set
\[
J(\tau)=\int_{\mathbb T}D_\tau(t)\,dm(t).
\]
The source paper establishes
\[
\beta(\tau)=2J'(\tau),\qquad
\alpha(\tau)=2J(\tau)-2\tau J'(\tau),
\]
where
\[
M_K=\alpha(\tau_K),\qquad
K=Q(\tau_K),\qquad
Q(\tau)=\frac{\alpha(\tau)}{\beta(\tau)}
=\frac{J(\tau)}{J'(\tau)}-\tau.
\]
Direct differentiation gives
\[
J''(\tau)
=
\int_{\mathbb T}
\frac{\sin^2t\,\cos^2t}{D_\tau(t)^3}\,dm(t)>0
\qquad(0<\tau\le1),
\]
and hence
\[
Q'(\tau)
=
-\frac{J(\tau)J''(\tau)}{J'(\tau)^2}<0.
\]
Also
\[
\alpha'(\tau)=-2\tau J''(\tau).
\]
Implicit differentiation of \(Q(\tau_K)=K\) therefore gives
\[
M_K'
=
\frac{\alpha'(\tau_K)}{Q'(\tau_K)}
=
\frac{2\tau_KJ'(\tau_K)^2}{J(\tau_K)}.
\]
Since
\[
\frac{J(\tau_K)}{J'(\tau_K)}=K+\tau_K,
\qquad
2J'(\tau_K)=\beta(\tau_K)=\frac{M_K}{K},
\]
this is exactly
\[
M_K'=\frac{\tau_KM_K}{K(K+\tau_K)}.
\]

For strict concavity define
\[
G(\tau)=\frac{2\tau J'(\tau)^2}{J(\tau)}.
\]
Then \(M_K'=G(\tau_K)\), while
\[
G'(\tau)
=
\frac{2J'(\tau)^2}{J(\tau)}
\left(1-\frac{\tau J'(\tau)}{J(\tau)}\right)
+
\frac{4\tau J'(\tau)J''(\tau)}{J(\tau)}.
\]
Every factor is positive. Indeed,
\[
J(\tau)-\tau J'(\tau)
=
\int_{\mathbb T}\frac{\cos^2t}{D_\tau(t)}\,dm(t)>0.
\]
Thus \(G'(\tau)>0\). Because \(Q'(\tau)<0\),
\[
M_K''
=
\frac{G'(\tau_K)}{Q'(\tau_K)}<0.
\]
This proves strict concavity.

At \(\tau=1\),
\[
J(1)=1,\qquad J'(1)=\frac12,\qquad J''(1)=\frac18.
\]
Hence
\[
Q'(1)=-\frac12,\qquad
G'(1)=\frac12,
\]
so the right-hand second derivative at the conformal endpoint is
\[
M''(1^+)=-1.
\]
Together with the already known \(M_1=1\) and \(M'(1^+)=1/2\), smooth implicit dependence near \(\tau=1\) yields
\[
M_K
=
1+\frac12(K-1)-\frac12(K-1)^2+O((K-1)^3).
\]

For the large-\(K\) endpoint, let
\[
k=\sqrt{1-\tau^2},
\qquad
L=\log\frac4\tau.
\]
The source paper gives
\[
\alpha(\tau)
=
\frac4\pi
\frac{E(k)-\tau^2\mathbf K(k)}{1-\tau^2},
\qquad
\beta(\tau)
=
\frac{4\tau}{\pi}
\frac{\mathbf K(k)-E(k)}{1-\tau^2},
\]
where \(\mathbf K,E\) are the complete elliptic integrals. The standard convergent expansions at complementary modulus \(\tau\to0^+\) are
\[
\mathbf K(k)
=
L+\frac{\tau^2}{4}(L-1)+O(\tau^4L),
\]
\[
E(k)
=
1+\frac{\tau^2}{2}\left(L-\frac12\right)+O(\tau^4L).
\]
Therefore
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
Put
\[
y(\tau)=L-1=\log\frac{4}{e\tau}.
\]
Then
\[
Q(\tau)=\frac{\alpha(\tau)}{\beta(\tau)}
=
\frac{1}{\tau y(\tau)}
\left(1+O(\tau^2y(\tau))\right).
\]
Thus \(Q(\tau_K)=K\) implies
\[
K\tau_Ky(\tau_K)
=
1+O(\tau_K^2y(\tau_K)).
\]

Let
\[
Y_K=-W_{-1}\!\left(-\frac{e}{4K}\right)
\]
and
\[
\tau_K^{(0)}=\frac{1}{K Y_K}.
\]
The identity \(Y_Ke^{-Y_K}=e/(4K)\) is equivalent to
\[
y(\tau_K^{(0)})=Y_K.
\]
Since the derivative of \(\tau\mapsto\tau y(\tau)\) equals \(y(\tau)-1\), a mean-value comparison with the previous asymptotic equation gives
\[
\tau_K
=
\tau_K^{(0)}
\left(1+O\!\left(\frac{1}{K^2Y_K}\right)\right).
\]
Substituting this in the expansion for \(\alpha\) gives
\[
\frac4\pi-M_K
=
\frac2\pi\tau_K^2
\left(y(\tau_K)-\frac12+O(\tau_K^2y(\tau_K))\right),
\]
hence
\[
\frac4\pi-M_K
=
\frac{2}{\pi K^2Y_K}
\left(
1-\frac{1}{2Y_K}
+O\!\left(\frac{1}{K^2Y_K}\right)
\right).
\]
The standard lower-branch Lambert expansion
\[
Y_K
=
\log\frac{4K}{e}
+
\log\log\frac{4K}{e}
+
O\!\left(\frac{\log\log K}{\log K}\right)
\]
then yields the simpler asymptotic equivalents.

Finally, since both \(\Phi_\tau\) and \(\Phi_0\) have pointwise norm one,
\[
\|\Phi_\tau-\Phi_0\|_2^2
=
2-2\int_{\mathbb T}
\frac{|\cos t|}{D_\tau(t)}\,dm(t).
\]
By symmetry and the substitution \(u=\sin t\),
\[
\int_{\mathbb T}
\frac{|\cos t|}{D_\tau(t)}\,dm(t)
=
\frac2\pi\int_0^{\pi/2}
\frac{\cos t\,dt}{\sqrt{\cos^2t+\tau^2\sin^2t}}
=
\frac2\pi
\frac{\arccos\tau}{\sqrt{1-\tau^2}}.
\]
This proves the exact \(L^2\) identity. Expanding it at \(\tau=0\) gives
\[
\|\Phi_\tau-\Phi_0\|_2^2
=
\frac4\pi\tau-\tau^2+O(\tau^3),
\]
and substitution of the asymptotic for \(\tau_K\) proves the stated rate.

## Relation to prior work

Knežević--Mateljević (arXiv:2609.19609) determine the exact extremal family, the unique optimizing parameter, the elliptic-integral formulas above, strict monotonicity of \(M_K\), the limit \(M_K\to4/\pi\), qualitative \(L^2\) convergence of the boundary extremals, and a first-order expansion at \(K\to1^+\). The strict concavity, the exact derivative identity, the second-order conformal expansion, the Lambert-\(W\) inversion at \(K\to\infty\), the \(2/(\pi K^2\log K)\) endpoint deficit, and the exact/rate form of the boundary degeneration are the additional conclusions here.

The same source observes that the planar boundary family and its first Fourier coefficients already occur in Wegmann's classical work on extremal harmonic mappings to convex regions; those formulas are not claimed as new here. Older work on harmonic \(K\)-quasiconformal self-maps, including Li's 2016 coefficient estimates and the Heinz-type literature cited there, concerns global quasiconformal hypotheses and different coefficient/derivative inequalities rather than the present sharp pointwise-distortion constant.

## Limitations

The result is an analysis of the sharp center constant \(M_K\) already characterized by arXiv:2609.19609. It does not extend the extremal theorem away from the center, does not treat general target domains, and does not replace the pointwise distortion constraint by a global quasiconformal one. The large-\(K\) statement concerns the particular sharp constant and extremal family from that theorem. No claim is made that the Lambert-\(W\) scale has an analogue for other harmonic Schwarz problems.

The originality assessment is to the best of our knowledge. The source preprint is very recent, so unindexed contemporaneous observations remain a residual risk.

## References

1. M. Knežević and M. Mateljević, *Target Geometry in Prescribed-Value Schwarz Lemmas for Harmonic Maps*, arXiv:2609.19609.
2. NIST Digital Library of Mathematical Functions, §19.12, *Asymptotic Approximations for Legendre's Integrals*.
3. R. Wegmann, *Extremal problems for harmonic mappings from the unit disc to convex regions*, Journal of Computational and Applied Mathematics 46 (1993/1994), 165--181, DOI: 10.1016/0377-0427(93)90293-K.
4. H.-P. Li, *An asymptotically sharp coefficients estimate for harmonic K-quasiconformal mappings*, Journal of Inequalities and Applications 2016:84, DOI: 10.1186/s13660-016-1033-0.
