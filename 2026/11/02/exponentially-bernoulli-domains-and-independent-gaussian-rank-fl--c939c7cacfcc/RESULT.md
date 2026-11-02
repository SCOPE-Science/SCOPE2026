# Exponentially Bernoulli domains and independent Gaussian rank fluctuations in cyclic idempotents

## Finding

Let \(P_n\) be the monoid of partial maps \(f:D\to[n]\), \(D\subseteq[n]\), whose image sequence in increasing order of \(D\) is cyclically nondecreasing. Here a finite sequence is *cyclically nondecreasing* when, after closing it cyclically, it has at most one strict descent. Select an idempotent \(F_n\) uniformly from \(\{f\in P_n:f^2=f\}\), including the empty map. Write \(D_n=|\operatorname{Dom}(F_n)|\) and \(K_n=|\operatorname{Im}(F_n)|\). Put

\[
\lambda=\frac{3+\sqrt5}{2},\quad p=\frac{\lambda}{1+\lambda}=\frac{5+\sqrt5}{10},\quad a=\frac1{\sqrt5},\quad b=\frac2{5\sqrt5}.
\]

**Theorem.** As \(n\to\infty\):

1. The *entire random subset* \(\operatorname{Dom}(F_n)\subseteq[n]\), not just its size, differs in total variation by at most \(O(n^2(2/(1+\lambda))^n)\) from an independent \(p\)-Bernoulli subset of \([n]\).
2. The centered vector converges jointly:
\[
\left(\frac{D_n-pn}{\sqrt n},\frac{K_n-pan}{\sqrt n}\right)
\ \xrightarrow{\mathrm d}\ N_2\left(0,\begin{pmatrix}1/5&\sqrt5/25\\\sqrt5/25&(2+\sqrt5)/25\end{pmatrix}\right).
\]
3. More structurally, the domain fluctuation and the rank residual are asymptotically **independent**:
\[
\left(\frac{D_n-pn}{\sqrt n},\frac{K_n-aD_n}{\sqrt n}\right)
\ \xrightarrow{\mathrm d}\ N(0,1/5)\otimes N\left(0,\frac{1+\sqrt5}{25}\right).
\]
These limits also give \(D_n/n\to p\) and \(K_n/n\to pa=(1+\sqrt5)/10\) in probability. More precisely, the means and covariances differ from \(n\) times the stated constants by exponentially small terms multiplied by a polynomial in \(n\).

## Assumptions and scope

Every \(n\) is a positive integer; composition is composition of partial transformations. An idempotent partial map must have its image in its domain and must fix each point in its image. \(D_n\) counts defined arguments, while \(K_n\) counts distinct images; they are not interchangeable. The Gaussian limits concern uniformly sampled *idempotents*, not uniformly sampled arbitrary transformations or uniformly sampled images. The total-variation statement is over the full Boolean cube \(2^{[n]}\) and does not assume exchangeable coordinates become independent only in fixed marginals.

## Proof

**1. A direct cyclic-gap count.** Let \(A_m(u)=\sum_{k=1}^m a_{m,k}u^k\), where \(a_{m,k}\) is the number of idempotents of the full orientation-preserving transformation monoid on a cyclically ordered set of size \(m\), with image size \(k\). For \(m\ge1\), \(a_{m,1}=m\). For \(2\le k\le m\), the \(k\) fixed image points appear in cyclic order and every inverse-image class is a circular interval containing exactly its fixed image point. Let \(g_i\ge0\) be the number of non-fixed points in the arc from fixed point \(i\) to fixed point \(i+1\). The separating cut in this arc has \(g_i+1\) choices. Rooting the cyclic list of gaps at one of the \(m\) labeled positions and dividing by its \(k\) possible choices of a fixed-point root gives
\[
 a_{m,k}=\frac mk\sum_{g_1+\cdots+g_k=m-k}\prod_{i=1}^k(g_i+1)
 =\frac mk[z^{m-k}](1-z)^{-2k}
 =\frac mk\binom{m+k-1}{m-k}.
\]
This finite rank count is already implicit in the cited 2022 enumeration; it is used as established input rather than asserted as the novel conclusion. The special case \(k=1\) is \(m\), not the formal \(m^2\) obtained from the displayed \(k\ge2\) formula.

