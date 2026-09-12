# Hyperbolic Poisson–Voronoi typical-cell area variance: the uniform lower bound is impossible

## Context

Let $\mathbf{H}^2$ be the hyperbolic plane of curvature $-1$ with a stationary Poisson–Voronoi tessellation of intensity $\lambda>0$. Let $C_\lambda$ be the Palm typical cell at the origin and $V(\lambda)=\lambda^2\mathrm{Var}(\mathrm{area}(C_\lambda))$ the scale-normalized variance. The admitted target asked for explicit $0<a<b$ with $a/\lambda^2\le\mathrm{Var}\le b/\lambda^2$ for all $\lambda>0$, strict decrease of $V$, and $V(1)$ within half-width $0.01$. Euclidean intuition suggests $V$ is approximately constant ($\approx 0.28$); hyperbolic low-intensity geometry breaks this.

## Definitions

- $B(r)=|\mathcal{D}(o,r)|=2\pi(\cosh r-1)$: hyperbolic disk area; $r(v)=B^{-1}(v)=\mathrm{arcosh}(1+v/2\pi)$.
- $\Pi_\lambda$: homogeneous Poisson process of intensity $\lambda$; under Palm, a nucleus sits at origin $o$.
- $C_\lambda=\{y:d(y,o)\le d(y,p)\ \forall p\in\Pi_\lambda\}$.
- $M(\lambda)=\lambda^2\mathbb{E}[\mathrm{area}(C_\lambda)^2]$, $V(\lambda)=M(\lambda)-1$.
- $I(r_1,r_2,d)$: lens area $|\mathcal{D}(y_1,r_1)\cap\mathcal{D}(y_2,r_2)|$; $U=v_1+v_2-I$ union area; $J(\lambda)=\lambda I$ scaled lens.

## Result

The target conjunction as stated is **false**, resolved by rigorous disproof:

1. **No uniform $a>0$ exists.** $V(\lambda)\ge 0$ for all $\lambda>0$ but $V(\lambda)\to 0$ as $\lambda\to 0$. Hence $\inf V=0$ and no $a>0$ satisfies $\mathrm{Var}\ge a/\lambda^2$ uniformly.
2. **Monotonicity direction is backwards.** $V(0.5)\approx 0.2387 < V(1)\approx 0.2566 < V(2)\approx 0.2675$, rising toward the Euclidean value $\approx 0.280$; $V$ is not strictly decreasing.
3. **Corrected proved picture:** $0<V(\lambda)\le 1$ for all $\lambda>0$ (so $b=1$ is an explicit upper constant), $V(\lambda)\to 0$ as $\lambda\to 0$, $V(\lambda)\to V_{\mathrm{eucl}}\approx 0.280$ as $\lambda\to\infty$, and $\mathrm{Var}(\mathrm{area}(C_1))=V(1)\in[0.2466,0.2666]$ (center $0.2566$, half-width $0.01$).

## Proof / Evidence

**First moment.** $\mathbb{P}(y\in C_\lambda)=\exp(-\lambda B(d(o,y)))$ by void probability; $\int_{\mathbf{H}^2}e^{-\lambda B}d\mathcal{A}=\int_0^\infty e^{-\lambda v}dv=1/\lambda$.

**Second moment (two-point coverage integral).** By Slivnyak–Mecke, $\mathbb{P}(y_1,y_2\in C_\lambda)=\exp(-\lambda|\mathcal{D}(y_1,d(o,y_1))\cup\mathcal{D}(y_2,d(o,y_2))|)$. Inclusion–exclusion gives union area $U=v_1+v_2-I$; integrating over $y_1,y_2$ with rotation invariance yields $\mathbb{E}[A^2]=(2\pi)^{-1}\int_0^\infty\int_0^\infty\int_0^{2\pi}e^{-\lambda U}dv_1dv_2d\theta$. With $w_i=\lambda v_i$, $M(\lambda)=(2\pi)^{-1}\int e^{-(w_1+w_2)+J}dw_1dw_2d\theta$.

