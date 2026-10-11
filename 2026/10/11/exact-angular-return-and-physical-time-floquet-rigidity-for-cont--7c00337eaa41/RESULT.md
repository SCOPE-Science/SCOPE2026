# Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles

## Finding

Fix any integer \(p\ge1\). For the entire class of contracting homogeneous star-node flows with nowhere-vanishing angular drift, the exact angular Poincaré return map is affine in the radial power \(v=r^{2p}\). More significantly, the **original physical-time period** and the **transverse Floquet multiplier** of the unique attracting cycle obey the rigid relation

\[
T_\lambda=-\frac1\lambda\int_0^{2\pi}\frac{f(\theta)}{|g(\theta)|}\,d\theta,\qquad
\rho=\exp(-2p\lambda T_\lambda),\qquad
\frac{\log\rho}{T_\lambda}=-2p\lambda.
\]

Every nonzero orbit obeys the same exact one-revolution relaxation ratio \(\rho\), not merely the infinitesimal Floquet linearization. There is a noncircular, anisotropic cubic family whose physical-time period and multiplier do not change as anisotropy varies.

## Assumptions and scope

Let \(Q:\mathbb R^2\to\mathbb R^2\) be a real homogeneous polynomial map of odd degree \(2p+1\), with \(p\ge1\), and let \(\lambda>0\). Let \(J(x,y)=(-y,x)\) and \(u_\theta=(\cos\theta,\sin\theta)\). Assume **strict radial contraction** and **strict angular rotation**:

\[
 f(\theta)=\langle u_\theta,Q(u_\theta)\rangle<0,\qquad
 g(\theta)=\langle Ju_\theta,Q(u_\theta)\rangle\ne0
 \quad\text{for every }\theta\in\mathbb R.
\]

All intervals, integrals, returns and periods use the original, unrescaled physical time of \(\dot z=\lambda z+Q(z)\). The continuous nonzero function \(g\) has one global sign \(\sigma\in\{-1,1\}\). Let \(s=\sigma\theta\) (modulo \(2\pi\)), and write \(F(s)=f(\sigma s)\), \(G(s)=|g(\sigma s)|>0\). Define

\[
 a(s)=\frac{2pF(s)}{G(s)},\qquad b_\lambda(s)=\frac{2p\lambda}{G(s)},\qquad
 H(s)=\int_0^s a(w)\,dw.
\]

The positive constants required below are

\[
\rho=e^{H(2\pi)},\qquad
B_\lambda=\int_0^{2\pi}e^{H(2\pi)-H(u)}b_\lambda(u)\,du.
\]

Both \(\rho\) and \(B_\lambda\) are independent of the initial point, and \(0<\rho<1\), \(B_\lambda>0\).

## Proof

**Polar reduction and global well-posedness.** Writing \(z=r u_\theta\) for \(r>0\), homogeneity gives

\[
\dot r=\lambda r+f(\theta)r^{2p+1},\qquad
\dot\theta=g(\theta)r^{2p}.
\]

The strict bounds \(f\le-c<0\) and \(f\ge-C\) imply that positive solutions remain positive at every finite forward time and cannot blow up in finite forward time. Comparison with scalar logistic-type equations also keeps them in a positive, bounded annulus depending on their initial radius. As \(g\) is bounded away from zero, every forward trajectory with \(r(0)>0\) crosses every oriented angular section repeatedly in finite physical time.

**Global affine angular return.** Put \(v=r^{2p}\). Differentiation with respect to \(s\) is legitimate along every nonzero trajectory and gives the **exact** scalar linear equation

\[
\frac{dv}{ds}=\frac{2p(\lambda+F(s)v)}{G(s)}=a(s)v+b_\lambda(s).
\]

Variation of constants yields, for \(s\ge0\),

\[
v(s)=e^{H(s)}v(0)+\int_0^s e^{H(s)-H(u)}b_\lambda(u)\,du.
\]

At \(s=2\pi\), this is the whole positive-section Poincaré map \(P_\lambda(v)=\rho v+B_\lambda\). Since \(0<\rho<1\), the unique fixed radius power is \(v_*=B_\lambda/(1-\rho)>0\). It produces a smooth, once-around periodic orbit; no other periodic orbit can exist because any periodic orbit must close at a fixed point of some positive iterate of the strict affine contraction. For every \(v_0>0\) and integer \(k\ge0\),

\[
 v_k-v_*=\rho^k(v_0-v_*).
\]

The explicit variation-of-constants formula bounds the difference between any two solutions at intermediate angles by a fixed multiple of their initial radial-power difference. Hence all positive-radius solutions converge uniformly by turns to the periodic graph, establishing attraction globally outside the repelling origin. This assertion concerns convergence to the cycle as a set, not equal physical-time phase convergence.

**Exact physical-time period.** On the periodic graph, the logarithmic-radius derivative per angular increment is

\[
\frac{d\log r}{ds}=\frac{\lambda}{G(s)v(s)}+\frac{F(s)}{G(s)}.
\]

