# Independent mathematical audit

## correctness

PASS

The original RESULT.md (frozen Git blob 2a150752f94a0aa65620b4590f42bc12ed6d9a8c) gives the exact precontact scalar recurrence X_(n+2)=T X_(n+1)-D X_n-epsilon, with U_0=u,U_1=Tu+v,h_0=h_1=0,h_(n+2)=T h_(n+1)-D h_n+1. Both max gates remain on their positive branches before first contact: X_n=U_n-epsilon h_n, X_(tau)<=0 and Y_tau=-epsilon-D X_(tau-1)<0; two further iterations reach (-epsilon,-epsilon) for the first time. For 0<D<1,0<T<1+D,u>0,v>=0,epsilon>0, companion eigenvalues are stable. When T²<4D an unforced decaying sinusoid has a fixed negative sample, giving tau=O(1) as epsilon->0. For T²>4D, exact positive U_n~c lambda_+^n and h_n->1/(1-T+D) imply tau=log(1/epsilon)/(-log lambda_+)+O(1). At repeated positive root r=sqrt(D), U_n=(u+n(u+v/r))r^n, so tau=[log(1/epsilon)+loglog(1/epsilon)]/(-log r)+O(1). Exact first-crossing thresholds U_n/h_n hold for n>=2 without asserting globally monotonic initial thresholds. Independent Fraction iteration, recurrence and reset gave tau=5,32,80 for (T,D)=(9/10,3/10),(1,1/4),(11/10,6/25), (u,v)=(1,1),epsilon=10^-8. Finite samples corroborate, not prove, the full quantifier statement.

## originality

PASS

Best-of-knowledge PASS for the negative-bias, fixed-seed three-regime first-contact latency, especially the repeated-eigenvalue loglog term. Existing exact homogeneous zero-bias extinction/persistence, general max-plus Selkov branch dynamics, and phase-bottleneck delays have different forcing or initial-data normalization and do not directly imply the complete epsilon-downarrow-zero trichotomy. An unindexed older first-passage recurrence theorem could subsume it; this remains a priority risk.

## value

PASS

The reset-time boundary separates bounded focus passage, logarithmic node passage, and an extra loglog critical slowdown at the discriminant. The model is an established max-plus oscillator, the first-switching time is a natural observable, and the critical asymptotic coefficient is exact. It is more than a normalization check or numerical phase plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
