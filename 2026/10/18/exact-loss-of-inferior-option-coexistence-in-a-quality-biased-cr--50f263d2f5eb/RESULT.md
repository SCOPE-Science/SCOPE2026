# Exact loss of inferior-option coexistence in a quality-biased cross-inhibition model

## Finding
For the Reina–Zakir–De Masi–Ferrante deterministic two-option cross-inhibition model with balanced zealot populations and unequal quality ratio \(q>1\), the entire **physical equilibrium diagram** has one exact algebraic threshold. Define, for \(0<t<1\),
\[
H_q(t)=q^4+q^3t+q^2t-q^2t^2-qt^2-t^3,
\qquad
\Phi_q(t)=\frac{q^2t(1-t)}{H_q(t)},
\]
and let \(t_*(q)\) be the unique root in \((0,1)\) of
\[
G_q(t)=q^4(1-2t)-q(q^2-1)t^2+t^3(2-t)=0.
\]
Put \(z_*(q)=\Phi_q(t_*(q))\). For each \(0<z<1/2\), the positive-population equilibrium counts and types are exactly:

* \(0<z<z_*(q)\): three equilibria, consisting of a locally exponentially attracting \(X\)-majority equilibrium, a locally exponentially attracting \(Y\)-majority equilibrium, and one hyperbolic saddle with a \(Y\) majority.
* \(z=z_*(q)\): exactly two equilibria, namely the attracting \(X\)-majority equilibrium and a collision of the two \(Y\)-majority branches with one zero and one negative eigenvalue. The collision is a nondegenerate quadratic fold of the equilibrium curve.
* \(z_*(q)<z<1/2\): exactly one equilibrium, the locally exponentially attracting \(X\)-majority equilibrium.

The threshold is strictly decreasing in \(q\), and its sharp limits are
\[
\lim_{q\downarrow1}z_*(q)=\frac15,
\qquad
\lim_{q\to\infty}q^2z_*(q)=\frac14.
\]
These are statements about deterministic local equilibrium types, **not** global selection probabilities or switching times in finite swarms.

## Assumptions and scope
Write \(x\) and \(y\) for the fractions of flexible individuals committed to options \(X\) and \(Y\); each option additionally has a fixed zealot fraction \(z\). The undecided fraction is \(u=1-x-y-2z\). With the time normalization of the cited model, the equations are
\[
\dot x=q u(x+z)-x(y+z),\qquad
\dot y=u(y+z)-q y(x+z).
\]
Quantifiers: every real \(q>1\) and every real \(z\in(0,1/2)\), on the physical simplex \(\{x,y\ge0: x+y\le 1-2z\}\). The ratio \(q>1\) says option \(X\) is of higher quality; the case \(0<q<1\) follows by exchanging the two options and replacing \(q\) by its reciprocal (with a positive rescaling of time). The cases \(z=0\), \(z=1/2\), and \(q=1\) are boundary limits and are not asserted to share the stated hyperbolic classifications.

## Proof
**1. No boundary equilibrium and a complete rational parametrization.** For \(z>0\), a putative equilibrium with \(x=0\) and \(u>0\) has \(\dot x=qzu>0\), and similarly for \(y=0\). If \(u=0\), then \(\dot x=-x(y+z)\) and \(\dot y=-qy(x+z)\), so both would force \(x=y=0\), contrary to \(z<1/2\). Thus every physical equilibrium has \(x,y,u>0\). Set
\[
r=\frac{x+z}{y+z}>0,\qquad
D_q(r)=q^2r^3+(q^2+q)r^2-(q+1)r-1.
\]
Dividing the stationary equations gives \(x/y=q^2r^2\); solving the stationary equations and the normalization yields **every** equilibrium, without extraneous roots, as
\[
\boxed{\quad
x=\frac{q^2r^2(r-1)}{D_q(r)},\quad
y=\frac{r-1}{D_q(r)},\quad
u=\frac{qr(r-1)}{D_q(r)},\quad
z=\frac{r(q^2r-1)}{D_q(r)}.\quad}
\]
Conversely, substituting these expressions into the ODE and into \(x+y+u+2z=1\) gives zero residual. All fractions are positive precisely for the two disjoint branches \(0<r<q^{-2}\) and \(r>1\); indeed \(D_q(r)=(r+1)(q^2r^2-1)+qr(r-1)\) is negative on the first branch and positive on the second. Ratios between the branches cannot yield physical equilibria.

