# Boundary-current tomography and its reflection-blind subspace in a resetting diffusion ring

## Finding

Fix a ring of length \(L>0\), diffusivity \(D>0\), and a semipermeable membrane of permeability \(\kappa>0\). At independently occurring Poisson times of rate \(r>0\), a Brownian particle is reset to a fresh point with a fixed Borel probability distribution \(\mu\) supported in \((0,L)\). The distribution \(\mu\) must not depend on \(r\). Write \(J_\mu(r)\) for the signed stationary probability current through the membrane, oriented in the direction of increasing coordinate from \(L^-\) to \(0^+\), and put \(\lambda=\sqrt{r/D}\).

**Exact observable transform.** The current is
\[
J_\mu(r)=\frac{\kappa\lambda}{\cosh(\lambda L/2)+\frac{2\kappa}{D\lambda}\sinh(\lambda L/2)}
\int_{(0,L)}\sinh\!\big(\lambda(y-L/2)\big)\,\mu(dy).
\]
For two reset laws \(\mu,\nu\), equality \(J_\mu(r)=J_\nu(r)\) for every \(r\) in **any set having an accumulation point in \((0,\infty)\)** holds if and only if their difference \(\mu-\nu\) is invariant under reflection \(R(y)=L-y\). Thus even a narrow open sweep of exact reset-rate-dependent current determines the entire reflection-*antisymmetric* part of an arbitrary reset law. Reflection-symmetric differences are invisible to the instrument, although positivity and total mass can restrict which differences are admissible.

**Exact probability-law fiber.** Let \(a=(\mu-R_*\mu)/2\) denote the reflection-antisymmetric signed measure recovered from the flux response and let \(m=|a|((0,L))\in[0,1]\) be its total variation mass. Every compatible probability law, and no other law, has the form
\[
\mu=a+|a|+(1-m)\sigma,
\]
where \(\sigma\) is an arbitrary reflection-symmetric probability measure on \((0,L)\). In particular, the full source is **uniquely identified if and only if** \(m=1\); for \(m<1\) infinitely many distinct reset laws have exactly the same current curve. The latter freedom is genuine, but the need for nonnegative probabilities prevents arbitrary symmetric perturbations.

**Sharp observation boundary.** For each finite family of positive resetting rates there exist two probability measures with different antisymmetric components that yield exactly the same currents at those rates. At a single rate \(r>0\), zero stationary membrane current and zero membrane entropy production require only one weighted hyperbolic-sine moment to vanish, and do not require \(\mu\) to be symmetric. In contrast, current (equivalently, interfacial entropy production) vanishes on any rate set with an interior accumulation point if and only if \(\mu=R_*\mu\). Reflecting the reset law reverses the signed current but leaves the entire interfacial entropy-production curve unchanged.

As an observable check, the small-rate response contains the mean reset location:
\[
\lim_{r\downarrow0}\frac{J_\mu(r)}r=
\frac{\kappa}{D+\kappa L}
\left(\int y\,\mu(dy)-\frac L2\right).
\]
The theorem is an exact population-level identifiability statement, not a stable finite-sample inversion algorithm.

## Assumptions and scope

Brownian motion has generator \(D\partial_{xx}\). Cutting the ring at the symmetric, unbiased interface gives a coordinate \(x\in(0,L)\). For each \(r>0\), the stationary probability density \(p_r\) is the positive, normalized weak solution of
\[
-Dp_r''+rp_r=r\mu\quad\text{in }(0,L),
\]
with interface law
\[
-Dp_r'(0^+)=-Dp_r'(L^-)=J_\mu(r),\qquad
J_\mu(r)=\kappa[p_r(L^-)-p_r(0^+)].
\]
Here an atomic reset distribution is interpreted distributionally; atoms lie strictly inside the cut ring. These boundary conditions match the unbiased-interface convention of Bressloff, *Physical Review Research* **6**, 023283 (2024), Eqs. (4.1). No resetting event is blocked by the membrane; resetting can jump across the cut. The membrane is diffusive and only resists spatial transport between \(L^-\) and \(0^+\).

The permeability, length, and diffusivity are known and fixed when the resetting rate is varied. Current measurements are signed; entropy-production observations alone generally do not distinguish reflected sources. Both singular and continuous Borel reset laws are allowed, provided there are no atoms on the interface itself. The stationary law is unique for every positive rate because the diffusion-with-reset generator is irreducible and resets occur at a positive rate.

## Proof

**1. Neumann resolvent and interface correction.** For \(\lambda=\sqrt{r/D}\), the Green kernel for the Neumann problem on \([0,L]\) is
\[
G_N(x,y)=\frac{\cosh(\lambda\min(x,y))\cosh(\lambda(L-\max(x,y)))}{D\lambda\sinh(\lambda L)}.
\]
It satisfies \((-D\partial_{xx}+r)G_N=\delta_y\), has zero derivatives at both endpoints, and has the correct derivative jump at \(x=y\). Therefore
\[
p_N(x)=r\int G_N(x,y)\,\mu(dy)
\]
solves the stationary source equation with reflecting endpoints. Writing \(c=\lambda L/2\), the unique homogeneous correction having outward derivatives corresponding to the unknown oriented flux \(J\) is
\[
h_J(x)=-\frac{J\sinh(\lambda(x-L/2))}{D\lambda\cosh c}.
\]
Indeed \(h_J'(0)=h_J'(L)=-J/D\). Thus \(p_r=p_N+h_J\). Integrating the differential equation gives \(\int_0^L p_r(x)\,dx=1\); also \(\int_0^L h_J(x)\,dx=0\).

