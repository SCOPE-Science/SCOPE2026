# Exact angular-chain singular spectrum of geometric tree Toeplitz operators

## Finding

Let \(b\geq2\) be an integer and \(0<r<1\). On the rooted homogeneous \(b\)-ary tree, let \(T=\Delta M_\varphi\nabla\) have radial symbol \(\varphi(v)=r^{|v|}\), with the definitions below. Then \(T\) extends boundedly to the vertex Hilbert space \(\ell^2(V)\) if and only if \(br^2<1\). In that range it is compact, and it admits the exact orthogonal-sum decomposition

\[
T\simeq\bigoplus_{k=0}^{\infty}(r^k A_{b,r})^{\oplus d_k},\qquad
 d_0=1,\quad d_k=(b-1)b^{k-1}\quad(k\geq1),
\]

where \(A_{b,r}\) acts on \(\ell^2(\mathbb N_0)\) and has entries

\[
(A_{b,r})_{i,j}=\begin{cases}
r^i,&i=j,\\
(r-1)r^{j-1}b^{(j-i)/2},&i<j,\\
0,&i>j.
\end{cases}
\]

Consequently the *entire multiset of positive singular values* is \(\{r^k s_j(A_{b,r}): k\geq0,\,j\geq1\}\), with each \(k\)-th scale repeated \(d_k\) times (including any multiplicities within the one-chain operator). Write \(q_c=\log b/\log(1/r)\in(0,2)\) and \(\gamma=\log(1/r)/\log b=1/q_c\). For every real \(q>q_c\),

\[
\operatorname{Tr}|T|^q=\frac{1-r^q}{1-br^q}\operatorname{Tr}|A_{b,r}|^q,
\qquad
\lim_{q\downarrow q_c}(q-q_c)\operatorname{Tr}|T|^q
=\frac{1-b^{-1}}{\log(1/r)}\operatorname{Tr}|A_{b,r}|^{q_c}>0.
\]

There are explicit positive constants \(c,C\), depending only on \(b,r\), such that for all integers \(j\geq1\),

\[
cj^{-\gamma}\leq s_j(T)\leq Cj^{-\gamma}.
\]

In particular \(T\in\mathcal S_q\) exactly for \(q>q_c\), and \(T\in\mathcal S_{q_c,\infty}\setminus\mathcal S_{q_c}\). Its Hilbert--Schmidt norm is exactly

\[
\|T\|_{\mathcal S_2}^2=
\frac{1+b(1-r)^2/(1-br^2)}{1-br^2}.
\]

## Assumptions and scope

The vertex set consists of finite words over \(\{1,\dots,b\}\), including the empty root word. Let \(|v|\) be word length and \(S_v\) the descendant sector including \(v\). On finitely supported functions define

\[
(\nabla f)(v)=f(v)-\sum_{w\text{ child of }v}f(w),\qquad
(\Delta g)(v)=\sum_{w\in S_v}g(w),\qquad
(M_\varphi g)(v)=r^{|v|}g(v).
\]

The operator initially means \(\Delta M_\varphi\nabla\) on finitely supported functions; its unique bounded extension is considered if it exists. All Hilbert spaces and Schatten ideals are complex. The finite-branching and radial-positive hypotheses are essential to the stated direct-sum formula. The one-chain operator is itself trace class and belongs to every positive Schatten class.

## Proof

**1. Kernel and sharp boundedness domain.** Interchanging finite sums gives

\[
T_{u,v}=\begin{cases}
r^{|u|},&u=v,\\
(r-1)r^{|v|-1},&u\text{ is a proper ancestor of }v,\\
0,&\text{otherwise}.
\end{cases}
\]

Indeed, the coefficient of \(f(v)\) in the sector sum is \(\varphi(v)-\varphi(v^-)\) for a proper descendant and \(\varphi(u)\) on the diagonal. The root row has squared \(\ell^2\) norm \(1+b(1-r)^2\sum_{h\geq0}(br^2)^h\). Thus no bounded extension exists when \(br^2\geq1\), because an output coordinate of a bounded operator must define a bounded functional on \(\ell^2\). When \(br^2<1\), the row indexed by any vertex of depth \(n\) has squared norm

