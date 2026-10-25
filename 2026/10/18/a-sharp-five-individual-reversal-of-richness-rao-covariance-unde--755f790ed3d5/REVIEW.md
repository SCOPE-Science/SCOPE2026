# Independent mathematical audit

## correctness

PASS

Uniform sampling of m labeled individuals without replacement makes Rao Q_m the sum of sampled off-diagonal species distances divided by C(m,2). For N<=4, m=N gives constant richness; m=2 has Q=0 at richness one and Q>=0 otherwise. At N=4,m=3, all abundance types are trivial except (2,1,1), where the two omitted-individual categories have probability one-half, conditional mean-Q difference d(B,C)/3 and covariance d(B,C)/12>=0. In a population (2,1,...,1) with r singleton species sampled at m=r+1, omission of a doubleton member has probability 2/(r+2), while omission of singleton has r/(r+2); conditional distance-counting gives 4*(2V−(r−2)U)/((r+2)^2*r*(r+1)) exactly. Substituting U=rH,V=C(r,2)ℓ gives 4*((r−1)ℓ−(r−2)H)/((r+2)^2*(r+1)); negative iff H/ℓ>(r−1)/(r−2). For r=3, (H,ℓ)=(3,1), exact covariance for m2..m5 is (21/100,3/100,-1/25,0). For fixed H/ℓ>1 choose r>2+1/(H/ℓ−1), proving star-limit instability, not a finite extrapolation. Independent exact Fraction labeled-subset enumerations and inspected check.py corroborate all bounded instances.

## originality

PASS

Best-of-knowledge: prior diversity sources establish expected functional rarefaction or deterministic nonmonotonicity under species additions, not the cross-statistic covariance and sharp minimum N=5. A published positive richness–unbiased Gini–Simpson covariance theorem is limited to iid sampling and equal-distance specialization, so it cannot rule out or imply an ultrametric negative result with sampling without replacement. Highly relevant 2009 Rao optimization full text could not be obtained: authorized institutional retrieval reported VPN disconnected; treated as explicit residual risk, not scientific failure.

## value

PASS

The dependence of two established biodiversity sample statistics is an intrinsically motivated mathematical question, not a cosmetic reparametrization. The result gives a universal sharp minimum population N=5 for negative sample richness–Rao covariance, an exact arbitrary-distance near-census criterion, and an ultrametric sign reversal arbitrarily close to equal distances as the clade grows. This supplies an explicit boundary and interpretable phenomenon that first-moment rarefaction or uniform Gini–Simpson positivity would miss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
