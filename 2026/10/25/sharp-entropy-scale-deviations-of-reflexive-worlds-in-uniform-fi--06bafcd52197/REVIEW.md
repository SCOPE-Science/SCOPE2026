# Independent mathematical audit

## correctness

PASS

Seriality makes successor sets nonempty. Transitivity and right-Euclideanness force S(v)=S(u) on uRv, hence distinct successor sets disjoint; their fibers partition W and each contains its nonempty reflexive set, giving a bijection with partitions carrying nonempty marked subsets in each block. Uniform ordinary set partition plus independent fair Bernoulli vertex marks, conditioned on at least one mark in every block, gives exactly uniform decorated partitions. The number of blocks K_n in a uniform ordinary partition satisfies E K_n=o(n): for q=floor(n/log n), onto-function count yields Bell lower log B_n >= n log n-n log log n-O(n), whereas partitions with >=epsilon n blocks have numerator at most n^{n+1}/ceil(epsilon n)!; their ratio decays. Thus P(A)>=2^{-E K}=exp(-o(n)). Conditional on precisely m~alpha n marks, on K<=2 E K+1 (partition probability >=1/2), requiring fixed representatives to be marked costs at worst (alpha/2)^K=exp(-o(n)). So P(M=m)=Bin(n,m)2^-n P(A|Z=m)/P(A), giving binomial rate I(alpha) by Stirling and Chernoff matching tails with a single interior m. Independent exact recurrence for T(n,m) matched decorated partitions through n=11, finite corroboration only. Endpoints alpha=0,1 and CLT/local relative-error not claimed.

## originality

PASS

OEIS A143396 already gives exact T(n,m) and EGF exp(exp((1+y)z)-exp(z)); A143405 gives totals and a 2026 relational interpretation. Kotěšovec's 2022 work analyzes asymptotic row totals. The inspected sources do not state the conditional binomial entropy-rate for reflexive-world density. A general combinatorial-assembly large-deviation theorem might imply it and remains a real priority risk.

## value

PASS

The fraction of reflexive worlds is an intrinsic semantic statistic of the uniform labelled KD45 frame ensemble. The sharp entropy-rate theorem goes substantially beyond a preexisting exact counting triangle by proving that an occupancy/conditioning constraint has subexponential cost, giving typical 1/2 and exponential tail profiles useful for random-frame modeling. It does not misrepresent the known finite combinatorics as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
