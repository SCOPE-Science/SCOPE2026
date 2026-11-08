# Independent mathematical audit

## correctness

PASS

Read RESULT.md blob cbb49a92c755325bbf57d07adbb2a583fb7a0e35 and complete artifacts/verify_attractors.py blob 680a9c804a5bce0cccfd3bc181c94a89c216c037. Each distinct factor gives the exact union-of-occurrence-spans mask; every attractor is a hitting set for these masks, no implication gap. Inclusion-minimal masks preserve all hitting sets: 48 among 7008 distinct factors at n=128, 64 among 28128 at n=256. Supplied witnesses hit all original masks. A separately implemented exact recursive branch search with memoized no-solution states proved no hitting set of size ≤9 and ≤10, respectively, returning 243 and 3710 nodes (the source uses a different deterministic branch order with 243 and 3703). No timeout or sampled factors. This is a complete finite proof at these two sizes, not an extrapolation to all n.

## originality

PASS

Best-of-knowledge priority based on comparison of actual statements and implication directions: Same object and same invariant compared directly. No synonym/variant makes the old 12/13 upper bounds exact; candidate gives complete matching upper and lower values 10/11. A general decision/search algorithm is not itself a published exact result for an uncomputed case; prior certified inequalities leave multiple possible integer values. Residual overlap risk retained; search absence alone is not evidence of novelty.

## value

PASS

Computes two previously unknown exact natural attractor invariants for the next Rudin–Shapiro dyadic prefixes after the established ≤64 exact census. The result improves prior certified upper bounds 12 and 13 and lower bound 8 at both n=128 and n=256 to exact optima 10 and 11, information a future finite-automatic-word study or solver benchmark can directly use; no paper-sized general theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
