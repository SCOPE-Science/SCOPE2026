# Sharp one-to-three peak transition for three geometric Debye relaxations

## Finding

For equal-strength dielectric Debye relaxation processes with geometrically spaced relaxation times, the loss profile changes from one peak to precisely three peaks at a sharp algebraic separation ratio. More precisely, let \(\tau_0>0\), \(\Delta\varepsilon>0\), and \(r>1\), and define the positive-frequency loss
\[
L_r(\omega)=\Delta\varepsilon\sum_{j=-1}^{1}\frac{\omega\tau_0r^j}{1+(\omega\tau_0r^j)^2},\qquad \omega>0.
\]
Set \(r_*=4+\sqrt{15}\) and \(c=(r+r^{-1})/2\).

**Sharp mode count.** For \(1<r\le r_*\), the only local maximum is the strict global maximum at \(\omega=\tau_0^{-1}\). When \(r=r_*\), two additional horizontal stationary shoulders exist but they are not extrema. For \(r>r_*\), there are exactly three strict local maxima and exactly two strict local minima. The middle maximum is at \(\omega=\tau_0^{-1}\). The other extrema are explicitly determined as follows. Define
\[
y_\pm=\frac{(c^2-1)\big(c-1\pm\sqrt{c(c-4)}\big)}{2c+1},\qquad
s_\pm=\operatorname{arcosh}\sqrt{y_\pm}.
\]
For \(r>r_*\), the two minima are at \(\omega=\tau_0^{-1}e^{\pm s_-}\) and the two outer maxima are at \(\omega=\tau_0^{-1}e^{\pm s_+}\), where \(0<s_-<s_+\). The profile is reciprocal in frequency: \(L_r(\omega)=L_r(\tau_0^{-2}/\omega)\).

**Bifurcation and high-contrast asymptotics.** Writing \(c=4+\delta\) with \(\delta\downarrow0\), the emerging stationary points on the positive log-frequency half-axis satisfy
\[
s_\pm=\operatorname{arcosh}\sqrt5\ \pm\frac{\sqrt5}{6}\sqrt\delta+O(\delta).
\]
As \(r\to\infty\), the positive-log-frequency minimum and maximum satisfy
\[
s_- =\tfrac12\log r+o(1),\qquad s_+=\log r+o(1),\qquad
L_r(\tau_0^{-1}e^{s_-})\sim\frac{2\Delta\varepsilon}{\sqrt r}.
\]
These statements concern the exact response model, not noisy or instrumentally broadened observations.

## Assumptions and scope

Each of three independent linear-response Debye processes has the same *dielectric strength* \(\Delta\varepsilon\) and a distinct relaxation time from \(\{\tau_0/r,\tau_0,\tau_0r\}\). Angular frequency is strictly positive. The model is a phenomenological sum with no coupling between relaxors, no non-Debye broadening, and no independent loss background. Peak count is invariant under positive rescaling of amplitude and frequency.

## Proof

Put \(t=\log(\omega\tau_0)\), \(a=\log r>0\), and \(c=\cosh a>1\). The elementary identity \(e^u/(1+e^{2u})=\tfrac12\operatorname{sech}u\) gives
\[
L_r(\omega)=\frac{\Delta\varepsilon}{2}g_a(t),\qquad
g_a(t)=\operatorname{sech}(t-a)+\operatorname{sech}t+\operatorname{sech}(t+a).
\]
In particular, \(g_a\) is even. For \(z=\cosh t\ge1\), the addition identity for hyperbolic cosines reduces the three-term sum to
\[
g_a(t)=G_c(z),\qquad
G_c(z)=\frac1z+\frac{2cz}{z^2+c^2-1}.
\]
With \(h^2=c^2-1>0\), direct differentiation yields
\[
G_c'(z)=-\frac1{z^2}+\frac{2c(h^2-z^2)}{(z^2+h^2)^2}
=-\frac{h^4Q_c(z^2/h^2)}{z^2(z^2+h^2)^2},
\]
where \(Q_c(u)=(1+2c)u^2+2(1-c)u+1\). Its discriminant is
\[
\operatorname{disc}(Q_c)=4c(c-4).
\]
For \(1<c<4\), \(Q_c(u)>0\) at every real \(u\). At \(c=4\), the polynomial is nonnegative and vanishes only at \(u=1/3\), corresponding to \(z^2=5\); its double zero does not reverse the derivative sign. Thus \(G_c\) strictly decreases for \(z\ge1\), aside from an isolated horizontal tangent at the threshold. Since \(z=\cosh t\) increases strictly for \(t>0\), this establishes unimodality and the threshold shoulders.

