# Independent mathematical audit

## correctness

PASS

With the E matching pairs e_i=(u_i,v_i), F matching pairs f_i=(v_i,u_(i+1)), frozen proof inductively identifies occupied output pairs at step t with cyclic windows of t fully present original E-pairs, respecting parity of step. Full e_i occurs with probability 1/4 independently across i. For nonall-one cyclic words, mark starts of t runs after a zero. Inclusion–exclusion over r cyclic starts separated by at least t+1 yields A(n,t)=4^n−1+Σ(-1)^r(n/r)C(n−rt−1,r−1)3^r4^(n−r(t+1)); all-ones is excluded explicitly. Independent disjoint components multiply extinction CDFs; infinite survival =1−Π(1−4^(−n_i)); a nonfull connected component dies by time n and the single-zero word attains n. Factorial moments for markers at t=floor(log_4n)+j converge to Poisson mean (3/4)4^(theta−j), giving lattice cutoff and phase-dependent limit; finite enumeration is not its proof. Independent direct subset experiment checked 5,460 inputs n≤6.

## originality

PASS

Rough approximation compositions are classical; Gopaulsingh 2016 studies decomposition/reconstruction of two successive operators, which is not a law for random extinction under arbitrarily many alternating matching erosions. Classical iid longest-run Poisson techniques cover run probabilities and are expressly not novel. The surviving statement is the exact identification of the alternating rough-set process with a cyclic run plus the all-cycle-component product CDF and lattice cutoff. Potential equivalent mathematical morphology or automata treatment remains residual.

## value

PASS

The exact extinction-time law links repeated rough set approximation to random cyclic-run extremes for pair partitions, resolving transient duration and permanent persistence in a natural finite operator class. The complete distribution, disconnected component factorization, sharp worst case, and phase-dependent cutoff have independent use; this goes beyond counting isolated small cases or a textbook erosion observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
