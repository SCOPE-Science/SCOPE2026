# The spanning-tree polytope in price-optimal one- and two-bit hypercube mixing

## Finding
Let \(d\ge3\) be an integer, let \(N=2^d\), and connect vertices of \(\mathbb F_2^d\) at Hamming distance one or two. Give every distance-one edge price one and every distance-two edge price \(t>0\). Individual undirected edge conductances are arbitrary nonnegative reals, with total price-weighted expenditure one. Write \(\gamma\) for the second-smallest eigenvalue of the resulting combinatorial weighted Laplacian, equivalently the decay gap of its symmetric continuous-time Markov generator.

**Exact global optimum, without a symmetry assumption:**
\[
\boxed{\sup\gamma=\Gamma_d(t)=\begin{cases}
\dfrac{8}{2^d[2+(d-1)t]},&0<t\le2,\\[5pt]
\dfrac{4}{d2^d},&t\ge2.
\end{cases}}
\]
(The two branches agree at \(t=2\).) If \(0<t<2\), every global optimizer has total conductance \(W_1=2/[2+(d-1)t]\) on distance-one edges and \(W_2=(d-1)/[2+(d-1)t]\) on distance-two edges. If \(t>2\), the global optimizer is **unique even among individually weighted edges**: every distance-two edge is deleted and every distance-one edge has conductance \(2/(d2^d)\).

There is an exact and substantially nonunique **classification of every translation-invariant global optimizer** for \(0<t\le2\). Put \(q=\Gamma_d(t)/2\). A translation-invariant conductance is specified by \(b_i\) for all edges with displacement \(e_i\), and \(a_{ij}=a_{ji}\) for edges with displacement \(e_i+e_j\). Its optimality is equivalent to the existence of nonnegative \(z_{ij}\) such that
\[
 a_{ij}=\frac q2z_{ij},\qquad b_i=q\left(1-\frac12\sum_{j\ne i}z_{ij}\right),
\]
\[
\sum_{\{i,j\}\subset S}z_{ij}\le |S|-1
\quad\text{for each nonempty }S\subseteq[d],\qquad
\sum_{j\ne i}z_{ij}\le2\quad(i\in[d]),
\]
and, when \(0<t<2\), the further equality \(\sum_{i<j}z_{ij}=d-1\). At \(t=2\) that equality is dropped. Thus the indexing weights \(z\) form the fractional spanning-tree base polytope of \(K_d\) for \(t<2\), or the fractional spanning-forest polytope at the critical price, in each case intersected with coordinate-degree upper bounds two. These polyhedral descriptions are given explicitly by the displayed inequalities; no characterization of nonsymmetric optimizers below or at the threshold is claimed.

For every \(0<t\le2\), any Hamilton path on the **coordinate-index graph** \([d]\) gives \(z_{i,i+1}=1\) and all other \(z\)'s zero. This yields a global optimizer with only \(d+1\) active edge-displacement classes, compared with the \(d+\binom d2\) available classes. For \(0<t<2\), another optimizer assigns the same positive conductance to *every* available edge, so optimal networks can be drastically different even with the same price.

## Assumptions and scope
All edges are undirected and appear once in the budget. The one-bit edges number \(Nd/2\), while two-bit edges number \(N\binom d2/2\). For an edge \(\{x,y\}\) of weight \(w_{xy}\), the Laplacian acts as \((Lf)(x)=\sum_yw_{xy}(f(x)-f(y))\). The budget is \(\sum_{\text{one-bit edges}}w_{xy}+t\sum_{\text{two-bit edges}}w_{xy}=1\). Conductances can vanish; no positive-connectivity constraint is required because any spectral-gap optimum is connected. A translation-invariant allocation has \(w_{x,x+e_i}=b_i\) and \(w_{x,x+e_i+e_j}=a_{ij}\), independent of the vertex \(x\).

The statements quantify over every integer \(d\ge3\), every real \(t>0\), and every feasible individual assignment of the indicated edge weights. The polyhedral optimizer classification is deliberately restricted to translation-invariant assignments; only the global value, budget totals for \(t<2\), and uniqueness for \(t>2\) concern all edgewise assignments.