For \(c>4\), \(Q_c\) has two positive simple roots, corresponding to the squared \(z\)-coordinates \(y_-<y_+\) displayed above. Both exceed one. Indeed \(G_c'(1)=-(c^3-2c^2+4)/c^3<0\), because \(c^3-2c^2+4=(c-2)^2(c+2)+4(c-1)>0\). Also \(y_+>5\) for \(c>4\), and if \(y_-\le1<y_+\) the derivative would be nonnegative at \(z=1\), a contradiction; equality is excluded because \(G'_c(1)<0\). The sign of \(-Q_c\) changes from negative to positive to negative across \(y_-,y_+\), proving one minimum followed by one maximum on the positive half-axis. Even symmetry supplies the negative half-axis; strict curvature at the simple roots makes these four extrema nondegenerate. At \(t=0\), \(g_a''(0)=G_c'(1)<0\), so the central peak always remains strict. This exhausts all extrema because the derivative has no other real zeros.

The threshold equation \(c=4\) is \(r+r^{-1}=8\), and the root greater than one is exactly \(r_*=4+\sqrt{15}\). For \(c=4+\delta\), expand \(\sqrt{c(c-4)}=2\sqrt\delta+O(\delta^{3/2})\) and \(y_\pm=5\pm(10/3)\sqrt\delta+O(\delta)\). Since the derivative of \(\operatorname{arcosh}\sqrt y\) at \(y=5\) is \(1/(4\sqrt5)\), the asserted square-root splitting follows. Finally, with \(c=(r+r^{-1})/2\), expansion gives \(y_-=r/4+O(1)\) and \(y_+=r^2/4+O(r)\). Taking inverse hyperbolic cosines yields the positions. Evaluating the exact three-secant sum at \(s_-\sim(\log r)/2\), the central and upper-frequency components each contribute \(2/\sqrt r+o(r^{-1/2})\) to \(g_a\), while the third is smaller. Multiplication by \(\Delta\varepsilon/2\) gives \(2\Delta\varepsilon/\sqrt r\). This completes the proof.

## Verification

The accompanying standalone Python file `verify.py` reconstructs the loss and its derivative directly from the three original Debye terms, compares them to the rationalized expressions, independently locates critical points by grid bracketing and bisection, and tests the transition signs and asymptotic laws. It completed 506 comparisons, returning `VERIFY_OK checks=506`. These finite computations check implementations and selected parameter values; the quadratic-discriminant proof establishes the universal claims for the full continuous range.

## Relationship to prior work

Hoffman and Axilrod (1957) construct multi-relaxation dielectric-loss profiles from polar-rotator lattices and give a sufficient condition for **two** well-separated loss regions; their model is not this equal-strength, three-geometric-time classification. Ribeiro and Vieira (2003) explicitly discuss sums of Debye relaxors, emphasizing physical limitations of the uncoupled model and alternative factorized response forms; the inspected source motivates but does not give the sharp three-peak transition. Došlá (2009) treats mixtures of **two** unimodal densities and does not supply a three-component criterion. Hansen et al. (2016) describe experimentally relevant overlapping Debye components, not the equal-geometric triple model. The reduction to a three-component hyperbolic-secant mixture and the elementary quadratic analysis here are disclosed to clarify how this specialized result follows from known functional identities. Novelty is assessed against examined material rather than established by a failed search.

## Limitations

The classification is restricted to exactly three **equal-strength** Debye processes whose time constants form a geometric progression. Arbitrary positive amplitudes, unequal logarithmic spacings, physically coupled relaxations, distributions of activation energies, complex non-Debye response functions, finite-resolution measurements, and experimental identifiability are not addressed. The critical ratio is a mathematical resolvability boundary for this idealized loss curve, not a universal experimental threshold. An earlier specialist derivation of this precise symmetric three-component formula may exist despite the examined literature.

## References

1. J. D. Hoffman and B. M. Axilrod, "Theory of Dielectric Relaxation for the Three-Dimensional Polar Rotator: Lattice Models Leading to Bimodal Loss Curves," *Journal of Research of the National Bureau of Standards* **58** (1957), 61–73. https://upload.wikimedia.org/wikipedia/commons/5/5a/Theory_of_dielectric_relaxation_for_the_three-dimensional_polar_rotator-_Lattice_models_leading_to_bimodal_loss_curves_%28IA_jresv58n2p61%29.pdf
2. J. L. Ribeiro and L. G. Vieira, "The factorized form for dielectric relaxation," *European Physical Journal B* **36** (2003), 21–26; first published online 19 November 2003. https://doi.org/10.1140/epjb/e2003-00313-2
3. Š. Došlá, "Conditions for bimodality and multimodality of a mixture of two unimodal densities," *Kybernetika* **45** (2009), 279–292. https://dml.cz/bitstream/handle/10338.dmlcz/140075/Kybernetika_45-2009-2_6.pdf
4. J. S. Hansen and collaborators, "Identification of structural relaxation in the dielectric response of water," arXiv:1603.00725 (posted 2 March 2016). https://arxiv.org/abs/1603.00725
