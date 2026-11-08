# Independent mathematical audit

## correctness

PASS

For a mutation-free, well-mixed discrete-time Moran birth-death chain with self-replacement, one-step gain/loss probabilities are u_j(w)=j(N-j)w/[N(jw+N-j)] and d_j(w)=j(N-j)/[N(jw+N-j)]. Writing drift g_w(j)=u_j-d_j, two-step fitness order gap is the commutator of transition kernels applied to the count function. Independent SymPy derivation from the two-step kernel reproduced all six exact expressions for N=2,3,4 and interior k; all have the positive factor (a-b), except (N,k)=(4,2), which has further P(a,b)=[3a²b²+6a²b−9a²+6ab²+116ab+6a−9b²+6b+3] and strictly positive displayed denominator. The identities P(1+x,1+y)=H(x,y)>0 and P((1+x)^-1,(1+y)^-1)=H(x,y)/[(1+x)²(1+y)²] settle same-side-neutrality signs. For a>1>b, P(a,b)=3(a-1)(a+3)b²+(6a²+116a+6)b−3(a-1)(3a+1) is strictly increasing in b, negative at b=0, positive at b=1; hence a single root b*(a) gives exactly the sign reversal. Fresh exact matrix-product checks reproduce Delta_4,2(5,1/5)=-1/96 and Delta_4,2(5,1/2)=5/224. Four is minimal among N=2,3,4. No fixation probability or multi-generation claim.

## originality

PASS

Best-of-knowledge PASS for smallest population of deterministic two-single-update Moran order reversal and its unique cross-neutrality threshold. General Moran fixation analyses in temporally varying random environments address different observables and often different temporal protocols. Although the formula follows from transition matrices, neither the sign classification nor minimum four-population result was found in inspected primary literature. Priority risk of an implicit commutator theorem remains.

## value

PASS

A strict, sharply parameterized reversal of the intuitive stronger-first ordering appears at the first population size permitting it. It determines the entire six-case low-N classification and exact threshold for a natural two-epoch dynamical statistic, not an arbitrary small-instance value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