## Proof
**1. Universal upper bounds.** For \(S\subseteq[d]\), let \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\). Every nonempty character is orthogonal to constants and has squared norm \(N\). Write \(W_1,W_2\) for the two total conductances. A one-bit edge changes the parity character \(\chi_{[d]}\), while a two-bit edge does not. Since an edge crossing signs \(\pm1\) contributes \(4w\) to the Laplacian quadratic form, its Rayleigh quotient is \(4W_1/N\). Hence
\[
\gamma\le\frac{4W_1}{N}.
\]
For a singleton character \(\chi_{\{i\}}\), only edges whose flip set contains \(i\) contribute. Summing these \(d\) Rayleigh quotients counts each one-bit edge once and each two-bit edge twice. Thus their average is \(4(W_1+2W_2)/(dN)\), yielding
\[
\gamma\le\frac{4(W_1+2W_2)}{dN}.
\]
Put \(u=W_2\), so \(W_1=1-tu\) and \(0\le u\le1/t\). Then
\[
\gamma\le\frac4N\min\left\{1-tu,\frac{1+(2-t)u}{d}\right\}.
\]
For \(0<t<2\), one affine term decreases and the other increases with \(u\); their unique intersection is
\[
 u=\frac{d-1}{2+(d-1)t},\qquad W_1=\frac2{2+(d-1)t}.
\]
This proves the stated upper bound and the necessity of the total conductances. For \(t\ge2\), the second affine term does not increase, so the maximum bound occurs at \(u=0\) and equals \(4/(dN)\). For \(t>2\), equality of the upper bound forces \(W_2=0\).

**2. Attainment for every dimension.** For \(0<t\le2\), assign every available edge the common conductance
\[
 c=\frac4{Nd[2+(d-1)t]}.
\]
It has the prescribed budget. Each Walsh character of Hamming weight \(k\in\{1,\ldots,d\}\) is an eigenvector with eigenvalue
\[
\lambda_k=2c\{k+k(d-k)\}=2c\,k(d-k+1).
\]
Because \(k(d-k+1)\ge d\) for \(1\le k\le d\), with equality at \(k=1\) and \(k=d\), its spectral gap is \(2cd=\Gamma_d(t)\). At \(t\ge2\), assigning the constant \(2/(dN)\) to all one-bit edges and zero to all two-bit edges gives eigenvalues \(4k/(dN)\), hence gap \(4/(dN)\). The upper bounds are therefore sharp.

**3. Unique global design for \(t>2\).** Any optimizer has \(W_2=0\). Its average singleton-character Rayleigh quotient equals the optimal gap, so every singleton-character Rayleigh quotient attains the smallest nonzero eigenvalue. Equality in the Rayleigh principle forces \(L\chi_{\{i\}}=\Gamma_d(t)\chi_{\{i\}}\) for every \(i\). At vertex \(x\), this equation is \(2w_{x,x+e_i}=\Gamma_d(t)\). Thus every one-bit edge weight equals \(\Gamma_d(t)/2=2/(dN)\), proving uniqueness without any invariance assumption.

**4. Complete translation-invariant classification for \(t\le2\).** Suppose the conductances have invariant direction weights \(b_i,a_{ij}\). For each nonempty \(S\subseteq[d]\), the Fourier eigenvalue is exactly
\[
\lambda_S=2\left(\sum_{i\in S}b_i+\sum_{\substack{i\in S\\j\notin S}}a_{ij}\right).
\]
At a global optimum, the averaged singleton-character upper bound equals \(\Gamma_d(t)\) for every \(0<t\le2\). Since each singleton eigenvalue is at least \(\Gamma_d(t)\), each equals it. Consequently
\[
 b_i+\sum_{j\ne i}a_{ij}=q\qquad(i\in[d]).
\]
Set \(z_{ij}=2a_{ij}/q\), so the asserted formulas for \(a_{ij},b_i\) and nonnegative bounds follow. Substituting them into the eigenvalues gives the precise identity
\[
\lambda_S=2q\left(|S|-\sum_{\{i,j\}\subset S}z_{ij}\right).
\]
For every nonempty \(S\), the condition \(\lambda_S\ge\Gamma_d(t)=2q\) is therefore *equivalent* to the family of subset inequalities in the theorem. For \(0<t<2\), the parity-character bound is tight, hence \(\sum_i b_i=q\). Summing the singleton equalities gives \(\sum_i b_i+2\sum_{i<j}a_{ij}=dq\), so \(\sum_{i<j}z_{ij}=d-1\). Conversely, these equations plus the subset and degree constraints make every character eigenvalue at least \(2q\); the budget is
\[
 \frac N2\left(\sum_i b_i+t\sum_{i<j}a_{ij}\right)
 =\frac{Nq}{4}[2+(d-1)t]=1.
\]
Thus every displayed vector gives an optimum. At \(t=2\), the same singleton identities imply the budget automatically since \(N(dq)/2=1\), and the full-set subset inequality yields \(\sum z_{ij}\le d-1\). Again the subset constraints exactly characterize the required spectral bound. This proves necessity and sufficiency at the boundary.

