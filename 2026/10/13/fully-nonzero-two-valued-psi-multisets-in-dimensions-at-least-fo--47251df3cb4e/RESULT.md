# Fully nonzero two-valued PSI multisets in dimensions at least four have a unique exceptional entry
## Finding
Let \(n\ge4\), and let \(r,s\in\mathbb Z\setminus\{0\}\) be distinct. Consider a multiset of \(n^2\) integers that takes exactly the two values \(r\) and \(s\). It is permutation-spectrally integral if and only if, after interchanging \(r\) and \(s\) if necessary, it has the form
\[
\{r^{[n^2-1]},s\}
\]
and, with \(t=s/r\), both
\[
(t-(n-1))^2+4(n-1),\qquad 4t+n^2-4
\]
are squares in \(\mathbb Q\).

Equivalently, every fully nonzero nonconstant two-valued permutation-spectrally integral multiset in dimension at least \(4\) has exactly one exceptional entry.

## Assumptions and scope
A multiset of \(n^2\) integer entries is permutation-spectrally integral (PSI) if every \(n\times n\) arrangement of those entries has only integer eigenvalues. The result concerns exactly two distinct nonzero entry values and dimensions \(n\ge4\).

The one-exception sufficiency and necessity are those of Cheng--Zhang Theorem 5.2. Their Theorem 5.4 excludes exactly two equal deviations from a nonzero background. The new step is a uniform obstruction for every larger multiplicity, including the balanced \(4\times4\) case.

## Proof
Write the multiset as
\[
\mathcal S=\{r^{[n^2-m]},s^{[m]}\},
\]
where, after swapping the names of the two values if necessary,
\[
1\le m\le\left\lfloor\frac{n^2}2\right\rfloor.
\]
Put \(\delta=s-r\ne0\). Every arrangement can be written as \(rJ_n+\delta C\), where \(J_n\) is the all-ones matrix and \(C\) is a zero-one matrix with exactly \(m\) ones.

If \(m=1\), Cheng--Zhang Theorem 5.2 gives exactly the two rational-square conditions stated above. If \(m=2\), their Theorem 5.4 says that \(\{r^{[n^2-2]},s^{[2]}\}\) is PSI only when \(r=0\) or \(s=r\), both excluded by the hypotheses.

Assume \(m\ge3\). First take \(n\ge5\). Let
\[
C_0=E_{12}+E_{23}+E_{31}.
\]
Place the remaining \(m-3\) ones of \(C\) anywhere in columns \(4,\ldots,n\). There is enough room because
\[
n(n-3)+3-\frac{n^2}2=\frac{(n-3)^2-3}2>0
\]
for \(n\ge5\), hence
\[
m-3\le n(n-3).
\]
Let \(\omega\) be a primitive cube root of unity and set
\[
v=(1,\omega,\omega^2,0,\ldots,0)^{\mathsf T}.
\]
Then \(J_nv=0\). The added ones in columns \(4,\ldots,n\) also annihilate \(v\), while
\[
C_0v=\omega v.
\]
Consequently
\[
(rJ_n+\delta C)v=\delta\omega v.
\]
Since \(\delta\ne0\), the eigenvalue \(\delta\omega\) is nonreal, so this arrangement does not have integral spectrum. Thus no \(m\ge3\) can be PSI when \(n\ge5\).

For \(n=4\), the same construction works for \(3\le m\le7\), because the fourth column supplies four additional positions. The only remaining case is \(m=8\). Take
\[
C=\begin{pmatrix}
1&1&1&1\\
1&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix}
\]
and
\[
v=(0,\omega^2,\omega,1)^{\mathsf T}.
\]
Again \(J_4v=0\), while direct multiplication gives
\[
Cv=\omega^2v.
\]
Hence \(rJ_4+\delta C\) has the nonreal eigenvalue \(\delta\omega^2\), excluding the balanced case as well.

This exhausts all multiplicities. Therefore a fully nonzero nonconstant two-valued PSI multiset in dimension \(n\ge4\) must have minority multiplicity \(1\), and Cheng--Zhang Theorem 5.2 gives the displayed criterion.

## Verification
The proof is symbolic and covers every \(n\ge4\). A standalone checker `check_binary_psi.py` verifies the exact cube-root arithmetic for the directed-cycle obstruction and the special balanced \(4\times4\) matrix, and checks the packing inequality over a large finite range. It terminates with `CHECK_OK`.

The finite checks are only consistency checks. The infinite statement follows from the inequalities and exact eigenvector calculations in the proof.

## Relationship to prior work
Cheng and Zhang introduce the PSI problem in arbitrary dimension. Their Theorem 5.2 completely handles one exceptional entry over a nonzero constant background, and Theorem 5.4 proves that two equal exceptional entries cannot occur in the fully nonzero nonconstant case. Their Section 5 then turns to two distinct deviations and dimension three; it does not classify arbitrary multiplicities of a two-valued fully nonzero multiset. The present result closes all multiplicities for the natural two-valued family in every dimension \(n\ge4\).

Hall's earlier paper develops the motivating \(2\times2\) Pythagorean constructions. It does not imply the higher-dimensional two-valued classification here.

## Limitations
The theorem does not treat \(n=3\), where the motivating paper explicitly leaves the general fully nonzero problem open, nor does it classify multisets with three or more distinct entry values. It also does not solve the Diophantine square conditions in Cheng--Zhang Theorem 5.2 beyond using their exact criterion.

The originality comparison is bounded by the inspected primary papers and targeted searches. Because the motivating preprint is very recent, an unindexed contemporaneous observation could exist.

## References
1. S. Cheng and S. Zhang, “Square matrices with integer eigenvalues under entry permutations,” arXiv:2609.36524v1, 2026. See Proposition 5.1, Theorems 5.2 and 5.4, Proposition 5.5, and Section 6.
2. M. J. W. Hall, “Matrices with integer eigenvalues for all permutations of coefficients (thanks to Pythagoras!),” arXiv:2601.01083v1, 2026.
