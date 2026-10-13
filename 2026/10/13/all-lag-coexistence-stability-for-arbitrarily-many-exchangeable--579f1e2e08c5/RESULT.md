# All-lag coexistence stability for arbitrarily many exchangeable behaviorally coupled pathogens

## Finding
For every finite \(n\ge2\), the exchangeable \(n\)-pathogen extension of the two-pathogen behavioral-spillover SIRS model has exactly one strictly positive coexistence equilibrium if and only if \(\mathcal R_0>1\). That equilibrium is symmetric and hyperbolically attracting for all positive recovery, waning-immunity, and perception-adjustment rates, all nonnegative behavioral sensitivities, and every spillover fraction in \([0,1]\). The proof rules out equilibrium symmetry breaking and local Hopf instability at coexistence; it does **not** claim global convergence.

## Assumptions and scope
Take an integer \(n\ge2\), rates \(a,b,c,\beta_0>0\), behavioral sensitivity \(k\ge0\), and spillover fraction \(s\in[0,1]\). Disease \(i\) has state \(S_i,I_i,R_i,P_i\) with \(S_i+I_i+R_i=1\), no cross-immunity, and its own exponential risk-perception filter. Set
\[
 m_i=\exp(-kP_i),\qquad Q(z)=1-s+s\exp(-kz),\qquad
 \beta_i=\beta_0m_i\prod_{j\ne i}Q(P_j).
\]
For all \(i=1,\ldots,n\), the complete equations are
\[
 \dot S_i=-\beta_iS_iI_i+bR_i,\qquad
 \dot I_i=\beta_iS_iI_i-aI_i,\qquad
 \dot R_i=aI_i-bR_i,\qquad
 \dot P_i=c(I_i-P_i).
\]
The physical smooth phase space consists of \(n\) product simplices \(S_i,I_i,R_i\ge0\), \(S_i+I_i+R_i=1\), with nonnegative \(P_i\). In the interior use coordinates \((S_i,I_i,P_i)\), so the linearized physical system has dimension \(3n\), not \(4n\). Parameter identifications with the original two-pathogen formulation are \(a=1/\tau_I\), \(b=1/\tau_R\), \(c=1/\tau_P\), and \(\mathcal R_0=\beta_0/a\). The product across other pathogens is the natural exchangeable extension of the original two-pathogen multiplier; it is an explicitly defined mathematical extension, not a claim that the original article modeled more than two pathogens.

## Proof
**Existence and absence of asymmetric coexistence.** At a strictly positive equilibrium, \(P_i=I_i\), \(R_i=aI_i/b\), and \(S_i=1-\eta I_i\), where \(\eta=1+a/b>1\). Thus \(0<I_i<1/\eta\), and the infection balances give, with \(\mathcal R_0=\beta_0/a\),
\[
 1=\mathcal R_0 f(I_i)\prod_{j\ne i}Q(I_j),\qquad
 f(z)=(1-\eta z)e^{-kz}.
\]
Since every \(Q(z)>0\), division by the full product \(\prod_jQ(I_j)\) shows that \(g(I_i)=f(I_i)/Q(I_i)\) is independent of \(i\). On \(0\le z<1/\eta\),
\[
 \frac{d}{dz}\log g(z)
 =-\frac{\eta}{1-\eta z}
  -k\left(1-\frac{s e^{-kz}}{Q(z)}\right)<0,
\]
because \(0\le s e^{-kz}/Q(z)\le1\). Hence all \(I_i\) coincide, say at \(x\), and all other compartments also coincide. The common equilibrium equation is
\[
 F(x)=\mathcal R_0(1-\eta x)e^{-kx}Q(x)^{n-1}=1.
\]
The continuous function \(F\) is strictly decreasing on \([0,1/\eta]\), with \(F(0)=\mathcal R_0\) and \(F(1/\eta)=0\). It has exactly one root \(x\in(0,1/\eta)\) if and only if \(\mathcal R_0>1\). The remaining states are \(S=1-\eta x>0\), \(R=ax/b>0\), and \(P=x>0\).

**All-mode Jacobian reduction.** Work in the reduced state \((S_i,I_i,P_i)\). At the coexistence equilibrium define
\[
 u=\beta x=\frac{ax}{S}>0,\quad
 w=\frac{s e^{-kx}}{1-s+s e^{-kx}}\in[0,1],\quad
 \gamma=akx\ge0.
\]
On perturbing the perceived prevalences, the linearized transmission response in a disease's susceptible/infectious equations is respectively
\[
 +\gamma\left(\delta P_i+w\sum_{j\ne i}\delta P_j\right),\qquad
 -\gamma\left(\delta P_i+w\sum_{j\ne i}\delta P_j\right).
\]
The all-to-all coupling matrix on \(\delta P\) is \((1-w)\mathbf I_n+w\mathbf1\mathbf1^{\mathsf T}\). Its eigenvalue is \(\theta_+=1+(n-1)w\) on the common mode and \(\theta_-=1-w\) on the \((n-1)\)-dimensional zero-sum subspace. Both are nonnegative. For either \(\theta\), the corresponding block in \((\delta S,\delta I,\delta P)\) is
\[
 M(v)=\begin{pmatrix}
 -u-b&-a-b&v\\u&0&-v\\0&c&-c
 \end{pmatrix},\qquad v=akx\theta\ge0.
\]
The matrix of the complete linearization is orthogonally similar to one \(M(akx\theta_+)\) block and \(n-1\) identical \(M(akx\theta_-)\) blocks. Hence the full spectrum is accounted for, including every transverse direction.

