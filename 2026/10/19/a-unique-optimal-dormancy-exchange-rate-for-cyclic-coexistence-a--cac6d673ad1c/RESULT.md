# A unique optimal dormancy exchange rate for cyclic coexistence at matched timescales

## Finding

For a three-type rock–paper–scissors population coupled to a dormant reservoir, the active-to-dormant exchange rate maximizing the **local exponential return rate** to equal coexistence is finite, nonzero, and unique when the reservoir reactivation rate matches the active subsystem's natural angular frequency. In the normalization below the optimum is
\[
 a_*=0.602354933981\ldots,\qquad d_*=0.156459729915\ldots.
\]
It is characterized exactly by the unique root \(v_*\in(1/2,2/3)\) of
\[
4v(1-v)^4+3v-2=0,\qquad
 d_*=2v_*(1-v_*)^2,\quad
 a_*=d_*-1+\frac{v_*(1-v_*)}{d_*}.
\]
Increasing exchange beyond this value **slows**, rather than speeds, the local decay of coexistence perturbations. This statement concerns the spectral decay exponent of a deterministic linearization, not an optimization of stochastic extinction times.

## Assumptions and scope

Let \(x=(x_0,x_1,x_2)\) and \(y=(y_0,y_1,y_2)\) belong to the probability simplex \(\Delta_2\), and let cyclic indices be taken modulo three. Consider the active–dormant cyclic dynamics
\[
\dot x_i=\sqrt3\,x_i(x_{i-1}-x_{i+1})+a(y_i-x_i),\qquad
\dot y_i=x_i-y_i,\qquad a>0.
\]
The two simplex constraints are separately preserved, because the cyclic interaction sums to zero. Their product is forward invariant. Equal coexistence is \(x_i=y_i=1/3\) for each species. The selection coefficient \(\sqrt3\) makes the uncoupled active linearization at equal coexistence have conjugate frequencies \(\pm i\), and the dormant reactivation rate is one: this is the biologically interpretable matched-frequency slice of the positive-rate active–dormant system. The rate \(a\) is the parameter to be optimized, all others being fixed. The asymptotic linear decay exponent is minus the largest real part of the tangent-space Jacobian eigenvalues, not a uniform nonlinear contraction bound.

## Proof

**1. Spectral reduction.** On the two-dimensional tangent space of the active simplex, the cyclic interaction Jacobian is \((1/\sqrt3)C\), where \((Cz)_i=z_{i-1}-z_{i+1}\). Its two Fourier eigenvalues are \(\pm i\). For the positive-frequency eigenvector, the active/dormant block is
\[
\begin{pmatrix}i-a&a\\1&-1\end{pmatrix},
\]
with characteristic polynomial
\[
p_a(\lambda)=\lambda^2+(a+1-i)\lambda-i.
\]
The negative-frequency block is its complex conjugate. Define \(\lambda_+(a)\) to be the root continued from \(\lambda_+(0)=i\), equivalently
\[
\lambda_+(a)=-\frac{a+1-i}{2}+
\frac12\sqrt{a(a+2)+2i(1-a)},
\]
using the square-root branch with positive real part. The other root is \(-(a+1)+i-\lambda_+\). Write \(\lambda_+=-d+iv\). The discriminant never vanishes for real \(a>0\), so this branch is smooth.

**2. A one-dimensional spectral locus.** From the characteristic equation, solve for the real rate:
\[
a=\frac{(i-\lambda)(1+\lambda)}{\lambda}.
\]
Its vanishing imaginary part yields the exact identity
\[
d=(1-v)(d^2+v^2).
\]
The continuation from \((d,v)=(0,1)\) lies on the smaller positive root of this quadratic in \(d\). For \(0<v<1\), this is
\[
d(v)=\frac{2v^2(1-v)}{1+\sqrt{1-4v^2(1-v)^2}}.
\]
In particular \(0<d<1/2\). The real part of the same identity gives
\[
a=d-1+\frac{v(1-v)}{d}.
\]
The imaginary part of \(p_a(\lambda)=0\) is \((a+1-2d)v+d=1\). By implicit differentiation,
\[
\frac{dv}{da}=-\frac{1-2d(1-v)}{|2\lambda+a+1-i|^2}<0.
\]
The numerator is the positive square root \(\sqrt{1-4v^2(1-v)^2}\), by the smaller-root formula. Near \(a=0\), the root has \(v<1\), and the displayed relation makes it strictly decreasing; it cannot reach \(v=0\) for finite positive \(a\) because the characteristic equation would force \(d=1\) and \(d=a+1\) simultaneously. The quadratic formula for \(\lambda_+\) shows \(v\to0\) as \(a\to\infty\). Consequently \(a\mapsto v\) is a smooth bijection from \((0,\infty)\) to \((1,0)\). The companion eigenvalue has real part \(-(a+1)+d<-d\), since \(d<1/2\). Thus the exact spectral decay exponent is \(d(a)=d(v(a))\).

