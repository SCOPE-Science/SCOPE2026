# A universal one-quarter mixing reversal and a two-moment alias in four-site epidemic spread

## Finding

Consider a four-site independent-bond epidemic with a uniformly random initial case. Every unordered pair receives an independent global transmission opportunity of probability \(g\). In addition, the three edges of a fixed local spanning tree receive independent local opportunities of probability \(r\); a contact succeeds if at least one opportunity succeeds. Compare the star \(K_{1,3}\) with the four-vertex path \(P_4\), leaving the values of \(g\) and \(r\) unchanged. Let \(Z_S\) and \(Z_P\) denote the final infected-component sizes, respectively.

**Theorem.** For all \(0\le g,r\le1\), put
\[
p=g+(1-g)r,\qquad K=(1-p)(p-g)^2.
\]
The entire difference of final-size laws is
\[
\boxed{\left(\Pr(Z_S=j)-\Pr(Z_P=j)\right)_{j=1}^{4}
 =\frac K4\left(1,-4(1-g),3,-4g\right).}
\]
Consequently,
\[
\boxed{\mathbb E Z_S-\mathbb E Z_P=\frac K2(1-4g),\qquad
\mathbb E Z_S^2-\mathbb E Z_P^2=3K(1-4g).}
\]
For nondegenerate mixing \(0<g<1\), \(0<r<1\), the star has strictly greater mean outbreak size for \(g<1/4\), the path has strictly greater mean for \(g>1/4\), and they tie precisely at \(g=1/4\). The threshold does not depend on local contact efficiency \(r\). Yet the path has strictly greater complete-outbreak probability for **every** such \(g,r\):
\[
\Pr(Z_P=4)-\Pr(Z_S=4)=gK>0.
\]
At the mean crossover, the first and second raw moments, and hence mean and variance, coincide while the laws remain distinct:
\[
\left(\Pr(Z_S=j)-\Pr(Z_P=j)\right)_{j=1}^{4}
=\frac K4(1,-3,3,-1),\qquad
\mathbb E Z_S^3-\mathbb E Z_P^3=-\frac{3K}{2}<0.
\]
Four vertices are the smallest population size with two nonisomorphic connected local spanning trees; all trees on at most three vertices are isomorphic.

## Assumptions and scope

The sites are \(V=\{1,2,3,4\}\). The local star has edges \(\{12,13,14\}\) and the local path has edges \(\{12,23,34\}\). All global and local Bernoulli opportunities are mutually independent. Successful undirected edges are transmissible in either direction and the epidemic reaches precisely the connected component containing a uniformly selected initial vertex. This is an explicitly defined undirected bond-percolation epidemic, **not** a claim about arbitrary continuous-time SIR models with correlated outgoing transmissions or variable infectious periods. The observation is the complete cluster size \(Z\), including the initial site. No asymptotic or large-population limit is taken.

On local edges the union of two opportunities has probability \(p=1-(1-g)(1-r)\); on the other three edges the probability is \(g\). These six edge states are mutually independent. The theorem includes endpoints \(g,r\in\{0,1\}\), where some differences vanish. All strict inequalities stated above assume \(0<g,r<1\).

## Proof

Write \(q=g\) temporarily and consider the six unordered pairs \(12,13,14,23,24,34\). Let \(T\) be the local tree. For any set \(A\) of successful edges, write \(k=|A\cap T|\), \(\ell=|A\setminus T|\). Its probability is
\[
w_{k\ell}=p^k(1-p)^{3-k}q^{\ell}(1-q)^{3-\ell}.
\]
If the connected components of \((V,A)\) are \(C\), then the probability that a uniform seed produces an outbreak of size \(j\), conditional on \(A\), equals \(\frac14\sum_C |C|\mathbf1_{\{|C|=j\}}\). This formula exactly enumerates all four possible seeds without assuming independence of infection outcomes.

For each \(j,k,\ell\), sum \(\sum_C|C|\mathbf1_{\{|C|=j\}}\) over the sets \(A\) having \(k\) local successes and \(\ell\) nonlocal successes. Subtract the path total from the star total. A complete tabulation of the **nonzero** differences, arranged as vectors with coordinates \(j=1,2,3,4\), is:

| \((k,\ell)\) | Star count minus path count |
|---|---|
| \((0,2)\), \((2,0)\) | \((1,-4,3,0)\) |
| \((1,1)\) | \((-2,8,-6,0)\) |
| \((0,3)\), \((2,1)\) | \((1,0,3,-4)\) |
| \((1,2)\) | \((-2,0,-6,8)\) |

All other \((k,\ell)\) rows vanish. This table follows directly by considering the \(2^6=64\) subsets of the named six edges and partitioning their connected components. It is independently reproduced by the embedded exact checker.

