# Sparse-optimal Gabor tomography on Singer cycles: complete rigidity and near-SIC floor

## Finding
Let \(k\ge2\) be an integer and \(G\) any finite abelian group with \(|G|=v=k(k-1)+1\). A normalized window \(g\in\mathbb C^G\) with at most \(k\) nonzero coordinates can give informationally complete full Weyl–Heisenberg intensity measurements **only** when its support is a \((v,k,1)\) perfect difference set. On such a support, informational completeness holds **if and only if** all its zero-shift, nontrivial-character weighted Fourier sums \(\sum_{s\in S}|g(s)|^2\chi(s)\) are nonzero; in particular it holds for every flat-modulus window. Writing
\[
\delta(g)=\min_{a\in G,\,\chi\in\widehat G}|\langle g,M_\chi T_a g\rangle|,
\]
for these sparse windows the **sharp global ambiguity margin** is
\[
\max_{\|g\|_2=1,\,|\operatorname{supp}g|\le k}\delta(g)=\frac1k
\]
provided a perfect difference set exists, and is zero otherwise. Equality is attained **exactly** when the support is a perfect difference set and every nonzero coefficient has magnitude \(1/\sqrt{k}\); any coefficient phases work.

For each optimizer, the full rank-one measurement operator has exactly three eigenvalue levels in its positive frame operator, counted with multiplicities:
\[
\begin{array}{c|ccc}
\text{eigenvalue}&v&v(k-1)/k^2&v/k^2\\
\text{multiplicity}&1&v-1&v(v-1).
\end{array}
\]
The complete condition number is exactly \(k\), and the trace-free condition number is exactly \(\sqrt{k-1}\); both are the smallest achievable within this coordinate-sparsity class. The minimum nonidentity ambiguity intensity reaches the proportion
\[
\frac{v+1}{k^2}=1-\frac1k+\frac2{k^2}\ge\frac78
\]
of the universal SIC/Welch worst-direction bound, tending to one as \(k\to\infty\). This is **near-optimality of the least spectral direction only**; the system is not generally equiangular or spectrally flat. The perfect-difference-set construction itself and its injectivity were previously known; the claim concerns the sharp sparsity-constrained stability optimization, equality rigidity, both condition numbers, and the worst-direction SIC comparison.

## Assumptions and scope
For a character \(\chi\) of \(G\), define \((T_a g)(x)=g(x-a)\) and \((M_\chi g)(x)=\chi(x)g(x)\), with standard unnormalized Fourier sums and Euclidean norm \(\|g\|_2=1\). Define \(A_g(a,\chi)=\langle g,M_\chi T_a g\rangle\). Its absolute value is independent of inner-product convention. A \((v,k,1)\) perfect difference set is a set \(S\subseteq G\) of size \(k\) in which **every nonzero** group element occurs exactly once as an ordered difference \(s-t\) with distinct \(s,t\in S\). The lifted map is
\[
\mathcal L_g(X)_{a,\chi}=\operatorname{tr}\bigl(X\,\Pi_{a,\chi}\bigr),\qquad
\Pi_{a,\chi}=(M_\chi T_a)gg^*(M_\chi T_a)^*.
\]
The domain is the complex Hilbert–Schmidt space of matrices; its Hermitian real subspace has identical singular values. On traceless matrices, omit the identity eigen-direction. The projectors are **not** divided by \(v\); dividing them uniformly rescales all singular values but changes neither condition number nor the normalized spectral comparisons. Condition numbers of singular maps are infinite. No prime assumption is imposed on \(v\).

