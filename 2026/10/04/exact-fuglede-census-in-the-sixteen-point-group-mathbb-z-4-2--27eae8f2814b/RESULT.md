# Exact Fuglede census in the sixteen-point group \(\mathbb Z_4^2\)
## Finding
Let \(G=(\mathbb Z/4\mathbb Z)^2\), written additively and identified with its character group by
\[
\chi_\xi(x)=i^{\langle x,\xi\rangle}.
\]
For every nonempty \(A\subseteq G\), the following are equivalent: \(A\) is spectral, and \(A\) tiles \(G\) by translations. Exactly \(2155\) nonempty subsets satisfy these conditions. Their cardinality distribution for \(|A|=1,2,4,8,16\) is
\[
16,\ 120,\ 1244,\ 774,\ 1,
\]
and there are no examples of any other size. Modulo affine automorphisms of \(G\), the corresponding orbit counts are
\[
1,\ 2,\ 8,\ 7,\ 1,
\]
so there are exactly \(19\) affine classes.

## Assumptions and scope
A spectrum of \(A\) is a set \(B\subseteq G\) with \(|B|=|A|\) such that the characters indexed by \(B\) are pairwise orthogonal on \(A\). A tiling complement is a set \(T\subseteq G\) for which every element of \(G\) has a unique representation \(a+t\) with \(a\in A\) and \(t\in T\). The affine equivalence uses all translations and all invertible \(2\times2\) matrices over \(\mathbb Z/4\mathbb Z\).

## Proof
For a fixed \(A\), compute its Fourier zero set
\[
Z_A=\{\xi\in G:\sum_{a\in A}i^{\langle a,\xi\rangle}=0\}.
\]
All values lie in the Gaussian integers, so zero testing is exact. If a spectrum exists, translating it lets us assume that it contains \(0\). Thus \(A\) is spectral exactly when there is a set \(B\ni0\) of size \(|A|\) such that every nonzero difference in \(B-B\) lies in \(Z_A\). This is a finite clique condition checked over every candidate \(B\).

Likewise, if a tiling complement exists, translating it lets us assume that it contains \(0\). For \(D(S)=S-S\), uniqueness of sums is equivalent to
\[
D(A)\cap D(T)=\{0\},
\]
together with \(|A||T|=16\). The exhaustive check therefore tests every possible complement of the forced size. Running these two independent exact predicates over all \(2^{16}-1=65535\) nonempty subsets gives identical truth values in every case and the stated cardinality counts.

For the affine quotient, an invertible matrix over \(\mathbb Z/4\mathbb Z\) is exactly one with odd determinant. There are \(96\) such linear maps and hence \(1536\) affine maps after translations. Orbit closure of the \(2155\) good sets yields the profile \(1,2,8,7,1\).

## Verification
The bundled `verify.py` re-enumerates all nonempty subsets, computes Fourier sums as integer pairs representing Gaussian integers, tests the exact spectrum and tiling criteria, and then computes affine orbits. Its reviewed run returned:

`VERIFY_OK total=2155 size_counts=16,120,1244,774,1 affine_orbits=1,2,8,7,1 GL2Z4=96`

The computation is exhaustive because every nonempty subset of the sixteen-point group is visited and, after the harmless translation normalization, every candidate spectrum or tiling complement of the required size is visited.

## Relationship to prior work
Malikiosis, arXiv:2005.05800, surveys the finite-abelian Fuglede landscape and records positive two-generator results for \(\mathbb Z_p\times\mathbb Z_p\), then \(\mathbb Z_p\times\mathbb Z_{p^2}\), and more generally \(\mathbb Z_p\times\mathbb Z_{p^n}\); these do not include \(\mathbb Z_4\times\mathbb Z_4\). Zhou, arXiv:2412.16865, studies \(\mathbb Z_{p^2}\times\mathbb Z_{p^2}\) directly but proves structural spectral statements only for special tiling complements and explicitly motivates the analysis from the still-limited understanding of such tiling pairs. Fan--Kadir, arXiv:2609.00087, gives tile-without-spectrum counterexamples in substantially larger finite abelian \(p\)-groups, including an exponent-four group, so the small square group is a meaningful positive boundary case.

## Limitations
This is a complete finite classification only for \(\mathbb Z_4^2\). It does not assert Fuglede's conjecture for \(\mathbb Z_{p^2}^2\) at odd primes or for larger exponent-four groups. Priority risk remains that an unindexed table, thesis, or source using different terminology may have recorded the same order-sixteen census.

## References
1. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800; Forum of Mathematics, Sigma 10 (2022), e23.
2. W. Zhou, *Mutual Annihilation of Tiles* / *An Equi-distribution Equality of Tiles*, arXiv:2412.16865.
3. S. Fan and M. Kadir, *Translational tiles without spectra in finite abelian p-groups*, arXiv:2609.00087.
