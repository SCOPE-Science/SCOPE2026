# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof is a direct consequence of the 2026 classification of locally finite
Schreier varieties, followed by an affine-polynomial argument.

The classification gives two possible polynomial types. The \(G\)-set case is
excluded because every polynomial operation of a \(G\)-set is essentially unary or
constant, whereas vector addition on a nontrivial \(k\)-vector space depends on both
variables. In the remaining vector-space case, each basic operation is affine in the
polynomially equivalent vector-space coordinates. A \(k\)-multilinear operation of
arity at least two becomes constant whenever any coordinate is the original additive
zero; this forces every affine coefficient to vanish and the remaining constant to
be the additive zero. The zero-product converse reduces to the elementary fact that
subspaces of vector spaces are free.

Potential edge cases were checked explicitly in the proof: the additive zero of the
original \(k\)-vector space need not coincide with the origin of the polynomially
equivalent vector-space structure; the affine argument uses it merely as a fixed
point and remains valid. The presence of a distinguished unit is handled separately
and forces triviality after multiplication vanishes.

## Originality

The originality claim is narrow and to the best of our knowledge. Searches were made
for combinations of "Schreier variety", "locally finite", "finite field",
"linear algebra", "multilinear", and "zero multiplication", together with synonymous
Nielsen--Schreier terminology.

The closest older source found is Burgin (1974), which describes Schreier varieties
of linear \(\Omega\)-algebras over commutative rings subject to homogeneous
identities and, as a corollary, all such varieties over an infinite field. Lewin
(1968) likewise focuses on infinite fields. The recent Kearnes--Moorhead--Szendrei
classification is the essential new prior theorem that makes the finite-field
collapse immediate once the linear structure is exploited.

No located source stated the general finite-field conclusion that every higher-arity
multilinear basic operation must vanish in a nontrivial locally finite Schreier
variety, nor the exact consequence that the zero-product variety is the only
nontrivial one-product example. Because this specialization is short once the new
classification is available, independent or differently phrased prior observation
remains a material residual risk.

Burgin (1974) was the source most capable of overturning originality. Its available
bibliographic abstract and accessible description were inspected and explicitly
state the homogeneous-identity scope over commutative rings and the infinite-field
classification. The full older literature is not exhaustively searchable, so an
equivalent finite-field corollary under different terminology cannot be excluded.

## Value

The result turns an abstract universal-algebra classification into a sharp rigidity
theorem for a broad algebraic class. It simultaneously classifies all nontrivial
locally finite Schreier varieties with a single bilinear product over a finite field,
rules out the unital case, and applies to arbitrary (including nonhomogeneous)
identities. It also isolates the precise contrast with the many nonzero-product
Schreier varieties known outside the locally finite finite-field regime.
