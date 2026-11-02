# Arithmetic nullity of singleton–cyclic-adjacency cross-covariance in uniform set partitions

## Finding

For every integer \(n\ge3\) and nonzero displacement \(d\in\{1,\ldots,n-1\}\), let \(\Pi\) be a uniformly random set partition of the cyclically labeled set \(\mathbb Z/n\mathbb Z\). Let \(I_i\) indicate that \(\{i\}\) is a singleton block and let \(A_j^{(d)}\) indicate that \(j\) and \(j+d\pmod n\) lie in the same block. This counts oriented displacement pairs, so columns at opposite orientations may coincide when \(2d\equiv0\pmod n\).

Write \(B_n\) for the number of set partitions of an \(n\)-element set (the Bell number), and put
\[
p=\frac{B_{n-1}}{B_n},\qquad r=\frac{B_{n-2}}{B_n},\qquad C^{(d)}_{ij}=\operatorname{Cov}(I_i,A_j^{(d)}).
\]
The complete cross-covariance matrix is
\[
\boxed{C^{(d)}=(r-p^2)\mathbf1\mathbf1^{\mathsf T}-r(I+P_d),}
\]
where \((P_d)_{ij}=\mathbf1\{i\equiv j+d\pmod n\}\) is a permutation matrix. In particular, an incident singleton–pair covariance equals \(-p^2<0\), whereas a disjoint-site covariance equals \(r-p^2>0\).

The matrix is real circulant, with Fourier eigenvalues
\[
\lambda_0=(n-2)r-np^2<0,\qquad
\lambda_m=-r(1+e^{-2\pi imd/n})\quad(1\le m<n).
\]
Its singular values are \(np^2-(n-2)r\) and \(2r\lvert\cos(\pi md/n)\rvert\), for \(1\le m<n\). With \(g=\gcd(n,d)\),
\[
\boxed{\operatorname{nullity}C^{(d)}=\begin{cases}g,&n/g\text{ even},\\0,&n/g\text{ odd},\end{cases}
\qquad \operatorname{rank}C^{(d)}=n-\operatorname{nullity}C^{(d)}.}
\]
When \(n/g\) is even, the nullspace is spanned by the alternating-sign vectors on each of the \(g\) disjoint cycles of translation by \(d\). Despite the positive correlations at all disjoint sites, the aggregate dependence is strictly negative and independent of displacement:
\[
\boxed{\operatorname{Cov}\left(\sum_i I_i,\sum_j A_j^{(d)}\right)=n\big((n-2)r-np^2\big)<0.}
\]
For example, at \(n=6\), the cross-covariance ranks for displacements \(d=1,2,3\) are respectively \(5,6,3\), although all three displacement statistics have the same mean.

## Assumptions and scope

The sample space consists of all \(B_n\) ordinary (not necessarily noncrossing) partitions of \(\mathbb Z/n\mathbb Z\), with each partition equally likely. The order \(n\) and displacement \(d\) are arbitrary integers satisfying \(n\ge3\) and \(1\le d<n\). The Bell numbers use \(B_0=1\). Every sum over sites is taken modulo \(n\). The cross-covariance is between the \(n\) singleton indicators and the \(n\) oriented pair indicators at one fixed displacement. It is not claimed to describe their full joint distribution or covariance matrices within either family.

## Proof

**Step 1: singleton, pair and joint counts.** Fix distinct sites \(a,b\). Deleting a designated singleton gives a bijection from partitions with \(\{a\}\) a block to partitions on \(n-1\) sites. Contracting a designated pair \(a,b\) into one site gives a bijection from partitions containing them in one block to partitions on \(n-1\) sites. Thus both events have probability \(p\). If site \(i\) equals either endpoint of the pair \(j,j+d\), the two events are incompatible. Otherwise, deleting singleton \(\{i\}\) and contracting the pair \(\{j,j+d\}\) are independent bijective reductions, leaving \(B_{n-2}\) partitions. Hence their joint probability is \(0\) for an incident site and \(r\) for a disjoint site. Since the two endpoints are distinct for every admissible \(d\),
\[
C^{(d)}_{ij}=(r-p^2)-r\big(\mathbf1\{i=j\}+\mathbf1\{i=j+d\pmod n\}\big).
\]
This is precisely the displayed matrix formula.

**Step 2: strict signs, including the constant Fourier mode.** Ordinary Bell numbers are strictly log-convex in the needed range, so \(B_{n-2}B_n>B_{n-1}^2\), equivalently \(r>p^2\). For completeness, Dobinski's formula identifies \(B_k\) with the \(k\)-th moment of a Poisson random variable of mean one; strict Cauchy–Schwarz on its positive support gives this strict inequality. The normalized Bell-number log-concavity bound of Asai–Kubo–Kuo gives, for every \(n\ge2\),
\[
\frac{B_{n-2}B_n}{B_{n-1}^2}\le\frac{n}{n-1}.
\]
Thus
\[
(n-2)r-np^2\le p^2\left(\frac{n(n-2)}{n-1}-n\right)=-\frac{n}{n-1}p^2<0.
\]
Both strict local sign claims and strict negativity of the all-ones eigenvalue follow.

