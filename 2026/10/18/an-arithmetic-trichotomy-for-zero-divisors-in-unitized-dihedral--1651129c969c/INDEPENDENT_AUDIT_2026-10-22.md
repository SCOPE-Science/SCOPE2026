# Independent mathematical audit

## correctness

PASS

For S=F_q1⊕F_q[R3], the exact polynomial determinant of left multiplication is a(a+s)(a²-Q), s=x+y+z and Q=x²+y²+z²-xy-xz-yz. Independent symbolic determinant factorization was verified over Z[a,x,y,z], and independent direct finite-field brute-force found singular nonzero counts 14,62,320,852,3740 for q=2,3,5,7,11. Fourier coordinate splitting over F_q for q≡1 mod3 yields norm-level q-1; conjugate-pair norm-one group for q≡2 yields q+1; in characteristic 3 Q=s². Thus Z(q)=q³-1+(q-1)B(q), B=2q²-2q+1 / 2q²-1 / 2q² in the three regimes. General prime-power formula follows finite-field group counting, not prime-only tests.

## originality

PASS

Best-of-knowledge statement-level comparison: Neither idempotent counts nor F2 graph produce the uniform singular left-multiplication count mechanically without the new arithmetic split.

## value

PASS

Provides a natural full finite-field family invariant extending an explicitly studied F2 example; the split/inert/characteristic-three arithmetic regimes illuminate the algebraic source of nontrivial vertex-count behavior, beyond recomputation of a known small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
