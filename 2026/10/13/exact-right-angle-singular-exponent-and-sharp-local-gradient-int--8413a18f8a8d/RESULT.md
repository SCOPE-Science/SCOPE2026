# Exact right-angle singular exponent and sharp local gradient-integrability threshold for a Lorentz-scalar Dirac shell
## Finding
For the Lorentz-scalar \(\delta\)-shell Dirac operator on a straight wedge of opening \(\omega=\pi/2\), with the coupling convention \(0<|\mu|<1\) of Pizzichillo--Van Den Bosch, write
\[
t=\frac{2|\mu|}{1+\mu^2}.
\]
The singular angular exponent \(\lambda_0^L\in(-1/2,0)\) appearing in the most regular self-adjoint extension is
\[
\lambda_0^L(\mu)=-\frac12+\frac{2}{\pi}\arcsin\!\left(\frac{\sqrt{t^2+8}-t}{4}\right).
\]
It is strictly decreasing in \(|\mu|\), with endpoint limits \(0\) as \(|\mu|\downarrow0\) and \(-1/6\) as \(|\mu|\uparrow1\).

Define
\[
p_c(\mu)=\frac{2}{1-\lambda_0^L(\mu)}.
\]
Then \(12/7<p_c(\mu)<2\), and on any bounded neighborhood of the corner the distinguished domain \(\mathcal D(D_0^L)\) is contained componentwise in \(W^{1,p}\) for every \(1\le p<p_c(\mu)\), but is not contained in \(W^{1,p}\) for any \(p\ge p_c(\mu)\). At the endpoint \(p=p_c(\mu)\), the gradient of the corner generator diverges logarithmically.

## Assumptions and scope
The operator, coupling \(\mu\), cutoff \(\phi\), angular functions \(f_k^L\), and exponents \(\lambda_k^L\) are those of arXiv:1902.05010v2. The claim concerns the straight-wedge model with \(\omega=\pi/2\); the same angular equation occurs for \(\omega=3\pi/2\) because it depends on \(|\pi-\omega|\). The Sobolev statement is local and componentwise on the two sides of the shell. No claim is made that the identical sharp cutoff persists for arbitrary curvilinear corners without further analysis.

## Proof
Definition 3.1 of arXiv:1902.05010v2 gives
\[
|\tanh\alpha|=\frac{2|\mu|}{1+\mu^2}
=\frac{|\cos(\pi(\lambda_0^L+1/2))|}{|\sin((\pi-\omega)(\lambda_0^L+1/2))|}.
\]
For \(\lambda_0^L\in(-1/2,0)\), set \(x=\lambda_0^L+1/2\in(0,1/2)\). At \(\omega=\pi/2\), both trigonometric factors are positive, so
\[
\cos(\pi x)=t\sin(\pi x/2).
\]
With \(y=\sin(\pi x/2)\), the double-angle identity gives
\[
1-2y^2=ty,
\]
hence the positive root is
\[
y=\frac{\sqrt{t^2+8}-t}{4}.
\]
This yields the displayed closed form for \(\lambda_0^L\).

For \(m=|\mu|\in(0,1)\), \(t=2m/(1+m^2)\) is strictly increasing. Differentiating \(2y^2+ty-1=0\) gives \(dy/dt=-y/(4y+t)<0\). Therefore \(\lambda_0^L\) is strictly decreasing. At \(t\downarrow0\), \(y\to1/\sqrt2\), giving \(\lambda_0^L\to0\); at \(t\uparrow1\), \(y\to1/2\), giving \(\lambda_0^L\to-1/6\).

Theorem 3.5 of the same source gives
\[
\mathcal D(D_0^L)=\mathcal D(D^L)+\operatorname{span}\{u_0^L\},
\]
and Definition 3.1 gives \(u_0^L=\phi(r/\rho)r^{\lambda_0^L}f_0^L(\theta)\). The minimal domain \(\mathcal D(D^L)\) is \(H^1\) on each side, hence locally \(W^{1,p}\) for every \(1\le p\le2\). Near the corner, the nonzero singular generator satisfies \(|\nabla u_0^L|\asymp r^{\lambda_0^L-1}\) on at least one angular subinterval. Thus its local \(L^p\) gradient integral has the same convergence as
\[
\int_0^\delta r^{p(\lambda_0^L-1)+1}\,dr.
\]
This is finite exactly when \(p<2/(1-\lambda_0^L)\), and at equality the integrand is proportional to \(r^{-1}\). Since \(u_0^L\in\mathcal D(D_0^L)\), the threshold is sharp for containment of the full distinguished domain.

## Verification
The accompanying `verify.py` evaluates the closed form at several couplings, checks the source angular equation numerically, verifies strict monotonic decrease of \(\lambda_0^L\) and \(p_c\) on the test grid, and checks that the radial gradient exponent equals \(-1\) at \(p=p_c\). These computations corroborate the algebra; the proof above is analytic and does not infer an infinite-domain statement from sampling.

## Relationship to prior work
Pizzichillo--Van Den Bosch derive the transcendental angular equation, identify \(\lambda_0^L\in(-1/2,0)\), and prove that the extension with domain in \(H^{1/2}\) is obtained by adjoining \(u_0^L\). The inspected source does not specialize the right angle to a closed form and does not state the sharp local \(W^{1,p}\) threshold.

Benhellal--Pankrashkin--Zreik, arXiv:2307.12772v1, later obtain broad self-adjointness conditions for relativistic shell interactions on Lipschitz curves and curvilinear polygons; for polygon angles between \(\pi/2\) and \(3\pi/2\) they give a full noncritical self-adjointness range. Their inspected statements concern existence/self-adjointness of the \(H^{1/2}\)-domain realization, not the right-angle corner singular exponent or the sharp local \(W^{1,p}\) cutoff proved here.

## Limitations
The formula uses the coupling normalization \(\mu\in(-1,1)\) from arXiv:1902.05010v2. The endpoint values are limits because the source excludes \(\mu=0\), while \(|\mu|=1\) lies at the edge of that parametrization. The exact \(W^{1,p}\) cutoff is proved for the straight wedge/local straight-edge model; transferring this exact endpoint to general curvilinear corners would require controlling the straightening perturbation in \(W^{1,p}\).

## References
1. F. Pizzichillo and H. Van Den Bosch, *Self-Adjointness of two dimensional Dirac operators on corner domains*, arXiv:1902.05010v2; J. Spectr. Theory 11 (2021), 1043--1079, DOI:10.4171/JST/365.
2. B. Benhellal, K. Pankrashkin, and M. Zreik, *On the self-adjointness of two-dimensional relativistic shell interactions*, arXiv:2307.12772v1; J. Operator Theory 93 (2025), 569--591.
