# Independent mathematical audit

## correctness

PASS

For the published finite-parameter four-operator iteration at α=β=η, γ=η/2 on f=Fx²/2,p=−Px²/2, define u=ηF>v=ηP≥0. Direct substitution of exact prox maps gives the full 2×2 state matrix M with first row ((1+v)/2,(1−u)/(2(1+u))) and second row (τ(1+v)/2,1−τ/2). The three Jury inequalities simplify to τ(u−v)/(2(1+u))>0, v+3−τ(u+v+2)/(2(1+u))>0, (1−v+τ(1+v)/(1+u))/2>0; hence the precise open stability window. For v>1 endpoint collision iff u≥u_c(v)=v+8+16/(v−1), minimum u_c=17 at v=5; a nontrivial eigenvalue −1 Jordan collision occurs at equality. A common τ for all v<u requires u−1<U(0)=6(1+u)/(u+2), yielding u<(5+sqrt57)/2; separate 0<u≤1 case admits τ=1. The smooth witness p″=−5+5(cosx−cos2x)∈[−15,5/8] gives globally ≥5-convex objective and Jacobian M(20,5,τ) unstable for all τ>0, establishing local fixed-point instability, not global divergence. Independent SymPy checked all Jury identities, collision and 6 unstable witness rates. One nonessential source phrase says U(v) increases for every u>0; the exact derivative has sign(u−1), so that phrase is false when u≤1. Its use is only in the u>1 case, and the u≤1 case is separately settled; the stated theorem survives intact. It should be corrected editorially before publication.

## originality

PASS

Alcantara–Lee–Takeda introduce the four-operator iteration and prove global subsequential convergence under sufficient conditions; these are all prior. Their full preprint Algorithm 1 matches the audited finite-parameter map but does not provide the complete necessary-and-sufficient scalar Schur window, the two curvature ceilings, or the explicit strongly-convex weak-concavity instability construction. General Jury criteria are textbook prior methods, while application and sharp collision calculation to this exact algorithm are specific. Related doubly relaxed forward-Douglas–Rachford work addresses a different step map. Best-of-knowledge originality with other finite-parameter stability-table risk.

## value

PASS

Knowing precise allowable relaxation intervals and a hard obstruction to *any* relaxation on a strongly convex test problem is a substantive algorithmic boundary, especially separating per-instance parameter tuning (17) from a robust common choice ((5+sqrt57)/2). The smooth instability witness clarifies why a source's sufficient small-step hypotheses matter; it is not merely checking a randomly chosen scalar matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