## Proof
**1. Sharp support threshold.** If \(S=\operatorname{supp}g\), then for each shift \(a\notin S-S\) and every character \(\chi\), the product \(g(x)\overline{g(x-a)}\) vanishes identically, so \(A_g(a,\chi)=0\). Because \(|S-S|\le |S|(|S|-1)+1\le k(k-1)+1=v\), nonvanishing for all shifts requires \(|S|=k\) and exactly one ordered representation of each nonzero difference. Thus \(S\) is perfect. Conversely if \(S\) is perfect, each nonzero shift contributes precisely one nonzero term to every ambiguity sum, hence all off-zero-shift ambiguity values are nonzero. For zero shift and nontrivial \(\chi\), the condition is exactly \(\sum_{s\in S}p_s\chi(s)\ne0\); this need **not** hold for arbitrary positive, nonuniform weights. It is automatic for a **flat** window, as shown below. Consequently, existence of a fully nonvanishing sparse window is equivalent to the existence of a perfect support set.

**2. Sharp margin and rigidity.** On a perfect support, each nonzero shift corresponds to a unique pair of distinct support positions \(s,t\), and for every character
\[
|A_g(s-t,\chi)|=|g(s)g(t)|=\sqrt{p_s p_t},\qquad p_s=|g(s)|^2,\quad\sum_{s\in S}p_s=1.
\]
Consequently \(\delta(g)\le\min_{s\ne t}\sqrt{p_s p_t}\le1/k\). The last inequality is strict unless every \(p_s=1/k\): indeed, if every distinct product were at least \(1/k^2\), then the product of all pairs would imply \(\prod_s p_s\ge k^{-k}\), while AM–GM gives \(\prod_s p_s\le k^{-k}\), forcing equality and uniform weights. If some pair is smaller, strictness is immediate. This also covers \(k=2\). For a uniform perfect support, the nonzero-shift ambiguity has modulus \(1/k\). At zero shift, \(A_g(0,1)=1\); for \(\chi\ne1\), character orthogonality and unique differences yield
\[
\biggl|\sum_{s\in S}\chi(s)\biggr|^2
=\sum_{s,t\in S}\chi(s-t)=k+\sum_{a\ne0}\chi(a)=k-1.
\]
Thus \(|A_g(0,\chi)|=\sqrt{k-1}/k\ge1/k\); the sharp margin and equality characterization follow. Any choice of coefficient phases leaves these moduli unchanged.

**3. Exact lifting spectrum and sharp condition numbers.** The finite Weyl operators \(M_\chi T_a\) form an orthogonal Hilbert–Schmidt basis. Expanding a matrix in this basis and Fourier transforming the covariant output indices diagonalizes \(\mathcal L_g^*\mathcal L_g\); for every Weyl label \((a,\chi)\), its eigenvalue is exactly \(v|A_g(a,\chi)|^2\). This follows directly by writing each translated projector coefficient as \(A_g(a,\chi)\) times the corresponding commutator character and applying orthogonality of all \(v^2\) such characters. Substituting the three ambiguity moduli from step 2 gives the spectrum above.

The identity-sector singular value is \(\sqrt v\) for **every** normalized \(g\), while the smallest singular value is \(\sqrt v\delta(g)\le\sqrt v/k\), so every invertible sparse lifting has full condition number at least \(k\), with equality exactly at the flat perfect-difference-set windows.

For the trace-free sector, the largest nonidentity ambiguity modulus is at least
\[
\max_{\chi\ne1}|A_g(0,\chi)|
\ge\sqrt{\frac{v\sum_{s\in S}p_s^2-1}{v-1}}
\ge\sqrt{\frac{k-1}{k^2}},
\]
where the first step is Parseval on \(G\) and the second is \(\sum p_s^2\ge1/k\). Its least nonidentity modulus is at most \(1/k\), by step 2. Therefore the trace-free condition number is at least \(\sqrt{k-1}\); flat perfect supports attain equality, and equality requires flatness by the preceding chain (or the sharper global margin rigidity).