**2. Exact bivariate polynomial.** For a formal variable \(u\) near 1, let \(\lambda(u)\) be the larger root of \(t^2-(2+u)t+1=0\), analytically continued near \(u=1\). The logarithmic series gives, for \(m\ge1\),
\[
\sum_{k\ge1}\frac mk\binom{m+k-1}{m-k}u^k
=m[z^m]\log\frac{(1-z)^2}{(1-z)^2-uz}
=\lambda(u)^m+\lambda(u)^{-m}-2.
\]
Consequently,
\[
 A_m(u)=\lambda(u)^m+\lambda(u)^{-m}-2-m(m-1)u.
\]
For \(m=0\), put \(A_0(u)=1\), accounting for the empty map. A partial idempotent with a prescribed domain of size \(m\) restricts to a full orientation-preserving idempotent on that domain. Thus the *exact* joint rank/domain generating polynomial is
\[
 H_n(s,u)=\sum_{m=0}^n\binom nm s^mA_m(u)
 =(1+s\lambda(u))^n+(1+s\lambda(u)^{-1})^n-2(1+s)^n+1-n(n-1)u s^2(1+s)^{n-2}.
\]
For \(n=1\) interpret the last term as zero. The constant \(H_n(1,1)\) is exactly the number of idempotents in \(P_n\).

**3. Exponentially accurate Bernoulli-domain law.** Set \(W_n=(1+\lambda)^n\), \(Z_n=H_n(1,1)\). For every particular subset \(A\subseteq[n]\) of cardinality \(m\), the unnormalized probability weight of the event \(\operatorname{Dom}(F_n)=A\) is \(A_m(1)\). Compare it with the independent Bernoulli law's unnormalized weight \(\lambda^m\). The explicit formula above, together with \(A_0(1)=1\), gives
\[
 \sum_{A\subseteq[n]}|A_{|A|}(1)-\lambda^{|A|}|
 \le (n^2+3)2^n.
\]
In particular \(|Z_n-W_n|\le(n^2+3)2^n\) and \(Z_n/W_n\to1\). Normalizing the two weight systems and applying the triangle inequality gives
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(\operatorname{Dom}(F_n)),\operatorname{Bernoulli}(p)^{\otimes n}\bigr)
 \le \frac{(n^2+3)2^n}{Z_n}
 =O\left(n^2\left(\frac2{1+\lambda}\right)^n\right).
\]
The inequality is valid as written because the coefficients \(A_m(1)\) never exceed \(\lambda^m\) (the \(m=0\) case is equality); an alternative triangle estimate with an absolute constant gives the same asserted bound without using the one-sided inequality. Since \(1+\lambda>2\), the error decays exponentially.

