# Independent mathematical audit

## correctness

PASS

For an odd squarefree n=p1...pk, symmetric included divisors correspond to complementary pairs (d,n/d), weighted d+n/d, so existence is an exact finite subset-sum condition. Sigma(n)>=2n is necessary. For k<=4 the maximal odd-prime Euler factor product at 3,5,7,11 is 768/385<2. For k=5 abundance forces the three smallest primes 3,5,7, then fourth r in {11,13,17,19}, fifth s in bounded ranges; independently enumerated precisely 71+12+3+1=87 candidates and (by McCormack–Zelinsky necessary congruence) 37+6+1+1=45 n≡1(mod4) survivors. Recomputed all 16 complementary pair weights for each of 45 and independently exhaustive meet-in-the-middle split 8+8 (at most 256 sums per half); no omitted-pair subset sums to sigma(n)-2n. Thus k<=5 impossible. For n=937365=3*5*11*13*19*23, the five omitted pairs (55,17043),(57,16445),(65,14421),(143,6555),(165,5681) multiply to n pairwise, have ten distinct divisors, and total sigma(n)-2n=60630; including all other pairs sums exactly 2n. This proves lower bound and sharpness, not just a search timeout or failed heuristic; no claim about even or nonsquarefree numbers.

## originality

PASS

The concrete witness 937365 is explicitly mentioned by Wang–Zelinsky (2026 v3, §2), so neither that number nor its bare strong pseudoperfectness is original. McCormack–Zelinsky proves congruence obstructions and defines the object; the new statement is exact optimality of six distinct prime factors specifically among odd squarefree strongly pseudoperfect numbers. Read the 22-page primary update including its §5 computation tables; it does not state or prove that five support primes are impossible. Resultary has a related published low-support Ω(n)<=3 result, which covers a much smaller restriction and cannot imply exclusion of all five-prime odd squarefree candidates. The exhaustive finite upper-bounded certificate is the real additional result.

## value

PASS

Determining the first admissible support size for the natural odd squarefree subfamily is a meaningful extremal parameter, with a complete finite reduction and exact minimal witness. It strengthens a known existence example with a sharp impossibility theorem rather than simply recomputing a table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
