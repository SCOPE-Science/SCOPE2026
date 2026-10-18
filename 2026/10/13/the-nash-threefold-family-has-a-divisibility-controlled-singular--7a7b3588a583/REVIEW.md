# Independent mathematical audit

## correctness

PASS

For every n>=2 with algebraically closed char p>0 dividing n, the prime-characteristic Jacobian-minor monomials omit exactly the minor n, yielding three Newton vertices. On one normalized chart the character cone has primitive rays (1,0,0),(0,1,0),(-1,-2,n),(-2,-1,n); its dual primitive rays r0=(0,0,1), rx=(n/g2,0,2/g2), rm=(n/g3,n/g3,3/g3), ry=(0,n/g2,2/g2). Their consecutive cross-product gcds are n/g2,n/(g2*g3),n/(g2*g3),n/g2. Four rays give singular fixed point; the nonregular two-faces give 0,2,4 per-chart curve components as claimed. Solving <m,r>=1 gives m=((g2-2)/n,(g2-2)/n,1) and consistency g3=2*g2-1, hence n multiple of 6 has Cartier index 1, odd n coprime to 3 has exact index n, others are not Q-Cartier. I independently recomputed gcd cases n=2,3,4,5,6,7,8,9,10,12,15,30 (independent_checks.py), and checked the pinned verifier code, which exhaustively tests n=2..512; finite tests do not prove the uniform theorem. Boundary cases n=2,3,6 checked separately. Scope per affine chart, not global irreducible-curve count.

## originality

PASS

Best-of-knowledge new all-exponent per-chart singular-face and canonical-index trichotomy. Duarte–Jeffries–Núñez-Betancourt provide the positive-characteristic Nash algorithm and n=2 example; standard toric face/Gorenstein criteria alone do not state the divisibility-index enumeration without an additional explicit family computation.

## value

PASS

A geometrically natural higher-dimensional Nash family displays exact transitions among isolated/nonisolated singularities and Gorenstein/Q-Gorenstein failures. The n-divisibility boundaries and precise canonical index supply useful data for singularity and birational classification beyond a routine single-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
