# Three-regime rank law for random idempotents in finite-field restricted-range semigroups

## Finding
Let \(q\) be a fixed prime power, \(V=\mathbb F_q^{k+m}\), and \(W\le V\) a specified \(k\)-dimensional subspace. Select an endomorphism \(E:V\to V\) uniformly from the idempotents of the restricted-range semigroup
\[
T(V,W)=\{A\in\operatorname{End}_{\mathbb F_q}(V):\operatorname{im}(A)\subseteq W\}.
\]
Write \(R=\operatorname{rank}(E)\), \(\Phi_j(q)=\prod_{i=1}^{j}(1-q^{-i})\) with \(\Phi_0(q)=1\), and \(\Phi_\infty(q)=\prod_{i\ge1}(1-q^{-i})>0\). For all integers \(k,m\ge0\) and \(0\le r\le k\), the exact number of rank-\(r\) idempotents is
\[
I_{k,m;q}(r)={k\brack r}_q\,q^{r(k+m-r)}
=q^{(2k+m)r-2r^2}\frac{\Phi_k(q)}{\Phi_r(q)\Phi_{k-r}(q)}.
\tag{1}
\]
Here \({k\brack r}_q\) denotes the Gaussian binomial coefficient. The new distributional contribution is a sharp three-regime law for \(k\to\infty\) with \(m=m(k)\ge0\):

* **Interior (\(m-2k\to-\infty\)).** Set \(b_k=\lfloor(2k+m)/4\rfloor\) and \(\theta_k=(2k+m)/4-b_k\). Then the total-variation distance between the law of \(R-b_k\) and the integer-valued discrete Gaussian with weights \(q^{-2(h-\theta_k)^2}\), \(h\in\mathbb Z\), tends to zero. The centering phase \(\theta_k\) belongs to \(\{0,1/4,1/2,3/4\}\); this statement allows it to vary with \(k\).
* **Boundary (\(m=2k+t\), fixed integer \(t\)).** With \(J=k-R\), its law converges in total variation to
\[
\mathbb P_{q,t}(J=j)=\frac{q^{-2j^2-tj}/\Phi_j(q)}{Z_{q,t}},\qquad
Z_{q,t}=\sum_{h=0}^{\infty}\frac{q^{-2h^2-th}}{\Phi_h(q)},\quad j\ge0.
\tag{2}
\]
In particular the probability of a full-image idempotent tends to \(Z_{q,t}^{-1}\), strictly between zero and one.
* **Saturated (\(m-2k\to+\infty\)).** The full-image event \(R=k\) has probability tending to one.

For a fixed real ratio \(m/k\to\alpha\in[0,\infty)\), the normalized rank converges in probability to \(\rho(\alpha)=\min\{1,(2+\alpha)/4\}\), and the total number \(N_{k,m;q}=\sum_{r=0}^k I_{k,m;q}(r)\) has free-energy limit
\[
\lim_{k\to\infty}\frac{\log_q N_{k,m;q}}{k^2}=F(\alpha),\qquad
F(\alpha)=\begin{cases}(2+\alpha)^2/8,&0\le\alpha\le2,\\\alpha,&\alpha\ge2.\end{cases}
\tag{3}
\]
The function \(F\) is continuously differentiable but its second derivative jumps from \(1/4\) to \(0\) at \(\alpha=2\).

## Assumptions and scope
All limits fix \(q\) and let \(k\) tend to infinity. The ambient dimension is \(k+m\), not \(m\). The rank is the ordinary \(\mathbb F_q\)-linear rank of an idempotent, not the semigroup-theoretic *idempotent rank* (minimum size of an idempotent generating set). In the interior regime \(m-2k\to-\infty\), the existence of \(m\ge0\) ensures both the center and its distance from the right endpoint tend to infinity. No limiting field-size asymptotic is asserted. The formulas also include the finite-dimensional cases \(k=0\) and \(m=0\).

## Proof
**Finite classification.** An idempotent is the projection onto its image \(U\) along its kernel \(K\), so \(V=U\oplus K\) and \(E\vert_U=\operatorname{id}_U\). Its image must be an \(r\)-subspace of \(W\), giving exactly \({k\brack r}_q\) possibilities. Relative to one fixed complement \(K_0\) of \(U\) in \(V\), all complements are graphs of unique linear maps \(K_0\to U\), hence there are \(q^{r(k+m-r)}\). This proves the first equality of (1). The product formula for Gaussian binomials gives its second equality. All such projections have image in \(W\), and no endomorphism appears twice.

**Uniform weight control.** Since \(q\ge2\), the product \(\Phi_\infty(q)\) is positive, and for every nonnegative \(j\), \(\Phi_\infty(q)\le\Phi_j(q)\le1\). Consequently the factor \(\Phi_k/(\Phi_r\Phi_{k-r})\) in (1) is between \(\Phi_\infty(q)\) and \(\Phi_\infty(q)^{-2}\). On any family with both \(r\to\infty\) and \(k-r\to\infty\), it converges to \(\Phi_\infty(q)^{-1}\).

**Interior total variation.** Complete the square in the exponent of (1):
\[
(2k+m)r-2r^2=\frac{(2k+m)^2}{8}-2\left(r-\frac{2k+m}{4}\right)^2.
\]
Set \(h=r-b_k\). The permitted interval \(-b_k\le h\le k-b_k\) expands to all of \(\mathbb Z\), since \(b_k\to\infty\) and \(k-b_k\to\infty\) under the interior hypothesis. At each bounded \(h\), the finite-product factor tends uniformly to \(\Phi_\infty(q)^{-1}\). For \(\theta_k\in[0,1)\) every tail is uniformly bounded by a constant times \(\sum_{|h|>H}q^{-2(|h|-1)^2}\), which tends to zero as \(H\to\infty\). Uniform bounded-window approximation and this tail domination show \(\ell^1\), hence total-variation, convergence to the moving discrete Gaussian with weights \(q^{-2(h-\theta_k)^2}\). No unspecified choice of a phase subsequence is needed.