**Strict Hurwitz certificate.** Direct expansion gives
\[
 \det(z\mathbf I_3-M(v))=z^3+A_1z^2+A_2z+A_3
\]
where
\[
 A_1=b+c+u,\quad
 A_2=u(a+b)+c(b+u+v),\quad
 A_3=c\bigl(u(a+b)+bv\bigr).
\]
All coefficients are strictly positive and their third-order Routh--Hurwitz determinant is exactly
\[
 A_1A_2-A_3
 =(b+u)\{u(a+b)+c(b+u+c)\}+cv(u+c)>0.
\]
By the cubic Routh--Hurwitz criterion both \(M(v)\) blocks are strictly Hurwitz for every \(v\ge0\). Consequently all \(3n\) physical eigenvalues have negative real part. Smooth linearization theory gives local exponential asymptotic stability. The strict inequalities exclude any zero or purely imaginary eigenvalue at positive coexistence, for every finite admissible parameter choice.

## Verification
The entire proof is symbolic; it does not rely on finite enumeration to establish a universal statement. The standalone Python-3 script `verify.py` constructs the characteristic polynomial directly from a three-by-three determinant using exact rational polynomial arithmetic, checks the coefficient identities and the displayed positive Routh--Hurwitz factorization, and independently tests both the common and zero-sum invariant-mode reductions of the full linearization. Reproduce with `python3 verify.py`. The test covers a finite grid of representative positive rates, dimensions, and spillover weights, including zero response and perfect spillover; its output is `VERIFY_OK 2916 exact rational characteristic-polynomial and invariant-mode checks`. Finite testing supplements, but does not replace, the preceding unrestricted algebraic proof.

## Relationship to prior work
LeJeune, Saucedo, Childs, and Ghaffarzadegan (arXiv:2510.19153, first publicly available 2025-10-22; later Journal of Biological Dynamics DOI below) introduced the two-pathogen behavioral-spillover SIRS formulation. They proved coexistence stability for the no-spillover case, while their Tables 4 and 5 expressly label the positive-coexistence stability conditions under perfect or imperfect spillover as conjectures. Their manuscript does not give an all-parameter stability proof for those coupled cases, nor an all-\(n\) result. The present exchangeable theorem proves those conjectured implications when the pathogens share baseline parameters, and extends the conclusion to every finite number of identically parametrized pathogens. The equal-parameter hypothesis is substantive: the argument uses the complete-graph coupling's nonnegative symmetric and transverse eigenvalues.

Blyuss (arXiv:1311.4808) previously developed eigenmode and equivariant-symmetry approaches for multi-strain disease models, but analyzed antigenic cross-immunity rather than delayed behavioral suppression. That prior method motivates the reduction, not the positivity of the specific cubic Hurwitz determinants established here. Gavish (DOI below) studies a distinct partial-cross-immunity SIR framework and can exhibit instability; its dynamics contain neither these perceived-infection states nor the present waning-immunity/spillover mechanism. Berry and coauthors (DOI below) consider adaptive behavior and vaccination in an SIR model but do not supply an all-pathogen exchangeable behavioral-spillover theorem in the available source evidence.

## Limitations
Stability is local on the physical simplex and is not a claim of global attraction, global elimination of periodic orbits, or robustness to arbitrary pathogen heterogeneity. Each \(n\) is finite and all diseases share \(\beta_0,a,b,c,k,s\). Heterogeneous infections, cross-immunity, vaccination, seasonality, other risk-perception kernels, and network-specific behavioral spillover are outside the result. Stability need not have a decay rate uniform as \(c\to0\), \(n\to\infty\), or \(\mathcal R_0\downarrow1\). The uniqueness claim concerns strictly positive coexistence equilibria; disease-free and boundary equilibria can also exist. Methodological antecedents in multi-strain equivariance and possibly unindexed mathematical epidemiology create residual literature-overlap risk.

## References
1. L. LeJeune, O. Saucedo, L. M. Childs, N. Ghaffarzadegan, *The behavioral spillover effect: Modeling behavioral interdependencies in multi-pathogen dynamics*, arXiv:2510.19153v1 (2025-10-22); v2 (2026-04-17); *Journal of Biological Dynamics* 20 (2026), doi:10.1080/17513758.2026.2676366.
2. K. B. Blyuss, *Analysis of symmetries in models of multi-strain infections*, arXiv:1311.4808; *Journal of Mathematical Biology* 69 (2014), doi:10.1007/s00285-013-0740-0.
3. N. Gavish, *Hidden Oscillations: How Minimal Immunological Interactions Destabilize Two-Strain Epidemic Models*, *SIAM Journal on Life Sciences* 1 (2026), doi:10.1137/25M1826160.
4. T. Berry, M. Ferrari, T. Sauer, S. J. Greybush, D. Ebeigbe, A. J. Whalen, S. J. Schiff, *Existence and stability of equilibria in infectious disease dynamics with behavioral feedback*, *Physical Review E* 111 (2025), doi:10.1103/PhysRevE.111.014317.