\[
r^{2n}C_0^2,\qquad C_0^2=1+\frac{b(1-r)^2}{1-br^2}.
\]

There are \(b^n\) vertices at depth \(n\), so summation proves both the Hilbert--Schmidt formula and compactness. Moreover \(M_\varphi\nabla f\in\ell^1\) for every \(f\in\ell^2\): multiplication uses \(\varphi\in\ell^2\) and \(\nabla\) is bounded on \(\ell^2\), since the child-sum operator has norm \(\sqrt b\). Hence the matrix extension agrees with the defining product.

**2. Exact angular-wavelet decomposition.** Set \(H_n=\ell^2(\{1,\dots,b\}^n)\). If \(m\geq n\), let \(E_{n,m}:H_n\to H_m\) replicate each coefficient to every depth-\(m\) descendant with factor \(b^{-(m-n)/2}\). These are isometries satisfying \(E_{m,\ell}E_{n,m}=E_{n,\ell}\). Put \(W_0=H_0\) and \(W_k=H_k\ominus E_{k-1,k}H_{k-1}\) for \(k\geq1\). Their dimensions are \(d_0=1\) and \(d_k=(b-1)b^{k-1}\). Choose an orthonormal basis \(\mathcal B_k\) for each \(W_k\). For \(\xi\in\mathcal B_k\), the vectors \(E_{k,k+i}\xi\), placed in depth \(k+i\), form an orthonormal half-line, and all such half-lines from all \(k,\xi\) constitute an orthonormal basis of \(\ell^2(V)\). Orthogonality across distinct starting depths follows because \(W_k\) is perpendicular to replicated coefficients from earlier levels.

The kernel depends only on ancestral relation and depth, so it does not mix these half-lines. For input depth \(k+j\) and output depth \(k+i\), with \(i<j\), summing the \(b^{j-i}\) descendants of each output vertex contributes the replication factor \(b^{(j-i)/2}\); the resulting coefficient is \((r-1)r^{k+j-1}b^{(j-i)/2}\). Diagonal entries are \(r^{k+i}\). Thus the restriction to every half-line starting at depth \(k\) is precisely \(r^k A_{b,r}\), establishing the unitary equivalence. This also gives an explicit constructive unitary, not merely an equality of singular-value counts.

**3. One-chain exponential singular decay.** The restriction of \(A_{b,r}\) to output indices \(i\geq N\), acting on the input tail \(j\geq N\), is unitarily \(r^N A_{b,r}\). Truncating its first \(N\) output rows therefore gives a rank-at-most-\(N\) operator with error norm at most \(r^N\|A_{b,r}\|\). Thus \(s_{N+1}(A_{b,r})\leq r^N\|A_{b,r}\|\), and every positive-power singular-value sum is finite. Its Hilbert--Schmidt norm is \(\|A_{b,r}\|_{\mathcal S_2}^2=C_0^2/(1-r^2)\).

**4. Exact singular-value zeta and its pole.** Taking \(q\)-powers and summing the singular values of the orthogonal sum gives

\[
\operatorname{Tr}|T|^q
=\operatorname{Tr}|A_{b,r}|^q\left(1+\sum_{k\geq1}(b-1)b^{k-1}r^{kq}\right)
=\frac{1-r^q}{1-br^q}\operatorname{Tr}|A_{b,r}|^q
\]

when \(br^q<1\). The sum diverges for \(br^q\geq1\), since \(A_{b,r}\ne0\). Continuity of the one-chain trace at \(q_c>0\) follows from exponential singular decay. Expanding \(1-br^q\) at \(q_c\) proves the stated positive residue.

