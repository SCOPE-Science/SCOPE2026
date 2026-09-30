# Non-displaceability and Newton-polytope rigidity of the k>2 toric-mutated monotone torus in CP^n

## Context

Let X=CP^n with n>=3 and L the monotone toric fibre. Pascaleff-Tonkonog construct higher-dimensional toric mutations of monotone Lagrangian tori and give an explicit wall-crossing rule for disk potentials. Chanda-Hirschi-Wang describe lifted Vianna tori in CP^n and the Markov-edge structure of their Newton simplices. We compare the k>2 Pascaleff-Tonkonog mutation of the Clifford torus with those established families.

## Definitions

Fix 3<=k<=n. For the Pascaleff-Tonkonog mutation at the face and interior lattice point used in their CP^n example, write
P=prod_i y_i and Q=1+sum_{j<k} y_k/y_j.
In the mutated basis the disk potential is

W' = sum_{i=k}^n y_i^{-1} + P Q^k.

The Newton polytope is taken in the standard monomial lattice; affine edge length means the gcd of the coordinates of the edge vector.

## Result

For every n>=3 and 3<=k<=n:

1. W' has the critical point rho=(1/k,...,1/k,1,...,1), with k entries 1/k, and critical value n+1. Hence the corresponding deformed Floer cohomology is nonzero and the mutated monotone torus is Hamiltonian non-displaceable.

2. Newt(W') is the n-simplex with vertices
   C=(1,...,1),
   P^(j)=C+k(e_k-e_j) for j<k,
   and D_j=-e_j for j>=k.
   Its normalized volume is k^(k-1)(n+1). Exactly the k vertices C,P^(1),...,P^(k-1) are incident to an edge of affine length k; all other edges have affine length one.

3. This Newton simplex is not GL(n,Z)-equivalent to the Clifford simplex and is not GL(n,Z)-equivalent to any lifted Vianna Newton simplex described by Chanda-Hirschi-Wang. Thus the mutated torus is not symplectomorphic, and in particular not Hamiltonian isotopic, to the Clifford torus or to any torus in that lifted Vianna family.

The single Pascaleff-Tonkonog k>2 wall-crossing transformation is non-binomial, as already observed in their paper. No claim is made here that it cannot be expressed as a finite composition of arbitrary binomial or solid mutations; Pascaleff-Tonkonog describe such finite non-factorization as an expectation rather than a proved consequence.

## Proof / evidence

At rho, Q=k. Differentiating W' shows that every partial derivative vanishes: for j<k the two contributions in the Q-derivative cancel, for y_k the inverse-monomial derivative -k^2 is cancelled by the P Q^k derivative, and for j>k the two derivatives are -1 and +1. The value is n from the inverse terms plus 1 from P Q^k.

Expanding P Q^k shows that its exponent support lies in Conv(C,P^(1),...,P^(k-1)) and contains all of those vertices. Adding the inverse monomials gives the stated simplex. Taking edge vectors from C and performing unimodular column operations gives determinant k^(k-1)(n+1). Differences inside {C,P^(j)} have coordinate gcd k. Every edge involving a D_j has a coordinate equal to +/-1, and D_j-D_l=e_l-e_j, so all such edges have affine length one.

The volume already excludes the Clifford simplex. Chanda-Hirschi-Wang's lifted Vianna simplex has one distinguished triangular face whose three edge lengths form a Markov triple, with all other edges of length one. For k>3 our simplex has k>=4 vertices incident to long edges, so the incidence pattern differs. For k=3 its long triangle has edge lengths (3,3,3), which is not a Markov triple since 3^2+3^2+3^2=27 whereas 3*3*3*3=81.

The Floer non-displaceability implication uses the standard monotone-torus criterion that a critical local system of the disk potential has nonzero deformed Floer cohomology.

## Limitations

The argument takes the Pascaleff-Tonkonog existence, monotonicity and wall-crossing theorem as input, and uses the Chanda-Hirschi-Wang Newton-simplex description for the lifted Vianna family. It proves no classification of all monotone tori in CP^n and no finite-binomial-factorization obstruction. The symbolic verifier checks the displayed critical point and Newton-polytope arithmetic for 3<=k<=n<=7; the algebraic proof is uniform in n and k.

## Reproducibility

Run `artifacts/verify_target.py` with sympy installed. It checks the critical point/value, determinant, affine edge lengths, long-edge incidence count and the non-Markov (3,3,3) test for 3<=k<=n<=7.

## References

- James Pascaleff and Dmitry Tonkonog, The wall-crossing formula and Lagrangian mutations, Advances in Mathematics 361 (2020), arXiv:1711.03209.
- Sayantan Chanda, Joé Hirschi, and Bing Wang, Infinitely many monotone Lagrangian tori in higher projective spaces, arXiv:2307.06934.
- Standard Cho-Oh / Fukaya-Oh-Ohta-Ono monotone torus Floer critical-point criterion.
