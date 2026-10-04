# Full box dimension for higher effective genericity despite zero Hausdorff dimension
## Finding

Fix
\[
n\ge2
\]
and an oracle
\[
A\subseteq\mathbb N.
\]

Work in Cantor space
\[
2^{\mathbb N}
\]
with Lebesgue measure and the standard ultrametric
\[
d(x,y)=2^{-\min\{i:x_i\ne y_i\}}.
\]

Let
\[
G_n^A
\]
be the set of \(\Pi^0_n\)-generic points relative to \(A\) in the sense of Veltri, and let
\[
W_n^A
\]
be the corresponding weakly \(\Pi^0_n\)-generic set.

Then both sets are dense in Cantor space.

In fact, if
\[
N_k(S)
\]
denotes the minimum number of subsets of diameter at most
\[
2^{-k}
\]
needed to cover a set \(S\subseteq2^{\mathbb N}\), then for every integer
\[
k\ge0
\]
we have the exact identities
\[
\boxed{N_k(G_n^A)=N_k(W_n^A)=2^k.}
\]

Therefore
\[
\boxed{
\underline{\dim}_B(G_n^A)
=
\overline{\dim}_B(G_n^A)
=
\underline{\dim}_B(W_n^A)
=
\overline{\dim}_B(W_n^A)
=
1.
}
\]

Veltri proves that
\[
\dim_H(W_n^A)=0
\]
for every
\[
n\ge2.
\]
Since
\[
G_n^A\subseteq W_n^A,
\]
the same Hausdorff-dimension conclusion holds for \(G_n^A\).

Thus both higher effective-genericity classes have the extremal fractal-dimension profile
\[
\boxed{
\dim_H=0
\qquad\text{but}\qquad
\underline{\dim}_B=\overline{\dim}_B=1.
}
\]

This gives a quantitative affirmative answer to Question 3.28 of the source, which asks whether these classes are large in any meaningful sense other than cardinality.

## Assumptions and scope

The notions of \(\Pi^0_n\)-genericity and weak \(\Pi^0_n\)-genericity are exactly those introduced in the source.

For
\[
n\ge2,
\]
a \(\Pi^0_n\)-generic point relative to \(A\) has the following local property: whenever it belongs to a \(\Pi^0_n(A)\) set, that set contains around the point a positive-measure
\[
\Pi^0_1(A^{(n-2)})
\]
subset.

The proof uses the source's forcing construction over positive-measure
\[
\Pi^0_1(A^{(n-2)})
\]
conditions.

The box-counting dimensions are the standard lower and upper Minkowski dimensions computed using covering numbers in the displayed Cantor ultrametric.

The theorem concerns classical set dimensions of the entire genericity classes. It does not claim that individual generic reals have effective Hausdorff or effective packing dimension \(1\).

## Proof

### Density

Fix a finite binary string
\[
\sigma\in2^{<\mathbb N}.
\]

Its cylinder
\[
[\sigma]
=
\{x\in2^{\mathbb N}:\sigma\prec x\}
\]
is compact, is a computable
\[
\Pi^0_1
\]
set, and has positive Lebesgue measure
\[
2^{-|\sigma|}.
\]

Veltri's Lemma 3.18 defines the forcing partial order of positive-measure
\[
\Pi^0_1(A^{(n-2)})
\]
sets and proves that, for every \(\Pi^0_n(A)\) set \(P\), the collection of conditions deciding \(P\) is dense.

The proof of Corollary 3.19 then meets the countably many dense decision requirements by a nested sequence of closed positive-measure conditions below an initial compact positive-measure condition.

Nothing in that argument requires the initial condition to be chosen independently of \(\sigma\). We may take the initial compact condition to be
\[
[\sigma].
\]

The nested construction therefore produces a point
\[
x\in[\sigma]
\]
which is \(\Pi^0_n\)-generic relative to \(A\).

Since \(\sigma\) was arbitrary, every basic cylinder meets
\[
G_n^A.
\]
Hence \(G_n^A\) is dense.

Every \(\Pi^0_n\)-generic point is weakly \(\Pi^0_n\)-generic, so
\[
G_n^A\subseteq W_n^A.
\]
Therefore \(W_n^A\) is dense as well.

### Exact covering numbers

Fix
\[
k\ge0.
\]

The \(2^k\) cylinders
\[
[\tau],
\qquad
\tau\in2^k,
\]
partition Cantor space, and every such cylinder has diameter
\[
2^{-k}.
\]

They therefore give a cover of either genericity class by \(2^k\) sets of diameter at most \(2^{-k}\). Thus
\[
N_k(G_n^A)\le2^k,
\qquad
N_k(W_n^A)\le2^k.
\]

