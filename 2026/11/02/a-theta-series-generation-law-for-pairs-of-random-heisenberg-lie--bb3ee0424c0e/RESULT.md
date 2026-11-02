# A theta-series generation law for pairs of random Heisenberg Lie subalgebras

## Finding
Fix a prime power \(q\ge2\). For each integer \(n\ge1\), let \(H_n(q)\) be the Heisenberg Lie algebra \(V_n\oplus\mathbb F_q z\), where \(V_n\) is a \(2n\)-dimensional symplectic space and \([u+az,v+bz]=\omega(u,v)z\). Choose two Lie subalgebras \(A_n,B_n\) independently and uniformly from **all** Lie subalgebras, without restricting their dimensions. Put
\[
\Phi_m(q)=\prod_{i=1}^{m}(1-q^{-i}),\qquad
\Phi_\infty(q)=\prod_{i=1}^{\infty}(1-q^{-i}),\qquad
\Theta(q)=\sum_{j\in\mathbb Z}q^{-j^2}.
\]
Here \(\Phi_0(q)=1\). Define the convergent, explicit constant
\[
\boxed{\mathcal G(q)=\frac{\Phi_\infty(q)}{\Theta(q)^2}
\sum_{\substack{j,k\in\mathbb Z\\j+k\ge0}}
\frac{q^{-j^2-k^2}}{\Phi_{j+k}(q)}.}
\]
Then
\[
\boxed{\Pr\!\left(\langle A_n,B_n\rangle_{\rm Lie}=H_n(q)\right)
=\mathcal G(q)+O_q(q^{-n/2}),\qquad 0<\mathcal G(q)<1.}
\]
The algebraically defined generation probability thus converges to a nontrivial constant. Numerically, \(\mathcal G(2)=0.309726368448897\ldots\), \(\mathcal G(3)=0.485338463362391\ldots\), and \(\mathcal G(5)=0.632486751446923\ldots\).

A structural universality statement is part of the finding: if \(U_n,W_n\) are independent uniformly chosen **linear subspaces** (all dimensions) of \(\mathbb F_q^{2n}\), then
\[
\left|\Pr(\langle A_n,B_n\rangle_{\rm Lie}=H_n(q))
-\Pr(U_n+W_n=\mathbb F_q^{2n})\right|
\le 2\Pr(z\notin A_n)
=O_q\!\left((n+1)q^{-n^2/3+n+3/8}\right).
\]
The right-hand bound holds with a constant depending only on \(q\), and is superexponentially small in \(n\).

## Assumptions and scope
The field \(\mathbb F_q\) may have any characteristic, including characteristic two. The form \(\omega\) is nondegenerate and alternating; thus \(H_n(q)\) has one-dimensional center and derived algebra \(\mathbb F_qz\). By \(\langle A,B\rangle_{\rm Lie}\) we mean the *smallest Lie subalgebra containing both* \(A\) and \(B\), not the vector-space sum \(A+B\), which need not be bracket-closed. Uniform choice is from the finite set of all Lie subalgebras, rather than from one dimension stratum or one automorphism orbit. All asymptotics keep the prime power \(q\) fixed as \(n\to\infty\). The constants are not claimed uniform in \(q\).

## Proof
**1. Generation is a spanning condition.** Let \(\pi:H_n(q)\to V_n\) be the quotient by \(\mathbb F_qz\). For arbitrary Lie subalgebras \(A,B\),
\[
\langle A,B\rangle_{\rm Lie}=H_n(q)
\quad\Longleftrightarrow\quad \pi(A)+\pi(B)=V_n.
\]
Necessity is immediate. Conversely, if the projected subspaces span \(V_n\), all projected vectors have lifts in \(\langle A,B\rangle_{\rm Lie}\). Nondegeneracy of \(\omega\) yields two such lifts with a nonzero bracket, hence \(z\) lies in the generated algebra. The full quotient and the central line then lie in it. This proof also works in characteristic two.

