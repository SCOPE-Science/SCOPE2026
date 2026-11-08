# Independent mathematical audit

## correctness

PASS

For C>0, h>0, x0!=0, r0=q(x0), elimination of the positive-root square-law SAV BE equations yields r_{n+1}=r_n/sqrt(1+h(x_n/q(x_n))^2), x_{n+1}=x_n-h(x_n/q(x_n))r_{n+1}; modified-energy decrement equals -(x_{n+1}-x_n)^2/h. For large h, first step sends x1=-sgn(x0)q0 sqrt(h)+x0+O(h^-1/2), r1=O(h^-1/2). A bootstrap keeps |x_j|>=q0 sqrt(h)/2 and opposite sign for j>=1; c(x_j)^2>=1 yields geometric decay of r_j and bounded total later displacement. The second step contributes q0^2/x0+O(h^-1), subsequent steps O(h^-1/2), giving X_h=-sgn(x0)q0 sqrt(h)+x0+q0^2/x0+O(h^-1/2). Algebraic C=x0=1,h=100 bounds X<-73/8 while auxiliary falls to 0; tests at three h values corroborate only.

## originality

PASS

PASS qualified: Huang–Liu–Wang–Yan introduced the same positive-root SAV step and modified-energy dissipation, but their inspected full 17-page paper treats algorithmic positivity and numerical examples, not the shown fixed-step infinite-time scalar amplification. Earlier SAV wrong-equilibrium warnings by Bouchriti et al. concern related general phenomena, not this sharp asymptotic, but priority risk remains.

## value

PASS

A transparent convex one-variable counterexample to equating auxiliary positivity and modified-energy decay with physical convergence is a motivated stability boundary for a recent numerical integrator; the quantitative sqrt(h) amplification and exact finite h witness are not routine restatements of SAV energy decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
