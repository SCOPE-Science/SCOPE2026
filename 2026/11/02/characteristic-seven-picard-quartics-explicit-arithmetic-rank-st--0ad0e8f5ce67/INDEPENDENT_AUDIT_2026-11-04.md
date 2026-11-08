# Independent mathematical audit

## correctness

PASS

For the smooth depressed quartic F=x^4+a x^2+bx+c in characteristic 7, squarefreeness is Delta != 0 and the superelliptic genus equals 3. Reconstructing Cartier on dx/y, dx/y^2, x dx/y^2 gives H=diag(2a, [[U,V],[W,Z]]) with U=[x^6]F^4, V=[x^5]F^4, W=[x^13]F^4, Z=[x^12]F^4. Independent SymPy reduction mod 7 checked UZ-VW=5a Delta and det(H)=3a^2 Delta. For a=0 the block has rank 1 and factors as (3bc,1)^t(4b,4c), with stable-rank contraction 5c(b^4-3c^3)(b^4-4c^3). Smooth a!=0 means (f,a-number)=(3,0); smooth a=0 means a-number 2 and rank either 0 or 1 according to c(b^4-4c^3)=0. Independently counted all 343 F7 coefficients by gcd: 49 singular, 252 ordinary, 30 rank 1, 12 rank 0. Finite census only checks F7; semilinear algebra gives the geometric family classification.

## originality

PASS

Prior Picard-curve normal forms, p-rank existence/dimension results, and Hasse-Witt criteria are not attributed to this claim. The exact characteristic-7 depressed marked-coordinate rank-zero component equations, a-number rigidity and coefficient census are not established by the accessible compared primary statements. A 1991 primary Picard Hasse-Witt paper is strongly plausible overlap, but only an abstract was accessible, and authorized full text was blocked by VPN; do not infer novelty from that failure. Qualified best-of-knowledge PASS for the narrowly stated formula and complete census.

## value

PASS

A full arithmetic stratification and complete natural marked-coefficient count of smooth genus-three Picard curves in the smallest 1 mod 3 characteristic is independently useful beyond knowing which p-ranks can occur. Exact a-number restriction and rank-zero components can inform construction, moduli computations and finite-field examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
