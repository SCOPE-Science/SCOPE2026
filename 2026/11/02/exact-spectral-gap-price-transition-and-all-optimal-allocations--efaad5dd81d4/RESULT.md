# Exact spectral-gap price transition and all optimal allocations for matching-priced complete bipartite networks

## Finding

Let \(m\ge3\) be an integer. The graph is the complete bipartite graph \(K_{m,m}\), with labeled vertex classes \(\{L_1,\ldots,L_m\}\) and \(\{R_1,\ldots,R_m\}\). Every edge \(L_iR_j\) has an independently chosen nonnegative conductance \(w_{ij}\). A distinguished perfect matching, consisting of the \(m\) edges with \(i=j\), has price \(P>0\) per unit conductance; the \(m(m-1)\) other edges have price \(Q>0\). Given \(B>0\), impose
\[
P\sum_{i=1}^m w_{ii}+Q\sum_{i\ne j}w_{ij}\le B.
\]
Write \(L(W)\) for the ordinary combinatorial weighted Laplacian on the \(2m\) vertices and \(\lambda_2(W)\) for its second-smallest eigenvalue (including its value zero when the positive support is disconnected). Define the exact threshold
\[
P_c=\frac{2(m-1)}{m-2}Q.
\]
The unrestricted maximum of \(\lambda_2(W)\) is
\[
\boxed{\max_W\lambda_2(W)=
\begin{cases}
\dfrac{B}{P+(m-1)Q},&0<P\le P_c,\\[2mm]
\dfrac{(m-2)B}{m(m-1)Q},&P\ge P_c.
\end{cases}}
\]
The formulas agree at equality, and **every** maximizing allocation is as follows.

* For \(P<P_c\), the unique maximizing matrix is constant on *all* edges:
\[
w_{ij}=\frac{B}{m(P+(m-1)Q)}\qquad(1\le i,j\le m).
\]
* For \(P>P_c\), the unique maximizing matrix deletes the entire distinguished matching and is constant on the remaining edges:
\[
w_{ii}=0,\qquad w_{ij}=\frac{B}{m(m-1)Q}\quad(i\ne j).
\]
The resulting positive-support graph is the connected crown graph \(K_{m,m}-M\).
* At \(P=P_c\), all maximizing matrices, and no others, have a common matching conductance \(a\), a common nonmatching conductance \(b\), and satisfy
\[
0\le a\le b,\qquad mPa+m(m-1)Qb=B.
\]
Thus the boundary contains a genuine one-parameter continuum of distinct global optimizers. No symmetry constraint was imposed in the optimization.

## Assumptions and scope

The conductances are symmetric continuous-time transition rates, so \(L(W)\) generates the Markov semigroup \(e^{-tL(W)}\) with uniform stationary distribution whenever the positive-support graph is connected. The objective is the *continuous-time* spectral gap, not the second-largest eigenvalue modulus of a discrete-time stochastic matrix, the effective resistance, the spanning-tree determinant, or the minimum hitting time. Exactly two positive price classes and one positive linear budget are used. The graph size satisfies \(m\ge3\); this ensures the crown graph remains connected. Zero edge rates are permitted.

## Proof

**1. Two universal trace bounds.** Put \(A=\sum_iw_{ii}\) and \(N=\sum_{i\ne j}w_{ij}\). Let \(H=I_m-\mathbf1\mathbf1^{\mathsf T}/m\) and define the mutually orthogonal, \((m-1)\)-dimensional subspaces
\[
E_+=\{(x,x):\mathbf1^{\mathsf T}x=0\},\qquad
E_-=\{(x,-x):\mathbf1^{\mathsf T}x=0\}.
\]
Their orthogonal projectors are
\[
\Pi_+=\tfrac12\begin{pmatrix}H&H\\H&H\end{pmatrix},\qquad
\Pi_-=\tfrac12\begin{pmatrix}H&-H\\-H&H\end{pmatrix}.
\]
For an edge vector \(g_{ij}=(e_i,-e_j)\), direct calculation gives
\[
\|\Pi_+g_{ij}\|^2=\begin{cases}0,&i=j,\\1,&i\ne j,\end{cases}
\qquad
\|\Pi_-g_{ij}\|^2=\begin{cases}2-2/m,&i=j,\\1-2/m,&i\ne j.\end{cases}
\]
Since \(L(W)=\sum_{i,j}w_{ij}g_{ij}g_{ij}^{\mathsf T}\), and both subspaces lie in \(\mathbf1^\perp\), the Rayleigh minimum and the projector traces yield **without any orbit reduction**
\[
\lambda_2(W)\le U:=\frac{\operatorname{tr}(\Pi_+L(W))}{m-1}=\frac{N}{m-1},
\]
\[
\lambda_2(W)\le V:=\frac{\operatorname{tr}(\Pi_-L(W))}{m-1}
=\frac{2A}{m}+\frac{(m-2)N}{m(m-1)}.
\]
Whenever \(\lambda_2(W)\) equals either trace average, every vector of the corresponding subspace belongs to the \(\lambda_2(W)\)-eigenspace. Indeed \(L(W)-\lambda_2(W)I\) is positive semidefinite on \(\mathbf1^\perp\); zero trace against a projector onto that subspace forces its quadratic form and hence its action to vanish on that subspace.

**2. Optimal-value certificates.** First suppose \(P<P_c\). The number
\[
\theta=1-\frac{mP}{2(P+(m-1)Q)}
\]
lies strictly between zero and one. The previous bounds imply
\[
\lambda_2(W)\le\theta U+(1-\theta)V
=\frac{PA+QN}{P+(m-1)Q}
\le\frac{B}{P+(m-1)Q}.
\]
For \(P\ge P_c\), the second trace bound instead yields
\[
\lambda_2(W)\le V\le
\frac{m-2}{m(m-1)Q}(PA+QN)
\le\frac{(m-2)B}{m(m-1)Q}.
\]
For \(P>P_c\), the middle inequality is strict if \(A>0\).

