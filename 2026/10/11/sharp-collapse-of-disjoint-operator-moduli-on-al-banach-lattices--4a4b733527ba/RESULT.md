# Sharp collapse of disjoint operator moduli on AL Banach lattices

## Finding

**Theorem.** Let \(E\) be an infinite-dimensional abstract AL Banach lattice over \(\mathbb R\) or \(\mathbb C\), let \(Y\) be any Banach space over the same scalar field, and let \(T,S:E\to Y\) be bounded linear operators. In the disjoint-operator notation defined below,
\[
\boxed{\beta(T)=\Gamma_d(T)=\kappa_d(T).}
\]
In addition, the second disjoint norm modulus has the disjoint-sequence representation
\[
\Delta_d(T)=\sup_{\mathbf x\in\mathcal D(E)}\beta(T|_{M(\mathbf x)}),
\]
and the common modulus satisfies the sharp perturbation inequality
\[
\boxed{|\beta(T+S)-\beta(T)|\leq\Delta_d(S).}
\]
The coefficient \(1\) is optimal; if \(S\) is disjointly strictly singular, then \(\beta(T+S)=\beta(T)\). In particular \(\kappa_d(T)\leq \beta(T)\) holds with sharp coefficient \(1\) throughout the AL class, giving a class-level affirmative answer to the comparison question posed by González and Martinón (2021, Question 1), without answering that question on arbitrary Banach lattices.

## Assumptions and scope

An **abstract AL Banach lattice** is a Banach lattice for which \(\|u+v\|=\|u\|+\|v\|\) whenever \(u,v\geq0\). Disjointness means \(|x|\wedge|y|=0\). Write \(\mathcal D(F)\) for the set of all infinite sequences \(\mathbf x=(x_n)_{n\geq1}\) of pairwise disjoint norm-one vectors of a Banach lattice \(F\); for each such sequence put \(M(\mathbf x)=\overline{\operatorname{span}}\{x_n:n\geq1\}\). Infinite-dimensional AL lattices admit such sequences (equivalently, use their standard \(L_1\)-space representation); each \(M(\mathbf x)\) carries the coordinate AL lattice order transported from its isometric \(\ell_1\) representation. This transported positive cone need not equal the positive cone inherited from \(E\); nevertheless, disjointness of vectors in \(M(\mathbf x)\) is exactly the same in both descriptions.

For a bounded operator \(R:F\to Y\), let
\[
\begin{aligned}
\beta(R)&=\inf_{\mathbf x\in\mathcal D(F)}\liminf_{n\to\infty}\|Rx_n\|,\\
\Gamma_d(R)&=\inf_{\mathbf x\in\mathcal D(F)}\|R|_{M(\mathbf x)}\|,\\
\tau_d(R)&=\sup_{\mathbf x\in\mathcal D(F)}j(R|_{M(\mathbf x)}),\\
\kappa_d(R)&=\inf_{\mathbf x\in\mathcal D(F)}\tau_d(R|_{M(\mathbf x)}),\\
\Delta_d(R)&=\sup_{\mathbf x\in\mathcal D(F)}\Gamma_d(R|_{M(\mathbf x)}),
\end{aligned}
\]
where \(j(U)=\inf_{\|z\|=1}\|Uz\|\) is the injection modulus. When the domain is \(M(\mathbf x)\), disjointness is tested in the ambient lattice \(E\), equivalently in the transported coordinate lattice order, and normalization uses the inherited norm. These are the quantities and conventions of González and Martinón (2021). The theorem makes no separability, nonatomicity, norm-attainment or target-space assumption.

## Proof

**1. Isometric disjoint spans.** Fix \(\mathbf x=(x_n)\in\mathcal D(E)\). For every finitely supported scalar family \((a_n)\), disjoint lattice moduli and additivity on the positive cone give
\[
\left\|\sum_n a_nx_n\right\|=\left\|\sum_n|a_n||x_n|\right\|=\sum_n|a_n|.
\]
This is valid for either scalar field and extends by completion. Consequently,
\[
\|T|_{M(\mathbf x)}\|=\sup_n\|Tx_n\|.\tag{1}
\]
In particular, \(\Gamma_d(T)=\inf_{\mathbf x}\sup_n\|Tx_n\|\).

**2. The first equality.** For every normalized disjoint sequence, \(\liminf_n\|Tx_n\|\leq\sup_n\|Tx_n\|\); taking infima gives \(\beta(T)\leq\Gamma_d(T)\). Conversely, fix \(\varepsilon>0\) and any \(\mathbf x\in\mathcal D(E)\). There is an infinite subsequence \(\mathbf y\) with \(\sup_k\|Ty_k\|\leq\liminf_n\|Tx_n\|+\varepsilon\). By (1), \(\Gamma_d(T)\leq\|T|_{M(\mathbf y)}\|\leq\liminf_n\|Tx_n\|+\varepsilon\). Taking the infimum over \(\mathbf x\), then sending \(\varepsilon\downarrow0\), proves \(\Gamma_d(T)=\beta(T)\).

