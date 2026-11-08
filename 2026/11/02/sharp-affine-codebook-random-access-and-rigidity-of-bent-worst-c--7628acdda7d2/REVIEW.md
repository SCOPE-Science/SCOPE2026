# Independent mathematical audit

## correctness

PASS

For even m>=2, Parseval H^T H=NI gives sum_a W_a^2=N^2; inverse Walsh gives E decoded sign=(N/S)s_x under mixture |W_a|/S, hence per-coordinate (1+N/S)/2. Cauchy gives S<=N sqrt(N), strict for any nonbent. Quadratic sum x_{2j-1}x_{2j} is bent for all even m. At bent s, average signed success <=1/sqrt N from sum |t_a|<=1; all-coordinate optimality forces equality, inverse Walsh fixes t_a=sgn(W_a)/N, and termwise saturation uniquely fixes every p_{a,b}. Independent direct character-sum truth-table enumeration recovered exactly 8 maximizers for m=2 and 896 for m=4; finite census supports but does not prove the all-m claim.

## originality

PASS

Best-of-knowledge contribution is precise fixed RM(1,m) affine-decoder RAC minimax and unique randomized encoder at bent inputs; known Walsh and covering-radius results are explicitly excluded.

## value

PASS

A fixed Reed-Muller affine codebook is natural in finite-bit random access. The exact minimax and uniqueness of the optimizer on every bent hard input give a meaningful operational interpretation and rigidity strengthening of known Walsh flatness, with precise unavoidable restriction to this decoder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
