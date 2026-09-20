# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the operator norm to a finite matrix block and uses the diagonal
right-translation symmetry
\[
(r,c)\mapsto(rg,cg)
\]
of the Toeplitz pattern. Infinitely many translates of a fixed finite block can be
chosen with pairwise disjoint initial and final coordinate sets. For Schatten
\(S_p\), disjoint rectangular blocks have exactly the \(\ell_p\)-sum norm; for
\(S_\infty=K\), the norm is the maximum and the closed span is \(c_0\).
Consequently the multiplier acts on the translated-block span as a scalar multiple
of an isometry, with scalar arbitrarily close to its full operator norm.

This single witness gives the Bernstein lower bounds and the exact distance to
strictly singular operators. Finite-rank operators are strictly singular, giving the
approximation-number equality. Finite-codimensional subspaces meet the witness in an
infinite-dimensional subspace, giving the Gelfand equality.

The Kolmogorov and Hausdorff-noncompactness arguments require a separate escape
check because the approximating finite-dimensional subspace or finite covering
centers need not lie in the translated-block span. The rectangular compressions
\[
Q_jz=P_{Rg_j}zP_{Cg_j}
\]
converge to zero on every fixed Schatten-class element and uniformly on every
finite-dimensional set, while \(Q_j(Tx_j)=Tx_j\). This yields the exact Kolmogorov
lower bound and prevents any finite cover with radius below the near-norm block
ratio. The upper bounds are the general norm bounds. The \(p=\infty\) case is valid
because all elements of \(K(\ell_2\Gamma)\) are compact and finite matrix support is
norm-dense.

No complementability assumption is used. The only group-theoretic input is that an
infinite group admits infinitely many pairwise disjoint right translates of a fixed
finite set.

## Originality

**PASS, to the best of our knowledge.**

The classical Schur-multiplier literature establishes boundedness and compactness
criteria in neighboring settings. Bennett (1977) gives foundational Schur-multiplier
theory; Hladnik (2000) characterizes compact Schur multipliers on \(B(H)\);
Aleksandrov--Peller (2002) treats Hankel and Toeplitz--Schur multipliers.
Oikhberg (2010) computes several \(s\)-numbers for elementary rank-one-symbol Schur
multipliers. Neuwirth--Ricard (2011) develops relative Toeplitz--Schur transference
on Schatten--von Neumann--Orlicz classes and explicitly localizes the multiplier norm
to finite rectangles.

The located texts and searchable records did not state that relative Toeplitz Schur
multipliers have all approximation, Gelfand, Kolmogorov and Bernstein numbers equal
to their norm, nor that their distance to the strictly singular class equals the
norm. Exact and synonymous searches combining Toeplitz/Herz--Schur multipliers with
strict singularity, essential norm, these \(s\)-numbers, and maximal noncompactness
did not locate an equivalent theorem.

The most relevant recent analogues are maximal-noncompactness results for
translation-invariant operators on commutative Banach sequence/function spaces and
for Wiener--Hopf operators. They support the general phenomenon but have different
ambient spaces and do not imply the Schatten Schur-multiplier statement directly.

Residual risk remains because the full text of Hladnik (2000) was not available in
the inspected sources, and the older Schur-multiplier/\(s\)-number literature was not
exhaustively checked theorem by theorem. The novelty claim therefore does not rest
on the weaker assertion “nonzero Toeplitz Schur multipliers are noncompact”; it is
centered on the exact flat \(s\)-number profiles and norm distance to strict
singularity.

## Value

**PASS.**

The result identifies an extreme rigidity phenomenon for a standard operator class:
Toeplitz symmetry forces every bounded multiplier to be either zero or maximally
noncompact at every finite-dimensional approximation scale. In particular,
compactness, finite strict singularity and strict singularity collapse to the zero
multiplier inside this class.

The relative-pattern form is useful because it applies directly in the framework
used for Fourier/Schur transference and lacunary subsets, rather than only to the full
matrix algebra. The proof also isolates a reusable mechanism—near-norm finite blocks
plus disjoint symmetry translates—that can be tested in other homogeneous operator
spaces.

## Scientific limitations

- The group must be infinite; finite groups give finite-dimensional Schatten spaces.
- The pattern is Toeplitz/right-diagonally invariant and the multiplier is assumed
  bounded on the stated relative Schatten space.
- Only Banach Schatten classes \(1\le p<\infty\) and \(S_\infty=K\) are covered.
- No assertion is made for arbitrary Schur symbols, quasi-Banach \(0<p<1\), or
  completely bounded \(s\)-number variants.
- Hladnik (2000) was not fully inspected, leaving a documented residual
  prior-coverage risk under different terminology.
