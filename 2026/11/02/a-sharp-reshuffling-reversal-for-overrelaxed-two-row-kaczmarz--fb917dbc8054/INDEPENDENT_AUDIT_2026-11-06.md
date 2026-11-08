# Independent mathematical audit

## correctness

PASS

For two independent real unit row normals u,v with positive oriented inner product ρ∈(0,1), relaxed row maps B=I−αuuᵀ and C=I−αvvᵀ, 0<α<2. The exact IID-with-replacement Gram average over four ordered two-update sequences is (B⁴+C⁴+BC²B+CB²C)/4, while uniform random reshuffling without replacement is (BC²B+CB²C)/2. Their difference D=(β/4)[(β+α²ρ²)(P+Q)−2α(PQ+QP)], β=α(2−α), P=uuᵀ,Q=vvᵀ. P+Q has orthogonal eigenvectors u±v with eigenvalues 1±ρ; substitution yields λ±=α²(2−α)(1−ρ²)[2−α(1±ρ)]/4. λ−>0 for α∈(0,2), λ+ changes sign exactly at α=2/(1+ρ); thus RR beats IID for all deterministic e exactly up to that sharp threshold, with equality only e∥u+v at boundary. Above threshold IID wins on + direction, while RR wins on −. Independent exact rational computation gives u=(1,0),v=(3/5,4/5),α=3/2,e=(2,1), E_I=161/100,E_R=197/100, D spectrum {−9/125,63/250}. Convergence is separate: IID stepwise mean-square contraction 1−β(1−ρ)/2 and both deterministic two-row sweep norms <1, hence RR epoch convergence. Source verify.py independently inspected.

## originality

PASS

Qualified PASS for necessary-and-sufficient two-update directionwise sign reversal criterion at overrelaxation α>1, within convergent regime. Existing unrelaxed RR-Kaczmarz proofs, noncommutative arithmetic-geometric mean comparisons for positive semidefinite update operators, and deterministic finite-horizon two-row overrelaxation concern different norms or sampling protocols. The exact two-projection matrix formula may be implicit in earlier matrix-product inequalities, which is recorded as risk.

## value

PASS

Sharp α=2/(1+ρ) frontier exposes non-monotone algorithmic performance under overrelaxation, with exact rational counterexample where both algorithms still converge; quantifies when a general preference for sampling without replacement fails in its first nontrivial noncommuting setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
