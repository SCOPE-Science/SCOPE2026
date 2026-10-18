# Independent mathematical audit

## correctness

PASS

At pinned RESULT.md, the renewal recursion u_n=sum_{j=1}^4 p_j u_{n−j} with u0=1 makes every n>=4 a convex combination of its preceding four values, so the global positive-time minimum is min(u1,u2,u3). Independently expanded the three displayed nonnegative residual factorizations u_j−P and reduced under a+b+c+d=1: all polynomial differences vanish identically. At c=0, u3−(Q4+lambda abd)=ab[b+(2−lambda)d]; an exact rational witness a=49/100,b=1/100,d=1/2 makes lambda=21/10 already fail, while lambda=2 is safe. The cumulative-coordinate restriction proves membership in both classes. Verified actual verify.py coefficient structure, not just its output.

## originality

PASS

The 2024 primary article Conjecture 3.7 asserts exactly the opposite of this constructed admissible polynomial: Q_4 maximal in A_4 and largest in restricted hat A_4. Its Proposition 3.5 proves only Q_4 is a lower bound; Proposition 3.8 treats k=3. The present P=Q_4+2abd strictly dominates in the interior and belongs to both classes, an explicit new counterexample with sharp directional coefficient; no equivalent counterexample found.

## value

PASS

Constructive falsification of two clauses of a named published conjecture at the first previously unsettled support size, supplying an exact positive perturbation and a sharp one-parameter coefficient; the finite-degree minorant problem is naturally motivated by renewal probabilities rather than arbitrary coefficient improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
