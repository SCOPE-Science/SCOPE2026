# Critical power-log Hellinger transition in compact-support location families

## Result

For \(\kappa\ge 0\), define the compactly supported symmetric density
\[
f_\kappa(x)=\frac{1}{Z_\kappa}
\frac{(1-x^2)_+}{\left[\log\!\left(e/(1-x^2)\right)\right]^\kappa},
\qquad
Z_\kappa=\int_{-1}^{1}
\frac{1-x^2}{\left[\log\!\left(e/(1-x^2)\right)\right]^\kappa}\,dx,
\]
and its location translates \(f_{\kappa,h}(x)=f_\kappa(x-h)\). Write
\[
H^2(P,Q)=\frac12\int(\sqrt{dP}-\sqrt{dQ})^2
\]
for squared Hellinger distance.

This is the critical \(\alpha=1\) line of the power-log family
\[
f_{\alpha,\kappa}(x)\propto
\frac{(1-x^2)^\alpha}
{\left[\log(e/(1-x^2))\right]^\kappa}\mathbf 1_{\{|x|<1\}}
\]
considered by Wang and Gao (2026), whose displayed power-log example assumes
\(\alpha\in(0,1)\), \(\kappa>0\). The case \(\kappa=0\) is the Epanechnikov density, already treated there.

The following sharp small-shift asymptotics hold as \(h\downarrow0\):
\[
\boxed{
H^2(f_{\kappa,0},f_{\kappa,h})
\sim
\frac{h^2}{2Z_\kappa(1-\kappa)}
\left[\log\frac1h\right]^{1-\kappa},
\qquad 0\le\kappa<1,
}
\]
\[
\boxed{
H^2(f_{1,0},f_{1,h})
\sim
\frac{h^2}{2Z_1}\log\log\frac1h,
}
\]
and, for \(\kappa>1\),
\[
\boxed{
H^2(f_{\kappa,0},f_{\kappa,h})
\sim \frac{I_\kappa}{8}h^2,
}
\]
where
\[
I_\kappa=
\frac4{Z_\kappa}\int_{-1}^{1}
\frac{x^2}{1-x^2}
\left[\log\!\left(\frac e{1-x^2}\right)\right]^{-\kappa}
\left(
1+\frac{\kappa}{\log(e/(1-x^2))}
\right)^2dx.
\]
The integral \(I_\kappa\) is finite if and only if \(\kappa>1\).

Consequently, the \(\alpha=1\) boundary contains a second phase transition:
\[
\kappa<1:\quad
H^2/h^2\asymp (\log(1/h))^{1-\kappa}\to\infty,
\]
\[
\kappa=1:\quad
H^2/h^2\asymp \log\log(1/h)\to\infty,
\]
\[
\kappa>1:\quad
H^2/h^2\to I_\kappa/8<\infty.
\]
Thus ordinary finite-Fisher quadratic-mean differentiability is restored exactly when \(\kappa>1\).

## Inverse Hellinger modulus

For the convention used by Wang and Gao,
\[
\omega_\kappa(t)
=
\sup\{r\ge0:H^2(f_{\kappa,0},f_{\kappa,2r})\le t\},
\]
the exact first-order inverses are
\[
\boxed{
\omega_\kappa(t)
\sim
\sqrt{\frac{Z_\kappa(1-\kappa)}{2^\kappa}}\,
\frac{\sqrt t}{[\log(1/t)]^{(1-\kappa)/2}},
\quad 0\le\kappa<1,
}
\]
\[
\boxed{
\omega_1(t)
\sim
\sqrt{\frac{Z_1}{2}}\,
\sqrt{\frac{t}{\log\log(1/t)}},
}
\]
and
\[
\boxed{
\omega_\kappa(t)
\sim
\sqrt{\frac{2t}{I_\kappa}},
\quad \kappa>1.
}
\]

Wang and Gao prove that, for every symmetric log-concave noise density, the known-shape location benchmark and their shape-agnostic adaptive estimator are governed up to universal constants by this inverse Hellinger modulus. Since every \(f_\kappa\) above is symmetric log-concave, the corresponding fixed-confidence location-rate orders are therefore
\[
\boxed{
n^{-1/2}(\log n)^{-(1-\kappa)/2},
\quad 0\le\kappa<1,
}
\]
\[
\boxed{
(n\log\log n)^{-1/2},
\quad \kappa=1,
}
\]
and
\[
\boxed{
n^{-1/2},
\quad \kappa>1.
}
\]
For \(\kappa=0\), the first line reduces to the previously known Epanechnikov order \((n\log n)^{-1/2}\). The new feature is the interpolation along the critical power boundary and the iterated-logarithm threshold at \(\kappa=1\).

