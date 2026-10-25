# Exact phase-balanced placement of unequal absorbing point traps on a Robin interval

## Finding
Consider a one-dimensional diffusion or quantum point-interaction system on an interval of length \(L>0\). With two nonnegative fixed Robin endpoint coefficients and any finite ordered list of independently prescribed positive point-absorption strengths, the slowest decay rate is **uniquely maximized by an explicit nonuniform spatial allocation**. No restriction to equal trap strengths, equal endpoint coefficients, weak coupling, or a fixed number of traps is required.

Let \(N\ge1\) and \(a_j>0\). Define \(t_*>0\) by the single transcendental equation
\[
 t_*L=\arctan\!\left(\frac{h_0}{t_*}\right)+\arctan\!\left(\frac{h_L}{t_*}\right)+2\sum_{j=1}^N\arctan\!\left(\frac{a_j}{2t_*}\right).
\]
It has exactly one positive solution. Put \(\phi_0=\arctan(h_0/t_*)\), \(\phi_L=\arctan(h_L/t_*)\), and \(\psi_j=\arctan(a_j/(2t_*))\). The unique maximizer is
\[
 x_j^*=\frac{\phi_0+2\sum_{i<j}\psi_i+\psi_j}{t_*},\qquad j=1,\ldots,N,
\]
and the maximal principal eigenvalue is \(\lambda_{1,\max}=t_*^2\). Equivalently, the consecutive optimal gaps satisfy
\[
 t_*x_1^*=\phi_0+\psi_1,\quad
 t_*(x_{j+1}^*-x_j^*)=\psi_j+\psi_{j+1},\quad
 t_*(L-x_N^*)=\psi_N+\phi_L.
\]
In a diffusion problem with diffusivity \(D>0\), the maximal exponential survival-decay rate is \(Dt_*^2\) when \(a_j\) and \(h_0,h_L\) are normalized by \(D\).

## Assumptions and scope
The operator is the self-adjoint Schrödinger operator associated with the quadratic form on \(H^1(0,L)\)
\[
 Q_{\boldsymbol x}[u]=\int_0^L |u'(z)|^2\,dz+h_0|u(0)|^2+h_L|u(L)|^2+\sum_{j=1}^N a_j|u(x_j)|^2.
\]
Its eigenfunctions are continuous, solve \(-u''=\lambda u\) between traps, satisfy \(u'(0)=h_0u(0)\) and \(u'(L)=-h_Lu(L)\), and have derivative jump \(u'(x_j+)-u'(x_j-)=a_ju(x_j)\). We optimize over **strictly interior, ordered** points \(0<x_1<\cdots<x_N<L\), holding the labeled positive strengths and endpoint coefficients fixed. All \(L>0\), \(h_0,h_L\ge0\), \(N\ge1\), and \(a_j>0\) are covered. The positive simple lowest eigenvalue \(\lambda_1(\boldsymbol x)>0\) is the target; its eigenfunction is strictly positive on the closed interval.

