# Sharp two-source collision law for binary scattered-pair profiles

## Finding

Let \(n\ge1\) be an integer, and let \(p,q\) be **fixed** real numbers in \((0,1)\). Draw independent words \(X_n,Y_n\in\{0,1\}^n\), using independent Bernoulli \(p\) letters for \(X_n\) and independent Bernoulli \(q\) letters for \(Y_n\). Write \(\mathcal D_{\le2}(w)\) for the complete vector of counts (with multiplicities) of the six scattered subsequences \(0,1,00,01,10,11\). Put
\[
s=\sqrt{pq}+\sqrt{(1-p)(1-q)}.
\]
Then, as \(n\to\infty\),
\[
\boxed{\Pr\{\mathcal D_{\le2}(X_n)=\mathcal D_{\le2}(Y_n)\}
=\frac{\sqrt3\,s^{2n+2}}{2\pi n^2\sqrt{pq(1-p)(1-q)}}\bigl(1+o_{p,q}(1)\bigr).}
\]
For equal fair sources this specializes to \(\frac{2\sqrt3}{\pi n^2}(1+o(1))\). For \(p\ne q\), \(s<1\), so the collision has both an exact exponential rate \(s^2\) and a sharp order-\(n^{-2}\) prefactor. The statement is a single two-source theorem; its symmetric-source cases are specializations.

## Assumptions and scope

A scattered occurrence of a word of length two is an ordered pair of distinct increasing positions, not necessarily adjacent. Equivalence is equality of the complete multiplicity vector for lengths one and two. All parameters \(p,q\) are fixed independently of \(n\); no uniform estimate as either parameter approaches zero or one is asserted. The error term is relative to the displayed strictly positive leading expression.

## Proof

**Step 1 (complete profile reduction).** For a word \(w\), let \(K(w)\) be its number of ones and let \(I(w)\) be the number of pairs \(i<j\) with \(w_i=1,w_j=0\). All six subsequence counts are determined by \((n,K,I)\): they are \(n-K\), \(K\), \(\binom{n-K}{2}\), \(K(n-K)-I\), \(I\), and \(\binom K2\), respectively, in the listed order. Conversely, the counts of \(1\) and \(10\) recover \((K,I)\). Consequently two length-\(n\) words have the same profile exactly when they have the same \((K,I)\).

**Step 2 (exact cross-source tilt).** Define
\[
a=\sqrt{pq},\qquad b=\sqrt{(1-p)(1-q)},\qquad s=a+b,\qquad t=a/s.
\]
Let \(A_{n,k,r}\) denote the number of words with \(K=k\) and \(I=r\). Each such word has probabilities \(p^k(1-p)^{n-k}\) and \(q^k(1-q)^{n-k}\) under the respective sources. It follows *exactly for every* \(n\) that
\[
 C_n(p,q):=\Pr\{\mathcal D_{\le2}(X_n)=\mathcal D_{\le2}(Y_n)\}
 =\sum_{k=0}^n\sum_r A_{n,k,r}^2 (pq)^k((1-p)(1-q))^{n-k}
 =s^{2n}C_n(t,t).
\]
Here \(t\in(0,1)\). Thus it remains to determine a single-source collision asymptotic.

**Step 3 (conditional inversion collision).** For each \(k\), let \(B_{n,k}=\binom nk\) and \(f_{n,k}(r)=A_{n,k,r}/B_{n,k}\). Conditional on \(K=k\), all binary words of that composition are uniform. The probability-generating polynomial for \(I\) is the Gaussian binomial coefficient \(\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]_z\); its mean and variance are
\[
 \mu_{n,k}=\frac{k(n-k)}2,\qquad \sigma_{n,k}^2=\frac{k(n-k)(n+1)}{12}.
\]
The local limit theorem of Canfield, Janson and Zeilberger (2009, Theorem 4.5) applies uniformly to \(k/n\) in any fixed closed subinterval of \((0,1)\). It gives, uniformly in integer \(r\),
\[
 f_{n,k}(r)=\frac{e^{-(r-\mu_{n,k})^2/(2\sigma_{n,k}^2)}}{\sqrt{2\pi}\,\sigma_{n,k}}
 +O\!\left(\frac1{n\sigma_{n,k}}\right).
\]
Indeed, in this two-letter regime the theorem's smaller composition \(N_*\) is a positive constant times \(n\), and its condition on the largest composition holds for sufficiently large \(n\). Let \(g_{n,k}(r)\) be the displayed Gaussian term. Since \(\sum_r f_{n,k}(r)=1\) and \(\sum_{r\in\mathbb Z}g_{n,k}(r)=1+o(1)\), the uniform error implies
\[
\left|\sum_r f_{n,k}(r)^2-\sum_{r\in\mathbb Z}g_{n,k}(r)^2\right|
\le\sup_r|f_{n,k}(r)-g_{n,k}(r)|\sum_r(f_{n,k}(r)+g_{n,k}(r))
=O\!\left(\frac1{n\sigma_{n,k}}\right).
\]
A Gaussian Riemann sum (or Poisson summation) then yields
\[
 \sum_r f_{n,k}(r)^2=\frac{1+O(1/n)+o(1)}{2\sqrt\pi\,\sigma_{n,k}}
 =\frac{1+o(1)}{2\sqrt\pi\,\sigma_{n,k}},
\]
uniformly over a fixed central composition band.

