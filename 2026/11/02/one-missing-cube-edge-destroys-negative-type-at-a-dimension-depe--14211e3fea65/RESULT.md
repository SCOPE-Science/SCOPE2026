# One missing cube edge destroys negative type at a dimension-dependent sharp exponent

## Finding

For each integer \(n\ge3\), let \(G_n\) be the unweighted Boolean cube graph \(Q_n\) with exactly one edge deleted; give \(G_n\) its shortest-path metric \(d_n\). Put \(N=2^n\). For \(0<p<1\) and \(1\le k\le n\) define the finite Walsh eigenvalue
\[
\Lambda_{n,k}(p)=\sum_{j=1}^{n}j^p\sum_{h=0}^{k}(-1)^h\binom{k}{h}\binom{n-k}{j-h},
\]
where binomial coefficients outside their natural index range equal zero. Every \(\Lambda_{n,k}(p)\) is strictly negative. Define
\[
R_n(p)=\frac{2(3^p-1)}{2^n}\sum_{k=1}^{n-1}\frac{\binom{n-1}{k}}{-\Lambda_{n,k}(p)}.
\]

**Theorem.** There exists exactly one \(p_n\in(0,1)\) with \(R_n(p_n)=1\). The graph metric has strict \(p\)-negative type for \(0\le p<p_n\), nonstrict \(p_n\)-negative type, and fails \(p\)-negative type for every \(p>p_n\). The critical equality space in the real zero-sum hyperplane has dimension exactly one. Consequently, the minimum affine dimension of a Hilbert realization of the snowflake \(d_n^{p/2}\) is \(N-1\) for \(0\le p<p_n\) and \(N-2\) for \(p=p_n\); no such realization exists for \(p>p_n\). Furthermore,
\[
1>p_3>p_4>p_5>\cdots>0,\qquad\lim_{n\to\infty}p_n=0.
\]
In contrast, the unmodified full Hamming cube has supremal negative-type exponent exactly \(1\) for every \(n\ge2\).

For orientation, \(p_3\approx0.7474072433\), \(p_4\approx0.6477208242\), \(p_5\approx0.5946979926\), and \(p_8\approx0.5226056823\).

## Assumptions and scope

Vertices are binary strings \(x=(x_1,\ldots,x_n)\in\{0,1\}^n\). By cube automorphism, the deleted edge may be taken to be \(\{u,v\}=\{0,e_1\}\), where \(e_1=(1,0,\ldots,0)\). All remaining graph edges have geometric length one. For \(p\ge0\), write \(D_p=[d_n(x,y)^p]_{x,y}\), with diagonal zero also when \(p=0\). Negative type means \(\xi^{\mathsf T}D_p\xi\le0\) for every real \(\xi\) satisfying \(\sum_x\xi_x=0\); strict negative type means strict inequality for every nonzero such \(\xi\). The minimum affine Hilbert dimension refers to realizations satisfying \(\|f(x)-f(y)\|_2^2=d_n(x,y)^p\).

## Proof

**1. Exact metric defect.** For every pair other than \(\{u,v\}\), a Hamming-geodesic survives the deletion. A pair differing in at least two coordinates can order its bit-flips to avoid the removed edge; an adjacent pair other than \(\{u,v\}\) retains its original edge. The two exceptional vertices remain connected by a three-edge path around any square containing the deleted edge, and bipartiteness excludes a two-edge path. Therefore the only changed distance is \(d_n(u,v)=3\), instead of one. If \(H_p=[|x\oplus y|^p]_{x,y}\) denotes the complete Hamming powered-distance matrix and \(\delta=3^p-1\), then
\[
D_p=H_p+\delta(e_ue_v^{\mathsf T}+e_ve_u^{\mathsf T}).
\]

**2. Hamming Walsh spectrum.** The orthonormal characters \(\chi_S(x)=2^{-n/2}(-1)^{\sum_{i\in S}x_i}\) diagonalize \(H_p\), and the eigenvalue at a nonempty character \(S\) is \(\Lambda_{n,|S|}(p)\) above. For \(0<p<1\), the Bernstein integral identity gives
\[
-\Lambda_{n,k}(p)=\frac{p}{\Gamma(1-p)}\int_0^\infty t^{-p-1}(1-e^{-t})^k(1+e^{-t})^{n-k}\,dt>0
\quad(1\le k\le n).
\]
Thus \(-H_p\) is positive definite on the zero-sum subspace. At \(p=0\), each nonconstant eigenvalue is \(-1\). At \(p=1\), elementary Fourier summation gives \(\Lambda_{n,1}(1)=-2^{n-1}\) and \(\Lambda_{n,k}(1)=0\) for \(k\ge2\).

