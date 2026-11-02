# Four equal-depth infiltration readings with unknown volume and clock origins

## Finding

**Theorem (sharp four-reading identifiability and feasibility).** Let the positive classical Green–Ampt infiltration curve obey
\[
 t=t_\star+\frac{1}{K}\left[F-a\log\left(1+\frac{F}{a}\right)\right],
 \qquad K>0,\quad a>0,\quad F>0.
\]
An instrument observes \(z=F+c\), with an unknown additive depth zero \(c\in\mathbb R\). The unknown clock origin is \(t_\star\in\mathbb R\). Suppose observations are made at four successive instrument levels \(z_i=z_0+ih\), \(i=0,1,2,3\), for known \(h>0\), producing observed times \(t_i\). Require the first observation to occur after positive cumulative infiltration, \(F_0=z_0-c>0\).

Set \(\tau_i=t_{i+1}-t_i\), \(i=0,1,2\), and \(\delta_0=\tau_1-\tau_0\), \(\delta_1=\tau_2-\tau_1\). Define
\[
 D(x)=\log\frac{(x+1)^2}{x(x+2)}\quad (x>0).
\]
The four readings arise from **exactly one** admissible parameter tuple \((K,a,c,t_\star)\) if and only if
\[
 0<\delta_1<\delta_0,
 \qquad \tau_0>\frac{\delta_0}{D(x)}\left[\frac1x-\log\left(1+\frac1x\right)\right],
 \tag{1}
\]
where \(x>0\) is the **unique** solution of
\[
 \frac{\delta_0}{\delta_1}=\frac{D(x)}{D(x+1)}. \tag{2}
\]
In particular, (2) always has a unique positive solution whenever \(\delta_0>\delta_1>0\); thus (1) is a direct necessary-and-sufficient test of physical compatibility, not just a local rank condition.

Explicit reconstruction is obtained with
\[
 S=\frac{\delta_0}{D(x)},\quad
 L=\log(1+1/x),\quad
 \lambda=\frac{\tau_0+SL}{h},\quad
 K=\lambda^{-1},\quad a=\frac S\lambda,
 \quad c=z_0+a-hx. \tag{3}
\]
Writing \(F_0=hx-a>0\), the remaining parameter is
\[
 t_\star=t_0-\lambda\left[F_0-a\log(1+F_0/a)\right].\tag{4}
\]
Four levels are **minimal**: every admissible three-level data set from this model is produced by a continuum of distinct admissible parameter tuples, even with the level spacing \(h\) known.

## Assumptions and scope

The model is the ideal constant-parameter Green–Ampt law for saturated-boundary, one-dimensional infiltration during a single continuous infiltration episode. The capillary-drive length \(a\) equals suction head times moisture deficit; the theorem identifies their product, not the two factors separately. The hydraulic conductivity \(K\), capillary-drive length \(a\), additive volume baseline \(c\), and time origin \(t_\star\) are unknown. The instrument-level spacing \(h\) is known, and level-crossing times are observed without error. No claim is made for rainfall-limited, layered, hysteretic, or non-Green–Ampt infiltration, nor for stochastic measurement errors.

## Proof

Put \(x=(F_0+a)/h>0\) and \(\lambda=1/K\). Taking consecutive differences of the Green–Ampt equation gives
\[
 \tau_i=\lambda h-\lambda a\log\frac{x+i+1}{x+i}.
 \tag{5}
\]
Since \(\lambda a>0\), the successive time increments increase. Their successive differences are
\[
 \delta_0=\lambda aD(x),\qquad
 \delta_1=\lambda aD(x+1).\tag{6}
\]
The function \(D\) is positive and strictly decreasing, proving \(0<\delta_1<\delta_0\).

To show (2) is globally invertible, use the exact Laplace representation
\[
 D(x)=\int_0^\infty e^{-xt}\frac{(1-e^{-t})^2}{t}\,dt.
 \tag{7}
\]
The integral is finite and strictly positive for every \(x>0\). Differentiating under the integral (dominated convergence on each compact positive \(x\)-interval) shows \((\log D)''(x)\) equals the strictly positive variance of \(t\) under the normalized measure with density proportional to the integrand in (7). Thus \(\log D\) is strictly convex. Consequently,
\[
 \frac{d}{dx}\log\frac{D(x)}{D(x+1)}
 = (\log D)'(x)-(\log D)'(x+1)<0.
\]
Moreover \(D(x)\to\infty\) as \(x\downarrow0\), while \(D(x+1)\) tends to a finite positive number; as \(x\to\infty\), \(D(x)\sim x^{-2}\) and \(D(x)/D(x+1)\to1\). Therefore this ratio bijectively maps \((0,\infty)\) onto \((1,\infty)\), establishing existence and uniqueness of \(x\).

