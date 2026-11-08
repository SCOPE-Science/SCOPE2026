# Independent mathematical audit

## correctness

PASS

For N>=2 and a,b,c>0 the age since the last complete Poisson reset is Exp(c). Conditioning on it gives the exact scaled-Beta(1,alpha) binomial-mixture integral for P_k, alpha=c/(a+b), rho=a/(a+b). The adjacent ratio is a positive constant times E_{k,alpha}[U/(1-rho U)]; likelihood-ratio ordering under (1-u)^(alpha-1) makes it strictly decreasing in alpha with boundary limits (N-k)rho/((k+1)(1-rho)) and 0. Hence k<h=ceil((N+1)rho)-1 gives precisely one unit crossing and k>=h gives none. The stationary balance recurrence b(k+1)Delta_k=a(N-k+1)Delta_(k-1)+(c-a-b)P_k implies one-peaked mass sequence, and successive unit crossings are strictly ordered by applying it to Delta_(k+1) at Delta_k=0. At alpha>=1, all adjacent differences are strictly negative. Independently recomputed exact rational stationary mass vectors at N=4,rho=1/2 and several adjacent ratios; the finite checks corroborate but do not prove all parameters.

## originality

PASS

The all-N consecutive mode-switch staircase is not stated in the inspected unbounded immigration/death with partial catastrophe model or in the accessible 2007 finite-case abstract. Regeneration and stochastic ordering are standard ingredients, not original. The saturating finite-N binomial mixture, its strict adjacent-ratio crossings and globally ordered mode classification together are the assessed claim.

## value

PASS

A complete parameter-sharp classification of the most probable occupied-patch count for a natural finite exchangeable habitat model: it supplies the number, existence and order of all actual mode transitions, not just a mean or a generic stochastic ordering. Boundary rho and alpha dependence matter for interpreting typical occupancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
