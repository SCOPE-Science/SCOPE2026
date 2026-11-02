# Independent mathematical audit

## correctness

PASS

PASS. For n>=3, M=7*2^n, a=M+1 and S_n=<M2^i+1:i>=0>, published finite-generator and greedy coin-Apéry results imply W(t)=Mt+a ell(t), 0<=t<=M, where ell is minimal coin number for coins 2^i-1 up to i=n+2. An Apéry-maximality criterion gives W(t)-a pseudo-Frobenius iff every eligible coin c_i with t+c_i<=M has ell(t+c_i)<=ell(t); wraparound generator additions are strictly above corresponding Apéry minima. The greedy-digit constraint bounds ell<=n+2, giving the two length-n+2 witnesses tA=4*2^n-n-2 and tB=6*2^n-n-2. Popcount contradiction proves ell(M-j)=j for 3<=j<=n+2, and direct boundary counts ell(M)=4,ell(M-1)=5,ell(M-2)=4 give the n-2 indexed family j5..n+2 plus two endpoints. There are 2+(n-2)+2=n+2 distinct indices, so type>=n+2=e-1; equality of type for all n is NOT established. Independently rebuilt Apéry shortest paths with Dijkstra for n=3,4,5, exactly checked all 57/113/225 residues and each proposed PF witness; actual types equal 5/6/7 in these finite tests. Finite equality is not promoted into a global theorem.

## originality

PASS

PASS best-of-knowledge for a uniform explicit multiplier-seven pseudo-Frobenius family and linear type lower bound, not the known Apéry/greedy algorithm or Frobenius/genus formulas. Srivastava–Thakkar 2023 complete primary text §5 Theorem 5.2 gives full PF sets and types for k=2^r+1, which excludes k=7 since 7-1=6 is not a power of two. Liu–Xin–Ye–Yin 2023 full primary text gives general greedy Apéry formula including this k7 specialization but does not explicitly list the present PF witnesses; a simple consequence might exist for experts, but deriving an unbounded maximal-element family via sharp popcount constraints is additional content. Related general semigroup algorithms can compute examples but are not a preexisting all-n witness theorem. The result claims only lower bound, preserving its limited scope.

## value

PASS

PASS, narrowly. Type is a central numerical-semigroup invariant, and a family of at least e(S)-1 explicit distinct maximal gaps for the natural Proth multiplier seven is a linear, uniform structural obstruction rather than an arbitrary finite sample. The result is a meaningful lower bound despite not determining exact type; its value depends on the explicit uniform family and cannot be attributed to the known generic algorithm alone. Earlier multiplier 2^r+1 exact types are prior and not reassigned novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
