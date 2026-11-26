# Independent mathematical audit

## correctness

PASS

For m=2^ap^b, factor σ(m²)=(2^{2a+1}−1)(1+p+⋯+p^{2b}). Both factors are odd and the latter is 1 mod p, so equality of the GCDs is exactly ν_p(2^{2a+1}−1)≤b. If d is even it does not divide L=2a+1; in the odd-order case the valuation is zero unless d|L, and then odd-prime LTE gives c+ν_p(L/d). This yields the exact failure criterion also at c=b+1 and c>b+1. Each odd modulus M_b cuts out one residue class, of density 1/M_b. In fact, the count in a∈[1,N] is floor((floor((2N+1)/M_b)+1)/2), since L ranges over odd values 3 through 2N+1 and M_b≥3. Columns 1≤b<c supply (c−1)N/d+O_p(1) for large N. For b≥c the modulus is dp^k, k=b+1−c; at most O_p(log(2N)) moduli are at most 2N+1, and the constraint b≤N eventually includes all of them. Rounding costs O(1) per column and extending the truncated geometric main-term sum costs O_p(1). Its sum is N/[d(p−1)], giving the stated square count and vanishing relative frequency among exponent pairs. An independent divisor sum and floor-count check (review_evidence/reproduce.py 2) checks bounded prime/exponent grids and the odd-order Wieferich case p=3511, d=1755, c=2: at a=877 the tested b=1 fails and b=2,3 belong. The infinite proof is not inferred from those tests. The passage saying the global conjecture is not resolved should be read as a limitation of this theorem, not as a claim about the later or independently indexed literature.

## originality

PASS

Pass for the mixed-support exponent classification and the exact linear exponent-box main term with logarithmic remainder, not for the ambient Dris condition or ambient-density results. Order and LTE are standard and do the local valuation work. The combined classification and the count were not supplied by the most relevant statements inspected. This is an evidence-limited priority assessment.

## value

PASS

Mixed support on 2 and one odd prime is a complete naturally defined family in a preexisting problem, not a selected numerical instance. Its exact exceptional lattice distinguishes the order-parity and Wieferich regimes and yields the contrast between positive column densities and a linear, hence sparse, square count. These explicit facts can be used for arithmetic membership tests and for comparisons with other support families. The argument is elementary, but the exact combined classification and two-dimensional count are not a restatement of LTE or of ambient zero density. No global advance is attributed to this local theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
