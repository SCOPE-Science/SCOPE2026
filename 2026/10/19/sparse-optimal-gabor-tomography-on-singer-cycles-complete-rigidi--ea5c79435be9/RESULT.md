# Sparse-optimal Gabor tomography at the perfect difference-set threshold

## Finding

Let \(k\ge2\) be an integer and \(G\) a finite abelian group of order \(v=k(k-1)+1\). Consider normalized windows \(g\in\mathbb C^G\) with at most \(k\) nonzero coordinates. If the full Weyl–Heisenberg intensity measurement is informationally complete, the support must be a \((v,k,1)\) perfect difference set. On a perfect support \(S\), informational completeness holds exactly when \(\sum_{s\in S}|g(s)|^2\chi(s)\ne0\) for each nontrivial character \(\chi\); in particular flat-modulus windows on such a support are informationally complete.

Define \(\delta(g)=\min_{a,\chi}|\langle g,M_\chi T_a g\rangle|\). If a perfect difference set exists, the maximum of \(\delta(g)\) over the indicated sparse class is \(1/k\). It is attained precisely on perfect difference sets with all nonzero coefficients of magnitude \(1/\sqrt{k}\), with arbitrary phases. If no perfect difference set exists, every eligible window has \(\delta(g)=0\) and neither the full nor the traceless lifting is injective.

For each flat perfect-support optimizer the eigenvalue **multiset** of the positive frame operator is
\[
\begin{array}{c|ccc}
\text{eigenvalue}&v&v(k-1)/k^2&v/k^2\\
\text{multiplicity before merging equal values}&1&v-1&v(v-1).
\end{array}
\]
There are three distinct levels for \(k>2\). For \(k=2\), \(v=3\), there are **two** levels: \(3\) with multiplicity one and \(3/4\) with multiplicity eight. In every feasible case the same optimizers uniquely minimize both the full singular-value condition number (\(k\)) and the trace-free singular-value condition number (\(\sqrt{k-1}\)) within the class, with uniqueness understood up to choice of perfect support and coefficient phases.

The minimum nonidentity ambiguity intensity at these optimizers is the fraction
\[
\frac{v+1}{k^2}=1-\frac1k+\frac2{k^2}\ge\frac78
\]
of the universal SIC/Welch worst-direction upper bound. The fraction tends to one as \(k\) grows, including along infinitely many composite cyclic orders supplied by Singer's construction. This is a statement about the least direction, not overall spectral flatness. At \(k=2\) the fraction equals one and all nonidentity ambiguity intensities are equal; for \(k>2\) the two nonidentity levels differ.

## Assumptions and scope

Use \((T_ag)(x)=g(x-a)\), \((M_\chi g)(x)=\chi(x)g(x)\), unnormalized character sums and \(\|g\|_2=1\). A perfect difference set is a support of size \(k\) in which each nonzero group element is represented exactly once as an ordered difference of two distinct support points. Write \(A_g(a,\chi)=\langle g,M_\chi T_a g\rangle\). The measurement lifting is
\[
\mathcal L_g(X)_{a,\chi}=\operatorname{tr}(X\Pi_{a,\chi}),\qquad
\Pi_{a,\chi}=(M_\chi T_a)gg^*(M_\chi T_a)^*.
\]
The projectors are not divided by \(v\). The domain can be the complex Hilbert–Schmidt space, or the real space of Hermitian matrices with the same singular values. Informational completeness here means injectivity of the lifting, not merely recovery on rank-one inputs. The trace-free lifting restricts the domain to traceless matrices and omits the identity eigen-direction from the frame spectrum. The condition number of a noninjective lifting is infinite. The optimization assumes no primality of \(v\).

## Proof

**Spectrum of the lift and support threshold.** The Weyl operators \(M_\chi T_a\) form an orthogonal Hilbert–Schmidt basis, of norm \(\sqrt v\) per operator. Conjugating by another Weyl operator multiplies a Weyl basis element by the corresponding commutator character of \(G\times\widehat G\); these characters are distinct since pairing with every translation and modulation separates the label. Thus the output of a normalized Weyl basis element under \(\mathcal L_g\) is that character, up to conjugation, scaled by a coefficient of magnitude \(|A_g(a,\chi)|/\sqrt v\). Character orthogonality proves that the eigenvalue is \(v|A_g(a,\chi)|^2\). This proves the nonvanishing criterion, with the same spectrum on the real Hermitian space by complexification. The identity eigenvalue is \(v\), which is maximal by Cauchy–Schwarz.

Put \(S=\operatorname{supp}g\). If \(a\notin S-S\) then all ambiguity coefficients at shift \(a\) vanish. The count \(|S-S|\le |S|(|S|-1)+1\le v\) forces equality throughout for injectivity. Equality is equivalent to \(S\) being a perfect difference set. For such a support and any nonzero shift \(s-t\), only the ordered pair \((s,t)\) contributes, so
\[
|A_g(s-t,\chi)|=\sqrt{p_s p_t},\qquad p_s=|g(s)|^2,\quad \sum_s p_s=1.
\]
These coefficients never vanish. Zero shift gives the weighted Fourier sums stated in the finding (up to conjugation, depending on convention); the trivial-character sum equals one. If no perfect support exists, a missing nonzero shift therefore forces a zero eigenvalue also on the trace-free sector.

