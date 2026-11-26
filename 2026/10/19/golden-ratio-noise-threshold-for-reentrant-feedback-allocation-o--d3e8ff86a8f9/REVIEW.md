# Independent mathematical audit

## correctness

PASS

For a connected unit star and an exact positive budget, the quadratic form of L+diag(g) is positive definite even on the simplex boundary. The trace of the covariance is half of J by the Lyapunov equation. The second differential of J is twice tr(PK^2) for P positive definite and K a nonzero symmetric conjugate of the gain perturbation. Compactness and strict convexity give uniqueness, and uniqueness under leaf permutations forces equal leaf gains without imposing them beforehand. With x the hub gain, y=(B-x)/m, the Schur denominator is B+xy. Independent differentiation gives F'(0)=m(m-1)/(B+m)^2-rho(B+2m)/(m^2 B) and F'(B)=1+2/B. This yields exactly the claimed non-strict hub-zero criterion, rules out x=B, and gives a unique interior critical point otherwise. For z=B/m, f(z)=z/[(1+z)^2(2+z)] has derivative 2(1-z-z^2)/[(1+z)^3(2+z)^2], vanishes in value at the two limiting ends, and has peak (5sqrt(5)-11)/2 at z=(sqrt(5)-1)/2. This proves the two-root, tangency and no-root cases including ties. The end expansions f(z)~z/2 and f(z)~z^-2 give both budget asymptotics for fixed rho; at m=2 and rho=1/6 the equation factors as (B-2)(B^2+10B-8). Replay by the block inverse and the endpoint calculations above and in RESULT.md §§1–5. The package records 3,371 checker assertions; its uploaded code was not executed for this review. The proof, not the recorded tests, covers all parameters.

## originality

PASS

Best-of-knowledge pass for the joint heterogeneous-noise/budget diagram, sharp cusp and switching scales; not for generic convexity, inverse-trace methods, or uniform-noise reentrance. The strongest catalogue match is exactly the rho=1 slice, not the two-parameter classification. Catalogue dates do not establish dependence or priority.

## value

PASS

The natural question is whether increasing a continuous stabilizing feedback budget preserves the support of an optimal controller. The result gives an exact nonmonotonicity region with a sharp tangency boundary, different small and large switching scales, and a three-node witness that the uniform-noise case cannot supply. This is a substantive support classification, not just a stationarity formula or a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
