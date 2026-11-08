# Independent mathematical audit

## correctness

PASS

The pinned RESULT.md proof was reconstructed for every nonzero even integer p (including negative p), even m>2 and entry-point e>0. The doubling identity V_(2j)=V_j²−2(−1)^j gives ν₂(V_even)=1, and C_j=V_(2j+1)/p with C0=1,C1=p²+3,C_(j+1)=(p²+2)C_j−C_(j−1) proves ν₂(V_odd)=ν₂(|p|). If m=2^t r and t≥2, an entry V_e≡0 enforces e odd and 2^t|p. For odd r, gcd(V_f,V_(f+1))=2 makes V_(f+1) invertible, so the shifted sequence V_(f+n)=V_(f+1)U_n has precisely the U period d. For r>1, Cassini at d yields (−1)^d≡1 mod r, forcing d even. For t=1, π_U(2)=2 but π_V(2)=1, absorbed by even d since m>2; for t≥2, both periods mod 2^t are 2 by p≡0, and CRT/lcm yields equality. The r=1, m a 2-power case and p<0 are covered. Independent finite modular recurrence checks and V 2-adic checks corroborate but do not prove the infinite statement. The packaged verify.py was inspected and not treated as a proof; the external Lean/expert statuses remain not_performed.

## originality

PASS

Best-of-knowledge original, exact resolution of the even-p/even-modulus q=-1 parity case left as Question 5.3 by Fiebig–Mbirika–Spilker. Directly inspected full arXiv HTML proves neighboring cases but not this one; its strongest unit and discriminant criteria fail at the even 2-primary factor. A full Renault primary PDF covers first-sequence periods/ranks rather than this companion equality. Semantic published-finding searches returned the indexed copy of the assigned claim itself (excluded as independent priority), and nearby unrelated Lucas results. Historical priority is qualified by older-notation and unindexed-literature risks, not asserted as absolute.

## value

PASS

The theorem answers the specific natural parity gap Question 5.3 from a recent Lucas period/entry-point paper. Its exact all-index 2-adic valuation lemma explains the obstruction to the earlier unit argument, provides a reusable necessary divisibility criterion for V entry points, and fully settles the equality conditional for all even p,m>2. This is a mathematically motivated open classification, not a textbook substitution, tiny computational case or prior table reproduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
