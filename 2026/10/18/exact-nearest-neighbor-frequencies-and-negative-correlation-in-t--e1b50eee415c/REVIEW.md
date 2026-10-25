# Independent mathematical audit

## correctness

PASS

For all n>=0 define recurrence a(0)=0,a(1)=1,a(n)=n-a(n-a(n-a(n-1))) and increments d(n); the infinite morphic representation is a stated premise from Cloitre–Ma–Zhang, not inferred from a finite prefix. The productive 25-symbol substitution has incidence matrix M primitive because M^20 has all positive entries; its Perron root rho solves rho^3=rho+1. Letter frequencies v solve Mv=rho v. Every internal symbolic ordered pair contributes b_{uv}; each prior boundary pair maps to (last mu(u),first mu(v)), giving a 67-state deterministic Q and exact balance (rho I-Q)w=b. Since spectral radius(Q)=1<rho, w is uniquely determined. Count output 11 internally within eta(q) and across paired boundaries, normalize by mean output length L=1-rho+rho^2. Exact symbolic algebra in inspected verify.py is designed to verify P11=(4+9rho-8rho^2)/7 and output normalization; independent separately reconstructed PF/pair numerical system obtained P11≈0.2690628978898806 and covariance≈-0.0556550593548617, agreeing with formula. Stationarity yields P10=P01=rho^-2-P11 and P00=1-2rho^-2+P11, with rho^-2=1+rho-rho^2. Covariance (11+2rho-8rho^2)/7 is negative since rho>33/25 and its numerator is decreasing for x>1/8 and negative at 33/25. Finite prefix or floating checks alone are not exact cubic field certificates.

## originality

PASS

The cited primary authors published the substitution and one-letter increment frequency, but not the exact adjacent binary-pair vector or quantified negative lag-one covariance. This naturally calculable statistic is not automatically a stated/known result and its algebraic closed form is a specific new calculation. Best-of-knowledge PASS, with implicit-literature risk.

## value

PASS

For a newly characterized nested recurrence, the nearest-neighbor joint law is the canonical first statistic beyond single-bit density. The exact four-cell algebraic distribution and strictly negative covariance demonstrate genuine local repulsion instead of independent Bernoulli increments, using a nontrivial 67-state boundary transfer. This precise natural invariant has value independent of any larger mixing theorem; no arbitrary lag selection is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