## Product-experiment critical profiles

Let \(P_{\kappa,h}\) denote the law with density \(f_{\kappa,h}\). Hellinger affinity tensorizes:
\[
1-H^2(P_{\kappa,h}^{\otimes n},P_{\kappa,0}^{\otimes n})
=
\left(1-H^2(P_{\kappa,h},P_{\kappa,0})\right)^n.
\]
Hence the one-observation constants yield exact two-point critical profiles.

If \(0\le\kappa<1\) and
\[
h_n=a\,n^{-1/2}(\log n)^{-(1-\kappa)/2},
\]
then
\[
nH^2(P_{\kappa,h_n},P_{\kappa,0})
\longrightarrow
\lambda_\kappa(a)
=
\frac{a^2}{2^{\,2-\kappa}Z_\kappa(1-\kappa)}
\]
and
\[
\boxed{
H^2(P_{\kappa,h_n}^{\otimes n},P_{\kappa,0}^{\otimes n})
\longrightarrow
1-e^{-\lambda_\kappa(a)}.
}
\]

If \(\kappa=1\) and \(h_n=a/\sqrt{n\log\log n}\), then
\[
\boxed{
H^2(P_{1,h_n}^{\otimes n},P_{1,0}^{\otimes n})
\longrightarrow
1-\exp\!\left(-\frac{a^2}{2Z_1}\right).
}
\]

If \(\kappa>1\) and \(h_n=a/\sqrt n\), then
\[
\boxed{
H^2(P_{\kappa,h_n}^{\otimes n},P_{\kappa,0}^{\otimes n})
\longrightarrow
1-\exp\!\left(-\frac{I_\kappa a^2}{8}\right).
}
\]
In each regime, smaller shifts make the product Hellinger distance vanish, while larger vanishing shifts make it tend to one. These are exact two-point Hellinger separation scales; no claim of a full likelihood-ratio limit experiment is made.

## Proof

Set
\[
g_\kappa=\sqrt{f_\kappa}.
\]
Near the right endpoint, with \(t=1-x\downarrow0\),
\[
1-x^2=2t-t^2\sim2t,
\qquad
L(t):=\log\frac e{1-x^2}
=
\log\frac1t+O(1),
\]
so
\[
g_\kappa(1-t)
\sim
\sqrt{\frac2{Z_\kappa}}\,
t^{1/2}L(t)^{-\kappa/2}.
\]
Differentiating gives
\[
|g_\kappa'(1-t)|^2
\sim
\frac{1}{2Z_\kappa}\,
\frac1{tL(t)^\kappa}.
\]
The same asymptotic holds at the left endpoint.

For \(0\le\kappa\le1\), split
\[
\|g_\kappa(\cdot-h)-g_\kappa\|_2^2
\]
into endpoint strips of width comparable to \(h\), intermediate endpoint regions \(h\ll t\ll1\), and a fixed interior region. The support-mismatch strips contribute
\[
O\!\left(h^2[\log(1/h)]^{-\kappa}\right).
\]
On any fixed interior set the contribution is \(O(h^2)\). In the intermediate regions, the mean-value formula and the displayed endpoint derivative asymptotic give
\[
\|g_\kappa(\cdot-h)-g_\kappa\|_2^2
\sim
\frac{h^2}{Z_\kappa}
\int_h^{c}\frac{dt}{t[\log(1/t)]^\kappa}.
\]
The omitted strip and interior terms are lower order. Therefore
\[
H^2=\frac12\|g_\kappa(\cdot-h)-g_\kappa\|_2^2
\sim
\frac{h^2}{2Z_\kappa}
\int_h^{c}\frac{dt}{t[\log(1/t)]^\kappa}.
\]
The elementary integral satisfies
\[
\int_h^{c}\frac{dt}{t[\log(1/t)]^\kappa}
\sim
\frac{[\log(1/h)]^{1-\kappa}}{1-\kappa}
\quad(0\le\kappa<1)
\]
and
\[
\int_h^{c}\frac{dt}{t\log(1/t)}
\sim
\log\log(1/h)
\quad(\kappa=1),
\]
which proves the first two formulas.

