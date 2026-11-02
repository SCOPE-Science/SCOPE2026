# Terminal-vertex negative regression against cyclic-vertex counts in random mappings

## Finding

Let \(f:[n]\to[n]\) be uniformly sampled from the \(n^n\) self-maps, for an integer \(n\ge2\). Write \(C_n\) for the number of vertices lying on directed cycles of \(f\), and \(L_n\) for the number of vertices of indegree zero (terminal vertices, also called leaves). For every \(1\le k\le n\), put \(m=n-k\). Conditional on \(C_n=k\), \(L_n\) has **exactly** the occupancy law of the number of empty boxes among a specified set of \(m\) boxes when \(m-1\) independent uniformly chosen balls are thrown into \(n\) boxes (with \(L_n=0\) if \(m=0\)). Specifically, for \(0\le s\le m\),
\[
\mathbb E[(L_n)_s\mid C_n=k]=(m)_s\left(1-\frac{s}{n}\right)^{m-1}\quad (m\ge1).
\]
Here \((z)_s=z(z-1)\cdots(z-s+1)\), with \((z)_0=1\). The conditional probability of \(L_n=\ell\) is, when \(m\ge1\),
\[
{m\choose\ell}\sum_{j=0}^{m-\ell}(-1)^j{m-\ell\choose j}\left(1-\frac{\ell+j}{n}\right)^{m-1},\qquad 0\le\ell\le m.
\]

For fixed \(n\), these conditional distributions are **strictly decreasing in the usual stochastic order** as \(k\) increases. Hence, for nondecreasing real functions \(\phi,\psi\),
\[
\operatorname{Cov}\!\bigl(\phi(C_n),\psi(L_n)\bigr)\le0,
\]
strictly if both functions are strictly increasing on their attainable supports. In particular, this implies negative quadrant dependence, not merely negative covariance.

The ordinary covariance has the exact form
\[
\operatorname{Cov}(C_n,L_n)=n\left(1-\frac1n\right)^n \bigl(\mathbb E C_{n-1}-\mathbb E C_n\bigr)<0,
\]
where \(C_{n-1}\) refers to a separate uniform mapping of \(n-1\) vertices. In the limit,
\[
\operatorname{Cov}(C_n,L_n)=-\frac{\sqrt{\pi/8}}e\sqrt n+o(\sqrt n),\qquad
\operatorname{Corr}(C_n,L_n)=-\frac{\sqrt{\pi/8}}{\sqrt{(2-\pi/2)(e-2)}}\,n^{-1/2}+o(n^{-1/2}).
\]
Thus negative stochastic dependence persists at each finite size even as correlation tends to zero.

## Assumptions and scope

All mappings are sampled independently across their \(n\) source vertices with equal target probability \(1/n\). Loops and cycles of every length are allowed. A terminal vertex has **zero incoming** directed edges, not zero outgoing edges. Every map has at least one cyclic vertex, and no cyclic vertex can be terminal. The general stochastic and exact identities hold for each integer \(n\ge2\). The occupancy convention when \(m=0\) is the constant zero random variable. Asymptotic statements take \(n\to\infty\) with no conditioning on \(C_n\).

## Proof

**1. Exact cyclic-vertex law.** If precisely \(k\) vertices are cyclic, choose them in \({n\choose k}\) ways, arrange their outgoing arrows as any of the \(k!\) permutations, and attach the remaining vertices as a forest of \(k\) rooted directed trees. The rooted-forest count for a specified root set is \(k n^{n-k-1}\), including the all-cyclic boundary \(k=n\), where this expression is one. Thus
\[
\mathbb P(C_n=k)=\frac{k(n)_k}{n^{k+1}},\qquad 1\le k\le n.
\]
Equivalently, by summation of the telescoping difference,
\[
\mathbb P(C_n\ge j)=\frac{(n)_j}{n^j},\qquad 1\le j\le n.
\]
One way to see the telescoping is \(k(n)_k/n^{k+1}=(n)_k/n^k-(n)_{k+1}/n^{k+1}\).

