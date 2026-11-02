# Sparse cyclic tomography on prime-affine groups

## Finding
Let \(p\) be prime, let \(q\ge3\) divide \(p-1\), and choose \(r\in\mathbb F_p^\times\) of multiplicative order \(q\). On the nonabelian affine group \(G=\mathbb F_p\rtimes_r C_q\), consider the maximal cyclic translation subgroup \(P\) and the \(p\) cyclic complements \(H_a\), indexed by \(a\in\mathbb F_p\). Each direction supplies the unweighted sum of an arbitrary complex-valued function over every left coset.

For ANY subset \(A\subseteq\mathbb F_p\), let \(m=|A|\), and let \(R_{A,\epsilon}\) include all coset sums for the complements \(H_a\), \(a\in A\), together with those for \(P\) if \(\epsilon=1\), and without \(P\) if \(\epsilon=0\). Then
\[
\dim\ker R_{A,\epsilon}=(p-1)\max(q-m,0)+\begin{cases}0,&\epsilon=1,\\q-\mathbf1_{m>0},&\epsilon=0.\end{cases}
\]
Thus injectivity holds **exactly** when \(P\) is used and at least \(q\) *distinct* complements are used. The minimum is \(q+1\) complete maximal-cyclic directions, and **every** such minimum family \(\{P\}\cup\{H_a:a\in A,\ |A|=q\}\) succeeds, without any arithmetic restriction on the positions in \(A\). It produces only \(q(p+1)\) coset sums to reconstruct \(pq\) unknown function values.

Write \(\zeta=e^{2\pi i/p}\) and \(M_k(A)=(\zeta^{ka(1-r^t)})_{a\in A,\ 0\le t<q}\). The exact squared-singular-value multiset for \(\epsilon=1\) is the union of the eigenvalues of \(pI_q+m\mathbf1\mathbf1^{\!*}\) and, for every \(1\le k<p\), those of \(M_k(A)^{\!*}M_k(A)\). For \(m=q\), the normal determinant is exactly
\[
\det(R_{A,1}^{\!*}R_{A,1})=(p+q^2)p^{q-1}\prod_{k=1}^{p-1}|\det M_k(A)|^2>0.
\]
For \(m\ge q\) its general exact determinant replaces each last squared determinant by \(\sum_{B\subseteq A,\ |B|=q}|\det M_k(B)|^2\).

In the full affine case \(q=p-1\), for ANY minimal family (all complements but one, plus \(P\)), the squared singular values are **exactly**
\[
1\quad (p-1\text{ times}),\qquad p\quad (p(p-2)\text{ times}),\qquad p+(p-1)^2\quad (\text{once}).
\]
The sharp condition number restricted to mean-zero functions is therefore \(\sqrt p\), independently of which complement is omitted.

## Assumptions and scope
Multiplication is \((x,t)(y,u)=(x+r^t y,t+u)\), where \(x,y\in\mathbb F_p\) and \(t,u\in C_q\). The groups are \(P=\{(x,0):x\in\mathbb F_p\}\) and \(H_a=\{(a(1-r^t),t):0\le t<q\}\). These are exactly the maximal cyclic subgroups: every element with nonzero second coordinate lies in the unique complement corresponding to its affine fixed point, and every element with zero second coordinate lies in \(P\). All sums are unweighted, once per distinct left coset. Input and output have counting-measure \(\ell^2\) norms. There are no assumptions on the complex function being reconstructed. The theorem is stated for \(q\ge3\); the analogous \(\(q=2\)\) dihedral boundary was previously studied.

## Proof
A left coset of \(H_a\) has the form \((x,0)H_a=\{(x+a(1-r^t),t):0\le t<q\}\). Thus
\[
(R_af)(x)=\sum_{t=0}^{q-1}f(x+a(1-r^t),t),\qquad
(R_Pf)(t)=\sum_{x\in\mathbb F_p}f(x,t).
\]
Apply the unitary length-\(p\) Fourier transform in the first coordinate to the input slices and complement outputs. With \(\widehat f_t(k)=p^{-1/2}\sum_x f(x,t)\zeta^{-kx}\), the exact identity is
\[
\widehat{R_af}(k)=\sum_{t=0}^{q-1}\zeta^{ka(1-r^t)}\widehat f_t(k).
\]
For \(k=0\), the \(m\) complement rows coincide with \((1,\ldots,1)\), and the \(P\) observations are \(\sqrt p\,\widehat f_t(0)\), one for each \(t\). Therefore the zero-frequency rank is \(q\) when \(P\) is included; otherwise it is \(1\) for \(m>0\) and \(0\) for \(m=0\).

