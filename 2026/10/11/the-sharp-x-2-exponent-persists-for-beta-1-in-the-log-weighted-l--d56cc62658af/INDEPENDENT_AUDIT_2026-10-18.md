# Independent mathematical audit

## correctness

PASS

Set a=(beta-1)(N-1)/N, t=log(e R/r), s=log t and u=t^{-a} phi((s-S)/L). Direct radial change of variables gives the exact defect integral omega*int(|a v-v_prime|^N-a^N|v|^N) ds and D_q=omega*int|v|^N (1+s)^(-q) ds. The first variation integrates to zero, convex Taylor remainder is O(L^-1), and a plateau contributes D_q>=c_q L^(1-q). Thus I/D_q=O(L^(q-2))->0 for all q<2. Independently checked the exponential consequence: after rescaling u by c L^(1/N) so I<=1, on s in [S+L,S+2L] the exponential argument is alpha c L^(1/(N-1)) e^s (1+s)^(-theta); for theta<1/(N-1) this dominates the radial volume-decay factor e^(-N e^s). Hence the exponential integral diverges. Exact parameter cancellation -N(a+1)+beta(N-1)=-1 checked for arbitrary real beta>1.

## originality

PASS

The materially inspected complete Ghosh arXiv manuscript Theorem 1.4 explicitly asserts optimality only beta<1 (introduction and Section 6.2), and its Propositions 5.2,5.3 give the needed subquadratic obstruction only for 0<beta<1 or beta<0. The reconstructed beta>1 cutoff closes that gap. Resultary searches found the same submitted target, but no independently stronger covering record. Best-of-knowledge PASS with indexing and alternate-embedding risks.

## value

PASS

The exact missing positive-weight range is part of a natural sharp log-weighted critical Sobolev embedding; determines a sharp nested-logarithm exponent, not merely a routine cutoff renaming. The explicit q<2 remainder obstruction and failure of any smaller exponential correction settle a meaningful analytic boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
