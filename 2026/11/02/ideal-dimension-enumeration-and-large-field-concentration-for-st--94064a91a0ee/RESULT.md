# Ideal-dimension enumeration and large-field concentration for star-graph Lie algebras

## Finding

For every integer \(n\geq1\) and prime power \(q\), let \(L_{n,q}\) be the two-step nilpotent Lie algebra over \(\mathbb F_q\) associated to the star graph \(K_{1,n}\), with its \(n\) edges distinctly labeled. Its ideal-dimension polynomial is

\[
F_{n,q}(t)=\sum_{k=0}^{n}{n\brack k}_q\left(q^{n-k}t^{n+k+1}+\sum_{j=k}^{n}{n-k\brack j-k}_q q^{k(n-j)}t^{k+j}\right),
\]

where \({a\brack b}_q\) denotes the Gaussian binomial coefficient and the coefficient of \(t^d\) is the number of Lie ideals of \(\mathbb F_q\)-dimension \(d\). Thus the formula simultaneously determines every ideal-dimension stratum, not merely the total number of ideals.

For fixed \(n\geq4\), choose an ideal uniformly from the finite ideal set and let \(D_{n,q}\) be its dimension. As \(q\to\infty\) through prime powers, the following limits hold:

\[
\begin{aligned}
 &n\text{ even}:&&\mathbb P(D_{n,q}=n)\longrightarrow1,\\
 &n\text{ odd}:&&\big(\mathbb P(D_{n,q}=n-1),\mathbb P(D_{n,q}=n),\mathbb P(D_{n,q}=n+1)\big)\longrightarrow(1/3,1/3,1/3).
\end{aligned}
\]

The first formula also applies in the smaller dimensions \(n=1,2,3\); the large-field conclusion deliberately assumes \(n\geq4\).

## Assumptions and scope

Let \(V=\mathbb F_q h\oplus U\), where \(U=\operatorname{span}_{\mathbb F_q}\{u_1,\ldots,u_n\}\), and let \(Z=\operatorname{span}_{\mathbb F_q}\{z_1,\ldots,z_n\}\). Define \(L_{n,q}=V\oplus Z\), with only nonzero brackets on basis vectors

\[
[h,u_i]=z_i,\qquad [u_i,h]=-z_i,\qquad 1\leq i\leq n,
\]

and extend bilinearly and alternatingly. The bracket is a Lie bracket in every characteristic, including characteristic \(2\): since all its values lie in the central subspace \(Z\), the Jacobi identity holds. Moreover, \([L_{n,q},L_{n,q}]=Z\) and \(\dim L_{n,q}=2n+1\). A *Lie ideal* is an \(\mathbb F_q\)-linear subspace \(I\) with \([I,L_{n,q}]\subseteq I\); it is not an associative-ring ideal or an abstract additive subgroup. There is no restriction on the characteristic or on the finite-field extension degree.

For integers \(0\leq b\leq a\), define \({a\brack b}_q=\prod_{i=0}^{b-1}(q^{a-i}-1)/(q^{b-i}-1)\), and set it to zero outside this range. The empty product is \(1\).

## Proof

Let \(\pi:L_{n,q}\to V\) be projection along \(Z\). For an arbitrary ideal \(I\), set \(S=\pi(I)\leq V\) and \(T=I\cap Z\leq Z\). Since \(Z\) is central, the ideal condition is exactly

\[
[S,V]\subseteq T.
\]

Conversely, if subspaces \(S\leq V\) and \(T\leq Z\) satisfy this condition, every linear map \(\phi:S\to Z/T\) uniquely determines an ideal \(I\) with \(\pi(I)=S\) and \(I\cap Z=T\): take the inverse image in \(S\oplus Z\) of the graph of \(\phi\) in \(S\oplus(Z/T)\). Distinct maps give distinct ideals, of dimension \(\dim S+\dim T\). Hence the number of such ideals for fixed \(S,T\) is exactly \(q^{\dim S(n-\dim T)}\). This construction does not assume that the ideal is homogeneous with respect to \(V\oplus Z\); all tilted subspaces are included.

Identify \(U\) with \(Z\) by \(u_i\mapsto z_i\). There are two disjoint cases.

First suppose \(S\not\subseteq U\). Put \(K=S\cap U\), of dimension \(k\). Then \(S=K\oplus\mathbb F_q(h+w)\) for a unique coset \(w+K\in U/K\). There are \({n\brack k}_q q^{n-k}\) choices of \(S\) of this form. Because \([h+w,U]=Z\), the ideal condition forces \(T=Z\). There is one graph lift and its dimension is \(n+k+1\). These ideals contribute

\[
\sum_{k=0}^n{n\brack k}_q q^{n-k}t^{n+k+1}.
\]

Next suppose \(S\subseteq U\) and \(\dim S=k\). Then \([S,V]\subset Z\) is precisely the image of \(S\) under \(U\simeq Z\), and so has dimension \(k\). There are \({n\brack k}_q\) possibilities for \(S\). For \(k\leq j\leq n\), the subspaces \(T\leq Z\) of dimension \(j\) containing this image number \({n-k\brack j-k}_q\). The graph maps \(S\to Z/T\) number \(q^{k(n-j)}\), and each corresponding ideal has dimension \(k+j\). The contribution is therefore