**2. Endpoint jump.** Directly evaluating the Green function at the two sides of the cut gives
\[
p_N(L)-p_N(0)=
\frac{\lambda}{\cosh c}\int\sinh\big(\lambda(y-L/2)\big)\,\mu(dy).
\]
The homogeneous correction contributes
\[
h_J(L)-h_J(0)=-\frac{2J}{D\lambda}\tanh c.
\]
Impose \(J=\kappa[p_r(L)-p_r(0)]\) and solve the resulting scalar equation. This yields the displayed exact current transform. Its multiplier is strictly positive for \(D,L,\kappa,r>0\). Positivity of stationary endpoint densities follows from the positive resolvent of the irreducible diffusion with membrane and positive resetting; equivalently the one-dimensional maximum principle excludes a nonpositive stationary endpoint minimum.

**3. Complete equivalence classes.** Set \(z=y-L/2\) and let \(\delta=\mu-\nu\) be a finite signed measure on \((0,L)\). The signed-current curves agree precisely where
\[
F_\delta(\lambda)=\int\sinh(\lambda z)\,\delta(dy)=0.
\]
This is an entire function of the complex argument \(\lambda\), because \(|z|\le L/2\). A rate set with an accumulation point in \((0,\infty)\) yields a set of positive \(\lambda\)-values with an interior accumulation point, so the identity theorem gives \(F_\delta\equiv0\). Its Taylor coefficients show
\[
\int z^{2j+1}\,\delta(dy)=0\qquad\text{for every integer }j\ge0.
\]
By uniform polynomial approximation followed by antisymmetrization under \(z\mapsto-z\), odd polynomials are dense in the continuous functions that are odd about the midpoint. Hence \(\delta\) integrates every odd continuous function to zero. This is equivalent to \(\delta=R_*\delta\). Conversely reflection invariance annihilates every odd integrand, proving the complete if-and-only-if statement. Applying it to \(\nu=R_*\mu\) proves that identically zero current is equivalent to \(\mu=R_*\mu\).

**4. All admissible distributions with the same current.** For a probability measure \(\mu\), put \(a=(\mu-R_*\mu)/2\) and \(s=(\mu+R_*\mu)/2\). Both \(s\) and \(|a|\) are reflection-symmetric measures, \(a\) is antisymmetric, and \(\mu=s+a\). Positivity of both \(\mu=s+a\) and its reflection \(R_*\mu=s-a\) implies \(s\ge|a|\) as measures: on any Borel partition, the combined inequalities dominate the sums of absolute signed masses. Therefore \(m=|a|((0,L))\le s((0,L))=1\). If \(m<1\), write \(s=|a|+(1-m)\sigma\) with \(\sigma\) a symmetric probability measure. Conversely any such \(\sigma\) makes \(\mu=a+|a|+(1-m)\sigma\) a positive probability law with antisymmetric part \(a\), because \(|a|+a=2a_+\ge0\). If \(m=1\) the additional symmetric mass is forced to zero, yielding one admissible law. If \(m<1\), choosing different symmetric \(\sigma\) gives infinitely many different admissible laws on the nondegenerate interval. This establishes the complete positive-law fiber and its sharp uniqueness criterion.

**5. Finite measurements cannot suffice nonparametrically.** Fix any positive rates \(r_1,\ldots,r_k\). Choose \(k+1\) distinct offsets \(0<u_j<L/2\) and the paired points \(L/2\pm u_j\). The \(k\) by \(k+1\) matrix with entries \(\sinh(\sqrt{r_i/D}\,u_j)\) has a nonzero null vector \(a=(a_j)\). The signed atomic measure
\[
\xi=\sum_{j=1}^{k+1} a_j\left(\delta_{L/2+u_j}-\delta_{L/2-u_j}\right)
\]
has total mass zero and vanishing current contributions at every prescribed rate, but its antisymmetric part is nonzero. Starting with a strictly positive probability weight at every chosen atom and perturbing by \(\pm\varepsilon\xi\) for sufficiently small \(\varepsilon>0\) produces two legitimate, distinct reset distributions with equal observed currents. The equivalence classification of Step 3 ensures their full current curves differ at some other rate. Thus the accumulation-point hypothesis is sharp for arbitrary reset laws without finite-parametric priors.