For \(\kappa>1\), the endpoint integral of \(|g_\kappa'|^2\) is finite. Thus
\(g_\kappa\in H^1(\mathbb R)\), and the standard \(L^2\) translation derivative gives
\[
\|g_\kappa(\cdot-h)-g_\kappa\|_2^2
\sim h^2\|g_\kappa'\|_2^2.
\]
Since \(I_\kappa=4\|g_\kappa'\|_2^2\),
\[
H^2(f_{\kappa,0},f_{\kappa,h})
\sim I_\kappa h^2/8.
\]
Direct logarithmic differentiation of \(f_\kappa\) yields the stated integral for \(I_\kappa\), and its endpoint integrand is comparable to
\(1/[t(\log(1/t))^\kappa]\), proving finiteness exactly for \(\kappa>1\).

It remains to verify that this critical family lies in the symmetric log-concave class. Put
\[
q(x)=-\log(1-x^2),\qquad L(x)=1+q(x),\qquad 0<x<1.
\]
Up to an additive constant,
\[
\log f_\kappa(x)=-q(x)-\kappa\log L(x).
\]
Moreover,
\[
\frac{q'(x)^2}{q''(x)}
=
\frac{2x^2}{1+x^2}\le1.
\]
Hence
\[
(\log f_\kappa)''(x)
=
-\left(1+\frac{\kappa}{L}\right)q''
+\frac{\kappa}{L^2}q'^2
<0.
\]
Symmetry and continuity at the origin complete log-concavity on the support.

The inverse-modulus formulas follow by asymptotically solving the preceding Hellinger formulas with shift \(h=2r\). The product profiles follow from tensorization of Hellinger affinity.

## Context and originality boundary

Wang and Gao (2026) give an instance-optimal adaptive location estimator whose rate is controlled by the inverse Hellinger modulus. Their examples include triangle and Epanechnikov laws with rate \((n\log n)^{-1/2}\), and a power-log family with \(\alpha\in(0,1)\), \(\kappa>0\), for which the polynomial boundary singularity dominates. Their displayed power-log family does not include the critical line \(\alpha=1,\kappa>0\).

Laha (2021/2023) studies adaptive location estimation under log-concavity and records, for a symmetrized beta family proportional to \((1-x^2/r)^{r/2}\), that Fisher information is infinite for \(r\le2\) and finite for \(r>2\). This identifies the pure-power critical exponent corresponding to \(\alpha=1\), but does not analyze logarithmic modifiers or the Hellinger translation modulus at that boundary.

General links between square-root \(L^2\) differentiability, Fisher information, quadratic-mean differentiability, local asymptotic normality, and contiguity are classical; these are not claimed as new. Likewise, the Epanechnikov \(\kappa=0\) rate and general regular-variation/modulus-of-smoothness techniques are prior art.

To the best of our knowledge, targeted searches did not locate the exact \(\alpha=1\) power-log Hellinger asymptotics above, the \(\kappa=1\) iterated-logarithm transition, or the resulting exact product-Hellinger critical profiles. Older nonregular-location, cusp, regular-variation, and approximation-theoretic translation-modulus literature remains a residual originality risk.

## Limitations

The result concerns a one-dimensional, centered compact-support location family and Hellinger geometry. It does not derive a likelihood-ratio limit experiment, sharp minimax constants for estimation, or the limiting distribution of a particular estimator. The adaptive statistical consequence uses Wang and Gao's universal-constant theorem, so only the rate orders—not the exact displayed inverse-modulus constants—are inherited by their estimator. The literature search cannot exclude an equivalent translation-modulus calculation hidden in older nonregular-location or approximation-theory literature.

## References

- Qiaosen Wang and Chao Gao, *Instance-Optimal Adaptive Location Estimation via Multiscale Mid-Summaries*, arXiv:2609.20749, 2026. https://arxiv.org/abs/2609.20749
- Nilanjana Laha, *Adaptive estimation in symmetric location model under log-concavity constraint*, arXiv:2105.04287, 2021; revised 2023. https://arxiv.org/abs/2105.04287
- Shivam Gupta, Jasper C. H. Lee, and Eric Price, *Finite-Sample Symmetric Mean Estimation with Fisher Information Rate*, COLT 2023, PMLR 195:4777-4830. https://proceedings.mlr.press/v195/gupta23a.html
- David Pollard, *Another Look at Differentiability in Quadratic Mean*, in *Festschrift for Lucien Le Cam*, Springer, 1997, pp. 305-314. https://doi.org/10.1007/978-1-4612-1880-7_19
