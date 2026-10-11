# Two-level Slepian spectrum for point stars in finite Grassmann schemes
## Finding
Let \(q\ge2\) be any prime power, \(n\ge4\), and \(2\le k\le n-1\). In the complex Hilbert space of functions on the finite Grassmannian \(X=\operatorname{Gr}_q(n,k)\), let \(H_{\le1}\) be the span of the projective-point incidence functions \(U\mapsto\mathbf1_{\{P\subseteq U\}}\). This is the degree-zero-plus-degree-one spherical harmonic space. Fix a projective point \(P_0\) and the Schubert star \(A=\{U\in X:P_0\subseteq U\}\). Let \(P\) be the orthogonal projection onto \(H_{\le1}\), and let the Slepian concentration operator on that space be
\[
C=P M_{\mathbf1_A}P\big|_{H_{\le1}}.
\]
Put \([s]_q=(q^s-1)/(q-1)\) for every positive integer \(s\), and \(\theta=[k-1]_q/[n-2]_q\). Its **entire spectrum, with algebraic multiplicities**, is
\[
\boxed{\operatorname{spec}(C)=\left\{1,\ \underbrace{\theta,\ldots,\theta}_{[n-1]_q-1\text{ times}},\ \underbrace{0,\ldots,0}_{q^{n-1}\text{ times}}\right\}.}
\]
At the boundary \(k=n-1\), \(\theta=1\), so the two displayed unit-eigenvalue multiplicities are combined. In the genuinely bandlimited regime \(2\le k\le n-2\), the three displayed eigenvalues are distinct. In every case, \(\dim H_{\le1}=[n]_q\), \(\operatorname{rank}(C)=[n-1]_q\), and \(\operatorname{tr}(C)=[k]_q\).

Equivalently, restriction of low-pass functions from \(X\) to \(A\) has nonzero singular values \(1\) once and \(\sqrt\theta\) with multiplicity \([n-1]_q-1\). Its kernel has dimension exactly \(q^{n-1}\), independent of \(k\). For data on \(A\) lying in the quotient first-harmonic space, the optimal norm of the minimum-energy bandlimited extension map is
\[
\boxed{\theta^{-1/2}=\sqrt{\frac{[n-2]_q}{[k-1]_q}}.}
\]
## Assumptions and scope
Throughout, functions carry uniform counting inner products; replacing these simultaneously with normalized counting inner products does not change concentration eigenvalues. The star is canonically identified with \(\operatorname{Gr}_q(n-1,k-1)\) by \(U\mapsto U/P_0\). The quotient first-harmonic space consists of linear combinations of indicators that a projective point of \(\mathbb F_q^n/P_0\) lies in \(U/P_0\); it includes the constants. The statement covers all prime powers, all specified ranks, and the degenerate top-degree boundary; it does not make a claim about higher Grassmann harmonic cutoffs or different spatial windows.
## Proof
**1. Incidence representation.** Set \(V=\mathbb F_q^n\). Let \(\mathcal P\) be its set of projective points and write \(v=[n]_q\), \(r=[k]_q\), and \(B=|X|\). Form the point–subspace incidence matrix \(N\), with rows indexed by \(U\in X\) and columns by \(Q\in\mathcal P\), where \(N_{U,Q}=\mathbf1_{\{Q\subseteq U\}}\). The projective general linear group is doubly transitive on projective points. Thus \(N^*N=aI+bJ\), with
\[
a=\frac{B\,r(v-r)}{v(v-1)}>0.
\]
Indeed, each row has \(r\) entries equal to one; counting ordered pairs of points inside \(U\) shows that the diagonal entries are \(Br/v\) and the off-diagonal entries are \(Br(r-1)/(v(v-1))\). Therefore \(N\) has full column rank, \(H_{\le1}=\operatorname{ran}(N)\), and \(\dim H_{\le1}=v\). Moreover \(\sum_{Q\in\mathcal P}N_{U,Q}=r\), so constants belong to this space.

**2. Restricted incidence rank.** Let \(R:\ell^2(X)\to\ell^2(A)\) be coordinate restriction. Every \(U\in A\) contains \(P_0\). The column of \(RN\) corresponding to \(P_0\) is constant one. For \(Q\ne P_0\), its restriction depends only on the projective point \(\overline Q=(P_0+Q)/P_0\) of the quotient \(V/P_0\) and equals \(\mathbf1_{\{\overline Q\subseteq U/P_0\}}\). Each quotient point has exactly \(q\) distinct projective lifts \(Q\ne P_0\). Hence \(R(H_{\le1})\) is exactly the span of the quotient point-incidence columns. Denote their number by \(v'=[n-1]_q\). Because \(1\le k-1\le n-2\), the quotient incidence Gram matrix has the same form as in step 1 with strictly positive coefficient of \(I\); consequently these columns are independent and the restricted rank is exactly \(v'\).

