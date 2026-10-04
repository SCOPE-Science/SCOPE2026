# The compression component of \(3\times 3\) matrix nets has Plücker degree \(927\)
## Finding
For \(A=B=\mathbf C^3\), let \(\mathcal C\subset\operatorname{Gr}(3,A\otimes B)\) denote the compression component of matrix nets: its points are the three-dimensional subspaces \(K\) for which there exist \(U\in\operatorname{Gr}(2,A)\) and \(V\in\operatorname{Gr}(2,B)\) with \(K\subset U\otimes V\) and \(\dim K=3\). Then the degree of \(\mathcal C\) in the Plücker embedding is
\[
\deg(\mathcal C)=927.
\]
Equivalently, seven general Plücker hyperplanes meet \(\mathcal C\) in a zero-dimensional scheme of length \(927\).

## Assumptions and scope
The ground field is \(\mathbf C\). The component \(\mathcal C\) is the smooth-conic compression component identified by Dinh--Ho--Le--Vuong: if
\[
\mathbf B=\operatorname{Gr}(2,A)\times\operatorname{Gr}(2,B)\cong\mathbf P^2\times\mathbf P^2
\]
and \(\mathcal U,\mathcal V\) are the tautological rank-two bundles, then their construction identifies
\[
\mathcal C\cong X:=\mathbf P((\mathcal U\otimes\mathcal V)^*)
\]
with the point \((U,V,[\ell])\) mapped to \(K=\ker(\ell:U\otimes V\to\mathbf C)\). This gives \(\dim X=4+3=7\), so the seventh power of the pulled-back Plücker hyperplane class computes the degree.

## Proof
Write \(h,k\) for the hyperplane classes of the two factors of \(\mathbf B\cong\mathbf P^2\times\mathbf P^2\). Thus
\[
\operatorname{CH}^*(\mathbf B)=\mathbf Z[h,k]/(h^3,k^3),\qquad \int_\mathbf B h^2k^2=1.
\]
For the tautological rank-two bundles,
\[
c(\mathcal U)=1-h+h^2,\qquad c(\mathcal V)=1-k+k^2.
\]
Set \(F=(\mathcal U\otimes\mathcal V)^*\), a rank-four bundle, and let \(\pi:X=\mathbf P(F)\to\mathbf B\) use the convention that \(\mathbf P(F)\) parametrizes lines in \(F\). Put \(\xi=c_1(\mathcal O_X(1))\).

The line \(\mathcal O_X(-1)\subset\pi^*F\) is the universal functional. Dualizing its inclusion gives a surjection
\[
\pi^*(\mathcal U\otimes\mathcal V)\longrightarrow\mathcal O_X(1)
\]
whose kernel \(\mathcal S\) is the rank-three subbundle corresponding to the net \(K\). Hence
\[
0\longrightarrow\mathcal S\longrightarrow\pi^*(\mathcal U\otimes\mathcal V)\longrightarrow\mathcal O_X(1)\longrightarrow0.
\]
The Plücker line bundle is \(\det(\mathcal S^*)\), so its first Chern class on \(X\) is
\[
H=c_1(\det\mathcal S^*)=\xi+c_1(F)=\xi+2h+2k.
\]

By the splitting principle, the Chern classes of \(F\) in \(\operatorname{CH}^*(\mathbf B)\) are
\[
\begin{aligned}
c_1(F)&=2h+2k,\\
c_2(F)&=3h^2+3hk+3k^2,\\
c_3(F)&=3h^2k+3hk^2,\\
c_4(F)&=0.
\end{aligned}
\]
The fourth class vanishes after imposing \(h^3=k^3=0\). Inverting \(c(F)\) gives
\[
\begin{aligned}
s_0(F)&=1,\\
s_1(F)&=-2h-2k,\\
s_2(F)&=h^2+5hk+k^2,\\
s_3(F)&=-3h^2k-3hk^2,\\
s_4(F)&=3h^2k^2.
\end{aligned}
\]
For a rank-four line-projective bundle, \(\pi_*(\xi^{3+i})=s_i(F)\). Therefore
\[
\deg(\mathcal C)=\sum_{i=0}^4 \binom{7}{3+i}\int_{\mathbf B}(2h+2k)^{4-i}s_i(F).
\]
Taking the coefficient of \(h^2k^2\) gives the five contributions
\[
3360,\ -3360,\ 1008,\ -84,\ 3,
\]
whose sum is \(927\). This proves the claim.

## Verification
The bundled `verify.py` recomputes the Chow-ring calculation using integer arithmetic in \(\mathbf Z[h,k]/(h^3,k^3)\). It follows two routes. The first derives the Segre classes recursively from \(s(F)c(F)=1\) and applies the projective-bundle pushforward formula. The second expands \(H^7\) in \(\mathbf Z[h,k,\xi]\), reduces powers of \(\xi\) using
\[
\xi^4+c_1(F)\xi^3+c_2(F)\xi^2+c_3(F)\xi+c_4(F)=0,
\]
and then extracts the coefficient that survives pushforward. Both routes return \(927\); `verification_output.txt` records `VERIFY_OK`.

## Relationship to prior work
Dinh--Ho--Le--Vuong, arXiv:2609.09675v1, identify \(\mathcal C\) as the projective bundle above and prove its smoothness and dimension as part of their classification of matrix nets with positive-dimensional rank-one locus. Their result supplies the geometric presentation used here; the Plücker degree is not part of the stated component invariants in the inspected text.

Chan--Ilten, *Fano schemes of determinants and permanents*, Algebra & Number Theory 9 (2015), study compression components of Fano schemes of determinantal varieties. Their Theorem 4.7 computes degrees of loci of maximal compression spaces, while their Table 4 shows that the compression components of \(F_2(D^3_{3,3})\) have dimensions \(11,10,11\). Those loci are therefore not this seven-dimensional projective-bundle locus of nets supported in a \(2\times2\) tensor block. Breiding--Santarsiero, arXiv:2402.12217v1, compute degrees of ordinary tensor subspace varieties in projective tensor space; their objects are tensors of bounded multilinear rank, not three-dimensional subspaces in a Grassmannian under the Plücker embedding.

## Limitations
The calculation is only for the \(3\times3\) compression component \(\mathcal C\). It does not give the Plücker degrees of the other two components in the Dinh--Ho--Le--Vuong classification, nor a formula for arbitrary \(a,b\). The literature comparison was targeted rather than exhaustive: general intersection-theoretic formulas could specialize to the same number even when they do not name this component. No claim of priority beyond the stated searches is made.

## References
1. T. H. Dinh, M. T. Ho, C. T. Le, T. D. Vuong, *Determinantal Kernel Schemes of Matrix Nets and Applications to Positive Maps*, arXiv:2609.09675v1 (2026).
2. M. Chan, N. Ilten, *Fano schemes of determinants and permanents*, Algebra & Number Theory 9 (2015), 627--678.
3. P. Breiding, P. Santarsiero, *Degree of the subspace variety*, arXiv:2402.12217v1 (2024).