**4. SIC comparison and infinite cyclic realization.** The finite Moyal identity gives \(\sum_{a,\chi}|A_g(a,\chi)|^2=v\). Since \(|A_g(0,1)|=1\), the average nonidentity squared ambiguity is \(1/(v+1)\), so no window can exceed that minimum squared modulus. In our sparse-optimal family its minimum is \(1/k^2\), yielding exact SIC-relative fraction \((v+1)/k^2\ge7/8\); the minimum of this elementary expression over integer \(k\ge2\) occurs at \(k=4\).

For any prime power \(q\ge2\), put \(k=q+1\), \(v=q^2+q+1\) and take the cyclic quotient \(G=\mathbb F_{q^3}^{\times}/\mathbb F_q^{\times}\). The projective points of a two-dimensional \(\mathbb F_q\)-linear subspace \(W\subset\mathbb F_{q^3}\) form a set \(S\subseteq G\) of size \(q+1\). For each nontrivial quotient element represented by \(\xi\notin\mathbb F_q\), the planes \(W\) and \(\xi W\) meet in exactly one projective point: dimension counting gives at least one, while equality of planes would make a two-dimensional subspace invariant under a degree-three field generator, which is impossible. This gives exactly one ordered difference for every nonidentity quotient element. Thus Singer perfect difference sets give the asserted family. In particular, for \(q=2^{3t+1}\) and \(t\ge1\), \(v=q^2+q+1\) is a composite multiple of seven, yielding infinitely many composite cyclic dimensions.

## Verification
The accompanying `verify.py` checks perfect-difference-set uniqueness and the complete self-ambiguity modulus distribution for explicit cyclic examples \((v,k)=(7,3),(13,4),(21,5),(31,6)\), including nontrivial coefficient phases and two nonuniform weight configurations. It asserts the predicted three-level multiplicities and the sharp bound. A separate direct dense Hilbert–Schmidt singular-value computation in dimension seven also matched \(\sqrt v\) times those moduli. These finite checks corroborate but do not replace the general proof, which establishes all dimensions and equality cases without numerical assumptions.

## Relationship to prior work
Bojarovska–Flinth, *Phase Retrieval from Gabor Measurements* (2015), already establishes the nonzero-ambiguity injectivity criterion and presents difference-set examples. Bojarovska–Paternostro, *Gabor fusion frames generated by difference sets* (2015), computes Gabor coherence for flat perfect difference sets, including the nontrivial overlap levels. Zhu–Wang, *Uniformly Stable Minimal Weyl–Heisenberg Measurements Approaching the SIC Benchmark* (first public August 12, 2026), formulates worst-direction operator-Gram stability through ambiguity intensities. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (first public September 9, 2026), gives a different full-spark construction and quantitative ambiguity margins. Here the specific further conclusions are a sharp theorem **over every window with at most \(k\) coordinates**, complete optimizer rigidity, both minimum condition numbers, and the exact near-SIC worst-direction ratio, including infinitely many non-prime-power cyclic dimensions. Earlier characteristic-function constructions and their coherence constants are credited, not reclassified as new.

## Limitations
Optimality is only within the at-most-\(k\) coordinate-sparse class in dimensions \(v=k(k-1)+1\). It is not a globally optimal condition number over all windows, and the SIC fraction concerns the **minimum**, not uniform equiangularity, of ambiguity intensities. For groups lacking perfect difference sets, no window of this sparsity can be informationally complete. The theorem is analytic, not an experimental stability guarantee under a specific physical noise model. The two 2026 preprints were compared using available abstracts/metadata because their full manuscripts were inaccessible; overlap with an unavailable theorem cannot be categorically excluded. No independent mathematical review has been performed.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), especially Theorem 2.2 and the difference-set construction.
2. I. Bojarovska and V. Paternostro, *Gabor fusion frames generated by difference sets*, arXiv:1507.01829 (2015), especially Proposition 2.5 and Theorem 2.9.
3. X. Zhu and Y. Wang, *Uniformly Stable Minimal Weyl–Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850 (first public 2026-08-12).
4. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (first public 2026-09-09).
