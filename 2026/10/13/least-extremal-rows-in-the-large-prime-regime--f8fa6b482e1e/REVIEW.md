# Review

## Correctness
PASS. The proof fixes the exact target \(T=p+s\) with \(1\le s<m\), proves that every selected \(k\) satisfies \(s<k<p\), and therefore obtains exactly one Kummer borrow. Every earlier admissible row is below \(p\), hence has valuation zero. The global upper bound \(1\) is reconstructed by the leading-digit case split for an arbitrary multiplier. The exact-integer checker independently exercises 5,250 parameter pairs through \(m=80\) and \(p=401\).

## Originality
PASS. The closest source, arXiv:2610.01328v1, proves the maximum and gives \(N=mp\) as one attaining row when \(m<p\), but defines the least-row invariant separately and determines it only for \(m=p^a+1\) with \(a\ge2\). McTague's theorem covers only the congruence-one subfamily, and arXiv:2609.37754v1 covers the congruence-minus-one subfamily. None of the inspected statements implies the unrestricted all-residue formula for every prime \(p>m\).

## Value
PASS. The source paper explicitly promotes \(T_p(m)\) to a natural exact invariant. This result completely resolves the entire first sharpness layer \(r_p(m)=1\), replacing a generic attaining row of size \(mp\) by the exact minimum in the interval \(p<T_p(m)<p+m\). The complete classification is structural rather than a finite table or an arbitrary parameter slice.

## Closest literature and limitations
The strongest overlaps are the congruence-one valuation theorem of McTague and the congruence-minus-one theorem of Fairfax-Ball. They cover proper residue-class subfamilies, not arbitrary \(p>m\). The 2026 non-coprime-index paper cited by the lead source uses a different selection rule and was not fully inspectable in the literature trail, leaving a low residual equivalence risk. No claim of historical uniqueness is made.

Self-review: passed. Independent audit: not yet performed.
