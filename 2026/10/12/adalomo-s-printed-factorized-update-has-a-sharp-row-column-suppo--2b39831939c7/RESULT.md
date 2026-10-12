# AdaLomo's printed factorized update has a sharp row–column support singularity
## Finding

Consider the matrix branch of printed AdaLomo Algorithm 1 at its first optimization step. Let
\[
G\in\mathbb R^{m\times n}
\]
be the first gradient matrix, let
\[
0\le\beta<1,
\]
and initialize the factorized second-moment states at zero.

Define the row and column gradient energies
\[
R_i=\sum_{j=1}^{n}G_{ij}^2,
\qquad
C_j=\sum_{i=1}^{m}G_{ij}^2.
\]

The original public AdaLomo version forms row and column states proportional to these energies and then forms their outer product. The current paper version additionally divides that outer product by the total row mass. In both versions the support of the printed factorized second moment is identical.

For the current normalized formula and any nonzero \(G\),
\[
r_i=(1-\beta)R_i,
\qquad
c_j=(1-\beta)C_j,
\qquad
\mathbf 1^\top r=(1-\beta)\|G\|_F^2,
\]
so
\[
\boxed{
V_{ij}
=
(1-\beta)
\frac{R_iC_j}{\|G\|_F^2}.
}
\]
The original version differs only by a positive global factor and therefore has the same zero pattern.

The printed AdaLomo raw update is
\[
U_{ij}=\frac{G_{ij}}{V_{ij}}.
\]
Consequently,
\[
\boxed{
U\text{ is finite entrywise}
\iff
G\text{ has no zero row and no zero column}.
}
\]

This is a sharp support criterion. If row \(i\) is identically zero, then
\[
R_i=0,
\]
so
\[
V_{ij}=0
\]
for every column \(j\), while also
\[
G_{ij}=0.
\]
Every entry of that printed update row is therefore the undefined quotient
\[
0/0.
\]
The same argument applies to a zero column. Conversely, if every row and every column contains a nonzero gradient entry, then all \(R_i\) and \(C_j\) are positive, hence every \(V_{ij}>0\), and the raw update is finite.

The all-zero gradient is also undefined in the printed rule: in the current normalized formula the factorization itself has zero total mass, and in the original formula the subsequent division still gives \(0/0\).

Grouped update normalization does not repair this boundary. It is applied only after the raw matrix \(U\) has already been formed, so an undefined row or column propagates into its RMS normalization.

A two-by-two strongly convex witness makes the obstruction independent of any nonconvex neural-network pathology. Let
\[
F(W)=\frac12\|W-B\|_F^2
\]
with arbitrary fixed \(B\), and choose
\[
W_0-B
=
\begin{pmatrix}
0&0\\
1&-1
\end{pmatrix}.
\]
Then \(F\) is \(1\)-strongly convex and
\[
\nabla F(W_0)
=
\begin{pmatrix}
0&0\\
1&-1
\end{pmatrix}
\ne0.
\]
Both columns carry gradient energy, but the first row does not. The printed first AdaLomo update is therefore undefined on the entire first row even though the point is not stationary.

This boundary is directly relevant to the paper's stated motivation that second-moment adaptation is effective for sparse data: sparsity can create exactly zero gradient rows or columns without making the full gradient zero.

The singularity is not intrinsic to factorized second moments. The cited Adafactor rule uses
\[
G/(\sqrt V+\epsilon),
\]
so, whenever the total gradient is nonzero, a zero row has \(V=0\) there but still receives the finite zero update. The current first-party AdaLomo implementation likewise avoids the printed support singularity: it adds a strictly positive floor to squared gradients before constructing row and column accumulators and applies an inverse-square-root factorization.

## Assumptions and scope

The claim concerns the mathematical update printed in AdaLomo Algorithm 1, not every software implementation bearing the same name.

The factor states are initialized at zero, matching the first-party implementation and the standard exponential-moving-average initialization used by the surrounding adaptive-optimizer literature.

The sharp criterion is a first-step statement. Later steps can retain positive row or column state from earlier gradients, so the instantaneous support of a later gradient alone does not determine well-definedness.

The matrix gradient may be deterministic. No stochasticity, nonconvexity, or finite-precision effect is used.

The current paper revision normalizes the factorized matrix by total row mass; the original public revision did not. The zero-pattern argument is unchanged by this revision.

## Proof

At the first step, zero state initialization gives
\[
r=(1-\beta)G^{\odot2}\mathbf1,
\qquad
c=(1-\beta)\mathbf1^\top G^{\odot2}.
\]
Thus
\[
r_i=(1-\beta)R_i,
\qquad
c_j=(1-\beta)C_j.
\]

