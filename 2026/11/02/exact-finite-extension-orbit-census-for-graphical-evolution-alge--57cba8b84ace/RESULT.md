# Exact finite-extension orbit census for graphical evolution-algebra squaring

## Finding

Let \(G\) be any finite simple graph with \(N\ge1\) vertices, and let \(k=\mathbb F_{2^f}\) with \(f\ge1\). Give \(E_G(k)\) the natural basis \(e_1,\ldots,e_N\), multiplication \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_{j\sim i}e_j\). Let \(T(x)=x^2\), with iterates understood as repeated squaring, **not** associative powers, and let \(A\) be the adjacency matrix of \(G\), regarded over \(\mathbb F_2\). Put \(\rho_j=\operatorname{rank}_{\mathbb F_2}(A^j)\), including \(\rho_0=N\), and \(s=\rho_N\). For each positive integer \(m\), put \(d=\gcd(m,f)\) and \(\ell=\operatorname{lcm}(m,f)\).

**Orbit census theorem.** The following two formulas determine every primitive cycle count and every preperiod-depth count of the quadratic evolution operator \(T\):

\[
\#\operatorname{Fix}(T^m)=2^{d\,\bigl(N-\operatorname{rank}_{\mathbb F_2}(A^\ell-I_N)\bigr)}\qquad(m\ge1),
\]
\[
\#\{x:\text{first entry into a periodic orbit occurs by iterate }j\}
=(2^f)^{s+N-\rho_j}\qquad(j\ge0).
\]

Hence the number of points of *exact* preperiod \(j\ge1\) is the difference between the second expression at \(j\) and \(j-1\), and the exact number of primitive \(m\)-cycles is
\[
\frac1m\sum_{a\mid m}\mu(m/a)\,\#\operatorname{Fix}(T^a).
\]
The formulas apply even when \(A\) is singular or not diagonalizable over any field.

For a **complete multipartite** graph \(G=K_{n_1,\ldots,n_r}\), \(r\ge2\), \(n_i\ge1\), let \(o\) count odd \(n_i\), \(e=r-o\), and put \(s=o-\mathbf1_{o\text{ odd}}\). Then
\[
\begin{aligned}
\rho_0&=N,\\
\rho_1&=r-\mathbf1_{r\text{ odd}},\\
\rho_2&=o-\mathbf1_{e=0,\ o\text{ odd}},\\
\rho_j&=s\quad(j\ge3).
\end{aligned}
\]
For every \(m\ge1\), the **closed arithmetic periodic-point formula**, valid over every binary extension field, is
\[
\boxed{
\#\operatorname{Fix}(T^m)=
\begin{cases}
1,&o=0,\\
2^{(o-1)\gcd(f,m)},&o\text{ odd},\\
2^{\bigl(o-\mathbf1_{f\text{ odd},\ m\text{ odd}}\bigr)\gcd(f,m)},&o\ge2\text{ even}.
\end{cases}}
\]
Together with the displayed ranks and Möbius inversion, this is a complete closed census by transient depth and periodic cycle length in every dimension and over every \(\mathbb F_{2^f}\). All exact preperiods are at most three; preperiod three occurs precisely when \(e>0\) and \(o\) is odd. The maximum primitive period is \(1\) when \(o\le1\), \(f\) when \(o\ge3\) is odd, and \(\operatorname{lcm}(2,f)\) when \(o\ge2\) is even; each stated maximum is attained.

For example, on \(K_{1,1}\), \(o=2\). The squaring map over \(\mathbb F_4\) has **four** fixed points, whereas over the larger field \(\mathbb F_8\) it has only **two**. Thus replacing \(2\) by the extension cardinality in the earlier binary fixed-point count is incorrect.

## Assumptions and scope

Only unweighted, loopless, undirected simple graphs are considered; the natural basis and the quadratic map are fixed, and no claims are made about basis-invariant nonlinear dynamics under arbitrary algebra isomorphisms. The finite field has characteristic two and cardinality \(2^f\). The number of cycles counts distinct directed periodic cycles; a cycle of length \(m\) contains \(m\) points. A preperiod is the least nonnegative number of iterations required to enter a periodic cycle. Rank calculations for \(A\) and its powers occur over \(\mathbb F_2\), not over the real numbers.

## Proof