**3. Attainment and spectral factors.** Put \(w_{ii}=a\) and \(w_{ij}=b\) for \(i\ne j\). The weighted bipartite adjacency block is \(W=(a-b)I_m+b\mathbf1\mathbf1^{\mathsf T}\), and every vertex has degree \(a+(m-1)b\). The Laplacian spectrum, with multiplicities, is
\[
\{\,0,\ \underbrace{mb,\ldots,mb}_{m-1},\
\underbrace{2a+(m-2)b,\ldots,2a+(m-2)b}_{m-1},\
2[a+(m-1)b]\,\}.
\]
For \(P<P_c\), taking \(a=b=B/[m(P+(m-1)Q)]\) attains the first bound. For \(P>P_c\), taking \(a=0\) and \(b=B/[m(m-1)Q]\) attains the second. At equality \(P=P_c\), every class-constant choice with \(0\le a\le b\) and full budget has smallest positive eigenvalue \(2a+(m-2)b\), attaining the common upper bound.

**4. Exhaustion and unrestricted uniqueness.** For any optimizer, the budget is saturated, because scaling every weight up increases a positive spectral gap. Equality in the certificates forces \(E_-\) to consist entirely of eigenvectors for the optimum eigenvalue \(\lambda_*\): this holds in both price regimes, including their boundary, because the coefficient of \(V\) in the cheap certificate is positive.

Write the completely unrestricted conductance matrix as \(W=(w_{ij})\), with row-sum diagonal \(D_L\) and column-sum diagonal \(D_R\). The eigenvector condition for every \(x\perp\mathbf1\) is
\[
(D_L+W)x=\lambda_*x,\qquad(D_R+W^{\mathsf T})x=\lambda_*x.
\]
Taking \(x=e_j-e_k\) with \(j,k\ne i\) shows that in each row all off-diagonal \(w_{ij}\) are equal; the transposed equation similarly makes each column's off-diagonal entries equal. For \(m\ge3\), the graph of off-diagonal matrix positions is connected by shared rows and columns; consequently all \(w_{ij}\), \(i\ne j\), equal one common \(b\). The diagonal row equation then reads
\[
\lambda_*=(m-2)b+2w_{ii},
\]
so every \(w_{ii}\) is the same common \(a\). Thus **every** optimum, without an a priori symmetry assumption, is class-constant.

If \(P<P_c\), equality in the positively weighted trace certificate additionally forces \(E_+\) into the same eigenspace. The explicit eigenvalues on \(E_+\) and \(E_-\) are \(mb\) and \(2a+(m-2)b\), giving \(a=b\), hence the stated unique allocation. If \(P>P_c\), strictness of the price comparison unless \(A=0\) gives \(a=0\); budget saturation fixes \(b\) uniquely. Finally, at \(P=P_c\), the class-constant spectrum reaches the certificate precisely when \(2a+(m-2)b\le mb\), equivalently \(a\le b\); the budget then describes exactly the stated segment. This proves all assertions.

## Verification

The accompanying `verify.py` uses exact symbolic characteristic-polynomial factors for four network sizes, exact rational checks of the three price regimes and the critical segment, and independent numerical diagonalization of 2,160 independently generated non-symmetric rate matrices. Its reproducible run returned `PASS: 4506 exact symbolic/rational and independent numerical checks`. These computations are supplementary; they do not substitute for the two-subspace trace certificates and equality analysis above. Run with `python verify.py` in an environment with NumPy and SymPy installed.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate the general continuous-time fastest-mixing process as a weighted-conductance semidefinite optimization problem and work out selected graph examples, including paths. The inspected original establishes the general framework, not this two-price matching perturbation of a balanced complete bipartite graph or the unrestricted boundary optimizer classification. Ghosh, Boyd and Saberi (2006 conference proceedings; 2008 journal article) develop total-effective-resistance minimization and discuss Laplacian spectral-gap optimization as a different associated objective. Their resistance objective does not imply the displayed spectral-gap price threshold. Boyd, Diaconis, Parrilo and Xiao (2007 preprint, 2009 journal) examine symmetry reductions for the *discrete-time* SLEM objective; equality of mathematical formulations cannot be assumed across these two mixing metrics.

The present result does not claim novelty for Fourier/block diagonalization, convexity of the spectral-gap objective, the spectrum of an unweighted complete bipartite graph, or the general priced SDP. Its specific contribution is the exact two-price phase boundary, matching deletion, strict-phase unrestricted uniqueness, and complete boundary optimizer segment. Mathematical priority remains subject to specialist literature not accessible in full.

## Limitations

The theorem assumes balanced sides, a complete bipartite underlying graph, a single distinguished perfect matching, identical costs within each of two edge classes, symmetric continuous-time rates, and \(m\ge3\). It does not assert an analogous result for unequal bipartition sizes, arbitrary cost matrices, arbitrary stationary masses, or discrete-time SLEM. The self-review is not independent validation. The exact matching-priced continuous-time classification should be subjected to separate specialist priority verification, especially against treatments under different graph or process terminology.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI `10.1137/S0036144504443821`. Public original: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf ; publisher public date 2006-11-02.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, 2006-07-24 to 2006-07-28, pp. 1185–1196; conference original: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; extended journal paper SIAM Review **50** (2008), 37–66, DOI `10.1137/050645452`.
3. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first submitted 2007-09-06; SIAM Journal on Optimization **20** (2009), 792–819, https://arxiv.org/abs/0709.0955 . Its discrete-time objective differs from the present one.