**2. Jointly forbidding incoming edges.** Let \(S\subset[n]\) have size \(s\) and let \(A_S\) be the event that none of its vertices receives an incoming arrow. Each of the \(n\) source arrows must then point into \([n]\setminus S\), giving \(\mathbb P(A_S)=(1-s/n)^n\). Under \(A_S\), the restriction of the map to \([n]\setminus S\) is itself a uniform mapping on \(n-s\) vertices; no element of \(S\) can lie on a cycle because no arrow enters \(S\). Therefore
\[
\mathbb P(A_S,C_n=k)=\left(\frac{n-s}{n}\right)^n \mathbb P(C_{n-s}=k).
\]
When \(n-s\ge k\) and \(m=n-k\ge1\), substitute the preceding cyclic-vertex law and simplify:
\[
\mathbb P(A_S\mid C_n=k)=\frac{(m)_s}{(n)_s}\left(1-\frac{s}{n}\right)^{m-1},\qquad 0\le s\le m.
\]
The left side is zero when \(s>m\). Summing over ordered distinct choices of \(S\) yields the factorial-moment identity. The occupancy count \(O_m\) of empty eligible boxes after \(m-1\) throws has the same factorial moments because every specified ordered set of \(s\) eligible boxes survives all throws with probability \((1-s/n)^{m-1}\). Factorial moments determine the law of a variable supported on \(\{0,1,\ldots,m\}\); inclusion–exclusion produces the displayed probability formula.