**Step 4 (average over the binomial composition).** Fix \(t\in(0,1)\), and set \(b_{n,t}(k)=\binom nk t^k(1-t)^{n-k}\). Then
\[
 C_n(t,t)=\sum_k b_{n,t}(k)^2\sum_r f_{n,k}(r)^2.
\]
In the band \(|k-nt|\le n^{2/3}\),
\[
 \sigma_{n,k}=n^{3/2}\sqrt{\frac{t(1-t)}{12}}\,(1+o(1))
\]
uniformly. Outside that band, \(\sum b_{n,t}(k)^2\le\Pr\{|\operatorname{Bin}(n,t)-nt|>n^{2/3}\}=O_t(e^{-c_t n^{1/3}})\), and every conditional collision is at most one. Finally, Parseval's identity for the characteristic function of a binomial variable gives
\[
 \sum_k b_{n,t}(k)^2
 =\frac1{2\pi}\int_{-\pi}^{\pi}\bigl(1-4t(1-t)\sin^2(\theta/2)\bigr)^n\,d\theta
 =\frac{1+o(1)}{2\sqrt{\pi n t(1-t)}}.
\]
The last equality follows by Laplace's method near the sole maximizer \(\theta=0\). Multiplying the two central Gaussian factors, with negligible tails, gives
\[
 C_n(t,t)=\frac{\sqrt3}{2\pi t(1-t)}\frac{1+o(1)}{n^2}.
\]

**Step 5 (substitute the tilt).** Because \(t(1-t)=ab/s^2=\sqrt{pq(1-p)(1-q)}/s^2\), Step 2 gives
\[
 C_n(p,q)=s^{2n}\,\frac{\sqrt3}{2\pi t(1-t)n^2}(1+o(1))
 =\frac{\sqrt3\,s^{2n+2}}{2\pi n^2\sqrt{pq(1-p)(1-q)}}(1+o(1)).
\]
Cauchy–Schwarz gives \(s\le1\), with equality exactly when \(p=q\). This completes the proof.

## Verification

The standalone standard-library program `verify.py` enumerates the full six-coordinate deck independently for every binary word through length ten and checks that it induces exactly the same partition as \((K,I)\). A second dynamic program enumerates every composition and inversion count, matching direct enumeration through length twelve and exact binomial composition totals through length 160. It checks rational weighted collision identities through length ten. Numerical evaluations for \(n=10,20,40,80,120,160\) and source pairs \((\frac12,\frac12)\), \((\frac14,\frac14)\), \((0.3,0.65)\), \((0.1,0.8)\) approach the stated asymptotic with their ratios at length 160 between \(0.9962\) and \(0.9989\). Run `python3 verify.py`. These finite calculations do not replace the local limit theorem or prove the infinite asymptotic.

## Relationship to prior work

Rigo and Salimov (2013 preprint, later 2015) introduce binomial-equivalence profiles; Lejeune, Rigo and Rosenfeld (2020) identify the binary degree-two profiles with Parikh matrices and cite the exact \(\frac{n^3+5n+6}{6}\) number of fixed-length classes. Golafshan (2026) identifies the full class-size distribution with coefficients of Gaussian binomials. Those class-size identities allow exact finite collision sums, but the inspected statements do not give the sharp stochastic collision probability for two Bernoulli sources. Canfield, Janson and Zeilberger (2009) prove the crucial inversion local limit theorem, but do not study these profile collisions. The contribution is their sharp probabilistic synthesis, including an exact Hellinger-affinity transfer for unequal sources, not a new enumeration of class sizes or a new inversion local limit theorem.

The collision reciprocal is the order-two Rényi-effective number of observable profiles. For a fair source it grows as \(\frac{\pi}{2\sqrt3}n^2\), whereas the *total* number of possible profiles is cubic. Thus sheer profile-count growth overstates the effective discriminatory richness of the scattered-pair sketch under random inputs.

## Limitations

The argument uses a published local limit theorem as a clearly identified input; it is not an independent new proof of that theorem. The asymptotics require fixed positive source parameters and are not asserted uniformly near the boundary of the parameter square. The output is a self-reviewed mathematical claim, **not an independent scientific audit**. As in any literature search, an unindexed calculation of this particular derived collision constant cannot be excluded.

## References

- E. R. Canfield, S. Janson, D. Zeilberger, *The Mahonian probability distribution on words is asymptotically normal*, arXiv:0908.2089v1 (first posted 2009-08-14), especially Theorem 4.5 and the variance formula. https://arxiv.org/abs/0908.2089
- M. Rigo, P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, public author preprint since 2013-05-27; subsequent *Theoretical Computer Science* 601 (2015), 47–57. https://orbi.uliege.be/handle/2268/149313
- M. Lejeune, M. Rigo, M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), especially Section 2. https://arxiv.org/abs/2001.11732
- M. Golafshan, *Binary binomial equivalence via hyperplane arrangements*, arXiv:2606.23426 (first posted 2026-06-22), especially Section 5.2 and Corollaries 5–6. https://arxiv.org/abs/2606.23426