**6. Entropic blindness and a nonsymmetric zero-current law.** The interfacial entropy production introduced in Bressloff's Eq. (4.5) is
\[
I_{\mathrm{int},\mu}(r)=J_\mu(r)\log\frac{p_r(L^-)}{p_r(0^+)}\ge0.
\]
The permeability law and strictly positive endpoint densities imply \(I_{\mathrm{int},\mu}(r)=0\) if and only if \(J_\mu(r)=0\). Under \(\mu\mapsto R_*\mu\), uniqueness and reflection symmetry give \(p_{r,R_*\mu}(x)=p_{r,\mu}(L-x)\), whence \(J_{R_*\mu}(r)=-J_\mu(r)\) and \(I_{\mathrm{int},R_*\mu}(r)=I_{\mathrm{int},\mu}(r)\). For a concrete asymmetric zero-current reset law at a chosen \(\lambda>0\), select unequal \(0<u,v<L/2\), positions \(L/2-u\) and \(L/2+v\), and assign probability
\[
q=\frac{\sinh(\lambda v)}{\sinh(\lambda u)+\sinh(\lambda v)}
\]
to the left point, with complementary probability to the right. Its relevant hyperbolic-sine moment is exactly zero, although it is not reflection symmetric. Thus one vanishing entropy/current observation does not certify a symmetric resetting rule.

**7. Small-rate calibration.** Taylor expansion yields \(F_\mu(\lambda)=\lambda\int(y-L/2)\,\mu(dy)+O(\lambda^3)\), while the current-transform denominator is \(1+\kappa L/D+O(\lambda^2)\). Since \(\lambda^2=r/D\), the small-rate slope follows, with no moment assumption beyond compact spatial support.

## Verification

An accompanying, separately executable Python script (`check_current.py`, NumPy 2 or later) performs deterministic checks of the exact endpoint Green function, permeability boundary law, reflected-current and reflected-entropy identities, positivity for tested measures, small-rate limits, asymmetric zero-current examples, and nonidentifiability under symmetric perturbation. An independent finite-volume discretization of the differential equation is checked against the exact transform for three parameter sets and successively refined meshes. It includes the half-cell membrane resistance when translating physical permeability to center-to-center grid conductance. Running the script produced `PASS 428 deterministic checks including probability-law fiber`.

The analytical proof, not numerical coverage, establishes the all-parameter statement. The code does not purport to invert measured noisy curves or prove that any existing literature lacks an equivalent theorem.

## Relationship to prior work

Bressloff (2024), particularly Eqs. (4.1), (4.5), (4.13), (4.20), and (4.22), establishes the forward stochastic-resetting membrane model, stationary density via superposition of point-source solutions, and the interface entropy-production formula. Those forward laws are **prior work**, not new here. The additional inverse question is: what can a scalar *signed boundary current observed as the reset rate varies* identify about an otherwise arbitrary reset-location distribution? The complete reflection-antisymmetric equivalence classes and positive-law fiber (including the exact uniqueness criterion), sharp distinction between finite rate sets and sets with an interior accumulation point, and entropic reflection-blindness theorem are the present deductions. They require transform injectivity and measure-level kernel arguments beyond merely stating the forward solution. No claim is made that the one-dimensional Green kernel or hyperbolic-sine transform itself was unknown.

Mori, Olsen, and Krishnamurthy (2023) treat entropy production of resetting processes with random reset locations on the line, without the semipermeable-ring boundary-current inverse data used here. Bressloff (2023) treats semipermeable screening of resetting in first-passage problems on a half-line and in spherical geometry, rather than ring stationary-flux tomography. The inverse result may be derivable from published forward Green representations by specialists; independent publication-priority review remains necessary.

## Limitations

All data are ideal exact population stationary currents across a continuous set of resetting rates, with \(D,L,\kappa\) known. Analytic continuation and moment inversion are generally ill-conditioned under noise; the theorem does not provide stable estimation rates. A flux curve cannot distinguish admissible symmetric changes to the reset law; in the extremal case of unit total-variation antisymmetry there is no such freedom, and the full source is recovered. The orientation of the asymmetry cannot be recovered from entropy production alone. Any single nonzero finite collection of rates is insufficient for arbitrary reset measures. The membrane is unbiased and the reset distribution remains fixed as the rate changes; spatially asymmetric permeability, reset rules conditioned on pre-reset location, finite-rate samples, unknown physical coefficients, and non-Poisson resetting are not covered. Interfacial entropy production is one contribution to the total irreversible cost and may vanish while resetting itself still produces entropy.

## References

1. P. C. Bressloff, “Entropy production for diffusion processes across a semipermeable interface,” *Physical Review Research* **6**, 023283 (2024), DOI: 10.1103/PhysRevResearch.6.023283; first public preprint arXiv:2402.16403 (2024-02-26). Full paper, Sec. IV, Eqs. (4.1), (4.5), (4.13), (4.20), (4.22).
2. F. Mori, K. Stølevik Olsen, and S. Krishnamurthy, “Entropy production of resetting processes,” *Physical Review Research* **5**, 023103 (2023), DOI: 10.1103/PhysRevResearch.5.023103; arXiv:2211.15372.
3. P. C. Bressloff, “Diffusion with stochastic resetting screened by a semipermeable interface,” *Journal of Physics A* **56**, 105001 (2023), DOI: 10.1088/1751-8121/acba63; arXiv:2211.12468.