**2. The unique high-quality branch.** Write \(Z_q(r)=r(q^2r-1)/D_q(r)\) and
\[
E_q(r)=1+qr^2-q^3r^2+2q^2r^3-2q^2r-q^4r^4.
\]
Differentiation yields \(Z'_q(r)=E_q(r)/D_q(r)^2\). On \(r\ge1\), \(E_1(r)=-(r-1)^3(r+1)\le0\), and
\[
\partial_q E_q(r)=-4qr^3(q^2r-1)-r^2(3q^2-1)-4qr<0
\]
for all \(q\ge1\). Hence \(Z'_q(r)<0\) when \(q>1,r>1\). Its endpoint limits are \(Z_q(1)=1/2\) and \(Z_q(+\infty)=0\). Therefore each \(0<z<1/2\) has exactly one equilibrium on \(r>1\), and \(x/y=q^2r^2>1\).

**3. Exactly one fold on the low-quality branch.** Set \(t=q^2r\in(0,1)\). Then \(Z_q(r)=\Phi_q(t)\). The denominator is positive because
\[
\frac{H_q(t)}{q^2}=q^2+qt+t-t^2-\frac{t^2}{q}-\frac{t^3}{q^2}
\]
is strictly increasing in \(q\ge1\), and at \(q=1\) equals \((1-t)(1+3t+t^2)>0\). Exact differentiation gives
\[
\Phi'_q(t)=\frac{q^2G_q(t)}{H_q(t)^2}.
\]
Now \(G_q(0)=q^4>0\) and \(G_q(1)=-(q+1)(q^3-1)<0\). Moreover
\[
G'_q(t)=-2q^4-2q(q^2-1)t+6t^2-4t^3<0
\]
for \(q>1,\ 0<t<1\), since \(6t^2-4t^3\le2\). There is exactly one zero \(t_*(q)\) and exactly one strict maximum \(z_*(q)\). The curve returns to zero at both endpoints; hence it has two, one, or zero preimages according as \(z<z_*\), \(z=z_*\), or \(z>z_*\). On both branches \(x/y=q^2r^2<1\). Since \(G'_q(t_*)<0\), the maximum is quadratic, not a higher-order tangency.

**4. Stability of all branches.** Let \(J\) be the \(2\times2\) Jacobian. At an equilibrium put \(s=x+z\) and \(v=y+z\). From stationarity, \(qu=v(1-z/s)<v\) and \(u=qs(1-z/v)<qs\). Consequently
\[
\operatorname{tr}J=(qu-v)+(u-qs)-qs-v<0.
\]
Direct algebra using the parametrization gives the exact determinant identity
\[
\boxed{\quad \det J=-\frac{(q^2r^2-1)E_q(r)}{D_q(r)^2}.\quad}
\]
On \(r>1\), both \(q^2r^2-1>0\) and \(E_q(r)<0\), so \(\det J>0\). On \(0<r<q^{-2}\), the factor \(q^2r^2-1\) is negative, so the determinant has the sign of \(E_q(r)\), equivalently of \(G_q(q^2r)\). The small-\(r\) branch is attracting, and the larger-\(r\) branch is a saddle. At the unique fold \(\det J=0\) and \(\operatorname{tr}J<0\), hence exactly one eigenvalue is zero. The parametrized stationary curve has nonzero tangent (its ratio coordinate changes) and a strict quadratic extremum in \(z\), giving the asserted nondegenerate equilibrium fold.

**5. Quality monotonicity and sharp asymptotics.** For fixed \(t\in(0,1)\), write
\[
\Phi_q(t)=\frac{t(1-t)}{q^2+qt+t-t^2-t^2/q-t^3/q^2}.
\]
Its denominator strictly increases with \(q\), so \(\Phi_q(t)\) strictly decreases. Taking the unique maxima preserves strict decrease: \(z_*(q_2)<z_*(q_1)\) whenever \(q_2>q_1>1\). Pointwise as \(q\downarrow1\), \(\Phi_q(t)\to t/(1+3t+t^2)\), whose supremum on \((0,1)\) is \(1/5\). Monotonicity gives the upper bound and taking fixed \(t\) arbitrarily close to one gives the matching lower limit. Uniformly for \(0\le t\le1\), \(H_q(t)/q^4\to1\) as \(q\to\infty\), so \(q^2\Phi_q(t)\to t(1-t)\) uniformly. Its maximum is \(1/4\), proving the second limit.

## Verification
The supplied standalone `verify.py` uses exact symbolic algebra to verify stationary parametrization, normalization, derivative, determinant, and quartic fold identities. It also samples seven distinct quality ratios, computes candidate equilibrium coordinates, independently checks ODE residuals and Jacobian spectra, and reports 126 passed assertions. These finite checks corroborate the analytic proof; they do not substitute for the quantifiers established in it.

As an exact test, for \(q=2\) one has
\[
G_2(t)=16-32t-6t^2+2t^3-t^4,\qquad
z_*(2)\approx0.0493061260208877.
\]
At \(t=1/2\), \(\Phi_2(1/2)=8/163>1/25\), so \(z=1/25\) has three equilibria. Conversely, \(\Phi_2(t)<1/20\) for every \(0<t<1\) because
\[
H_2(t)-80t(1-t)=16-68t+74t^2-t^3
\ge16-68t+73t^2>0,
\]
and the last quadratic has negative discriminant \(-48\). Thus \(z=1/20\) has exactly one equilibrium, with no floating-point dependence.

## Relationship to prior work
Reina, Zakir, De Masi, and Ferrante derive the same model (their equation (8)), identify the balanced-zealot pitchfork at equal qualities, and illustrate unequal-quality saddle-node behavior numerically (their Figure 5b). They explicitly note that the asymmetric-quality equilibrium equations are too complex to classify analytically in their displayed form. **Those model equations, qualitative bistability, and the numerically observed trend of the fold are prior art.** The present contribution is an exact all-parameter, root-isolated threshold, a complete count and stability classification of all physical equilibria, and rigorous monotonicity and two sharp limiting laws. It does not claim to discover cross-inhibition bistability itself.

Antonic, Zakir, Dorigo, and Reina (2024) investigate mixtures of heterogeneous decision-maker behaviors and robustness to zealots; the accessible abstract does not settle the specific one-population quality-ratio threshold stated here, but complete-text coverage remains a priority risk. March-Pons, Pastor-Satorras, and Miguel (2025) analyze nonlinear inhibitory response functions, discovery probabilities, and interdependence in a different LES-type dynamical system rather than the fixed linear cross-inhibition, quality-scaled zealot ODE above.

## Limitations
Only the deterministic, well-mixed, two-option, balanced-zealot, equal-per-option quality-scaled cross-inhibition model is covered. Stability is local; a finite-population Markov chain may still switch between metastable alternatives. Nothing is proved about attraction basins, global convergence, noisy updating, imbalanced zealot counts, additional alternatives, or nonlinear inhibitory response. Full publication-priority verification, including exhaustive inspection of all supplementary software and related proceedings, remains open. No external independent scientific audit is represented.

## References
1. A. Reina, R. Zakir, G. De Masi and E. Ferrante, *Cross-inhibition leads to group consensus despite the presence of strongly opinionated minorities and asocial behaviour*, Communications Physics **6**, 236 (2023), DOI: 10.1038/s42005-023-01345-3; arXiv:2211.09531 (first publicly posted 2022-11-17). Equations (7)–(8), stability discussion and Fig. 5, with full accessible version at https://eprints.whiterose.ac.uk/id/eprint/202997/1/s42005-023-01345-3.pdf.
2. N. Antonic, R. Zakir, M. Dorigo and A. Reina, *Collective Robustness of Heterogeneous Decision-Makers Against Stubborn Individuals*, AAMAS 2024, pp. 68–77, DOI: 10.5555/3635637.3662853, available proceedings location https://www.ifaamas.org/Proceedings/aamas2024/pdfs/p68.pdf.
3. D. March-Pons, R. Pastor-Satorras and M. C. Miguel, *Non-linear inhibitory responses enhance performance in collective decision-making*, Communications Physics **8**, 119 (2025), DOI: 10.1038/s42005-025-02046-9.
