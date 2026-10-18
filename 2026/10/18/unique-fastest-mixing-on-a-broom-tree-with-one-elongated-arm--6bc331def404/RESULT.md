# Unique fastest mixing on a broom tree with one elongated arm

## Finding
For every integer \(n\ge3\), form the diameter-three tree \(B_n\) with four vertex types: one leaf \(u\), its neighbor \(v\), a second hub \(w\), and the \(n\) leaves \(z_1,\ldots,z_n\) at \(w\). Its edges are \(uv\), \(vw\), and \(wz_i\) for all \(i\). Put
\[
D=n^2+n-1,\qquad
(a_*,b_*,c_*)=\left(\frac{n(n-1)}D,\frac{2n-1}D,\frac{n-1}D\right).
\]
The **unique globally fastest-mixing** symmetric stochastic transition matrix assigns transition probabilities \(a_*\), \(b_*\), and \(c_*\) to these three respective kinds of edges. It assigns zero holding probability to both hubs and the remaining probability to the leaves. Its smallest possible second-largest eigenvalue modulus is
\[
\mu_* =\frac{n^2}{n^2+n-1},\qquad 1-\mu_*=\frac{n-1}{n^2+n-1}.
\]
Uniqueness holds among **all** feasible symmetric stochastic matrices, even without imposing exchangeability of the \(n\) leaves. The same rational weight formula fails to optimize the five-vertex case \(n=2\).

## Assumptions and scope
Here \(n\) denotes the number of leaves incident with \(w\), so that \(B_n\) has \(n+3\) vertices. A feasible matrix \(P\) is real, symmetric, nonnegative, row-stochastic, and has off-diagonal entries only along graph edges; diagonal holding entries are allowed. For \(J\) the all-ones matrix of order \(n+3\), define \(\mu(P)=\|P-J/(n+3)\|_2\). Since the graph is connected, \(\mu(P)\) is the maximum modulus of the eigenvalues other than the stationary eigenvalue \(1\); the definition also applies if the stationary eigenvalue is repeated. The objective is \(\min_P\mu(P)\), with no reversibility constraints beyond symmetry and uniform stationary distribution. The classification applies only for \(n\ge3\).

## Proof
### 1. Symmetry reduction
For every permutation \(\sigma\) of the right-hand leaves, relabeling a feasible matrix gives another feasible matrix with the same objective. Matrix operator norm is convex, so averaging over all such permutations cannot increase \(\mu\). Hence a globally optimal **invariant** matrix exists. An invariant kernel is determined by nonnegative \(a,b,c\) representing the probabilities on \(uv\), \(vw\), and each \(wz_i\). Nonnegative diagonal entries are equivalent to
\[
a+b\le1,\qquad b+nc\le1.\]
The \(n-1\)-dimensional space of vectors supported on \(z_1,\ldots,z_n\) with coordinate sum zero consists of eigenvectors with eigenvalue \(1-c\). In particular
\[\mu(P)\ge1-c.\tag{1}\]

### 2. Sharp Rayleigh certificate
In the indicated order \((u,v,w,z_1,\ldots,z_n)\), take the zero-sum vector
\[
x=(n^2,\ n(n-1),\ 0,\ -(2n-1),\ldots,\ -(2n-1)).\]
Its squared norm is \(N=n^4+n^2(n-1)^2+n(2n-1)^2\). For the weighted graph Laplacian \(L=I-P\), its Dirichlet energy is
\[
E=x^{\mathsf T}Lx=n^2a+n^2(n-1)^2b+n(2n-1)^2c.
\]
By the variational characterization of the greatest nontrivial eigenvalue \(\lambda_2(P)\),
\[\mu(P)\ge\lambda_2(P)\ge1-E/N.\tag{2}\]
For \(n\ge3\), the feasibility constraints imply
\[
\begin{aligned}
E&\le n^2+n^3(n-2)b+n(2n-1)^2c\\
 &\le n^2(n-1)^2+c\bigl(n(2n-1)^2-n^4(n-2)\bigr).
\end{aligned}
\]
The coefficient of \(c\) in the last line is strictly negative: \(n^3(n-2)>(2n-1)^2\) for every integer \(n\ge3\). (At \(n=3\) the difference is \(2\); the difference increases with \(n\), since the derivative of \(n^3(n-2)-(2n-1)^2\) is positive for real \(n\ge3\).)
Define \(c_*=(n-1)/D\). Direct polynomial substitution gives
\[n^2(n-1)^2+c_*\bigl(n(2n-1)^2-n^4(n-2)\bigr)=Nc_* .\]
Consequently if \(c\ge c_*\), then \(E\le Nc_*\), so (2) gives \(\mu(P)\ge1-c_*=n^2/D\). If \(c<c_*\), (1) gives the strict inequality \(\mu(P)>1-c_*=n^2/D\). Thus every invariant feasible kernel satisfies \(\mu(P)\ge\mu_*\). Equality requires \(c=c_*\), \(a+b=1\), and \(b+nc=1\), because the two intermediate upper bounds are strict unless the corresponding hub row is saturated. These equations force \(a=a_*\), \(b=b_*\). Hence **there is at most one invariant optimizer**.

