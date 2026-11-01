# Independent mathematical audit

## correctness

PASS

For q odd and q≡3 mod4, −1 is nonsquare, making Q(x)=x₁²+x₂² anisotropic. The exact published q^{-2} input/q³ counting-target normalization gives best fourth-power constant 1+q^{-1}−q^{-2}, and published §4.1 yields nonzero constant modulus. In pair-sum fibers (s,t), write u=s/2+d, v=s/2−d: Q(d) is fixed, with exactly one ordered pair for radius zero and q+1 ordered pairs otherwise. The sharp proof has a sum of nonnegative fiberwise Cauchy–Schwarz deficits; equality forces f(x)f(x+a+b)=f(x+a)f(x+b) whenever a·b=0. Nonzero modulus makes D_a f well-defined; D_a f(x) is constant along a⊥ and depends only on x·a. For linearly independent a,b, B_x(a,b)=D_af(x+b)/D_af(x) depends separately on x·a and x·b, so is constant in x. For collinear a,b choose c outside F_q a and use D_bf(x)=D_cf(x)D_{b−c}f(x+c) to reduce mixed differences to independent pairs; zero increments are trivial. The resulting B(a,b) is a symmetric additive bicharacter trivial on orthogonal pairs. For fixed a≠0 it is χ_a(a·b); linear independence of a,a′ and surjectivity of b↦(a·b,a′·b) show χ_a=χ_a′=χ_{a+a′}, and a third vector connects collinear a’s. Thus B(a,b)=ψ(δ a·b) for one δ∈F_q. Divide f by ψ((δ/2)Q) to get a linear character times λ, giving precisely ψ(αu₁+βu₂+γQ(u)). Conversely target translations by (α,β,γ) preserve the full L⁴ sum, so all chirps saturate. Equality of projective chirps implies their second-difference δ vanishes, then their first differences vanish; trace pairing nondegeneracy proves q³ distinct classes. This covers q=3, nonprime extension fields, λ≠0, and all odd q≡3 mod4. Independent checks: exact unordered pair-fiber cardinalities and phase linear constraints at p=3,7 give mod-p ranks 5,45; p=3 integer Smith normal form has rank 8 and invariant factors 3,3,3, yielding exactly 27 projective solutions; normalized fourth moments from exact pair counts equal 1+1/p−1/p². Finite tests corroborate but are not the general proof.

## originality

PASS

Best-of-knowledge originality for the COMPLETE complex-phase classification in the anisotropic q≡3 (mod 4) branch. González-Riquelme–Oliveira e Silva, arXiv:2405.16647 Theorem 1.1 proves the sharp constant and constant-modulus necessity; their Theorem 1.2 is restricted to q≡1 (mod 4), and §4.1 ends before classifying anisotropic phases. González-Riquelme–Ismoilov arXiv:2509.05600 §1.2 explicitly says the paraboloid complex phase issue had only been settled in the opposite congruence class; its theorems concern four-dimensional punctured cones. Ronda arXiv:2609.13023 treats nondegenerate homogeneous quadratic level sets (spheres/cones), not the rank-two quadratic graph with linear t term, and establishes constant modulus rather than this phase census. Older orthogonally additive functional equations may overlap a lemma but no actual checked theorem implies the exact q³ projective finite-field extremizer classification. The exact indexed mirror is not prior independent coverage. Nonappearance in searches is not priority proof.

## value

PASS

The exact complex equality locus for the anisotropic half of the sharp endpoint paraboloid inequality is a natural structural problem left by the known constant and constant-modulus result. A modulus constraint leaves a huge torus of possible phases; the theorem instead proves complete rigidity to three field parameters and counts exactly q³ projective extremizers for every relevant prime power. This is a motivated natural classification of all optimizers, not merely another sharp norm, finite-table recomputation, arbitrary parameter slice or textbook substitution. The phase-rigidity argument uses orthogonal finite differences and bilinear character geometry and is independently useful to researchers analyzing equality/stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
