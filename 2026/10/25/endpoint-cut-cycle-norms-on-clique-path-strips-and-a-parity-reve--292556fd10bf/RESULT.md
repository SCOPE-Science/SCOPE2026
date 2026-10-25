# Endpoint cut--cycle norms on clique--path strips and a parity reversal

## Finding

Let \(G_{m,n}=K_m\square P_n\) be the unit-edge Cartesian product of a complete graph with a path, where \(m\ge3\) and \(n\ge4\) are integers. Give the real edge-coordinate space the ordinary \(\ell_1\) norm. Let \(Q\) be its *canonical Euclidean-orthogonal cut projection* and \(P=I-Q\) its complementary cycle projection. The formulas also hold for the induced edge-\(\ell_\infty\) norms because both matrices are symmetric.

Put
\[
\rho=\frac{m+2-\sqrt{m(m+4)}}2,\qquad
\delta=\sqrt{m(m+4)},\qquad
a=\lfloor n/2\rfloor,\quad b=\lceil n/2\rceil,
\]
\[
A=\frac{\rho^a+\rho^b}{1+\rho^n},\qquad
D=\frac{(1-\rho^{2a})(1-\rho^{2b})}{1-\rho^{2n}}.
\]
Then **every norm-maximizing column of the cut projection corresponds to a path-direction edge in a central path interval**, and
\[
\boxed{\|Q\|_{1\to1}=3-\frac2m-\frac{2(m-1)}m A.}
\]
For the complementary cycle projection there is an exact orbit switch:
\[
\boxed{
\|P\|_{1\to1}=\begin{cases}
\displaystyle \frac73-\frac{2\rho}{1-\rho}\,
\frac{\rho^{\lfloor(n-1)/2\rfloor}+\rho^{\lceil(n-1)/2\rceil}}{1-\rho^n}, &m=3,\\[8pt]
\displaystyle \frac{2(m-1)}m(1-A)+\frac{2(m-1)}\delta D,&m\ge4.
\end{cases}}
\]
For \(m=3\), a central *clique-direction edge* maximizes \(\|P\|\); for every \(m\ge4\), a central *path-direction edge* does. In addition, the ordering of the two canonical norms is determined completely:
\[
\boxed{
\begin{array}{ll}
\|Q\|>\|P\|,&m=3\text{ and }n\text{ even},\\
\|P\|>\|Q\|,&m=3\text{ and }n\text{ odd},\\
\|P\|>\|Q\|,&m\ge4.
\end{array}}
\]
Thus widening the clique from three to four destroys an exact parity reversal for *every* path length at least four.

## Assumptions and scope

The graph is simple, unweighted and connected. Its vertices are \((c,x)\), where \(1\le c\le m\), \(0\le x<n\). Clique edges join distinct \(c\) at fixed \(x\), while path edges join \((c,x)\) and \((c,x+1)\). Each edge is assigned any reference orientation; changing orientations conjugates both projections by a diagonal sign matrix and does not affect these norms. If \(B\) is the oriented vertex--edge incidence matrix, then \(Q=B^{\mathsf T}(BB^{\mathsf T})^+B\) and \(P=I-Q\). Superscript \(+\) means the Moore--Penrose inverse. These are *canonical orthogonal* projections, not minimum-norm projections among all choices. The norm is the induced matrix operator norm, namely the largest absolute column sum.

## Proof

**1. Product reduction.** Write \(D_0\) for the \(n\)-vertex path incidence matrix, and \(L_0=D_0D_0^{\mathsf T}\). The clique Laplacian is \(m(I-\Pi)\) with \(\Pi=\mathbf1\mathbf1^{\mathsf T}/m\). Hence the product Laplacian has the two spectral blocks \(L_0\) and \(mI+L_0\). Put
\[
R=(mI_n+L_0)^{-1},\quad
E=(mI_{n-1}+D_0^{\mathsf T}D_0)^{-1},\quad
T=D_0^{\mathsf T}RD_0=I_{n-1}-mE.
\]
The entries of \(E\) are strictly positive. Its tridiagonal inverse operator has diagonal \(m+2\) and both neighboring diagonals \(-1\); consequently \(0<T_{jj}<1\) and \(T_{ij}<0\) for \(i\ne j\). The positive Green matrix \(R\) has column sums \(1/m\), each of its columns increases toward its source and then decreases, and for the dipole \(u=R(\mathbf e_{j+1}-\mathbf e_j)\), the entries are negative up to \(j\), positive from \(j+1\), with \(\sum_x|u_x|=2E_{jj}\). The last identity follows by summing \((mI+L_0)u=\mathbf e_{j+1}-\mathbf e_j\) over vertices to the right of the edge: \(m\sum_{x>j}u_x+u_{j+1}-u_j=1\), and \(u_{j+1}-u_j=T_{jj}=1-mE_{jj}\).

