# Sharp norm and essential spectrum of monomial slant Bergman commutators

## Finding

On the unweighted analytic Bergman space of the unit disk, let \(r\geq2\) be an integer, and let the downsampling operator \(W_r\) act on ordinary monomials by \(W_r(z^{rn})=z^n\) and \(W_r(z^j)=0\) when \(r\nmid j\). Put \(B_a=W_rT_{z^a}\), where \(a\) is any nonnegative integer and \(T_{z^a}\) is analytic Toeplitz multiplication. For nonnegative integers \(a\ne b\), define the commutator \(C=[B_a,B_b]\).

Then the **ordinary and essential operator norms coincide**, with a sharp congruence transition:
\[
\|C\|=\|C\|_{\mathrm{ess}}=\begin{cases}
r\sqrt2,&r^2\nmid(a-b),\\
2r,&r^2\mid(a-b).
\end{cases}
\]
Its **positive essential spectrum** is also exact:
\[
\sigma_{\mathrm{ess}}(CC^*)=\begin{cases}
\{2r^2\},&r^2\nmid(a-b),\\
[0,4r^2],&r^2\mid(a-b).
\end{cases}
\]
Here \(\sigma_{\mathrm{ess}}\) is the spectrum of the image in the Calkin algebra. Neither nonzero commutator attains its ordinary operator norm. When \(a=b\), the commutator is zero, so the displayed nonzero formulas do not apply.

The degree condition is structural: changing only the residue class of \(a-b\) modulo \(r^2\) changes the Calkin square from an asymptotic scalar to an asymptotic discrete Laplacian.

## Assumptions and scope

The norm on \(A^2(\mathbb D)\) is defined using normalized planar area measure. Its orthonormal basis is \(e_n(z)=\sqrt{n+1}z^n\) for \(n=0,1,\ldots\). The operators \(T_{z^a}\) and \(W_r\) are bounded on this Hilbert space; the convention for \(W_r\) is on *ordinary monomials*, not a coefficient-normalized downsampler on orthonormal monomials. This distinction affects all sharp constants. Parameters are integers \(r\ge2\), \(a,b\ge0\). The result makes no assertion for general polynomial, harmonic or polyanalytic symbols, nor for other Bergman weights.

The essential norm means distance to the compact operators, and the essential spectrum of \(CC^*\) is understood via the quotient by the compact operators. Norm attainment means existence of a unit vector realizing the norm.

## Proof

**Step 1 (exact two-step action).** By applying analytic multiplication and then the slant map, one has
\[
B_a e_n=\begin{cases}
\sqrt{\frac{n+1}{m+1}}e_m,&m=(n+a)/r\in\mathbb Z_{\ge0},\\
0,&r\nmid(n+a).
\end{cases}
\]
The weights telescope upon composing two such operators. Set \(d_1=b+ra\) and \(d_2=a+rb\). Then, for every \(n\ge0\),
\[
Ce_n=\mathbf{1}_{r^2\mid n+d_1}\sqrt{\frac{n+1}{m_1+1}}\,e_{m_1}
-\mathbf{1}_{r^2\mid n+d_2}\sqrt{\frac{n+1}{m_2+1}}\,e_{m_2},
\qquad m_i=\frac{n+d_i}{r^2}
\]
(with each \(m_i\) used only when integral). The weights on such an input have squares
\[
\frac{n+1}{m_i+1}=r^2-\frac{d_i+r^2-1}{m_i+1}<r^2,
\]
and tend to \(r^2\) as the output index tends to infinity. Hence each order-two product has norm exactly \(r\), but does not attain it on any nonzero vector. In particular, \(\|C\|\le2r\).

**Step 2 (distinct residue streams).** Since
\[
d_1-d_2=(r-1)(a-b),\qquad\gcd(r-1,r^2)=1,
\]
the congruence classes \(-d_1\) and \(-d_2\) modulo \(r^2\) differ precisely when \(r^2\nmid(a-b)\). In this case the two terms of the action use disjoint input basis vectors. Their outputs lie in the *same* output basis, so \(CC^*\) is diagonal. Its \(m\)-th diagonal entry is, exactly,
\[
\lambda_m=\sum_{i=1}^{2}\mathbf{1}_{r^2m\ge d_i}\frac{r^2m-d_i+1}{m+1}.
\]
Every \(\lambda_m<2r^2\), but \(\lambda_m\to2r^2\). Therefore \(CC^*-2r^2I\) is compact, \(\|C\|^2=\|CC^*\|=2r^2\), and its positive essential spectrum is the singleton \(\{2r^2\}\). The top diagonal value is never an eigenvalue. If \(C\) attained its norm, its positive adjoint square would have a top eigenvector; transferring this eigenvector through \(C\) would give a top eigenvector of \(CC^*\), which is impossible.

