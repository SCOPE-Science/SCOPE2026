# Independent mathematical audit

## correctness

PASS

The exact two-box ODE has generator [[-k-ell1,k],[k,-k-ell2]] and initial (1,0). Writing m=(ell1+ell2)/2, delta=(ell1-ell2)/2 gives x2(T;k)=exp(-(k+m)T)k*sinh(T sqrt(k²+delta²))/sqrt(k²+delta²) by a 2x2 matrix exponential. For dimensionless y=kT, r=(Tdelta)², the log derivative of y exp(-y)sinh(sqrt(y²+r))/sqrt(y²+r) is D=r/[y(y²+r)]+y/z*coth(z)-1. When r>0, D is positive near zero and negative for large y. Substitution of its critical equation yields D_y|D=0=-r(y²-3y+3)/(y²(y²+r))<0, so all crossings are strictly downward and the root is unique and globally optimal. D(1,r)>0 proves y*>1. The sign D_r<0 follows from positive hyperbolic series H(z)=z sinh z cosh z+z²-2sinh²z=sum_{n>=3}[(n-2)2^(2n-1)/(2n)!]z^(2n); hence the root strictly decreases as r increases. Limits r down to0 and up to infinity and peak above perfect-mixing value follow. At r=0 response (1-exp(-2y))/2 is monotone with no finite optimum. Swapping losses leaves x2 invariant. Independent symbolic curvature identity and numerical roots confirm, not replace, all-r proof.

## originality

PASS

Best-of-knowledge PASS. The archived National Simulation Resource Comp2ExchangeReaction model has precisely the prior art two-box exchange plus independent losses and exact governing equations, and its four-page guide studies time courses but not a theorem globally optimizing the receiver concentration over k at fixed horizon. The Comp2Exchange no-loss model is an even simpler known specialization. The candidate new finding is the global optimizer uniqueness, threshold at equal losses, y*>1, strict contrast monotonicity and above-fast-mixing peak. Historical transport literature may have an equivalent optimization under another name; inaccessible full 1984/2000 texts are explicitly retained as risks.

## value

PASS

Exchange-rate tuning at a finite observation time is a physically and mathematically natural design parameter: strong mixing need not maximize downstream snapshot when losses differ. The sharp unique exchange optimum, its dimensionless lower bound and contrast sensitivity make an exact interpretable boundary in the minimal reactive two-zone model; not just a restatement of its textbook ODE or a tiny numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
