# Sharp negative-type exponent and endpoint dimension for nonsymmetric Steiner incidence metrics

## Finding
Let \(\mathcal D\) be a finite Steiner \(2\)-\((v,k,1)\) design with \(k\ge3\), with \(r=(v-1)/(k-1)>k\) blocks through each point and \(b=vr/k>v\) blocks in total. On the vertices of the unit-edge point–block incidence graph \(X\), use shortest-path distance \(d\). Define the supremal negative-type exponent by
\[
\wp(X)=\sup\left\{p\ge0:\sum_{x,y\in X}\xi_x\xi_y d(x,y)^p\le0\text{ for every real }\xi\text{ with }\sum_x\xi_x=0\right\}.
\]
Then
\[
\boxed{\wp(X)=\log_2\!\left(\frac{k}{k-1}\right).}
\]
The metric \(d^{p/2}\) admits an isometric embedding into real Hilbert space exactly for \(0<p\le\wp(X)\). At the endpoint its least affine embedding dimension is \(2v-1\), while for every \(0<p<\wp(X)\) the least affine dimension is \(v+b-1\). The endpoint equality subspace has dimension \(b-v\), consisting precisely of the real block-side incidence dependencies. All statements are independent of the isomorphism type of the design.

## Assumptions and scope
A Steiner \(2\)-\((v,k,1)\) design has \(v\) points, blocks of size \(k\), and exactly one block through any pair of distinct points. By elementary double counting, every point lies in \(r=(v-1)/(k-1)\) blocks and \(b=vr/k\). The assumption \(r>k\) excludes symmetric designs, which have distinct spectral behavior. Write \(N\) for the real \(v\)-by-\(b\) incidence matrix, so that
\[
NN^{\mathsf T}=(r-1)I_v+J_v,
\qquad N\mathbf1_b=r\mathbf1_v,
\qquad N^{\mathsf T}\mathbf1_v=k\mathbf1_b.
\]
Here \(J\) is an all-ones matrix of the indicated size. These identities imply \(\operatorname{rank}N=v\). Every two points have distance \(2\); a point and an incident (respectively nonincident) block have distance \(1\) (respectively \(3\)); distinct intersecting (respectively disjoint) blocks have distance \(2\) (respectively \(4\)). For disjoint blocks, a length-four path exists using the unique connecting block through a chosen point of each.

## Proof
**1. Powered-distance matrix.** Put \(a=2^p\), \(t=3^p\), and \(c=4^p=a^2\). The matrix \(D_p=(d(x,y)^p)_{x,y\in X}\), ordered with points first and blocks second, has blocks
\[
D_{PP}=a(J_v-I_v),\quad D_{PB}=tJ_{v,b}+(1-t)N,
\quad D_{BB}=cJ_b+(a-c)N^{\mathsf T}N+((k-1)c-ka)I_b.
\]
Its diagonal is zero. Conditional negative semidefiniteness means that the quadratic form of \(D_p\) is nonpositive on \(\mathbf1_{v+b}^{\perp}\).

**2. Exact orthogonal reduction.** The identity \(NN^{\mathsf T}=(r-1)I_v+J_v\) gives \(v-1\) nonconstant singular values \(\sqrt{r-1}\) and one constant singular value \(\sqrt{rk}\), with \(\ker N\subset\mathbf1_b^\perp\) of dimension \(b-v\). Thus the zero-sum space decomposes orthogonally into the block kernel, \(v-1\) paired mean-zero singular spaces, and the one-dimensional constant-population direction.

On \(\ker N\) the powered-distance quadratic form has eigenvalue
\[
h(p)=(k-1)c-ka=a((k-1)a-k).
\]
This vanishes exactly when \(a=k/(k-1)\) and is positive for every larger \(p\). A nonzero vector in \(\ker N\) therefore proves failure of negative type above the proposed threshold.

**3. Negativity of all other modes at the threshold.** Set \(p_*=\log_2(k/(k-1))\), \(a_*=k/(k-1)\), and \(t_*=3^{p_*}\). Every mean-zero coupled singular space has quadratic-form matrix
\[
M(p)=\begin{pmatrix}
-a &(1-t)\sqrt{r-1}\\
(1-t)\sqrt{r-1}&a(r-k-1)+c(k-r)
\end{pmatrix}.
\]
At \(p_*\), its lower diagonal entry equals \(-a_*(r-1)/(k-1)\), and
\[
\det M(p_*)=(r-1)\left(\frac{a_*^2}{k-1}-(t_*-1)^2\right)>0.
\]
For the strict inequality, write \(\beta=\log_2 3<5/3\), noting \(3^3<2^5\). If \(k\ge4\), then the mean-value theorem and \(a_*-1=1/(k-1)\) give
\[
t_*-1=a_*^\beta-1<\frac{\beta a_*}{k-1}<\frac{a_*}{\sqrt{k-1}},
\]
since \(5/3<\sqrt3\le\sqrt{k-1}\). For \(k=3\), \(a_*=3/2\) and \(t_*<(3/2)^{5/3}<2\), so \(t_*-1<1<a_*/\sqrt2\). Hence each \(M(p_*)\) is negative definite.

