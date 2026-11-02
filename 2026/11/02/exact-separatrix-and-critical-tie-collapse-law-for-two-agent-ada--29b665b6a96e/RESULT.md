# Exact separatrix and critical tie-collapse law for two-agent adaptive opinion dynamics

## Finding

For the two-person, symmetric, continuously weighted adaptive-opinion model of Nugent, Gomes and Wolfram with **logistic edge dynamics**, there is a complete sharp division of positive initial ties into consensus and persistent disagreement. The division holds for a class of smooth decreasing interaction kernels, not only the exponential kernel used in the motivating simulations.

**Theorem (sharp two-person phase portrait).** Let \(\phi:[0,2]\to(0,1]\) be \(C^2\), strictly decreasing, with \(\phi(0)>1/2\), \(\phi(2)<1/2\), and a unique \(r_c\in(0,2)\) satisfying \(\phi(r_c)=1/2\) and \(\phi'(r_c)<0\). Give two persons distinct initial opinions \(x_1(0)<x_2(0)\) in \([-1,1]\), an initial symmetric inter-person tie \(0<w_0<1\), and fixed unit self-ties. Write \(d_0=x_2(0)-x_1(0)>0\). Define

\[
H(d)=\int_{r_c}^{d}\frac{2\phi(s)-1}{2s\phi(s)}\,ds,\qquad
C=\operatorname{arctanh}(w_0)+H(d_0).
\]

If \(d_0\le r_c\), consensus always occurs. If \(d_0>r_c\), put
\[
w_c(d_0)=\tanh\!\big(-H(d_0)\big)\in(0,1).
\]
Then precisely three behaviors occur:

* **Weaker initial tie, \(0<w_0<w_c\):** \(d(t)\downarrow d_*\in(r_c,d_0)\), where \(H(d_*)=C\), and \(w(t)\to0\). This is persistent nonzero opinion separation despite an initially positive tie.
* **Critical tie, \(w_0=w_c\):** \(d(t)\downarrow r_c\) and \(w(t)\to0\), with the universal sharp asymptotics
  \[
  \lim_{t\to\infty}t\big(d(t)-r_c\big)=\frac{1}{-\phi'(r_c)},\qquad
  \lim_{t\to\infty}t^2w(t)=\frac{1}{r_c[-\phi'(r_c)]}.
  \]
* **Stronger initial tie, \(w_c<w_0<1\):** \(d(t)\to0\) and \(w(t)\to1\). The two opinions converge to their initial arithmetic mean.

In the first regime, the gap above its positive limit and the tie weight both have exponential logarithmic rate \(1-2\phi(d_*)>0\). In the last regime, the gap has exponential logarithmic rate \(\phi(0)\) and the tie deficit has rate \(2\phi(0)-1\).

For the source's exponential interaction \(\phi(d)=e^{-\alpha d}\), \(\alpha>0\), the crossing is \(r_c=(\log2)/\alpha\) when \(\alpha>(\log2)/2\). The function can be written using the classical exponential integral:
\[
H(d)=\log\frac d{r_c}-\frac12\left[\operatorname{Ei}(\alpha d)-\operatorname{Ei}(\alpha r_c)\right].
\]
Thus the critical tie is given explicitly by \(\tanh[-H(d_0)]\), and its critical decay is
\[
 t\left(d(t)-\frac{\log2}{\alpha}\right)\to\frac2\alpha,
 \qquad t^2w(t)\to\frac2{\log2}.
\]
When \(0<\alpha\le(\log2)/2\), every admissible positive initial tie leads to consensus, because the interaction remains at least \(1/2\) across the entire opinion domain. For \(\alpha=1\) and \(d_0=2\), the critical tie is approximately \(0.7137933377355186\); initial ties on either side have different limiting outcomes.

## Assumptions and scope

The system is a two-vertex instance of the continuous-time, undirected, positive-tie model. It assumes exactly two persons, bounded real opinions, symmetric weights \(w_{12}=w_{21}=w\), permanently fixed diagonal weights \(w_{11}=w_{22}=1\), instantaneous normalization by the row sums \(1+w\), and the logistic update with unit rate. Its equations are
\[
\dot x_1=\frac{w}{1+w}\phi(d)(x_2-x_1),\quad
\dot x_2=\frac{w}{1+w}\phi(d)(x_1-x_2),\quad
\dot w=w(1-w)(2\phi(d)-1),\quad d=x_2-x_1>0.
\]
The midpoint \((x_1+x_2)/2\) is conserved. The theorem applies to each admissible \(d_0\in(0,2]\) and \(w_0\in(0,1)\); it does not replace a finite population with a mean-field limit. The boundary cases \(w_0=0\) and \(w_0=1\) are fixed-tie faces: \(w_0=0\) prevents all motion, while \(w_0=1\), under a positive interaction kernel, leads to consensus. The derivative condition at \(r_c\) is essential for the stated quadratic tie-gap law and its \(t^{-2}\) exponent.

## Proof

**1. Reduced flow and invariant.** Subtract the opinion equations. Positivity of the initial gap and weight is preserved for all finite times by the multiplicative vector fields, and the reduced ODE is
\[
\dot d=-\frac{2w}{1+w}\phi(d)d<0,\qquad
\dot w=w(1-w)(2\phi(d)-1).
\]
By differentiation,
\[
\frac{d}{dt}\operatorname{arctanh}(w)
=\frac{w}{1+w}(2\phi(d)-1),
\quad
\frac{d}{dt}H(d)
=-\frac{w}{1+w}(2\phi(d)-1).
\]
Therefore \(\operatorname{arctanh}(w(t))+H(d(t))=C\) exactly for all finite times. Equivalently \(w(t)=\tanh(C-H(d(t)))\), with \(C-H(d(t))>0\).

**2. Geometry of the invariant.** Since \(\phi\) decreases strictly through one half, \(H'(d)>0\) for \(d<r_c\), and \(H'(d)<0\) for \(d>r_c\). Hence \(H\) has its unique strict global maximum \(H(r_c)=0\). As \(d\downarrow0\), the assumption \(\phi(0)>1/2\) gives \(H(d)\to-\infty\). Because \(d(t)\) decreases and is nonnegative it has a limit \(d_\infty\). If \(d_\infty>0\), then the invariant implies \(w(t)\) has a limit, which must equal zero, since \(\dot d\to0\) while \(\phi(d_\infty)d_\infty>0\). It follows that \(H(d_\infty)=C\). If instead \(d_\infty=0\), the invariant and the divergence of \(H\) force \(w(t)\to1\). This also proves there are no other limits.

For \(d_0\le r_c\), the strictly decreasing trajectory stays on the increasing side of \(H\), and \(H(d)<H(d_0)<C\) for \(0<d<d_0\), precluding any positive terminal root. For \(d_0>r_c\), the only possible terminal root along the decreasing trajectory lies in \([r_c,d_0)\) and exists if and only if \(C\le0\): it is the unique solution \(H(d_*)=C\) in \((r_c,d_0)\) when \(C<0\), or is \(r_c\) when \(C=0\). When \(C>0\), no root exists and consensus follows. Solving \(C=0\) for the initial weight gives exactly \(w_c(d_0)\). (A root of \(H(d)=C<0\) below \(r_c\) is dynamically inaccessible because \(C-H(d)\) would become negative before the trajectory could cross the right-hand root.)

**3. Critical slowing.** Set \(h=d-r_c>0\) on the critical orbit, where \(C=0\). Taylor expansion at the nondegenerate maximum gives
\[
H(r_c+h)=\frac{\phi'(r_c)}{r_c}h^2+o(h^2).
\]
Consequently \(w=\tanh(-H(d))\sim-\phi'(r_c)h^2/r_c\). The gap equation yields \(\dot h\sim\phi'(r_c)h^2\). Since \(\phi'(r_c)<0\), integration of \((1/h)'\to-\phi'(r_c)\) gives \(th\to1/[-\phi'(r_c)]\). Substituting into the weight-gap relation yields \(t^2w\to1/[r_c(-\phi'(r_c))]\).

**4. Off-critical rates.** When \(d\to d_*>r_c\) and \(w\to0\), the logarithmic weight equation implies \((\log w)'\to2\phi(d_*)-1<0\). The simple root \(H'(d_*)<0\) gives \(w\sim-H'(d_*)(d-d_*)\), so both quantities have the same exponential logarithmic rate. At consensus, the equations for \(\log d\) and \(\log(1-w)\) give limiting derivatives \(-\phi(0)\) and \(-[2\phi(0)-1]\) respectively. These deductions use ordinary ODE limits, not finite simulations. For the exponential kernel, direct integration of \(H'\) yields the stated \(\operatorname{Ei}\) expression and the explicit critical coefficients.

## Verification

The accompanying `verification.py` numerically integrates the **reduced source equations**, recomputes the conserved quantity independently, checks all three regimes, and checks scaled critical asymptotics. It uses Python 3 with NumPy/SciPy. Run `python verification.py` from the extracted package folder. Tests include 80 combinations of exponential-kernel parameters, two independent critical boundary points, and an elementary rational kernel \(\phi(d)=1/(1+d)\), whose first integral is \(H(d)=\tfrac12(\log d-d)\) up to an additive constant. All reported tests passed at packaging. Such finite and numerical checks corroborate, but do not prove, the universal theorem; the preceding calculus argument supplies the proof.

## Relationship to prior work

Nugent, Gomes and Wolfram, *On evolving network models and their influence on opinion formation* (first public May 16, 2023), introduce the precise normalized opinion ODE, unit self-ties, logistic edge dynamics, and exponential interaction used above. Their Section 3.4 reports a numerical consensus-to-clustering transition; it does not derive an exact two-person initial-tie separatrix or critical powers. Nugent, Calatayud Fernández and Gomes, *Emergent structures in coupled opinion and network dynamics* (arXiv February 3, 2026), prove substantially broader population-level clustering and convergence alternatives for logistic weights (Theorem 3.1 and Corollaries 3.2–3.4). Those conclusions say when limits must be clusters or decayed ties, but do not determine the explicit initial-weight boundary or its sharp algebraic rates on the two-person invariant curve. Wang, Luo and Gao's signed-appraisal coevolution model uses different coupling and allows signed weights, so its structural-balance theorem does not furnish this positive logistic-tie phase portrait.

## Limitations

This is an exact two-person solution, not a classification for arbitrary networks or more than two agents. The result assumes symmetry, fixed self-ties, unit relative time scales, and positive smooth strictly decreasing kernels with a transverse half-interaction crossing. The exponent statement does not cover a degenerate crossing where \(\phi'(r_c)=0\), and the outcome threshold may differ for directed or asymmetric ties. No experiment is presented as an infinite proof. Although relevant primary literature and research records were compared, undiscovered equivalent special-case analyses remain a priority risk, and independent external validation has not been performed.

## References

1. A. J. Nugent, S. N. Gomes, M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, arXiv:2305.09483 (first public May 16, 2023), https://arxiv.org/abs/2305.09483 ; *Physica D* **456** (2023), 133914.
2. A. Nugent, C. Calatayud Fernández, S. N. Gomes, *Emergent structures in coupled opinion and network dynamics*, arXiv:2602.03738 (February 3, 2026), https://arxiv.org/abs/2602.03738 .
3. H. Wang, F. Luo, J. Gao, *Co-evolution of Opinion and Social Tie Dynamics Towards Structural Balance*, arXiv:2107.05796 (July 13, 2021), https://arxiv.org/abs/2107.05796 .
