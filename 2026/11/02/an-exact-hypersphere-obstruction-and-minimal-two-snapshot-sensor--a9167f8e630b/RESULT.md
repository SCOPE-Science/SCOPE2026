# An exact hypersphere obstruction and minimal two-snapshot sensor theorem for an unknown-diffusivity pollutant puff

## Finding

For each integer spatial dimension \(d\ge 1\), fixed distinct observation times \(t_1<t_2\), and a finite nonempty set of sensor locations \(s_i\in\mathbb R^d\), consider the single instantaneous pollutant-release model

\[
C(s,t)=\frac{Q}{[4\pi\kappa(t-t_0)]^{d/2}}
\exp\!\left(-\frac{\|s-z\|^2}{4\kappa(t-t_0)}\right),\qquad t>t_0.
\]

The location \(z\in\mathbb R^d\), release mass \(Q>0\), diffusivity \(\kappa>0\), and release time \(t_0<t_1\) are all unknown. Assume every sensor returns a calibrated positive, noiseless concentration at both times. Put

\[
H=\begin{pmatrix}
1&s_{11}&\cdots&s_{1d}&\|s_1\|^2\\
\vdots&\vdots&&\vdots&\vdots\\
1&s_{N1}&\cdots&s_{Nd}&\|s_N\|^2
\end{pmatrix}.
\]

**Exact classification.** The parameter-to-two-snapshot data map is injective for every admissible parameter set if and only if \(\operatorname{rank}H=d+2\). If the rank is smaller, then for some distinct admissible parameter sets *all* readings agree at *every* post-emission time: sampling more frequently cannot resolve the ambiguity. Thus exactly \(d+2\) suitably placed sensors are necessary and sufficient for universal two-snapshot identification. In the planar atmospheric-column model this is four sensors not all on one circle or line. Even an arbitrarily dense spatial array at one time cannot separately determine \(\kappa\) and \(t_0\).

## Assumptions and scope

The field is a single vertically integrated passive tracer puff in unbounded constant-coefficient, isotropic, advection-free diffusion; the theorem also applies to the corresponding free-space heat kernel in any integer dimension. The true release precedes both measurement times, the source mass and diffusivity are positive, the observation clocks and sensor coordinates are known, and the concentrations are strictly positive. Sensor gains are fixed and known. No physical boundary, wind, chemical reaction, decay, multiple releases, finite sensor support, or measurement noise is included.

A family of sensors is called *cospherical* if it lies on a sphere of any positive radius in its ambient Euclidean space; a set may alternatively lie in an affine hyperplane. A generic \(d+2\)-sensor configuration has full rank, but even a very large cospherical array is deficient. The universal statement does not say every particular source is ambiguous for a deficient design: it says that *some* distinct admissible sources share the same observations.

## Proof

**1. Reconstruction when \(H\) has full column rank.** Write \(w_j=\kappa(t_j-t_0)>0\). Taking logarithms at snapshot \(j\) gives a quadratic-affine spatial polynomial:

\[
\log C(s,t_j)=A_j+B_j\cdot s+c_j\|s\|^2,
\]
\[
 c_j=-\frac1{4w_j},\qquad
 B_j=\frac{z}{2w_j},\qquad
 A_j=\log Q-\frac d2\log(4\pi w_j)-\frac{\|z\|^2}{4w_j}.
\]

The full-rank matrix \(H\) determines \((A_j,B_j,c_j)\) uniquely from the positive sensor data at each time. Their physically necessary signs satisfy \(c_j<0\). The entire parameter vector is then reconstructed with the explicit formulae

\[
 w_j=-\frac1{4c_j},\quad
 \kappa=\frac{w_2-w_1}{t_2-t_1},\quad
 t_0=t_1-\frac{w_1}{\kappa},\quad
 z=-\frac{B_1}{2c_1},
\]
\[
 Q=(4\pi w_1)^{d/2}\exp\!\left(A_1+\frac{\|z\|^2}{4w_1}\right).
\]

For true model-generated observations, \(w_2>w_1\) because \(\kappa>0\) and \(t_2>t_1\); all reconstructed quantities have their required signs. This proves global, not merely local, uniqueness.

**2. Every rank-deficient geometry is a sphere or a hyperplane.** If \(\operatorname{rank}H<d+2\), then some nonzero \((a,b,c)\in\mathbb R\times\mathbb R^d\times\mathbb R\) satisfies

\[
 a+b\cdot s_i+c\|s_i\|^2=0\qquad\text{for every }i.
\]

For \(c=0\), nonzero \(b\) determines an affine hyperplane containing all the sensors. If \(c\ne0\), completing the square places the sensors on a sphere centered at \(o=-b/(2c)\). When this sphere has radius zero, all sensors coincide and hence lie in a hyperplane. These exhaust the possible deficient geometries; conversely any set in a hyperplane or sphere makes a column combination vanish.

**3. Hyperplane and sphere give exact all-time nonidentifiability.** If the sensors lie in an affine hyperplane, pick a source \(z\) outside that hyperplane and reflect it to the distinct point \(z'\) across it. Every sensor has the same distance to both sources, so keeping \(Q,\kappa,t_0\) fixed yields equal sensor time traces for all \(t>t_0\).

If all the sensors lie on a sphere of center \(o\) and radius \(R>0\), choose a source \(z=o+v\) with \(v\ne0\) and \(\|v\|\ne R\). Put \(\alpha=R^2/\|v\|^2\ne1\) and define

\[
 z'=o+\alpha v,\qquad
 \kappa'=\alpha\kappa,\qquad
 Q'=\alpha^{d/2}Q,\qquad t_0'=t_0.
\]

Writing \(s_i=o+u_i\) with \(\|u_i\|=R\), direct expansion gives the exact inversion identity

\[
 \|s_i-z'\|^2=\alpha\|s_i-z\|^2.
\]

The exponent \(\|s_i-z'\|^2/[4\kappa'(t-t_0)]\) and amplitude \(Q'/[4\pi\kappa'(t-t_0)]^{d/2}\) therefore equal their unprimed counterparts at every time. The parameter sets are different since \(\alpha\ne1\). Hence even complete positive-time traces cannot guarantee uniqueness in any deficient geometry.

