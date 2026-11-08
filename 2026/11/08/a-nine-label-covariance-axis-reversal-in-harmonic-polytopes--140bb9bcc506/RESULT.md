# A nine-label covariance-axis reversal in harmonic polytopes

## Finding
For every integer \(n\ge2\), let \(H_{n,n}\subset\mathbb R^n\times\mathbb R^n\) be the harmonic polytope in the standard Ardila--Escobar realization,
\[
H_{n,n}=(\Pi_n\times\Pi_n)+\operatorname{conv}\{e_i+f_i:1\le i\le n\},
\]
where \(\Pi_n\) is the permutohedron of coordinate permutations of \((1,\ldots,n)\), and \(e_i,f_i\) are the standard basis vectors of the respective blocks. Choose \((X,Y)\) uniformly from its **distinct vertices**, not from its volume measure or from pairs of permutations chosen uniformly without a distinguished label. Put
\[
h_n=\sum_{j=1}^{n}\frac1j,\qquad
v_n=\frac{n^2-1}{12}+1+\frac2n-\frac1{n^2}-\frac2{h_n},
\]
\[
c_n=\frac{(3n-1)(n+2)}{2n^2}-\frac{n+11}{4h_n}.
\]
Then \(\mathbb E X_i=\mathbb E Y_i=(n+1)/2+1/n\), and for all \(i,j\in[n]\),
\[
\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(Y_i,Y_j)=
\begin{cases}v_n,&i=j,\\-v_n/(n-1),&i\ne j,\end{cases}
\]
\[
\operatorname{Cov}(X_i,Y_j)=
\begin{cases}c_n,&i=j,\\-c_n/(n-1),&i\ne j.\end{cases}
\]
The full \(2n\)-by-\(2n\) covariance matrix has two zero eigenvalues in the directions \((\mathbf1,0)\) and \((0,\mathbf1)\), and exactly two positive spectral sectors,
\[
\boxed{\lambda_{\mathrm{sym}}=\frac{n}{n-1}(v_n+c_n),\quad
\lambda_{\mathrm{anti}}=\frac{n}{n-1}(v_n-c_n)}
\]
with multiplicity \(n-1\) **each**. Their eigenspaces are respectively the symmetric contrasts \(\{(u,u):u\perp\mathbf1\}\) and antisymmetric contrasts \(\{(u,-u):u\perp\mathbf1\}\).

The ordering reverses exactly once across integer dimensions:
\[
\boxed{\lambda_{\mathrm{sym}}>\lambda_{\mathrm{anti}}\quad(2\le n\le8),
\qquad
\lambda_{\mathrm{anti}}>\lambda_{\mathrm{sym}}\quad(n\ge9).}
\]
There is no tied case. At the transition,
\[
c_8=\frac{2395}{48704}>0,\qquad c_9=-\frac{1153}{577449}<0.
\]
Moreover, the intrinsic covariance condition number tends to one at the quantitative rate
\[
\boxed{\kappa_n=\frac{\lambda_{\max}}{\lambda_{\min}^{+}}
=1+\frac{6}{n\log n}+o\!\left(\frac1{n\log n}\right).}
\]
Thus the absolute difference of the two nonzero eigenvalues grows asymptotically like \(n/(2\log n)\), even as their relative difference vanishes.

## Assumptions and scope
The Euclidean metric is that inherited from \(\mathbb R^{2n}\). The harmonic polytope is the concrete Minkowski sum above, not an arbitrarily affinely equivalent realization. Every fine harmonic triple labels a distinct vertex, and the uniform measure is on those vertices. The affine dimension is \(2n-2\) for \(n\ge2\), as proved by Ardila and Escobar. The labels \(i\) are simultaneously permuted in the two blocks. All limiting statements are as the integer \(n\to\infty\). No claim is made about covariance under uniform interior volume or surface area.

