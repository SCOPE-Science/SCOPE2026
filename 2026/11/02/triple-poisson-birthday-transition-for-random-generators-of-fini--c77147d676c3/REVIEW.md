# Review of the triple-Poisson local-algebra birthday transition

## Correctness — PASS

The domain is fixed integers \(f,k\ge1\), \(0\le d\le k\), fixed \(c>0\), and arbitrary finite commutative local \(\mathbb F_q\)-algebras with residue field size \(q^f\) and cotangent dimension \(d\), with \(q\) over prime powers. The structural reduction is proved from coefficient-field Frobenius lifting, local cotangent generation, Chinese remainder separation of full-degree Frobenius orbits, and elementary counting. The exact probability has independently verified normalization, including zero probability beyond the orbit count and for insufficient tuple length. The separate binomial/occupancy asymptotics give Poisson means \(c\), \(c\), and \(fc^2/2\) at the simultaneous critical balance, and factorial moments establish independence of the collision count from the bounded bad-residue count. Exponent comparisons give all other cases of the phase diagram. The standalone direct-multiplication verifier passed 10 square-zero finite tests, 2 length-three truncation tests and 1 mixed-local-type test. The code is finite corroboration, not an asymptotic proof.

## Originality — PASS, relative to inspected evidence

The essential **algebraic** generator criterion is *already known* from Kravchenko–Mazur–Petrenko (2014, Theorem 2.2 and Corollary 2.6), and the exact finite generator-count product is obtained from that criterion by elementary field and matrix enumeration. Neither is claimed as an original contribution. The candidate instead proves and classifies the **joint independent Poisson scaling laws**, including the unique simultaneous three-obstruction balance \(2\mid f\), \(2\mid k\), \(d=k/2+1\), and a complete zero-versus-positive phase boundary in \(d\). The inspected 2014 result does not state a probabilistic limit, independent obstruction laws, or the critical-balance classification. Sercombe–Shalev (2020) studies random generation for broad associative algebra families but does not provide this law; Arpin et al. (2021) studies generator schemes rather than the corresponding occupancy limit. The closest retrieved research-record hit concerns collision phenomena in ordered Boolean products, without local-algebra cotangent obstructions. No equivalence with a located theorem was established.

Residual priority risk: this could be derived from an unlocated asymptotic random-generation theorem for Artinian algebra products or a generator-scheme occupancy principle. Ordinary birthday-Poisson limits are classical; novelty rests on the three-way coupling and sharp parameter balance, not the Poisson approximation alone. Independent literature assessment remains necessary.

## Mathematical value — PASS

Randomly generating a large direct product is a natural algebraic question. The limit distinguishes three intrinsic sources of failure—proper residue subfields, failure to span the cotangent space, and collisions in Frobenius-orbit labels—at one sharp square-root scale. The complete phase diagram identifies exactly when all three mechanisms contribute at nonzero intensity; it is invariant under arbitrary changes to higher radical multiplication and Loewy length. This provides a genuine asymptotic structural classification, rather than a small finite count, an arbitrary parameter slice, or a restatement of the earlier algebraic generation criterion.

## Limitations and closest literature

The result is limited to finite commutative equicharacteristic local factors, fixed \(f,k,d\), and uniform independent sampling; the proof gives a limit but no explicit sharp error rate. Kravchenko–Mazur–Petrenko (2014) is the closest theorem in terms of implications and is acknowledged as subsuming the base generation criterion. Kravchenko–Mazur–Petrenko (2010) and Sercombe–Shalev (2020) give prior general random-generation methods and bounds. Arpin et al. (2021) gives a geometric generator-scheme framework. Publication priority is provisional and only self-review has been performed.

Self-review: passed. Independent audit: not yet performed.