**3. Strict negative regression.** Fix an infinite sequence of independent uniform draws \(B_1,B_2,\ldots\) from \([n]\). For \(1\le m\le n-1\), let \(O_m\) be the number of unhit boxes among \(1,\ldots,m\) after draws \(B_1,\ldots,B_{m-1}\), and set \(O_0=0\). When passing from \(O_m\) to \(O_{m+1}\), the new eligible box adds at most one empty box, while the one new ball can eliminate at most one; these effects are coupled so that \(O_{m+1}\ge O_m\) almost surely. Indeed the difference is either zero or one. It is strictly positive with positive probability (for \(m=0\), it equals one). Hence the conditional laws \(L_n\mid C_n=k\), equal in law to \(O_{n-k}\), are strictly decreasing in \(k\). For nondecreasing \(\psi\), put \(g(k)=\mathbb E[\psi(L_n)\mid C_n=k]\), a nonincreasing function. The identity
\[
2\operatorname{Cov}(\phi(C_n),g(C_n))=\mathbb E\left[(\phi(C_n)-\phi(C_n'))(g(C_n)-g(C_n'))\right],
\]
with an independent copy \(C_n'\), gives nonpositivity and the stated strictness. Taking indicator functions of upper tails proves negative quadrant dependence.

**4. Covariance identity.** For any marked vertex \(v\), conditioned on it having indegree zero, the map on the other \(n-1\) vertices is uniform, and all cycles lie there. Consequently, for arbitrary \(\phi\),
\[
\mathbb E[\phi(C_n)L_n]=n\left(1-\frac1n\right)^n\mathbb E[\phi(C_{n-1})],\qquad \mathbb E L_n=n\left(1-\frac1n\right)^n.
\]
Subtracting the product of means gives the exact covariance identity for \(\phi(C_n)\) and \(L_n\). Strict negativity follows from the preceding stochastic ordering.

**5. Sharp covariance and correlation scale.** Put \(a_n(j)=(n)_j/n^j\) for \(1\le j\le n\) and zero outside this range. Tail summation gives \(\mathbb E C_n=\sum_j a_n(j)\). For fixed \(x\ge0\) and \(j/\sqrt n\to x\), elementary logarithmic expansions give
\[
a_n(j)\to e^{-x^2/2},\qquad n\bigl(a_n(j)-a_{n-1}(j)\bigr)\to\frac{x^2}{2}e^{-x^2/2}.
\]
For \(j\le n/2\), write \(a_{n-1}(j)/a_n(j)=\prod_{i=0}^{j-1}(1-i/((n-1)(n-i)))\). The inequality \(1-\prod_i(1-u_i)\le\sum_i u_i\), together with \(a_n(j)\le\exp[-j(j-1)/(2n)]\), bounds the difference by \(O(j^2/n^2)\exp[-j(j-1)/(2n)]\). For \(j>n/2\), each summand is at most \(a_n(j)\le\exp(-c n)\) for an absolute \(c>0\). These estimates justify dominated Riemann summation:
\[
\sqrt n\bigl(\mathbb E C_n-\mathbb E C_{n-1}\bigr)\to \int_0^\infty\frac{x^2}{2}e^{-x^2/2}\,dx=\sqrt{\pi/8}.
\]
Multiplication by \(\mathbb E L_n\sim n/e\) proves the covariance asymptotic. The same Gaussian tail bounds show \(C_n/\sqrt n\) converges with two moments to a Rayleigh variable of density \(xe^{-x^2/2}\) on \(x>0\), so \(\operatorname{Var}(C_n)/n\to2-\pi/2\). For leaves, the independent-target representation gives
\[
\operatorname{Var}(L_n)=n p_n(1-p_n)+n(n-1)(q_n-p_n^2),\quad p_n=\left(1-\frac1n\right)^n,\quad q_n=\left(1-\frac2n\right)^n.
\]
Taylor expansion proves \(\operatorname{Var}(L_n)/n\to e^{-1}-2e^{-2}=e^{-2}(e-2)\). Dividing the covariance asymptotic by the standard deviations yields the correlation coefficient stated above.

## Verification

An independent exhaustive checker (`checker.py`, standard-library Python) directly enumerates each of the \(n^n\) maps for \(1\le n\le6\) (50,069 mappings in all), directly counts cyclic and zero-indegree vertices, compares the full conditional law against independently enumerated occupancy configurations, verifies factorial moments, negative conditional stochastic order, exact covariance and tail identities, and checks the leading asymptotic constant numerically at selected large sizes. The checker reports 241 passed exact/numerical assertions. The finite enumeration and numerical values corroborate but do not establish the unrestricted mathematical proof above.

## Relationship to prior work

Mutafchiev and Finch (2023) study the deepest cycle and classical marginal cyclic-vertex structure of uniform random mappings, not a joint terminal-vertex conditional distribution. Drmota and Soria (1997) develop a general generating-function framework for images and preimages of random mappings and analyze indegree multiplicities; that framework is an important potential source of implicit moment identities. Tavaré (2022) gives exact cyclic-vertex tails in a related random-mapping model, independently consistent with the tail formula used here. Flajolet and Odlyzko (1990) and earlier work establish much of the underlying random-mapping enumerative machinery. None of their specifically inspected claims states the conditional finite-occupancy representation, strict stochastic antitonicity and sharp joint covariance/correlation scale together; this is a provisional best-knowledge originality judgment, not a certified priority claim.

## Limitations

All dependence conclusions require uniformly random complete self-maps. They need not carry over to conditioned connectivity, nonuniform target probabilities or forests with preassigned roots. The leading covariance is an asymptotic, not a uniform finite-sample error bound. General generating-function identities in older literature could encode the exact factorial moments implicitly; historical priority has not been independently established. Independent mathematical validation has not been performed.

## References

1. Ljuben Mutafchiev and Steven Finch, *On the Deepest Cycle of a Random Mapping*, arXiv:2301.13829 (first posted January 31, 2023), https://arxiv.org/abs/2301.13829.
2. Michael Drmota and Michèle Soria, *Images and Preimages in Random Mappings*, *SIAM Journal on Discrete Mathematics* 10 (1997), DOI:10.1137/S0895480194268421.
3. Simon Tavaré, *A note on the Screaming Toes game*, *Journal of Applied Probability* 59 (2022), DOI:10.1017/jpr.2021.32.
4. Philippe Flajolet and Andrew Odlyzko, *Random Mapping Statistics* (1990), DOI:10.1007/3-540-46885-4_34.
5. Antti Mylläri, *Limit distributions for the number of leaves in a random forest* (2002), DOI:10.1239/aap/1037990959.
