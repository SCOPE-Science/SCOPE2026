# Independent mathematical audit

## correctness

PASS

PASS: For a binary run decomposition with lengths a1,...,am, a left-minimal mixed interval starts exactly at the last letter of run i-1 and ends in run i. Thus L_w(h)=sum_{i=2}^m 1_{2<=h<=a_i+1}, delta(2)=m-1, delta(j+2)=-multiplicity of noninitial run length j. The multiset of noninitial run lengths is a partition of t=n-a1, 0<=t<=n-1, and every such partition is realizable by alternating runs. The sole negative jump outside observable lengths occurs at partition (n-1), which has unique delta2=1 and no later jump, distinct from the empty zero profile. Fibers have two initial letters and permutations k!/prod m_j!, with exceptional and empty fibers each of size two. Distinct k positive run lengths cost at least k(k+1)/2 symbols after the first, giving sharp d=1+floor((sqrt(8n-7)-1)/2) for n>=3 and 2k! shortest extremizers (k>=2); n=1,2 checked separately. Independent direct mixed-window enumeration of all words n<=11 matched cumulative partition counts 1,2,4,7,12,19,30,45,67,97,139 and total word mass.

## originality

PASS

PASS, qualified: Bille–Gortz–Stordalen 2022 already prove generic left-minimal co-occurrence interval decomposition and sparse first-difference bounds; OEIS A000070 already lists the numerical cumulative partition sequence. The new contribution is the exact binary-specialized attainable-profile bijection, all fiber sizes and sharp extremal support, not the count sequence itself or a generic co-occurrence data structure. Sobel et al. 2021 use all-window co-occurrence queries, not left-minimal profile equivalence classes. A specialized unindexed binary example of the general lemma may exist.

## value

PASS

PASS: Profile ambiguity is central to the information content of all-window-length co-occurrence queries. Exact classes, fiber sizes and sparse-support extremizers are natural complete binary classifications not implied merely by big-O space bounds; the exceptional length-(n-1) run boundary is essential. Known integer partition numbers alone are not proposed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