Equations (5)–(6) now force exactly the reconstruction (3). Every reconstructed \(K\) and \(a\) is positive because \(S>0\), \(\tau_0>0\), and \(L>0\). The physical first-depth constraint reads
\[
 F_0=z_0-c=hx-a=hx-\frac S\lambda>0
 \quad\Longleftrightarrow\quad
 \tau_0>S\left(\frac1x-L\right),
\]
which is precisely the second inequality in (1). This is the only additional physical feasibility restriction. With \(F_0>0\), formula (4) fixes \(t_\star\), and substituting (3)–(4) into (5) reproduces all four measured times. The map \(F\mapsto F-a\log(1+F/a)\) has strictly positive derivative \(F/(F+a)\) for \(F>0\); hence the reconstructed curve passes the four levels in their observed order. This proves sufficiency and global uniqueness, including the strict boundary cases.

For only three levels, there are only \(\tau_0,\tau_1\). Holding these fixed, let \(x\) vary in a small open interval around any admissible original value, and set
\[
 S(x)=\frac{\tau_1-\tau_0}{D(x)},\quad
 \lambda(x)=\frac{\tau_0+S(x)\log(1+1/x)}{h},
\]
with \(a(x)=S(x)/\lambda(x)\), \(K(x)=1/\lambda(x)\), \(c(x)=z_0+a(x)-hx\), and \(t_\star(x)\) chosen to match the first reading. These parameters reproduce the same three times. All positive inequalities hold on some neighborhood by continuity, and \(x=(z_0+a-c)/h\) distinguishes the tuples. Thus three levels cannot identify the four parameters.

## Verification

**Exact logarithmic instance.** Set \(K=1\), \(a=1/2\), \(c=3/2\), \(t_\star=3\), and \(z_i=2+i\) for \(i=0,1,2,3\). Then \(F_i=i+1/2>0\),
\[
 t_i=\frac72+i-\frac12\log(2i+2),
\]
and
\[
 (\tau_0,\tau_1,\tau_2)
 =\left(1-\tfrac12\log2,\ 1-\tfrac12\log\tfrac32,\ 1-\tfrac12\log\tfrac43\right).
\]
The ratio \(\delta_0/\delta_1=\log(4/3)/\log(9/8)=D(1)/D(2)\) forces \(x=1\); (3)–(4) exactly recover the chosen tuple.

The standalone `CHECKER.py`, runnable by `python3 CHECKER.py` with the Python standard library, tests the exact logarithmic example, 800 seeded randomized admissible parameter sets, two distinct three-reading reconstructions, and three excluded data shapes. Its finite floating-point checks corroborate the formulas; the universal theorem rests on (5)–(7) and the strict positivity arguments, not on numerical testing.

## Relationship to prior work

The underlying idealized Green–Ampt equation is classical. Mohammadzadeh-Habili and Heidarpour (online January 15, 2011) estimate hydraulic parameters from infiltration and wetting-front observations. Chen and Young (2006) derive and analyze Green–Ampt infiltration on slopes; Triadis and Broadbridge (2012) give a detailed analytic comparison with more realistic soil-hydraulic behavior. Singh and Yu (1990) discuss parameter estimation for a broader infiltration model, and Philip (1990) uses an inverse-PDE technique to study infiltration-series coefficients. These works provide the physical and analytic context, but the accessible material did not yield the exact minimal four-equal-level theorem with *both* an unknown cumulative-depth zero and an unknown start-time origin, together with its sharp physical-feasibility inequality. The close 2011 parameter-estimation paper was available only by abstract/metadata in this review; its full argument remains an explicit historical-priority risk. The mathematical result is model-specific, not a claimed universal infiltration-inverse theorem.

## Limitations

This is structural identifiability from ideal noiseless observations. It neither supplies error bounds nor guarantees stable statistical estimation. Particularly when \(x\) is large, \(D(x)/D(x+1)\) approaches \(1\), so ratio-based reconstruction may be ill-conditioned. The four equal-depth readings may require event-driven measurement; they are not arbitrary four equally spaced times. The output \(a\) is a combined hydraulic parameter, not a separate determination of suction and moisture deficit. Historical priority is provisional pending inspection of the full text of the most directly related 2011 calibration study and any broader inverse-design literature.

## References

1. J. Mohammadzadeh-Habili and M. Heidarpour, *Estimating Soil Hydraulic Parameters By Using Green and Ampt Infiltration Equation*, Journal of Hydrologic Engineering 16 (2011), 772–780. First online January 15, 2011. DOI: https://doi.org/10.1061/(ASCE)HE.1943-5584.0000373.
2. L. Chen and M. H. Young, *Green-Ampt infiltration model for sloping surfaces*, Water Resources Research 42 (2006). DOI: https://doi.org/10.1029/2005WR004468.
3. D. Triadis and P. Broadbridge, *The Green–Ampt limit with reference to infiltration coefficients*, Water Resources Research 48 (2012). DOI: https://doi.org/10.1029/2011WR011747.
4. V. P. Singh and F. X. Yu, *Derivation of Infiltration Equation Using Systems Approach*, Journal of Irrigation and Drainage Engineering 116 (1990), 837 onward. DOI: https://doi.org/10.1061/(ASCE)0733-9437(1990)116:6(837).
5. J. R. Philip, *Inverse solution for one-dimensional infiltration, and the ratio A/K1*, Water Resources Research 26 (1990), 2023–2027. DOI: https://doi.org/10.1029/WR026i009p02023.
