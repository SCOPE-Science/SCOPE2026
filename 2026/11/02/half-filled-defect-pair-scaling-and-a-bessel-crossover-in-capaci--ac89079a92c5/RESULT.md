# Half-filled defect-pair scaling and a Bessel crossover in capacity-two exclusion

## Finding

Consider the stationary capacity-two deformation of the asymmetric exclusion process on a periodic ring, with hopping asymmetry \(q\geq0\) and deformation \(t>0\). Let \(L\geq2\) sites contain exactly \(n\in\{0,\ldots,2L\}\) particles and define
\[
z=\frac{t}{(1+t)^2}\in(0,1/4],\qquad M=\#\{i:\eta_i=2\}.
\]
The exact canonical distribution of the number of doubly occupied sites is
\[
\mathbb P(M=m)=\frac{1}{\mathcal Z_{L,n}(z)}
\frac{L!\,z^m}{m!\,(n-2m)!\,(L-n+m)!},\quad
\max(0,n-L)\leq m\leq\lfloor n/2\rfloor.
\tag{1}
\]
In particular, the finite-ring on-site variance \(V_{L,n}(t)=\operatorname{Var}(\eta_1)\) is invariant under \(t\mapsto1/t\), and for \(2\leq n\leq2L-2\) it is strictly increasing for \(0<t<1\) and strictly decreasing for \(t>1\). It is independent of \(t\) when \(n\in\{0,1,2L-1,2L\}\). The unique maximum in the nontrivial cases is
\[
V_{L,n}(1)=\frac{n}{L}\left(1-\frac1L\right)\frac{2L-n}{2L-1}.
\tag{2}
\]

The following two distinct singular limits characterize the near-singly-occupied regime. First take \(L\to\infty\) at fixed positive \(z\), with \(n/L\to\rho\in(0,2)\). The double-occupancy density converges to the unique \(u(\rho,z)\in(\max(0,\rho-1),\rho/2)\) satisfying
\[
z(\rho-2u)^2=u(1-\rho+u).
\tag{3}
\]
For any real \(\xi\), if subsequently \(z\downarrow0\) and \(\rho=1+\xi\sqrt z+o(\sqrt z)\), then
\[
\frac{u(\rho,z)}{\sqrt z}\longrightarrow
\frac{\xi+\sqrt{\xi^2+4}}2,\qquad
\frac{\lim_{L\to\infty}V_{L,n}(t)}{\sqrt z}
\longrightarrow\sqrt{\xi^2+4}.
\tag{4}
\]
In the second limit, fix an integer \(k\) and \(a>0\), set \(n=L+k\) and \(z=a/L^2\) for sufficiently large \(L\), and let \(J_L=M-\max(k,0)\). Then \(J_L\) converges in total variation to the Bessel-count distribution
\[
\mathbb P(J=j)=
\frac{a^{j+|k|/2}}{j!\,(j+|k|)!\,I_{|k|}(2\sqrt a)},
\qquad j=0,1,2,\ldots,
\tag{5}
\]
where \(I_h\) is the standard modified Bessel function. Moreover,
\[
\lim_{L\to\infty}L\,V_{L,L+k}(t)
=|k|+2\sqrt a\,\frac{I_{|k|+1}(2\sqrt a)}{I_{|k|}(2\sqrt a)}.
\tag{6}
\]
These statements hold for every \(q\geq0\), including totally asymmetric hopping. They are stationary results, not relaxation-time or dynamical-phase-transition claims.

## Assumptions and scope

A configuration is \(\eta\in\{0,1,2\}^L\) with \(\sum_i\eta_i=n\). Periodic neighboring sites exchange particles according to the capacity-two \((q,t)\) asymmetric exclusion dynamics of Ayyer and Misra: a clockwise transition \((b,c)\mapsto(b-1,c+1)\) occurs at rate \([b]_t([2]_t-[c]_t)\); an anticlockwise transition occurs at rate \(q[c]_t([2]_t-[b]_t)\), where \([0]_t=0\), \([1]_t=1\), \([2]_t=1+t\), and forbidden moves have zero rate. The source establishes a unique stationary state at every \(t>0\), independent of \(q\). In the second limiting statement choose either positive solution of \(t/(1+t)^2=a/L^2\); both have the same stationary law. The thermodynamic and finite-size limits above have distinct, explicitly stated orders; no other simultaneous-limit uniformity is asserted.

## Proof

