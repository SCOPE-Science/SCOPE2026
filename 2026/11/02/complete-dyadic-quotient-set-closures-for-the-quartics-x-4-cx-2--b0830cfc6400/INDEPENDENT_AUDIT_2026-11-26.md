# Independent mathematical audit

## correctness

PASS

Positive integers are dense in Z_2 and division is continuous off zero denominators, so it suffices to take dyadic inputs. Every 1 mod 8 unit is a square: if an odd x is correct modulo 2^N, adding 0 or 2^(N−1) sets the next square bit for N≥3. The resulting approximate roots are Cauchy (they need not preserve the last bit of the preceding root). For x=2^k u with u a unit, divide f(x) by 2^(2k) and use t=u². Differences of t(c+2^(2k)t) on 1+8Z_2 are t−s times an odd factor, including k=0; this makes the induced maps injective on residues and therefore bijective onto the matching output ball modulo every 2^N. Compactness gives exact equality. Odd inputs give c+1+8Z_2; even inputs' normalized values are c+4 mod 8 for valuation k=1 and c mod 8 for k≥2. For c≡7 the odd ball is 8Z_2, giving every quotient; for c≡3 it is 4Z_2^×, so output valuations are even and varying an odd denominator fills every nonnegative even quotient valuation and all its units. For c≡1,5 odd inputs give the full valuation-one unit coset, which realizes the allowed odd quotient shells and all of 1+4Z_2 at valuation zero. At each positive even valuation 2r, input valuation pairs (r+1,1) and (r+2,2) give the normalized cosets 5 mod 8 and 1 mod 8 respectively. Inversion gives the negatives. The residue and parity restrictions are closed relative to Q_2^×, and f(2^k) with a fixed nonzero denominator tends to zero. Thus these are the exact closures, with the three proper parts distinct index-two subgroups.

## originality

PASS

The density conclusion for c≡7 mod 8 is known by the simple-root criterion. The supported distinct content is the three exact proper closures, which specify all unit cosets at all valuations. The closest indexed exact closure is for a genuinely different binary homogeneous form with a different density criterion even in degree four.

## value

PASS

The family tests the exact outcome of a polynomial-image quotient problem at the exceptional prime two, where the simple-root condition does not classify non-split cases. The result goes past showing failure of density: it identifies three distinct index-two kernels, and for two of them valuation support alone cannot distinguish the closures. The full shells give precise benchmarks for future local quotient-set analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