## Proof
**1. Exact vertex parametrization.** Ardila--Escobar, Proposition 3.6, gives every vertex as
\[
(\pi_1^{-1}+e_k,\pi_2^{-1}+f_k),
\]
where \(\pi_1,\pi_2\) are permutations of \([n]\) and \(k\) is maximal in the product order of their position vectors. The source's fine-harmonic-triple count is \((n!)^2h_n\). Fixing the first permutation's rank order, denote by \(\sigma_j\) the second rank of the label with first rank \(j\). The allowable distinguished positions \(j\) are precisely the right-to-left records \(\sigma_j>\max_{r>j}\sigma_r\). For a uniform random relative permutation \(\sigma\), the chance that position \(j\) is such a record is \(1/(n-j+1)\). Consequently the size-biased distribution of the relative permutation plus its distinguished record is normalized by \(h_n\). Independent uniform relabeling recovers uniform sampling over all fine triples.

**2. Rank and marking moments.** Let \(R_i\) and \(S_i\) be the two ranks of a fixed label \(i\) and \(J_i=\mathbf1_{\{i=k\}}\). Uniform relabeling makes each individual rank uniform on \(\{1,\ldots,n\}\), \(\mathbb E J_i=1/n\), and \(\mathbb E(R_i)=\mathbb E(S_i)=(n+1)/2\). Write \(t=n-j+1\). The first rank of a distinguished record has mean
\[
\mathbb E R_k=\frac{\sum_{t=1}^n(n-t+1)/t}{h_n}
=n+1-\frac{n}{h_n}.
\]
Therefore
\[
\operatorname{Cov}(R_i,J_i)=\operatorname{Cov}(S_i,J_i)
=\frac{n+1}{2n}-\frac1{h_n},
\qquad
\operatorname{Var}(J_i)=\frac{n-1}{n^2}.
\]
For the cross-rank moment put \(T(\sigma)=\sum_{j=1}^{n}j\sigma_j\). On conditioning that the position \(j\), with suffix length \(t\), is a right-to-left record, exchangeability of the random suffix values gives
\[
\mathbb E(\sigma_j\mid\text{record})=\frac{t(n+1)}{t+1},
\qquad
\mathbb E(\sigma_r\mid\text{record})=
\frac{t(n+1)}{2(t+1)}\quad(r>j),
\]
while the conditional mean at every \(r<j\) is \((n+1)/2\). Hence, including \(t=1\) (for which the second conditional formula is vacuous),
\[
\mathbb E(T\mid\text{record at }j)
=\frac{n(n+1)^2}{4}
-\frac{(n+1)t(t-1)}{4(t+1)}.
\]
Under the marked-record law, divide the sum over \(j\) of these conditional expectations weighted by \(1/t\) by \(h_n\). As each label's rank-pair average equals \(T/n\), one gets
\[
\operatorname{Cov}(R_i,S_i)
=-\frac{n+1}{4nh_n}\sum_{t=1}^n\frac{t-1}{t+1}
=-\frac{n+1}{4nh_n}\left(n+2-2h_{n+1}\right)
=\frac{n+1}{2n}-\frac{n+3}{4h_n}.
\]
The last equality uses \(h_{n+1}=h_n+1/(n+1)\).

**3. Covariance and eigenspaces.** Since \(X_i=R_i+J_i\) and \(Y_i=S_i+J_i\), adding the computed moments gives exactly \(v_n=\operatorname{Var}(X_i)\) and \(c_n=\operatorname{Cov}(X_i,Y_i)\) in the finding. Their means equal \((n+1)/2+1/n\). Each vertex has the two constant coordinate sums \(\sum X_i=\sum Y_i=n(n+1)/2+1\). Permuting labels simultaneously is transitive on same-block off-diagonal coordinate pairs and on cross-block unequal-label pairs, so the constant-sum identities force all such covariances to be respectively \(-v_n/(n-1)\) and \(-c_n/(n-1)\). On \(\mathbf1^{\perp}\oplus\mathbf1^{\perp}\), the covariance is \(n/(n-1)\) times the \(2\)-by-\(2\) matrix with diagonal \(v_n\) and off-diagonal \(c_n\). Diagonalizing the two block-swapping eigenspaces proves both eigenvalues and their multiplicities. Since the vertices affinely span a \((2n-2)\)-dimensional polytope, these eigenvalues are strictly positive.

