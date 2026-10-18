# Exact dyadic-residue spectra for contiguous-block Walsh sketches

## Finding
Consider the globally transformed, contiguous-block subsampled randomized Hadamard transform. Its Gram matrix on **every coordinate subspace** decomposes exactly by the low-order binary labels of its coordinates. This gives a complete classification of coordinate subspaces preserved isometrically for *every* possible sequence of sampled blocks, and an exact finite-sample spectral distribution on every coordinate two-plane.

Let \(d\ge2\), \(1\le s<d\), \(N=2^d\), \(\tau=2^s\), and \(K=N/\tau\). Index rows and columns of the normalized Sylvester-Hadamard matrix by binary vectors, so that
\[
H_{r,a}=N^{-1/2}(-1)^{\langle r,a\rangle_2},\qquad 0\le r,a<N.
\]
For an arbitrary diagonal signature \(D=\operatorname{diag}(\epsilon_a)\), with \(\epsilon_a\in\{-1,1\}\), draw \(q\) blocks independently and uniformly **with replacement**, with \(1\le q\le K\). Block \(k\) consists of the consecutive rows \(k\tau,\ldots,(k+1)\tau-1\). Let \(R_{\boldsymbol{k}}\) stack all rows of sampled blocks \(k_1,\ldots,k_q\), retaining repetitions, and put
\[
T=\sqrt{K/q}\,R_{\boldsymbol{k}}HD.
\]
For a nonempty coordinate set \(S\subseteq\{0,\ldots,N-1\}\), let \(U_S\) consist of the corresponding standard coordinate columns. Write each frequency uniquely as \(a=v_a\tau+w_a\), where \(0\le v_a<K\) and \(0\le w_a<\tau\). Its sketched Gram matrix \(G_S=U_S^{\mathsf T}T^{\mathsf T}TU_S\) satisfies the **exact identity**
\[
(G_S)_{a b}=
\mathbf 1_{\{w_a=w_b\}}\,\epsilon_a\epsilon_b\,
\frac1q\sum_{j=1}^q(-1)^{\langle k_j,v_a\oplus v_b\rangle_2},
\qquad a,b\in S. \tag{1}
\]
Thus \(G_S\) is block diagonal after grouping coordinates by their residues \(w_a\), and the block associated with a residue represented \(m_w\) times has rank at most \(\min(q,m_w)\). In particular,
\[
G_S=I_{|S|}\text{ for every sampled block sequence}\quad\Longleftrightarrow\quad
\text{the residues }\{w_a:a\in S\}\text{ are pairwise distinct}. \tag{2}
\]
For each \(1\le m\le\tau\), the exact number of \(m\)-coordinate subspaces satisfying (2) is \(\binom{\tau}{m}K^m\); it is zero for \(m>\tau\). Nevertheless **every** transformed coordinate subspace with \(|S|=m\) has identical block Frobenius leverage masses \(\|(HDU_S)_{\mathcal B_k}\|_F^2=m/K\) for every \(k\), regardless of whether (2) holds.

For every two-element set \(S=\{a,b\}\), the spectral defect \(\Delta=\|G_S-I_2\|_2\) has the exact dichotomy
\[
\Delta=0\quad\text{almost surely if }w_a\ne w_b;
\qquad
\Delta\ \overset{\mathrm d}=\ \frac{|2B-q|}{q},\quad B\sim\operatorname{Binomial}(q,1/2),
\quad\text{if }w_a=w_b. \tag{3}
\]
In the latter case the two Gram eigenvalues are \(1\pm\Delta\), and
\[
\Pr\{\operatorname{rank}(TU_S)<2\}=2^{1-q}. \tag{4}
\]
Exactly \(\tau\binom K2\) coordinate pairs have the second, potentially singular law; all other \(\binom N2-\tau\binom K2\) pairs are exactly isometric for every draw. The laws are independent of the realization of \(D\).

