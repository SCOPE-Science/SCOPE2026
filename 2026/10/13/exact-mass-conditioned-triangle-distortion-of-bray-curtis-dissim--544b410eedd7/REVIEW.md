# Independent mathematical audit

## correctness

PASS

For fixed endpoint masses m=min(a,c)<=M and middle mass b>0, define alpha=1/(m+b)>=beta=1/(M+b), u0=|m-b| and v0=|M-b|. With u=||x-y||_1, v=||y-z||_1, w=||x-z||_1, have u>=u0,v>=v0,u+v>=w,w<=m+M; thus alpha*u+beta*v>=alpha*u0+beta*max(v0,w-u0)=g(w). Since w/g(w) is nondecreasing on the nonzero-denominator region, the distortion is bounded by 1/g(m+M). Witness x=(m,0), z=(0,M), y=(min(m,b),(b-m)_+) realizes equality with two species. Piecewise evaluation gives (m+b)/(2m) for b<=m; the inverse of (b-m)/(m+b)+(M+2m-b)/(M+b) for m<=b<=m+M; and inverse of (b-m)/(m+b)+(b-M)/(M+b) thereafter. The ratio exceeds one exactly for max{m,M-2m}<b<(m+M+sqrt((m+M)^2+12mM))/2. Algebraic proof valid for all positive real masses and any number >=2 of available species, not only integers. Independent exhaustive exact-fraction checks covered 147 ordered integer mass triples and 15,190 two-species profiles; witnesses and bound matched.

## originality

PASS

Bray–Curtis is known nonmetric and the global sharp multiplicative 3/2 bound for the related Sørensen–Dice index was previously published. The retained claim is the exact SHARP ratio and violation window for every ordered fixed total-mass triple, independent of species count. Relevant Gragera–Suppakitpaisarn 2018 primary source was checked through accessible bibliographic/abstract material but full text could not be acquired; its potential conditional generalization is a material priority risk recorded, not falsely deemed absent.

## value

PASS

This is a natural ecologically motivated refinement because total abundance differences and compositional distance are confounded in Bray–Curtis comparisons. The theorem identifies the exact mass-only interval allowing a triangle violation and gives a universally sharp two-species witness, rather than restating 3/2 or performing an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
