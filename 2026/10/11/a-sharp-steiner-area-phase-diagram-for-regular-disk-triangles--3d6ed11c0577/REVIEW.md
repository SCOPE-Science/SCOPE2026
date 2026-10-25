# Independent mathematical audit

## correctness

PASS

Reconstructed actual geometry: beta in (0,pi/6], F=1−cos(beta)+sqrt3 sin(beta), r=w/F(beta), G=sqrt3 sin²(beta)+3(beta−sin(beta)cos(beta)); area/w²=G/F², perimeter/w=6beta/F, so Steiner parallel area/w²=a(beta)+tau p(beta)+pi tau². F_prime>0, p_prime<0, and U=−a_prime/p_prime. Rebuilt H=J H0_prime−J_prime H0 symbolically from these formulas, independently extracted the 20 Fourier-Laurent terms with beta degree≤2 and frequency≤4, reproduced all 15 nonzero degree-20 Taylor coefficients from order 6, exact per-degree coefficient norms 14sqrt3+6sqrt7+2sqrt291+4sqrt111<117, 114 and 48, negative high-order Taylor mass 0.053565<0.06, and global exponential remainder coefficient 0.000170004<1/5000. Combining Q20>0.4 beta^6 with remainder<beta^6/5000 gives H>0 for every 0<beta≤pi/6, not just a sampled grid; U_prime>0. Endpoint derivatives give U(0+)=1/3 and U(pi/6)=(3+2sqrt3−2pi)/(2pi−6), hence derivative sign proves three sharp phases and uniqueness/nonattainment. Independently reconstructed assigned Git tree from its eight blob SHA identities, exactly matching source_tree_sha.

## originality

PASS

Full theorem-level comparison distinguishes the known area/perimeter formulas and fixed-radius isominwidth results from the new strict global monotonicity U=-a_prime/p_prime and complete sharp three-phase minimizer classification for the variable-radius outer-parallel objective. Fresh mathematical corpus queries exactly matched the audited record itself but no independent covering result. Adjacent Pál stability and INNER parallel Cheeger theorems were read at the relevant primary mathematical passages and lack the target implication. Originality is best-of-knowledge only: older equivalent area-perimeter convexity results could be unindexed, and the known scalar ingredients carry no novelty credit.

## value

PASS

Optimizing outer parallel area over the canonical regular r-disk triangle family at fixed minimum width is a natural intrinsic geometry/Pál-to-Blaschke-Lebesgue tradeoff: Steiner polynomial couples two classical competing invariants, area and perimeter. The theorem establishes exact sharp transition ratios (1/3,tau+), unique interior curved optimum on a genuine open interval, strict comparison to both endpoint shapes, and boundary uniqueness/nonattainment through a substantive global analytic curvature certificate. This is not just restatement of known scalar area/perimeter formulas or simple endpoint substitution; the precise variable-radius optimizer would be useful for geometric offset and width extremal studies. No claim of global optimality outside this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