## Proof
**Step 1: A sharp upper bound on each trap's phase jump.** For any admissible configuration write \(t=\sqrt{\lambda_1}>0\) and choose the strictly positive ground eigenfunction \(u\). On each open gap introduce the principal Prüfer phase
\[
 \theta(z)=\arctan\!\left(\frac{u'(z)}{t u(z)}\right)\in(-\pi/2,\pi/2).
\]
Since \(u''=-t^2u\), differentiation gives \(\theta'=-t\) on each gap. Across the \(j\)th point trap, \(u\) stays continuous and positive while the derivative increases by \(a_ju\). Consequently, with \(r=u'(x_j-)/(t u(x_j))\) and \(s=a_j/t>0\),
\[
 \theta(x_j+)-\theta(x_j-)=\arctan(r+s)-\arctan(r)\le 2\arctan(s/2).
\]
The inequality is globally sharp: differentiating \(\arctan(r+s)-\arctan(r)\) shows a unique maximum at \(r=-s/2\), and this maximum is exactly \(2\arctan(s/2)\). Equality therefore holds if and only if the incoming and outgoing logarithmic slopes are \(-a_j/2\) and \(+a_j/2\), respectively.

**Step 2: Integrate the phases and bound the ground energy.** At the left endpoint, \(\theta(0)=\arctan(h_0/t)\), while at the right endpoint \(\theta(L)=-\arctan(h_L/t)\). Summing the uniform phase decrease over the full length and the jumps gives the *exact identity*
\[
 tL=\arctan(h_0/t)+\arctan(h_L/t)+\sum_{j=1}^N\bigl(\theta(x_j+)-\theta(x_j-)\bigr).
\]
Step 1 implies
\[
 tL\le\arctan(h_0/t)+\arctan(h_L/t)+2\sum_{j=1}^N\arctan(a_j/(2t)).
\]
The right-hand side is strictly decreasing (or nonincreasing in a zero endpoint term) for positive \(t\) while \(tL\) is strictly increasing. As \(t\downarrow0\), the right side tends to \(N\pi\) plus nonnegative endpoint contributions; as \(t\to\infty\), it tends to zero. Thus there is exactly one intersection \(t_*>0\), and every placement satisfies \(t\le t_*\).

**Step 3: Construct a positive eigenfunction attaining the bound.** Let the gaps be those specified in the Finding, so their sum is exactly \(L\) by the defining equation. Since \(\psi_j>0\) and all endpoint phases are nonnegative, every gap is strictly positive. Start with a positive solution \(u(0)=1\), \(u'(0)=h_0\), and propagate with \(u''+t_*^2u=0\). The phase falls from \(\phi_0\) to \(-\psi_1\) at the first trap. Impose the prescribed derivative jump: since \(t_*[\tan(\psi_1)-\tan(-\psi_1)]=a_1\), the phase jumps exactly to \(+\psi_1\). Repeat from \(+\psi_j\) to \(-\psi_{j+1}\) across each next gap and then to \(-\phi_L\) at the right endpoint. All phases remain strictly between \(-\pi/2\) and \(+\pi/2\), so the resulting continuous piecewise harmonic eigenfunction remains strictly positive everywhere. Its eigenvalue is therefore the ground eigenvalue \(t_*^2\), attaining the upper bound.

**Step 4: Global uniqueness.** If another ordered trap placement attained the same ground eigenvalue, every nonnegative deficit in the phase-jump bound of Step 1 would have to vanish. At every trap the phase must therefore pass exactly from \(-\psi_j\) to \(+\psi_j\). The endpoint phases and the fixed rate of decrease \(-t_*\) uniquely fix every gap as in the displayed formulas. Hence all positions coincide with \(\boldsymbol x^*\); every different placement has strictly smaller ground eigenvalue.

## Verification
The standalone file `point_trap_verify.py` implements independent piecewise-harmonic transfer matrices and an independent first-positive-eigenvalue root search; running `python3 point_trap_verify.py` with NumPy and SciPy passed **1,260 assertion groups** over 120 randomized parameter sets with between one and six unequal traps. These corroborate that the stated positions are strictly ordered, obey the spectral equation, and outperform randomized admissible competitors. They do not replace the all-parameter analytical phase argument.

For illustration, if both endpoints are reflecting and all strengths equal, the theorem gives equal interior gaps and half-sized endpoint gaps, with a *strength-dependent* overall wavenumber. For different strengths, the optimal interior gaps are sums of adjacent individual phase half-shifts, so equal spacing is generally not optimal.

## Relationship to prior work
Karulina and Vladimirov (arXiv:1206.5081; initial submission 22 June 2012) analyze extrema of the first eigenvalue for fixed-integral sign-constrained singular potentials on Robin intervals; their explicit point-interaction examples concern a single concentration, and their unconstrained positive-budget maximizing potential is not a fixed array of independently specified atoms. Exner (arXiv:1906.01229) optimizes **same-strength** point interactions on circles and periodic intervals; the periodic symmetry and interchangeable strengths differ from a heterogeneous ordered Robin interval. Kurasov and Serio (2019) optimize potential and coupling *resources* on fixed metric graphs, not the positions of a prescribed ordered list of positive atoms with fixed separate strengths. A published equal-strength periodic-loop optimization likewise does not imply the displayed unequal-strength Robin formula. The proof above supplies the explicit multiple-interface global comparison rather than assuming novelty from differing terminology.

## Limitations
The theorem requires a homogeneous one-dimensional bulk diffusion coefficient, nonnegative endpoint losses, strictly positive and fixed individual point-trap strengths, and no additional distributed potential. Its decay interpretation concerns long-time survival; it does not optimize mean first-passage times, finite-time absorption, nonlinear dynamics, higher-dimensional traps or arbitrary time-varying controls. Positions of traps with zero strength are not identifiable and are deliberately excluded. The literature comparison does not establish absolute historical priority, especially for broader Sturm–Liouville optimal placement formulations not available in full text.

## References
1. E. S. Karulina and A. A. Vladimirov, *The Sturm–Liouville problem with singular potential and the extrema of the first eigenvalue*, arXiv:1206.5081 (first public version 2012-06-22), https://arxiv.org/abs/1206.5081.
2. P. Exner, *An optimization problem for finite point interaction families*, arXiv:1906.01229 (2019), https://arxiv.org/abs/1906.01229.
3. P. Kurasov and A. Serio, *Optimal Potentials for Quantum Graphs*, Annales Henri Poincaré 20 (2019), 1517–1542, DOI 10.1007/s00023-019-00783-6.
