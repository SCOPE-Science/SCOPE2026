# Sharp acute-phase positivity and disconnected resonance islands on Hamming products

## Finding
For integers \(q\ge2\) and \(n\ge2\), the complete sharp positive-semidefiniteness test for the damped, oscillating radial Hamming kernel
\[
K_{q,n;r,\theta}(x,y)=r^{d_H(x,y)}\cos(\theta d_H(x,y)),\qquad 0\le r\le1,\quad0\le\theta\le\pi/2
\]
on \(G=(\mathbb Z/q\mathbb Z)^n\) consists of only two inequalities. Put \(\phi=\pi/(2n)\). Then
\[
\boxed{r\sin(\theta+\phi)\le\sin\phi,\qquad(q-1)r\sin(\theta-\phi)\le\sin\phi.}\tag{1}
\]
Both inequalities include equality. The full Gram matrix has eigenvalues
\[
\lambda_k=\operatorname{Re}\bigl[(1+(q-1)re^{i\theta})^{n-k}(1-re^{i\theta})^k\bigr],
\quad k=0,\ldots,n,
\]
with multiplicities \(\binom nk(q-1)^k\). Except for the all-ones kernel \(r=1,\theta=0\), strict positive definiteness is equivalent to both inequalities being strict, and at each boundary a precisely identified endpoint Fourier eigenspace becomes null.

The angular admissibility has an unusual *resonance-island dichotomy*. For \(q=2\), writing \(s=\sin\phi/r\), whenever \(\sin\phi<r<\tan\phi\) there are two separated admissible intervals:
\[
[0,\arcsin(s)-\phi]\ \cup\ [\pi-\arcsin(s)-\phi,\pi/2].\tag{2}
\]
At \(r=\tan\phi\) the upper interval is the single point \(\pi/2\). If \(r>\tan\phi\), it disappears. For every nonbinary alphabet \(q\ge3\), disconnected angular admissibility can occur **only when \(n=2\)**. In that case it occurs precisely for
\[
\frac1{\sqrt2}<r\le r_c(q),\qquad
r_c(q)=\sqrt{\frac12+\frac1{2(q-1)^2}}.\tag{3}
\]
For \(1/\sqrt2<r<r_c(q)\), the two intervals are
\[
[0,\arcsin(s)-\pi/4]\ \cup\
[3\pi/4-\arcsin(s),\ \pi/4+\arcsin(s/(q-1))],
\qquad s=1/(\sqrt2r).\tag{4}
\]
At \(r=r_c(q)\) the second interval is a singleton. For other \(r\) or for \(q\ge3,n\ge3\), the nonempty admissible angle set is connected.

At the critical nonbinary endpoint \(n=2,r=r_c(q)\), choose the unique angle \(\theta_*\in[0,\pi/2]\) with
\[
r_c(q)e^{i\theta_*}=\frac{q-2+iq}{2(q-1)}.\tag{5}
\]
The Gram operator equals \(q^2/[2(q-1)]\) times the orthogonal projection onto the first Fourier-weight sector: its rank is exactly \(2(q-1)\), with all nonzero eigenvalues equal. Equation (5) includes the binary endpoint \(q=2\).

## Assumptions and scope
The distance \(d_H(x,y)\) counts coordinates in which \(x\) and \(y\) differ, with the conventions \(0^0=1\) and diagonal kernel value \(1\). The group is finite and carries counting measure; Fourier eigenvalues are eigenvalues of the full \(q^n\)-by-\(q^n\) unnormalized kernel matrix. Here *positive semidefinite* means every finite complex quadratic form is nonnegative; *strict* means positive for every nonzero coefficient vector on distinct elements. The angle is restricted to the natural acute modulation sector \([0,\pi/2]\), not to arbitrary real phases. The statement makes no assertion for other angle sectors. The Fourier weight of a character is its number of nontrivial coordinate characters.

## Proof
**1. Exact spectrum.** Put \(z=re^{i\theta}\), so the kernel is the real part of \(z^{d_H(x,y)}\). For a one-coordinate character, the Fourier sum \(\sum_{u\in\mathbb Z/q\mathbb Z}z^{\mathbf1_{u\ne0}}\overline{\chi(u)}\) equals \(1+(q-1)z\) for the trivial character and \(1-z\) for a nontrivial character. Tensoring \(n\) coordinates and taking real parts gives the displayed eigenvalues. Their multiplicities are \(\binom nk(q-1)^k\); Fourier diagonalization is exact even for composite \(q\).

**2. A phase-strip lemma.** Assume \(r>0\) and exclude \(r=1,\theta=0\). Put
\[
\alpha=\arg(1+(q-1)z)\in[0,\pi/2),\qquad
\beta=\arg(1-z)\in(-\pi/2,0],
\]
and \(\delta=\alpha-\beta\in[0,\pi)\). The argument in the \(k\)-th Fourier level is \((n-k)\alpha+k\beta\), forming a decreasing arithmetic progression of step \(\delta<\pi\), and the two factors have nonzero modulus. Every component on which cosine is nonnegative is a closed interval of width \(\pi\), separated from the next component by a negative-cosine interval of width \(\pi\). Consecutive progression values cannot cross between two positive components while skipping the intervening negative interval, since their step is strictly less than \(\pi\). Hence all \(n+1\) cosines are nonnegative if and only if all phase values lie in the *same* positive component. Since the progression starts at \(n\alpha\ge0\), ends at \(n\beta\le0\), and brackets zero, this component must be \([-\pi/2,\pi/2]\). Consequently
\[
\lambda_k\ge0\ \forall k\quad\Longleftrightarrow\quad
\alpha\le\phi\text{ and }-\beta\le\phi.\tag{6}
\]
Equality in either boundary condition forces respectively \(\lambda_0=0\) or \(\lambda_n=0\); all intermediate levels have strictly positive eigenvalues. At \(r=0\), the kernel is the identity, and at \(r=1,\theta=0\) it is the all-ones matrix, both handled directly.