**1. Frobenius-linearization.** Write \(\sigma(x_1,\ldots,x_N)=(x_1^2,\ldots,x_N^2)\). Since all mixed products in an evolution algebra vanish,
\[
T(x)=A\sigma(x).
\]
The entries of \(A\) lie in \(\mathbb F_2\), so \(A\sigma=\sigma A\). Therefore \(T^j=A^j\sigma^j\) for every nonnegative integer \(j\). As an \(\mathbb F_2\)-linear endomorphism of the \(fN\)-dimensional additive state space, \(T\) has the same iterated kernel cardinalities as \(A\): \(\#\ker(T^j)=(2^f)^{N-\rho_j}\).

**2. Preperiod strata.** The Fitting decomposition for \(A\) gives \(k^N=U\oplus V\), where \(U=\operatorname{im}(A^N)\), \(V=\ker(A^N)\), \(\dim_k U=s\), and \(A\) is bijective on \(U\) and nilpotent on \(V\). Both subspaces have bases over \(\mathbb F_2\), hence are preserved by coordinate Frobenius and by \(T\). Consequently the periodic state set is exactly \(U\), with \(\#U=(2^f)^s\). A state \(u+v\) first reaches a periodic cycle by iteration \(j\) precisely when \(T^j(v)=0\). Multiplying \(\#U\) by the kernel size from Step 1 proves the preperiod formula, including \(j=0\) and the stationary case \(A=0\).

**3. Exact iterate-fixed points.** Choose a normal basis \(\theta,\theta^2,\ldots,\theta^{2^{f-1}}\) of \(k/\mathbb F_2\). In its \(\mathbb F_2\)-coordinates, \(\sigma\) is a cyclic shift of \(f\) slots. Thus \(T^m\) acts on \(f\) slots of \(\mathbb F_2^N\) as \(A^m\) composed with a shift by \(m\) slots. That shift has \(d=\gcd(f,m)\) disjoint cycles of length \(h=f/d\). On each slot-cycle, specifying one vector \(v\) determines the remaining slots, and the consistency equation is exactly \(A^{mh}v=v\). Its solution space has \(\mathbb F_2\)-dimension \(N-\operatorname{rank}_{\mathbb F_2}(A^{mh}-I_N)\). Independent choices across the \(d\) slot-cycles prove the fixed-point formula because \(mh=\ell\). Notice that this argument does not assume \(A\) invertible. Möbius inversion supplies the primitive-cycle formula.

**4. Rank profile for multipartite graphs.** Let \(S:k^N\to k^r\) take sums within each part and let \(E:k^r\to k^N\) repeat each part value. They are respectively surjective and injective. Over \(\mathbb F_2\), let \(C=I_r+\mathbf1\mathbf1^{\mathsf T}\), \(D=\operatorname{diag}(n_i\bmod2)\). Then \(A=ECS\), \(SE=D\), and \(A^2=ECDCS\). The matrix \(C\) has rank \(r\) for even \(r\) and \(r-1\) for odd \(r\). In block order (odd-sized parts, then even-sized parts), direct multiplication gives
\[
CDC=
\begin{cases}
\begin{pmatrix}I_o&J_{oe}\\J_{eo}&0\end{pmatrix},&o\text{ even},\\[4pt]
\begin{pmatrix}I_o+J_{oo}&0\\0&J_{ee}\end{pmatrix},&o\text{ odd},
\end{cases}
\]
with the usual interpretation of empty blocks. The ranks are respectively \(o\) and \(o-1+\mathbf1_{e>0}\), proving the stated \(\rho_2\). On part-constant vectors, the next odd-part coordinates are \(B\sigma(u)\), where \(B=I_o+J_{oo}\); the next even-part coordinates are all \(\sigma(\sum_i u_i)\). For even \(o\), \(B^2=I_o\), so the stable image has dimension \(o\). For odd \(o\), \(B^2=B\), \(\operatorname{im}B=\ker\sum_i u_i\), and the even coordinates vanish from the next step onward; the stable image has dimension \(o-1\). This proves all \(\rho_j\), \(j\ge3\), and the three-step transient bound.

**5. Exact multipartite periods.** If \(o=0\), the stable image is zero. If \(o\) is odd, the stable image is the odd-part hyperplane \(H=\{u:\sum u_i=0\}\), with all even-part coordinates zero; \(T\) acts on this \(o-1\)-dimensional \(k\)-space by \(\sigma\), giving \(2^{(o-1)\gcd(f,m)}\) fixed points of its \(m\)th iterate. If \(o\ge2\) is even, the stable image is identified with \(k^o\) by \(u\mapsto(u,(\sum u_i)\mathbf1_e)\), and \(T\) becomes \(B\sigma\), where \(B^2=I_o\) and \(\dim_{\mathbb F_2}\ker(B-I_o)=o-1\). Applying Step 3 to \(B\) gives \(2^{o\gcd(f,m)}\) unless \(\ell=\operatorname{lcm}(f,m)\) is odd, in which case it gives \(2^{(o-1)\gcd(f,m)}\). The oddness of \(\ell\) is equivalent to both \(f\) and \(m\) being odd. This proves the closed periodic-point formula.

For sharpness of maximal period, the restriction to \(H\) for odd \(o\ge3\) contains a nonzero \(\mathbb F_2\)-vector tensored with a normal-basis element of Frobenius order \(f\). For even \(o\ge2\), choose \(v\in\mathbb F_2^o\) with odd coordinate sum; then \(Bv\ne v\), \(B^2v=v\). Tensor \(v\) with a normal-basis element of Frobenius order \(f\): its orbit under \(B\sigma\) has exact period \(\operatorname{lcm}(2,f)\). Finally \(\rho_2>\rho_3\) holds exactly when \(e>0\) and \(o\) is odd, establishing sharp preperiod three via Step 2.

## Verification

The standalone script `check_dynamics.py` independently enumerates every state of selected \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\) evolution algebras; it constructs the full state transition function, follows its actual cycles and preperiods, and counts fixed points of iterates. It separately forms binary adjacency powers and computes ranks. Across **21 complete configurations**, including complete multipartite families and nonmultipartite paths and cycles, all results agree with the general and specialized formulas. The diagnostic is `EVOLUTION_SQUARE_ORBIT_CENSUS_OK 21`. Running `python3 check_dynamics.py` requires only the Python standard library; `verification_output.txt` records output. Exhaustive testing in small finite state spaces is corroboration, not a replacement for Steps 1--5.

## Relationship to prior work

Elduque and Labra (2013) establish the graphical evolution-algebra framework and relate directed cycles to algebraic nilpotency; their original article does not give arithmetic orbit counts of the quadratic squaring map. General linear finite dynamical systems and the normal-basis theorem provide indispensable classical mechanisms, so the general Frobenius-graph reduction should not be mistaken for a new theory of linear dynamics. The published *Sharp period-four census for complete multipartite parity automata* already gives the \(\mathbb F_2\) graph-parity specialization and the exact first three adjacency ranks; both are acknowledged as known. Its hypothesis fixes a Boolean alphabet. The present closed arithmetic formula instead treats every binary extension field and exhibits a sharp dependence on the parity of the extension degree: the fixed-point count can **decrease** from \(\mathbb F_4\) to \(\mathbb F_8\), which is not reproduced by replacing the Boolean alphabet size with the field cardinality. The all-graph normal-basis expression unifies these counts and gives full preperiod data. Varro (2019/2020) treats the qualitative categories of characteristic-two evolution operators; the accessible abstract does not settle the prescribed graph-family point-count comparison. This remains a source-access risk rather than proof of absence.

## Limitations

The finite-field point counts are confined to characteristic two and to evolution algebras whose structure constants are the binary adjacency entries of a simple graph. They do not imply corresponding formulas in odd characteristic or for arbitrary weighted graphs. The result determines global cycle-length and preperiod-depth counts, not the detailed branching shapes or attachment patterns of trees rooted at individual periodic points, nor orbit-equivalence classifications under algebra automorphisms. The general reduction uses standard finite-linear-dynamics machinery; novelty rests on the explicit characteristic-two graphical formulas, especially the extension-degree dependence. Publication-priority verification cannot exclude an equivalent presentation in unavailable historical literature, and no independent mathematical audit has been conducted.

## References

1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, publicly submitted 17 December 2013. https://arxiv.org/abs/1312.4685
2. R. A. Hernández Toledo, *Linear Finite Dynamical Systems*, Communications in Algebra 33 (2005), 2977--2989, DOI 10.1081/AGB-200066211.
3. U. Dempwolff, J. C. Fisher and A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Mathematical Journal 42 (2000), 289--295, DOI 10.1017/S0017089500020164.
4. *Sharp period-four census for complete multipartite parity automata*, publicly available result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-period-four-census-for-complete-multipartite-parity-automa--acea41c73be7/RESULT.md .
5. R. Varro, *Étude des opérateurs d'évolution en caractéristique 2*, arXiv:1911.07001 (2019); related journal article *On evolution operators in characteristic 2*, Communications in Algebra 49 (2021), 590--613, DOI 10.1080/00927872.2020.1812620.
