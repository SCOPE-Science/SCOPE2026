# Independent mathematical audit

## correctness

PASS

Let c=2−2^(1/q)>0 for finite p≥1, with conjugate q and σ=1/(2−c)=2^(−1/q). The concrete B_c=min(u,v,max((u+v−c)/(2−c),0)) is a bivariate copula: for fixed u its conditional u derivative is nondecreasing as v increases, giving nonnegative rectangle volumes by integration, with correct margins. Its a.e. gradients (0,0),(1,0),(0,1),(σ,σ) all have dual ell_q norm≤1, as does M=min(u,v). Convex interpolations in disjoint ordinal-sum blocks and fixed top B_c block therefore form copulas globally one-Lipschitz in ell_p. At the strict middle-affine point of the fixed top block the gradient equals (σ,σ), whose dual ell_qprime norm exceeds 1 for every p′>p (also p′=infinity); every member has exact sharp p threshold, including p=1 and any finite p>1. The family parameterized by x∈[0,1]^N is affine, uniformly continuous in the product topology because the n-th block has height 2^(−n−1), hence compact and convex in sup norm. For x_n=t^n, a hypothetical finite linear relation vanishes at (1,1) and then yields ∑a_j t_j^n=0 on each nonanchor block; the first k such relations are an invertible Vandermonde system. Thus the compact convex set contains continuum many linearly independent members, maximal by cardinality of C([0,1]^2). Source check.py was inspected; its finite grids cannot establish the infinitely many p thresholds, which are separately proved.

## originality

PASS

The exact Lipschitz-exponent copula class and B_c base family appear in de Amo et al. (2026); its Theorem 3.6 proves maximal convex lineability and its conclusion explicitly leaves convex spaceability of precisely this class open. The fixed top block plus independently variable shrinking blocks supplies the missing norm closure and linearly independent continuum. No stronger coverage was found.

## value

PASS

Constructs a compact convex continuum-linearly-independent family inside a natural sharp-Lipschitz copula class, answering an explicit 2026 open convex-spaceability problem. The fixed-anchor/variable-shrinking-block mechanism is reusable for preserving a sharp invariant while enforcing closure; substantial motivated structure beyond a routine Lipschitz check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