## Assumptions and scope
The transform is **one global** normalized Sylvester-Hadamard matrix multiplied on the right by a sign diagonal, followed by uniform sampling of complete **contiguous dyadic row blocks** with replacement and the exact \(\sqrt{K/q}\) normalization. The same sampled block is allowed to recur. This is the unpermuted block-SRHT construction of Charalambides, Mahdavifar, Pilanci, and Hero (arXiv:2201.08522, Algorithm 1 and Section IV), for a specific lawful equal-size partition. The statement concerns exact real arithmetic, canonical binary row ordering, and coordinate subspaces; \(D\) need not be random.

No rank guarantee is asserted for arbitrary non-coordinate subspaces. The random variable \(B\) in (3) describes randomness of the sampled **block indices**, not a conditional distribution over \(D\). The rank-failure law (4) requires independent sampling with replacement. Random row permutations, non-dyadic partitions, and locally constructed block-Hadamard sketches define different objects.

## Proof
Write a row index as \(r=k\tau+u\) and a frequency as \(a=v\tau+w\), where \(k,v\in\{0,\ldots,K-1\}\) and \(u,w\in\{0,\ldots,\tau-1\}\). In binary coordinates the Sylvester character splits:
\[
(-1)^{\langle r,a\rangle_2}=(-1)^{\langle k,v\rangle_2}(-1)^{\langle u,w\rangle_2}.
\]
For two columns \(a,b\), directly expand their contribution to \(G_S\). The \(j\)-th sampled block contributes
\[
\frac{K}{qN}\epsilon_a\epsilon_b
(-1)^{\langle k_j,v_a\oplus v_b\rangle_2}
\sum_{u=0}^{\tau-1}(-1)^{\langle u,w_a\oplus w_b\rangle_2}.
\]
Orthogonality of the complete \(s\)-bit Walsh character system makes this last sum equal to \(\tau\) if \(w_a=w_b\), and zero otherwise. Since \(K\tau=N\), summing the \(q\) blocks proves (1). When \(a=b\), each term equals one, so the Gram diagonal is exactly one.

For any fixed low-bit residue \(w\), its Gram block is a sum of \(q\) rank-one matrices \(q^{-1}z_jz_j^{\mathsf T}\), where \((z_j)_a=\epsilon_a(-1)^{\langle k_j,v_a\rangle_2}\) for \(a\in S\) with \(w_a=w\). This proves the rank bound. If each residue occurs once, all off-diagonal Gram entries vanish and each diagonal entry is one, proving the forward statement of (2). Conversely, if a residue occurs for distinct \(a,b\), choose any one block index and repeat it \(q\) times; (1) then gives \(|(G_S)_{ab}|=1\), so \(G_S\ne I\). This proves (2), including its universal quantifier. To count the isometric supports of cardinality \(m\), select \(m\) of the \(\tau\) residues and one of the \(K\) high-bit labels for each selected residue. That gives exactly \(\binom{\tau}{m}K^m\). The constant block Frobenius mass follows because every entry of \(HDU_S\) has squared magnitude \(1/N\), and a block has \(\tau m\) such entries.

If \(a\ne b\) but \(w_a=w_b\), then \(v_a\oplus v_b\ne0\). The map \(k\mapsto(-1)^{\langle k,v_a\oplus v_b\rangle_2}\) takes each sign equally often among the \(K\) possible blocks. Its evaluations at independently sampled \(k_j\) are therefore independent fair signs. Formula (1) makes the off-diagonal Gram entry a fixed overall sign times their average; its diagonal entries are one. The Gram eigenvalues are \(1\pm\left|q^{-1}\sum_jX_j\right|\), so \(\Delta=\left|q^{-1}\sum_jX_j\right|\). Expressing the sign sum as \(2B-q\) proves (3). A two-by-two Gram matrix of this form loses rank exactly when all \(q\) signs agree; this has probability \(2(1/2)^q\), proving (4). If the low-bit residues differ, (1) gives the identity Gram instead. Finally, for each of the \(\tau\) low-bit residues there are \(K\) column indices, hence \(\binom K2\) pairs with equal residue, proving the pair count. A change of signs \(D\) only conjugates the Gram by an invertible diagonal sign matrix, leaving all claimed spectral facts unchanged.