**5. Sparse path designs.** For any fixed Hamilton path on the \(d\) coordinate labels, let \(z_{ij}=1\) on its \(d-1\) edges and zero otherwise. Every induced subgraph of a tree has at most \(|S|-1\) edges and maximum degree two, so the polyhedral constraints hold. The \(d-1\) active two-bit direction classes and two positive one-bit endpoint direction classes total exactly \(d+1\), verifying the claimed sparse optimal design. This finishes the proof.

## Verification
The accompanying standalone Python script `verify.py` uses exact `fractions.Fraction` arithmetic. Running `python3 verify.py` produces:

`VERIFY_OK 84 exact optimal designs; 10752 Walsh-Laplacian equations; 1440 irregular Rayleigh upper bounds`

It checks dimensions \(3\) through \(8\) and prices on both sides of the threshold, verifies exact spectra, budgets, radial, Hamilton-path and critical forest constructions, directly checks Walsh eigen-equations against the full Laplacian for smaller dimensions, and tests Rayleigh upper certificates on individually irregular conductances. This finite reproducibility evidence is separate from, and does not imply, the universal proof above.

## Relationship to prior work
Ghosh and Boyd (2006) present symmetry-based convex bounds for algebraic connectivity; Sun, Boyd, Xiao and Diaconis (2006) formulate the exact general continuous-time fastest-mixing weighted-graph optimization problem with linear edge costs. Their general semidefinite framework covers the *formulation* here, but the inspected full papers do not derive this Hamming-distance-one/two price law, the critical value two, or its fractional tree/forest polytope of optimizers.

Boyd, Diaconis, Parrilo and Xiao (2007) analyze **discrete-time** fastest-mixing Markov chains on symmetric graphs including the ordinary hypercube and Hamming graphs. Their operator objective is a transition-matrix eigenvalue modulus, rather than this price-normalized continuous-time Laplacian gap, and the hypercube examples do not yield the stated cross-distance priced optimizer classification.

Mirafzal (2021) studies the square graph of the hypercube (the same unweighted underlying distance-one/two adjacency) and derives its ordinary graph spectrum. The fixed-weight spectrum is relevant input but does not determine the global price-dependent conductance optimization or nonsymmetric designs. Another published exact result on positive-definite Turán extremizers for the weight-two Boolean Hamming shell concerns the same displacement geometry, but its Fourier nonnegativity objective and equality conditions are distinct and do not imply this priced gap theorem. The older hypercube-walk paper by Karlin, Lindqvist and Yao (1993) is a remaining comparison risk: its abstract addresses spectral representations and majorization, but its complete text was unavailable for inspection.

## Limitations
The design objective is the unnormalized combinatorial-Laplacian spectral gap under a linear total conductance budget; it is not necessarily optimal for discrete-time SLEM, worst-case total-variation mixing, robustness, or vertex-normalized generators. We prove **complete** optimizer classification only in the translation-invariant subclass for \(t\le2\). For larger prices, global uniqueness holds without any invariance restriction. Exact spectra and arbitrary-dimensional claims rest on analysis, not exhaustive finite numerics. Historical priority cannot be certified conclusively, especially because a potentially relevant 1993 hypercube-walk full text was inaccessible.

## References
1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra Appl. 418 (2006), 693–707. DOI 10.1016/j.laa.2006.03.006 (available online 2006-05-05).
2. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The fastest mixing Markov process on a graph and a connection to a maximum variance unfolding problem*, SIAM Review 48 (2006), 681–699. DOI 10.1137/S0036144504443821 (first published online 2006-11-02).
3. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955, first posted 2007-09-06.
4. S. M. Mirafzal, *Some remarks on the square graph of the hypercube*, arXiv:2101.01615, first posted 2021-01-05.
5. S. Karlin, B. Lindqvist and Y. Yao, *Markov chains on hypercubes: spectral representations and several majorization relations*, Random Structures & Algorithms 4 (1993), 1–36. DOI 10.1002/rsa.3240040102 (abstract inspected; full text inaccessible).
