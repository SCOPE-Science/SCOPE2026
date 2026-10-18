# Exact oscillatory instability from directed vaccination information on three epidemic patches

## Finding

Three homogeneous, demographically coupled epidemic patches can become oscillatory-linearly unstable solely because **current vaccination information is passed in one direction**, even when susceptible and infectious mobility is symmetric and no delayed information is used. We establish the exact threshold, a strict comparison with reciprocal information, increasing stabilization by symmetric migration, and a sharp three-patch minimum when migration is absent.

Let \(c=\mu+\beta i_*>0\), \(B=\beta i_*\gamma>0\), \(Z=\beta i_*\mu p'(i_*)>0\), \(h=c+6D\), and \(k=B+3cD+9D^2\) be defined below. Under cyclic one-directional information, the positive homogeneous endemic equilibrium is locally exponentially stable precisely when
\[
0<Z<Z_{\mathrm{dir}}(D)=\frac h3\bigl(\sqrt{h^2+12k}-h\bigr).
\]
At equality there is exactly one simple conjugate pair of imaginary linear eigenvalues of angular frequency
\[
\omega_{\mathrm{dir}}(D)=\frac{\sqrt3 Z_{\mathrm{dir}}(D)}{2h}>0,
\]
with all other eigenvalues strictly in the left half-plane. As \(Z\) increases through the threshold the conjugate pair moves strictly into the right half-plane, and there is exactly one unstable conjugate pair for every \(Z>Z_{\mathrm{dir}}(D)\).

For the reciprocal, direction-averaged information channel with *identical* epidemic parameters, homogeneous equilibrium, and symmetric mobility, the stability threshold is instead
\[
Z_{\mathrm{rec}}(D)=2k>Z_{\mathrm{dir}}(D).
\]
The reciprocal first instability is a **zero-real-eigenvalue** instability, not an oscillatory one. Thus a nonempty strict interval of signal strengths destabilizes the directed system while leaving the reciprocal system stable. The directed threshold is strictly increasing in \(D\ge0\) and obeys \(Z_{\mathrm{dir}}(D)/D^2\to12\) as \(D\to\infty\).

Among one- and two-patch homogeneous epidemic systems of the same form with no migration and **any nonnegative row-stochastic instantaneous information channel**, increasing the nonnegative vaccination-response slope cannot produce a nonzero-frequency imaginary eigenvalue crossing. Three patches are therefore necessary and sufficient for this instantaneous-information oscillatory mechanism in that class.

## Assumptions and scope

Index three patches cyclically by \(j\in\{0,1,2\}\); indices on information channels are understood modulo three. Let susceptible fractions \(s_j\) and infectious fractions \(i_j\) satisfy
\[
\begin{aligned}
\dot s_j&=\mu\bigl[1-p(i_{j+1})\bigr]-\mu s_j-\beta s_ji_j+D\sum_{\ell\ne j}(s_\ell-s_j),\\
\dot i_j&=\beta s_ji_j-\gamma i_j+D\sum_{\ell\ne j}(i_\ell-i_j).
\end{aligned}
\]
Here \(\mu,\nu,\beta>0\), \(\gamma=\mu+\nu\), \(D\ge0\), and \(p:[0,1]\to(0,1)\) is continuously differentiable near \(i_*\), with \(p'(i_*)>0\). The homogeneous endemic equilibrium \((s_*,i_*)\) is assumed to exist, satisfy \(s_*=\gamma/\beta\in(0,1)\), \(i_*\in(0,1-s_*)\), and obey
\[
\mu[1-p(i_*)]=\mu s_*+\gamma i_*.
\]
Symmetric population migration occurs between every pair with rate \(D\); only the **information channel** is oriented. The reciprocal comparison replaces \(p(i_{j+1})\) with \(p((i_{j+1}+i_{j-1})/2)\). These have the same endemic equilibrium and linear local response magnitude \(Z\).

The threshold class varies \(p'(i_*)\) while retaining its value \(p(i_*)\), thus preserving the equilibrium. Every \(Z>0\) can be realized by a smooth strictly increasing probability function (see the example below). Stability refers solely to eigenvalues of the six-state Jacobian, hence to **local exponential stability**; an imaginary crossing alone does not establish a nonlinear family or stability of periodic orbits.

## Proof

**1. Full linearization and modal factors.** Write perturbations \(u_j=s_j-s_*\), \(v_j=i_j-i_*\). On a mobility eigenmode \(u_{j+1}=\kappa u_j\), \(v_{j+1}=\kappa v_j\) with cyclic-shift eigenvalue \(\kappa\), the symmetric complete-graph mobility operator equals \(-3D\) on nonuniform modes and zero on the homogeneous mode. Using \(\beta s_*=\gamma\), the mode matrix is
\[
M_\kappa=\begin{pmatrix}-(c+3D)&-\gamma-\mu p'(i_*)\kappa\\\beta i_*&-3D\end{pmatrix}
\]
for nonuniform modes. Its characteristic polynomial is
\[
P_\kappa(\lambda)=\lambda^2+h\lambda+k+Z\kappa,
\]
with \(h=c+6D\), \(k=B+3cD+9D^2\) and \(B=\beta i_*\gamma\). The homogeneous mode has \(\kappa=1\) and no mobility, hence characteristic \(\lambda^2+c\lambda+B+Z\), strictly Hurwitz for every \(Z>0\). The other two cyclic-shift eigenvalues are \(\kappa_\pm=-1/2\pm i\sqrt3/2\). The resulting real spatial characteristic quartic is
\[
\bigl(\lambda^2+h\lambda+k\bigr)^2-Z\bigl(\lambda^2+h\lambda+k\bigr)+Z^2.
\]

**2. Unique oscillatory threshold and direction.** For \(\kappa_+=-1/2+i\sqrt3/2\), substitute \(\lambda=i\omega\) into \(P_{\kappa_+}=0\). The imaginary part gives \(\omega=-\sqrt3 Z/(2h)\); the real part gives
\[
k=\frac Z2+\frac{3Z^2}{4h^2}.
\]
For fixed \(D\ge0\) this equation has exactly one positive solution, the displayed \(Z_{\mathrm{dir}}\). The conjugate spatial mode gives the conjugate eigenvalue, with the opposite frequency sign. No nonuniform zero eigenvalue is possible for \(Z>0\), because \(k+Z\kappa_+\) has nonzero imaginary part. At \(Z=0\) all modes are strictly Hurwitz. Since roots of a polynomial depend continuously on coefficients, and the above is their only imaginary-axis crossing, the equilibrium is stable below the threshold. At the crossing the eigenvalue is simple because \(\partial_\lambda P_{\kappa_+}=h+2i\omega\ne0\), and
\[
\operatorname{Re}\frac{d\lambda}{dZ}
=\operatorname{Re}\frac{-\kappa_+}{h+2i\omega}
=\frac{h/2+3Z/(2h)}{h^2+3Z^2/h^2}>0.
\]
(The imaginary-root sign is \(\omega=-\sqrt3 Z/(2h)\).) Both conjugate crossing eigenvalues move rightward; the two other roots of the nonuniform quartic have real part \(-h\) at the crossing. This establishes the stated spectral count for all \(Z\ge0\) with no further crossings.

**3. Reciprocal-channel separation.** The reciprocal information matrix has eigenvalue \(1\) on uniform vectors and \(-1/2\) on each independent nonuniform mode. Consequently the spatial factor is \((\lambda^2+h\lambda+k-Z/2)^2\). It is Hurwitz precisely when \(Z<2k\). At \(Z=2k\) each nonuniform quadratic has one zero root, and above it one positive real root. The directed threshold identity gives
\[
2k=Z_{\mathrm{dir}}+\frac{3Z_{\mathrm{dir}}^2}{2h^2}>Z_{\mathrm{dir}},
\]
proving the strict interval of differing stability.

**4. Symmetric mobility stabilizes.** Define \(F(D,Z)=k-Z/2-3Z^2/(4h^2)\). For \(D\ge0\), \(Z>0\),
\[
\partial_D F=3c+18D+\frac{9Z^2}{h^3}>0,
\qquad
\partial_Z F=-\frac12-\frac{3Z}{2h^2}<0.
\]
Implicit differentiation at \(F(D,Z_{\mathrm{dir}}(D))=0\) gives \(Z'_{\mathrm{dir}}(D)>0\). Divide the positive-root formula by \(D^2\) and use \(h/D\to6\), \(k/D^2\to9\) to obtain \(Z_{\mathrm{dir}}(D)/D^2\to12\).

**5. Minimal patch count at zero mobility.** With one patch the perception matrix is \((1)\), hence the quadratic is strictly Hurwitz. For two patches every nonnegative row-stochastic perception matrix is \(K=\bigl(\begin{smallmatrix}a&1-a\\b&1-b\end{smallmatrix}\bigr)\) with \(a,b\in[0,1]\), and has real eigenvalues \(1\), \(a-b\). At \(D=0\), every eigenmode has characteristic \(\lambda^2+c\lambda+B+Z\eta\) with real \(\eta\). Since \(c>0\), a nonzero imaginary root would have imaginary part \(c\omega\ne0\), a contradiction. (Real stationary destabilization is possible if \(\eta<0\).) Thus the directed oscillatory crossing requires at least three patches, achieved by the directed cyclic channel above.

**6. Realizable positive-parameter witness.** Take \(\mu=\nu=1\), \(\gamma=2\), \(\beta=6\), \(s_*=1/3\), \(i_*=1/12\), and define for any \(Z>0\)
\[
p_Z(m)=\frac1{1+\exp[-8Z(m-1/12)]}.
\]
Then \(p_Z(i_*)=1/2\) and \(p_Z'(i_*)=2Z\), giving exactly \(c=3/2\), \(B=1\), and the designated \(Z=\beta i_*\mu p_Z'(i_*)\). At \(D=0\),
\[
Z_{\mathrm{dir}}=\frac{\sqrt{57}-3}{4}<\frac32<2=Z_{\mathrm{rec}}.
\]
Thus at \(Z=3/2\), the directed system has exactly one unstable conjugate eigenpair and the reciprocal system is strictly stable, with every epidemiological rate positive and \(0<p_Z(m)<1\).

## Verification

The standalone `verify.py` uses Python, SymPy and NumPy. It differentiates the original six equations directly for both information channels and checks their complete characteristic polynomials symbolically; verifies endemic balance, sigmoid slope, threshold identity, imaginary crossing, the zero-migration exact example, transversality, two-patch matrix spectrum, and 24 direct six-state eigenvalue tests across the threshold. The script reports a successful run when invoked as `python verify.py`. The general theorem follows from the proof above, not from the finite sample checks.

## Relationship to prior work

Banerjee, Ghosh, Manfredi and d'Onofrio (2023) introduced spatial and temporal nonlocal vaccination information in an SIR model. Their general dispersion equation already exhibits a Fourier multiplier of an information kernel, and their symmetric-kernel, no-memory analysis treats stationary Turing thresholds. The present nonreciprocal three-patch construction specializes a related dispersion mechanism, but establishes a concrete **oscillatory** sharp threshold with no temporal memory, its strict reciprocal comparison, a mobility-dependent law, and a minimum-patch boundary. The general modal-reduction technique is not claimed as new.

Asllani and collaborators (2014) developed directed-network pattern-instability theory from complex **mobility-Laplacian** spectra, including oscillatory modes. Zheng and collaborators (2022) analyzed directed epidemiological movement networks and delays. Here the mobility is reciprocal and the only directed component is vaccination-information acquisition; neither prior result directly states the particular epidemic theorem or directed-versus-reciprocal thresholds. Related nonlocal-feedback epidemic literature includes a 2024 SIS paper about traveling waves, and a 2025 nonlocal asymmetric-kernel wave-stability study; the accessible evidence was insufficient to exclude all implicit broader-priority results. No general claim of having invented directed-network oscillatory instabilities is made.

## Limitations

The result is a local linear stability theorem, **not** a nonlinear Hopf bifurcation or guaranteed traveling-wave solution. It requires a homogeneous endemic state, three symmetric-mobility patches, synchronous instantaneous observations, an increasing vaccination response, and unchanged channel-specific vaccination-response magnitude in the comparison. The two-patch minimality statement assumes zero migration and homogeneous parameters. The exact threshold is particular to the cyclic/reciprocal three-patch information matrices; the proof does not cover arbitrary directed sensing graphs. Source priority is not independently certified, and related 2024/2025 work was not fully accessible.

## References

1. M. Banerjee, S. Ghosh, P. Manfredi, A. d'Onofrio (2023), *Spatio-temporal chaos and clustering induced by nonlocal information and vaccine hesitancy in the SIR epidemic model*, arXiv:2305.02191 (first public 2023-02-06); DOI: 10.1016/j.chaos.2023.113339. https://arxiv.org/abs/2305.02191
2. M. Asllani, J. D. Challenger, F. S. Pavone, L. Sacconi, D. Fanelli (2014), *The theory of pattern formation on directed networks*, Nature Communications 5, 4517. DOI: 10.1038/ncomms5517. https://www.nature.com/articles/ncomms5517
3. Q. Zheng, J. Shen, L. Zhou, L. Guan (2022), *Turing pattern induced by the directed ER network and delay*, Mathematical Biosciences and Engineering. DOI: 10.3934/mbe.2022553. https://www.aimspress.com/article/doi/10.3934/mbe.2022553
4. M. Banerjee, V. Volpert, P. Manfredi, A. d'Onofrio (2024), *Behavior-induced phase transitions with far from equilibrium patterning in a SIS epidemic model: Global vs non-local feedback*, Physica D 469, 134316. DOI: 10.1016/j.physd.2024.134316.
5. Y.-R. Yang, K.-W. Mu, Y.-L. Yang (2025), *Stability of monostable waves for a class of epidemic system with asymmetry and nonlocal effects*, International Journal of Biomathematics. DOI: 10.1142/S1793524525501396.
