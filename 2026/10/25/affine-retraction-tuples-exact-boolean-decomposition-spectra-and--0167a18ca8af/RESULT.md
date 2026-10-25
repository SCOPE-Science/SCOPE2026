# Affine retraction tuples: exact Boolean-decomposition spectra and periodic discrete-Gaussian commutativity costs

## Finding

Let \(q\) be a prime power, let \(V=\mathbb F_q^n\), and let \(\operatorname{AffEnd}(V)\) be the monoid of all affine self-maps \(v\mapsto Av+b\). Here \(n\ge1\) and \(k\ge1\). An *affine retraction* is an idempotent affine self-map. An ordered \(k\)-tuple of affine retractions is *compatible* when its members commute pairwise. Put \(m=2^k\), label the elements of \(\{0,1\}^k\) by \(\sigma\), and denote the all-one label by \(\mathbf1\).

**Exact orbit and counting theorem.** Compatible ordered tuples are classified up to simultaneous conjugation by the affine unit group \(\operatorname{AGL}(V)\) by a unique weak composition \(a=(a_\sigma)_{\sigma\in\{0,1\}^k}\) of \(n\) into \(m\) parts. The common image of the product retraction has dimension \(a_{\mathbf1}\). The number of tuples of profile \(a\) is
\[
 T_q(a)=q^{n-a_{\mathbf1}}\frac{|\operatorname{GL}_n(\mathbb F_q)|}{\prod_\sigma|\operatorname{GL}_{a_\sigma}(\mathbb F_q)|}.
\]
Consequently there are exactly \(\binom{n+m-1}{m-1}\) simultaneous affine-conjugacy classes, and the exact number of compatible ordered tuples is
\[
 C_{n,k}(q)=\sum_{\substack{a_\sigma\ge0\\\sum_\sigma a_\sigma=n}}
 q^{n-a_{\mathbf1}}\frac{|\operatorname{GL}_n(\mathbb F_q)|}{\prod_\sigma|\operatorname{GL}_{a_\sigma}(\mathbb F_q)|}.
\]
The stabilizer of a tuple of profile \(a\) in \(\operatorname{AGL}(V)\) has cardinality \(q^{a_{\mathbf1}}\prod_\sigma|\operatorname{GL}_{a_\sigma}(\mathbb F_q)|\). For fixed commuting linear parts, there are exactly \(q^{n-a_{\mathbf1}}\) compatible translation choices.

**Sharp fixed-arity limit law.** Fix \(q\) and \(k\) while letting \(n\) grow. Write
\[
 \Phi_q=\prod_{j=1}^{\infty}(1-q^{-j}),\qquad
 \mathcal L_{m,s}=\bigl\{\delta\in(\mathbb Z-s/m)^m:\sum_\sigma\delta_\sigma=0\bigr\},
\]
and, for each residue \(s\in\{0,\ldots,m-1\}\), define the absolutely convergent positive theta sum
\[
 Z_{q,k,s}=\sum_{\delta\in\mathcal L_{m,s}}
 q^{-\sum_\sigma\delta_\sigma^2-\delta_{\mathbf1}}.
\]
Along integers \(n\to\infty\) with \(n\equiv s\pmod m\), one has the exact asymptotic equivalent
\[
 C_{n,k}(q)\sim \Phi_q^{1-m}Z_{q,k,s}\,q^{(1-1/m)(n^2+n)}.
\]
If a compatible tuple is chosen uniformly, the centered profile \(\delta_\sigma=a_\sigma-n/m\) converges in total variation to the probability mass function
\[
 \Pr(\delta=d)=Z_{q,k,s}^{-1}q^{-\sum_\sigma d_\sigma^2-d_{\mathbf1}},\qquad d\in\mathcal L_{m,s}.
\]
In particular every joint eigenspace has dimension \(n/m+O_{\Pr}(1)\), each individual linear retraction has image dimension \(n/2+O_{\Pr}(1)\), and the common product retraction has image dimension \(n/m+O_{\Pr}(1)\).

Let \(R_{n,k}(q)\) be the probability that \(k\) independent uniformly chosen affine retractions commute pairwise, with repetitions allowed. For \(k\ge2\), set \(\gamma_k=k/2-1+2^{-k}\). Along the same residue subsequence,
\[
 \boxed{\lim_{\substack{n\to\infty\\n\equiv s\, (\mathrm{mod}\,m)}}
 q^{\gamma_k(n^2+n)}R_{n,k}(q)
 =\Phi_q^{k+1-m}\frac{Z_{q,k,s}}{Z_{q,1,s\bmod2}^{\,k}}>0.}
\]
Thus \(\log_q R_{n,k}(q)=-\gamma_k(n^2+n)+O_{q,k}(1)\), including a sharp linear correction and an explicit nontrivial periodic limiting multiplier. For \(k=2\), the quadratic commutativity cost is \(1/4\); for \(k=3\), it is \(5/8\).