Integrating over one revolution gives zero on the left. Since \(dt/ds=1/[G(s)v(s)]\), the first term integrates to \(\lambda T_\lambda\). Thus

\[
\lambda T_\lambda=-\int_0^{2\pi}\frac{F(s)}{G(s)}\,ds
=-\int_0^{2\pi}\frac{f(\theta)}{|g(\theta)|}\,d\theta.
\]

The period is minimal: a positive polar radius can return to its original planar point only after an integer number of full angular rotations, and the fixed graph makes one rotation the first return.

**Exact Floquet rigidity.** Differentiating the global section map gives the transverse Floquet multiplier \(\rho\). Its defining integral is \(\log\rho=2p\int F/G\). Combining with the physical-time identity proves

\[
\rho=e^{-2p\lambda T_\lambda},\qquad
 \chi_\perp=\frac{\log\rho}{T_\lambda}=-2p\lambda.
\]

The other Floquet multiplier is \(1\), corresponding to the tangent flow direction. These identities are exact for every permitted polynomial and do not require approximation or perturbation theory. For fixed \(Q\), \(B_\lambda\) is linear in \(\lambda\), hence the invariant graph's radial power scales linearly with \(\lambda\), while \(\rho\) stays fixed and \(T_\lambda\) scales as \(1/\lambda\).

**A noncircular isoperiodic cubic family.** For \(p=1\), fix \(a>|\varepsilon|\), \(\omega>0\), and define

\[
Q(x,y)=-\bigl[a(x^2+y^2)+\varepsilon(x^2-y^2)\bigr](x,y)
+\omega(x^2+y^2)(-y,x).
\]

Its polar data are \(f(\theta)=-a-\varepsilon\cos(2\theta)\) and \(g(\theta)=\omega\), so the hypotheses hold for every such \(\varepsilon\). The angular average of the cosine vanishes, giving

\[
 T_\lambda=\frac{2\pi a}{\lambda\omega},\qquad
 \rho=e^{-4\pi a/\omega}.
\]

If \(\varepsilon\ne0\), no positive constant-radius orbit is possible: a constant radius would require \(\lambda=(a+\varepsilon\cos(2\theta))r^2\) at every angle, an impossibility. The attracting periodic orbit is therefore genuinely noncircular while both measured quantities remain invariant under anisotropy.

## Verification

The standalone script `check.py` integrates the exact radial-power angular equation using fourth-order Runge–Kutta quadrature for two admissible noncircular cubic examples. It independently checks the affine section map, the exact multiplier and the original-time period against the proved formulas. Run it with `python3 check.py`; it prints `CHECK_OK` when all checks pass. The numerical experiment tests examples only. The proof of the universal and infinite-family statements is the analytic calculation above, independent of finite numerical tests.

## Relationship to prior work

Alarcón, Castro and Labouriau prove existence and global attraction of the invariant circle under radial contraction and classify the cases where it is a periodic orbit or an equilibrium polycycle. The earlier Bendjeddou–Llibre–Salhi paper establishes integrability and existence/nonexistence criteria for homogeneous star-node systems. The broader Alarcón–Castro–Labouriau classification of homogeneous nonlinearities also gives a signed integral criterion for the existence of a limit cycle. Those **qualitative existence, uniqueness and hyperbolicity conclusions are not proposed as new**.

The quantitative contribution here is the global affine angular return in a specified physical radial coordinate, the exact original-time period identity, the universal transverse Floquet exponent, and the noncircular isoperiodic cubic example. The signed integral from earlier existence criteria appears in these formulas, but its quantitative identification with physical period and Floquet decay is a distinct statement.

## Limitations

The theorem requires strict radial contraction and a nowhere-zero angular factor. It does not classify flows with angular equilibria or polycycles, does not describe backward completeness, and makes no claim for nonhomogeneous perturbations or variable linear parts. The exact contraction ratio is per **angular revolution**, not per fixed physical-time interval away from the limit cycle. The 2013 integrability paper could not be inspected in complete text, leaving a genuine risk that related quantitative consequences may be implicit or explicitly established there. Neither absolute publication priority nor independent validation is claimed.

## References

1. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first public version, 29 July 2023), and *Research in the Mathematical Sciences* 11, article 21 (2024), DOI:10.1007/s40687-024-00427-0. Full text: https://link.springer.com/article/10.1007/s40687-024-00427-0.
2. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Qualitative planar dynamics with star nodes and homogeneous nonlinearities: beyond Hilbert's 16th problem*, arXiv:2106.07516 (first public version, 14 June 2021); see the broader classification and its limit-cycle existence criterion.
3. A. Bendjeddou, J. Llibre, T. Salhi, *Dynamics of the polynomial differential systems with homogeneous nonlinearities and a star node*, *Journal of Differential Equations* 254 (2013), 3530–3537, DOI:10.1016/j.jde.2013.01.032.
