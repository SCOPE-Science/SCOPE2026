# Independent mathematical audit

## correctness

PASS

For m>=2 let Y_j=j(X_[j]-X_[j+1]) on ordered uniform simplex (X_[m+1]=0). This is a bijective linear map of constant Jacobian to the full simplex, so Y~Dirichlet(1,...,1). Then X_[k]=sum_{j=k}^m Y_j/j and Q=sum_{a,b} Y_aY_b/max(a,b). Direct factorial Dirichlet moments of degree three give Cov(Y_j,Q)=2(T_{m,j}-1)/(m(m+1)(m+2)), hence Cov(X_[k],Q)=(T_{m,k}²+U_{m,k}-2T_{m,k})/[m(m+1)(m+2)], where T=sum_{j>=k}1/j, U=sum_{j>=k}1/j². For W equal to numerator, W_k-W_{k+1}=2(T_k-1)/k, and T_k strictly decreases in k: W first decreases then increases; W_1>0 and W_m<0 ensure exactly one positive-to-negative sign boundary (possible one zero). At k=ceil(theta*m), T->log(1/theta), U->0, so threshold fraction r_m/m->e^-2. Verified 44 all-rank covariance values via independent degree-three factorial-moment integration for m=2..9 and all 349 complete sign profiles m=2..350 with rational arithmetic. No finite extrapolation used for arbitrary m.

## originality

PASS

Known ordered-spacing joint distributions (Rao–Sobel 1980) and marginal squared-spacing distributions/quantiles (Royen 2010) are acknowledged as foundations. The claimed additional joint-moment simplification to two harmonic tails and sharp positive-rank fraction e^-2 is not stated in inspected source material. A broad incomplete-Dirichlet integral formula could permit a derivation, but source comparison found no already published exact rank sign boundary.

## value

PASS

The covariance of each descending order statistic with the canonical Greenwood quadratic concentration index is a natural finite-sample dependence invariant, and its exact harmonic formula plus universal e^-2 rank cutoff make a useful quantitative classification across sample size. It is neither a marginal Greenwood table recomputation nor simply a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