**3. Unique optimum.** The implicit locus can be written
\[
F(d,v)=(1-v)(d^2+v^2)-d=0.
\]
Because \(F_d=2(1-v)d-1<0\), an interior stationary point of \(d(v)\) is characterized by
\[
F_v=-d^2+2v-3v^2=0.
\]
At such a point \(d^2=v(2-3v)\). Substitution into \(d=(1-v)(d^2+v^2)\) gives \(d=2v(1-v)^2\), and then
\[
f(v)=4v(1-v)^4+3v-2=0.
\]
Its derivative is \(f'(v)=3+4(1-v)^3(1-5v)\). On \([0,1/5]\) this is at least three. On \([1/5,1]\), the maximum of \((1-v)^3(5v-1)\) is \(27/125\) (attained at \(v=2/5\)), so \(f'(v)\ge267/125>0\). Also \(f(1/2)=-3/8<0\) and \(f(2/3)=8/243>0\). Hence exactly one stationary point exists and it lies in \((1/2,2/3)\). Since \(d(v)\to0\) at both \(v\downarrow0\) and \(v\uparrow1\) while \(d(v)>0\) inside, that point is the unique global maximum. It is strict and nondegenerate, since \(f'(v_*)>0\) and the equivalent stationarity equation has a simple root.

**4. Endpoint damping.** At \(a=0\), implicit differentiation of \(p_a(\lambda)=0\) gives \(\lambda_+'(0)=-(1+i)/2\), hence \(d(a)\sim a/2\) as \(a\downarrow0\). For large \(a\), the slow root satisfies \(v\sim a^{-1}\); the locus \(d=(1-v)(d^2+v^2)\) then gives \(d\sim a^{-2}\). Both limits certify the vanishing-return-rate mechanism at the two extremes.

## Verification

The self-contained Python program `verify.py` reproduces the isolating rational interval \(654193/10^6<v_*<654194/10^6\), the candidate rate and damping, the characteristic residuals, the dominance of the slow eigenvalue, and representative off-optimum comparisons. Exact rational signs certify the polynomial bracket; the proof of global uniqueness and the full spectral statement are analytic, not based on finite sampling. Run `python3 verify.py` with Python 3.9 or later.

## Relationship to prior work

Chacón, González-Casanova, Nuñez, Peña-Miller, Pérez, and Yang (arXiv:2608.17179v1, first posted 17 August 2026) formulate the active–dormant cyclic-competition dynamics and analyze stability and stochastic persistence. The present result addresses a distinct design question: the **unique rate maximizing the deterministic linear return exponent** on an explicitly normalized, matched-frequency slice. Existence of stabilization is not claimed as new.

Anish, De Baets, and Rao (2024) treat a substantially broader class of antisymmetric Lotka–Volterra metapopulations and prove convergence by Lyapunov arguments. Their conclusions explicitly identify the effects of migration rates on convergence speed as an unstudied direction. The current calculation makes that rate question exact for the specified asymmetric active/reservoir specialization, rather than purporting to extend their global-stability theorem. Vilk, Mobilia, and Assaf (2025) address non-Markovian RPS models with different waiting-time dynamics, not this matching-frequency spectral optimum.

## Limitations

The optimum depends on the chosen physical normalization: the dormant exit rate equals the intrinsic angular frequency of the uncoupled active three-species equilibrium. No claim is made for arbitrary ratios of the two frequencies, heterogeneous exchange, nonlinear global convergence rates, finite-population fixation probabilities, or power-law waiting times. All mathematical uniqueness assertions are restricted to the stated model and the positive scalar exchange parameter. Results remain subject to independent mathematical review and the possibility of unindexed equivalent prior work.

## References

1. J. Chacón, A. González-Casanova, I. Nuñez, R. Peña-Miller, J. L. Pérez, and J. Yang, *Dormancy stabilizes non-transitive competitive dynamics*, arXiv:2608.17179v1 (2026), https://arxiv.org/abs/2608.17179.
2. A. S. Anish, B. De Baets, and S. Rao, *Metapopulation models with anti-symmetric Lotka–Volterra systems*, Journal of Biological Dynamics **18** (2024), DOI:10.1080/17513758.2024.2397404, https://doi.org/10.1080/17513758.2024.2397404.
3. O. Vilk, M. Mobilia, and M. Assaf, *Non-Markovian rock-paper-scissors games*, Physical Review Research **7**, 023284 (2025), DOI:10.1103/4mm1-943p, https://doi.org/10.1103/4mm1-943p.
