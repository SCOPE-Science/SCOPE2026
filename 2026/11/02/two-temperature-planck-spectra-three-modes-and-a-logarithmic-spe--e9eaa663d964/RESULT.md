# Two-temperature Planck spectra: three modes and a logarithmic spectral notch

## Finding

Let \(f(x)=x^3/(e^x-1)\) for \(x>0\), and let \(a=2.821439372122\ldots\) be the unique positive solution of \(3(1-e^{-a})=a\). For the exact two-temperature frequency spectrum
\[
F_R(x)=f(x)+R f(x/R),\qquad R>1,
\]
there exists a finite constant \(R_0>1\) such that, for every \(R\ge R_0\), the spectrum has *exactly three* distinct positive critical points. They are two strict nondegenerate local maxima \(x_1(R)<x_3(R)\) separated by a strict nondegenerate local minimum \(x_2(R)\). As \(R\to\infty\),
\[
\begin{aligned}
x_1(R)&=a-\frac{2a}{R f''(a)}+O(R^{-2}),\\
x_2(R)&=\log R+2\log\log R-\log 2+o(1),\\
x_3(R)&=aR+o(1).
\end{aligned}
\]
Their spectral heights satisfy
\[
F_R(x_1)=f(a)+O(R^{-1}),\qquad
F_R(x_2)\sim\frac{(\log R)^2}{R},\qquad
F_R(x_3)=R f(a)+o(1).
\]
The logarithmic location and height of the intervening minimum are the distinctive feature: the notch is neither at a fixed fraction of the temperature separation nor exponentially small in the temperature ratio.

## Assumptions and scope

The quantity \(x=h\nu/(k_B T_c)\) is a dimensionless *frequency*, with \(T_c>0\) the colder blackbody temperature. The hotter body has temperature \(T_h=RT_c\) and emitting-area (or frequency-independent geometrical) weight \(R^{-2}\) relative to the colder body. For frequency spectral radiance, after a common positive normalization, the sum equals
\[
\frac{x^3}{e^x-1}+\frac{R^{-2}x^3}{e^{x/R}-1}
=f(x)+R f(x/R).
\]
The theorem is specifically about spectral radiance **per unit frequency**, not per unit wavelength. There is no scattering, absorption, noise, or non-Planck spectral modification. The assertion is existential in \(R_0\); no sharp numerical threshold is claimed.

## Proof

