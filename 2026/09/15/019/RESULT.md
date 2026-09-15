# Non-displaceability and Hamiltonian rigidity of the k>2 toric-mutated monotone torus in CP^n

## Context

Let X = CP^n with n >= 3 and L the monotone toric fibre. Pascaleff-Tonkonog construct higher-dimensional toric mutations of monotone Lagrangian tori with an explicit wall-crossing rule for disk potentials (Theorem 5.7). Chanda-Hirschi-Wang lift Vianna's CP^2 exotic tori to CP^n and show finite binomial (k=2, solid) mutations from the Clifford torus stay inside the lifted Vianna family with Markov Newton data (Proposition 4.6). The question is whether the k>2 toric mutation of the Clifford torus in CP^n produces a non-displaceable torus distinct from the Clifford torus and from every lifted Vianna torus, so that its wall-crossing map is not binomially realizable.

## Definitions

Standard monotone polytope of CP^n: Delta = {x_i >= -1, sum x_i <= 1}. Fix 3 <= k <= n. Let F be the (n-k)-face in {x_1 = ... = x_k = -1} with interior lattice point w = (-1,...,-1,0,...,0) (k entries -1). Let L' = mu_{F,w} L be the monotone torus of Pascaleff-Tonkonog Theorem 5.7 / Example 5.5 / Corollary 5.8. Write P = prod y_i and Q = 1 + sum_{j<k} y_k/y_j. In the mutated basis (up to GL(n,Z) by PT Lemma 5.9) the disk potential is W' = sum_{i=k}^n y_i^{-1} + P Q^k. Its Newton polytope Newt(W') is taken in the standard monomial lattice. A critical point rho in (C*)^n means all partial derivatives of W' vanish at rho. The Clifford torus has potential sum x_i + (prod x_i)^{-1} with simplex volume n+1 and all edges affine length 1. Lifted Vianna tori T^{(n)}_{(a,b,c)} have Newton simplices with one triangular face of Markov lengths (a,b,c) and all other edges length 1 (CHW Proposition 4.6).

## Result

For every n >= 3 and 3 <= k <= n, the mutated torus L' satisfies: (i) W' admits the critical point rho = (1/k,...,1/k,1,...,1) in (C*)^n with critical value n+1, hence HF^*((L',rho),(L',rho)) is isomorphic to H^*(T^n;C), nonzero, and L' is Hamiltonian non-displaceable in CP^n; (ii) Newt(W') is the n-simplex on vertices C = (1,...,1), P^{(j)} = C + k(e_k - e_j) for j < k, and D_j = -e_j for j >= k, with normalized volume k^{k-1}(n+1), exactly the complete graph K_k on {C, P^{(j)}} of affine edge length k and every other edge of length 1, so exactly k vertices are incident to a long edge; (iii) L' is not symplectomorphic (hence not Hamiltonian isotopic) to the Clifford torus nor to any lifted Vianna torus T^{(n)}_{(a,b,c)}; for k > 3 by long-incidence count k >= 4 versus at most 3, and for k = 3 because the long triangle (3,3,3) is not Markov (27 != 81); (iv) consequently the k>2 wall-crossing map producing (5.6) is not realized by any finite sequence of k=2 binomial/solid mutations.

## Proof / evidence

Telescoping derivation: substituting the PT rule into W_L, the k terms y_i^{-1} for i <= k sum to 1/y_k, giving W' = sum_{i>=k} y_i^{-1} + P Q^k with all positive coefficients. Gradient check: at rho, Q = k. For j < k, dW'/dy_j = (P Q^{k-1}/a)(Q - k b/a) = 0 since Q = k and b/a = 1. For y_k, dW'/dy_k = -1/b^2 + P Q^{k-1}[Q/b + k(k-1)/a] = -k^2 + (1/k)(k^3) = 0. For j > k, dW'/dy_j = -1/c^2 + (P/c)Q^k = -1 + 1 = 0. Value: sum_{i>=k} rho_i^{-1} = n plus P Q^k = 1, total n+1. Monotonicity is PT Theorem 5.7; the Floer implication is the standard Cho-Oh/FOOO torus criterion. Newton analysis: expanding P Q^k gives monomials M(m) in Conv(C, P^{(j)}) with C and each P^{(j)} occurring; together with D_j this yields Conv(S). Edge matrix from C with A_i = k(e_k - e_i), B_j = -u - e_j reduces by unimodular operations to volume k^{k-1}(n+1), proving S affinely independent. Affine lengths: C-P^{(i)} and P^{(i)}-P^{(j)} differences are multiples of k with gcd k; every pair involving D_j has a coordinate 1 (using k-1 >= 2), and D_j - D_l = e_l - e_j, all length 1. Since k^{k-1} >= 9, volume excludes Clifford; CHW Proposition 4.6 induction excludes lifted Vianna as above; binomial closure (CHW Theorem 3.4) then excludes binomial realizability. Reproducible check: output/artifacts/verify_target.py (sympy) passes gradient, value, volume, edge pattern, incidence count, and non-Markov tests for 3 <= k <= n <= 7.

## Limitations

The argument takes as input the Pascaleff-Tonkonog Theorem 5.7 package (existence and monotonicity of the mutated torus and the wall-crossing rule in the stated basis, up to GL(n,Z)) and the standard facts that a critical point gives nonzero deformed Floer cohomology and that the Newton polytope up to GL(n,Z) is a symplectomorphism invariant. Symbolic verification covers 3 <= k <= n <= 7 with analytic proofs valid for all n, k in range. No claim is made beyond the stated (F, w) family or about Hamiltonian isotopy classes within the new family itself.

## Reproducibility

Run python3 output/artifacts/verify_target.py with sympy installed; expect ALL CHECKS PASSED. Inputs: DRAFT.md derivation, PT reference (Adv Math 361:106850, arXiv:1711.03209), CHW reference (arXiv:2307.06934).

## References

Pascaleff-Tonkonog, The wall-crossing formula and Lagrangian mutations, Adv Math 361 (2020), arXiv:1711.03209. Chanda-Hirschi-Wang, Infinitely many monotone Lagrangian tori in higher projective spaces, arXiv:2307.06934. Vianna, Infinitely many exotic monotone Lagrangian tori in CP^2. Cho-Oh / FOOO torus Floer criterion; Sheridan.
