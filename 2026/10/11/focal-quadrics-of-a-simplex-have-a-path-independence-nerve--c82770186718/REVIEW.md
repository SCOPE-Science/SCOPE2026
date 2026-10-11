# Same-model review

## Correctness

PASS. The primary source's focal-set/repeated-eigenvalue theorem was checked directly. Necessity follows from Cauchy interlacing: a repeat at \(d_k\) occupies \(\mu_{k-1}=\mu_k=d_k\), so adjacent focal indices cannot occur together. Sufficiency is constructive. Every nonconsecutive index set is encoded by an interlacing target spectrum; the nonnegative residues
\[
\frac{p_\mu(d_i)}{p_D'(d_i)}
\]
produce a real rank-one vector, and the determinant lemma recovers the target characteristic polynomial. The complementary-block nullity argument shows every repeat is exactly double. The four-dimensional example is verified exactly.

## Originality

PASS. The focal paper treats the focal quadrics individually and identifies their union with the repeated-eigenvalue locus; it does not classify simultaneous intersections. General rank-one perturbation theory covers multiplicity and inverse-spectral background but not the simplex focal incidence complex. Targeted searches under intersection, nonconsecutive, nerve, path-independence, and source-specific formulations found no statement implying the complete classification. The claimed novelty is the focal-incidence theorem, not the standard multiplicity-two fact.

## Value

PASS. This is a complete classification of a natural structure left undescribed by the new focal-set construction. It identifies the entire nerve with
\[
\operatorname{Ind}(P_{n-1}),
\]
gives the exact maximal simultaneous degeneracy
\[
\left\lfloor\frac n2\right\rfloor,
\]
and counts all indexed \(r\)-fold intersections by
\[
\binom{n-r}{r}.
\]
The source's four-dimensional example gains an explicit four-point double-degeneracy locus.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Anatoly Eydelzon, arXiv:2609.37448v1, which supplies the focal equations and individual repeated-eigenvalue characterization. Dobosevych--Hryniv provide broader rank-one perturbation theory but no focal-geometry incidence result.

The theorem requires pairwise distinct semiaxes and classifies incidence rather than the topology of every higher intersection. Classical confocal-quadric literature under different terminology remains a residual bibliographic risk.
