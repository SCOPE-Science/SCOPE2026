# A conserved sphere forces two neutral Lyapunov exponents in the Lu–Yu–Zhu flow
## Finding
Consider the smooth four-dimensional system
\[
\dot x=az,\qquad \dot y=bw,\qquad \dot z=-ax+cxw,\qquad \dot w=-by-cxz,
\]
with real \(c\) and nonzero \(a,b\). Define
\[
H(x,y,z,w)=x^2+y^2+z^2+w^2.
\]
Then \(H\) is conserved exactly. The origin is the only equilibrium. Consequently every non-equilibrium ergodic invariant probability measure is carried by one sphere \(H=R^2\), \(R>0\), and its Lyapunov spectrum in the ambient four-dimensional tangent bundle is
\[
\{\lambda,0,0,-\lambda\},\qquad \lambda\ge 0,
\]
counting multiplicity. Thus this vector field cannot possess two positive asymptotic Lyapunov exponents on a nonzero energy sphere.

For the published example \((a,b,c)=(12,8,8)\) with initial condition \((1,1.1,3.2,3.3)\), the orbit stays exactly on \(H=23.34\). The source reports the numerical spectrum \((0.004260,0.005551,-0.002850,-0.006961)\) and interprets its two positive entries as hyperchaos. The exact argument above shows that, for the stated ODE, two entries of the true asymptotic spectrum must instead be zero.

## Assumptions and scope
The statement concerns the continuous-time ODE exactly as printed in Lu, Yu and Zhu (2021), with \(a\ne0\), \(b\ne0\), and arbitrary real \(c\). It concerns Oseledec Lyapunov exponents of non-equilibrium ergodic invariant probability measures on the exact flow. It does not assert a numerical value for the remaining exponent \(\lambda\), does not classify whether a given orbit is periodic, quasiperiodic, or chaotic on its invariant sphere, and does not analyze the discretized Runge–Kutta sequence used by the encryption algorithm.

The primary classification is MSC2020 \(37\mathrm{C}10\), dynamics induced by flows and semiflows.

## Proof
Differentiate \(H\) along a classical trajectory:
\[
\begin{aligned}
\dot H
&=2x(az)+2y(bw)+2z(-ax+cxw)+2w(-by-cxz)\\
&=0.
\end{aligned}
\]
Thus each sphere \(S_R^3=\{H=R^2\}\) is invariant. If \(a,b\ne0\), stationarity gives successively \(z=0\), \(w=0\), \(x=0\), and \(y=0\), so the origin is the unique equilibrium. Therefore the vector field is nowhere zero on every \(S_R^3\) with \(R>0\).

Let \(\phi_t\) denote the flow. The identity
\[
D\phi_t(p)F(p)=F(\phi_t(p))
\]
provides an invariant tangent line inside \(T_pS_R^3\). Compactness of \(S_R^3\) and absence of equilibria bound \(\lVert F\rVert\) above and away from zero there, so this tangent direction has Lyapunov exponent zero.

Conservation of \(H\) gives
\[
dH_{\phi_t(p)}\circ D\phi_t(p)=dH_p.
\]
On \(S_R^3\), \(\lVert dH\rVert=2R\) is constant. Hence the one-dimensional quotient cocycle transverse to \(TS_R^3\), normalized by \(dH\), also has exponent zero. This quotient exponent is distinct from the flow-direction exponent inside \(TS_R^3\), so zero occurs with multiplicity at least two.

Finally,
\[
\nabla\!\cdot F=0.
\]
Liouville's formula therefore gives \(\det D\phi_t=1\), and the sum of all four Lyapunov exponents is zero. Removing the two zero exponents leaves two exponents whose sum is zero; ordering them gives \(\lambda\) and \(-\lambda\) with \(\lambda\ge0\). This proves the stated spectrum and excludes two positive asymptotic exponents.

## Verification
The accompanying `verify.py` symbolically reconstructs the vector field, differentiates \(H\), computes the divergence, checks the source example's exact energy, and checks that the published four numerical values contain two positive entries while summing to zero. Running `python3 verify.py` returns `VERIFY_OK`.

The Lyapunov-multiplicity conclusion is proved analytically above rather than inferred from a finite numerical integration.

## Relationship to prior work
Lu, Yu and Zhu introduce the ODE, verify zero ambient divergence, and report two positive numerical Lyapunov exponents, using them to classify the system as conservative hyperchaotic. Their full text does not state the conserved quadratic \(H\), and searches of the article for “first integral”, “invariant”, and the quadratic expression found no such result. The exact first integral is stronger than zero divergence: it confines each orbit to a three-sphere and forces a second neutral Lyapunov direction in addition to the usual flow direction.

Targeted searches for the article title, DOI, exact equations, the quadratic integral, and formulations combining a regular first integral with two neutral Lyapunov exponents did not identify a published result establishing this claim for the Lu–Yu–Zhu system. The closest retrieved literature concerned different flows or general conservative/first-integral mechanisms and therefore does not imply the system-specific statement here.

## Limitations
The conclusion is about the exact continuous-time equations, not finite-time Lyapunov estimates. A finite-time algorithm can return small nonzero approximations to mathematically zero exponents, and a non-structure-preserving numerical integrator need not conserve \(H\) exactly. The result also does not show that the remaining exponent \(\lambda\) is positive; chaos on an invariant sphere is neither proved nor disproved here. No claim is made about the cryptographic security of the full image-encryption construction independently of its stated hyperchaos rationale.

## References
1. Q. Lu, L. Yu, C. Zhu, “A New Conservative Hyperchaotic System-Based Image Symmetric Encryption Scheme with DNA Coding,” *Symmetry* 13 (2021), 2317. DOI: 10.3390/sym13122317. Published 2021-12-04.
2. MSC2020, class \(37\mathrm{C}10\): dynamics induced by flows and semiflows.