**3. The injection-modulus envelope.** We establish the auxiliary inequality \(\beta(R)\leq\kappa_d(R)\) for any Banach lattice \(F\) supporting infinite disjoint sequences and any bounded \(R:F\to Y\). If \(\beta(R)=0\) this is immediate. Otherwise fix \(\mathbf x=(x_n)\in\mathcal D(F)\), set \(M_N=\overline{\operatorname{span}}\{x_n:n\geq N\}\), and fix \(0<\varepsilon<\beta(R)\). We claim that for some \(N\),
\[
 j(R|_{M_N})\geq\beta(R)-\varepsilon.\tag{2}
\]
If not, for every \(N\) there is a unit vector of \(M_N\) sent by \(R\) to norm strictly below \(\beta(R)-\varepsilon\). Because finite linear combinations of the \(x_n\) are dense in each \(M_N\), we can normalize approximants and preserve the relaxed bound \(\|Rz\|<\beta(R)-\varepsilon/2\). Choose such finitely supported unit vectors inductively, with each support lying strictly after the preceding support. They form a normalized disjoint block sequence in \(F\), while all their image norms are below \(\beta(R)-\varepsilon/2\). This contradicts the definition of \(\beta(R)\) and proves (2).

Since the tail \((x_n)_{n\geq N}\) is an admissible disjoint sequence within \(M(\mathbf x)\), (2) gives \(\tau_d(R|_{M(\mathbf x)})\geq\beta(R)-\varepsilon\). Infimizing over \(\mathbf x\) and letting \(\varepsilon\downarrow0\) yields \(\kappa_d(R)\geq\beta(R)\). Conversely, by definition \(\tau_d(R|_{M(\mathbf x)})\leq\|R|_{M(\mathbf x)}\|\), so \(\kappa_d(R)\leq\Gamma_d(R)\). Apply these comparisons to the AL-domain operator \(T\) and Step 2 to obtain the asserted triple equality.

**4. Second envelope and perturbations.** Each \(M(\mathbf x)\) is isometric to \(\ell_1\) under its coordinate map. In fact, if \(u=\sum_n a_nx_n\) and \(v=\sum_n b_nx_n\), then ambient disjointness \(|u|\wedge|v|=0\) holds exactly when \(a_nb_n=0\) for every \(n\): use \(|u|=\sum_n|a_n||x_n|\) and the disjointness of the \(|x_n|\). Thus the transported coordinate AL order has precisely the ambient disjoint sequences on this subspace. Applying Step 2 to restrictions gives \(\Gamma_d(T|_{M(\mathbf x)})=\beta(T|_{M(\mathbf x)})\); taking suprema gives the claimed representation of \(\Delta_d\). Proposition 4.5 of González and Martinón (2021) establishes for all Banach lattices the inequality \(\Gamma_d(T+S)\leq\Gamma_d(T)+\Delta_d(S)\). Applying Step 2 on \(E\) and then applying the same inequality with \(T=(T+S)-S\), using \(\Delta_d(-S)=\Delta_d(S)\), gives the two-sided bound for \(\beta\). For \(T=0\), \(S=I_E\), each modulus \(\beta(I_E)\) and \(\Delta_d(I_E)\) equals \(1\), so the coefficient cannot decrease. Proposition 4.4 of the same paper characterizes disjointly strictly singular operators by \(\Delta_d(S)=0\), giving the last assertion. \(\square\)

## Verification

The proof is analytic and requires no numerical sampling. Step 1 follows from the AL axiom and the lattice disjointness identity. Step 2 is an exact infimum/supremum comparison that crucially uses passing to subsequences. Step 3 uses only density of finite supports, normalizations, and disjointness of successive blocks; no compactness or separability assumption is hidden. Step 4 uses the explicitly cited Proposition 4.5, and optimality is directly checked at the identity on any infinite-dimensional AL lattice. A finite enumeration would not establish any of the infinite-dimensional claims.

## Relationship to prior work

González and Martinón, *A quantitative approach to disjointly non-singular operators* (arXiv:2108.01052v1, first available August 2, 2021), introduced the relevant operational quantities, showed \(\beta\leq\Gamma_d\) in Proposition 6.1, proved the general perturbation bound for \(\Gamma_d\) in Proposition 4.5, and posed in Question 1 the general comparison of \(\kappa_d\) against \(\beta\). Their Example 6.3 rules out a universal comparison between \(\Gamma_d\) and \(\beta\) in arbitrary lattice domains. The present AL theorem provides a sharp class-specific equality, not an unrestricted solution. Their Corollary 4.6 already established \(\Gamma_d\)-invariance under disjointly strictly singular perturbations; the corresponding \(\beta\)-invariance here follows from the new equality rather than being an independently claimed result. The earlier arXiv:2012.10683 develops disjointly non-singular operators and \(\beta\) but does not introduce this combined four-modulus comparison. Bilokopytov's arXiv:2501.03866 addresses topological DNS characterizations rather than quantitative equality of these moduli.

## Limitations

The comparison problem for arbitrary Banach lattices remains open here. In particular the AL disjoint additivity needed for (1) is absent for general \(L_p\) with \(p>1\); the 2021 paper exhibits arbitrarily large separation in a Hilbert-lattice setting. The theorem is restricted to infinite-dimensional domains where the disjoint-sequence infima are meaningful; it makes no assertion for conventions applied to finite-dimensional domains. Novelty is limited to the inspected primary literature and indexed research records, not guaranteed against unindexed equivalent formulations. No independent scientific audit has been performed.

## References

1. M. González and A. Martinón, *A quantitative approach to disjointly non-singular operators*, arXiv:2108.01052v1 (August 2, 2021), https://arxiv.org/html/2108.01052v1; journal version: RACSAM 115, article 185 (2021), https://doi.org/10.1007/s13398-021-01124-1.
2. M. González, A. Martínez-Abejón and A. Martinón, *Disjointly non-singular operators on Banach lattices*, arXiv:2012.10683v1 (December 19, 2020), https://arxiv.org/html/2012.10683v1.
3. E. Bilokopytov, *Disjointly non-singular operators and various topologies on Banach lattices*, arXiv:2501.03866v2 (2025), https://arxiv.org/html/2501.03866v2.