For nonzero \(k\), the \(m\)-by-\(q\) coefficient matrix \(M_k(A)\) is a submatrix of the order-\(p\) discrete Fourier matrix. The row frequencies \(a\) are distinct by construction; its column frequencies \(k(1-r^t)\) are distinct because \(r\) has order \(q\). Every square minor of a prime-order Fourier matrix is nonzero (Chebotarev's Fourier-minor theorem), so this block has rank \(\min(m,q)\). Summing the zero-frequency nullity and the \(p-1\) identical-size nonzero-frequency nullities proves the claimed formulas and the sharp minimum.

For completeness, the required Fourier-minor fact can be checked algebraically. For distinct integers \(x_i,y_j\) representing residues modulo \(p\) and \(s=q(q-1)/2\), put \(F(T)=\det((1+T)^{x_i y_j})\in\mathbb Z[T]\). Expanding \(\det(e^{x_i y_j u})\) through the first nonzero degree gives
\[
F(T)=cT^s+O(T^{s+1}),\qquad
c=\frac{\prod_{i<j}(x_j-x_i)\prod_{i<j}(y_j-y_i)}{\prod_{j=0}^{q-1}j!},
\]
up to an irrelevant sign. This coefficient is an integer not divisible by \(p\), because \(q<p\) and all residue differences are nonzero modulo \(p\). In the cyclotomic integer ring, \(\pi=\zeta-1\) generates a prime ideal with residue field \(\mathbb F_p\). Hence \(F(\pi)=\pi^s(c+\pi Q(\pi))\ne0\). This proves the nonvanishing needed for every chosen square minor (using its own size in place of \(q\)).

The unitary Fourier decomposition also proves the full normal-block formula. For \(k=0\), the normal block is \(pI_q+m\mathbf1\mathbf1^{\!*}\), with eigenvalues \(p+mq\) and \(p\) of multiplicities one and \(q-1\). Every nonzero-frequency normal block is \(M_k(A)^{\!*}M_k(A)\). Taking determinants and applying Cauchy–Binet proves both determinant formulas.

Finally, if \(q=p-1\) and \(|A|=p-1\), the row and column index sets of every \(M_k(A)\) each omit exactly one position from the complete order-\(p\) Fourier matrix. Orthogonality of its full columns shows \(M_k(A)^{\!*}M_k(A)=pI_{p-1}-vv^{\!*}\) with \(\|v\|^2=p-1\). Its spectrum is \(1\) once and \(p\) with multiplicity \(p-2\). Combining all \(p-1\) nonzero frequencies with the zero-frequency block gives the three displayed levels. The unique constant-function eigenvector has squared singular value \(p+(p-1)^2\), proving the mean-zero condition number.

## Verification
The accompanying `CHECKER.py` builds independent exact \(0/1\) left-coset incidence matrices and checks their nullities by modular Gaussian elimination. It passed 610 comparisons across ten prime/complement-order configurations, including 168 exhaustive small-prime direction-subset choices. It additionally passed 22 full Fourier-block spectral comparisons, including the full-affine three-level laws at primes \(5,7,11,13\). Finite computations corroborate but do not replace the all-parameter Fourier-minor proof. Run with `python CHECKER.py` (Python 3, NumPy for the spectral section).

## Relationship to prior work
Ilmavirta (2014, Sections 2, 6, and 7.3) studies injectivity of cyclic-coset Radon transforms on finite groups, including the maximal-cyclic variant. The inspected text establishes broad full-direction criteria but not this all-subsets rank law or a sharp \(q+1\)-direction theorem on prime-affine groups. Tao (2003, Lemma 1.3) proves the prime Fourier-minor theorem used as an essential ingredient here; that lemma alone does not specify or classify nonabelian coset-data selections. Scarabotti (2003) studies Fourier analysis of finite Radon transforms between multiplicity-free permutation representations; a complete comparison with that source was not possible. The previously studied dihedral case \(\(q=2\)\) is not claimed as a new special case.

## Limitations
The theorem requires a prime translation field, cyclic complement order dividing \(p-1\), and complete unweighted coset families; it does not assert the same rank law over prime-power translation fields, with incomplete coset sampling, or for arbitrary subgroup choices. The determinant formula gives exact spectral blocks but not elementary closed radicals for their eigenvalues in general. Published results beyond the inspected sources could contain equivalent formulations. Independent review has not been performed.

## References
- J. Ilmavirta, *On Radon transforms on finite groups*, first public arXiv version 2014-11-14, https://arxiv.org/abs/1411.3829 .
- T. Tao, *An uncertainty principle for cyclic groups of prime order*, first public arXiv version 2003-08-29, https://arxiv.org/abs/math/0308286 .
- F. Scarabotti, *Fourier Analysis of a Class of Finite Radon Transforms*, SIAM Journal on Discrete Mathematics 16 (2003), 545–554, https://doi.org/10.1137/S0895480102416398 .