**4. Strict nine-label transition.** Write
\[
c_n=r_n-\frac{n+11}{4h_n},\qquad
r_n=\frac32+\frac{5}{2n}-\frac1{n^2}.
\]
The positive rational term \(r_n\) strictly decreases for integers \(n\ge2\). Also
\[
\frac{n+12}{h_{n+1}}>\frac{n+11}{h_n}
\iff
h_n>\frac{n+11}{n+1}.
\]
The latter is true at \(n=6\) because \(h_6=49/20>17/7\), and remains true afterward because the left side increases and the right side decreases. Thus \(c_n\) strictly decreases for \(n\ge6\). Direct exact substitution shows \(c_n>0\) for each \(2\le n\le8\); the endpoint values \(c_8\) and \(c_9\) above prove \(c_n<0\) for every \(n\ge9\). Since the eigenvalue difference has the sign of \(c_n\), the asserted ordering and absence of ties follow.

**5. Asymptotic.** The standard harmonic estimate \(h_n=\log n+\gamma+O(1/n)\) gives \(v_n=n^2/12+O(1)\) and \(c_n=-n/(4\log n)(1+o(1))\). Therefore \(\lambda_{\mathrm{anti}}-\lambda_{\mathrm{sym}}=-2nc_n/(n-1)\sim n/(2\log n)\) for large \(n\), and expanding \((v_n-c_n)/(v_n+c_n)\) gives the stated condition-number asymptotic.

## Verification
Execute `python3 artifacts/verify.py` from the extracted package directory. Using only the Python standard library, it independently enumerates all distinct fine-harmonic-triple vertices for \(n=2,3,4,5\), respectively \(6,66,1200,32880\) vertices; accumulates every coordinate of the exact rational \(2n\)-by-\(2n\) covariance matrix; and compares every entry against the claimed formula. It also checks positivity and the phase signs using exact fractions for \(2\le n\le300\) and checks the exact transition fractions. The observed success marker is `HARMONIC_COVARIANCE_CHECKS_PASSED vertices=34152 profiles=299`. These finite checks are corroborative only; the proof for all \(n\) is symbolic.

## Relationship to prior work
Ardila and Escobar determined the harmonic polytope's normal fan, fine harmonic triples, vertex and facet descriptions, and volume. The vertex formula and count are the indispensable inputs to the present calculation, but that source does not present a vertex-uniform covariance tensor or the symmetric/antisymmetric spectral transition. Ardila's bipermutahedron is a related but different polytope; its face enumeration and deformation theory do not imply the stated vertex-measure covariance.

Existing mathematical records for the harmonic polytope determine its concentric vertex shells and circumsphere, its Euclidean inball, and its local graph degrees. Shell radii constrain only the trace of a covariance matrix, not the two separate symmetric and antisymmetric eigenvalues or the sign reversal of the cross-block covariance. Inball and graph-degree formulas likewise do not imply this distributional second-moment classification.

Searches for vertex covariance, inertia, principal axes, rank correlations, harmonic triples, and equivalent permutation-record moment formulations found no prior statement of the two exact eigenvalues with the strict \(n=9\) reversal. This is a provisional priority assessment, not a guarantee that no earlier equivalent moment formula exists.

## Limitations
The result concerns equally weighted distinct vertices and the source's fixed Euclidean realization, not Euclidean volume sampling. It uses the primary paper's characterization of harmonic triples, not an independent proof of that source's polyhedral description. Large integer orders are covered analytically, not by finite enumeration. An equivalent theorem expressed as the covariance of a marked Pareto-maximum permutation-pair process, rather than as polytope geometry, remains the principal historical-priority risk.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, publicly submitted 2020-06-04; Selecta Mathematica 27 (2021), article 91, DOI 10.1007/s00029-021-00687-6. The vertex description and counting argument appear in Propositions 3.5--3.6.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, publicly submitted 2020-08-05; Combinatorial Theory 2(3) (2022).
3. *Harmonic-polytope vertices form exactly n Euclidean shells*, published mathematical result, October 2026, record f2f2da42b2f8.
4. *Exact Euclidean inradius and incenter transition of the harmonic polytope*, published mathematical result, October 2026, record 81e898ba9eb4.
5. *Simple vertices and local degree of the harmonic polytope*, published mathematical result, October 2026, record 8017b01864fe.
