# Exact relative numerical-index trichotomy for finite-dimensional Hilbert operators

## Finding

Let \(H_1,H_2\) be nonzero finite-dimensional Hilbert spaces over the same field \(\mathbb K\in\{\mathbb R,\mathbb C\}\). For every norm-one \(G:H_1\to H_2\), define the relative operator seminorm \(p_G\), relative numerical radius \(\nu_G\), and relative numerical index \(n_G^{(2)}\) as specified below. Then the **exact index**, with no restriction on ranks or relative dimensions, is
\[
n_G^{(2)}(H_1,H_2)=
\begin{cases}
1,&\dim H_2=1,\\
\tfrac12,&\mathbb K=\mathbb C,\ \dim H_2\ge2,\ GG^*=I_{H_2},\\
0,&\text{otherwise.}
\end{cases}
\]
Here the middle case means precisely that \(G\) is a coisometry. In particular, **the relative spear identity** \(\nu_G(T)=p_G(T)\) for every \(T\) holds exactly when the codomain has dimension one.

The theorem is underpinned by a pointwise reduction valid for **every** \(T\). Put \(E=\ker(I_{H_1}-G^*G)\), \(F=GE\), and let \(U=G|_E:E\to F\), an isometric isomorphism. Then
\[
p_G(T)=\|T|_E\|,\qquad
\nu_G(T)=w\!\left(U^*P_F T|_E\right),
\]
where \(w\) is the usual Hilbert numerical radius and \(P_F\) is the orthogonal projection onto \(F\). These formulas identify the natural quotient by \(\ker p_G\), even when \(p_G\) is only a seminorm.

If \(\mathbb K=\mathbb C\), \(\dim H_2\ge2\), and \(\dim H_1\ge\dim H_2\), the map from the operator-norm unit sphere of \(\mathcal B(H_1,H_2)\) to its relative index is zero off the coisometries and equals \(1/2\) exactly on them. It is therefore discontinuous at every coisometry. This is not the classical index whose denominator is the full operator norm.

## Assumptions and scope

All dimensions are positive and finite; \(G\in\mathcal B(H_1,H_2)\) has \(\|G\|=1\). Inner products and adjoints use the Hilbert structure. For \(T\in\mathcal B(H_1,H_2)\), put
\[
p_G(T)=\inf_{\delta>0}\sup_{\substack{\|x\|=1\\\|Gx\|>1-\delta}}\|Tx\|,
\]
\[
\nu_G(T)=\inf_{\delta>0}\sup_{\substack{\|x\|=\|y\|=1\\\operatorname{Re}\langle Gx,y\rangle>1-\delta}}
|\langle Tx,y\rangle|,
\qquad n_G^{(2)}=\inf_{p_G(T)=1}\nu_G(T).
\]
The inner-product convention is immaterial because only absolute values appear in the final expressions. The defining constraint is nonempty for each positive \(\delta\). The seminorm and numerical radius may vanish on nonzero operators, and the index is understood in the explicit published sense of normalizing by \(p_G(T)=1\), rather than requiring that \(p_G\) be a norm. The unit sphere \(\{T:p_G(T)=1\}\) is nonempty, for example it contains \(G\).

The classical numerical radius for a square Hilbert operator \(A\) is \(w(A)=\sup_{\|z\|=1}|\langle Az,z\rangle|\). A **coisometry** is an operator satisfying \(GG^*=I_{H_2}\). In particular, a coisometry can exist only when \(\dim H_1\ge\dim H_2\).

## Proof

**1. Exact top-singular-space localization.** Since \(\|G\|=1\) and \(H_1\) is finite-dimensional, the positive contraction \(G^*G\) has eigenvalue one, so \(E\ne\{0\}\). Its eigenspace at one is exactly the set of norming unit vectors for \(G\), together with zero. Indeed,
\[
\|x\|^2-\|Gx\|^2=\langle (I-G^*G)x,x\rangle\ge0,
\]
with equality precisely when \(x\in E\). Compactness of the unit sphere makes each decreasing near-norming supremum converge to the supremum on \(S_E\), giving
\[
p_G(T)=\sup_{\substack{x\in E\\\|x\|=1}}\|Tx\|=\|T|_E\|.
\]