**Step 3 (one common residue stream).** Suppose \(r^2\mid(a-b)\) and \(a\ne b\). Exchanging the two operators if necessary replaces \(C\) by \(-C\), and we may arrange \(d_2>d_1\). Thus
\[
q=\frac{d_2-d_1}{r^2}\in\mathbb Z_{>0}.
\]
For every sufficiently large \(m\), the single input \(n=r^2m-d_1\) contributes two output components, at \(m\) and \(m+q\), with respective weights tending to \(r\) and \(-r\). Thus the matrix of \(CC^*\), away from finitely many initial rows, has a main diagonal tending to \(2r^2\) and diagonals at offsets \(\pm q\) tending to \(-r^2\); all other entries vanish. A banded operator whose entries along each of finitely many diagonals tend to zero is compact, because truncation of those diagonals to finitely many coordinates converges in operator norm. Hence, writing \(S\) for the standard unilateral shift,
\[
CC^*=r^2(2I-S^q-S^{*q})+K
\]
for some compact \(K\). The Toeplitz operator \(2I-S^q-S^{*q}\) has essential spectrum the range of its continuous symbol \(2-2\cos(q\theta)\), namely \([0,4]\). Consequently \(\sigma_{\mathrm{ess}}(CC^*)=[0,4r^2]\), and \(\|C\|_{\mathrm{ess}}=2r\). The upper estimate from Step 1 yields \(\|C\|=2r\).

**Step 4 (norm nonattainment in the common-residue case).** Denote the two order-two products by \(P_1\) and \(P_2\). For any nonzero vector \(x\), the strict weight estimate in Step 1 implies \(\|P_i x\|<r\|x\|\) for both \(i=1,2\), even if one product vanishes on part of the support. Thus
\[
\|Cx\|\le\|P_1x\|+\|P_2x\|<2r\|x\|=\|C\|\|x\|.
\]
This completes the proof for all parameters in the stated scope.

## Verification

The supplied `check_slant.py` independently computes the action of the two compositions and the telescoped formula, verifies the congruence test and strict weight bounds for a broad deterministic finite parameter set, and estimates selected finite-section norms from below. A run from the extracted package passed **29,766 deterministic assertions**. Sample lower estimates for \((r,a,b)=(2,0,1)\) and \((2,0,4)\) are approximately \(2.821379\) and \(3.976143\), versus rigorous infinite-dimensional norms \(2\sqrt2\) and \(4\), respectively. The finite samples do **not** prove the norm limit, essential spectrum, or norm nonattainment; those are proved analytically above. Execute with `python check_slant.py` using NumPy and SciPy.

## Relationship to prior work

Cui, Li, and Lu (2026, arXiv:2610.09728v1), first public on October 7, 2026, study commuting slant Toeplitz operators for polyanalytic and harmonic symbols on the unweighted Bergman space. Their Section 2 proves zero and finite-rank commutator rigidity, but does not supply the sharp two-level commutator norm, positive essential spectrum, or nonattainment classification calculated here. Their definition of the second-order slant operator agrees with the monomial normalization used here when \(r=2\).

Lu, Liu, and Yang (2010) establish equivalence between commutativity and essential commutativity for relevant slant Toeplitz operators, a qualitative noncompactness statement. Liu and Lu (2013) study commuting and product identities. These statements do not by themselves determine the two distinct exact essential-norm levels or their Calkin spectral sets. The full text of the 2010 source could not be inspected in the present comparison, leaving a priority risk. Singh, Singh, and Singh (2025, arXiv:2507.06546v1) examine weighted Bergman slant operators and finite-section examples, but employ a differently normalized downsampler and do not report this universal sharp congruence-dependent commutator classification.

## Limitations

The theorem concerns only pairs of analytic monomial symbols and normalized-area analytic Bergman space. The positive essential spectrum is computed for \(CC^*\), not the nonnormal commutator \(C\) itself. The compact-perturbation proof does not give finite-rank singular spectra, nor does finite numerical truncation certify any infinite-dimensional conclusion. Historical priority needs independent comparison, particularly with Lu–Liu–Yang (2010) and potentially related weighted-composition literature whose entire text was not available.

## References

1. Puyu Cui, Ran Li, YuFeng Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1, 2026-10-07. https://arxiv.org/html/2610.09728v1
2. Yufeng Lu, Chaomei Liu, Jun Yang, *Commutativity of \(k\)-th-order slant Toeplitz operators*, Mathematische Nachrichten 283 (2010), 1304–1313. https://doi.org/10.1002/mana.200710100
3. Chaomei Liu, Yufeng Lu, *Product and Commutativity of \(k\)-th-Order Slant Toeplitz Operators*, Abstract and Applied Analysis 2013 (2013), article 473916. https://doi.org/10.1155/2013/473916
4. Oinam Nilbir Singh, M. P. Singh, Thokchom Sonamani Singh, *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546v1 (2025). https://arxiv.org/html/2507.06546v1