## Assumptions and scope

An affine map is a map \(f(v)=Av+b\) with \(A\in\operatorname{End}_{\mathbb F_q}(V)\) and \(b\in V\), with composition as the semigroup product. The affine-unit group consists of the invertible such maps. Each map is counted as a distinct function, rather than counted by a choice of fixed point. The group order convention is \(|\operatorname{GL}_0(\mathbb F_q)|=1\). The word 'rank' for a retraction means affine image dimension; the linear rank of its linear part agrees with that dimension. All asymptotic assertions hold with fixed finite field and fixed positive tuple length, not uniformly with either parameter varying.

## Proof

**1. Shared fixed point.** Given commuting idempotents \(f_1,\ldots,f_k\), their product \(P=f_1\circ\cdots\circ f_k\) is idempotent. Moreover \(f_i\circ P=P\) for every \(i\). Therefore \(c=P(0)\) is a common fixed point. Write \(f_i(v)=A_iv+b_i\). The equation \(f_i(c)=c\) gives \(b_i=(I-A_i)c\), hence \(f_i(v)=c+A_i(v-c)\). The idempotence and commutation identities for \(f_i\) reduce to \(A_i^2=A_i\) and \(A_iA_j=A_jA_i\). Conversely any such commuting linear idempotents and any \(c\in V\) give commuting affine idempotents by this formula. Two choices \(c,c'\) give the same ordered tuple precisely when \((I-A_i)(c-c')=0\) for every \(i\). In other words, \(c-c'\) lies in the joint fixed space \(W=\bigcap_i\operatorname{im} A_i\).

**2. Orthogonal joint spectral projections.** For \(\sigma\in\{0,1\}^k\), define
\[
 E_\sigma=\prod_{i:\sigma_i=1}A_i\prod_{i:\sigma_i=0}(I-A_i).
\]
All factors commute. The maps \(E_\sigma\) are pairwise orthogonal idempotents with sum \(I\). Thus \(V=\bigoplus_\sigma V_\sigma\), where \(V_\sigma=\operatorname{im}E_\sigma\), and \(A_i\) acts by scalar \(\sigma_i\) on \(V_\sigma\). Conversely every such labelled direct-sum decomposition defines one linear commuting tuple. Writing \(a_\sigma=\dim V_\sigma\), the common fixed space is exactly \(W=V_{\mathbf1}\). The product's linear part is \(E_{\mathbf1}\); its affine image is \(c+V_{\mathbf1}\).

**3. Enumeration and affine conjugacy.** For a fixed profile \(a\), the invertible linear group acts transitively on the labelled direct-sum decompositions. The stabilizer is the block product \(\prod_\sigma\operatorname{GL}_{a_\sigma}(\mathbb F_q)\), so the orbit has size \(|\operatorname{GL}_n|/\prod_\sigma|\operatorname{GL}_{a_\sigma}|\). For each such linear tuple, the translations \(c\in V/W\) give exactly \(q^{n-a_{\mathbf1}}\) distinct compatible affine tuples. The affine group acts transitively on this fibre by common translation, and it is transitive on the labelled decompositions by its linear subgroup. After conjugating the common fixed point to the origin, the stabilizer consists precisely of block-diagonal linear automorphisms and translations in \(W\); before this normalization, a stabilizing affine map \(v\mapsto Bv+u\) has \(B\) block diagonal and \(u=(I-B)c+w\) for some \(w\in W\). This establishes the exact count, the stabilizer, and the class count, without assuming a simultaneous fixed point beforehand.

**4. Completion of squares for the counting weight.** Define \(\Phi_q(r)=\prod_{j=1}^r(1-q^{-j})\), with \(\Phi_q(0)=1\). The standard finite-field identity \(|\operatorname{GL}_r(\mathbb F_q)|=q^{r^2}\Phi_q(r)\) turns the exact count into
\[
 C_{n,k}(q)=\sum_{\sum a_\sigma=n}
 q^{n+n^2-a_{\mathbf1}-\sum_\sigma a_\sigma^2}
 \frac{\Phi_q(n)}{\prod_\sigma\Phi_q(a_\sigma)}.
\]
Set \(\delta_\sigma=a_\sigma-n/m\). Since \(\sum\delta_\sigma=0\), elementary expansion gives the exact exponent identity
\[
 n+n^2-a_{\mathbf1}-\sum_\sigma a_\sigma^2
 =(1-1/m)(n^2+n)-\sum_\sigma\delta_\sigma^2-\delta_{\mathbf1}.
\]
When \(n\equiv s\pmod m\), all possible deviations lie in \(\mathcal L_{m,s}\); the finite-dimensional condition only requires \(\delta_\sigma\ge-n/m\).

**5. Theta limits and total variation.** The infinite product satisfies \(0<\Phi_q\le\Phi_q(r)\le1\) for all \(r\ge0\). Therefore the normalized summands are bounded by
\[
 \Phi_q^{-m}q^{-\sum\delta_\sigma^2-\delta_{\mathbf1}},
\]
a summable function on the fixed zero-sum lattice \(\mathcal L_{m,s}\). Indeed a quadratic form on a finite-dimensional lattice dominates the linear term. For any fixed \(\delta\) on that lattice, all \(a_\sigma=n/m+\delta_\sigma\) tend to infinity, so \(\Phi_q(n)/\prod_\sigma\Phi_q(a_\sigma)\to\Phi_q^{1-m}\). Dominated convergence gives the asymptotic equivalent and, applied to the normalized summands, convergence in \(\ell^1\), which is total-variation convergence. This also proves \(a_\sigma-n/m=O_{\Pr}(1)\). Summing appropriate spectral blocks gives the individual and common product ranks.

**6. Compatibility probability.** The number of single affine retractions is \(C_{n,1}(q)\). An independent uniformly sampled \(k\)-tuple is compatible with probability \(R_{n,k}(q)=C_{n,k}(q)/C_{n,1}(q)^k\). Apply the proven asymptotic for arities \(k\) and \(1\); the latter has exactly two joint eigenspaces and residue \(n\bmod2\). Cancelling powers of \(q\) yields \(\gamma_k=k/2-1+1/m\), and cancelling the finite positive theta constants gives the displayed limit. There are only finitely many residue classes, so the logarithmic remainder is globally bounded for fixed \(q,k\). This completes every claimed statement.

## Verification

The reproducible standalone script `VERIFY.py` exhaustively constructs affine maps as functions, tests idempotence and tuple-wise commutation by composing their full transformation tables, and independently evaluates the finite general-linear-group sum. It checks eleven configurations in \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); the quadratic field uses the irreducible polynomial \(t^2+t+1\). For instance the commuting ordered-pair counts are \(5233\) for \((q,n)=(2,3)\), \(460\) for \((3,2)\), and \(1249\) for \((4,2)\); the ordered-triple count for \((2,2)\) is \(617\). On execution the script reports `VERIFY_OK: affine idempotent tuple formula; all 11 cases`.

