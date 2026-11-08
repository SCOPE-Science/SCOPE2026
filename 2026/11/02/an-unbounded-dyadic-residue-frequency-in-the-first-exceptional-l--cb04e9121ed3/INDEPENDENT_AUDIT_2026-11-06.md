# Independent mathematical audit

## correctness

PASS

For A=[[1,9],[1,0]], A³=[[19,90],[10,9]] and A⁶=[[1261,2520],[280,981]]=I+4B with B≡I mod2. Hence order A mod2^k is 3·2^{k−1} for k≥2 and period of U_n equals A order because (1,0), A(1,0) are a basis. The convergent log L=log(A⁶)∈4M₂(Z₂) interpolates f(t)=U_{6t+3}. For v3=(19,10), J=L/4≡I mod2, the lower coordinate of J² exp(tL)v3 is 2 mod4, so ν₂(f″(t))=5. The exact cancellation (Xv3)_2=15120 and (X²v3)_2/2=14288400 gives f′(0)≡0 mod64. Taylor coefficients imply g=f′/32=c+ut+2H(t), c even,u odd,H 1-Lipschitz, hence g is a bijective 2-adic isometry with unique zero τ. Leading quadratic coefficient f″(τ)/2 has ν₂=4 and all higher coefficients have strictly larger valuations at every h≠0, yielding ν₂(f(t)−f(τ))=4+2ν₂(t−τ). Only indices n≡3 mod6 can give a value ≡2 mod4; counting congruence t≡τ mod2^{ceil((k−4)/2)} within the exact period gives v_{2^k}(r_k)=2^{floor(k/2)}, k≥5. This is an infinite proof, not extrapolation from residue tables.

## originality

PASS

The 1996 Carlip–Jacobson Fibonacci Quarterly primary full text explicitly restricts its all-residue stability theorem to odd a and b≡1 mod16, and marks b≡9 mod16 as unresolved (table and text p299). The (1,9) theorem supplies a new exact 2-adic critical-point frequency growth in this excluded family; the published 1996 Acta work studies distinct stable parameter cases. The 1996 Finite Fields and Their Applications paper A Criterion for Stability of Two-Term Recurrence Sequences Modulo 2^k is a highly plausible stronger source whose full text was not obtained; it might already classify nonstability of b=9, and priority must be qualified accordingly. Even a weaker nonstability criterion would not automatically provide the sharp distinguished-fiber multiplicities.

## value

PASS

A historically identified missing congruence class b≡9 mod16 is resolved for its first natural coefficient pair. The unbounded exact frequency 2^{floor(k/2)} supplies a concrete quantitative obstruction to eventual stable residue sets; the rigid 2-adic quadratic critical contact explains growth at every precision. Neither a recomputation of stable b=1 tables nor an unmotivated arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