For the relative numerical radius, compactness of both unit spheres shows that the limit constraint is \(\operatorname{Re}\langle Gx,y\rangle=1\). The Cauchy–Schwarz equality condition forces \(\|Gx\|=\|x\|=\|y\|=1\) and \(y=Gx\), with no remaining complex phase because of the real-part constraint. Thus
\[
\nu_G(T)=\sup_{\substack{x\in E\\\|x\|=1}}|\langle Tx,Gx\rangle|.
\]
Since \(U=G|_E\) is an isometry onto \(F=GE\), \(\langle Tx,Ux\rangle=\langle U^*P_FTx,x\rangle\); the claimed compression formula follows.

**2. Orthogonal-output obstruction.** If \(F\ne H_2\), choose unit vectors \(e\in E\) and \(z\in F^\perp\). Define \(T\) on \(E\) by \(Tx=\langle x,e\rangle z\), and set it to zero on \(E^\perp\). Then \(p_G(T)=1\), but \(P_F T|_E=0\), so \(\nu_G(T)=0\). Hence \(n_G^{(2)}=0\) if the top singular range is proper.

**3. Full-range case and exact Hilbert index.** If \(F=H_2\), the isometry \(U:E\to H_2\) is surjective, thus unitary. For \(e\in E\) and \(v\in E^\perp\), the identity \(G^*Ge=e\) gives \(\langle Gv,Ge\rangle=\langle v,G^*Ge\rangle=0\). Thus \(G(E^\perp)\perp F=H_2\), so \(G\) vanishes on \(E^\perp\); for every \(z\in H_2\) one has \(G^*z=U^*z\), hence \(GG^*z=z\). Conversely, if \(GG^*=I_{H_2}\), then \(E=\operatorname{ran}G^*\), and \(G|_E\) is a surjective isometry, so \(F=H_2\). Consequently
\[
F=H_2\quad\Longleftrightarrow\quad GG^*=I_{H_2}.
\]
Every operator \(A:E\to E\) is realized as \(A=U^*T|_E\) by taking \(T|_E=UA\) and \(T|_{E^\perp}=0\). The preceding pointwise formulas then show
\[
\inf_{p_G(T)=1}\nu_G(T)=\inf_{\|A\|=1}w(A)=n(E).
\]
For \(\dim E=1\), \(w(A)=\|A\|\), over either field. For real \(\dim E\ge2\), a norm-one skew-symmetric rotation on a two-dimensional subspace (zero elsewhere) has \(w(A)=0\). For complex \(\dim E\ge2\), the standard polarization estimate \(\|A\|\le2w(A)\) gives \(w(A)\ge\|A\|/2\). To prove sharpness, extend the matrix \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\) by zero to all of \(E\): it has norm one and numerical radius exactly \(1/2\), because \(|\overline z_1z_2|\le(|z_1|^2+|z_2|^2)/2\). These arguments give the displayed trichotomy.

**4. Rigidity, density and jump.** The relative spear identity for every \(T\) is equivalent to \(n_G^{(2)}=1\): if the index is one, homogeneity and \(\nu_G(T)\le p_G(T)\) give equality for all \(T\), including the kernel of the seminorm; the converse is immediate. The trichotomy forces precisely \(\dim H_2=1\). In the complex case with \(m=\dim H_2\ge2\) and \(n=\dim H_1\ge m\), the coisometries form a closed subset of the norm-one operator sphere. They have empty interior: after unitary changes of coordinates any coisometry has \(m\) leading singular values one, and arbitrarily small positive attenuation of only one of these values (leaving another at one) gives a norm-one operator that is not a coisometry. Such matrices are dense in the complement; the complement is also open. Since the relative index takes exactly \(1/2\) on coisometries and zero elsewhere, it is discontinuous at every coisometry and continuous at every non-coisometry. When \(n<m\), coisometries do not exist and the index vanishes identically; when \(m=1\), it is identically one. This establishes the asserted boundaries.

