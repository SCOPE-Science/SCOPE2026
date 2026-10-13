# Euler characteristic collapses the entire multilinear-rank filtration
## Finding
Let
\[
t\ge3,
\]
let \(A_i\) be complex vector spaces of dimensions
\[
a_i\ge2,
\]
and let
\[
\mathbf r=(r_1,\ldots,r_t),
\qquad
1\le r_i\le a_i.
\]
Write
\[
\operatorname{Sub}_{\mathbf r}
\subset
\mathbb P(A_1\otimes\cdots\otimes A_t)
\]
for the subspace variety of nonzero tensors whose mode-\(i\) flattening ranks are at most \(r_i\).

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\operatorname{Sub}_{\mathbf r}\right)
=
\prod_{i=1}^{t}a_i
}
\]
for every bound vector \(\mathbf r\).

Thus every nonempty member of the multilinear-rank filtration has exactly the same Euler characteristic as the full ambient projective tensor space.

Let
\[
E_{\mathbf s}
\]
be the locally closed locus of tensors of exact multilinear rank
\[
\mathbf s=(s_1,\ldots,s_t).
\]
Then
\[
\boxed{
\chi_c(E_{(1,\ldots,1)})
=
\prod_{i=1}^{t}a_i
}
\]
and, for every realizable
\[
\mathbf s\ne(1,\ldots,1),
\]
\[
\boxed{
\chi_c(E_{\mathbf s})=0.
}
\]

Hence compactly supported Euler characteristic is completely blind to every higher exact Tucker-rank layer.

## Assumptions and scope
The base field is \(\mathbb C\). The multilinear rank is the tuple of ranks of the mode flattenings.

The restriction
\[
t\ge3
\]
isolates genuine higher-order tensors. For two factors, multilinear rank reduces to ordinary matrix rank, and the corresponding rank-locus Euler constancy is the determinantal specialization.

A bound vector need not itself be realizable as an exact multilinear rank. The cumulative variety
\[
\operatorname{Sub}_{\mathbf r}
\]
is nevertheless nonempty because it contains all rank-one tensors.

The cumulative varieties are projective, so ordinary and compactly supported Euler characteristics agree there. The exact-rank strata are quasi-projective, so compactly supported Euler characteristic is the additive invariant used for them.

## Proof
Choose bases
\[
e_{i,0},\ldots,e_{i,a_i-1}
\]
of the spaces \(A_i\). Let
\[
B=\max_i a_i.
\]
Define a one-parameter subgroup by
\[
z\cdot e_{i,j}
=
z^{\,jB^{i-1}}e_{i,j}.
\]

The tensor-coordinate line indexed by
\[
(j_1,\ldots,j_t)
\]
has weight
\[
w(j_1,\ldots,j_t)
=
\sum_{i=1}^{t}j_iB^{i-1}.
\]
Since
\[
0\le j_i<B,
\]
base-\(B\) uniqueness shows that all tensor-coordinate weights are pairwise distinct. Hence the fixed locus on the ambient projective space consists exactly of the coordinate tensor lines
\[
[e_{1,j_1}\otimes\cdots\otimes e_{t,j_t}],
\]
of which there are
\[
N=\prod_{i=1}^{t}a_i.
\]

Every coordinate tensor has multilinear rank
\[
(1,\ldots,1),
\]
so every ambient fixed point lies in every
\[
\operatorname{Sub}_{\mathbf r}.
\]
Conversely, a fixed point of a subspace variety is fixed in the ambient projective space. Therefore
\[
\operatorname{Sub}_{\mathbf r}^{\mathbb C^*}
\]
is the same set of \(N\) coordinate points for every positive bound vector.

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
For completeness, remove the fixed locus and apply Rosenlicht's theorem together with Noetherian induction. After stratifying by stabilizer type, each nonfixed constructible piece admits a geometric quotient and is a locally trivial bundle with fiber
\[
\mathbb C^*/\mu_q\cong\mathbb C^*.
\]
Since
\[
\chi_c(\mathbb C^*)=0,
\]
every such piece contributes zero. Additivity leaves only the fixed locus.

