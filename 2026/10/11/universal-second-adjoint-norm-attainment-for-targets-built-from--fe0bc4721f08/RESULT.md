# Universal second-adjoint norm attainment for targets built from finite-dimensional \(\ell_1\)-blocks

## Finding
Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), let \(X\ne\{0\}\) be any Banach space over \(\mathbb K\), and let \(\Gamma\ne\varnothing\) be an arbitrary index set. For each \(\gamma\in\Gamma\), choose a nonzero finite-dimensional Banach space \(F_\gamma\) over \(\mathbb K\), with **no uniform bound on its dimension**. Put
\[
Y=\left(\bigoplus_{\gamma\in\Gamma}F_\gamma\right)_{\ell_1},
\quad\|(y_\gamma)\|_Y=\sum_{\gamma\in\Gamma}\|y_\gamma\|_{F_\gamma}.
\]
Then **every** bounded operator \(T:X\to Y\) has a norm-attaining second adjoint:
\[
\boxed{\operatorname{NA}_2(X,Y)=\mathcal L(X,Y).}
\]
Precisely, for each nonzero \(T\), there is \(\xi\in S_{X^{**}}\) satisfying \(\|T^{**}\xi\|=\|T\|\). The zero operator also attains its norm because \(S_{X^{**}}\ne\varnothing\).

A representative nonscalar target is \(Y=(\bigoplus_{n\ge1}\ell_2^n)_{\ell_1}\), with unbounded Hilbertian block dimensions. The new assertion is the universal **target-pair** result for arbitrary finite-dimensional block geometries, not the previously established scalar \(\ell_1\) case.

## Assumptions and scope
The \(\ell_1\)-sum is taken with its canonical isometric block norm; blocks need not share a model norm or have uniformly bounded dimension. The index set may be uncountable. \(T^{**}:X^{**}\to Y^{**}\) is the canonical second adjoint of \(T\). Norm attainment means existence of a unit vector attaining the **operator norm**, not merely a maximizing sequence or a norm-attaining first adjoint. No assumption of separability, reflexivity, approximation property, positivity or compactness is made on \(X\) or \(T\).

## Proof
**1. Compactness in each block.** Normalize \(\|T\|=1\) and pick \(x_n\in S_X\) such that \(\|Tx_n\|_Y\to1\). Write \(u_n=Tx_n\). Each \(u_n\) has countable support, and the union \(S\) of these supports is countable: for a vector in an \(\ell_1\)-sum, each set where the coordinate norm exceeds \(1/k\) is finite. Thus we may enumerate \(S\). Since every \(F_\gamma\) is finite-dimensional, diagonal compactness gives a subsequence (relabelled \(u_n\)) whose \(\gamma\)-coordinates converge in norm for every \(\gamma\in S\). Denote their limit by \(u_\gamma\), and use zero coordinates elsewhere. Fatou's inequality for finite partial sums yields \(u=(u_\gamma)\in Y\) and \(t:=\|u\|\le1\).

**2. A disjoint-support splitting.** Put \(z_n=u_n-u\). Then \(z_n(\gamma)\to0\) in each block. Choose inductively a further subsequence \(z_{n_j}\) and nested finite index sets \(H_0=\varnothing\subset H_1\subset H_2\subset\cdots\) so that
\[
\|P_{H_{j-1}}z_{n_j}\|<2^{-j-1},\qquad
\|(I-P_{H_j})z_{n_j}\|<2^{-j-1}.
\]
The first bound follows from convergence on each fixed finite set; the second follows from the defining \(\ell_1\)-summability of each vector. Write \(D_j=H_j\setminus H_{j-1}\), \(b_j=P_{D_j}z_{n_j}\). Then the \(D_j\)'s are pairwise disjoint and finite, and \(\|z_{n_j}-b_j\|<2^{-j}\). In particular, \(\|u_{n_j}-(u+b_j)\|\to0\). Since \(\sum_j\|P_{D_j}u\|\le t\), the coordinate mass \(\|P_{D_j}u\|\) tends to zero, and the elementary disjoint-support estimate gives
\[
0\le t+\|b_j\|-\|u+b_j\|\le2\|P_{D_j}u\|\longrightarrow0.
\]
As \(\|u_{n_j}\|\to1\), this proves
\[
\|b_j\|\longrightarrow1-t. \tag{1}
\]

**3. Ultralimit and norm preservation.** Fix a free ultrafilter \(\mathcal U\) on \(\mathbb N\), and define \(\xi\in X^{**}\) by
\[
\xi(x^*)=\lim_{j\to\mathcal U}x^*(x_{n_j})\qquad(x^*\in X^*).
\]
Then \(\|\xi\|\le1\). Using the canonical embeddings into second duals, one has
\[
T^{**}\xi=J_Yu+\mathrm{w^*\!\!-}\lim_{j\to\mathcal U}J_Yb_j. \tag{2}
\]
We prove its norm is exactly one, without assuming any unproved direct-sum decomposition of \(Y^{**}\).

