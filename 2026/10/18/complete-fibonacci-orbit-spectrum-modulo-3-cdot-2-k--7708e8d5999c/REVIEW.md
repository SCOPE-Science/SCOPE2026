# Independent mathematical audit

## correctness

PASS

A=[[0,1],[1,1]] has determinant -1. The exact matrices (A^3-I)/2, (A^6-I)/4 and (A^12-I)/8 have odd determinants. Primitive 2-adic states therefore have respective least periods 3,6,3·2^(j-1) for j>=3; the squaring/odd-multiplier induction proves no earlier return at every 2-adic layer. Each primitive layer has 3·2^(2j-2) states, and modulo 3 the only cycles have length 1 (zero) and 8 (all nonzero). CRT pairs an r-cycle and s-cycle into gcd(r,s) orbits of lcm(r,s). Assembling gives k=3 multiplicities (1,1,2,1,4,21), k>=4 (1,1,2,1,4,93) plus 9·2^(j-1) at length 3·2^(j-1) for j=5..k; total 9·2^k−42. Independent direct enumeration of all (3·2^k)^2 state pairs for k=3,4,5,6 gave 30,102,246,534 orbits with every length/count matched. The induction, not finite testing, establishes all k>=3.

## originality

PASS

The numerical identity itself was an explicit **conjecture** in OEIS A015134, not presented as a novel guess; a rigorous all-k proof and length-resolved orbit multiplicities are the claimed improvements. Classical recurrence periods and the CRT lcm rule for a single starting pair are weaker because they do not count all state orbits or their least period distribution. The full 2014 Avila–Khovanova article discusses free Fibonacci numbers, distinct modulo-8 finite cycles and OEIS counts, not the given all-k 3·2^k theorem.

## value

PASS

Resolves the explicitly recorded 2023 OEIS A015134 conjecture for 3·2^k, all k>=3, and provides strictly finer full least-period multiplicity spectrum. Explicit 2-adic matrix valuation stratification plus CRT provides transferable orbit enumeration information for modular linear recurrences. Known numerical terms are not falsely claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