**4. Joint Gaussian limit.** The moment-generating function for \((D_n,K_n)\) is \(H_n(e^t,e^v)/Z_n\). On a sufficiently small complex neighborhood of \((t,v)=(0,0)\), its first exponential term dominates all remaining terms exponentially: their bases at the origin are \(1+\lambda^{-1}<2<1+\lambda\), and the polynomial factor \(n^2\) is harmless. Therefore, locally uniformly,
\[
 \log\frac{H_n(e^t,e^v)}{Z_n}
 =n\left(h(t,v)-h(0,0)\right)+O(c^n),\qquad
 h(t,v)=\log(1+e^t\lambda(e^v)),
\]
for some \(0<c<1\) (or \(O(n^2 c^n)\) if the base is kept explicit). Let \(g(v)=\log\lambda(e^v)=\operatorname{arcosh}(1+e^v/2)\). Direct differentiation gives \(g'(0)=a\), \(g''(0)=b\). With \(p=\lambda/(1+\lambda)\), the gradient and Hessian of \(h\) at zero are
\[
 \nabla h(0,0)=(p,pa),\qquad
 \nabla^2 h(0,0)=\begin{pmatrix}p(1-p)&p(1-p)a\\p(1-p)a&pb+p(1-p)a^2\end{pmatrix}.
\]
These entries simplify to the matrix stated above. Put \(t=x/\sqrt n\), \(v=y/\sqrt n\), subtract the linear term and use Taylor's formula. The log moment-generating functions converge to the Gaussian quadratic form; the multivariate continuity theorem proves assertion 2. Replacing the second coordinate by \(K_n-aD_n\) diagonalizes the limiting covariance: the residual variance is \(pb=(1+\sqrt5)/25\), proving assertion 3. Differentiating the uniform analytic expansion establishes the stated mean/covariance estimates. No finite enumeration is used to prove the infinite limits.

## Verification

The companion `verify.py` independently enumerates each partial map from \([n]\) to \([n]\) for \(1\le n\le6\), explicitly checks idempotence and the cyclic descent condition, and compares all joint \((|D|,|\operatorname{Im}|)\) counts against the cyclic-gap formula. It then performs 50 further integer polynomial checks through \(n=50\), comparing a Chebyshev recurrence with the binomial domain transform. Command: `python3 verify.py`. Successful output: `VERIFY_OK: 56 enumeration and exact polynomial checks`. These checks corroborate finite identities only; the uniform asymptotic estimates and Gaussian limit follow from the proof.

## Relationship to prior work

The monoid and its cyclic-sequence definition are standard; the 2022 paper of Li and Fernandes calculates the numbers of full and partial orientation-preserving idempotents by rank (Lemmas 3.2 and 3.4), including a different explicit sum. The 2011 paper of Fernandes, Gomes, and Jesus gives the total idempotent count in terms of Lucas numbers and a binomial transform; hence neither the finite counts nor their exact generating polynomial is claimed as an independent enumeration discovery. Umar's 2011 paper enumerates breadth and height profiles of *all* orientation-preserving partial maps, without conditioning on idempotence. The separate 2026 work of An, Zhang, and He concerns fixed points of *all full* orientation-preserving maps. These distinctions matter: our assertion is the exponentially accurate product-measure law for the **whole domain subset** of a uniform partial idempotent, together with its **joint** domain/image-rank Gaussian limit and independent rank-residual fluctuation.

## Limitations

The novelty claim is restricted to these quantitative probability laws and their joint asymptotic independence, not the previously known exact idempotent enumerations. Prior exact formulas do determine finite distributions and make an analytic derivation possible; a differently phrased asymptotic in the older probabilistic or analytic-combinatorics literature remains a publication-priority risk. The bound is asymptotic in \(n\), not a claim that the finite-domain coordinates are independent. The Gaussian law does not assert an unproved local limit theorem or convergence under arbitrary sampling schemes. Independent mathematical review has not been performed.

## References

1. De Biao Li and Vítor H. Fernandes, *Endomorphisms of semigroups of oriented transformations*, arXiv:2207.12823, first public version 2022-07-26, especially Section 3 and Lemmas 3.2 and 3.4. https://arxiv.org/abs/2207.12823
2. Vítor H. Fernandes, Gracinda M. S. Gomes, and Manuel M. Jesus, *The cardinal and the idempotent number of various monoids of transformations on a finite chain*, Bulletin of the Malaysian Mathematical Sciences Society 34 (2011), 79–85, Section 2. https://emis.muni.cz/journals/BMMSS/pdf/v34n1/v34n1p7.pdf
3. A. Umar, *Combinatorial results for semigroups of orientation-preserving partial transformations*, Journal of Integer Sequences 14 (2011), Article 11.7.5, especially Proposition 5 and Corollary 6. https://cs.uwaterloo.ca/journals/JIS/VOL14/Umar/umar2.pdf
4. Yang An, Wen Ting Zhang, Yi He, *Fixed points of orientation-preserving full transformation*, arXiv:2604.26661, 2026-04-29, a related but distinct sampling model. https://arxiv.org/abs/2604.26661
