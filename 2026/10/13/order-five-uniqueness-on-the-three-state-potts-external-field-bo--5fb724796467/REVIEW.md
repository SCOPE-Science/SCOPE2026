# Independent mathematical audit

## correctness

PASS

Directly differentiated K=L(p+1)^5/(p+L)^5 with p=v+v²+v³+v⁴,L=t p-v⁵-1,t=theta-1. Verified exact factorization K'(v)=(p+1)^4/(p+L)^6*(v-1)(v+1)v^5 R(v+1/v;t) and expansion R(2+z;t)=50(4t²+8t-7)+10(30t²+32t-119)z+10(17t²-4t-120)z²+(43t²-111t-550)z³+2(t-12)(2t+5)z⁴-2(2t+5)z⁵. For t in (1/2,(sqrt11-2)/2], all nonconstant coefficients strictly negative; constant is <=0. Hence R<0 for z>0 and K is strictly decreasing for v>1, reciprocal invariant under v->1/v, so unique maximum at v=1. At v=1 L=4t-2>0, so this is in physical domain. Original boundary-law reconstruction yields u=(4theta-2)/5. Independent Sympy expansion reproduced the factor and six z coefficients, not only the verifier log. This is an all-positive-v sign proof, not finite sampling.

## originality

PASS

Bogachev and Rozikov actually state Conjecture 2.1 in their primary mathematical paper and prove the global maximizer only for orders k=2,3,4 in Appendix B; their later survey still describes these orders. The k=5 reciprocal-polynomial certificate is not a restatement of their k<=4 instances, and does not follow from the numerical threshold values alone. Thus this is a new next-order case, best of knowledge.

## value

PASS

Resolving the first previously open tree order of a concrete conjecture on the critical external-field Gibbs uniqueness boundary is motivated mathematics. The exact globally negative reciprocal derivative polynomial is a significant structural certificate and potentially informative for higher orders; not a routine parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