**Envelopes.** $0\le I\le\min(v_1,v_2)$ gives $0\le J\le\min(w_1,w_2)$ and $e^{-(w_1+w_2)}\le F_\lambda\le e^{-\max(w_1,w_2)}$, with $\int e^{-\max}=2$. Hence $M\ge 1$ ($V\ge 0$; strict $>0$ since $J>0$ on overlaps of positive measure) and $M\le 2$ ($V\le 1$).

**Vanishing lens (Lemma 3).** Fix $w_i>0$, $\theta\ne 0$; $R_i=r(w_i/\lambda)\sim\log(1/\lambda)$. Hyperbolic cosine law gives $d-(R_1+R_2)\to\log((1-\cos\theta)/2)<0$. In Fermi coordinates along $y_1y_2$ ($d\mathcal{A}=\cosh s\,dt\,ds$), the lens lies in a $t$-interval of limiting length $c(\theta)=-\log((1-\cos\theta)/2)$ with uniformly bounded $s$-width, so $I$ stays bounded and $J=\lambda I\to 0$ a.e.

**Impossibility (Theorem 4).** $F_\lambda\to e^{-(w_1+w_2)}$ a.e., dominated by $e^{-\max}\in L^1$; DCT gives $M\to 1$, $V\to 0$. Any admissible uniform $a$ satisfies $a\le 0$, contradicting $a>0$. Since $V>0$ everywhere but $\inf V=0$, $V$ cannot be strictly decreasing on $(0,\infty)$ either; quadrature confirms the increasing direction.

**Numerics.** Tensor Simpson over $[0,W]^2\times[0,\pi]$ (folded $\times 2$) with exact disjoint/contained branches and trapezoidal $\beta$-quadrature for the lens. Tail complement bounded by $T(W)=2(W+2)e^{-W}$ ($T(18)\approx 6.1\times 10^{-7}$, conservative over exact $5.79\times 10^{-7}$). Grid refinement at $\lambda=1$: $1.256621\to 1.256633\to 1.256639$ (spread $2\times 10^{-5}$); inner-quadrature propagation $\lesssim 10^{-4}$; total $\lesssim 3\times 10^{-4}$, over $30\times$ inside $0.01$. Euclidean closed-form lens model gives $M_{\mathrm{eucl}}\approx 1.2802$, matching the classical $\approx 0.28$ planar variance.

## Limitations

The core impossibility ($V\to 0$, no uniform $a>0$) and upper bound $V\le 1$ are fully rigorous and analytic. The increasing trio and $V(1)$ interval use controlled deterministic quadrature with an explicit error budget rather than machine-checked interval arithmetic; the $0.01$ half-width margin exceeds the estimated error by more than $30\times$. The high-intensity Euclidean limit is a consistency check with a DCT sketch, not load-bearing.

## Reproducibility

Run `python3 compute_moment.py` (numpy only, deterministic, seed-free, ~40 s): reproduces the convergence sequence, the trio $V(0.5)=0.238743$, $V(1)=0.256639$, $V(2)=0.267480$, the Euclidean $M=1.280152$, and $T(18)$. Values archived in `bounded_test_results.json`. Area-preservation check $\Phi(\rho,\phi)=(2\sinh(\rho/2),\phi)$ validates the geometric pipeline.

## References

- D'Achille, Curien, Enriquez, Lyons, Ünel, Ideal Poisson–Voronoi tessellations on hyperbolic spaces, arXiv:2303.16831.
- D'Achille, Thäle, Face volume densities of positive-intensity and ideal Poisson–Voronoi tessellations in hyperbolic spaces, 2026.
- Godland, Kabluchko, Thäle, Beta-star polytopes and hyperbolic stochastic geometry, Adv. Math. 2022.
- Isokawa, Poisson–Voronoi tessellations in three-dimensional hyperbolic spaces, Adv. Appl. Prob. 2000.
- Muche, Ballani, The second volume moment of the typical cell, Monatsh. Math. 2011.
- Yao, On variances of partial volumes of the typical cell, Adv. Appl. Prob. 2010.
