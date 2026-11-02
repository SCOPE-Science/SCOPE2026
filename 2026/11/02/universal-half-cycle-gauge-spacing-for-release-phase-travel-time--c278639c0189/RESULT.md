# Universal half-cycle gauge spacing for release-phase travel-time spread in periodic one-way flow

## Finding

A passive tracer moves along a one-dimensional channel according to \(\dot x=U[1+f(\omega t)]\), where the modulation \(f\) is even, half-wave antisymmetric, and strictly decreases over each half cycle. The background flow never reverses. If a pulse is released at every possible forcing phase, the spread between the slowest and fastest first-arrival travel times is greatest **exactly** when the separation of launch and detection gauges equals an odd half-cycle's mean advective distance. This optimal separation does not depend on the detailed waveform within the stated class.

In nondimensional variables, let \(F(s)=\int_0^s f(t)\,dt\). There is a unique \(\delta\in(0,\pi/2)\) with
\[\delta=F(\pi/2-\delta).\]
The maximal possible range of first-arrival travel times is precisely \(4\delta\) (in units of inverse forcing angular frequency). Every nonresonant gauge separation has exactly one fastest and one slowest release phase. At exact multiples of one mean cycle-advective distance, release phase becomes invisible to arrival time; the width approaches zero with a sharp linear cusp of slope \(2c/(1-c^2)\).

## Assumptions and scope

Let \(f:\mathbb R\to\mathbb R\) be \(C^1\), \(2\pi\)-periodic, even, and half-wave antisymmetric:
\[ f(-t)=f(t),\qquad f(t+\pi)=-f(t). \]
Assume \(f\) is strictly decreasing on \([0,\pi]\) and \(c=f(0)\) satisfies \(0<c<1\). In particular \(f(\pi)=-c\) and \(1+f(t)\ge1-c>0\). The period mean of \(f\) is zero.

Define the dimensionless velocity \(v(t)=1+f(t)\). For any length \(\ell>0\) and release phase \(\phi\in\mathbb R/(2\pi\mathbb Z)\), define \(T_\phi(\ell)>0\) as the **unique** solution
\[\int_\phi^{\phi+T_\phi(\ell)}v(t)\,dt=\ell.\]
Its release-phase width is
\[W(\ell)=\max_{\phi}T_\phi(\ell)-\min_{\phi}T_\phi(\ell).\]
For \(s\in[0,\pi]\) set \(F(s)=\int_0^s f(t)\,dt\), continued as the periodic primitive \(F(t)=\int_0^t f(u)\,du\) on the line. The quantity \(F\) is strictly concave and positive on \((0,\pi)\), satisfies \(F(0)=F(\pi)=0\), and obeys \(F(\pi-s)=F(s)\) for \(0\le s\le\pi\).

The conclusions concern first arrival of an ideal advected particle at a downstream gauge. They do not describe stochastic dispersal, recirculation, shear, spatially varying currents, reversing tidal flow, or estuarine mixing. In physical units, the dimensionless distance is \(\ell=\omega L/U\) and dimensionless duration is \(\omega T\).

## Proof

**(1) Reduction to one forcing period.** Since the velocity has period \(2\pi\) and mean one, \(\int_\phi^{\phi+2\pi}v=2\pi\) for every phase. It follows from strict positivity that
\[T_\phi(\ell+2\pi m)=T_\phi(\ell)+2\pi m\]
for every integer \(m\ge0\). Consequently \(W(\ell+2\pi m)=W(\ell)\) wherever both lengths are positive. For \(\ell=2\pi m\) the travel time is identically \(2\pi m\), hence \(W(2\pi m)=0\).

