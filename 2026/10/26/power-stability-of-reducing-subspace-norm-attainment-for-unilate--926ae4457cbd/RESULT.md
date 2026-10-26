# Power stability of reducing-subspace norm attainment for unilateral weighted shifts

## Finding

Let \(H=\ell^2(\mathbb N_0)\), let \(w=(w_j)_{j\ge0}\) satisfy \(0<w_j\le M<\infty\), and define \(Se_j=w_je_{j+1}\). Let \(\beta(H)\) denote the set of bounded operators that attain their norm upon restriction to **every nonzero closed reducing subspace**. For integers \(n\ge1\), \(0\le r<n\), and \(k\ge0\), put
\[
a_{r,k}^{(n)}=\prod_{j=0}^{n-1}w_{r+nk+j}.
\]
Then the following is an exact criterion, with no convergence hypothesis on the weights:
\[
\boxed{\ S^n\in\beta(H)\quad\Longleftrightarrow\quad
\forall r\in\{0,\ldots,n-1\}\ \exists k\ge0:\ 
a_{r,k}^{(n)}=\sup_{\ell\ge0}a_{r,\ell}^{(n)}.\ }
\]
In particular, the set of powers belonging to \(\beta(H)\) need not be an initial segment or upward closed: it is possible that \(S\in\beta(H)\) but \(S^n\notin\beta(H)\) for *all* \(n\ge2\), and possible that \(S\notin\beta(H)\) yet \(S^2\in\beta(H)\).

There is a precise stability boundary for hyponormal positive-weight shifts. Such a shift belongs to \(\beta(H)\) if and only if the weights become constant from some index onward. In this case every \(S^n\) lies in the stronger class \(\beta_0(H)=\{A:|A|\in\beta(H)\}\).

## Assumptions and scope

The Hilbert space is complex and separable, the shift is unilateral with all weights strictly positive and uniformly bounded, and every power exponent is a positive integer. The phrase *reducing subspace* means invariant under both the operator and its adjoint. No monotonicity, bounded-below condition, compactness, or limit of the weights is assumed in the main criterion. Hyponormality is used only in the final stability statement. This theorem is about norm **attainment on all reducing subspaces**, not about numerical radii, essential norms, or ordinary norm attainment alone.

## Proof

**1. Residue decomposition.** Fix \(n\ge1\). For each \(0\le r<n\), the space
\[
H_r=\overline{\operatorname{span}}\{e_{r+nk}:k\ge0\}
\]
reduces \(S^n\), and \(H=\bigoplus_{r=0}^{n-1}H_r\). Under the standard basis identification of \(H_r\) with \(\ell^2(\mathbb N_0)\), the restriction \(S^n|_{H_r}\) is the unilateral shift \(V_r\) with weights \(a_{r,k}^{(n)}>0\).

**2. Each residue shift is irreducible.** If \(V\) is any unilateral weighted shift whose weights are all nonzero, then \(\ker V^*=\mathbb Ce_0\), and the orbit of \(e_0\) under \(V\) spans a dense subspace. If an orthogonal projection \(P\) commutes with both \(V\) and \(V^*\), then \(Pe_0\in\ker V^*\). Since \(P\) is a projection, \(Pe_0\) is either \(0\) or \(e_0\). Commutation with \(V\) and cyclicity give \(P=0\) or \(P=I\). Thus \(V\) has no nontrivial reducing subspace.

For an arbitrary positive-weight shift \(V e_k=v_ke_{k+1}\), the norm is \(\|V\|=\sup_k v_k\); moreover \(V\) attains this norm if and only if one of its weights equals that supremum. Indeed,
\[
\|Vx\|^2=\sum_k v_k^2|x_k|^2\le(\sup_k v_k)^2\|x\|^2.
\]
If no individual weight is maximal, the inequality is strict for every nonzero vector. If one is maximal, its basis vector attains the norm.

**3. Why the finite residue test controls every reducing subspace.** It is necessary that each \(V_r\) attain its norm because \(H_r\) reduces \(S^n\). For sufficiency, consider the finite direct sum of the irreducible shifts \(V_r\). Let \(X\) intertwine two such shifts and their adjoints. Then \(X^*X\) commutes with both members of the first shift's adjoint pair, and \(XX^*\) commutes with both members of the second. Irreducibility implies these positive operators are scalar. If \(X\ne0\), it is therefore a nonzero scalar multiple of a unitary intertwiner. Consequently, intertwiners vanish between inequivalent irreducible summands, while on any block of \(m\) mutually equivalent summands the commutant of the operator and adjoint is precisely \(M_m(\mathbb C)\otimes I\). Hence every nonzero reducing subspace of \(S^n\) is unitarily equivalent to a finite orthogonal sum of copies of some of the \(V_r\). If each residue shift attains its norm, that finite direct sum also attains its norm: its norm is the largest of finitely many attained component norms. This proves the equivalence. The argument does **not** assume that the residue shifts are pairwise inequivalent.

