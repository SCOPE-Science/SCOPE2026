# Independent mathematical audit

## correctness

PASS

PASS. Binary-carry update (c,d) -> (floor((3b+c)/2),floor((5b+d)/2)) with sign (-1)^{b+(3b+c mod 2)+(5b+d mod 2)} and terminal sign t(c)t(d) is exact for every input binary digit. The seven reachable carry states form a closed automaton. Independent exact integer arithmetic regenerated its signed M and verified M(M^2-I)^3=0, giving C_{r+7}-3C_{r+5}+3C_{r+3}-C_{r+1}=0. The first seven values (1,0,0,-2,-2,-4,-4) plus the same recurrence for -2floor((r-1)/2) establish C0=1 and the formula for all r>=1; the displayed rational generating function and parity populations follow. The 65,535 direct summands for r<=15 are corroboration, not proof for unbounded r.

## originality

PASS

PASS (best-of-knowledge, with specified residual risks). Equivalent versions count the parity of s2(n)+s2(3n)+s2(5n), calculate a 7-state weighted automaton rational generating series, or evaluate a simultaneous multiplicative correlation. This is not a fixed-shift stationary third-order Thue–Morse correlation. Automatic sequence transducers, regular-sequence linear representations, and dilation correlation theory can in principle subsume the construction; no inspected theorem directly evaluates this 1,3,5 triple and all-r logarithmic law. The general method is not claimed new. Odd-order additive correlations vanishing in a stationary mean do not imply this exact nonstationary multiplicative finite-scale signed bias. Individual sequence t(kn) results do not determine triple joint products without carries.

## value

PASS

PASS. The first natural three odd dilations 1,3,5 of the canonical automatic sign sequence have an unexpected exact logarithmic signed bias (not merely zero limiting correlation). This is an explicit reproducible count of joint binary-digit parities for every dyadic length, useful for studying simultaneous arithmetic correlations and automata of multiplication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
