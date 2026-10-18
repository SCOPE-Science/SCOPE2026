# Independent mathematical audit

## correctness

PASS

Directly differentiated prod_{j=0}^8(x−j) and shifted z=x−4 to obtain g(z)=9z8−210z6+1365z4−2460z2+576=h(z²), h(T)=9T4−210T3+1365T2−2460T+576. Independently SymPy-factorized h mod17 (irreducible quartic) and mod11 (linear*irreducible cubic); together 4-cycle plus 3-cycle and transitivity force Gal(h)=S4. Product y_i=64 makes sqrt-root sign kernel even. Checked g mod7 squarefree type (1,1,2,4) with irreducible quadratic and quartic: square of Frobenius contributes a weight-two kernel sign vector; all S4 conjugates generate 2^3. Hence Gal(g)=W(D4) order192. Independently enumerated 24 permutations times 8 even sign masks and counted 75 with fixed signed root, yielding 25/64 via Frobenius–Chebotarev (ramified primes finite). Contribution to c is (25/64)/(8·9)=25/4608. Not an infinite conclusion drawn from modular sample frequencies.

## originality

PASS

The 2024/2025 primary paper explicitly leaves d=8,24,48 as exceptional even Galois cases in its finite survey and bounded remainder; the complete 2026 follow-up HTML defines c and establishes exact liminf without computing this local exceptional density. The present complete order-192 Galois identification resolves d8, with best-of-knowledge priority risk from unindexed computations.

## value

PASS

Explicitly resolves the first exceptional case of a published Galois-density computation which feeds a natural harmonic-denominator constant. Exact group W(D4) and density 25/64 are motivated arithmetic invariants, independently useful even without solving the remaining infinite series.

The dated certificate retains the supplied scientific assessment, sources and limitations.