\[
\sum_{k=0}^{n}{n\brack k}_q\sum_{j=k}^n{n-k\brack j-k}_q q^{k(n-j)}t^{k+j}.
\]

Adding the two cases proves the exact polynomial identity, including the zero ideal \((k,j)=(0,0)\) and the whole algebra \((k=n\) in the first case).

For the large-field statement, recall that \({a\brack b}_q\) is a monic polynomial in \(q\) of degree \(b(a-b)\). Thus every term from the second case, indexed by \((k,j)\), has \(q\)-degree

\[
 k(n-k)+(j-k)(n-j)+k(n-j)=k(n-k)+j(n-j).
\]

Its maximal possible degree is \(2\lfloor n^2/4\rfloor\), achieved precisely when both \(k\) and \(j\) are maximizers of \(r(n-r)\) under \(k\leq j\). For even \(n=2m\), this gives only \((k,j)=(m,m)\), with ideal dimension \(2m=n\). For odd \(n=2m+1\), it gives exactly \((m,m),(m,m+1),(m+1,m+1)\), of dimensions \(n-1,n,n+1\). Each maximal term is monic in \(q\).

Every term in the first case has \(q\)-degree \((n-k)(k+1)\), at most \(\lfloor(n+1)^2/4\rfloor\), which is strictly less than \(2\lfloor n^2/4\rfloor\) when \(n\geq4\). All other second-case terms have strictly lower degree. Dividing each coefficient by the total number \(F_{n,q}(1)\) now shows the stated concentration and the equiprobable three-point limit. No simultaneous limit in \(n\) and \(q\) is asserted.

## Verification

The standalone Python file `verify_star_ideals.py` uses only the standard library. It enumerates all reduced-row-echelon subspace bases of \(\mathbb F_q^{2n+1}\) for the specified small prime fields, directly tests the bracket against the full Lie-algebra basis, and compares the histogram of ideal dimensions against the displayed formula. It does not identify ideals by the classification used in the proof. Exhaustive checks passed for \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\). The corresponding dimension histograms are

\[
\begin{array}{c|c|l}
 n&q&\text{ideal counts in dimensions }0,\ldots,2n+1\\\hline
 1&2&(1,1,3,1)\\
 1&3&(1,1,4,1)\\
 1&5&(1,1,6,1)\\
 2&2&(1,3,7,7,7,1)\\
 2&3&(1,4,13,13,13,1)\\
 3&2&(1,7,35,43,43,35,15,1)
\end{array}
\]

Additional evaluations of the exact formula at \(q=257\) and \(n=4,5,6,7\) confirm the predicted high-field concentration numerically. Run `python3 verify_star_ideals.py` from a directory containing that file; success prints `VERIFY_OK`. These finite tests corroborate but do not prove the identities for all fields and dimensions: the unrestricted proof is given above.

## Relationship to prior work

Barrionuevo and Tirao's graph-Lie-algebra work establishes the construction and investigates rigidity over characteristic-zero fields [1]. DeCoste, DeMeyer, Mainkar and Ray explicitly study star-graph Lie algebras and their abelian factors; their Theorem 3.2 concerns the dimension of the abelian factor (for distinct edge labels it is zero), not the distribution of all ideals over finite fields [2]. Benito and Roldán-López investigate Lie algebras with a finite *field-independent* ideal lattice over characteristic zero, not the finite-field ideal-counting polynomial for this family [3]. Rossmann studies graphical-group centralizer/conjugacy-class counts, not Lie-ideal dimensions [4]. An abelian-factor calculation, rigidity classification, or centralizer distribution does not determine the ideal-count polynomial by implication alone.

The elementary subspace-lifting argument is included in full; any earlier equivalent finite-field ideal-count formula should take precedence. The claim is the explicit all-dimension polynomial and its large-field corollary, not originality of graph Lie algebras, Gaussian coefficients, or the general idea of projecting ideals along the center.

## Limitations

Only the distinctly labeled star construction is treated; repeated edge labels give other Lie algebras. The result counts linear Lie ideals, not Lie subalgebras, normal subgroups of associated finite \(p\)-groups, or submodule zeta functions over integer lattices. The large-field limit fixes \(n\geq4\); low-dimensional exceptions are not covered by that asymptotic statement. A search of relevant primary publications did not establish whether an older equivalent formula appears under generalized-Heisenberg, module-invariant-subspace, or finite-group language; publication priority requires further expert scrutiny. The computational verifier covers small prime fields, not arbitrary extension fields or infinite parameter ranges.

## References

[1] J. Barrionuevo and P. Tirao, *Rigid 2-step graph Lie algebras*, arXiv:2206.10572 (first public 2022-06-21). https://arxiv.org/abs/2206.10572

[2] R. DeCoste, L. DeMeyer, M. Mainkar and A. Ray, *Abelian Factor in 2-step Nilpotent Lie Algebras Constructed from Graphs*, arXiv:2208.09541 (first public 2022-08-19), especially Section 3. https://arxiv.org/abs/2208.09541

[3] P. Benito and J. Roldán-López, *Lie Algebras with a finite number of ideals*, arXiv:1911.01957 (2019). https://arxiv.org/abs/1911.01957

[4] T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (2021). https://arxiv.org/abs/2107.05564
