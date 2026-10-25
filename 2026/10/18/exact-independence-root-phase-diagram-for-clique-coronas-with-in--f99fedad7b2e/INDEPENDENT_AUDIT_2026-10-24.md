# Independent mathematical audit

## correctness

PASS

An independent set of G_{r,k}=K_r corona edgeless K_k contains no core vertex or exactly one; this yields I=(1+z)^{k(r−1)}((1+z)^k+r z), with −1 roots irrelevant for right-half-plane counts. At z=iy, y>0, argument of (1+iy)^k=−riy forces kθ=(4j+3)π/2 with θ=arctan y∈(0,π/2), and r=1/(sinθ cos^{k−1}θ); these are all axis crossing parameters. Derivative ∂_zQ=r(1−(k−1)z)/(1+z)≠0 on axis. Implicit derivative Re(dz/dr)=k y²/[r(1+(k−1)²y²)]>0, so each conjugate pair moves left to right. Since roots start at −1 as r→0 and degree stays fixed, full right-half-plane/root-on-axis counts follow without missed crossings. Independent NumPy root checks for k=1..12 and r=0.1,1,2,8,10,20,60,300 matched exact threshold counts; tested k=6,r=8 algebraic factor separately by SymPy. Limits: real r parameter for Q; graph only integer r.

## originality

PASS

PASS best of knowledge: Brown–Cameron 2018 Theorem 3.2 credits the corona polynomial identity and Section 4 studies qualitative instability/other multipartite families; its Proposition 3.1 is the r=1 star, not arbitrary r. Hibi–Kara–Vien 2026 full HTML gives leaf-attachment coefficients, values at −1 and symmetry, not precise right-half-plane crossings. No inspected Resultary phase diagram matched Q_{r,k}.

## value

PASS

Exact two-parameter half-plane root counts and threshold boundary multiplicities are natural analytic invariants in independence-polynomial stability. A family with a well-known factorization still has nontrivial multiple crossings (at k=8), and the theorem gives a complete classification beyond numerical roots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
