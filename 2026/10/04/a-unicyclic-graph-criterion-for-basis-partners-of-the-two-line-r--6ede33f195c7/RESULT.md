# A unicyclic graph criterion for basis partners of the two-line Riesz family
## Finding
Let \(p\) be an odd prime, let \(G=\mathbb F_p^2\), and put \(\omega=e^{2\pi i/p}\). Consider
\[
E_p=(\{0\}\times\mathbb F_p)\cup\{(t,t):t\in\mathbb F_p\}\cup\{(1,0)\}.
\]
The two lines meet only at \((0,0)\), while \((1,0)\) lies on neither, so \(|E_p|=2p\).

For a frequency \(\lambda=(a,b)\in G\), define \(c=a+b\). Given \(B\subset G\) with \(|B|=2p\), form a simple bipartite graph \(\Gamma_B\) with left and right vertex sets both equal to \(\mathbb F_p\), in which \((a,b)\) is the edge from left vertex \(b\) to right vertex \(c=a+b\). Label this edge by \(a=c-b\).

Then \(B\) is an exponential basis partner for \(E_p\) if and only if \(\Gamma_B\) is spanning, connected, and unicyclic and its unique cycle has unequal label multisets on its two alternating perfect matchings. If the cycle edges are \(e_1,\ldots,e_{2r}\) in cyclic order, this last condition is equivalently
\[
S_C=\sum_{j=1}^{2r}(-1)^j\omega^{a(e_j)}\ne0.
\]
For every basis partner,
\[
|\det T(E_p,B)|=p^p|S_C|.
\]

There is also an exact nullity formula before imposing invertibility. Let \(n_B\) be the number of nonisolated vertices of \(\Gamma_B\), let \(c_B\) be its number of edge-containing connected components, and let
\[
\beta_B=2p-n_B+c_B.
\]
Let \(K_B\) be the kernel of the unsigned vertex-edge incidence map and define \(\psi_B(z)=\sum_{e\in B}z_e\omega^{a(e)}\). Then
\[
\dim\ker T(E_p,B)=
\begin{cases}
\beta_B-1,&\psi_B|_{K_B}\ne0,\\
\beta_B,&\psi_B|_{K_B}=0.
\end{cases}
\]

## Assumptions and scope
Characters are normalized by
\[
\chi_{a,b}(x,y)=\omega^{ax+by},
\]
and \(T(E_p,B)\) is the unnormalized square Fourier evaluation matrix with rows indexed by \(E_p\) and columns by \(B\). The statement is for odd primes and exactly the family appearing in Ferguson--Mayeli--Sothanaphan Question 1.10. It classifies basis partners and their determinants; it does not determine the optimal Riesz ratio \(\rho(E_p)\) or its asymptotics.

## Proof
Take coefficients \(z=(z_{a,b})_{(a,b)\in B}\) and let
\[
F_z(x,y)=\sum_{(a,b)\in B}z_{a,b}\omega^{ax+by}.
\]
For a left vertex \(b\), set
\[
r_b=\sum_{(a,b)\in B}z_{a,b},
\]
and for a right vertex \(c\), set
\[
s_c=\sum_{(a,b)\in B:\ a+b=c}z_{a,b}.
\]
On the vertical line,
\[
F_z(0,y)=\sum_{b\in\mathbb F_p}r_b\omega^{by},
\]
so invertibility of the \(p\)-point Fourier transform gives \(F_z=0\) on that line exactly when every \(r_b=0\). On the diagonal,
\[
F_z(t,t)=\sum_{c\in\mathbb F_p}s_c\omega^{ct},
\]
so vanishing on that line is equivalent to every \(s_c=0\). At the extra point,
\[
F_z(1,0)=\sum_{(a,b)\in B}z_{a,b}\omega^a.
\]
Hence
\[
\ker T(E_p,B)=K_B\cap\ker\psi_B,
\]
where \(K_B\) is the kernel of the unsigned incidence map \(z\mapsto((r_b)_b,(s_c)_c)\).

For a bipartite graph with \(n_B\) nonisolated vertices and \(c_B\) edge-containing connected components, the unsigned incidence matrix has rank \(n_B-c_B\): changing the signs of all rows on one bipartition turns it into the usual oriented incidence matrix, whose rank on each connected component is one less than the number of its vertices. Since \(|B|=2p\),
\[
\dim K_B=2p-n_B+c_B=\beta_B.
\]
Intersecting \(K_B\) with one scalar hyperplane gives the stated nullity formula.

