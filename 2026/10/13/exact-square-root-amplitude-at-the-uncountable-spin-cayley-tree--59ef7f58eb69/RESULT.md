# Exact square-root amplitude at the uncountable-spin Cayley-tree bifurcation
## Finding
Consider the nearest-neighbor model of Botirov and Jahnel with local spin space \([0,1]\), Cayley-tree order \(k\ge2\), integer \(n\ge0\), and parameter \(0\le\theta<1\). Put
\[
m=2n+1,\qquad \theta_c=\frac{m+2}{km}.
\]
Assume \(\theta_c<1\), so the phase transition occurs inside the physical parameter interval. The source proves that for \(\theta>\theta_c\) there are exactly two nontrivial positive translation-invariant boundary laws, corresponding to the unique positive root \(z_0\) and its negative, where \(z=\theta C_2/C_1\).

The onset is quantitatively sharp:
\[
z_0(\theta)=A_{k,m}\sqrt{\theta-\theta_c}+O\!\left((\theta-\theta_c)^{3/2}\right)
\qquad(\theta\downarrow\theta_c),
\]
with
\[
A_{k,m}=2^{-1/m}\sqrt{\frac{3km(m+4)}{(k-1)\left((k+1)(m+2)^2-6k\right)}}.
\]
Hence the symmetry-breaking exponent is exactly \(1/2\) throughout this solvable family, while the critical amplitude is an explicit function of the tree order and spin-kernel exponent.

## Assumptions and scope
The Hamiltonian, kernel normalization, and boundary-law variables are those of arXiv:1803.02867v1. The integer parameters satisfy \(k\ge2\), \(m=2n+1\), and \(\theta_c<1\), equivalently \((k-1)m>2\). The asymptotic is one-sided from the phase-coexistence region \(\theta>\theta_c\). It concerns the translation-invariant splitting Gibbs measures classified by the source; it does not address non-translation-invariant states, extremality, or thermodynamic critical exponents defined from other observables.

## Proof
The source reduces the positive fixed-point problem to an odd polynomial \(P_\theta(z)\). Its linear coefficient is
\[
r_\theta(k,1)=\frac{-km\theta+m+2}{m+2}
=-\frac{km}{m+2}(\theta-\theta_c).
\]
The cubic coefficient at criticality can be read from the first and second sums in the source polynomial. Direct simplification gives
\[
r_{\theta_c}(k,3)=
\frac{2^{2/m}(k-1)\left((k+1)(m+2)^2-6k\right)}{3(m+2)(m+4)}.
\]
For \(k=2\), this formula agrees with the source's leading \(z^3\) coefficient \(2^{2/m}m/(m+2)\). For \(k\ge3\), it is the ordinary cubic coefficient. It is positive in the interior-transition regime, consistently with the source's strict ordering of coefficient sign-change thresholds.

Set \(\delta=\theta-\theta_c\) and \(w=z^2\). Since \(P_\theta\) is odd, division by \(z\) near the nonzero branch gives an analytic equation
\[
0=-\frac{km}{m+2}\delta+r_{\theta_c}(k,3)w+O(\delta w+w^2).
\]
The derivative with respect to \(w\) at \((w,\delta)=(0,0)\) is the strictly positive number \(r_{\theta_c}(k,3)\). The implicit-function theorem therefore gives
\[
w=\frac{km}{(m+2)r_{\theta_c}(k,3)}\delta+O(\delta^2).
\]
Taking the positive square root yields
\[
z_0=2^{-1/m}\sqrt{\frac{3km(m+4)}{(k-1)\left((k+1)(m+2)^2-6k\right)}}\sqrt{\delta}+O(\delta^{3/2}),
\]
as claimed. The negative branch follows from oddness of \(P_\theta\). The source proves that these two roots reconstruct the two additional positive boundary laws.

## Verification
The accompanying `verify.py` checks the cubic-coefficient simplification exactly after removing the common factor \(2^{2/m}\). It then builds the source polynomial directly from its two sums, isolates the unique positive root by bisection for several admissible \((k,m)\), and verifies convergence of \(z_0/\sqrt{\theta-\theta_c}\) to the displayed amplitude. These finite checks corroborate the analytic proof; they are not used to infer the all-parameter asymptotic.

## Relationship to prior work
The primary paper proves the exact threshold \(\theta_c=(2n+3)/(k(2n+1))\), the one-versus-three count of positive translation-invariant splitting Gibbs measures, and uniqueness of the positive nontrivial root \(z_0\). Its inspected proof determines signs and positivity bounds for \(z_0\), but does not state a critical exponent or the amplitude above.

The 2014 predecessor treats the special case \(n=1\) for arbitrary \(k\), and the 2017 predecessor treats arbitrary \(n\) at \(k=2\). The 2018 paper explicitly identifies those as special cases subsumed by its general theorem. Published-record and semantic-database searches did not locate a square-root onset formula or equivalent amplitude for this model. Because the earlier papers were not both available for complete full-text comparison during this review, an equivalent special-case expansion in weakly indexed literature remains a residual originality risk.

## Limitations
The claim is local to the bifurcation and does not give a closed form for \(z_0(\theta)\) away from criticality. It assumes \(\theta_c<1\); cases with \(\theta_c\ge1\) have no physical supercritical interval within \(0\le\theta<1\). No claim is made about other Gibbs-state classes, susceptibility, free energy, correlation length, or universality beyond this exactly reduced boundary-law order parameter.

## References
1. G. Botirov and B. Jahnel, “Phase transitions for a model with uncountable spin space on the Cayley tree: the general case,” arXiv:1803.02867v1; Positivity 23 (2019), 291–301, DOI:10.1007/s11117-018-0606-1.
2. B. Jahnel, C. Külske, and G. I. Botirov, “Phase Transition and Critical Values of a Nearest-Neighbor System with Uncountable Local State Space on Cayley Trees,” Mathematical Physics, Analysis and Geometry 17 (2014), 323–331, DOI:10.1007/s11040-014-9158-1.
3. G. I. Botirov, “A model with uncountable set of spin values on a Cayley tree: phase transitions,” Positivity 21 (2017), 955–961, DOI:10.1007/s11117-016-0445-x.
