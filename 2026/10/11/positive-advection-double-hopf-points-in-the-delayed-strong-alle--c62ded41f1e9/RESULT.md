# Positive-advection double Hopf points in the delayed strong-Allee model
## Finding
Consider the delayed population equation
\\[
u_t=d u_{{xx}}-\\alpha u_x+r u(u-1)\\left(1-\\frac{{u(x,t-\\tau)}}{{K}}\\right),
\\]
on \\(0<x<L\\), with \\(d u_x(0,t)-\\alpha u(0,t)=-\\alpha K\\) and \\(u(L,t)=K\\). Fix \\(r=1\\), \\(K=4\\), and \\(L=8\\). There is an \\(\\varepsilon>0\\) such that, for every \\(0\\leq\\alpha<\\varepsilon\\), some pair \\((d,\\tau)\\) makes the linearization at \\(u=K\\) have exactly two distinct simple conjugate imaginary pairs, arising from spatial modes \\(n=1\\) and \\(n=2\\). No higher spatial mode is imaginary there.

At zero advection, set
\\[
x=\\frac{{d\\pi^2}}{{768}}.
\\]
Then the \\((n,j)=(1,1)\\) and \\((2,0)\\) Hopf branches meet at the unique \\(x_*\\in(1/25,1/9)\\) satisfying
\\[
G(x):=\\frac{{\\arccos(-x)+2\\pi}}{{\\sqrt{{1-x^2}}}}-\\frac{{\\arccos(-9x)}}{{\\sqrt{{1-81x^2}}}}=0.
\\]
Numerically,
\\[
x_*\\approx0.104159188955685,\\qquad d_*\\approx8.10511281578182,
\\]
\\[
\\tau_*\\approx2.66728502385129,
\\]
with imaginary frequencies approximately \\(2.98368191505141\\) and \\(1.04449958668851\\). The two Hopf curves cross transversely at this point, and the intersection persists for all sufficiently small positive advection rates.

Thus the published assertion that simultaneous variation of diffusion and delay cannot produce a Hopf--Hopf bifurcation in this model is false. The issue is that ordering the first stability boundary does not prevent a higher Hopf branch of one spatial mode from intersecting the first branch of another mode.

## Assumptions and scope
The parameters are \\(r=1\\), \\(K=4\\), \\(L=8\\), \\(d>0\\), \\(\\tau>0\\), and \\(\\alpha\\geq0\\). The conclusion concerns the constant equilibrium \\(u=K\\) and the spectrum of its linearization. The term “double Hopf” is used in the spectral sense of two distinct simple conjugate imaginary pairs at the same parameter point, with a transverse intersection of their Hopf curves in the \\((d,\\tau)\\) plane. No nonlinear double-Hopf normal-form coefficients are computed here.

The earliest verified public version of the motivating source was posted on 2025-12-03. Its peer-reviewed version lists MSC 35K57 and 37G15.

## Proof
Write
\\[
a=r(K-1)=3.
\\]
The source derives, for the spatial eigenvalues \\(\\mu_n\\), the characteristic equation
\\[
\\lambda+\\mu_n+a e^{-\\lambda\\tau}=0.
\\]
A purely imaginary root \\(\\lambda=i\\omega\\) exists exactly when \\(0<\\mu_n<a\\), with
\\[
\\omega_n=\\sqrt{{a^2-\\mu_n^2}},\\qquad
\\tau_n^{{(j)}}=\\frac{{\\arccos(-\\mu_n/a)+2j\\pi}}{{\\omega_n}},\\quad j=0,1,2,\\ldots .
\\]

For \\(\\alpha=0\\), the spatial problem has Neumann boundary condition at \\(0\\) and Dirichlet boundary condition at \\(L\\), hence
\\[
\\mu_n=d\\left(\\frac{{(2n-1)\\pi}}{{2L}}\\right)^2.
\\]
With \\(L=8\\) and \\(x=\\mu_1/a=d\\pi^2/768\\),
\\[
\\frac{{\\mu_1}}a=x,\\qquad \\frac{{\\mu_2}}a=9x,\\qquad \\frac{{\\mu_3}}a=25x.
\\]
The equality \\(\\tau_1^{{(1)}}=\\tau_2^{{(0)}}\\) is exactly \\(G(x)=0\\), where \\(G\\) is displayed above.

At \\(x=1/25\\),
\\[
\\frac{{\\arccos(-x)+2\\pi}}{{\\sqrt{{1-x^2}}}}>\\frac{{5\\pi}}2,
\\]
while
\\[
\\frac{{\\arccos(-9x)}}{{\\sqrt{{1-81x^2}}}}<\\frac{{\\pi}}{{\\sqrt{{1-81/625}}}}=\\frac{{25\\pi}}{{4\\sqrt{{34}}}}.
\\]
Since \\(5/2>25/(4\\sqrt{{34}})\\), one has \\(G(1/25)>0\\). As \\(x\\uparrow1/9\\), the second term tends to \\(+\\infty\\) while the first remains finite, so \\(G(x)\\to-\\infty\\). Therefore a root exists in \\((1/25,1/9)\\).

