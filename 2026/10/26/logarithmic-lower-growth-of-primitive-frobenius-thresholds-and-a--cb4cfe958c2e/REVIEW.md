# Independent mathematical audit

## correctness

PASS

The frozen formula for a=2 is true, but its asserted resolution was already known. The replacement finding consists only of the finite obstruction for a>=3 and its fixed-a liminf. Re-audit of the replacement: gcd(a,Q_a(R))=1 gives a CRT class modulo m=aQ_a(R). Its first representative above Rb lies at most m beyond Rb and strictly below (R+1)b by m<b. Reduction of any nonnegative representation modulo a forces y congruent to -1 modulo a, so y>=a-1>=2 and is coprime to a; y<=R by the upper interval endpoint. If no such y exists, there is no representation. Otherwise any prime factor of y divides Q_a(R) and n but not a, and hence also divides x. The argument works if x=0 or if Q_a(R)=1. With fixed a, the omitted prime logarithms have bounded sum, so log Q_a(R)=R+o(R); taking floor((1-epsilon)log b) makes m<b for every sufficiently large coprime b, proving the liminf with constant one. The repair's two replay examples were checked, including the empty product. A separate seven-example nonnegative-solution enumeration corroborated the frozen finite obstruction; the uploaded verify.py was inspected rather than executed. Finite examples are not the proof.

## originality

PASS

This passes only for the repaired finding. The original novelty assertion for the exact a=2 formula fails: two inspected primary sources predate the frozen record and state that very formula on the entire claimed range. The replacement credits them and removes that component from the finding. The surviving contribution is the explicit uniformly applicable finite witness in (Rb,(R+1)b) and its sharpening from a published subsequence lower bound to the all-coprime-b lower bound with leading liminf constant one. An earlier joint-growth primorial result does not cover fixed a; a later distinct indexed record has exactly the same asymptotic and a closely related but differently formulated finite construction. That overlap is disclosed and no independent priority for the shared asymptotic is claimed.

## value

PASS

The exact finite obstruction can be replayed for any admissible b above a simple explicit threshold, and resolves a demonstrable gap left by the earlier subsequence bound. It establishes divergence of g(a,b)/b uniformly over large b at each fixed a>=3, in contrast to the known bounded a=2 behavior. This is a meaningful change in quantifier and order, not a new claim based on recomputing the prior exact boundary. Value is re-evaluated on the finite obstruction and all-b asymptotic only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