## Verification
The attached standard-library script `check.py` evaluates the direct Walsh Gram numerator and the closed form (1), using only integers and exhaustive sampled block tuples, for \(d\in\{3,4\}\), every allowed \(s\), all coordinate pairs, \(q\in\{1,2,3\}\), and both relative signature signs. It also independently checks the exact count in (2) for coordinate supports and the rank-loss frequency in (4). The successful finite replay covers 169168 Gram comparisons and 25 support-count checks. Run `python3 check.py` from this package to reproduce it. The all-dimension theorem is proved by character orthogonality above; finite enumeration is only a cross-check.

## Relationship to prior work
Charalambides, Mahdavifar, Pilanci, and Hero's 2022 block-SRHT samples complete transformed row blocks and proves a high-probability subspace-embedding bound (Theorem 7). Its later expanded treatment (arXiv:2308.04185, Section IV, Theorem 3, and associated proof) again controls embedding error by leverage-score flattening and concentration, not the exact residue-dependent Gram law (1), the all-support characterization (2), or the binomial rank-loss law (4). The present exact finite-sample statement is not by itself an assessment of the quantitative constants or regimes of those sufficient-probability bounds: it classifies supports that can behave differently even though their block Frobenius leverage scores are identical.

Balabanov, Beaupère, Grigori, and Lederer's 2023 block-SRHT uses a different matrix constructed from separately signed **local** Hadamard sketches summed across processors (their equation (4)); its oblivious embedding theorem does not apply to the present global-Hadamard, full-block-sampling Gram identity. A published exact two-character **cyclic** harmonic-frame erasure theorem gives spectral bounds for cyclic Fourier sampling with fixed-cardinality erasure masks. This model is neither the noncyclic Boolean Walsh character group nor sampling complete dyadic blocks independently with replacement; the cyclic result does not imply (1)–(4). The finite abelian character-orthogonality identity used in our proof is classical and is not claimed as new. The asserted contribution is the complete sample-path block-spectrum classification and its explicit sampling law in this particular algorithm.

## Limitations
This theorem treats coordinate subspaces, not all subspaces; full-block rather than individual-row sampling; and the unpermuted global Walsh transform with the specified dyadic ordering. In particular, it does **not** apply unchanged to the garbled construction involving an additional random row permutation, to the different local-block sketch of Balabanov and colleagues, or to sampling without replacement (where the two-plane sign count becomes hypergeometric). The findings make no claim about privacy, security, or optimal algorithmic complexity. A folklore statement phrased in finite-group Fourier terms could contain the underlying combinatorial identity; no claim of absolute uniqueness is made.

## References
1. N. Charalambides, H. Mahdavifar, M. Pilanci, and A. O. Hero III, *Orthonormal Sketches for Secure Coded Regression*, arXiv:2201.08522, first submitted 2022-01-21; Algorithm 1, Section IV, Theorem 7. https://arxiv.org/abs/2201.08522
2. N. Charalambides, H. Mahdavifar, M. Pilanci, and A. O. Hero III, *Iterative Sketching for Secure Coded Regression*, arXiv:2308.04185, first submitted 2023-08-08; Section IV, Theorem 3, Appendix proof. https://arxiv.org/abs/2308.04185
3. O. Balabanov, M. Beaupère, L. Grigori, and V. Lederer, *Block Subsampled Randomized Hadamard Transform for Nyström Approximation on Distributed Architectures*, PMLR 202 (2023), 1564–1576; Section 2. https://proceedings.mlr.press/v202/balabanov23a.html
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, public mathematical result (2026), comparison concerning a different cyclic character frame. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0