**5. Uniform sharp singular-value exponent.** Let \(P_n\) project onto level \(n\), dimension \(b^n\). The compression \(P_nTP_n=r^n I\), hence \(s_{b^n}(T)\geq r^n\). For any \(j\geq1\), choose \(n=\lceil\log_b j\rceil\); then \(s_j(T)\geq rj^{-\gamma}\). For the opposite inequality, let \(Q_{\geq N}\) project onto all levels at least \(N\). Its output restriction \(Q_{\geq N}T\), with the first \(N\) input levels ignored automatically, is the direct sum of \(b^N\) rescaled subtree copies of \(T\), so \(\|Q_{\geq N}T\|=r^N\|T\|\). The complementary first \(N\) output levels have dimension \(R_N=(b^N-1)/(b-1)\), implying \(s_{R_N+1}(T)\leq r^N\|T\|\). If \(R_N+1\leq j\leq R_{N+1}\), then \(j<b^{N+1}/(b-1)\), giving

\[
s_j(T)\leq\|T\|\left(\frac{b}{b-1}\right)^\gamma j^{-\gamma}
\leq\frac{C_0}{\sqrt{1-br^2}}\left(\frac{b}{b-1}\right)^\gamma j^{-\gamma}.
\]

Thus one can take \(c=r\) and the displayed explicit upper constant. Together with the zeta divergence at the critical exponent, this proves the stated weak-Schatten borderline.

## Verification

The accompanying standalone `checker.py` constructs finite tree matrices and their angular-chain bases. It verifies every one of 907 rational block inner products exactly in three configurations, along with finite Hilbert--Schmidt sums. Three additional floating-point comparisons of complete finite singular spectra on 63-, 63-, and 85-dimensional truncations had maximum discrepancies below \(5\times10^{-16}\). Run with `python checker.py` after installing NumPy. These checks test finite instances; the infinite direct-sum, Schatten threshold, and zeta residue follow from the proof above, not from extrapolating finite numerical data.

## Relationship to prior work

Colonna and Martínez-Avendaño introduced tree Toeplitz operators of the form \(\Delta M_\varphi\nabla\). Huang, Zhang and Zhao studied their spectra, positivity and finite rank on tree \(\ell^p\) spaces in arXiv:2301.08370v1 (public January 20, 2023). The subsequent journal abstract also mentions compactness and Schatten-membership criteria, so **Schatten membership as a qualitative concept is not claimed new**. Orthogonal radial/tree-harmonic decompositions are also familiar from spectral analysis of regular trees, including work by Kazun and Szwarc. The contribution asserted here is the explicit angular-block unitary equivalence for this nonself-adjoint Toeplitz operator, the full singular-value multiset and zeta-factorization formula with its exact positive critical residue, plus matching two-sided approximation-number power bounds. These quantitative statements do not follow solely from a general boundedness/compactness criterion or a qualitative Schatten-membership test.

## Limitations

The theorem requires an exactly homogeneous rooted tree, a geometric positive radial symbol, and the unweighted vertex \(\ell^2\) Hilbert space. The critical exponent is strictly below two because \(br^2<1\). It makes no assertion for \(r=1\) or for arbitrary radial profiles, irregular branching, other \(\ell^p\) norms, or all symbols covered by the earlier literature. The singular-value formula gives the full multiset in terms of one explicit compact one-chain operator but does not solve that operator's singular values in elementary closed form. The published journal version of the closest paper was not available for complete theorem-by-theorem comparison; an equivalent formula therein or in uncatalogued literature remains a possible originality risk. The scientific review here is not independent validation.

## References

1. M. Huang, X. Zhang and X. Zhao, *Toeplitz operators on \(\mathcal L^p\)-spaces of a tree*, arXiv:2301.08370v1 (first posted January 20, 2023); journal version, *Mediterranean Journal of Mathematics* 20 (2023), DOI:10.1007/s00009-023-02526-8.
2. F. Colonna and R. A. Martínez-Avendaño, original definition and foundational study of Toeplitz operators on tree \(\ell^p\) spaces (as cited and discussed in arXiv:2301.08370v1, introductory and preliminary sections).
3. V. Kazun and R. Szwarc, *Jacobi matrices on trees*, arXiv:0903.3547 (tree-harmonic orthogonal decomposition precedent, but a different self-adjoint operator family).
