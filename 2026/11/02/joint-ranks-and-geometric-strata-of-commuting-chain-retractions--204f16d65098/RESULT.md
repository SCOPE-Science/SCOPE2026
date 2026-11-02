# Joint ranks and geometric strata of commuting chain retractions

## Finding
Let \(k\) be any field and let \(C=(C^0\to C^1\to\cdots\to C^d)\) be a bounded cochain complex of finite-dimensional \(k\)-spaces, with \(d\ge1\). Put \(b_i=\operatorname{rank}(d_i:C^i\to C^{i+1})\), \(h_i=\dim_k H^i(C)\), and \(b_{-1}=b_d=0\). All \(b_i,h_i\) are nonnegative integers. Fix \(m\ge1\), write \(\Sigma=\{0,1\}^m\), and consider ordered *chain endomorphisms* \(E_1,\ldots,E_m\) such that
\[
E_j^2=E_j,\qquad E_iE_j=E_jE_i\quad(1\le i,j\le m).
\]
The result describes each isomorphism/conjugacy class, its exact size over finite fields, every possible degreewise and homology rank vector, and the reduced parameter variety.

For each degree \(i\) and color \(\sigma\in\Sigma\), choose nonnegative integers \(h_{i,\sigma},b_{i,\sigma}\) with \(\sum_\sigma h_{i,\sigma}=h_i\) and \(\sum_\sigma b_{i,\sigma}=b_i\). Denote these data by \(\mathcal D\). Set
\[
\rho(h,b)=\sum_{i=0}^{d-1}b_i(h_i+h_{i+1}+b_{i+1}),\qquad b_d=0,
\]
and for a prime power \(q\) put
\[
G_q(h,b)=q^{\rho(h,b)}\prod_{i=0}^{d}|\operatorname{GL}_{h_i}(\mathbb F_q)|\prod_{i=0}^{d-1}|\operatorname{GL}_{b_i}(\mathbb F_q)|.
\]
Here \(|\operatorname{GL}_0(\mathbb F_q)|=1\), and the usual product \(|\operatorname{GL}_r(\mathbb F_q)|=\prod_{j=0}^{r-1}(q^r-q^j)\) applies for \(r>0\). For a color \(\sigma\), let \((h_\sigma,b_\sigma)\) be its two sequences.

**Classification and exact strata.** Two tuples are conjugate by a cochain automorphism if and only if they have identical \(\mathcal D\). Every such \(\mathcal D\) occurs. Over \(\mathbb F_q\) its exact number of *actual labeled tuples* is
\[
\boxed{\displaystyle W_q(\mathcal D)=\frac{G_q(h,b)}{\prod_{\sigma\in\Sigma}G_q(h_\sigma,b_\sigma)}.}
\]
Define \(r_{j,i}=\operatorname{rank}(E_j|_{C^i})\), \(u_{j,i}=\operatorname{rank}(H^i(E_j))\), and \(v_{j,i}=\operatorname{rank}(d_i|_{\operatorname{im}E_j})\). Their values in the stratum \(\mathcal D\) are exactly
\[
\begin{aligned}
r_{j,i}&=\sum_{\sigma:\sigma_j=1}(h_{i,\sigma}+b_{i,\sigma}+b_{i-1,\sigma}),\\
u_{j,i}&=\sum_{\sigma:\sigma_j=1}h_{i,\sigma},\\
v_{j,i}&=\sum_{\sigma:\sigma_j=1}b_{i,\sigma}.
\end{aligned}
\]
Consequently, summing \(W_q(\mathcal D)\) over all admissible \(\mathcal D\), with monomial weights recording these three displayed sets of ranks, is the **complete joint rank enumerator for any tuple length**. This is a finite explicit sum involving only the homology and differential ranks of \(C\), not its chosen matrices.

**Geometry.** Over an algebraic closure of \(k\), the *reduced* commuting-idempotent tuple variety has exactly
\[
\boxed{\displaystyle \prod_{i=0}^{d}\binom{h_i+2^m-1}{2^m-1}\prod_{i=0}^{d-1}\binom{b_i+2^m-1}{2^m-1}}
\]
geometrically irreducible components. Each is the single smooth homogeneous orbit \(\operatorname{Aut}(C)/\prod_\sigma\operatorname{Aut}(C_\sigma)\), indexed by \(\mathcal D\), and has dimension
\[
\boxed{\displaystyle \rho(h,b)-\sum_\sigma\rho(h_\sigma,b_\sigma)+\sum_i\bigl(h_i^2-\sum_\sigma h_{i,\sigma}^2\bigr)+\sum_i\bigl(b_i^2-\sum_\sigma b_{i,\sigma}^2\bigr).}
\]
It is an iterated affine-space bundle over a product of partial flag varieties. No assertion about a potentially nonreduced defining scheme is required.

