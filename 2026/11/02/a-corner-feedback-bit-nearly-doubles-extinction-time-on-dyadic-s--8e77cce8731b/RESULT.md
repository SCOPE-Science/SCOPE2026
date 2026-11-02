# A corner feedback bit nearly doubles extinction time on dyadic square grids

## Finding

For each integer \(a\ge2\), put \(L=2^a\), \(s=L-1\), and \(D=s^2\). On the \(s\times s\) grid, let \(N\) be synchronous binary four-neighbor parity updating with zero exterior boundary, and change **only the upper-left corner** by adding its own previous bit to its update. Write the resulting linear map over \(\mathbb F_2\) as \(B=N+ee^{\mathsf T}\), where \(e\) is that corner's coordinate vector.

The complete rational Jordan decomposition is
\[
B\ \sim\ J_1(1)\oplus J_1(0)\oplus J_{2L-1}(0)\oplus J_L(0)^{\oplus(L-4)}.
\]
The multiplicity \(L-4\) is zero at \(L=4\). Thus there are exactly two periodic states, both fixed; the maximum first-entry time into the fixed-point set is \(2L-1\), and it is achieved.

Let \(T(x)\) be the smallest nonnegative integer for which \(B^{T(x)}x\) is fixed. Define \(r_t=\operatorname{rank}_{\mathbb F_2}(B^t)\). The exact labelled-state census is
\[
r_0=D,\qquad
r_t=\begin{cases}
(L-2)(L-t)+t,&1\le t\le L,\\
2L-t,&L\le t\le2L-1,\\
1,&t\ge2L-1,
\end{cases}
\]
and, for every integer \(t\ge0\),
\[
\#\{x:T(x)\le t\}=2^{D+1-r_t},\qquad
\#\{x:T(x)=t\}=\#\{T\le t\}-\#\{T\le t-1\}\quad(t\ge1).
\]
In particular \(\Pr(T=2L-1)=1/2\) under uniform initialization. By contrast, the original uniform rule has decomposition \(N\sim J_1(0)\oplus J_L(0)^{\oplus(L-2)}\), so every configuration extinguishes within \(L\) updates; that smaller bound is sharp. One feedback bit therefore changes global extinction into convergence to one of two fixed states and increases the sharp transient length from \(L\) to \(2L-1\).

## Assumptions and scope

The vertices are the ordered pairs \((i,j)\) with \(0\le i,j<s\). Outside-grid states are zero and are not variables. For every vertex other than \((0,0)\), the next bit equals the XOR of the available north, south, east and west neighbors; at \((0,0)\), it equals the XOR of the two available neighbors and its own bit. All updates are simultaneous. Graph vertices are labelled; no quotient by rotations, reflections, or other graph automorphisms is taken. All algebra is over \(\mathbb F_2\), and \(a\ge2\) is essential to the displayed uniform block formula.

## Proof

**1. The unperturbed polynomial model.** For the path on \(s\) vertices, write \(A_s\) for its symmetric adjacency matrix. Its characteristic polynomials obey \(f_0(u)=1\), \(f_1(u)=u\), and \(f_{m+1}(u)=u f_m(u)+f_{m-1}(u)\). In characteristic two, the same recurrence gives \(f_{2m+1}(u)=u f_m(u)^2\). Iterating along indices one less than powers of two yields \(f_{L-1}(u)=u^{L-1}\). The corner basis vector is cyclic for \(A_s\): the coefficient at distance \(j\) in \(A_s^j e_0\) is one, and in all earlier vectors is zero. Therefore \(A_s\) is one nilpotent Jordan block of size \(s\).

Under the two Krylov bases, the grid state space becomes \(R=\mathbb F_2[x,y]/(x^{L-1},y^{L-1})\), the corner vector \(e\) becomes the constant polynomial one, and \(N=A_s\otimes I+I\otimes A_s\) acts by multiplication by \(z=x+y\). Frobenius gives \(z^L=x^L+y^L=0\). Moreover \(z^{L-1}\ne0\) in \(R\), since all binomial coefficients of degree \(L-1\) are one modulo two and the surviving terms \(x^i y^{L-1-i}\), \(1\le i\le L-2\), are distinct nonzero monomials. Hence \(N\) has exact nilpotence index \(L\), and \(e\) generates a maximal length-\(L\) Jordan summand.