For the current paper formula,
\[
V=\frac{rc}{\mathbf1^\top r}.
\]
If \(G\ne0\), then
\[
\mathbf1^\top r=(1-\beta)\|G\|_F^2>0,
\]
and the displayed expression for \(V_{ij}\) follows.

Suppose row \(i\) is zero. Then \(R_i=0\), hence \(V_{ij}=0\) for all \(j\). Because the row itself is zero, \(G_{ij}=0\) for all \(j\), so the printed quotient \(G_{ij}/V_{ij}\) is \(0/0\). A zero column is identical with indices exchanged.

Conversely, suppose every row and every column contains a nonzero entry. Then
\[
R_i>0
\]
for all rows and
\[
C_j>0
\]
for all columns. Therefore every factorized entry satisfies
\[
V_{ij}>0,
\]
and the raw quotient is finite, including at individual entries where \(G_{ij}=0\).

The original public formula forms the unnormalized outer product of the same positive row and column states. Multiplication by or omission of a positive global normalization cannot alter which entries of \(V\) vanish, so the same support criterion holds there.

The strongly convex witness is immediate from
\[
\nabla F(W)=W-B.
\]
Its first gradient has one zero row and two nonzero columns, so the criterion applies.

Finally, the grouped normalization in the printed algorithm depends on \(\operatorname{RMS}(U)\) and is evaluated after \(U=G/V\). It therefore cannot define an entry that was already \(0/0\).

## Verification

The accompanying `verify.py` exhaustively enumerates all two-by-three gradient matrices with entries in \(\{-1,0,1\}\). For each nonzero matrix it checks that the current normalized printed formula is finite exactly when there is no zero row and no zero column, and it repeats the same support test for the original unnormalized outer product.

The script separately evaluates the two-by-two strongly convex witness and confirms that the zero row produces nonfinite printed raw-update entries while the full gradient remains nonzero.

It also checks two comparison rules: an Adafactor-style denominator \(\sqrt V+\epsilon\) gives a finite zero update on the zero row, and a positive squared-gradient floor of the form used by the current first-party AdaLomo implementation makes every row and column accumulator positive.

The finite enumeration is a transcription check. The all-dimensional support classification is proved algebraically above.

## Relationship to prior work

AdaLomo introduces factorized second-moment adaptation and grouped update normalization for memory-efficient large-model training. Both the original public version and the current paper version print the raw update as elementwise division by the factorized second-moment estimate. The current version changes the global normalization of that estimate but leaves the row–column support structure unchanged.

The AdaLomo paper explicitly motivates second-moment adaptation in part by its effectiveness on sparse data. The sharp support criterion identifies a boundary of the printed rule precisely in that sparse regime: a single completely inactive row or column makes the raw update undefined there even when other entries have nonzero gradient.

Adafactor is the closest structural predecessor. It uses the same row/column factorization idea, but its adaptive step divides by \(\sqrt V+\epsilon\). Therefore a zero row or column with nonzero total gradient yields a finite zero update rather than \(0/0\). The support singularity is not a generic consequence of low-rank factorization.

The current first-party AdaLomo implementation is also materially different from the printed formula. It adds a positive constant to squared gradients before accumulating row and column statistics, constructs inverse-square-root factors, and only then applies update clipping and parameter-scale normalization. Those safeguards make the exact zero-support obstruction inapplicable to that implementation.

Focused searches for AdaLomo together with zero rows, zero columns, sparse-gradient support, division by zero, factorized second moments, and grouped update normalization did not identify a published implication-equivalent support classification.

## Limitations

This is a mathematical boundary result for the printed algorithm. It is not a claim that the maintained first-party implementation produces nonfinite updates on sparse gradients.

The result does not quantify behavior when row or column energies are merely small but nonzero.

The support criterion is exact only for the first step from zero factor states. Positive historical state can regularize later zero-support gradients.

Because the maintained implementation already contains a positive squared-gradient floor and an inverse-square-root preconditioner, the practical value of the result is primarily interpretive: it distinguishes the literal paper recurrence from the safeguarded implementation and gives the exact support condition required by any analysis that uses the printed recurrence.

## References

1. Kai Lv, Hang Yan, Qipeng Guo, Haijun Lv, and Xipeng Qiu, “AdaLomo: Low-memory Optimization with Adaptive Learning Rate,” arXiv:2310.10195v1, first submitted 2023-10-16; current revision arXiv:2310.10195v3.
2. Noam Shazeer and Mitchell Stern, “Adafactor: Adaptive Learning Rates with Sublinear Memory Cost,” arXiv:1804.04235v1, first submitted 2018-04-11.
3. OpenLMLab, first-party AdaLomo implementation, `lomo_optim/adalomo.py`.