**2. A dominant population of centrally containing subalgebras.** Every subalgebra containing \(z\) has the unique form \(U\oplus\mathbb F_qz\), for an arbitrary subspace \(U\le V_n\). Write \(C_n\) for their number. A subalgebra avoiding \(z\) is the graph of one linear functional on a totally isotropic subspace \(R\le V_n\), with \(q^{\dim R}\) choices for each such \(R\). Write \(D_n\) for their number. These exact decompositions and their finite counts are established background, not a new counting claim here:
\[
C_n=\sum_{r=0}^{2n}{2n\brack r}_q,\qquad
D_n=\sum_{r=0}^{n}q^r\prod_{i=0}^{r-1}\frac{q^{2(n-i)}-1}{q^{r-i}-1}.
\]
Using \(\Phi_\infty(q)>0\), each summand in \(D_n\) is at most
\[
\Phi_\infty(q)^{-1}q^{2nr-\frac32r(r-1)}.
\]
Completing the square gives
\[
2nr-\frac32r(r-1)
=\frac{(2n+3/2)^2}{6}-\frac32\left(r-\frac{2n}{3}-\frac12\right)^2.
\]
Since \(C_n\ge {2n\brack n}_q\ge q^{n^2}\), it follows that
\[
\frac{D_n}{C_n+D_n}
=O_q\left((n+1)q^{-n^2/3+n+3/8}\right).
\]
Condition on both sampled subalgebras containing \(z\). Their projections are then independent uniform members of the *entire* subspace lattice of \(V_n\). By Step 1, their generation probability is precisely the ordinary random-subspace spanning probability. Removing this conditioning changes the probability by at most \(2D_n/(C_n+D_n)\).

**3. Exact conditional spanning kernel.** Put \(d=2n\). Let \(U,W\le\mathbb F_q^d\) have dimensions \(r=n+j\), \(s=n+k\), with \(-n\le j,k\le n\). The event \(U+W=\mathbb F_q^d\) is impossible for \(j+k<0\). Otherwise it forces \(\dim(U\cap W)=j+k\). Fixing \(U\), choose the intersection subspace inside \(U\), then choose a graph over a complement of \(U\); the number of valid \(s\)-subspaces \(W\) is
\[
{n+j\brack j+k}_q q^{(n-j)(n-k)}.
\]
Division by \({2n\brack n+k}_q\) yields the exact conditional probability
\[
\boxed{p_{n;j,k}(q)=
\begin{cases}
\displaystyle\frac{\Phi_{n+j}(q)\Phi_{n+k}(q)}{\Phi_{j+k}(q)\Phi_{2n}(q)},&j+k\ge0,\\
0,&j+k<0.
\end{cases}}
\]
The event therefore depends on \(j,k\) and \(q\), but not on the chosen \(U\) or the symplectic form.

**4. Dimension fluctuations and the limit.** By the Gaussian-binomial identity,
\[
{2n\brack n+j}_q=q^{n^2-j^2}
\frac{\Phi_{2n}(q)}{\Phi_{n+j}(q)\Phi_{n-j}(q)}.
\]
For fixed \(j\), the last factor tends to \(1/\Phi_\infty(q)\), and it is bounded above uniformly by \(\Phi_\infty(q)^{-2}\). Summability of \(q^{-j^2}\) therefore proves
\[
\Pr(\dim U_n=n+j)\longrightarrow\frac{q^{-j^2}}{\Theta(q)}.
\]
For fixed \(j,k\), Step 3 gives \(p_{n;j,k}\to \mathbf1_{j+k\ge0}\Phi_\infty/\Phi_{j+k}\). Dominated convergence over the two integer offsets proves that the random-subspace spanning probability tends to \(\mathcal G(q)\), and Step 2 transfers that limit to the Lie-algebra generation event.

For the stated convergence rate, restrict initially to \(|j|,|k|\le n/2\). The product tail estimate \(\Phi_m(q)=\Phi_\infty(q)(1+O_q(q^{-m}))\) makes each Gaussian weight and each conditional kernel within \(O_q(q^{-n/2})\) of its limiting value, uniformly on this central region. The omitted tails have total probability \(O_q(q^{-n^2/4})\), since the Gaussian weights are bounded by fixed multiples of \(q^{-j^2}\). The exceptional noncentral population has the still smaller bound in Step 2. Thus the total error is \(O_q(q^{-n/2})\).

Finally, the summand with \(j=k=1\) has positive weight and positive spanning probability, proving \(\mathcal G(q)>0\); the summand with \(j=k=-1\) has positive weight but zero spanning probability, proving \(\mathcal G(q)<1\). This completes the proof.

