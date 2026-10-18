# Independent mathematical audit

## correctness

PASS

The binary Baum–Sweet prefix starts b(0)=1 and b(n)=1 precisely when ordinary binary zero runs have even lengths. Adjacent ones occur iff n=4^t-1, with no triple ones, by following even last-zero-run parity under increment. The standard shortest complete-two-letter greedy arch decomposition exactly computes scattered-subsequence universality, as its constructive lower embedding and missing length-(a+1) word upper bound show. After initial word 110110 (four ones, two arches), a further one completes an arch unless it ends a pair of adjacent ones, when the second one requires the next zero. The only trailing pairs occur at prefix N=4^t+1; small N=0..6 checked. Thus for all N>=4, U=B-2-1_exception. The accepted positive binaries form 1(1|00)*, yielding count F_ell at bit-length ell and B(2^m)=F_{m+2}; monotonicity brackets all N to give Θ(N^log2φ), with exact dyadic limit φ²/sqrt5. Independently regenerated bits and greedy arches agreed for each N<=16384 and Fibonacci dyadic levels through 14; these are bounded checks supporting a full symbolic proof.

## originality

PASS

The general greedy-arch universality correspondence and the automatic Baum–Sweet sequence are classical. The inspected Schnoebelen–Veron work develops compressed input arch algorithms but does not provide a symbolic all-prefix closed form or sublinear exponent for this named sequence. The fixed regular-language universality problem of Adamson et al. is a distinct quantifier pattern. Resultary returned related general binary universality and Fibonacci SAS results, not a Baum–Sweet prefix formula. This specific all-N correction and dyadic count survive as mathematical specialization with new structural work.

## value

PASS

Exact sparse subsequence universality in a canonical 2-automatic binary sequence links digital regular-language counting, greedy arch factorization and Fibonacci growth. The exceptional 4^t+1 prefix correction and explicit O(log N) digit-DP make it a usable sharp combinatorial invariant for all prefixes, beyond merely applying a generic finite-input algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