1. The derivative is
\[
f'(x)=\frac{x^2 e^{-x}\bigl[(3-x)-3e^{-x}\bigr]}{(1-e^{-x})^2}.
\]
Since \(3(1-e^{-x})-x\) is strictly concave, starts at zero with positive derivative and tends to minus infinity, it has exactly one positive zero \(a\). Thus \(f'>0\) on \((0,a)\) and \(f'<0\) on \((a,\infty)\). Its derivative at the zero is \(3e^{-a}-1<0\), so \(f''(a)<0\). The Rayleigh--Jeans expansion is \(f(x)=x^2-x^3/2+x^4/12+O(x^6)\), hence \(f''(0)=2>0\). Direct differentiation yields
\[
f''(x)=\frac{x e^{-x}}{(1-e^{-x})^3}\left[x^2-6x+6+e^{-x}(x^2+6x-12)+6e^{-2x}\right].
\]
For \(x\ge5\) every displayed summand inside the bracket is positive, so \(f''(x)>0\) there. We also have \(f'(x)=-x^3e^{-x}(1+O(x^{-1}))\) and \(f''(x)=O(x^3e^{-x})\) at infinity.

2. Differentiating the exact two-temperature formula gives the essential cancellation
\[
F_R'(x)=f'(x)+f'(x/R),\qquad
F_R''(x)=f''(x)+R^{-1}f''(x/R).
\]
Choose \(0<\delta<a\) sufficiently small that \(f''<0\) throughout \([a-\delta,a+\delta]\), with \(a+\delta<5\), and then \(0<\eta<a-\delta\) sufficiently small that \(f''>0\) throughout \([0,\eta]\). The following statements all hold simultaneously once \(R\) is sufficiently large.

3. For \(0<x<a\), both terms in \(F_R'\) are positive. On \([a,a+\delta]\), \(F_R''<0\), while \(F_R'(a)>0\) and \(F_R'(a+\delta)<0\), giving exactly one strict maximum. On \([a+\delta,5]\), \(f'\) is uniformly negative and \(f'(x/R)=O(R^{-1})\), so no other critical point appears there.

4. On \([5,\eta R]\), both \(f''(x)\) and \(f''(x/R)\) are positive, hence \(F_R''>0\). The endpoint signs are \(F_R'(5)<0\) and \(F_R'(\eta R)>0\), giving exactly one strict minimum. On \([\eta R,(a-\delta)R]\), \(f'(x/R)\) has a positive lower bound independent of \(R\), while \(f'(x)\) tends uniformly to zero, hence there are no more roots.

5. On \([(a-\delta)R,aR]\), the negative term \(R^{-1}f''(x/R)\) dominates the exponentially small \(f''(x)\), so \(F_R''<0\). The derivative is positive at the left endpoint and negative at \(aR\), giving one last strict maximum. For \(x\ge aR\), both terms of \(F_R'\) are nonpositive and at least one is strictly negative. These six intervals cover all \(x>0\), proving the **exactly three** assertion and nondegeneracy.

6. At the first maximum, Taylor expansion at \(a\) and \(f'(x/R)=2x/R+O(R^{-2})\) give \(f''(a)(x_1-a)+2a/R+O(R^{-2})=0\), which proves the first location formula. The middle minimum tends to infinity but satisfies \(x_2/R\to0\). Balancing the two derivatives there gives
\[
x_2^2e^{-x_2}=\frac2R(1+o(1)),
\]
so \(x_2-2\log x_2=\log R-\log2+o(1)\), implying its stated two-logarithm location. The third maximum obeys \(x_3/R\to a\); the same derivative balance and exponential decay of \(f'(x_3)\) imply \(x_3=aR+o(1)\).

7. Finally, \(f(x)=x^2(1+O(x))\) at zero and \(f(x)=x^3e^{-x}(1+o(1))\) at infinity. At \(x_2\), the cold contribution is asymptotic to \(2x_2/R\) and the hot contribution to \(x_2^2/R\); thus \(F_R(x_2)\sim(\log R)^2/R\). The endpoint peak heights follow from continuity and exponential decay as stated.

## Verification

Run `python3 verification/check_planck_modes.py` using Python 3 and its standard library only. The program independently brackets the three stationary points, tests the signs of the derivative over logarithmically spaced frequency grids, and compares finite differences of the original spectrum with the claimed maximum/minimum types at five ratios. In the tested ratios \(R=100,200,500,1000,5000\), the program returns `VERIFY_OK checks=25`. The finite tests are diagnostics, not a substitute for the infinite-family interval-sign proof.

## Relationship to prior work

Khatri, Sunyaev and Chluba [1] formulate mixtures of Planck spectra and analyze the low-contrast limit and its \(y\)-type distortion. The present analysis studies the opposite regime of divergent temperature contrast, with a specially scaled two-component brightness ratio, and proves exact critical-point multiplicity and intermediate-notch asymptotics. Hou and collaborators [2] use a continuous, power-law temperature distribution to model multicolor blackbody spectra; their physical model is different from the two-atomic-temperature measure here. The usual Wien approximation [3] concerns the large-frequency tail of one Planck spectrum and cannot by itself establish the global critical-point count, which uses the Rayleigh--Jeans behavior near zero.

## Limitations

The theorem supplies neither the smallest \(R_0\) nor a complete phase diagram in arbitrary temperature and weight parameters. Its three-extrema classification is for the precise \(R^{-2}\) hot-area scaling and the frequency-domain Planck function only. It does not assert the same peak count in wavelength coordinates or after convolution with an instrument response. Novelty remains conditional on the examined literature; specialized earlier analyses of strongly separated blackbody mixtures could affect historical priority. Independent validation has not been performed.

## References

1. R. Khatri, R. A. Sunyaev and J. Chluba, *Mixing of blackbodies: entropy production and dissipation of sound waves in the early Universe*, arXiv:1205.2871 (initial posting 2012-05-13), https://arxiv.org/abs/1205.2871.
2. S.-J. Hou et al., *Multi-color blackbody emission in GRB 081221*, arXiv:1808.03942 (2018), https://arxiv.org/abs/1808.03942. This source is comparative and not the archive-cohort focal source.
3. Standard Planck frequency law and Wien displacement relation, as derived directly in the proof above.
