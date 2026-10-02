# Minimal pair in the degree spectrum of a finite-Ulm-length p-group

## Context

Fix a prime p. For a countable structure G with universe omega, the degree
spectrum DgSp(G) is the set of Turing degrees of atomic diagrams of structures
with universe omega isomorphic to G, computable or not. A minimal pair of
Turing degrees is a pair a,b > 0 with a wedge b = 0. Lachlan and Yates
independently proved that minimal pairs exist among the c.e. degrees; a later
Jockusch–Soare construction gives another route to the same existence fact.

## Definitions

- H = Z/p² (+) Z/p. G = countable direct sum of H, the countable direct sum of copies of H.
- Ulm subgroups: G_0 = G, G_{alpha+1} = p G_alpha, and intersections at limits.
- Ulm invariants f_alpha(G) = dim_{F_p} P_alpha/P_{alpha+1}, where
  P_alpha = {x in G_alpha : p x = 0}.
- P(A) = pA = {x : exists y (p y = x)}.
- Coding block B = H (+) H with standard layout B⁰ and transported layout B¹.
  In B⁰ fix socle elements t*=b, which is not p-divisible, and s*=pc, which is
  p-divisible. B¹ is obtained by transporting the operation across the
  transposition swapping t* and s*.
- For a c.e. set C, A_C is the countable direct sum whose i-th block uses B¹
  iff i is in C and B⁰ otherwise.

## Result

For every prime p, the computable reduced abelian p-group

  G = countable direct sum of Z/p² (+) countable direct sum of Z/p

has Ulm length exactly 2, divisible part 0, Ulm invariants
f_0 = f_1 = aleph_0 and all higher invariants 0. Its degree spectrum contains
every c.e. degree. Consequently its degree spectrum contains a minimal pair.

More explicitly, for every c.e. C there is a copy A_C isomorphic to G with
deg(A_C)=deg(C).

## Proof / evidence

Lemma (invariants). Since p²G=0 but pG is nonzero, the Ulm length is exactly 2.
A bounded p-group has no nonzero divisible subgroup. In the standard Ulm
quotients, each Z/p summand contributes one dimension to f_0, while each
Z/p² summand contributes one dimension to f_1. Since there are infinitely many
summands of each type, f_0=f_1=aleph_0.

Block pair. In the standard block, s*=pc is p-divisible and t*=b is not:
every p-multiple has zero Z/p-coordinates. Transporting the group law through
the transposition swapping t* and s* produces an isomorphic group in which
their p-divisibility statuses are swapped.

Purity. If an element supported only in block i equals p times an element of
A_C, projection to block i shows it is already p-divisible inside that block.
Thus, for fixed single-block witnesses tau_i and sigma_i,

  tau_i in pA_C  iff  i in C,
  sigma_i in pA_C iff i not in C.

Degrees. From an atomic-diagram oracle for A_C, dovetail the two searches
p y=tau_i and p y=sigma_i. Exactly one succeeds, deciding membership in C.
Hence C <=_T A_C. Conversely, a C-oracle decides the final layout of every
block touched by an addition query, and the finite block tables then compute
the operation. Hence A_C <=_T C, so deg(A_C)=deg(C).

Choose noncomputable c.e. sets C,D whose degrees form a minimal pair; existence
is due independently to Lachlan and Yates. Then A_C and A_D are isomorphic
copies of G of those two degrees, so DgSp(G) contains a minimal pair.

The stored finite checker verifies the two transported block laws and witness
patterns for p=2,3,5. The general-prime proof above is algebraic and does not
depend on those finite tests.

## Limitations

- Existence of a c.e. minimal pair is used as a classical black box.
- Only c.e. degrees are claimed here, although the same transported-block idea
  can be considered more broadly.
- The finite script checks sample primes only; the theorem for arbitrary p rests
  on the uniform transport argument.

## Reproducibility

`artifacts/check_blocks.py` records finite sanity checks for p=2,3,5. The
audit independently checked the Ulm quotients, the transport identity, the
block-projection argument, and both Turing reductions.

## References

- A. H. Lachlan, Lower bounds for pairs of recursively enumerable degrees,
  Proc. London Math. Soc. 16 (1966), 537–569.
- C. E. M. Yates, A minimal pair of recursively enumerable degrees,
  J. Symbolic Logic 31 (1966), 158–168.
- C. G. Jockusch Jr. and R. I. Soare, A minimal pair of Pi-zero-one classes,
  J. Symbolic Logic 36 (1971), 66–78.
- W. Calvert, D. Cenzer, V. Harizanov, A. Morozov, Effective categoricity of
  Abelian p-groups, arXiv:0805.1889.
- A. Melnikov, New Degree Spectra of Abelian Groups,
  Notre Dame J. Formal Logic 58 (2017), 507–525.
