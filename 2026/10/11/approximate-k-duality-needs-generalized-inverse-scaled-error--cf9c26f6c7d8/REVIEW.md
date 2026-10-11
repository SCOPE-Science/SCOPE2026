# Review

## Correctness
PASS. The example on \(\mathbb R^2\) satisfies both approximate-duality inequalities with error \(1/2\), while
\[
K^\dagger T_FR_G=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\]
is singular. The same data directly violate the lower \(K\)-frame inequality on \(e_2\).

The repaired condition follows independently from
\[
I-K^\dagger T_FR_G
=
K^\dagger(K-T_FR_G)
\]
and the Neumann lemma. Injectivity of \(K\) plus the generalized-inverse identity gives \(K^\dagger K=I\), so no extra inverse identity is being assumed.

## Originality
PASS. Exact-source searches, theorem-number searches, generalized-inverse aliases, approximate-duality formulations, and erratum searches were compared. No indexed correction of Lemma 19 or Proposition 20 was located.

The closest frame-theoretic results concern range compression, perturbation smallness in other frame models, diagonal scaling, projected excess, and a different dual-frame criterion. None implies this generalized-inverse conditioning obstruction. The target full text was materially inspected.

## Value
PASS. Approximate \((K,K^*)\)-duality is introduced to provide stable near-reconstruction. The source's unscaled error threshold can nevertheless make its normalized reconstruction singular and can fail to produce a \(K\)-frame at all. The corrected dimensionless error
\[
\|K^\dagger\|\,\|K-T_FR_G\|
\]
is the natural perturbation quantity and yields a direct, reusable repair.

## Limitations
The norm-product condition is a sharp universal Neumann-type sufficient threshold, not a necessary condition for every individual pair. The review does not assess downstream statements as separate claims. An unindexed correction remains a literature risk.

Same-model review: passed. Independent audit: not yet performed.