**3. Sine tests.** Since both factors have positive real part away from the separately handled endpoint, \(\alpha\le\phi\) is equivalent to
\((q-1)r\sin(\theta-\phi)\le\sin\phi\). Similarly, \(-\beta\le\phi\) is equivalent to \(r\sin(\theta+\phi)\le\sin\phi\). This proves (1) and the stated strict/endpoint cases.

**4. Connectedness and resonance islands.** For \(r\le\sin\phi\), the first sine inequality always holds, while the second constrains \(\theta\) to a (possibly full) initial interval; no disconnected phase is possible. For \(r>\sin\phi\), write \(s=\sin\phi/r<1\). The first sine inequality permits an initial interval up to \(\arcsin(s)-\phi\) and, if \(r\le\tan\phi\), a second interval starting at \(\pi-\arcsin(s)-\phi\). The second sine inequality excludes angles above \(\phi+\arcsin(s/(q-1))\) when that cap lies below \(\pi/2\). Its intersection with the first interval is always an initial interval. For \(q=2\), \(|\arg(1-z)|\ge\arg(1+z)\), so the second sine test is redundant, yielding (2). In the nonbinary case an upper component can survive only if
\[
\arcsin(s)+\arcsin\!\bigl(s/(q-1)\bigr)\ge\pi-2\phi.\tag{7}
\]
If \(n\ge3,q\ge3\), the left side is strictly below \(\pi/2+\pi/6=2\pi/3\) because \(s<1\) and \(q-1\ge2\), while the right side is at least \(2\pi/3\), a contradiction. For \(n=2\), condition (7) is equivalent to \(s^2+s^2/(q-1)^2\ge1\), giving precisely (3). The cap and branch endpoints then give (4). At the upper critical value the cap equals the second-branch start, and the interval becomes a single admissible angle.

**5. Exact first-harmonic projector at collision.** With the parameter (5), the two scalar Fourier factors are \(1+(q-1)z=q(1+i)/2\) and \(1-z=q(1-i)/[2(q-1)]\). At \(n=2\) their squared real parts vanish, whereas their mixed real part is \(q^2/[2(q-1)]\). Thus the only nonzero eigenvalue is \(\lambda_1=q^2/[2(q-1)]\), with multiplicity \(2(q-1)\), as claimed. This is an exact finite-rank *projection identity*, not just a numerical near-equality.

## Verification
A standalone standard-library Python checker, `CHECKER.py`, forms direct finite-group character sums and separately computes the factorized eigenvalues. It passed 540 deterministic comparisons across \(q\in\{2,3,4,5\}\), \(n\in\{1,2,3\}\), 45 parameter samples per configuration, verifying Fourier eigenvalues and sampled positivity decisions. For \(q=3,n=2,r=3/4\), it numerically locates the low admissible interval endpoint at \(0.445561253943326\) and the high interval at approximately \([1.125235072851571,1.276280841686760]\). These finite tests are not proofs of the statements over all integers and parameters: Steps 1–5 are the proofs.

## Relationship to prior work
Harrow–Kolla–Schulman, *Dimension-free L2 maximal inequality for spherical means in the hypercube* (arXiv:1209.4148, first posted 2012-09-19), treats spherical averages, Walsh/Krawtchouk diagonalization, and real Markov noise operators on the Boolean cube. Its main theorem is an \(L^2\) maximal inequality, not an exact positive-definiteness criterion for the real part of a complex-parameter distance kernel or its disconnected angle phase diagram. Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables* (arXiv:1309.1510, first posted 2013-09-05), develops multivariate Krawtchouk kernels and nonnegative Poisson kernels on finite multinomial/simplex structures; it does not assert the present two-sine admissibility test or the rank-collapse projection contact. These works supply relevant harmonic context; their general Fourier methods are compatible with but do not themselves state this classification. Other Hamming-shell Fourier concentration results concern *restricted subspaces*, not the full convolution matrix used here.

## Limitations
The classification is restricted to finite alphabet size \(q\ge2\), length \(n\ge2\), \(r\in[0,1]\), and acute angles \(\theta\in[0,\pi/2]\); no extension is asserted outside those ranges. Positivity of the full Hamming-product kernel does not automatically imply positivity of unrelated infinite-tree geodesic kernels. The mathematical derivation has not received independent audit. Literature comparisons were bounded; similar parameter inequalities could occur in terminology not retrieved by the searches.

## References
1. Aram W. Harrow, Alexandra Kolla, Leonard J. Schulman, *Dimension-free L2 maximal inequality for spherical means in the hypercube*, arXiv:1209.4148v1 (2012-09-19), https://arxiv.org/abs/1209.4148 ; accessible full text at https://arxiv.org/html/1209.4148v2 (Section 2, Fourier analysis and Krawtchouk polynomials).
2. Yuan Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables*, arXiv:1309.1510v1 (2013-09-05), https://arxiv.org/abs/1309.1510 ; accessible full text at https://arxiv.org/html/1309.1510v1 (orthogonal and Poisson kernel sections).
