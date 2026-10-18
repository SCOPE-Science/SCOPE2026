# A sharp resolution threshold for strict mass–moment feasibility under nodal Fourier positivity

## Finding

For every integer \(N\ge1\), let \(\mathbb T_N\) be the real trigonometric polynomials of degree at most \(N\) on \([-\pi,\pi]\), with the \(2N+1\) equispaced nodes \(x_j=2\pi j/(2N+1)\), \(-N\le j\le N\). For \(p\in\mathbb T_N\), require \(p(x_j)\ge0\) at every node, and set its mass and raw first moment to \(M(p)=\int_{-\pi}^{\pi}p(x)\,dx\) and \(P(p)=\int_{-\pi}^{\pi}xp(x)\,dx\).

**Sharp universal resolution theorem.** Every nonzero continuous nonnegative periodic input \(f\), with prescribed mass \(M(f)\) and raw first moment \(P(f)\), admits a trigonometric polynomial \(p\in\mathbb T_N\) satisfying *both moments exactly* and satisfying \(p(x_j)>0\) at **every** node if and only if \(N\ge63\), where the quantifier "every" is over all such inputs \(f\). For each \(1\le N\le62\) there is a smooth nonnegative periodic input with positive mass for which no polynomial with even nonnegative nodal values can match both moments. For each \(N\ge63\), every such input has a strictly nodally positive matching polynomial.

More precisely, define
\[
q_{N,j}=2\sum_{k=1}^{N}\frac{(-1)^{k+1}}{k}\sin\!\left(\frac{2\pi kj}{2N+1}\right),\qquad B_N=\max_{-N\le j\le N}|q_{N,j}|.
\]
For positive prescribed mass, nonnegative nodal interpolation permits exactly \(|P|/M\le B_N\); strict nodal positivity permits exactly \(|P|/M<B_N\). The exact threshold is \(B_N<\pi\) for \(1\le N\le62\), versus \(B_N>\pi\) for every \(N\ge63\). Moreover, the sharp asymptotic extremal normalized moment is
\[
\lim_{N\to\infty}B_N=2\operatorname{Si}(3\pi/2)
=3.216745507908\ldots>\pi,
\qquad \operatorname{Si}(t)=\int_0^t\frac{\sin u}{u}\,du.
\]
The asymptotic formula is the sampled version of the classical Gibbs phenomenon; the assessed new classification is the *exact resolution threshold and its necessary-and-sufficient strict feasibility interpretation*.

## Assumptions and scope

All integrals are ordinary Lebesgue integrals on \([-\pi,\pi]\). The target input is real, periodic, continuous, nonnegative and not identically zero; its first moment is the **nonperiodic raw polynomial moment** against \(x\), not a Fourier coefficient or circular mean. Positivity of the numerical polynomial is imposed only at the collocation nodes, not between them. The model is the one-dimensional specialization of the nodally positive, moment-preserving Fourier projection constraints introduced by Cai, Lin and Lin, with moments \((1,x)\); it is a feasibility theorem and not an assertion about an optimization algorithm's runtime.

## Proof

**1. Exact discrete moment cone.** Every real nodal vector \((u_{-N},\ldots,u_N)\) has a unique real degree-\(N\) trigonometric interpolant \(p\). Fourier inversion at the grid gives \(M(p)=2\pi\sum_j u_j/(2N+1)\). Since \(\int_{-\pi}^{\pi}x\sin(kx)\,dx=2\pi(-1)^{k+1}/k\), Fourier inversion also gives
\[
\frac{P(p)}{M(p)}=\frac{\sum_j u_j q_{N,j}}{\sum_j u_j}
\]
when \(M(p)>0\). The values \(q_{N,-j}=-q_{N,j}\) and \(q_{N,0}=0\). Thus, with \(u_j\ge0\), the normalized moment is exactly the convex hull \([-B_N,B_N]\). With all \(u_j>0\), it is exactly its interior: positivity forbids an endpoint, while any interior ratio is realized by mixing a positive constant nodal profile (ratio zero) with an extremal single-node nodal profile of the requested sign, using a mixing weight strictly below one.

**2. The physical moment range.** For every nonzero nonnegative continuous input, its normalized raw first moment lies strictly between \(-\pi\) and \(\pi\). Conversely, smooth nonnegative periodic bumps with positive mass can have normalized means arbitrarily close to \(\pi\) or \(-\pi\), by placing their support inside a short subinterval adjacent to, but strictly away from, either endpoint. Therefore the general universal strict-feasibility condition is \(B_N\ge\pi\), since every physical mean is strictly interior to \((-\pi,\pi)\). For this particular grid sequence the proven strict inequalities \(B_N<\pi\) or \(B_N>\pi\) eliminate the equality case. If \(B_N<\pi\), endpoint-concentrated bumps provide infeasible physical data.

**3. Exact finite-degree exclusion.** The accompanying executable \(`verification.py`\) proves \(B_N<\pi\) for **every** \(1\le N\le62\). It checks all \(\sum_{N=1}^{62}N=1953\) positive-index vertex inequalities and both signs using exact rational enclosures, not floating-point sign tests. In particular the smallest verified positive separation from \(\pi\) is at \((N,j)=(62,61)\), approximately \(0.00026671235867\). The verifier derives rational upper and lower bounds for \(\pi\) from Machin's arctangent identity and alternating series, reduces all sine arguments to \([0,\pi/2]\), and bounds them between consecutive alternating Taylor partial sums. Thus this is an exhaustive finite *proof certificate* for the displayed bounded range, not an inference from a plot or approximate enumeration.