It is unique and transverse. Define
\\[
H_j(y)=\\frac{{\\arccos(-y)+2j\\pi}}{{\\sqrt{{1-y^2}}}}.
\\]
Then
\\[
H_j'(y)=\\frac1{{1-y^2}}+\\frac{{y(\\arccos(-y)+2j\\pi)}}{{(1-y^2)^{{3/2}}}}.
\\]
For \\(1/25\\leq x<1/9\\), \\(H_1'(x)<81/80+(\\pi/3)(81/80)^{{3/2}}<2.1\\), whereas
\\[
9H_0'(9x)>\\frac9{{1-81x^2}}\\geq\\frac{{5625}}{{544}}>10.
\\]
Hence \\(G'(x)<0\\) throughout this interval.

At the unique root, \\(\\mu_2<a<\\mu_3\\), so precisely the first two spatial modes can carry imaginary roots. Their frequencies are distinct because \\(\\mu_1<\\mu_2\\). Each imaginary root is simple: if the derivative of the characteristic function with respect to \\(\\lambda\\) vanished, then \\(a\\tau e^{-i\\omega\\tau}=1\\), which would force \\(\\sin(\\omega\\tau)=0\\); the imaginary-root equations instead give \\(\\sin(\\omega\\tau)=\\omega/a>0\\).

To pass from \\(\\alpha=0\\) to positive advection, write \\(\\phi=e^{{\\alpha x/(2d)}}y\\). The spatial eigenproblem becomes
\\[
y''+k^2y=0,\\qquad y'(0)=\\frac{{\\alpha}}{{2d}}y(0),\\qquad y(L)=0,
\\]
with
\\[
\\mu=d k^2+\\frac{{\\alpha^2}}{{4d}}.
\\]
Equivalently, the spatial frequencies solve
\\[
\\cos(kL)+\\frac{{\\alpha}}{{2dk}}\\sin(kL)=0.
\\]
At \\(\\alpha=0\\), each root \\(k_n=(2n-1)\\pi/(2L)\\) is simple. The implicit-function theorem therefore makes \\(k_n\\), and hence \\(\\mu_n\\) and the Hopf branches, smooth in \\((d,\\alpha)\\) near the double-Hopf point. Because the difference \\(\\tau_1^{{(1)}}-\\tau_2^{{(0)}}\\) has nonzero \\(d\\)-derivative there, the intersection continues uniquely to a smooth curve \\(d=d(\\alpha)\\) for all sufficiently small \\(\\alpha\\). The strict inequalities \\(\\mu_2<a<\\mu_3\\) persist, so the continued points still have exactly two distinct simple imaginary pairs.

## Verification
The standalone script `verify_double_hopf.py` bisects the scalar equation \\(G(x)=0\\), reconstructs \\(d_*\\), \\(\\tau_*\\), \\(\\mu_1\\), \\(\\mu_2\\), \\(\\mu_3\\), and the two frequencies, and substitutes both imaginary roots directly into the published characteristic equation. It is a numerical consistency check only; the existence, uniqueness, transversality, and positive-advection persistence are proved analytically above.

The replay gives `VERIFY_OK`, with characteristic residuals below \\(5\\times10^{{-15}}\\).

## Relationship to prior work
The motivating preprint and its peer-reviewed version derive the characteristic equation and all Hopf delay branches, but then assert that simultaneous variation of \\(d\\) and \\(\\tau\\) cannot yield Hopf--Hopf bifurcations. Their argument only excludes intersections on the first stability boundary; it does not compare higher branch indices across different spatial modes. The intersection constructed here is between \\(\\tau_1^{{(1)}}\\) and \\(\\tau_2^{{(0)}}\\), so it lies outside that boundary argument.

General delayed reaction--diffusion theory already permits double-Hopf points, including work of Du, Niu, Guo and Wei on delayed reaction--diffusion systems and Liu and Wei on a diffusive predator--prey system with strong Allee effect and two delays. Those papers concern different systems and boundary/parameter structures; they do not state the present same-model intersection or invalidate it by stronger coverage.

## Limitations
The result is local and spectral. It does not compute the four-dimensional center-manifold normal form, determine resonant versus nonresonant nonlinear unfolding, or classify nearby periodic, quasiperiodic, or chaotic dynamics. The continuation argument proves existence for sufficiently small positive \\(\\alpha\\) but does not give a sharp maximal advection interval. The numerical values displayed for the zero-advection point are reproducibility aids, not the proof.

## References
1. Y. Liu and X. Wei, “Hopf Bifurcation Analysis in a Reaction-Diffusion-Advection Model with Strong Allee Effect and Delay,” Preprints.org, posted 2025-12-03, doi:10.20944/preprints202512.0404.v1.
2. Y. Liu and X. Wei, “Hopf bifurcation analysis in a reaction-diffusion-advection model with strong Allee effect and delay,” AIMS Mathematics 11 (2026), 11559–11579, doi:10.3934/math.2026476.
3. Y. Du, B. Niu, Y. Guo and J. Wei, “Double Hopf bifurcation in delayed reaction-diffusion systems,” Journal of Dynamics and Differential Equations 32 (2020), 313–358, arXiv:1804.03775, doi:10.1007/s10884-018-9725-4.
4. Y. Liu and J. Wei, “Double Hopf bifurcation of a diffusive predator-prey system with strong Allee effect and two delays,” Nonlinear Analysis: Modelling and Control 26 (2021), 72–92, doi:10.15388/namc.2021.26.20561.
