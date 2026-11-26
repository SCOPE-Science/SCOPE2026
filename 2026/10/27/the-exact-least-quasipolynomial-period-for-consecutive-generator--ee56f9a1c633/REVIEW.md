# Independent mathematical audit

## correctness

PASS

Writing x=ua+v with 0≤v<a gives membership iff u≥v: if a representation uses coefficient v+ta of a+1, the quotient only increases from v. Thus the gaps are exactly F_a-ia-j with 0≤j≤i≤a−2. On a residue r mod p, i=p−1 and the least residue j of r²−1 always qualify, since a>p. Costs with i≥p exceed its cost, and costs at smaller i are strictly ordered by i; the minimal (i,j) is independent of a within the class. For residue zero, j≡−1 forces i=j=p−1 at the minimum. For d|p proper, k=p/d, the proposed (d+k−2,d−1) lies in the triangle since p−1−i=(d−1)(k−1). Its cost is congruent to d²−d−1, with improvement over the zero-branch numerator equal to (d−1)(k−1)a+p−d>0, including d=1. A period d would force equality of the two polynomials on intersecting residue classes by the infinite-root property. The generalized CRT gives gcd(p,q) as a period if q is a period, by identifying the p-branch polynomials through a common q-branch on infinite progressions. Thus p divides any period, not just those among the divisors of p. The package's 3,234 enumerated instances and divisor-witness tests are finite diagnostics; verification rests on the uniform proof. The script was inspected, not executed.

## originality

PASS

Limited to the all-moduli least-period assertion and the explicit divisor separation, especially for composite p. The constituent formulas and the prime conclusion are already covered. The close higher-gap catalogue result expressly excludes gap 1 from its theorem and treats the gap-1 exact period as an independently existing result; its argument also works at gap 1, but the inspection does not identify an independent earlier source for that assertion.

## value

PASS

The natural minimal period of an exact Frobenius quotient function is stronger information than a convenient congruence period. It determines the smallest valid residue modulus even when some branch polynomials coincide. For composite p this is not automatic from having multiple branches or from the known recipe for each constituent: the explicit witnesses uniformly couple divisibility of p with an actual gap and rule out every candidate collapse. This is a useful exact invariant, not a claim of novelty for recomputing the branch table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
