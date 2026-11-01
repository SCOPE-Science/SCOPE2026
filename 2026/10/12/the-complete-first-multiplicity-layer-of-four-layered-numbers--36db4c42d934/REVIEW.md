# Independent mathematical audit

## correctness

PASS

For n=∏p_i^{a_i}, four equal divisor-sum parts imply σ(n)/n≥4. For any prime-power factor, A_a(p)=∑_{j=0}^a p^{-j}<p/(p−1); if m prime-factor slots remain, every continuation is bounded above by R times the Euler factors of the m smallest unused primes. Candidate next-prime upper envelope R·p/(p−1)·E(p,m−1) decreases with p and tends to R; induction over smaller Ω establishes every proper prefix R<4 and hence rigorous termination for Ω≤8 without a guessed prime bound. Independently coded exact Fraction depth-first search returned no σ≥4n integers for Ω=1..7 and exactly 27720,32760,120120,180180,235620 for Ω=8, matching the source traversal counts (1,1,1,1,1,3,8,33 nodes; 58 Ω=8 prime trials, maximum tested 19). Independent distinct exponent-partition/permutation scan of all 22 partitions of Ω=8 finds exactly three viable patterns and all lower-layer maxima <4; this crosschecks pruning independently. Parsed actual partitions.json blob e00f0240... via GitHub and independently reconstructed each complete divisor set and bin sums: all five four-part partition certificates verify, with 96,96,128,144,144 divisors. Exact ratios 312/77,4,576/143,224/55,3744/935 and Ω=8 verified. Program execution alone is not a global proof: the rigorous envelope, induction and termination justify exhaustion.

## originality

PASS

Best-of-knowledge originality: a global minimum total-prime-multiplicity classification for all four-layered integers, including an exact five-element fiber and sufficiency of four-abundancy within Ω≤8, is not implied by the checked primary results or finite OEIS tables. The exact quadriperfect theorem covers only σ(n)=4n (one of five); Jokar establishes the least integer and treats a restricted four-distinct-prime shape; Mahanta–Saikia–Yaqubi treat small distinct support. A392936 records all five examples as primitive four-abundant terms and discusses branch-and-cut search, but lists terms in numerical order rather than proving exhaustive Ω≤8 classification. Priority risk: an older or unindexed multiplicity-boundary classification or a dominating complete primitive-abundant classification may exist.

## value

PASS

The smallest total number Ω of prime factors permitting a four-way equal divisor-sum partition is an intrinsic natural boundary, distinct from the smallest numerical example. The exact five-element equality fiber (including 235620 beyond the displayed 31-term four-layered list) is a motivated complete classification and proves a nontrivial equivalence between a necessary abundancy inequality and actual layeredness in this minimal layer. The witness partitions and mathematically terminating unbounded-prime search supply precise facts useful for future k-layered and divisor-sum multiplicity investigations. This does not claim classification at Ω≥9 or a general abundance-to-partition theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
