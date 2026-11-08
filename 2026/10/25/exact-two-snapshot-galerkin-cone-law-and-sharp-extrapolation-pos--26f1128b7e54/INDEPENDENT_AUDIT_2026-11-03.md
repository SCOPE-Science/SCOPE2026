# Independent mathematical audit

## correctness

PASS

For all finite m>=2, with s<t in interval I, fixed nonzero b, A(y)=A0+yA1 real SPD and independent exact snapshots us=A(s)^-1 b, ut=A(t)^-1 b, the Gram G(y)=U^T A(y)U is SPD. Let a=b^T us, d=b^T ut; strict Cauchy-Schwarz in A(s) and A(t) gives Ks=a ut^T A(s)ut-d^2>0 and Kt=d us^T A(t)us-a^2>0. Because A(y)=alpha A(s)+beta A(t), alpha=(t-y)/(t-s), beta=(y-s)/(t-s), the reduced entries are G11=alpha*a+beta*us^T A(t)us, G12=alpha*d+beta*a, G22=alpha*ut^T A(s)ut+beta*d. Cramer's rule yields det(G)c_s=alpha Ks and det(G)c_t=beta Kt, thus nonnegative coefficients iff y in [s,t]∩I; no convex-hull sum-to-one assertion. The rational diagonal m=3 witness with A(y)=I+y diag(1/10,1/2,9/10), b=(1,3,10), s=0,t=1/2,y=-9/10 has exact projected first component -140484100/176978669, although A(y)^-1 b=(100/91,60/11,1000/19)>0 and both snapshots positive; independent exact rational calculation reproduced the determinant 404522672/165571875 and c=(523575200,-570826575)/25282667. For m=2 full-span snapshots give exact positive solution, and rank-one Galerkin spaces have positive scalar coefficient when the exact solution at the query parameter is coordinatewise positive; same m=1. No claim outside I, no more than two snapshots, no varying RHS. This is a universal algebraic proof, not inference from sample tests.

## originality

PASS

Qualified best-of-knowledge assessment of the exact iff signed two-snapshot Galerkin coordinate formula, its sharp interpolation cone domain, and minimal-dimensional extrapolated physical-positivity failure. The closest 2011 reduced-basis review (actual full PDF sections) formulates general Galerkin projection and best energy-norm approximation, not these coefficient signs. The accessible original 2002 Maday–Patera–Turinici HAL full article describes exponential best-approximation/convergence bounds (Theorem 3), which do not imply pointwise signs. The September 2026 Hannukainen–Toresen paper is especially relevant and explicitly presents ROM error/stability estimates at abstract level; its complete body was inaccessible in this execution, so its possible unindexed sign observation remains a material residual risk. Actual Resultary searches returned positivity defect and Krylov-method findings for distinct operators, not implication coverage. Negative searches alone are not novelty proof. No certificate of priority is asserted.

## value

PASS

The two-exact-snapshot Galerkin method is a natural simplest nontrivial parametric reduced-basis model, while physical coordinatewise nonnegativity is structurally important in diffusion and concentration models. The theorem determines the full parameter interval where the surrogate is automatically in the snapshot positive cone using only coercivity, symmetry, affine dependence and fixed load, and distinguishes cone membership from convex combination. The minimal dimension-three diagonal positive-system counterexample identifies a sharp and realistic extrapolation obstruction even when the full solution stays strictly positive, clarifying why error estimates do not guarantee physical sign. This is a motivated exact structural/boundary lemma rather than arbitrary finite numerology; no general higher-rank or nonsymmetric theorem is claimed. The derivation is short 2x2 algebra, but the sharp classification and physical failure witness are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
