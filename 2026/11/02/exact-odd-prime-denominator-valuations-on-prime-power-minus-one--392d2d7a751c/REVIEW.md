# Independent mathematical audit

## correctness

PASS

For q=p^m and 1<=r<q, all C(q-1,k) are units modulo p. Exactly k=q-r has denominator k+r=q of valuation m, numerator k valuation s=v_p(r). Every other term has strictly greater valuation because v_p(k+r)<m and v_p(k)>=min(v_p(r),v_p(k+r)). Therefore the sum has valuation s-m and leading unit (-1)^(q-r)(q-r)/p^s mod p. A factorial identity proves the universal denominator divides C(n+r,r), while v_p(C(q-1+r,r))=m-s, giving saturation. Independently computed exact fractions and residues for 80 tested (p,m,r) parameter cases. The proof is uniform for odd primes; the exclusion of p=2 is a novelty-scope choice, not needed by the minimum-term calculation.

## originality

PASS

Kellner 2023 already proves the general binomial denominator bound and several nonintegrality regimes, including full valuation at primes dividing the evaluation parameter ell. The current ell=2 case concerns odd primes p, and the exact q-1 row leading residue and saturation over all 1<=r<q are not claimed in inspected Theorems 2.1, 2.7, 3.3. Existing r=1 nonintegrality is credited. Older special sum evaluations could cover the simple minimum-term argument.

## value

PASS

The exact p-primary reduced denominator for all r in a complete infinite prime-power-minus-one row and the nonzero leading digit give a natural arithmetic sharpening of a universal denominator divisibility bound. The proof is short but the exact saturation and all-parameter nonintegrality are not merely a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
