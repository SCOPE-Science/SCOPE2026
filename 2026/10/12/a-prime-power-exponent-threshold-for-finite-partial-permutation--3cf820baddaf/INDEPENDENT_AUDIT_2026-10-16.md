# Independent mathematical audit

## correctness

PASS

Reconstructed the exact fixed-carrier equivalence between a permutation extension of a partial bijection with tau^(3^k)=id and a partition of whole directed paths into lengths 1,3,...,3^k, after checking forced cycles. In the strong-unary 3-PARTITION reduction Q is the least power of 3 at least B, P=3Q, C=Q-B and L_i=3a_i+C. Strict B/4<a_i<B/2 implies P/4<L_i<P/2, total mP. A P-cycle uses exactly 3 paths summing B; every exceptional P/3 singleton has a_i=B/3 and their count is divisible by 3, so grouped back into valid triples. All smaller allowed cycles are excluded. Polynomial NP witness and fixed-K type-count dynamic program are valid. Separately recalculated B=15 six-item positive witness (24,27,27,27,27,30) with one full and three exceptional length-27 cycles. Inspected full verify.py; bounded evidence supports but cannot prove NP-hardness.

## originality

PASS

The search of published findings and the inspected extension-property primary source found larger-carrier finite-group completion, not zero-enlargement prescribed-exponent decision complexity. The source paper supplies no fixed-carrier NP-hardness threshold. 3-PARTITION is an acknowledged classical packing primitive; its reduction to exact 3-power cycle lengths is the asserted new application. Older partial-permutation/packing formulations may encode the same result and remain a stated risk.

## value

PASS

A zero-added-vertex completion constraint is natural in permutation extension and is not interchangeable with arbitrarily large extensions. Its sharp transition from fixed exponent polynomial algorithms to binary-input NP-completeness provides a genuine structural/computational barrier, not a renamed generic packing table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