**Sharp floor, exact optimizer and spectrum.** For a perfect support,
\(\delta(g)\le\min_{s\ne t}\sqrt{p_s p_t}\le1/k\). Indeed, if all distinct pair products are at least \(1/k^2\), multiplying over pairs gives \(\prod_s p_s\ge k^{-k}\); normalization and AM–GM imply equality and uniform weights. Conversely for flat weights the nonzero-shift moduli equal \(1/k\), and for each \(\chi\ne1\),
\[
\left|\sum_{s\in S}\chi(s)\right|^2=k+\sum_{a\ne0}\chi(a)=k-1.
\]
The zero-shift nontrivial moduli are therefore \(\sqrt{k-1}/k\). The largest modulus is one and the smallest is \(1/k\). The multiset follows from the lift formula and the counts of identity, nontrivial zero-shift, and nonzero-shift labels. In particular the last two blocks coalesce at \(k=2\). All these quantities are independent of coefficient phases. The full condition-number minimum and its rigidity follow from the identity-sector singular value \(\sqrt v\) and the sharp floor.

**Sharp trace-free condition number.** In any injective eligible instance, Parseval gives
\[
\max_{\chi\ne1}|A_g(0,\chi)|^2\ge\frac{v\sum_s p_s^2-1}{v-1}\ge\frac{k-1}{k^2},
\]
since \(\sum_s p_s^2\ge 1/k\). The least nonidentity modulus is at most \(1/k\) by the pair argument. The ratio of largest to smallest trace-free singular value is therefore at least \(\sqrt{k-1}\). Nonuniform weights make both inequalities used for this lower bound strict; equality and admissibility are exactly the flat perfect-support cases already found.

**SIC benchmark and realizations.** Weyl orthogonality applied to \(gg^*\) gives the Moyal sum \(\sum_{a,\chi}|A_g(a,\chi)|^2=v\). The identity coefficient has intensity one, so the mean of all \(v^2-1\) nonidentity intensities is \(1/(v+1)\); their minimum is at most this value. For the optimizer the ratio is \((v+1)/k^2\), and the difference from \(7/8\) equals \((k-4)^2/(8k^2)\).

For a prime power \(q\ge2\), take the cyclic quotient \(G=\mathbb F_{q^3}^{\times}/\mathbb F_q^{\times}\). The projective points of a two-dimensional \(\mathbb F_q\)-subspace \(W\) form a support of size \(q+1\). For each nontrivial quotient element represented by \(\xi\notin\mathbb F_q\), \(W\) and \(\xi W\) meet in exactly one projective point. Their intersection has dimension at least one, and equality of the two planes would make a two-dimensional subspace invariant under multiplication by a degree-three generator of the field extension, which is impossible. This gives precisely one ordered difference at every nonidentity quotient element. Taking \(q=2^{3t+1}\), \(t\ge1\), yields \(q\equiv2\pmod7\) and \(q^2+q+1>7\) divisible by seven, hence infinitely many composite cyclic orders.

## Verification

The accompanying `verify.py` tests the four cyclic cases \((v,k)=(7,3),(13,4),(21,5),(31,6)\) with selected nontrivial phases and selected nonuniform weights. Those are cases with three distinct eigenvalue levels. The boundary case \(v=3,k=2\) instead follows exactly from \(k-1=1\) in the multiset formula, and the support \(\{0,1\}\) in \(\mathbb Z_3\) attains it. Finite evaluations corroborate but do not prove the general result.

## Relationship to prior work

Bojarovska–Flinth give the ambiguity-based lifting frame bounds and difference-set examples [1]; Bojarovska–Paternostro give the flat difference-set overlap moduli and Singer examples [2]. Zhu–Wang give the general Weyl–Heisenberg projector-Gram spectrum and SIC-normalized stability framework [3, Theorem 1]. Their Appendix D, Proposition 12(3), gives the cyclic support-count obstruction using \(|S-S|\le |S|(|S|-1)+1\), and explicitly notes that a difference set can saturate that count. The necessity of the support at equality, the optimizer's spectral levels, and its SIC ratio thus use these known structural facts; the ratio itself is an evaluation of the prior overlap values. Li gives a distinct full-spark and quantitative design construction [4].

The optimization asserted here concerns **all** coefficient allocations on all supports of size at most \(k\) in the indicated group order: the pair-product obstruction, with its equality rigidity, and the independent trace-free extremum using the zero-shift Parseval bound. Neither the known flat-window overlap table nor the lift diagonalization alone optimizes over nonflat coefficients. The Singer construction gives explicit cases but is not claimed as new.

## Limitations

The optimization is restricted to the at-most-\(k\) coordinate-sparse class at order \(k(k-1)+1\). It does not identify a globally optimal condition number without the sparsity restriction. The SIC fraction measures the minimum direction, not a uniform proximity claim for all spectral directions. The result concerns mathematical inversion in exact arithmetic, not a physical noise or implementation guarantee. The cited comparisons do not certify exhaustive historical priority.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, especially Theorems 2.2–2.3.
2. I. Bojarovska and V. Paternostro, *Gabor fusion frames generated by difference sets*, arXiv:1507.01829, Proposition 2.5 and Theorem 2.9.
3. X. Zhu and Y. Wang, *Uniformly Stable Minimal Weyl–Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850, Theorem 1 and Appendix D, Proposition 12.
4. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v2.
