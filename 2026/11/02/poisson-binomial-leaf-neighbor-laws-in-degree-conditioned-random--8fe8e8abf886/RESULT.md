# Poisson-binomial leaf-neighbor laws in degree-conditioned random labeled trees

## Finding

Let \(T\) be uniform over the \(n^{n-2}\) labeled trees on \([n]\), with \(n\ge 3\). Fix a vertex \(v\), and condition on \(\deg_T(v)=d\), where \(1\le d\le n-1\). For each \(u\ne v\) put \(I_u=\mathbf 1\{uv\in E(T),\ \deg_T(u)=1\}\), and let \(L=\sum_{u\ne v} I_u\): the number of leaf neighbors of \(v\).

**Theorem.** If \(1\le d\le n-2\), define \(N=n-1\), \(m=N-d\ge1\), and the linear polynomial operator
\[
\mathcal D_N f(t)=Nf(t)+(1-t)f'(t).
\]
Then the exact conditional probability-generating polynomial is
\[
G_{n,d}(t):=\mathbb E[t^L\mid\deg_T(v)=d]
=\frac{\mathcal D_N^{m-1}(t^{d-1})}{N^{m-1}}.
\]
Every zero of \(G_{n,d}\) is real and nonpositive. Equivalently, \(L\) is distributed as the sum of \(d-1\) independent (possibly deterministic) Bernoulli random variables, with parameters determined by those zeros. The full conditional vector \((I_u:u\ne v)\) is **strongly Rayleigh**, and hence negatively associated. When \(d=n-1\), the tree is a star and \(L=n-1\) deterministically; the same conclusions hold with \(n-1\) deterministic Bernoulli variables.

In particular, when \(n\ge4\) and \(2\le d\le n-2\), for distinct \(u,w\ne v\),
\[
\operatorname{Cov}(I_u,I_w\mid\deg_T(v)=d)<0.
\]
In the nonstar case the exact support is every integer from \(\max\{0,2d-n+1\}\) through \(d-1\). These conclusions apply at every finite \(n\) and admissible \(d\), without an asymptotic assumption.

## Assumptions and scope

Trees are undirected, simple, labeled, and chosen uniformly; the vertex \(v\) is fixed before sampling. The indicator \(I_u\) requires both adjacency to \(v\) and total tree degree one at \(u\). Conditional probabilities refer to the positive-probability event \(\deg_T(v)=d\). The exceptional case \(n=2\) is omitted to keep the root-as-leaf ambiguity out of the statement. The conditional law is exchangeable over the \(N=n-1\) labels other than \(v\).

## Proof

**1. Rooted-forest reduction and enumeration.** Delete \(v\) and root each of the resulting \(d\) components at its former neighbor of \(v\). This is a bijection between trees with the prescribed root degree and rooted labeled forests on the other \(N=n-1\) vertices with exactly \(d\) components. Moreover, \(I_u=1\) exactly when \(u\) forms a singleton component. Write \(T(z)\) for the exponential generating function for labeled rooted trees; it satisfies \(T(z)=ze^{T(z)}\). Marking a singleton component by \(t\) changes the rooted-tree series to \(T(z)+(t-1)z\). Thus
\[
G_{n,d}(t)=\frac{[z^N]\big(T(z)+(t-1)z\big)^d}{[z^N]T(z)^d}
=\frac{[z^m]\big(e^{T(z)}+t-1\big)^d}{[z^m]e^{dT(z)}}.
\]
For \(m\ge1\), Lagrange inversion yields
\[
[z^m]e^{jT(z)}=\frac{j(m+j)^{m-1}}{m!}\quad (j\ge1).
\]
Consequently the numerator, after multiplication by \(m!\), equals
\[
\sum_{j=1}^{d}\binom dj j(m+j)^{m-1}(t-1)^{d-j}
=d\sum_{k=0}^{d-1}\binom{d-1}{k}(m+1+k)^{m-1}(t-1)^{d-1-k}.
\]
The operator \(\mathcal D_N=N-(t-1)\tfrac{d}{dt}\) acts on \((t-1)^{d-1-k}\) by multiplication by \(N-(d-1-k)=m+1+k\). Since \(t^{d-1}=\sum_k\binom{d-1}{k}(t-1)^{d-1-k}\), the numerator is \(d\mathcal D_N^{m-1}(t^{d-1})/m!\). Substituting \(t=1\) yields the denominator \(dN^{m-1}/m!\), proving the asserted exact polynomial formula.

**2. Nonpositive real zeros.** We prove a preservation lemma. Suppose a nonzero polynomial \(f\) has nonnegative coefficients, degree \(r<N\), and all zeros in \(( -\infty,0]\). Its image \(\mathcal D_Nf\) has degree \(r\), positive leading coefficient, and nonnegative coefficients: the coefficient of \(t^k\) is \((N-k)a_k+(k+1)a_{k+1}\). For distinct zeros \(-\lambda_j\), of multiplicities \(b_j\), the logarithmic quotient outside the zeros is
\[
\frac{\mathcal D_Nf(t)}{f(t)}
=N+(1-t)\sum_j\frac{b_j}{t+\lambda_j}.
\]
Its derivative is \(-\sum_j b_j(1+\lambda_j)/(t+\lambda_j)^2<0\). It tends to \(N-r>0\) as \(t\to-\infty\), and has poles with a sign change across each distinct zero. Hence it has exactly one zero to the left of the leftmost zero of \(f\), and one between each adjacent pair of distinct zeros. A zero of \(f\) of multiplicity \(b_j\) remains a zero of \(\mathcal D_Nf\) of multiplicity \(b_j-1\). These account for all \(r\) zeros and lie in \(( -\infty,0]\). The constant-polynomial case is immediate. Iterate the lemma from \(f(t)=t^{d-1}\); throughout, \(d-1<N\). Therefore \(G_{n,d}\) has only nonpositive real zeros.

