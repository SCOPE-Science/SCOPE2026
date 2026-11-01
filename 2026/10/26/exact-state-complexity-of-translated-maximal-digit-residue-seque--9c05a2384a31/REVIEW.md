# Independent mathematical audit

## correctness

PASS

Each finite LSD-first prefix u of length j yields an exact residual output function F_(t,a)(x)=1_{d_b(x+t)+a≡0}, t=⌊(c+u)/b^j⌋ and a=d_b((c+u) mod b^j) mod m. The carry transition (t,a)→(⌊(t+z)/b⌋,a+1_{(t+z) mod b=b−1}) is total, handles redundant high zero digits, and includes the empty word. Equality of two binary residual indicator functions under arbitrary appended high maximal-digit blocks forces the digit-count congruence itself; choosing x=b^K−max(s,t), with b≥3 and K variable, shows t≠s impossible because the high block contains K−L maximal digits. Thus all reachable (t,a) states are Myhill–Nerode distinct. Quotients t≥2 occur in unique depth layers because b≥3, while t=0 contributes all m residues and t=1 exactly R[0,c); this proves the interval formula, including j=0/empty intervals. Power shifts and one-below powers yield the drop formula. Independent residual-state enumerator checked 1,296 base/modulus/shift combinations and 64 adjacent-power comparisons; exact proof, not finite sampling, establishes all b,m,c.

## originality

PASS

Allouche et al. (2026) introduce the base-4 digit-three residue automatic sequence and analyze its abelian-factor complexity, not minimal DFAO size under arbitrary additive input shifts. Moradi–Rampersad–Shallit (2025/26) give general subsequence constructions and msd-first translated Thue–Morse complexity bounds; Charlier–Cisternino–Massuir compute automata for forward images mT+r rather than the inverse shifted-input set. Neither theorem implies the exact LSD-first all-shift digit-interval count or unbounded adjacent-power downward jumps. A binary digit-sum translation analogue is not interchangeable because quotient levels overlap for b=2.

## value

PASS

The theorem completely computes a natural state-complexity invariant for all additive shifts in an infinite automatic sequence family, including the recently studied base-four mod-three sequence. Its injective residual-pair classification provides structural minimality, and the unbounded unit-shift drop identifies a sharp unexpected instability in automaton size rather than a trivial renaming or constructed upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