## Assumptions and scope
The cochain complex is bounded, the spaces are finite dimensional, and consecutive differentials compose to zero. A cochain endomorphism preserves every degree and commutes with each differential. Ranks are taken as linear ranks in the indicated degree; \(H^i(E_j)\) denotes the induced map on homology. The case of a zero-dimensional chain group and zero multiplicities is included. The theorem holds in all field characteristics; finite-field counting requires \(q\) a prime power. The object being counted is a tuple of actual endomorphisms, not an orbit or a homotopy class. The geometric assertion concerns the reduced algebraic variety.

## Proof
**Step 1: canonical indecomposables.** Choose degreewise complements to the boundaries and cycles. This decomposes \(C\) into \(h_i\) copies of the one-degree complex \(S_i\) concentrated at \(i\), and \(b_i\) copies of the two-degree identity complex \(D_i=(k\xrightarrow{1}k)\) in degrees \(i,i+1\). These objects are pairwise nonisomorphic indecomposables and their multiplicities are intrinsic: the former are the dimensions of homology and the latter the differential ranks.

**Step 2: cochain endomorphism ring.** Directly enforcing the chain-map equation on these elementary complexes gives precisely the following one-dimensional \(k\)-spaces of homomorphisms between individual copies:
\[
\operatorname{Hom}(S_i,S_i),\quad \operatorname{Hom}(D_i,D_i),\quad
\operatorname{Hom}(D_i,S_i),\quad
\operatorname{Hom}(S_{i+1},D_i),\quad
\operatorname{Hom}(D_{i+1},D_i).
\]
Every other such Hom space is zero. Matrix-block multiplicities therefore give
\[
\operatorname{End}(C)/J\cong \prod_i M_{h_i}(k)\times\prod_i M_{b_i}(k),
\]
where \(J\) is the ideal of the three off-diagonal Hom types. It is nilpotent: its directed Hom graph has no oriented cycles (indices weakly decrease and every zero-index step is followed by a strict decrease). Its dimension is precisely \(\rho(h,b)\) displayed above. Thus \(\operatorname{Aut}(C)=\operatorname{End}(C)^\times\) is an extension of \(\prod_i\operatorname{GL}_{h_i}\times\prod_i\operatorname{GL}_{b_i}\) by \(1+J\), giving \(G_q(h,b)\) rational points over \(\mathbb F_q\).

**Step 3: simultaneous splittings.** For \(\sigma\in\Sigma\), put
\[
P_\sigma=\prod_{j:\sigma_j=1}E_j\prod_{j:\sigma_j=0}(1-E_j).
\]
All factors commute. The \(P_\sigma\) are pairwise orthogonal cochain idempotents summing to \(1\); hence \(C=\bigoplus_\sigma\operatorname{im}P_\sigma\). Conversely, every such colored direct-sum decomposition defines exactly one commuting tuple. Each summand decomposes into \(S_i\) and \(D_i\) with multiplicities \((h_{i,\sigma},b_{i,\sigma})\). Uniqueness of these multiplicities and the fact that any isomorphisms of colored summands assemble to an automorphism prove the classification. The conjugation stabilizer is \(\prod_\sigma\operatorname{Aut}(C_\sigma)\). Finite-field orbit-stabilizer proves the displayed weight \(W_q(\mathcal D)\). The formulas for ranks follow by summing the degrees and homology of the selected summands.