### 3. The certificate is attained
At these weights, both hub holding probabilities vanish. On the four-dimensional invariant subspace (constant on all \(z_i\)), the quotient transition matrix is
\[
Q=\begin{pmatrix}
1-a_*&a_*&0&0\\
a_*&0&b_*&0\\
0&b_*&0&nc_*\\
0&0&c_*&1-c_*
\end{pmatrix}.
\]
Although \(Q\) is not literally symmetric in its displayed basis, it is similar to a real symmetric matrix by multiplying the last coordinate by \(\sqrt n\). Its characteristic polynomial is
\[
\det(tI-Q)=(t-1)(t-\mu_*)\left(t^2+\frac{n(n-1)}D t+\frac{n^3-5n^2+4n-1}{D^2}\right).
\]
Call the quadratic factor \(q_n(t)\). Exact identities give
\[
q_n(-\mu_*)=\frac{(n-1)^2(2n-1)}{D^2}>0,\quad
q_n(\mu_*)=\frac{(n-1)(2n^3+2n^2-3n+1)}{D^2}>0.
\]
The vertex of this upward quadratic is \(-n(n-1)/(2D)\), strictly between \(-\mu_*\) and \(\mu_*\); both roots are real because \(Q\) is symmetrizable. Both roots therefore lie strictly inside this interval (they cannot both lie beyond the same endpoint, which would put the quadratic vertex beyond that endpoint). The other \(n-1\) eigenvalues are all \(1-c_*=\mu_*\). Thus \(\mu(P_*)=\mu_*\), proving optimality and the unique invariant optimum.

### 4. No nonsymmetric optimal kernels
Let \(P\) be any globally optimal feasible matrix, without assuming invariance. Averaging its leaf permutations produces the unique invariant optimum \(P_*\). The edge \(uv\) and hub bridge \(vw\) are fixed by these permutations; therefore their weights in \(P\) are already \(a_*\) and \(b_*\). If \(c_i=P_{wz_i}\), averaging gives \(\sum_i c_i=nc_*\), and the holding probability at \(w\) is zero. Put \(d_i=c_i-c_*\).
For every \(z\in\mathbb R^n\) with \(\sum_i z_i=0\), extend \(z\) by zero on \(u,v,w\). Its Rayleigh quotient under \(P\) is
\[
\frac{z^{\mathsf T}Pz}{z^{\mathsf T}z}
=1-\frac{\sum_i c_i z_i^2}{\sum_i z_i^2}
\le\mu_*=1-c_*.
\]
Hence \(\sum_i d_i z_i^2\ge0\) on the zero-sum subspace. The compression of \(\operatorname{diag}(d_1,\ldots,d_n)\) to that subspace is positive semidefinite and has trace \((n-1)\sum_i d_i/n=0\). It is therefore the zero operator. Taking \(z=e_i-e_j\) yields \(d_i+d_j=0\) for every \(i\ne j\); because \(n\ge3\), all \(d_i=0\). Thus \(P=P_*\), proving **global uniqueness**.

### 5. Boundary at two leaves
For \(n=2\), the candidate weights predicted by the displayed formula are \((a,b,c)=(2/5,3/5,1/5)\), with SLEM \(4/5\). The feasible alternative \((a,b,c)=(1/2,1/2,1/4)\) has SLEM strictly below \(4/5\). Exact Sylvester-principal-minor tests of both \((4/5)I\pm(P-J/5)\) establish this strict inequality (see the standalone checker). This is only a boundary counterexample, not a classification of \(n=2\).

## Verification
The attached `verify_broom.py` executes polynomial identity checks for the four-dimensional quotient, exact substitutions in the Rayleigh certificate and its zero-sum eigenvector, an elementary integer inequality certificate for all \(n\ge3\), full-matrix spectral computations for 98 distinct values \(3\le n\le100\), and an exact-rational positive-definiteness test for the \(n=2\) witness. Run `python verify_broom.py` with Python 3, SymPy, and NumPy installed. The finite tests supplement the symbolic proof; they are not substituted for its unbounded quantifiers.

## Relationship to prior work
Boyd, Diaconis, and Xiao's 2004 formulation of the fastest-mixing Markov-chain problem provides the convex spectral-norm setting, and Boyd, Diaconis, Parrilo, and Xiao's symmetry paper provides a general averaging reduction and solves other graph families, but neither examined full text supplies the displayed broom-specific formula and unrestricted uniqueness theorem. Jafarizadeh's bistar-topology result treats exactly the same general graph class with **conditional** transition formulas: §6.7, eq. (60), requires \(\pi_{-1}\Pi^+\le\pi_1^2\). At uniform stationarity and \(n\ge3\) right leaves, this is \(n\le1\), so the stated conditional bistar theorem does not cover this regime. It also does not establish uniqueness without an orbit-invariance assumption. This provides a specific gap, not a proof that no unindexed equivalent result exists.

## Limitations
The graph is an unweighted simple double star with exactly one leaf at the first hub; arbitrary two-sided branch counts, nonuniform stationary distributions, and directed chains are not classified. The strict \(n=2\) comparison does not solve that smaller case. The claim of originality rests on the inspected sources and bounded searches and is susceptible to undiscovered prior coverage; no independent audit is claimed here.

## References
1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264; publicly dated 2004-10-29. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (2007). https://arxiv.org/abs/0709.0955
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, arXiv:2501.02421, §6.7 (2025). https://arxiv.org/html/2501.02421v1