**3. Exact rank-one obstruction.** Let \(P=I-N^{-1}\mathbf1\mathbf1^{\mathsf T}\) be the orthogonal projection onto zero-sum vectors, and define
\[
w=e_u+e_v-2N^{-1}\mathbf1,\qquad z=e_u-e_v.
\]
On that subspace,
\[
P(e_ue_v^{\mathsf T}+e_ve_u^{\mathsf T})P=\frac12(ww^{\mathsf T}-zz^{\mathsf T}).
\]
The reflection \(x\mapsto x\oplus e_1\) splits the zero-sum subspace into even characters \(S\) not containing coordinate one (with the constant excluded) and odd characters containing it. The vector \(w\) belongs to the even subspace; \(z\) belongs to the odd subspace. Hence the perturbation is negative semidefinite on the odd subspace, while the even block is the positive rank-one perturbation \(H_p+\delta ww^{\mathsf T}/2\). By the rank-one positive-definiteness criterion, it is negative semidefinite exactly when
\[
\frac\delta2\langle w,(-H_p|_{\mathrm{even}})^{-1}w\rangle\le1.
\]
Since \(\langle w,\chi_S\rangle=2/\sqrt N\) for each nonempty \(S\subseteq\{2,\ldots,n\}\), the left side is exactly \(R_n(p)\). In particular, equality produces exactly one zero direction, and there is no other zero direction at the threshold.

**4. Existence and uniqueness of the exponent.** As \(p\downarrow0\), all nonconstant Walsh eigenvalues tend to \(-1\) and \(R_n(p)\to0\). As \(p\uparrow1\), the summand at \(k=n-1\ge2\) diverges because \(\Lambda_{n,n-1}(p)\uparrow0\) in value, while \(3^p-1\to2\); thus \(R_n(p)\to\infty\). Continuity yields at least one root. At every root, negative type holds with a nonzero equality direction. The strict-negative-type propagation theorem of Li and Weston says that if a metric has \(q\)-negative type, then it has strict \(p\)-negative type for every \(p<q\). Therefore a second, larger root is impossible; nor can negative type return above the first. The standard negative-type interval property excludes all exponents above \(1\) once the threshold below \(1\) has been reached. This proves the exact classification.

**5. Critical equality and Hilbert rank.** An explicit generator of the one-dimensional critical equality space is
\[
\eta_n(x)=\frac2N\sum_{\varnothing\ne S\subseteq\{2,\ldots,n\}}\frac{(-1)^{\sum_{i\in S}x_i}}{-\Lambda_{n,|S|}(p_n)}.
\]
It is the inverse-Walsh image of \(w\), so it has zero sum, is independent of \(x_1\), and satisfies \(P D_{p_n}\eta_n=0\). Moreover \(\eta_n(u)=\eta_n(v)=1/(3^{p_n}-1)>0\). The Schoenberg centered Gramian \(-P D_pP/2\) is strictly positive on the zero-sum space below \(p_n\), and has precisely one zero eigenvalue there at \(p_n\). Its rank is therefore respectively \(N-1\) and \(N-2\), establishing the stated minimum affine Hilbert dimensions.

**6. Strict decrease with cube dimension.** For \(n\ge3\), the copies of \(G_n\) obtained inside \(G_{n+1}\) by fixing coordinate two to zero and by fixing coordinate three to zero are both isometric: their pair distances equal those in the smaller edge-deleted cube by step 1. Consequently \(p_{n+1}\le p_n\). Suppose equality held. Extend the critical equality vector from each of these two faces by zero outside the face. Both would be zero-sum equality vectors for the larger graph. They are linearly independent: the critical vector of \(G_n\) is invariant under permutations of coordinates other than the first, has positive values at both exceptional endpoints, and must have a nonzero value outside those endpoints because its total sum vanishes; hence for every nonexceptional coordinate it is nonzero somewhere with that coordinate equal to one. The two zero extensions therefore have distinct supports. But step 3 says the larger graph has only one critical zero direction. Contradiction. Hence \(p_{n+1}<p_n\).