**(2) Exact extrema.** Fix residual length \(0<r<2\pi\), and write \(s(\phi)=T_\phi(r)\in(0,2\pi)\). Differentiation of the distance identity gives
\[s'(\phi)=\frac{v(\phi)-v(\phi+s(\phi))}{v(\phi+s(\phi))}.\]
Evenness, strict half-cycle monotonicity, and periodicity imply that two different phase arguments have equal velocity precisely when they are negatives of one another modulo \(2\pi\). The endpoints cannot be identical modulo \(2\pi\), because \(0<r<2\pi\). Every stationary release phase therefore obeys \(2\phi+s\equiv0\pmod {2\pi}\). There are two branches: a release centered at the flow maximum (\(\phi=-s/2\)) and a release centered at the flow minimum (\(\phi=\pi-s/2\)). Direct integration on these symmetric arcs gives, respectively,
\[r=s+2F(s/2),\qquad r=s-2F(s/2).\]
Both right sides increase strictly from zero to \(2\pi\) because their derivatives are \(1\pm f(s/2)\ge1-c>0\). Thus each equation has exactly one root, called \(s_{\mathrm{fast}}\) and \(s_{\mathrm{slow}}\). Positivity of \(F\) on \((0,\pi)\) yields \(s_{\mathrm{fast}}<r<s_{\mathrm{slow}}\). Since the phase circle is compact and nonconstant \(s(\phi)\) has only these two stationary points, they are respectively the global minimum and maximum, and both are unique modulo \(2\pi\). Their phases are \(-s_{\mathrm{fast}}/2\) and \(\pi-s_{\mathrm{slow}}/2\). Therefore
\[W(r)=s_{\mathrm{slow}}-s_{\mathrm{fast}}>0.\]
In particular, the positive full-period lengths are the only zeros of \(W\).

**(3) Universal optimal length.** Put \(a=s_{\mathrm{fast}}/2\) and \(b=s_{\mathrm{slow}}/2\), so \(0<a<b<\pi\), and equate the two expressions for \(r\):
\[b-a=F(a)+F(b).\]
With \(m=(a+b)/2\) and \(d=(b-a)/2\), we get
\[2d=F(m-d)+F(m+d),\qquad d<m<\pi-d.\]
For each fixed \(d\), the right-hand side is strictly concave in \(m\), symmetric about \(\pi/2\), and has its unique maximum there. Thus
\[d\le F(\pi/2-d).\]
The function \(d\mapsto F(\pi/2-d)-d\) is strictly decreasing on \([0,\pi/2]\), positive at zero and negative at \(\pi/2\). It has exactly one zero \(\delta\in(0,\pi/2)\), and the inequality forces \(d\le\delta\). Since \(W=2(b-a)=4d\), this proves \(W(r)\le4\delta\). Equality requires \(m=\pi/2\), hence \(a=\pi/2-\delta\), \(b=\pi/2+\delta\). The fast-branch distance is then \(r=2a+2F(a)=\pi\). Conversely, \(r=\pi\) is realized by these values and attains equality. Therefore the maximum in each period is **unique**, at \(r=\pi\). At this length, \(s_{\mathrm{fast}}=\pi-2\delta\), \(s_{\mathrm{slow}}=\pi+2\delta\).

**(4) Sharp pinching at full-period separation.** Fix integer \(m\ge1\) and put \(\ell=2\pi m+\eta\) with small \(\eta\) of either sign. Differentiate the implicit travel-time identity in \(\ell\):
\[\partial_\ell T_\phi(\ell)=\frac{1}{v(\phi+T_\phi(\ell))}.\]
At \(\ell=2\pi m\), this equals \(1/v(\phi)\). As \(f\in C^1\) and \(v\ge1-c\), a uniform Taylor estimate yields
\[T_\phi(2\pi m+\eta)=2\pi m+\frac{\eta}{1+f(\phi)}+O(\eta^2),\]
where the error is uniform in \(\phi\). Since \(\max_\phi [1/v(\phi)]=1/(1-c)\) and \(\min_\phi [1/v(\phi)]=1/(1+c)\), taking the range proves
\[W(2\pi m+\eta)=\left(\frac{1}{1-c}-\frac{1}{1+c}\right)|\eta|+O(\eta^2)=\frac{2c}{1-c^2}|\eta|+O(\eta^2).\]
The coefficient is strictly positive, completing the cusp claim.

**(5) Sinusoidal specialization.** For \(f(t)=\varepsilon\cos t\) with \(0<\varepsilon<1\), \(F(s)=\varepsilon\sin s\), and the optimal-width parameter satisfies \(\delta=\varepsilon\cos\delta\). Thus \(W_{\max}=4\delta\) and the modulation amplitude is uniquely identified from the maximal time spread by \(\varepsilon=\delta/\cos\delta\). For a physical current \(U[1+\varepsilon\cos(\omega t)]\), the uniquely optimal gauge spacings are \(L=(2m+1)\pi U/\omega\), and maximal travel-time spread is \(4\delta/\omega\).

## Verification

The supplementary `verification.py` is a stand-alone numerical cross-check (Python 3, SciPy). It independently reconstructs travel times using the integral equation for 64 release phases, compares with the two exact stationary equations, checks the sharp half-cycle maximum and full-cycle cusp, and exercises three distinct flow profiles \(f(t)=\varepsilon\cos^{k}t\), \(k\in\{1,3,5\}\), at three amplitudes \(\varepsilon\in\{0.1,0.5,0.9\}\). It reported **495 passed numerical checks**. These finite spot checks do not establish the theorem for all admissible functions; the analytic argument above supplies the universal proof. For \(\varepsilon=1/2\), the maximum spreads are approximately \(1.800734445179\), \(1.327486785745\), and \(1.066552087536\) for the three respective profiles.

## Relationship to prior work

Warner, Geyer and Arango (2010) used three-dimensional estuarine modeling to demonstrate that passive-tracer residence time depends on release timing and location; the USGS publication summary was directly checked. Yuan, Lin and Falconer (2007) modeled macro-tidal residence time. Spydell and coauthors (2015) analyzed tracked drifters at a tidal inlet using detailed numerical hydrodynamics; the openly available full paper was inspected through its methods and conclusions. These works motivate phase-of-release sensitivity, but the inspected passages do not provide this exact one-way, spatially uniform travel-time-width optimizer. Warner and Yuan were not available in complete full text; their absence prevents any absolute historical-priority conclusion. This is a simple analytically solvable benchmark, not a claim to supersede the above empirical or numerical models.

## Limitations

The exact waveform-independent optimal location requires strict positivity, uniform current along space, half-wave antisymmetry, even reflection symmetry, and strict monotonicity on each half cycle. Direction reversal, weaker symmetry, spatial gradients, shear, turbulence, Brownian diffusion, dispersion of a cloud rather than a point tracer, and noisy detection can change the optimum. Historical priority is provisional because not every potentially related old article could be inspected completely. The theorem is an exact statement about the specified mathematical model, not a validated estuary-design prescription.

## References

1. Warner, J. C., Geyer, W. R., and Arango, H. G. (2010), *Using a composite grid approach in a complex coastal domain to estimate estuarine residence time*, Computers & Geosciences, DOI: 10.1016/j.cageo.2009.11.008; verified dated public record: https://www.usgs.gov/publications/using-a-composite-grid-approach-a-complex-coastal-domain-estimate-estuarine-residence (July 1, 2010).
2. Yuan, D., Lin, B., and Falconer, R. A. (2007), *A modelling study of residence time in a macro-tidal estuary*, Estuarine, Coastal and Shelf Science, DOI: 10.1016/j.ecss.2006.08.023.
3. Spydell, M. S., et al. (2015), *Observed and modeled drifters at a tidal inlet*, Journal of Geophysical Research: Oceans, DOI: 10.1002/2014JC010541; first published June 12, 2015; open full text: https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2014JC010541.