**4. Destruction of attainment at every higher power.** Take
\[
w_0=\frac32,\qquad w_j=\frac{j}{j+1}\quad(j\ge1).
\]
The shift \(S\) is irreducible and \(\|S\|=3/2\), attained at \(e_0\); thus \(S\in\beta(H)\). For \(n\ge2\), consecutive products are
\[
\prod_{j=0}^{n-1}w_j=\frac{3}{2n}<1,\qquad
\prod_{j=i}^{i+n-1}w_j=\frac{i}{i+n}<1\quad(i\ge1).
\]
The products with initial index \(i\ge1\) approach \(1\) as \(i\to\infty\), so \(\|S^n\|=1\) is never attained. In particular \(S^n\notin\beta(H)\) for every \(n\ge2\).

**5. Recovery of attainment upon squaring.** Define another shift \(R\) by
\[
w_0=w_1=w_2=\frac9{10},\qquad
w_{2k+1}=\frac1{10}\ (k\ge1),\qquad
w_{2k}=1-\frac1{k+3}\ (k\ge2).
\]
All weights are positive and smaller than \(1\), while the even subsequence tends to \(1\); hence \(\|R\|=1\) is not attained and \(R\notin\beta(H)\). For \(R^2\), both residue shifts have initial weight \((9/10)^2=81/100\); every subsequent weight is a product containing at least one factor \(1/10\), hence is at most \(1/10\). The two residue shifts therefore attain their norms at their initial basis vectors. The criterion gives \(R^2\in\beta(H)\).

**6. Rigidity in the hyponormal class.** A positive-weight unilateral shift \(S\) is hyponormal precisely when \(w_k\le w_{k+1}\) for all \(k\), since \(S^*S-SS^*\) is diagonal with entries \(w_0^2\) and \(w_k^2-w_{k-1}^2\) for \(k\ge1\). Irreducibility and Step 2 imply that \(S\in\beta(H)\) precisely when its nondecreasing bounded weight sequence actually reaches its supremum. That happens precisely when it becomes constant. Then for any \(n\), all sufficiently late consecutive \(n\)-fold products equal one fixed number; the diagonal operator \(|S^n|\) therefore has only finitely many distinct eigenvalues and is a pure-point operator. On each of its reducing subspaces its norm is attained at an eigenvector for the largest eigenvalue present. Therefore \(|S^n|\in\beta(H)\), or \(S^n\in\beta_0(H)\), for every \(n\ge1\).

## Verification

The companion standalone `verify.py` checks exact rational telescoping identities for the first example, the two residue maxima in the second, and coefficient-wise power-to-residue decomposition for dozens of randomly sampled finite shift matrices. Running `python verify.py` yields **PASS: 11538 exact rational checks**. These finite tests support the explicit formulas; none replaces the universal operator-theoretic argument in Steps 1–3 or the analytic limiting arguments in Steps 4–6.

## Relationship to prior work

The operator class \(\beta(H)\) was introduced and studied by Ramesh and Osaka (2021, 2022). Su and Zhang (first publicly posted September 29, 2026) analyze density and stability of \(\beta(H)\) and its modulus-defined subclass \(\beta_0(H)\), primarily under finite-rank and compact perturbations; their weighted-shift example concerns failure of passage to the modulus. Golla, Osaka, and Sequeira (first posted October 9, 2026) establish structural results for hyponormal and quasinormal operators in \(\beta(H)\) and give other weighted-shift examples. The present result addresses an additional stability operation, **taking powers**, with an all-exponents arithmetic test and genuinely opposite membership transitions. A previously indexed weighted-shift power-profile result concerns prescribed operator/essential *norms*, not norm **attainment on all reducing summands**.

## Limitations

Strict positivity of every weight is needed for irreducibility of the residue shifts; zeros require a different reducing-subspace analysis. The criterion does not classify arbitrary bounded operators or products of two different shifts. Although the literature inspection found no implication-equivalent power classification, older or unindexed operator-attainment literature may contain an equivalent result; independent publication-priority validation has not been performed. The finite checks do not certify an infinite-dimensional theorem, and no independent scientific audit has been performed.

## References

- Z. Su and Y. Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621 (first posted 2026-09-29), https://arxiv.org/abs/2609.37621.
- R. Golla, H. Osaka, and S. S. Sequeira, *Quasinormal and hyponormal operators in the beta(H)-class*, arXiv:2610.13490 (first posted 2026-10-09), https://arxiv.org/abs/2610.13490.
- G. Ramesh and H. Osaka, *On a subclass of norm attaining operators*, Acta Scientiarum Mathematicarum 87 (2021), DOI:10.14232/ACTASM-020-426-9.
- G. Ramesh and H. Osaka, *On operators which attain their norm on every reducing subspace*, Annals of Functional Analysis 13 (2022), DOI:10.1007/s43034-022-00167-8.