**4. Uniform existence for every \(N\ge63\).** Choose node \(j=N-1\), put \(\alpha=3\pi/2\), \(h=\alpha/(N+1/2)\), and let \(F(t)=\sin(t)/t=\int_0^1\cos(ts)\,ds\), extended by \(F(0)=1\). The exact nodal formula simplifies to
\[
q_{N,N-1}=2h\sum_{k=1}^{N}F(kh).
\]
The intervals of length \(h\) centered at \(kh\), plus the initial half-interval \([0,h/2]\), partition \([0,\alpha]\). As \(|F''(t)|\le\int_0^1s^2\,ds=1/3\), the midpoint integration error is at most \(h^3/72\) for each full interval. Hence
\[
2\operatorname{Si}(\alpha)-q_{N,N-1}
\le h+\frac{Nh^3}{36}
\le h+\frac{\alpha h^2}{36}.
\]
The right side decreases with \(N\). At \(N=63\), the exact-rational independent enclosure in \(`verification.py`\) proves
\[
2\operatorname{Si}(3\pi/2)-\pi
>\frac{3\pi/2}{63+1/2}
+\frac{3\pi/2}{36}\left(\frac{3\pi/2}{63+1/2}\right)^2.
\]
The certified positive margin exceeds \(0.00022110\). Therefore \(q_{N,N-1}>\pi\) for **every** \(N\ge63\), completing the two-sided universal resolution theorem.

**5. Sharp asymptotic.** For fixed integer \(r\ge0\), node \(j=N-r\) yields
\[
q_{N,N-r}=2\sum_{k=1}^{N}\frac{\sin(k\delta_r)}{k},
\qquad \delta_r=\frac{(2r+1)\pi}{2N+1},
\]
so its limit is \(2\operatorname{Si}((2r+1)\pi/2)\). The \(r=1\) limit exceeds \(\pi\). Certified sine-integral bounds place the \(r=0\) and \(r=2\) limits below \(\pi\). For every \(r\ge3\), twice integrating by parts in the sine-integral tail at the half-odd multiple \(t=(2r+1)\pi/2\) gives \(|2\operatorname{Si}(t)-\pi|\le4/t^2\le16/(49\pi^2)\), strictly less than \(2\operatorname{Si}(3\pi/2)-\pi\). For indices \(r\ge30\), Abel summation of the tail of \(\sum_{k\ge1}\sin(k\delta_r)/k=(\pi-\delta_r)/2\), together with \(\sin(\delta_r/2)\ge\delta_r/\pi\), gives uniformly
\[
q_{N,N-r}<\pi+\frac{4}{2r+1}\le\pi+\frac4{61}
<2\operatorname{Si}(3\pi/2).
\]
These estimates bound every maximizing index, while \(r=1\) attains the limiting upper bound. Symmetry handles negative indices.

## Verification

Run `python3 verification.py` using Python 3 with only the standard library. The program checks the 1953 finite vertex inequalities, verifies the strict \(N=63\) uniform lower-bound inequality, and establishes the strict separations used in the asymptotic comparison by exact rational enclosures of \(\pi\) and sine-integrals. All infinite-range assertions additionally require the analytic interpolation, midpoint and Abel-summation arguments above; the finite program alone is not an infinite theorem.

## Relationship to prior work

Cai, Lin and Lin (arXiv:2304.11847v1, April 24, 2023) introduced the moment-constrained Fourier projection with positivity at \(2N+1\) collocation nodes, including the strict feasibility hypothesis in their main accuracy theorem. Their method and its general approximation analysis are prior work. Pareschi and Rey (arXiv:2105.13158) developed an earlier moment-conserving Fourier-Galerkin projection without the same nodal positivity constraint. The classical Fourier series of the periodic sawtooth and its Gibbs overshoot supply the sine-kernel identities and explain the limiting overshoot; those are explicitly **not** claimed as discoveries here. The resolution number \(63\), the two-sided all-degree proof and the resulting universal strict-feasibility threshold for the \((1,x)\) moment pair are the specific contribution assessed. A later equivalent exact-threshold computation in spectral interpolation literature cannot be excluded by the available searches.

## Limitations

This theorem classifies strict feasibility for only the one-dimensional nodal positivity cone and the mass/first-raw-moment pair. It does not classify simultaneous mass/momentum/energy constraints, multi-dimensional grids, nonperiodic boundary handling, pointwise positivity away from nodes, discretization error, or a nonlinear kinetic solver. Strictly nodal positive polynomials can be negative between nodes, including cases whose raw moment exceeds the physical interval \([-\pi,\pi]\).

## References

1. Z. Cai, B. Lin and M. Lin, *A positive and moment-preserving Fourier spectral method*, arXiv:2304.11847v1 (first public 2023-04-24), https://arxiv.org/abs/2304.11847 .
2. L. Pareschi and T. Rey, *Moment preserving Fourier-Galerkin spectral methods and application to the Boltzmann equation*, arXiv:2105.13158 (2021), https://arxiv.org/abs/2105.13158 .
3. Classical Fourier-sawtooth identity and Gibbs phenomenon; see, for background, https://en.wikipedia.org/wiki/Gibbs_phenomenon and https://en.wikipedia.org/wiki/Sawtooth_wave .
