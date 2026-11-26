# Independent mathematical audit

## correctness

PASS

For any N-cycle the sign row of the second-smallest point is negative at just one residue t_0 (the unique time sending it to the minimum). A signature-preserving unit must fix t_0 modulo N. With N=p^k, writing t_0=p^v h, p not dividing h, forces u=1 mod p^(k-v), so there are at most p^v<=p^(k-1) possibilities, including for k=1. For sharpness, enumerate orbit time j modulo p^k, assigning its rank by reversing all k base-p digits, including leading zeros. For a nonzero increment t of valuation a, positions below a agree under addition modulo p^k, so there is no lower-place carry into a, and the digit at a changes by t/p^a modulo p. After reversal that position controls the sign. Multiplying t by u=1 mod p leaves both the valuation and this first nonzero increment digit unchanged, hence it preserves the sign for every starting time. Multiples of N are fixed returns, and reducing all other times modulo N loses no case. There are p^(k-1) such units, so the bound also excludes every other unit for the constructed cycle. Transfer the construction to any ordered S by matching ranks. Independent exact enumeration using the time-increment sign columns gave maxima 2, 4, 3 at N=4,8,9; analytically the congruence and digit argument cover all prime powers.

## originality

PASS

Prime-cycle rigidity and composite-cycle collision existence are known, as is an exact broad family of composite signature fibers. Neither supplies the prime-power maximum in the fixed-cycle unit action. In particular, the strongest same-day exact fiber result has an explicitly different intersection with powers: for its block shifts with block count m and block width r, the preserving unit powers satisfy u=1 mod m (by the block step) and u=1 mod r (by the fixed within-block return rotation). The two congruences suffice for all signs in that family and give gcd(m,r) powers. For m=p^i, r=p^(k-i) this is p^min(i,k-i); it supplies the attaining example at k=2 but is strictly below the frozen p^(k-1) at every k>=3. The frozen digit construction uses multiple digit levels, not just a single pair of rotations. The universal upper bound in the fixed-cycle action and its attainment for all k are the distinct claim. No within-day priority is asserted.

## value

PASS

Recovering a cyclic time step from complete order comparisons leads naturally to ambiguity under changing the generator of the same orbit. The exact extremum resolves that ambiguity at every prime-power length, with a construction and no unquantified multiplicative loss. In particular every generator at lengths 2^k can be indistinguishable, whereas prime lengths are rigid. This is distinct from the known count of arbitrary alternative cycles, which does not tell how many time changes are invisible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
