# Independent mathematical audit

## correctness

PASS

Independently, K=⟨g,h⟩ has order p³ since [g,h] generates the center and the two projections are independent. Left translation splits the regular space into p^(2n−2) copies on right cosets Kx. In coordinates g^i h^j [g,h]^k on K, Fourier transform in j and k makes h diagonal and g a cyclic shift in i. At zero central frequency a further Fourier transform gives each ordered pair of p-th roots once per coset. At each nonzero central frequency the h-diagonal runs through the p distinct roots of unity, with one clock–shift copy for each of the p j-frequencies. The two determinant permutations of a cyclic bidiagonal matrix give ∏_j(λ−a−cζ^j)−b^p=(λ−a)^p−c^p−b^p. For b≠0 the kernel recursion determines every coordinate from one, including the multiple-root case; if b=0 at a singular block then c≠0 and the diagonal entries are distinct. This establishes geometric nullity separately from algebraic multiplicity. The two-circle intersection bound, zero-coefficient strata and equilateral equal-weight case check directly. The three separation examples follow from equality in the triangle inequality, the cyclotomic degree obstruction to 2^(1/p), and the unique equilateral ordering permitted by a p-th-root phase, respectively. The packaged modular rank checker was inspected, not run. Independent phase-count arithmetic on its 15 inputs confirms a minor reporting limitation: none has Z=0 and F=0, contrary to the prose saying it tests a purely nonabelian case. It does not check characteristic polynomials or the all-n theorem; the analytic reconstruction checks the omitted stratum.

## originality

PASS

The exact ternary unweighted nullity is already covered and is not individually novel. The supported distinct claim is the full weighted, all-odd-prime factorization together with its geometric rank strata and how the two singular loci intersect, rather than the known Heisenberg representations or Cayley decomposition.

## value

PASS

For the minimal support with genuinely noncommuting generators, the theorem gives all singular weights and exact information loss (the geometric kernel dimension), even at defective blocks where a spectral multiplicity is misleading. The combination of phase resonances and a separate Fermat condition, with examples of both mechanisms occurring separately and together, provides a useful complete classification rather than another evaluation of the unweighted ternary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
