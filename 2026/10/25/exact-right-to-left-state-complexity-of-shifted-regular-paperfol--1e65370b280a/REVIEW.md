# Independent mathematical audit

## correctness

PASS

For LSD-first binary prefix x at level k, the exact residual z↦p(2^k z+c+x) is classified by r=(c+x+1) mod2^k: r=0 yields shift p(z+floor(c/2^k)), r=2^(k-1) yields parity z+floor((c+2^(k-1))/2^k) mod2, and all other residues yield constants. k=0 is treated separately and k=1 has no constant case; constants do occur from k=2. The attainable shifts are c,floor(c/2),...,0 (one when c=0, m+2 when c≥1 with m=floor(log2c)); both parities occur iff c≥1, both constants always. The proof by shifting 2^k−1 and 3·2^k−1 establishes non-eventual periodicity of p, ruling out residual collisions. Thus exactly 4 states at c=0 and 6+floor(log2c) for c≥1, with both reachability and distinguishability. Independent direct residual signature enumeration covered 39 shifts and 19096 prefix signatures; finite tests are corroboration of all-shift proof.

## originality

PASS

Best-of-knowledge qualified PASS: Zantema–Bosma already give reversed complexity 4 for unshifted regular paperfolding and 6 for its 1-step tail and general shift upper bounds. The complete dyadic staircase for arbitrary c≥1 and exact residual family are not obtained directly from those two special-case evaluations or the Fibonacci-word shift theorem.

## value

PASS

All-shift minimal-state complexity is a natural automata invariant of a canonical automatic sequence. A sharp logarithmic dyadic staircase separates true minimality from generic existence of an automatic transducer, filling the gap between c=0,1 benchmarks and general shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
