# Independent mathematical audit

## correctness

PASS

The cyclic binary-token folding is terminating and preserves residue modulo odd M=2^r-1; a positive reduced token sum <=M divisible by M must be M, requiring r ones. For H(t)=(2^(rt)-1)/M, odd-prime LTE establishes v_p(H(a)-H(b))=v_p(a-b) at every p|M; hence H permutes residues mod M^(k-1), providing a witness N=M(1+2H(t)) with exactly r distinct bits. Legendre gives v_2(binomial(2n,n))=s_2(n). For any odd p construct an index multiple of M^k with all base-p digits in {0,1}, so p has no central-binomial carry and cannot divide the infinite gcd. The argument covers k=1, r=2, arbitrary composite M; the binomial gcd is infinite-index, not numerical extrapolation. Independent bounded modular and odd-prime checks passed 45 r,k witnesses and 90 carry cases.

## originality

PASS

O(EIS A086342) and historical work already identify minimum r for modulus M=2^r-1 at k=1; that case is not original. Elsholtz gives sparse prime multiple methods, while Clokie et al study general sturdy/flimsy multiples; the inspected theorem statements do not give equality for M^k at every k. Kummer/Legendre is prior; gcd is a corollary. A general order-lifting argument elsewhere could cover the all-k result and remains an explicit risk.

## value

PASS

The minimum binary weight of a multiple is a natural arithmetic automaton invariant; uniform stability under arbitrarily large powers of every Mersenne modulus is not mechanically implied by the known base k=1 value and needs lifting. The connected exact infinite-index fixed divisor is a motivated arithmetic consequence; not a claim about the least-sized multiple.

The dated certificate retains the supplied scientific assessment, sources and limitations.
