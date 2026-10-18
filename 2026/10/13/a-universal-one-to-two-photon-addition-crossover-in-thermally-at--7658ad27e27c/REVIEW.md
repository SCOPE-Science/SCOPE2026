# Independent mathematical audit

## correctness

PASS

For exact normalized photon-added thermal Fock weights, summing Laguerre polynomials gives input characteristic e^{-(nbar+1/2)t}L_m((nbar+1)t). The thermal attenuator replaces this with e^{-a t}L_m(vt), a=1/2+eta*nbar+(1-eta)*nbar_b, v=eta(nbar+1). Fourier inversion gives the Laguerre Wigner radial profile, nonnegative for delta=v-a<=0, equivalent to eta<=(nbar_b+1/2)/(nbar_b+1). For delta>0, theta=delta/v in (0,1/2], radial negative regions y in (0,1) for m=1 and (2-sqrt2,2+sqrt2) for m=2; their exact Laplace integrals yield N1=(theta-1+e^-theta)/(1-theta) and N2=2e^-2theta/(1-theta)^2*(sqrt2*theta*cosh(sqrt2*theta)-sinh(sqrt2*theta)). For ratio R, d(log R)/dtheta=1/[theta(1-theta)]+mu1-mu2 > 4-(2+sqrt2)>0 because 0<mu1<1 and 2-sqrt2<mu2<2+sqrt2. R(0+)=0 and R(1/2)>1 give unique theta*=0.3013805517222; physical monotonic theta(eta) yields the seed threshold nbar*=1/(2theta*)-1=0.65903206807 and eta_* formula. Independent direct Laguerre negative-region quadrature at five theta values agreed with both formulas to <1e-12 and root=0.3013805517222024. Those checks are finite, the integral argument proves the global ordering.

## originality

PASS

Best-of-knowledge new exact 1-addition versus 2-addition integrated Wigner-negative volume crossover ordering and thermal-seed phase diagram. Li (2008) evaluated the single-addition negative volume; Marian–Ghiu–Marian (2012) give general photon-added Wigner-Laguerre profiles and positivity threshold, so neither fact is claimed new. Xu–Yuan (2019) use Wigner logarithmic negativity for photon-added thermal states under thermal reservoirs, an extremely plausible stronger covering source, but only abstract/first page material was accessible; it remains a material priority risk rather than automatic failure. The inspected source passages did not show the strict monotone R(theta) or universal theta_* phase diagram; no stronger pre-existing theorem was actually established by inspected material.

## value

PASS

Integrated Wigner negativity is a physically meaningful nonclassicality metric. The theorem answers the natural fixed-seed-and-channel protocol comparison: when a second heralded photon addition helps or hurts, with a sharp universal noise-scale crossover and exact conditions for its physical reachability. It does not measure energy-matched advantages, heralding rates, arbitrary squeezings or all photon numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