**3. Two isotypic eigenvalues.** The nonzero eigenvalues of \(C=(R|_{H_{\le1}})^*(R|_{H_{\le1}})\) equal those of \(S=RPR^*\) on \(\ell^2(A)\). The stabilizer of \(P_0\) induces the full group \(\operatorname{GL}(V/P_0)\) on \(A\), so \(S\) commutes with this action. Its range is the quotient point-incidence space from step 2. That space is the direct sum of the constant module and the nonconstant part of the projective-point permutation module. The action on projective points is doubly transitive, which makes the mean-zero permutation module irreducible over \(\mathbb C\): its commuting algebra has dimension two, one block for constants and one for the orthogonal complement. Schur's lemma therefore forces \(S\) to have a single eigenvalue \(\theta\) on the nonconstant part of dimension \(v'-1\).

The indicator \(\mathbf1_A(U)=N_{U,P_0}\) itself belongs to \(H_{\le1}\). It follows that \(S\mathbf1_A=\mathbf1_A\), so the constant quotient eigenvalue is exactly one. All other eigenvalues of \(C\) are zero, with multiplicity \(v-v'=q^{n-1}\).

**4. Sharp eigenvalue from the trace.** Transitivity of \(\operatorname{GL}(V)\) on \(X\) makes the diagonal of \(P\) constant and equal to \(v/B\). Since each \(U\) contains \(r\) projective points and every point lies in the same number of \(k\)-subspaces, \(|A|/B=r/v\). Thus
\[
\operatorname{tr}(C)=|A|\frac vB=r=1+(v'-1)\theta,
\]
and hence
\[
\theta=\frac{[k]_q-1}{[n-1]_q-1}=\frac{[k-1]_q}{[n-2]_q}.
\]
The quotient incidence rank ensures this eigenvalue is strictly positive. It is strictly less than one for \(k\le n-2\) and equals one at \(k=n-1\). This completes the entire spectrum, rank, nullity, and trace formulas.

**5. Optimal extension cost.** Singular values of the restriction \(R|_{H_{\le1}}\) are square roots of the nonzero eigenvalues of its Gram operator \(C\). On the range \(R(H_{\le1})\), the inverse restriction of minimum Hilbert-space norm is its Moore–Penrose pseudoinverse. Its norm equals the reciprocal of the smallest nonzero singular value, namely \(\theta^{-1/2}\), and this value is attained on every nonconstant quotient first-harmonic vector.
## Verification
A standalone checker, `verify_grassmann.py`, constructs all projective points and reduced-row-echelon-form subspaces, forms the exact incidence matrices, and compares the numerical eigenvalues of the whitened restricted Gram matrix with the analytic multiplicities. It verifies ten prime-field parameter cases at \(q=2,3\), including interior and top-rank boundaries, and one \(\mathbb F_4\) case using explicit polynomial-field arithmetic. The maximum reported absolute eigenvalue error is below \(5\times10^{-15}\). The checker uses Python 3 and NumPy; it checks finite examples and is not the proof of the all-parameter statement.
## Relationship to prior work
Simons, Dahlen, and Wieczorek formulate spatial-versus-bandlimit concentration as a finite-dimensional spectral problem on the continuous sphere, including a spatial bandwidth trace law, but not the finite-field Grassmannian. Marco and Parcet determine \(q\)-Grassmann equivariant Radon kernels using \(q\)-Hahn polynomials; their global intertwiner calculations do not evaluate restriction to a fixed point-containing star. Srinivasan constructs a simultaneous harmonic basis for the Grassmann scheme and establishes the relevant multiplicity-free point-incidence structure, but does not state the spectrum of the spatially compressed bandlimited projection. The present result computes the complete Schubert-star Slepian spectrum and its exact interpolation singular values by coupling finite-field incidence with point-stabilizer symmetry.
## Limitations
The theorem is limited to the degree-zero-plus-degree-one spherical band and one-point Schubert stars. More complicated flags, unions of Schubert cells, and higher harmonic bands are not classified here. The proof gives the sharp Hilbert-space restriction and extension constants, not optimal bounds in \(\ell^p\) spaces for \(p\ne2\). Numerically verified examples are not used as a substitute for the all-size proof.
## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (first public 2004-08-31), MSC primary 42B05; SIAM Review 48 (2006), 504–536.
2. J. M. Marco and J. Parcet, *Laplacian operators and Radon transforms on Grassmann graphs*, arXiv:math/0404019v1 (first public 2004-04-01), revised v2 (2005); see the introduction and §§1, 3, 5.
3. M. K. Srinivasan, *The Goldman-Rota identity and the Grassmann scheme*, arXiv:1304.6244v1 (first public 2013-04-23), especially §3, Theorems 3.1–3.2; Electronic Journal of Combinatorics 21 (2014), P1.37.
