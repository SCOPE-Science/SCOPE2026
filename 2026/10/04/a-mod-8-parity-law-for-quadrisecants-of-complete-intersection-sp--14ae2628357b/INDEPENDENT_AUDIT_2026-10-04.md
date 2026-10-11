# Independent mathematical audit

## correctness

PASS

Substituting d=ab and g=1+ab(a+b-4)/2 into Cayley's quadrisecant formula gives the displayed integer polynomial Q_{a,b}. A fresh exact-integer check confirmed the specialization against Cayley's formula for all 4<=a,b<=80. Symbolically, the numerator N=24Q satisfies N(a+8,b)-N(a,b)=16 b R(a,b), and bR is divisible by 3 because modulo 3 it reduces to b^2((a^3+a)b^2+a+2b^2+1), which vanishes in all residue cases; hence Q parity is 8-periodic in each degree. Exhausting the 64 residue pairs gives exactly the two stated parity rules and 24 odd classes. Complex conjugation pairs nonreal points of a real reduced zero-dimensional quadrisecant scheme, so odd complex degree forces a real line.

## originality

PASS

The classical literature supplies the Cayley degree formula and proves existence/maximal-order facts for general ACM curves, while Le Barz develops general multisecant enumeration. Targeted searches for parity, mod-8 complete-intersection specialization, and real quadrisecant consequences found no prior theorem giving the 24 residue classes or the exact oddness criterion. The arithmetic law is not stated or implied in the inspected primary formulas without the new two-adic reduction.

## value

PASS

The result extracts an exact two-adic phase law from a classical enumerative invariant and converts it into a real-existence criterion for a natural family of complete-intersection curves. The 24-class mod-8 profile is a motivated exact classification with geometric consequence, not a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