For the reverse inequality, density implies that each length-\(k\) cylinder contains at least one point of each class.

A set of diameter at most
\[
2^{-k}
\]
cannot meet two distinct length-\(k\) cylinders. Indeed, two points lying in different length-\(k\) cylinders disagree before coordinate \(k\), so their distance is strictly larger than
\[
2^{-k}.
\]

Hence every diameter-\(2^{-k}\) cover of either class needs at least one member for each of the \(2^k\) cylinders.

Therefore
\[
N_k(G_n^A)\ge2^k,
\qquad
N_k(W_n^A)\ge2^k.
\]

Combining the two inequalities gives
\[
N_k(G_n^A)=N_k(W_n^A)=2^k.
\]

### Box dimension

At the dyadic scales
\[
\varepsilon_k=2^{-k},
\]
we have
\[
\frac{\log N_k(G_n^A)}{-\log\varepsilon_k}
=
\frac{\log 2^k}{\log 2^k}
=
1,
\]
and identically for \(W_n^A\).

Monotonicity of covering numbers between consecutive dyadic scales gives the same limit inferior and limit superior over arbitrary
\[
\varepsilon\downarrow0.
\]

Thus both lower and upper box dimensions are \(1\).

### Contrast with Hausdorff dimension

Veltri's Corollary 3.24 proves
\[
\dim_H(W_n^A)=0.
\]

Since
\[
G_n^A\subseteq W_n^A,
\]
monotonicity of Hausdorff dimension gives
\[
\dim_H(G_n^A)=0.
\]

This proves the claimed Hausdorff/box-dimension separation.

## Verification

The argument was checked directly against the source's definitions, Lemma 3.18, Corollary 3.19, Theorem 3.20, Corollary 3.24, and Question 3.28.

The critical logical steps are:

1. every basic cylinder is a compact positive-measure computable closed set, so it may serve as the initial condition in the source's dense-set construction;
2. the construction therefore yields a \(\Pi^0_n\)-generic point in every cylinder;
3. \(\Pi^0_n\)-genericity implies weak \(\Pi^0_n\)-genericity;
4. at scale \(2^{-k}\), density forces a point in every one of the \(2^k\) length-\(k\) cylinders;
5. the ultrametric prevents one set of diameter at most \(2^{-k}\) from meeting two such cylinders;
6. the cylinders themselves give a matching \(2^k\)-set cover.

No finite experiment is used to infer the arbitrary-\(n\), arbitrary-\(A\), or arbitrary-scale claims.

## Relationship to prior work

Veltri introduces \(\Pi^0_n\)-genericity in the context of effective recurrence. For
\[
n\ge2,
\]
the paper proves existence and continuum cardinality of \(\Pi^0_n\)-generic points and proves that the weakly \(\Pi^0_n\)-generic class has Hausdorff dimension zero.

Immediately afterward, the source emphasizes the apparent smallness of these classes: they are meager, null, and Hausdorff-dimension zero. It states that cardinality appears to be their only large feature and asks in Question 3.28 whether there are meaningful senses other than cardinality in which the classes are large.

The source does not discuss box-counting or Minkowski dimension. The present observation localizes its forcing construction to every basic cylinder and then uses the exact dyadic geometry of Cantor space. This yields full box dimension for both the generic and weakly generic classes.

The contrast is maximal:
\[
\dim_H=0
\]
while both box dimensions equal the ambient value \(1\).

Standard fractal-geometry references explain that Hausdorff and box-counting dimensions can differ and that box dimension is controlled by covering numbers. The exact covering-number identity here depends on the effective-genericity density supplied by the source and the cylinder geometry of Cantor space.

Targeted searches for \(\Pi^0_n\)-genericity together with box-counting, Minkowski dimension, or the source's Question 3.28 did not locate this conclusion.

## Limitations

Box-counting dimension is closure-sensitive: every dense subset of Cantor space has full box dimension. The substantive input here is therefore the previously unstated density of the higher effective-genericity classes, obtained by localizing the source's forcing construction.

The result does not contradict the source's Hausdorff-dimension-zero theorem, because box-counting dimension can be strictly larger than Hausdorff dimension for nonclosed sets.

No packing-dimension, Assouad-dimension, effective-dimension, or category-strengthening claim is made.

The result is specific to Cantor space with its standard ultrametric and Lebesgue measure as stated. Analogous conclusions on other computable probability spaces require geometric hypotheses ensuring suitable positive-measure local conditions and control of covering numbers.

## References

[1] Joey Veltri, “Effective recurrence for computable measure-preserving transformations,” arXiv:2609.12402, first posted 11 September 2026.

[2] Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, third edition, Wiley, 2014.