**2. All unperturbed Jordan blocks.** Set \(S=\mathbb F_2[x,y]/(x^L,y^L)\). The change \(z=x+y\) identifies \(S\) with \(\mathbb F_2[z,y]/(z^L,y^L)\), free of rank \(L\) over \(K=\mathbb F_2[z]/(z^L)\). To recover \(R\), first quotient by \(y^{L-1}\), leaving \(K^{L-1}\), with basis \(1,y,\ldots,y^{L-2}\). Now impose \(x^{L-1}=0\). Since \(x x^{L-1}=0\) already in \(S\), the ideal it generates is exactly its \(K\)-span. In the displayed basis, its generator becomes \(z w\), where
\[
w=\sum_{j=0}^{L-2}z^{L-2-j}y^j.
\]
The coefficient of \(y^{L-2}\) in \(w\) is the unit one, so \(w\) is a primitive basis vector over \(K\). Quotienting the generated summand by \(z w\) replaces one copy of \(K\) by \(K/(z)\). Consequently, as a module under multiplication by \(z\),
\[
R\cong K^{L-2}\oplus K/(z),\qquad
N\sim J_L(0)^{\oplus(L-2)}\oplus J_1(0).
\]
In particular \(\operatorname{rank}N^t=(L-2)(L-t)\) for \(1\le t\le L\).

**3. The corner's vanishing return moments.** Put \(\mu_j=e^{\mathsf T}N^j e\). We have \(\mu_0=1\). For \(j>0\), \(\mu_j\) is the parity of length-\(j\) closed grid walks from \((0,0)\) to itself. Exchanging the two grid coordinates pairs these walks, with no fixed positive-length walk: a fixed walk would remain on the diagonal at every step, whereas each available edge changes exactly one coordinate. Thus \(\mu_j=0\) for every \(j>0\). Since \(N^L=0\), all moments beyond \(L-1\) are zero for that reason also.

Write \(u_i=N^i e\) and \(\varphi_j=e^{\mathsf T}N^j\), for \(0\le i,j<L\). Both collections are linearly independent, the latter because \(N\) is symmetric. The resolvent identity for rank-one feedback, together with \(e^{\mathsf T}(I-tN)^{-1}e=1\), gives the identity
\[
B^k=N^k+\sum_{\substack{0\le i,j<L\\i+j\le k-1}}u_i\varphi_j\qquad(k\ge1).
\]
One may also obtain it by expanding \((I-tB)^{-1}=(I-tN)^{-1}+\frac{t}{1+t}(I-tN)^{-1}ee^{\mathsf T}(I-tN)^{-1}\) over \(\mathbb F_2[[t]]\).

**4. Ranks before the unperturbed extinction time.** For \(1\le k\le L\), put \(U_k=\operatorname{span}(u_0,\ldots,u_{k-1})\) and \(W_k=U_k^\perp=\bigcap_{j=0}^{k-1}\ker\varphi_j\). Because \(e\) is a maximal cyclic generator, its \(L\)-chain splits off as an \(N\)-invariant direct summand. Thus \(U_k\cap\operatorname{im}N^k=0\). The displayed power identity shows that the image of \(B^k\) modulo \(\operatorname{im}N^k\) has dimension \(k\): the coefficients are invertible triangular combinations of the independent functionals \(\varphi_0,\ldots,\varphi_{k-1}\), while the vectors \(u_0,\ldots,u_{k-1}\) stay independent in the quotient. The kernel of this projected map is \(W_k\), on which \(B^k=N^k\).

To verify that \(N^k(W_k)=\operatorname{im}N^k\), take orthogonal complements. Symmetry of \(N\) implies \((N^kW_k)^\perp=\{v:N^k v\in U_k\}=\ker N^k\), the second equality using \(U_k\cap\operatorname{im}N^k=0\). Thus \(N^kW_k=\operatorname{im}N^k\) as claimed. It follows that
\[
\operatorname{rank}B^k=\operatorname{rank}N^k+k=(L-2)(L-k)+k.
\]

**5. Long chains and terminal rank.** The power identity gives
\[
P:=B^{2L-1}=\left(\sum_{i=0}^{L-1}u_i\right)\left(\sum_{j=0}^{L-1}\varphi_j\right).
\]
This is a rank-one idempotent because the row times the column equals \(\mu_0=1\), all other moments vanishing. Also \(BP=PB=P\). For \(L\le k\le2L-1\),
\[
B^k+P=\sum_{\substack{0\le i,j<L\\i+j\ge k}}u_i\varphi_j.
\]
The coefficient matrix has an invertible anti-triangular submatrix of dimension \(2L-1-k\), and all other rows and columns zero; the independent \(u_i\)'s and \(\varphi_j\)'s preserve that rank. Its image is in \(\ker P\), disjoint from \(\operatorname{im}P\). Therefore \(\operatorname{rank}B^k=1+(2L-1-k)=2L-k\) in this range, and \(B^k=P\) for all \(k\ge2L-1\).