**7. Collapse of the exponent at large dimension.** Fix \(0<p<1\). For every \(k\ge n/2\), the integral representation in step 2 satisfies
\[
0<-\Lambda_{n,k}(p)\le \frac{p}{\Gamma(1-p)}\int_0^\infty t^{-p-1}(1-e^{-2t})^{n/2}\,dt=:I_n(p).
\]
For \(n\ge4\), the integrand is dominated by \(t^{-p-1}(1-e^{-2t})^2\), which is integrable at zero and infinity. Dominated convergence gives \(I_n(p)\to0\). On the other hand, the proportion \(2^{1-n}\sum_{k=\lceil n/2\rceil}^{n-1}\binom{n-1}{k}\) tends to \(1/2\). Thus the defining expression obeys \(R_n(p)\ge (3^p-1)\bigl(2^{1-n}\sum_{k=\lceil n/2\rceil}^{n-1}\binom{n-1}{k}\bigr)/I_n(p)\to\infty\). For every fixed positive \(p<1\), the edge-deleted cube eventually fails \(p\)-negative type, so \(p_n\to0\).

## Verification

The standalone `verify.py` independently reconstructs shortest-path distances by breadth-first search, computes the Walsh scalar equation at 65-digit working precision, and compares complete centered powered-distance spectra with the predicted transition for dimensions three through seven. It additionally verifies the critical Fourier equality vector and lists numerical roots through dimension eight. Its replay returned `PASS supplementary assertions: 88343`. These finite checks do not establish the all-dimensional theorem or the limiting assertion; those follow from the preceding proof.

## Relationship to prior work

The finite-metric negative-type interval and strictness principles are due to the established theory of negative type, including Li and Weston. Robertson (first preprint 2020-04-23) develops general determinant/Gramian formulas for supremal generalized roundness. Doust, Robertson, Stoneham and Weston (first preprint 2020-05-19) analyze distance matrices of **metric subsets** of the unmodified Hamming cube, while Doust and Wolf (2021-09-15) study inverse-distance geometry for those same Hamming-subset metrics. Those results do not directly apply as Hamming-subset formulas to the modified graph metric here: the specific pair \(u,v\) is three units apart rather than one. Berleant and collaborators (2021-12-13) study embeddings of graphs into products of Hamming graphs, a different isometric target and a different invariant. The present classification uses a defect-specific rank-one Walsh reduction and adds a strict dimension law and a vanishing asymptotic threshold. General finite-metric algorithms alone do not explicitly state these identities. An unlocated equivalent special-case calculation under alternative embedding terminology remains a priority risk.

## Limitations

The result concerns finite binary cubes with precisely one deleted edge, the unweighted graph-path metric, real negative-type inequalities, and exact Hilbert embeddings of its snowflakes. It does not classify simultaneous multiple-edge faults or weighted faults. The threshold is given by a uniquely specified finite spectral equation rather than an elementary closed form. The numerical values and the checker are corroborating computations, not exhaustive proofs for unbounded dimension. Independent external validation has not been performed.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first public 2009-01-06), https://arxiv.org/abs/0901.0695.
2. G. Robertson, *The maximal generalised roundness of finite metric spaces*, arXiv:2004.10923 (first public 2020-04-23), https://arxiv.org/abs/2004.10923.
3. I. Doust, G. Robertson, A. Stoneham, and A. Weston, *Distance matrices of subsets of the Hamming cube*, arXiv:2005.09205 (first public 2020-05-19), https://arxiv.org/abs/2005.09205.
4. I. Doust and R. Wolf, *A problem on distance matrices of subsets of the Hamming cube*, arXiv:2109.07052 (first public 2021-09-15), https://arxiv.org/abs/2109.07052.
5. J. Berleant, K. Sheridan, A. Condon, V. Vassilevska Williams, and M. Bathe, *Isometric Hamming embeddings of weighted graphs*, arXiv:2112.06994 (first public 2021-12-13), https://arxiv.org/abs/2112.06994.