**Step 4: irreducible geometry.** The automorphism group \(G\) of \(C\) is an open subset of the affine endomorphism space; it is smooth, connected and irreducible. The subgroup \(H=\prod_\sigma\operatorname{Aut}(C_\sigma)\) is likewise smooth and connected. Thus the orbit \(G/H\) is smooth and irreducible, with dimension \(\dim G-\dim H\), yielding the displayed expression. The multiplicities in a family are locally constant: \(P_\sigma\) acts idempotently on fixed homology and boundary spaces, and its projective image ranks are locally constant. Hence each orbit is both open and closed in the reduced solution variety. These finitely many disjoint orbits are exactly its irreducible components. Stars-and-bars counts the color splittings of each multiplicity \(h_i,b_i\). Finally, let \(J_{\mathrm{diag}}=\bigoplus_\sigma P_\sigma JP_\sigma\) and \(J_{\mathrm{off}}=\bigoplus_{\sigma\ne\tau}P_\sigma JP_\tau\). The second space is stable under right multiplication by \(1+J_{\mathrm{diag}}\). For each \(j\in J\), with \(y=\operatorname{proj}_{\mathrm{diag}}(j)\), there is the **unique polynomial factorization** \(1+j=(1+x)(1+y)\), where \(x=(j-y)(1+y)^{-1}\in J_{\mathrm{off}}\). Inversion is a finite geometric sum because \(J\) is nilpotent. Thus the unipotent quotient \((1+J)/(1+J_{\mathrm{diag}})\) is an affine space; the full orbit fibers over \(\prod_i\operatorname{GL}_{h_i}/\prod_\sigma\operatorname{GL}_{h_{i,\sigma}}\times\prod_i\operatorname{GL}_{b_i}/\prod_\sigma\operatorname{GL}_{b_{i,\sigma}}\). Each such matrix-group quotient is itself an affine-space bundle over the corresponding partial flag variety. This exhibits the claimed iterated affine-bundle geometry and geometric irreducibility over the original field.

## Verification
The companion `verify_chain_retractions.py` uses two independent counting routes. The prediction enumerates all colored multiplicity vectors and group-order ratios. The direct route enumerates *all* degreewise linear maps in a fixed normal-form complex, filters by the actual differential-intertwining and idempotence equations, and checks commutation for each tuple; the rank profiles are computed by modular Gaussian elimination from those matrices. It compares **entire histograms** of degreewise ranks, homology ranks, and differential-image ranks, not just totals. The 11 fully exhaustive small-field configurations and 12 additional closed-form tests produce the marker `CHAIN_RETRACTIONS_JOINT_RANK_OK 11_DIRECT_HISTOGRAMS 12_CLOSED_FORM_TESTS`. Executing `python verify_chain_retractions.py` uses only Python's standard library and reproduces the companion `checker_output.txt`.

For instance, the complex having one copy each of \(S_0,S_1,D_0\) has exactly \(2^m(1+(2^m-1)q)^2\) commuting idempotent \(m\)-tuples. For \(m=2\) and \(q=2,3,5\), the totals are respectively \(196,400,1024\). A more coupled case, with one copy each of \(S_0,S_1\) and **two** copies of \(D_0\), has exactly \(5860\) commuting ordered pairs over \(\mathbb F_2\). Among them, exactly \(409\) pairs act as zero on *all* homology groups; their chain-level actions need not be zero. This case has \(160\) geometric components, including homogeneous strata with nontrivial matrix-factor/partial-flag geometry. Every stated finite figure is obtained by the independent checker.

## Relationship to prior work
The decomposability and the use of finite-field automorphism orders come from established representation theory, notably Reineke's Hall-algebra framework (2005) and Bridgeland's use of decompositions of complexes (2011); neither the standard decomposability nor generic orbit-stabilizer is claimed as new. The tensor-product idempotents in Kinser and Schiffler's representation *ring* (2010) are distinct from chain-map idempotents in an endomorphism algebra. The contribution assessed here is a complete **simultaneous** cochain-retraction classification with explicit full chain-and-homology joint rank weights for all lengths, together with explicit component dimensions and partial-flag stratification. A preexisting split-basic-algebra commuting-idempotent theorem covers multiplicity-free special cases but does not imply the general formula after Morita equivalence, since Morita equivalence does not preserve the number of actual idempotent tuples. All repeated-indecomposable cases have nontrivial general-linear factors. No broad priority claim is made beyond the stated refined enumeration/geometry.

## Limitations
All complexes considered are finite and over a field. No extension to complexes over general local rings, representations with nonzero differential composites, or unbounded complexes is proved. Homotopy classes, rather than actual strict cochain maps, are not counted. The geometric conclusion is for the reduced parameter variety, not a claim about possible nonreduced scheme structure. The classification follows from known splitting methods, so an unlocated broad theorem about idempotents in arbitrary endomorphism algebras could imply the formulas. Independent verification and exhaustive bibliographic priority checks have not been performed.

## References
1. M. Reineke, *Counting rational points of quiver moduli*, arXiv:math/0505389, public preprint 18 May 2005. https://arxiv.org/html/math/0505389v1
2. R. Kinser and R. Schiffler, *Idempotents in representation rings of quivers*, arXiv:1009.0029, first public preprint 31 August 2010. https://arxiv.org/html/1009.0029v2
3. T. Bridgeland, *Quantum groups via Hall algebras of complexes*, arXiv:1111.0745, first public preprint 3 November 2011. https://arxiv.org/abs/1111.0745