Applying this to the projective variety
\[
\operatorname{Sub}_{\mathbf r}
\]
gives
\[
\chi_{\mathrm{top}}\!\left(\operatorname{Sub}_{\mathbf r}\right)
=
N.
\]

Now stratify by exact multilinear rank. Each rank condition is a condition on finitely many matrix flattenings, so
\[
E_{\mathbf s}
\]
is locally closed, and
\[
\operatorname{Sub}_{\mathbf r}
=
\bigsqcup_{\mathbf 1\le\mathbf s\le\mathbf r}E_{\mathbf s},
\]
with unrealizable strata interpreted as empty.

Set
\[
e(\mathbf s)=\chi_c(E_{\mathbf s}).
\]
Additivity gives
\[
N
=
\sum_{\mathbf 1\le\mathbf s\le\mathbf r}e(\mathbf s)
\]
for every positive bound vector \(\mathbf r\).

At
\[
\mathbf r=(1,\ldots,1)
\]
this says
\[
e(\mathbf 1)=N.
\]
Induct on
\[
s_1+\cdots+s_t.
\]
If
\[
\mathbf s\ne\mathbf 1,
\]
then every proper lower rank vector has already been treated. Among those lower strata, only \(\mathbf 1\) contributes \(N\). Hence
\[
N
=
N+e(\mathbf s),
\]
so
\[
e(\mathbf s)=0.
\]
This proves the exact-stratum statement.

## Verification
The bundled checker tests the finite combinatorics of the proof for every tensor format with
\[
3\le t\le5,
\qquad
2\le a_i\le4.
\]

For each format it constructs the displayed mixed-radix weights and verifies that every tensor coordinate has a distinct weight. It then enumerates every positive bound vector and reconstructs the exact-stratum Euler values from the cumulative identity
\[
\chi(\operatorname{Sub}_{\mathbf r})=N
\]
by finite poset subtraction.

In every tested format the unique nonzero exact-stratum value occurs at
\[
(1,\ldots,1)
\]
and equals \(N\).

These computations are regression evidence only. The all-format theorem follows from base-\(B\) uniqueness, algebraic \(\mathbb C^*\)-localization, and finite additivity of exact-rank strata.

## Relationship to prior work
Landsberg and Weyman introduce subspace varieties as auxiliary tensor varieties and study their defining ideals, normality, and rational singularities. Yang formulates multilinear rank through mode flattenings and explicitly identifies the same subspace varieties with bounded multilinear-rank loci. More recent work computes their projective degrees and emphasizes the role of multilinear rank in Tucker decomposition.

The result here concerns a different invariant. It shows that ordinary Euler characteristic does not merely admit a simple formula: it is constant on the entire positive multilinear-rank filtration. Additivity then forces every higher exact multilinear-rank stratum to have compactly supported Euler characteristic zero.

Targeted searches using subspace variety, bounded multilinear rank, Tucker rank, Euler characteristic, exact multilinear rank, and torus fixed points did not locate this cumulative-constancy or exact-stratum-vanishing theorem.

## Limitations
Euler characteristic is coarse. Vanishing of
\[
\chi_c(E_{\mathbf s})
\]
does not imply that an exact multilinear-rank stratum is empty or topologically simple.

The result concerns the ordinary projective subspace varieties associated with mode flattenings. Other hierarchical tensor formats and additional symmetry constraints may have different fixed loci.

The matrix specialization is already classical and is excluded from the claimed higher-order novelty.

The localization argument is short once the common coordinate fixed locus is noticed, so an unindexed observation in tensor or transformation-group literature remains a residual novelty risk.

## References
J. M. Landsberg and Jerzy Weyman, *On the ideals and singularities of secant varieties of Segre varieties*, arXiv:math/0601452, first submitted 18 January 2006; *Bulletin of the London Mathematical Society* 39 (2007), 685--697.

Ming Yang, *On partial and generic uniqueness of block term tensor decompositions*, arXiv:1301.0920, first submitted 5 January 2013; *Annali dell'Università di Ferrara* 60 (2014), 465--493, DOI 10.1007/s11565-013-0190-z.

Paul Breiding and Pierpaola Santarsiero, *Degree of the subspace variety*, arXiv:2402.12217, first submitted 19 February 2024.