Fix \(\varepsilon>0\). Pick a finite set \(H\subset\Gamma\) with \(\|P_Hu\|\ge t-\varepsilon\). All sufficiently late \(D_j\)'s are disjoint from \(H\). Define one functional \(f_\varepsilon=(f_{\varepsilon,\gamma})\) in
\[
B_{Y^*}=B_{(\bigoplus_{\gamma\in\Gamma}F_\gamma^*)_{\ell_\infty}}
\]
as follows: on \(H\), choose component functionals of norm at most one satisfying \(f_{\varepsilon,\gamma}(u_\gamma)=\|u_\gamma\|\); on each late \(D_j\), choose them satisfying \(f_{\varepsilon,\gamma}(b_j(\gamma))=\|b_j(\gamma)\|\); set them zero elsewhere. The assignments are compatible because \(H\) and the late \(D_j\)'s are pairwise disjoint. The Hahn--Banach theorem gives these functionals over either scalar field. Then
\[
\operatorname{Re}f_\varepsilon(u)\ge t-2\varepsilon,
\qquad f_\varepsilon(b_j)=\|b_j\|\quad\text{for all sufficiently large }j.
\]
Apply \(f_\varepsilon\) to (2) and use (1):
\[
\|T^{**}\xi\|\ge\operatorname{Re}(T^{**}\xi)(f_\varepsilon)
\ge (t-2\varepsilon)+(1-t)=1-2\varepsilon.
\]
Since this holds for every \(\varepsilon>0\), and \(\|T^{**}\xi\|\le\|T\|\|\xi\|\le1\), equality follows. Thus also \(\|\xi\|=1\), proving the theorem.

## Verification
The argument checks an arbitrary, possibly nonseparable source; reduces the particular maximizing sequence to countably many active target blocks; extracts a coordinatewise convergent subsequence using finite dimensionality; constructs finite, disjoint blocks with a quantitative norm error; and uses one bounded dual functional for each \(\varepsilon>0\) to establish the bidual norm. Every limiting operation has a designated topology, and the same functional is valid simultaneously for all sufficiently late disjoint blocks. This is a purely analytic proof: it requires no finite experiment or external computational certificate.

The result is false if arbitrary infinite-dimensional blocks are allowed. Indeed, in the one-block Hilbert-space case \(X=Y=\ell_2\), the diagonal map
\[
Te_n=\frac{n}{n+1}e_n \quad(n\ge1)
\]
has norm \(1\) but never attains it on \(S_{\ell_2}\); reflexivity implies \(T^{**}=T\), so its second adjoint also fails to attain. This is a boundary illustration, **not** a characterization of all infinite-dimensional blocks.

## Relationship to prior work
Dantas, Jung and Martín establish universal second-adjoint norm attainment for \(\ell_1\) endomorphisms (Theorem 3.17), extend this to \(\ell_1(\Gamma)\) endomorphisms (Remark 3.20), and separately give universal second-adjoint norm attainment for endomorphisms on \(c_0\)-sums of finite-dimensional spaces (Remark 3.4). The scalar-block case with arbitrary source is already a consequence of their \(\ell_1\) result: a norm-one metric quotient \(\ell_1(S_X)\to X\) transfers a bidual maximizing point from the composed map, after representing its scalar \(\ell_1\) target as a coordinate summand. This scalar case is **not** claimed as new.

The present theorem handles \(\ell_1\)-sums whose individual blocks have arbitrary finite-dimensional norms, with unbounded dimensions, and supplies an explicit blockwise gliding-hump proof for all source spaces. The prior \(c_0\)-sum result addresses a different direct-sum norm and only the diagonal pair of spaces. A related published result on third-adjoint norm attainment for pairs of isometric \(\ell_1\)-preduals concerns a different adjoint level and different class of target spaces.

## Limitations
The theorem concerns isometric \(\ell_1\)-direct sums of **finite-dimensional** spaces. No conclusion is asserted for general isomorphic renormings or for blocks of arbitrary infinite dimension. The proof does not show that \(T\) or \(T^*\) attains its norm; prior work supplies examples with a non-norm-attaining first adjoint. The new generality lies in unrestricted finite-dimensional block geometries, not in the already covered scalar \(\ell_1\) case. Earlier, differently phrased structural results on L-embedded spaces or disjoint-support sequences could still provide equivalent coverage.

## References
1. Sheldon Dantas, Mingu Jung, Miguel Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794v1 (public submission 2026-09-01), Theorem 3.17, Remarks 3.4 and 3.20, and Proposition 2.12. https://arxiv.org/abs/2609.00794
2. *Third-adjoint norm attainment for all isometric \(\ell_1\)-predual pairs*, public mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-third-adjoint-norm-attainment-for-all-isometric-ell-1-predual-pa--219f642b555a