**3. Distribution and dependence.** Because \(G_{n,d}\) has nonnegative coefficients, \(G_{n,d}(1)=1\), and only nonpositive real zeros, its degree-\(d-1\) factorization is \(\prod_{j=1}^{d-1}(1-q_j+q_jt)\) with \(0<q_j\le1\), proving the Poisson-binomial representation. The joint generating polynomial of the exchangeable indicator vector is
\[
\sum_{\ell=0}^{N}\frac{\Pr(L=\ell\mid\deg(v)=d)}{\binom N\ell}\,e_\ell(z_1,\ldots,z_N),
\]
which is the \(N\)-variable symmetric multi-affine polarization of \(G_{n,d}\). By the Grace–Walsh–Szegő polarization theorem, it is real stable, hence the indicator measure is strongly Rayleigh. The strongly Rayleigh negative-association theorem then gives negative association (including the stronger conditional forms).

**4. Strict pairwise covariance and support.** Deleting prescribed pendant neighbors gives, for distinct \(u,w\ne v\) and \(2\le d\le n-2\),
\[
\Pr(I_u=1\mid d)=\frac{d-1}{n-2}\left(\frac{n-2}{n-1}\right)^{n-d-1}=:p_1,
\]
\[
\Pr(I_u=I_w=1\mid d)=\frac{(d-1)(d-2)}{(n-2)(n-3)}\left(\frac{n-3}{n-1}\right)^{n-d-1}=:p_2.
\]
Their ratio satisfies
\[
\frac{p_2}{p_1^2}=\frac{(d-2)(n-2)}{(d-1)(n-3)}\left(1-\frac1{(n-2)^2}\right)^{n-d-1}<1,
\]
with the \(d=2\) case interpreted as zero. Thus the covariance is strictly negative. Every forest with \(d\) components and \(N\) vertices has between \(\max\{0,2d-N\}\) and \(d-1\) singleton components when \(N>d\), and every intermediate number is attainable by valid positive-size component allocations and rooted trees. This proves the support assertion. The star case is direct.

## Verification

The accompanying standalone `verify.py` uses independent Prüfer-code enumeration of every labeled tree for \(3\le n\le8\), matching every conditional probability coefficient against the differential-operator formula. It separately checks factorial moments obtained by deleting prescribed pendant neighbors for all \(3\le n\le50\), exact strict pairwise covariance inequalities for \(4\le n\le100\), and, when SymPy is installed, exact Sturm-root counts for \(3\le n\le16\). All 27,106 assertions passed in the recorded verification. The algebraic proof, not these finite checks, establishes the theorem for all admissible sizes.

## Relationship to prior work

Pitman's *Coalescent Random Forests* (technical report dated September 1, 1996, §2) supplies the established rooted-forest enumeration and probabilistic model; no priority is claimed for Cayley enumeration or the tree–forest bijection. Borcea, Brändén, and Liggett (arXiv 0707.2340, 2007; §4) establish polarization/stability machinery and the general strongly Rayleigh negative-association theorem; these are used as prior theorems, not claimed anew. Bóna and Mező (arXiv 0705.2734, 2015 version, §§1–2) prove real-rootedness for a different generating polynomial: partitions into nonsingleton blocks enumerated by the number of blocks, rather than singleton components of rooted forests at fixed component count. The result here is the exact degree-conditioned local leaf law and its real-rootedness/strong Rayleigh consequence, not a generic theorem about all spanning-tree edge measures.

## Limitations

This is a finite uniform complete-graph spanning-tree statement. It does not assert the same properties for weighted spanning trees on arbitrary graphs, unconditional leaf-neighbor indicators, or multitype conditioned forests. The Bernoulli parameters are specified through zeros rather than elementary formulas. The established references may contain indirect consequences through broader enumeration or stability principles; no unconditional claim of historical priority or independent external certification is made.

## References

- J. Pitman, *Coalescent Random Forests*, University of California, Berkeley Statistics Technical Report 457 (dated September 1, 1996; revised 1998), §§2–3. https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf
- J. Pitman, *The Multinomial Distribution on Rooted Labeled Forests*, Berkeley Statistics Technical Report 499 (June 1998), §§1–2. https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/499.pdf
- J. Borcea, P. Brändén, T. M. Liggett, *Negative Dependence and the Geometry of Polynomials*, arXiv:0707.2340 (first posted July 16, 2007), especially Corollary 4.7 and Theorem 4.9. https://arxiv.org/pdf/0707.2340
- M. Bóna and I. Mező, *Real Zeros and Partitions without Singleton Blocks*, arXiv:0705.2734 (relevant 2015 version), §§1–2. https://arxiv.org/pdf/0705.2734