## Verification
The reproducible program `artifacts/verify.py` enumerates every row-reduced-echelon vector subspace of \(H_n(q)\) for \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3)\), tests Lie closure by the alternating bracket, then directly determines which *ordered pairs* span the symplectic quotient. It obtains \(77\) generating ordered pairs among \(12^2\) for \((1,2)\), \(7925\) among \(158^2\) for \((2,2)\), and \(203195\) among \(693^2\) for \((2,3)\). The same program independently evaluates the exact Gaussian finite sums for random-subspace spanning and compares them to the theta-series constant for \(q=2,3,5\) and \(n=8,16,32,48\), returning `VERIFY_OK`. The numerical checks are finite corroboration, not a proof of the infinite statement.

## Relationship to prior work
Eick and Moede (arXiv:2205.03155) develop algorithms to enumerate finite-field Lie subalgebras, testing simple Lie algebras of bounded dimension; their work does not calculate random-pair generation probabilities for growing Heisenberg rank. Glasby, Niemeyer and Praeger (arXiv:2109.10015, Lemma 2.1) give the ordinary fixed-complementary-dimension subspace-spanning probability as a finite Euler product; that previously known special kernel is **not** claimed new. Their main theorem and later arXiv:2111.02198 study **fixed dimensions of nondegenerate subspaces** of finite classical spaces. Neither gives the all-dimension, unrestricted-subspace theta mixture here. Muhie, Otera and Russo (arXiv:2609.19086) study *permutability* of subalgebras, a different pair property from generating the whole Lie algebra.

An accessible 2026 note titled *Exact subalgebra commutativity degree of finite Heisenberg Lie algebras* gives the exact **single-subalgebra census** \(C_n+D_n\) and exact nonpermuting-pair counts; that single-subalgebra formula is treated above as established background. Another note titled *Exact endpoint norms and Euler-product scaling for the first Grassmann Fourier projection* supplies a fixed-rank disjointness probability; it does not sum over independently fluctuating ranks or address random Lie-subalgebra generation. The present claim is solely the structural reduction of Lie generation to an unrestricted random-subspace spanning problem and the resulting full theta-mixture limit with an exponential convergence bound. Individual Gaussian counts, isotropic counts, and fixed-rank Grassmannian intersection counts are not claimed as new.

## Limitations
The theorem treats two uniformly chosen Lie subalgebras of a nondegenerate one-center Heisenberg Lie algebra, not arbitrary nilpotent Lie algebras or a fixed-dimensional sampling model. Convergence is for fixed \(q\) and is not uniform in growing field size. The proof uses known exact one-subalgebra and Gaussian-subspace counts; a different presentation of these inputs could yield an equivalent theorem. Searches and full-text comparisons reduce but cannot eliminate the risk of terminology-hidden earlier coverage, especially in random-subspace, classical-group, or extraspecial-group literature. Independent mathematical audit has not been performed.

## References
1. S. P. Glasby, A. C. Niemeyer, C. E. Praeger, *The probability of spanning a classical space by two non-degenerate subspaces of complementary dimensions*, arXiv:2109.10015v1, first public 2021-09-21; Lemma 2.1 treats ordinary fixed-dimension complements, https://arxiv.org/abs/2109.10015.
2. S. P. Glasby, A. C. Niemeyer, C. E. Praeger, *Random generation of direct sums of finite non-degenerate subspaces*, arXiv:2111.02198v1, first public 2021-11-03, https://arxiv.org/abs/2111.02198.
3. B. Eick, T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155v1, first public 2022-05-06, https://arxiv.org/abs/2205.03155.
4. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, 2026-09-16, https://arxiv.org/abs/2609.19086.
5. *Exact subalgebra commutativity degree of finite Heisenberg Lie algebras*, published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa.
6. *Exact endpoint norms and Euler-product scaling for the first Grassmann Fourier projection*, published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norms-and-euler-product-scaling-for-the-first-gra--ae0e928d4919.
7. J. Shen, C. Voll, *Symplectic lattice counting and zeta functions of higher Heisenberg groups*, arXiv:2605.23003 (2026), https://arxiv.org/abs/2605.23003.