For the remaining constant-population direction choose \(z=(b\mathbf1_v,-v\mathbf1_b)\). Direct expansion gives \(z^{\mathsf T}D_p z=vbS(p)\), where
\[
S(p)=b(v-1)a+v\left[k(r-1)a+(b-1-k(r-1))c\right]
-2v\left[r+(b-r)t\right].
\]
The double-counting identities simplify this, at \(p_*\), to
\[
S(p_*)=-rv-2v(b-r)\left(t_*-\frac{a_*+c_*}{2}\right)<0.
\]
Indeed \(p_*\in(0,1)\) for \(k\ge3\), so strict concavity of \(x\mapsto x^{p_*}\) gives \(3^{p_*}>(2^{p_*}+4^{p_*})/2\). Since \(b>r\), this proves the claimed strict negativity.

**4. Sharp exponent and rank.** At \(p_*\), exactly the \(b-v\) dimensions of \(\{(0,y):Ny=0\}\) vanish in the zero-sum powered-distance form; all other directions are strictly negative. The nonzero kernel witness makes negative type impossible for every \(p>p_*\). The Schoenberg nesting theorem yields strict \(p\)-negative type for all \(0\le p<p_*\). Its embedding theorem identifies this with isometric Hilbert embeddability of \(d^{p/2}\). For a finite metric the minimum affine Hilbert embedding dimension is the rank of its centered negative half-powered-distance Gram matrix, hence \((v+b-1)-(b-v)=2v-1\) at the threshold and \(v+b-1\) below it. This completes the classification.

## Verification
The standalone `steiner_negative_type_check.py` uses independent breadth-first-search distances and symmetric-matrix diagonalization for four explicitly reconstructed Steiner incidence designs: affine-plane examples of orders \(3\) and \(5\), and non-affine binary Steiner triple systems on \(15\) and \(31\) points. It checks combinatorial distances, incidence identities, conditional eigenvalue signs on either side of the endpoint, and the predicted endpoint ranks. Run `python steiner_negative_type_check.py` with NumPy version at least \(1.24\). The finite tests corroborate but do not replace the arbitrary-design proof.

For the binary Steiner triple system on \(15\) points, there are \(35\) blocks; the endpoint exponent is \(\log_2(3/2)\) and its minimum Hilbert embedding dimension is \(29\), dropping from the subcritical value \(49\). The full algebraic proof also covers nonlinear/nonisomorphic Steiner systems because only the incidence identities are used.

## Relationship to prior work
Robertson's 2020 maximal-generalized-roundness paper provides general methods for finite metrics, but does not evaluate these point–block incidence metrics. Robertson's 2023 paper provides the negative-type/Hilbert equivalence and examples involving complete bipartite and Hamming metrics, not this classification. Design libraries and spectral incidence studies supply combinatorial context rather than the present exact threshold. The affine-plane subfamily has previously been examined; its already-known special case is not claimed independently. The contribution here is the full nonsymmetric Steiner \(2\)-design class, including non-affine binary triple systems, and the arbitrary-design endpoint nullity formula \(b-v\). The full texts of the two Robertson preprints were examined in relevant definitions and results sections; an equivalent earlier calculation under another design/Levi-graph terminology remains possible.

## Limitations
The statement assumes \(k\ge3\), \(\lambda=1\), \(r>k\), the unweighted incidence graph and real Hilbert targets. It excludes symmetric designs, weighted incidence metrics, and general \(2\)-designs with \(\lambda>1\). Existence of a design with given parameters is not asserted. It does not classify other embedding norms, or give an independent assessment of mathematical priority.

## References
1. G. Robertson, *The Maximal Generalised Roundness Of Finite Metric Spaces*, arXiv:2004.10923, first posted 2020-04-23; https://arxiv.org/abs/2004.10923.
2. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070, first posted 2023-09-27; https://arxiv.org/abs/2309.16070.
3. D. Heinlein, D. Ivanov, B. McKay and P. Östergård, *A library of combinatorial 2-designs*, DOI:10.5281/zenodo.8262680 (2023); https://doi.org/10.5281/zenodo.8262680.
4. Schoenberg's classical Hilbert-embedding and strict-negative-type nesting theorems, as stated in reference 2, Theorem 1.2.