**4. Minimality of temporal and spatial sampling.** Rank \(d+2\) requires at least \(d+2\) sensors. Such configurations exist: an affine simplex with \(d+1\) vertices plus one additional point not on its circumsphere suffices. For one snapshot, even with concentration known on all of \(\mathbb R^d\), only \(w_1=\kappa(t_1-t_0)\) appears. For any arbitrary \(\kappa'>0\), choosing \(t_0'=t_1-w_1/\kappa'\) and keeping \(z,Q\) unchanged gives exactly the same single-snapshot field. Thus two time instants are necessary.

**5. Explicit sharp planar example.** The sensor triple \((0,0),(2,0),(0,2)\) lies on the circle centered at \((1,1)\) of radius \(\sqrt2\). The releases \((z,\kappa,Q,t_0)=((2,1),1,1,0)\) and \((z',\kappa',Q',t_0')=((3,1),2,2,0)\) produce identical observations at all three sensors for every \(t>0\). Adding a fourth sensor \((1,3)\) makes \(\det H=8\); its alternate-to-original concentration ratio at time \(t>0\) is \(\exp(1/(4t))\ne1\). This exhibits both the exact time-oversampling obstruction and a four-sensor design that breaks it.

## Verification

A self-contained Python 3 checker, \(\texttt{checker.py}\), uses rational arithmetic for the rank tests and circle-inversion squared-distance identity. It then independently evaluates time traces and reconstructs all unknown parameters from two log-concentration snapshots for 1,200 deterministic randomly generated planar instances. The executed checker passed 6,036 individual structural, exact, and floating-point assertions; the deliberately nonspherical four-sensor matrix has exact determinant eight. These finite checks corroborate the explicit identities, but the infinite-parameter theorem is established by the proof above, not by numerical sampling. Run with \(\texttt{python3 checker.py}\) using only the Python standard library.

## Relationship to prior work

Lu, Dragotti and Vetterli (2011) consider the very same impulsive free-space diffusion Green function and derive a source reconstruction using at least \(d+1\) sensors, but their equations (11)–(15) explicitly treat the diffusion coefficient as given, including its appearance as \(1/(4\mu)\) in their linear constraints. The present theorem asks a different inverse problem in which the diffusion coefficient itself is unknown. It identifies the additional necessary spatial degree of freedom, supplies a direct two-snapshot inverse, and proves a sharp full-continuous-trace ambiguity when the sensors lie on a sphere or hyperplane. The earlier minimum of \(d+1\) does not imply the new \(d+2\) classification under the enlarged unknown-parameter model.

Matthes, Gröll and Keller (2005) study source localization using distributed noses under diffusion/advection but assume a calibrated diffusion coefficient and consider the continuous-emission setting. Qu and colleagues (2014) study trace continuous pollutant-source identification in enclosed media; Turbelin, Singh and Issartel (2014) address atmospheric source reconstruction with a prescribed transport response. These are materially different inverse assumptions. A separate 2006 minimal-sensor source-localization contribution by Matthes, Gröll and Keller was compared at abstract level only; its inaccessible detailed geometry and broader inverse-theory results remain priority risks. No universal novelty against all extant literature or statistical stability under noisy readings is asserted.

## Limitations

This is a free-space, single instantaneous impulse and *noiseless structural-identifiability* result. In particular it does not treat wind, reflecting ground boundaries, multiple emitters, spatially varying or anisotropic diffusivity, sensor calibration uncertainty, finite sensitivity, background concentrations, chemical transformation, or turbulent transport. Near-cospherical geometry can be arbitrarily ill-conditioned even when the algebraic rank is full; the theorem provides no positive noise-stability bound. The nonidentifiability construction guarantees a distinct parameter pair for each deficient array, not that every release has an ambiguous twin. Literature priority, especially possible subsumption by general diffusion-system identification theory, requires independent assessment.

## References

1. Y. M. Lu, P. L. Dragotti, M. Vetterli, *Localization of Diffusive Sources Using Spatiotemporal Measurements*, Allerton 2011, DOI: 10.1109/ALLERTON.2011.6120286. Full publicly accessible author manuscript: https://www.commsp.ee.ic.ac.uk/~pld/publications/AllertonPaper.pdf. A related preprint by the same authors was publicly linked on 2011-03-01: https://nuit-blanche.blogspot.com/2011/03/cs-would-you-like-that-entry-supersized.html.
2. R. Matthes, L. Gröll, H. Keller, *Source Localization by Spatially Distributed Electronic Noses for Advection and Diffusion*, 2005, DOI: 10.1109/TSP.2005.845423.
3. R. Matthes, L. Gröll, H. Keller, *Source Localization with Minimal Number of Networked Sensors*, IFAC 2006; abstract-level comparison only.
4. H. Qu and coauthors, *Identifiability and Identification of Trace Continuous Pollutant Source*, 2014, DOI: 10.1155/2014/215104.
5. F. Turbelin, M. Singh, J.-P. Issartel, *Reconstructing Source Terms from Atmospheric Concentration Measurements*, 2014, DOI: 10.1002/2014MS000385.