Set \(A_0=(1,-4,3,0)\) and \(B_0=(1,0,3,-4)\). The first three rows contribute the scalar
\[
X=w_{02}+w_{20}-2w_{11}=(1-p)(1-q)(p-q)^2
\]
times \(A_0\). The last three rows contribute
\[
Y=w_{03}+w_{21}-2w_{12}=(1-p)q(p-q)^2
\]
times \(B_0\). The vector of probabilities is obtained by dividing the total counted vertices by four, so
\[
4\left(\Pr(Z_S=j)-\Pr(Z_P=j)\right)_{j=1}^{4}
 =XA_0+YB_0=K(1,-4(1-q),3,-4q).
\]
This proves the full-law identity, for every parameter including the endpoints. Multiplying the four coordinates by \(j\), \(j^2\), and \(j^3\) and summing gives, respectively,
\[
\mathbb E Z_S-\mathbb E Z_P=\frac K2(1-4q),\quad
\mathbb E Z_S^2-\mathbb E Z_P^2=3K(1-4q),\quad
\mathbb E Z_S^3-\mathbb E Z_P^3=K\left(\frac{25}{2}-56q\right).
\]
In the open parameter square, \(p-q=(1-q)r>0\) and \(1-p=(1-q)(1-r)>0\), hence \(K>0\). The sign assertions follow. At \(q=1/4\), the first two moment differences vanish but the third difference equals \(-3K/2\), while the law difference is nonzero. The four-infection probability difference is \(-qK\). Finally, connected trees on up to three vertices have only one isomorphism type, while the two four-vertex types are the star and path.

## Verification

Extract the embedded \(verify.py\) file into the same directory as this document and run `python3 verify.py`. The self-contained Python standard-library checker executes 338 exact checks. It reconstructs the entire \(4\times4\) coefficient table by enumerating the 64 occupied-edge patterns; separately, it enumerates the \(2^9\) original global/local opportunity patterns using a different breadth-first connectivity routine. For a grid of rational \(g,r\) values, these two implementations agree and match the four-component law and three moment differences. All finite checks supplement the exact algebraic proof rather than substituting for the universal parameter quantifiers.

For instance \(g=1/4\), \(r=1/2\) gives \(p=5/8\), \(K=27/512\), and
\[
\left(\Pr(Z_S=j)-\Pr(Z_P=j)\right)_{j=1}^{4}
=\frac{27}{2048}(1,-3,3,-1).
\]
The two means are both \(12415/4096\), and the two second moments are both \(85631/8192\); the complete-outbreak probabilities differ by \(27/2048\).

## Relationship to prior work

Newman, Jensen and Ziff (2001) study bond percolation and epidemic sizes in a two-dimensional small-world model with shortcuts. Newman (2002) gives a broad network-percolation approach. Ball and Neal (2004) analyze local and global mixing through stochastic epidemic models, with a focus on limit theorems. Kenah and Robins (2007) establish that undirected bond percolation does **not** represent every stochastic SIR model with nondegenerate infectious periods; that distinction is respected in the present assumptions. Ball and Neal (2008) further address epidemics with casual contacts and arbitrary degree distributions in large networks.

These works motivate the two-contact-layer setting or describe general inference methods, but the inspected material does not explicitly give the exact four-site star/path full-law difference, the global-contact probability \(1/4\) reversal, or the simultaneous first-two-moment alias. General finite-graph reliability methods can in principle reproduce individual polynomials; possessing such a method is not itself evidence of an earlier statement of this classification. Related mathematical and network publications may nevertheless contain an equivalent specialization. The full Ball–Neal (2008) journal article was not available for complete comparison; its abstract and an associated 2008 scientific presentation were inspected, creating a residual priority risk.

## Limitations

This is a theorem about a four-site finite bond-percolation epidemic. It does not describe directed contacts, variable infectious periods, temporal scheduling, heterogeneous initial infection risks, network sizes above four, vaccination cost, epidemic onset in an infinite population, or empirical transmission networks. In particular, the equal mean and variance at the critical global-contact probability do not imply equal distributions. The result has not received independent mathematical auditing, and no claim of exhaustive literature priority is made.

## References

1. M. E. J. Newman, I. Jensen and R. M. Ziff, *Percolation and epidemics in a two-dimensional small world*, arXiv:cond-mat/0108542v1, first posted 2001-08-31, https://arxiv.org/abs/cond-mat/0108542.
2. M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009v1, first posted 2002-04-30, https://arxiv.org/abs/cond-mat/0205009.
3. F. Ball and P. Neal, *Poisson approximations for epidemics with two levels of mixing*, Annals of Probability 32 (2004), 1168–1200, https://doi.org/10.1214/aop/1079021475.
4. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057, first posted 2006-10-30, https://arxiv.org/abs/q-bio/0610057.
5. F. Ball and P. Neal, *Network epidemic models with two types of mixing*, Mathematical Biosciences 212 (2008), 69–87, https://doi.org/10.1016/j.mbs.2008.01.001.