**2. The exact two column families.** For a clique edge at path level \(x\), its absolute cut-column sum and complementary cycle-column sum are respectively
\[
H_x=\frac{2(m-1)}m+4R_{xx}-2(R_{0x}+R_{n-1,x}),\qquad
H'_x=3-\frac2m-2(R_{0x}+R_{n-1,x}). \tag{1}
\]
Indeed the total absolute clique-edge response is \(2(m-1)\sum_yR_{yx}=2(m-1)/m\); the two nonzero clique components of the path response contribute \(2\sum_j|R_{j+1,x}-R_{jx}|=4R_{xx}-2(R_{0x}+R_{n-1,x})\). The source-edge diagonal is \(2R_{xx}\), yielding \(H'_x=1+H_x-4R_{xx}\).

For a path edge at level \(j\), let \(S_j=\sum_{i=0}^{n-2}E_{ij}\). The corresponding absolute column sums are
\[
V_j=1+2(m-1)S_j,\qquad V'_j=2(m-1)(S_j+E_{jj}).\tag{2}
\]
To see this, the uniform clique mode puts total absolute path current exactly \(1\) on the source interval. Every other path interval contributes \(2(m-1)E_{ij}\), summed over \(i\ne j\); the induced clique-edge current contributes \(2(m-1)E_{jj}\). The path-edge diagonal is \(1-(m-1)E_{jj}\), proving both equations.

**3. Green kernel and middle positions.** Set \(\rho+\rho^{-1}=m+2\), so \(0<\rho\le(5-\sqrt{21})/2<1/4\) for \(m\ge3\), and \(\delta=\rho^{-1}-\rho\). The exact inverse formulas, verifiable by the tridiagonal recurrence and endpoint conditions, give
\[
R_{xx}=\frac{(1+\rho^{2x+1})(1+\rho^{2n-2x-1})}{\delta(1-\rho^{2n})},\qquad
R_{0x}+R_{n-1,x}=\frac{\rho}{1-\rho}\frac{\rho^x+\rho^{n-1-x}}{1-\rho^n},\tag{3}
\]
\[
S_j=\frac1m\left(1-\frac{\rho^{j+1}+\rho^{n-1-j}}{1+\rho^n}\right),\qquad
E_{jj}=\frac1\delta\frac{(1-\rho^{2(j+1)})(1-\rho^{2(n-1-j)})}{1-\rho^{2n}}.\tag{4}
\]
For fixed positive exponent sum, the sum of two powers of \(\rho\) is minimized when the exponents are as balanced as possible. Similarly the product \((1-\rho^{2u})(1-\rho^{2v})\) is largest when \(u,v\) are balanced. It follows from (4) that \(V_j,V'_j\) are maximal at the central path edge(s), and from (3) that \(H'_x\) is maximal at the middle clique layer(s). Substituting \(a,b\) produces the stated three candidate formulas.

**4. Path columns dominate the cut norm.** We show for every \(x\) that
\[
H_x\le F_m:=\frac{2(m-1)}m+\frac4\delta.\tag{5}
\]
For completeness, write \(u=\rho^x\), \(v=\rho^{n-1-x}\). By (3), (5) is equivalent to
\[
2\rho(u^2+v^2)+4\rho^{2n}
\le(1+\rho)(1+\rho^n)(u+v).
\]
Since \(u^2+v^2\le u+v\), \(u+v\ge2\rho^{n-1}\), and \(2\rho^{n+1}\le1-\rho\) for \(n\ge4\), \(\rho<1/4\), this follows directly. At \(m=3\), (4) gives \(V_{\mathrm{middle}}=51/23>4/3+4/\sqrt{21}=F_3\) already for \(n=4\). For \(m\ge4\), the central path cut-column value at \(n=4\) is
\[
V_{\mathrm{middle}}(m,4)=1+\frac{2(m-1)(m+4)}{m^2+4m+2},
\]
which is increasing in \(m\) and at \(m=4\) is \(41/17>9/4\). Direct squaring shows \(F_m\le9/4\) for every \(m\ge4\): it reduces to \(m^3+20m^2-128m+256\ge0\), valid from \(m=4\) onward. The central values \(S_j\), and therefore \(V_j\), strictly increase with path length by positivity and domain monotonicity of the tridiagonal Dirichlet Green matrix. Thus all cut maxima are path columns for \(m\ge3,n\ge4\).

**5. The sharp cycle-column switch.** First suppose \(m=3\). At \(n=4\), the middle clique column is \(11/5\) and the largest path column is \(48/23\). For \(n\ge5\), the middle clique expression \(H'_x\) strictly increases with \(n\) and is at least its \(n=5\) value \(199/87\). On the other hand \(V'_j\le 2(m-1)(1/m+1/\delta)=4/3+4/\sqrt{21}<199/87\) by (4). Thus a middle clique edge strictly dominates all path columns.

Next let \(m=4\). At \(n=4\), the largest path cycle-column value is \(42/17>29/12\), the largest clique cycle-column value. At \(n=5\), the former equals \(2982/1189>5/2\), whereas every clique cycle column is strictly below \(3-2/m=5/2\). For \(n\ge5\), path cycle-column maxima increase strictly with \(n\) as above. Finally for \(m\ge5\), already at \(n=4\) the largest path cycle column equals
\[
\frac{4(m-1)(m+3)}{m^2+4m+2}>3-\frac2m,
\]
whose strict inequality is equivalent to \(m^3-2m^2-10m+4>0\), true for all integers \(m\ge5\). The same Green monotonicity covers every \(n\ge4\). This proves the cycle formulas and edge-orbit classification.

**6. Which canonical projection is larger?** For \(m\ge4\) both norms occur at a central path edge, so (2) gives
\[
\|P\|_{1\to1}-\|Q\|_{1\to1}=2(m-1)E_{jj}-1.
\]
Monotonicity in \(n\) and (4) show this is at least
\[
\frac{m^2-2m-6}{m^2+4m+2}>0\qquad(m\ge4).
\]
For \(m=3\), subtract the middle clique formula from the middle path formula. When \(n=2r\) is even, the sign is the sign of
\[
\frac{1+\rho}{(1-\rho)(1-\rho^{2r})}-\frac{4/3}{1+\rho^{2r}},
\]
which is positive because \(\rho>1/7\). When \(n=2r+1\ge5\) is odd, the sign is that of
\[
\frac{2\rho}{(1-\rho)(1-\rho^n)}-\frac23\frac{1+\rho}{1+\rho^n},
\]
which is negative: \(\rho<1/4\) and \(n\ge5\) imply \(3\rho(1+\rho^n)<(1-\rho^2)(1-\rho^n)\). This finishes the parity and clique-size classification.

## Verification

The independent-coordinate, exact-rational checker `check_clique_path.py` constructs the entire grounded product Laplacian, inverts it using fractions, and computes every column of both orthogonal projections. It independently constructs the two reduced Green matrices and checks the formulas in (1)--(2) column by column. Its eight tested graphs have \(327\) edge columns, giving \(654\) exact cut/cycle column-sum comparisons. All assertions passed. Its testing of finitely many graphs is not the all-parameter proof; steps 1--6 above supply the analytical argument.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023) develop invariant and minimal projections of graph cycle spaces and treat discrete tori and Hamming graphs in detail. The 2018 predecessor develops the Lipschitz-free-space quotient and recursive diamond/Laakso projection framework. This result concerns a *non-transitive open-boundary product* \(K_m\square P_n\), determines norms of the specified canonical projections, and derives a sharp edge-direction and parity ordering absent from the inspected relevant sections. The earlier case of three path layers and the cyclic product \(K_m\square C_n\) are excluded from the theorem's parameter range or geometry and are not newly claimed. Search and literature comparisons do not prove exhaustive novelty.

## Limitations

Only real, unit-edge Cartesian products with \(m\ge3,n\ge4\) are covered. Norms are canonical Euclidean-orthogonal projection norms, not minimal projection constants. The findings do not cover weighted graphs, arbitrary product factors, or complex nonorthogonal projections. Residual originality risk includes less-indexed equivalent transfer-current identities and uninspected specialized graph-network material. Independent mathematical audit has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 2023-05-21), https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (2018), https://arxiv.org/abs/1807.03814.
