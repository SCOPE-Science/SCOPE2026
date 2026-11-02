# Complete ideal census and smooth Goursat strata for bipartite graphical Lie algebras

## Finding
Let \(k\) be any field, and let \(A\) and \(B\) be vector spaces of respective positive dimensions \(p\) and \(r\). Consider the two-step nilpotent Lie algebra
\[
\mathfrak n_{p,r}(k)=A\oplus B\oplus (A\otimes_k B),\qquad
[(a,b,z),(a',b',z')]=a\otimes b'-a'\otimes b.
\]
This is the graphical Lie algebra of the complete bipartite graph \(K_{p,r}\). The tensor summand \(Z=A\otimes B\) is central.

**Classification.** Every Lie ideal \(I\) is uniquely determined by a subspace \(U\leq A\oplus B\), a subspace \(E\leq (A/P)\otimes(B/Q)\), and a map
\[
\phi:U\longrightarrow ((A/P)\otimes(B/Q))/E,
\qquad P=\pi_A(U),\quad Q=\pi_B(U).
\]
Put \(H=P\otimes B+A\otimes Q\leq Z\) and let \(K\) be the inverse image of \(E\) under the canonical quotient \(Z\to Z/H\cong(A/P)\otimes(B/Q)\). The ideal is
\[
I=\{u+z:u\in U,\ z\in Z,\ z\bmod K=\phi(u)\}.
\]
Conversely, every such triple defines an ideal. In particular, the classification does **not** restrict ideals to graph-induced coordinate subspaces.

**Finite-field dimension census.** For \(k=\mathbb F_q\), let \(\mathcal I_{p,r}(q;T)=\sum_I T^{\dim I}\), summing over all distinct \(k\)-linear Lie ideals, including \(0\) and the full algebra. Write \(\genfrac{[}{]}{0pt}{}{n}{j}_q\) for the Gaussian binomial coefficient and \(g_c(q)=\prod_{i=0}^{c-1}(q^c-q^i)\), with \(g_0(q)=1\). For \(0\leq\alpha\leq p\), \(0\leq\beta\leq r\), \(0\leq c\leq\min(\alpha,\beta)\), set \(u=\alpha+\beta-c\) and \(M=(p-\alpha)(r-\beta)\). Then
\[
\boxed{\begin{aligned}
\mathcal I_{p,r}(q;T)={}&
\sum_{\alpha=0}^{p}\sum_{\beta=0}^{r}\sum_{c=0}^{\min(\alpha,\beta)}
\genfrac{[}{]}{0pt}{}{p}{\alpha}_q
\genfrac{[}{]}{0pt}{}{r}{\beta}_q
\genfrac{[}{]}{0pt}{}{\alpha}{c}_q
\genfrac{[}{]}{0pt}{}{\beta}{c}_q
 g_c(q)\\
&\qquad\cdot\sum_{e=0}^{M}
\genfrac{[}{]}{0pt}{}{M}{e}_q
q^{u(M-e)}T^{u+pr-M+e}.
\end{aligned}}
\]
Every coefficient is an exact integer count for every prime power \(q\), including powers of two. The formula is a polynomial in \(q\) for each fixed \(p,r\) and exponent of \(T\).

**Geometric strata.** The fixed-ideal-dimension reduced ideal variety has a finite disjoint locally closed stratification indexed by \((\alpha,\beta,c,e)\), recording
\[
\alpha=\dim P,\quad\beta=\dim Q,\quad
c=\dim P-\dim(U\cap A)=\dim Q-\dim(U\cap B),\quad\ e=\dim E.
\]
Every nonempty stratum is smooth and geometrically irreducible over \(k\), with dimension
\[
\boxed{\alpha(p-\alpha)+\beta(r-\beta)+c(\alpha+\beta-c)+(u+e)(M-e).}
\]
This statement concerns the reduced locally closed strata, not the possibly nonreduced scheme structure of the entire ideal scheme, nor does it assert that distinct strata are distinct irreducible components of the entire ideal variety.

For example, \(\mathfrak n_{2,2}(\mathbb F_2)\) is eight-dimensional and has exactly \(247\) Lie ideals, with dimension multiplicities
\[
(1,15,35,39,55,51,35,15,1).
\]
For \(\mathfrak n_{1,2}(\mathbb F_q)\), the complete dimension polynomial simplifies to
\[
1+(q+1)T+(q^2+q+1)(T^2+T^3+T^4)+T^5.
\]

**Rigidity of the enumerator.** For fixed finite-field cardinality \(q\), the polynomial \(\mathcal I_{p,r}(q;T)\) determines the unordered pair \(\{p,r\}\). Its degree gives \(p+r+pr\); its coefficient of \(T\) is \(\genfrac{[}{]}{0pt}{}{pr}{1}_q\), which determines \(pr\). These two data determine \(p+r\), hence the two part sizes up to interchange.

## Assumptions and scope
The integers \(p,r\) are positive and \(k\) is an arbitrary field, without any characteristic restriction. All ideals are \(k\)-linear subspaces stable under brackets with the full Lie algebra; no grading, coordinate-support or automorphism-invariance condition is imposed. The finite-field counts enumerate embedded ideals, not abstract isomorphism types or automorphism orbits. All geometric assertions concern the reduced locally closed strata over the specified field and remain valid after algebraic closure.

## Proof
**1. Recover the minimal central part.** For any ideal \(I\), let \(U\) be its image under \(\pi:\mathfrak n\to A\oplus B\), and put \(K=I\cap Z\). Since \(Z\) is central, \(I\) is an ideal if and only if \([U,A\oplus B]\subseteq K\). If \(P=\pi_A(U)\) and \(Q=\pi_B(U)\), bracketing lifts of elements of \(U\) separately with pure \(A\)-vectors and pure \(B\)-vectors gives
\[
[U,A\oplus B]=P\otimes B+A\otimes Q=H.
\]
The quotient map \(A\otimes B\to(A/P)\otimes(B/Q)\) is surjective with kernel \(H\), by exactness of tensoring vector spaces over a field. Thus \(K/H\) is a unique subspace \(E\) of the stated quotient. Since \(I/K\) maps isomorphically onto \(U\), each \(u\in U\) has a unique lift modulo \(K\), giving the linear map \(\phi:U\to Z/K\). Conversely, the displayed inverse-image construction has intersection \(K\) with \(Z\), projects to \(U\), and is closed under all Lie brackets since \([U,A\oplus B]=H\subseteq K\). This proves existence and uniqueness of the triple, for every characteristic.

**2. Goursat description of the horizontal subspace.** Let \(A_0=U\cap A\) and \(B_0=U\cap B\). Then \(U\) induces an isomorphism \(\theta:P/A_0\to Q/B_0\): pair the two projections of a vector \((a,b)\in U\), modulo the respective intersections. Its graph recovers \(U\) uniquely. For fixed \(\alpha=\dim P\), \(\beta=\dim Q\), and \(c=\dim P/A_0=\dim Q/B_0\), choose \(P,Q,A_0,B_0\), then an invertible map between the two \(c\)-dimensional quotients. The number of choices over \(\mathbb F_q\) is
\[
\genfrac{[}{]}{0pt}{}{p}{\alpha}_q
\genfrac{[}{]}{0pt}{}{r}{\beta}_q
\genfrac{[}{]}{0pt}{}{\alpha}{c}_q
\genfrac{[}{]}{0pt}{}{\beta}{c}_q g_c(q).
\]
Here \(\dim U=\alpha+\beta-c=u\). This step accounts for genuinely mixed, non-coordinate horizontal ideals.

**3. Central and lifting choices.** The tensor quotient \((A/P)\otimes(B/Q)\) has dimension \(M=(p-\alpha)(r-\beta)\), so its \(e\)-planes \(E\) number \(\genfrac{[}{]}{0pt}{}{M}{e}_q\). The resulting \(K\) has dimension \(pr-M+e\). The maps \(\phi\) form an affine space of dimension \(u(M-e)\), hence contribute \(q^{u(M-e)}\) possibilities. The total ideal dimension is \(u+pr-M+e\). Multiplying these independent counts proves the exact polynomial.

**4. Geometry.** Choose \(P\in\operatorname{Gr}(\alpha,A)\), \(Q\in\operatorname{Gr}(\beta,B)\), then \(A_0\in\operatorname{Gr}(\alpha-c,P)\), \(B_0\in\operatorname{Gr}(\beta-c,Q)\). Over the product of these relative Grassmannians, the isomorphisms \(P/A_0\cong Q/B_0\) form a Zariski-locally trivial \(\mathrm{GL}_c\)-bundle. The central choices \(E\) form a relative \(\operatorname{Gr}(e,M)\)-bundle, and the lifting maps \(\phi\) form a vector bundle of rank \(u(M-e)\). Ordinary Grassmannians, \(\mathrm{GL}_c\) and affine spaces are smooth and geometrically irreducible. Their successive locally trivial bundles are, therefore, smooth and geometrically irreducible. Adding base, isomorphism-fiber, central Grassmannian and affine-fiber dimensions gives precisely the displayed stratum dimension.

**5. Enumerator rigidity.** The center is exactly \(Z\): a nonzero horizontal component brackets nontrivially with a pure vector from the opposite vertex part. If \(kv\) is a one-dimensional Lie ideal, then \([x,v]=\lambda_x v\) for each \(x\). But \(\operatorname{ad}(x)^2=0\) in any two-step nilpotent Lie algebra, so \(\lambda_x^2v=0\) and hence \(\lambda_x=0\). Every one-dimensional ideal is therefore a line in \(Z\). Its number over \(\mathbb F_q\) is \(\genfrac{[}{]}{0pt}{}{pr}{1}_q\); this and the total dimension prove the stated rigidity.

The proof uses no assumptions on invertibility of \(2\), does not require algebraic closure, and establishes equalities for every \(p,r\ge1\).

## Verification
A standalone Python checker enumerates all subspaces in reduced row-echelon form and tests Lie-ideal closure by bracketing their basis vectors against every horizontal basis element **using the original structure constants**. It then compares dimension-by-dimension multiplicities with the independently evaluated formula. Seven exhaustive cases pass: \(K_{1,1}\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\); \(K_{1,2}\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\); and \(K_{2,2}\) over \(\mathbb F_2\). In the last case all \(417199\) subspaces of an eight-dimensional binary vector space were checked. The \(\mathbb F_4\) operations use a genuine quadratic extension field. Reproduce with `python3 verify_ideals.py`; the expected output is in `verification_output.txt`. Finite tests corroborate but do not prove the arbitrary-field classification.

## Relationship to prior work
The Dani–Mainkar graphical Lie-algebra construction and Mainkar's graph-isomorphism theorem (arXiv:1310.3414v1, first public 2013-10-12) provide the natural objects but do not classify their arbitrary linear ideals. Godoy Molina and Lagos (arXiv:2308.00272v2, Sections 3 and 5) study special *graph-ideals* and graded derivations of complete-bipartite examples. Their special graph-ideals do not recover the non-coordinate Goursat parameters, arbitrary central subspaces, or the full ideal census. Rossmann's work on graphical groups (DOI 10.1112/blms.12665) counts conjugacy classes and related invariants, rather than Lie ideals. A general central-extension approach alone yields a necessary bracket-closure criterion; the explicit Goursat stratification, geometric dimensions, and all-dimensional Gaussian enumeration require the additional computations above.

No equivalent or stronger complete formula was identified in the performed mathematical literature and research-record comparisons. This negative search result is not a proof of historical originality; general ideal-zeta or subalgebra-enumeration literature may contain equivalent results, and independent priority assessment remains open.

## Limitations
This theorem does not classify ideals for arbitrary graphs, complete multipartite graphs with three or more vertex parts, or Lie algebras obtained by identifying multiple edge labels. It does not calculate automorphism orbits, the irreducible components of whole fixed-dimensional ideal varieties, or scheme-theoretic nilpotents. Geometrically irreducible strata need not be irreducible components of their union. The checker exhaustively covers only the listed small finite fields and ranks. No independent audit has been performed.

## References
1. Meera G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414v1 (public 2013-10-12), https://arxiv.org/abs/1310.3414.
2. Mauricio Godoy Molina and Diego Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272v2 (2023), https://arxiv.org/abs/2308.00272.
3. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bulletin of the London Mathematical Society (2022), DOI:10.1112/blms.12665.
4. Shrikrishna G. Dani and Meera G. Mainkar, *Anosov automorphisms on compact nilmanifolds associated with graphs*, Transactions of the AMS 357 (2005), 2235–2251, DOI:10.1090/S0002-9947-04-03518-4.