**Step 3: spectrum and nullity.** The vectors \(v^{(m)}=(e^{2\pi imj/n})_{j=0}^{n-1}\) form an orthogonal Fourier basis. The rank-one all-ones operator acts by \(n\) on \(v^{(0)}\) and by zero on all other modes. Since \(P_dv^{(m)}=e^{-2\pi imd/n}v^{(m)}\), the eigenvalues follow. The matrix is normal because it is circulant, so its singular values equal the moduli of these eigenvalues. The constant eigenvalue is strictly nonzero by Step 2. For \(m\ne0\), an eigenvalue vanishes precisely when \(e^{2\pi imd/n}=-1\). Let \(g=\gcd(n,d)\) and \(h=n/g\). The image of the homomorphism \(m\mapsto md\pmod n\) is the subgroup of multiples of \(g\), each attained \(g\) times. The value \(n/2\) occurs in this image exactly when \(h\) is even, and then occurs \(g\) times. This proves the nullity/rank formula. The translation \(j\mapsto j+d\) has \(g\) cycles of length \(h\). For even \(h\), alternating signs around any one cycle give a vector in the kernel of \(I+P_d\) with coordinate sum zero, hence in the kernel of \(C^{(d)}\). These \(g\) independent vectors form a basis by the computed nullity.

**Step 4: aggregate dependence.** Every row sum of the cross-covariance matrix equals \((n-2)r-np^2\). Summing all its entries gives the stated covariance of total singleton and displacement-adjacency counts, which is strictly negative by Step 2. Because the formula contains no displacement, that aggregate covariance is displacement-independent. This completes all claims.

## Verification

Run `python3 check.py` with Python 3 and the standard library. The checker enumerates all unlabeled set partitions through restricted-growth words for every \(3\le n\le9\) and every \(1\le d<n\), checks all singleton, pair and joint event counts, every covariance entry and exact rational matrix rank, and checks the Bell-ratio inequalities for \(3\le n\le99\). In the reviewed package it returned `PASS: 4358 exact assertions`; for \(n=6\) it returned ranks `5,6,3` for \(d=1,2,3\). The program checks finitely many cases only; Steps 1–4 above prove the theorem for all admissible \(n,d\).

## Relationship to prior work

Callan, *On Conjugates for Set Partitions and Integer Compositions* (2005), proves a bijection interchanging the **total number** of singleton blocks and the **total number** of cyclic nearest-neighbor adjacencies, giving equality in distribution of those aggregate counts. Munagi, *On Singletons and Adjacencies of Set Partitions* (2016), extends the count identity to circular displacements \(d\), including the marginal fact that each pair-membership indicator has probability \(p\). These marginal and distributional identities are prior work and are not claimed as new. The present theorem determines the *local cross-covariance matrix*, its exact Fourier/singular spectrum and its displacement-sensitive rank classification. The strict Bell-ratio inequality used in Step 2 is due to Asai–Kubo–Kuo (2001). The result is not a special case of a covariance statement located in the inspected papers; independent historical-priority review is still required.

## Limitations

This is an exact second-order dependence theorem for unrestricted uniform set partitions, not a theorem for noncrossing partitions, weighted partitions or arbitrary exchangeable partition laws. It does not assert that all disjoint indicator families are independent; positive covariance is strictly weaker than independence. It does not determine higher-order joint distributions. A more general, previously published exchangeability or association-scheme theorem could imply this matrix formula; no exhaustive historical-priority guarantee is made. The finite checker does not prove the infinite family and is supplementary to the analytic proof. No independent audit has been performed.

## References

1. David Callan, *On Conjugates for Set Partitions and Integer Compositions*, arXiv:math/0508052, first posted 2005-08-02. https://arxiv.org/abs/math/0508052 ; full text: https://arxiv.org/html/math/0508052v3
2. Augustine O. Munagi, *On Singletons and Adjacencies of Set Partitions*, Rocky Mountain J. Math. 46 (2016), 301–307, doi:10.1216/RMJ-2016-46-1-301. Author-posted full text: https://www.researchgate.net/publication/306144937_On_singletons_and_adjacencies_of_set_partitions
3. Nobuhiro Asai, Izumi Kubo, Hui-Hsiung Kuo, *Bell Numbers, Log-Concavity, and Log-Convexity*, arXiv:math/0104137, first posted 2001-04-12. https://arxiv.org/abs/math/0104137