Finally, the successive rank losses uniquely determine the nilpotent Jordan blocks. The stabilized idempotent supplies one eigenvalue-one block of length one, while the ranks reconstruct one block of length \(2L-1\), \(L-4\) blocks of length \(L\), and one block of length one, all at eigenvalue zero. The cumulative entry-time count follows because the nilpotent coordinates must be killed by time \(t\), while the one-dimensional fixed coordinate is arbitrary.

## Verification

`corner_grid_verify.py` is a standalone Python standard-library verifier. It constructs each update from the actual labelled grid-neighborhood rule and independently computes binary ranks of all matrix powers for \(a=2,3,4,5\), covering grids with \(9,49,225,961\) sites and every relevant power through stabilization. It checks both the modified and unmodified rules against the proved rank expressions. The script also enumerates all \(512\) initial configurations on the \(3\times3\) grid, obtaining the entry-time shells \((2,6,8,16,32,64,128,256)\), and tests \(4000\) additional pseudorandom trajectories on the \(7\times7\) grid. The recorded output is in `verification_output.txt` and terminates with `CORNER_GRID_FEEDBACK_VERIFY_OK`. Finite checks corroborate but do not substitute for the preceding all-\(a\) proof.

## Relationship to prior work

The unperturbed polynomial and Kronecker-sum framework is classical. Barua and Ramakrishnan (1996) derive path polynomials, the special powers-of-two-minus-one case, and null-boundary grid invertibility statements. Choudhury et al. (arXiv:0804.2346, first publicly submitted 15 April 2008) present matrix models for homogeneous and hybrid two-dimensional linear rules. Chang and Akın (arXiv:1609.09572, first publicly submitted 30 September 2016) derive general Kronecker-sum and generalized-Jordan approaches to finite multidimensional rules with uniform local coefficients. General positive-characteristic Jordan theory for Kronecker sums likewise concerns the unperturbed factorization.

None of the specific inspected statements gives the **single-corner feedback** block decomposition, its nearly doubled maximal transient, or the exact all-height stopping-time shells. The vertex-local inhomogeneous term is not the homogeneous self-term used in ordinary sigma-plus rules. The complete original text of Dihidar and Choudhury (2004), on exceptional two-dimensional transformations, could not be inspected, so historical equivalence with a previously analyzed exceptional hybrid rule remains a residual risk; the available abstract alone cannot settle that comparison.

## Limitations

The theorem applies only to binary states, synchronous parity updating, open square grids with side \(2^a-1\), \(a\ge2\), and feedback at a corner. It does not classify defects in the interior, other side lengths, or other fields. The claimed originality is relative to the literature and records actually examined, not a proof that an unindexed equivalent cannot exist. Computational enumeration was exhaustive only for the \(3\times3\) case; larger tests were rank calculations or samples. Independent mathematical validation has not been performed.

## References

1. R. Barua and S. Ramakrishnan, “\(\sigma\)-Game, \(\sigma^+\)-Game and Two-Dimensional Additive Cellular Automata,” *Theoretical Computer Science* **154** (1996), 349–366, doi:10.1016/0304-3975(95)00091-7.
2. P. P. Choudhury, B. K. Nayak, S. Sahoo and S. P. Rath, “Theory and Applications of Two-dimensional, Null-boundary, Nine-Neighborhood, Cellular Automata Linear rules,” arXiv:0804.2346, 15 April 2008.
3. C.-H. Chang and H. Akın, “Reversibility Problem of Multidimensional Finite Cellular Automata,” arXiv:1609.09572, 30 September 2016.
4. K. Dihidar and P. P. Choudhury, “Matrix algebraic formulae concerning some exceptional rules of two-dimensional cellular automata,” *Information Sciences* **165** (2004), 91–101, doi:10.1016/j.ins.2003.09.024 (abstract inspected; complete text unavailable).
5. “On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic,” *Linear and Multilinear Algebra* **56** (2008), doi:10.1080/03081080701395640 (abstract inspected).