## Verification

The derivation uses the compactness of finite-dimensional unit spheres, the equality case of Cauchy–Schwarz, singular-subspace orthogonality, and the elementary real/complex Hilbert numerical-index values. The source statement reduces to the two explicit compression formulas and the equivalence \(F=H_2\iff GG^*=I_{H_2}\); the proof above checks these without relying on numerical tests.

A standalone standard-library checker, `relative_index_check.py`, gives **6,720 supplementary finite tests**, verifying norming directions, annihilating codomain components, scalar output, real skew rotations, complex nilpotent radius \(1/2\), rectangular coisometry, and near-coisometric perturbations. Run it using `python3 relative_index_check.py`. These finite tests do not certify the quantifiers over all dimensions, fields, or operators; those follow from the analytic proof.

## Relationship to prior work

Dey and Pal, *On the geometry of \(G\)-norm* (arXiv:2603.20796v1), introduced the precise relative-index framework used here. Their Proposition 2.4 establishes finite-dimensional norming-pair localization in general Banach spaces, their Theorem 3.12 proves that finite-dimensional Hilbert relative spear operators must be partial isometries, and Theorem 3.13 treats norming-space reduction under a spectral gap. The present result supplies the full trichotomy, sharp positive value for complex rectangular coisometries, a complete sufficiency classification for relative spear operators, and the discontinuity locus; it does not claim novelty for Proposition 2.4 or the norming-space lemma.

Kadets, Martín, Merí, Pérez and Quero, *On the numerical index with respect to an operator* (arXiv:1905.12257), study the original \(G\)-numerical index with full-operator-norm denominator. In particular, their Hilbert-space discussion proves vanishing in many rectangular settings. Such a conclusion does **not** determine the relative index normalized instead by \(p_G\): a rectangular coisometry has relative index \(1/2\) over \(\mathbb C\) even when its classical full-norm index vanishes. Kadets, Martín, Merí and Quero, *Generating operators between Banach spaces* (arXiv:2306.02645v1), analyze when the relative seminorm equals the full operator norm, a different comparison.

A publicly available result titled *Compact-defect characterization of the essential norm among relative operator seminorms* addresses simultaneous equality with the Calkin norm for infinite-dimensional Hilbert operators; its compact-defect hypothesis and essential-norm conclusion do not imply this finite-dimensional numerical-index classification.

## Limitations

The trichotomy concerns only finite-dimensional Hilbert spaces over \(\mathbb R\) or \(\mathbb C\); it does not extend automatically to infinite dimensions or general Banach spaces. The relative seminorm is generally degenerate, so statements about its index use the explicit normalized-seminorm definition, not an implicit claim that it is a genuine norm on the full operator space. There is no classification here of all perturbations \(T\) attaining the index, nor a quantitative perturbation stability modulus. Prior-work comparisons establish a best-knowledge originality assessment, not publication priority guaranteed against unindexed equivalent results. Independent validation has not been performed.

## References

1. L. K. Dey and S. Pal, *On the geometry of \(G\)-norm*, arXiv:2603.20796v1, publicly submitted March 21, 2026. https://arxiv.org/html/2603.20796v1
2. V. Kadets, M. Martín, J. Merí, A. Pérez and A. Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257, 2019. https://arxiv.org/abs/1905.12257
3. V. Kadets, M. Martín, J. Merí and A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1, publicly submitted June 5, 2023. https://arxiv.org/html/2306.02645v1
4. *Compact-defect characterization of the essential norm among relative operator seminorms*, published mathematical research record. https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-compact-defect-characterization-of-the-essential-norm-among-rela--668d42891382/RESULT.md