**Canonical reduction.** The known one-site stationary weights for capacity two are \(w_0=t\), \(w_1=1+t\), \(w_2=1\), up to a common factor. If there are \(m\) sites of occupancy two, the numbers of sites with occupancy one and zero are \(n-2m\) and \(L-n+m\). Therefore the unnormalized weight of this macrostate is
\[
\frac{L!}{m!(n-2m)!(L-n+m)!}\,
 t^{L-n+m}(1+t)^{n-2m}.
\]
Dividing by the configuration-independent factor \(t^{L-n}(1+t)^n\) proves (1). In particular the parameter \(t\) enters only through \(z=t/(1+t)^2\), giving the reciprocity \(t\leftrightarrow1/t\) without asserting a conjugacy of the generators.

**Finite-volume strict optimization.** The deterministic identity \(\sum_i\eta_i^2=n+2M\), together with site exchangeability, gives
\[
V_{L,n}=\frac nL+\frac{2\mathbb E_zM}{L}-\left(\frac nL\right)^2.
\tag{7}
\]
Because (1) is an exponential family with sufficient statistic \(M\), differentiation of its finite normalization yields
\[
\frac{\partial V_{L,n}}{\partial\log z}=
\frac2L\operatorname{Var}_z(M).
\tag{8}
\]
The variance on the right is positive precisely when the allowed interval for \(m\) contains at least two integers, equivalently \(2\leq n\leq2L-2\). As \(z'(t)=(1-t)/(1+t)^3\), this proves all strict monotonicity assertions. At \(t=1\), the one-site weights \((1,2,1)\) describe two independent capacity-one slots per site conditioned on exactly \(n\) occupied slots among \(2L\). The single-site occupancy is hypergeometric, yielding (2). At the two limits \(t\to0\) and \(t\to\infty\), \(M\) concentrates at \(\max(0,n-L)\); hence the minimum of the on-site variance equals \(\delta(1-\delta)\), where \(\delta\) is the fractional part of \(n/L\) (and is zero at integer filling).

**Thermodynamic concentration.** Write \(m/L\to u\), \(n/L\to\rho\). Stirling's formula gives the exponential profile, up to constants independent of \(u\),
\[
\Phi_{\rho,z}(u)=-u\log u-(\rho-2u)\log(\rho-2u)
 -(1-\rho+u)\log(1-\rho+u)+u\log z.
\]
Here \(0\log0\) is defined by continuity. Throughout the interior of the admissible interval,
\[
\Phi'_{\rho,z}(u)=\log\frac{z(\rho-2u)^2}{u(1-\rho+u)},\qquad
\Phi''_{\rho,z}(u)=-\frac4{\rho-2u}-\frac1u-\frac1{1-\rho+u}<0.
\]
The first derivative diverges positively at the left boundary and negatively at the right boundary. Thus there is exactly one interior maximizer, given by (3). Uniform Stirling bounds with error \(O(\log L)\) for all multinomial coefficients, followed by a strict-maximum compactness argument, yield exponential concentration of \(M/L\) around that maximizer. Consequently \(\mathbb E[M]/L\to u\), and the one-site marginal converges to probabilities \((1-\rho+u,\rho-2u,u)\) for occupancies \((0,1,2)\). Formula (7) then yields limiting variance \(\rho+2u-\rho^2\).

**Critical filling window.** For \(0<z<1/4\), solving the quadratic (3) gives the exact admissible branch
\[
u(\rho,z)=\frac{\sqrt{(1-\rho)^2+4z\rho(2-\rho)}-(1-\rho+4z\rho)}{2(1-4z)}.
\]
Put \(\rho=1+\xi\sqrt z+o(\sqrt z)\). Expanding this explicit branch shows \(u/\sqrt z\to(\xi+\sqrt{\xi^2+4})/2\), equivalently the unique positive admissible solution of \(y(y-\xi)=1\). Substitution into \(\rho+2u-\rho^2\) gives \(\sqrt z(2y-\xi)+o(\sqrt z)=\sqrt z\sqrt{\xi^2+4}+o(\sqrt z)\), proving (4). At exact half filling \(\rho=1\), the full exact solution is \(u=\sqrt z/(1+2\sqrt z)\), so the thermodynamic variance is \(2\sqrt z/(1+2\sqrt z)\). This square-root limit should not be mistaken for a finite-positive-parameter singularity.

**Finite-size Bessel crossover.** Fix \(k\in\mathbb Z\), \(h=|k|\), \(a>0\), and take \(n=L+k\) and \(z=a/L^2\). With \(j=M-\max(k,0)\), the expression (1), after removing a factor independent of \(j\), has weights
\[
T_{L,j}=\frac{L!}{(L-h-2j)!\,j!\,(j+h)!}\left(\frac a{L^2}\right)^j
=L^h\frac{a^j}{j!\,(j+h)!}
 \prod_{s=0}^{h+2j-1}\left(1-\frac sL\right),
\tag{9}
\]
for \(0\le j\le\lfloor(L-h)/2\rfloor\), and zero otherwise. The product lies in \([0,1]\) and tends to one for each fixed \(j\). After dividing by \(L^h\), the weights are dominated by the summable series \(a^j/[j!(j+h)!]\), including after multiplication by \(j\). Dominated convergence proves total-variation convergence of the normalized distributions and convergence of their first moments. The identities
\[
\sum_{j=0}^{\infty}\frac{a^j}{j!(j+h)!}
=a^{-h/2}I_h(2\sqrt a),\qquad
\mathbb E J=\sqrt a\,\frac{I_{h+1}(2\sqrt a)}{I_h(2\sqrt a)}
\]
give (5). Finally, applying (7) with \(n=L+k\) and \(M=J+\max(k,0)\) yields
\[
L V_{L,L+k}=2\mathbb E J+|k|-\frac{k^2}{L},
\]
and therefore (6). This derivation supplies the required tightness and moment control, rather than extrapolating from finite enumeration.

## Verification

The included standalone `CHECKER.py` uses only the Python standard library. Run `python CHECKER.py`. It reconstructs small finite-state generators and verifies the proposed stationary measure at multiple asymmetries; compares the finite double-occupancy distribution against the hypergeometric endpoint; checks parameter monotonicity; and checks the Bessel and critical-window limits numerically. It reports 414 passing tests. These finite computations are independent corroboration of the analytic arguments, not proofs of infinite-system statements. Equations (1)–(9) and the dominated-convergence argument are the proof.

## Relationship to prior work

Ayyer and Misra derived the \((q,t)\) capacity-\(K\) process, its exact stationary one-site factors, its canonical generating functions, and reciprocal-parameter stationary symmetry. Their detailed occupation discussion concerns the most probable site occupancy for fixed parameters and in extreme-deformation limits. The stationary formula is **not new** here. The distinct claimed result is the exact strict finite-volume variance optimization together with the two near-half-filling scaling theorems, notably the Bessel order \(|k|\) for fixed integer doping and the square-root continuous density window. Evans and Waclaw's general misanthrope theory establishes when factorized stationary measures exist but does not provide these capacity-two critical and finite-size limits. Related zero-range condensation and facilitated exclusion studies concern different stationary weights or dynamics. No implication that the original generating function already constitutes an explicit published analysis of (4)–(6) is assumed; publication-priority comparison remains open to additional specialized sources.

## Limitations

The findings concern stationary, canonically conditioned, capacity-two occupation statistics with finite ring size or specified limiting sequences. They do not cover capacity \(K>2\), convergence rates to stationarity, dynamical currents, universality under altered jump rates, simultaneous limits outside the two specified scalings, or an actual phase transition at finite \(t>0\). The formula for the stationary law is due to prior work. The two asymptotic regimes are not interchangeable; finite \(L\) and singular \(z\to0\) may yield different exponents. No independent publication-priority audit is included.

## References

1. A. Ayyer and S. Misra, *An exactly solvable asymmetric \(K\)-exclusion process*, arXiv:2310.03343, first public preprint October 5, 2023; *Journal of Physics A* **57**, 315001 (2024), https://arxiv.org/abs/2310.03343, https://doi.org/10.1088/1751-8121/ad5edd. Relevant original results: stationary weights, Sections 2–3; occupation analysis, Section 4.
2. M. R. Evans and B. Waclaw, *Condensation in stochastic mass transport models: beyond the zero-range process*, arXiv:1312.5642 (2013), *Journal of Physics A* **47**, 095001 (2014), https://arxiv.org/abs/1312.5642. General factorized misanthrope stationary weights and condensation setting.
3. A. Ayyer, S. Goldstein, J. L. Lebowitz, and E. R. Speer, *Stationary states of the one-dimensional facilitated asymmetric exclusion process*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **59**, 726–742 (2023), https://doi.org/10.1214/22-AIHP1264. Distinct facilitated model and stationary-density regime.