**Critical total variation.** Substitute \(m=2k+t\) and \(r=k-j\) into (1), and divide by the \(r=k\) term \(I_{k,2k+t;q}(k)=q^{k(2k+t)}\):
\[
\frac{I_{k,2k+t;q}(k-j)}{I_{k,2k+t;q}(k)}
=q^{-2j^2-tj}\frac{\Phi_k(q)}{\Phi_{k-j}(q)\Phi_j(q)},\quad0\le j\le k.
\tag{4}
\]
For each fixed \(j\), the quotient of the first two \(\Phi\) factors tends to one. All the terms in (4) are dominated by \(\Phi_\infty(q)^{-2}q^{-2j^2+|t|j}\), which is summable over \(j\ge0\). Dominated convergence for series gives convergence of the normalizing constants to \(Z_{q,t}\), and convergence in \(\ell^1\) of the normalized probabilities proves (2). Since the \(j=0\) term is one and the \(j=1\) term is strictly positive, \(1<Z_{q,t}<\infty\).

**Saturation.** Equation (4), with \(t=m-2k>0\) variable, shows
\[
\frac{\sum_{j=1}^k I_{k,m;q}(k-j)}{I_{k,m;q}(k)}
\le \Phi_\infty(q)^{-2}\sum_{j\ge1}q^{-tj}
=\frac{\Phi_\infty(q)^{-2}q^{-t}}{1-q^{-t}}\to0.
\]
Therefore \(\mathbb P(R=k)\to1\).

**Macroscopic profile and free energy.** For \(r/k\to x\in[0,1]\) and \(m/k\to\alpha\), the base-\(q\) logarithm of each weight divided by \(k^2\) converges to \(x(2+\alpha-2x)\), uniformly over the discrete grid because the product factor is bounded above and below independently of \(k,r\). That strictly concave quadratic has unique maximizer \(\rho(\alpha)\) and maximum \(F(\alpha)\). There are only \(k+1\) weights, so the maximal term controls the logarithmic sum with an additive \(O(\log k)\) error; outside any fixed neighborhood of the maximizer, the exponent is smaller by a positive multiple of \(k^2\). This proves concentration and (3). Direct differentiation verifies the stated smoothness and second-derivative discontinuity at \(\alpha=2\).

## Verification
A standalone standard-library program, `verify.py`, uses direct matrix multiplication and Gaussian elimination to enumerate idempotents in the restricted-range semigroup for thirteen small prime-field parameter triples. It checks every rank coefficient against (1) without using (1) to identify idempotents. Larger arithmetic checks cover \(q\in\{2,3,4,5,7,8,9,11\}\), including prime powers not represented by the exhaustive prime-field enumeration. Numerical critical-window checks compare (4) with (2) for several \(q,t\). Running `python3 verify.py` prints `VERIFY_OK` on success. The infinite statements are supported by the proof above, not by finite tests.

For illustration, over \(\mathbb F_2\) with \(k=3\) and \(m=2\), the counts by ranks \(0,1,2,3\) are \((1,112,448,64)\). At the critical offset \(t=0\), the limit of the full-image probability is approximately \(0.6620638692505193\) for \(q=2\), and \(0.8569539309960834\) for \(q=3\).

## Relationship to prior work
Grau's 2022 work introduces the restricted-range endomorphism semigroup in the wider framework of independence algebras and proves results on regular elements, Green's relations, ideals and extended Green's relations. Sommanee and Sangkhanan's earlier work treats maximal regular subsemigroups, semigroup rank, and idempotent *generating* rank. These structural results motivate a rank distribution over the semigroup's idempotents but do not themselves state its sharp critical-window law. In particular, the finite count (1) is a direct consequence of classical subspace and complement enumeration and is **not claimed independently novel**. The proposed additional content is the joint three-regime probabilistic phase diagram and the nonanalytic free-energy profile extracted in this specific restricted-range setting. Fulman and Goldstein's random finite-field matrix-rank limit concerns unrestricted rectangular random matrices rather than uniformly random restricted-range projections.

## Limitations
The originality comparison covers specified inspected accessible literature and semantic-search results, not a proof of exhaustive publication priority. In particular the available author-hosted presentation of Sommanee--Sangkhanan was only partially text-accessible, so possible equivalent derivations in unseen pages remain a concrete risk. Full-result novelty is weaker if one regards the asymptotic analysis as a direct application of standard discrete Laplace estimates; the elementary exact binomial count alone does not establish substantial originality or value. The theorem concerns fixed \(q\), and no claims are made about growing-field regimes, all regular elements, or generator-set ranks.

## References
1. A. Grau, *The semigroup of endomorphisms with restricted range of an independence algebra*, arXiv:2206.12526v1 (publicly posted 25 June 2022), https://arxiv.org/html/2206.12526v1.
2. W. Sommanee and K. Sangkhanan, *The regular part of a semigroup of linear transformations with restricted range*, Journal of the Australian Mathematical Society 103 (2017), 402--419, DOI:10.1017/S144678871600080X, https://doi.org/10.1017/S144678871600080X.
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Ann. Probab. 43 (2015), 1274--1314; arXiv:1211.0504, https://arxiv.org/abs/1211.0504.