The finite exhaustive tests are independent checks of the counting formulas in those dimensions; they are not proofs of the asymptotic claims, whose justification is the dominated-convergence argument above.

## Relationship to prior work

Diatta, Manga, and Mbaye (arXiv:2002.08737v1, February 19, 2020) study general systems of commuting matrices, certain maximal abelian subalgebras, and a Gerstenhaber-type dimension bound in characteristic zero. Their methods and statements motivate attention to higher-arity commutation, but do not furnish finite-field counts of affine idempotent tuples or their large-dimensional probability law. Sharma (arXiv:1409.2698v7, first posted September 7, 2014) treats conjugacy of unrestricted commuting matrix tuples, particularly sizes up to four, rather than affine idempotent strata. Sharma (arXiv:1506.07678v5, first posted June 2015) treats fixed matrix size with increasing tuple length, and explicitly distinguishes fixed-length large-dimension asymptotics as a different question. The semisimple simultaneous eigenspace decomposition itself is standard, and is not claimed as a new lemma. The contribution claimed here is the combined affine translation-fibre census, all-arity conjugacy profiles, and the fixed-arity sharp theta-limit and compatibility exponent. Any stronger published finite-field affine-retraction theorem giving the displayed formulas would cover the claim; exhaustive priority is not asserted.

## Limitations

The field order \(q\) and arity \(k\) are fixed for the asymptotic results. No uniform estimates are claimed when \(k\), \(q\), or both grow with \(n\). The finite verification checks small dimensions only. In particular, the existence of higher-arity exact formulas for unrestricted matrices does not itself prove those formulas here unless the idempotent and affine translation restrictions are taken into account. No independent external mathematical audit has been performed.

## References

1. A. Diatta, B. Manga, A. Mbaye, *On systems of commuting matrices, Frobenius Lie algebras and Gerstenhaber's Theorem*, arXiv:2002.08737v1 (first public version February 19, 2020), https://arxiv.org/abs/2002.08737.
2. U. B. Sharma, *Simultaneous Similarity Classes of Commuting matrices over a finite field*, arXiv:1409.2698 (first public version September 7, 2014), https://arxiv.org/html/1409.2698v7.
3. U. B. Sharma, *Asymptotic of Number of Similarity Classes of Commuting Tuples*, arXiv:1506.07678, https://arxiv.org/html/1506.07678v5.