Because \(n_B\le2p\) and \(c_B\ge1\), one always has \(\beta_B\ge1\). Invertibility therefore forces \(\beta_B=1\) and \(\psi_B|_{K_B}\ne0\). Equality \(\beta_B=1\) is possible only when all \(2p\) vertices are nonisolated and the graph has one connected component. A connected graph with \(2p\) vertices and \(2p\) edges is unicyclic. Conversely, a connected spanning unicyclic graph has one-dimensional incidence kernel. Peeling its trees from the leaves shows that a generator is supported on the unique even cycle and alternates \(+1,-1,+1,-1,\ldots\) around it. Thus \(\psi_B\) on that generator is exactly \(S_C\), proving the invertibility criterion.

For a prime \(p\), the condition \(S_C=0\) has a purely combinatorial form. Let \(d_j\) be the difference between the number of positively and negatively signed cycle edges having label \(j\in\mathbb F_p\), and set \(P(X)=\sum_{j=0}^{p-1}d_jX^j\). The cycle has equally many positive and negative edges, so \(P(1)=0\). If \(P(\omega)=0\), the minimal polynomial \(1+X+\cdots+X^{p-1}\) divides \(P\). Both have degree at most \(p-1\), so \(P\) is a scalar multiple of that cyclotomic polynomial; evaluating at \(1\) forces the scalar to be zero. Therefore every \(d_j=0\). This is precisely equality of the two alternating label multisets. The converse is immediate.

For the determinant, replace the samples on the full vertical line by their inverse discrete Fourier coefficients \((r_b)_b\), and likewise replace the samples on the diagonal by \((s_c)_c\). Because the two line sample sets share the origin, keep \((r_b)_{b\ne0}\) and all \((s_c)_c\), together with the extra-point row. The resulting row transformation has determinant of modulus \(p^{-p}\): one full inverse Fourier transform contributes \(p^{-p/2}\), and after the shared origin is accounted for the second contributes another \(p^{-p/2}\). The transformed evaluation matrix consists of a reduced unsigned incidence matrix, followed by the row \((\omega^{a(e)})_e\).

For a connected unicyclic graph, deleting a cycle edge from the reduced incidence matrix leaves a spanning tree and gives a maximal minor of modulus \(1\); deleting a tree edge gives a disconnected graph and determinant \(0\). Laplace expansion against the last row therefore gives transformed determinant of modulus \(|S_C|\). Undoing the row transformation yields
\[
|\det T(E_p,B)|=p^p|S_C|.
\]

## Verification
The bundled `verify.py` uses only the Python standard library. It exhausts all \(\binom{9}{6}=84\) candidates when \(p=3\), obtaining exactly \(75\) basis partners from the graph criterion. It also checks an explicit spanning-unicyclic family and deterministic samples for \(p=5,7,11\). Determinants are evaluated exactly after specializing \(\omega\) to elements of order \(p\) in two finite fields for each tested prime, and the conjugate-product identity corresponding to
\[
|\det T(E_p,B)|^2=p^{2p}|S_C|^2
\]
is verified in every sampled unicyclic case. The script prints `VERIFY_OK exact_modular_cases=407 exhaustive_p3=84 p3_bases=75`.

These finite checks are not used to prove the universal theorem. The proof above supplies the incidence-kernel reduction, the cyclotomic zero criterion, and the determinant formula for every odd prime.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan introduce quantitative spectrality for finite abelian groups and identify invertibility of \(T(E,B)\) with the basis-pair property. Their Question 1.10 asks specifically about the asymptotic Riesz ratio of the family \(E_p\) used here, emphasizing that it has bounded multi-tiling level but increasing geometric complexity. The inspected full text does not give a graph or unicyclic characterization of basis partners for that family.

The same paper contains restriction-count arguments for sets that are nearly contained in a subgroup, but those statements do not imply the present two-line incidence reduction: here a full second line lies outside either chosen line. The later work of Zhou on principal non-singularity of Fourier matrices concerns principal minors of product Fourier matrices and their permutations. The present matrix has a fixed non-principal row set \(E_p\) and arbitrary column set \(B\), so those principal-minor results do not cover the criterion above.

## Limitations
The theorem is a structural reduction, not a solution of the asymptotic question \(\rho(E_p)\to\infty\). It does not optimize singular values over the surviving unicyclic graphs. The determinant formula controls the product of singular values, not the smallest singular value by itself. The literature search cannot exclude an unindexed or differently phrased equivalent graph reformulation.

## References
1. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487v6. First public version: 2019-04-09. Primary MSC: 43A70, 43A40.
2. W. Zhou, *Principal Non-singularity of Fourier Matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189v1, 2025.
