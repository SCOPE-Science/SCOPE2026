# Conditional joint leaf law along a marked path in a uniform Cayley tree

## Finding
Let \(T\) be uniform among the \(n^{n-2}\) labeled trees on \([n]\), for each integer \(n\ge3\). Fix two different labels \(a,b\), and let \(D\) be their graph distance. Conditional on \(D=d\), write \(X\) for the number of degree-one vertices *outside* the unique \(a\)-to-\(b\) path, and \(Y\) for the number of degree-one vertices among its two endpoints. Put \(m=n-d-1\). For every \(1\le d\le n-1\), integer \(0\le r\le m\), and \(s\in\{0,1,2\}\),

\[
\mathbb E[(X)_{\underline r}(Y)_{\underline s}\mid D=d]
=(m)_{\underline r}(2)_{\underline s}\frac{d+1-s}{d+1}
\left(\frac{n-r-s}{n}\right)^{n-d-2}.
\]

The sole exceptional interpretation is \(d=1,s=2\): **the right-hand side is defined to be zero**, because two adjacent marked endpoints cannot both be leaves when \(n\ge3\). We use \((z)_{\underline0}=1\) and \((z)_{\underline r}=z(z-1)\cdots(z-r+1)\). This identity determines the *entire joint conditional law* by its finite generating polynomial:

\[
\mathbb E[(1+u)^X(1+v)^Y\mid D=d]
=\sum_{r=0}^{m}\sum_{s=0}^2\binom mr\binom2s
\frac{d+1-s}{d+1}\left(\frac{n-r-s}{n}\right)^{n-d-2}u^rv^s,
\]

with the same zero convention for \(d=1,s=2\). All expressions are exact, including the spanning-path boundary \(d=n-1\).

In particular, if \(1\le d\le n-3\), the conditional covariance of the two disjoint leaf counts is **strictly negative**:

\[
\operatorname{Cov}(X,Y\mid D=d)
=\frac{2md}{d+1}\left[\left(1-\frac2n\right)^{n-d-2}-
\left(1-\frac1n\right)^{2(n-d-2)}\right]<0.
\]

It is zero at \(d=n-2\) and \(d=n-1\). The conditional variance of the total leaf count \(L=X+Y\) is also exact. Put \(A_1=((n-1)/n)^{n-d-2}\), \(A_2=((n-2)/n)^{n-d-2}\), and \(\mu_d=(m+2d/(d+1))A_1\). Then
\[
\operatorname{Var}(L\mid D=d)=
\left[m(m-1)+\frac{4md+2(d-1)}{d+1}\right]A_2+\mu_d-\mu_d^2.
\]
The already-known conditional **mean** \(\mu_d\) is included only to state the new variance; it is not claimed as a new result.

## Assumptions and scope
The random tree is sampled uniformly from all vertex-labeled **unrooted** Cayley trees; leaves have undirected degree one. The marked vertices are two fixed, distinct labels, not independently sampled dependent marks. Every parameter above is an integer in the displayed range. The spanning-path case has no outside vertices; for \(n=2\), both vertices are deterministically leaves and that separate trivial case is excluded from the factorial formula. No independence of \(X\) and \(Y\) is assumed.

## Proof
Fix an ordered path \(P\) with \(d\) edges, starting at \(a\) and ending at \(b\), with specified intermediate labels. A standard Cayley rooted-forest count states that, on a set of \(N\) labels, the number of spanning trees containing a fixed connected tree on \(q\) specified vertices (and no additional compulsory edges) is \(qN^{N-q-1}\). It is obtained by contracting the prescribed tree and applying the weighted matrix-tree formula (or by the rooted-forest extension bijection). Therefore the number of trees containing \(P\) is \((d+1)n^{n-d-2}\), where the usual exact count extends to \(d=n-1\), giving one tree.

Choose an ordered \(r\)-tuple of distinct labels outside \(P\), and an ordered \(s\)-tuple of different endpoints. Require them all to be leaves. If \(d=1,s=2\), this is impossible for \(n\ge3\). Otherwise delete these \(r+s\) leaves. The remaining obligatory path contains \(d+1-s\ge1\) vertices on a set of \(N=n-r-s\) labels. Its number of tree extensions is \((d+1-s)N^{N-(d+1-s)-1}\). Every deleted off-path leaf has an arbitrary parent among the \(N\) surviving vertices, independently of the other deleted leaves, supplying \(N^r\) possibilities; each removed endpoint must be reattached along its designated path edge. Consequently the number of original trees obeying these leaf requirements is precisely
\[
(d+1-s)(n-r-s)^{n-d-2}.
\]
Dividing by the path-extension count and multiplying by the numbers \((m)_{\underline r}\) and \((2)_{\underline s}\) of ordered choices proves the factorial identity. All path-label choices give the same count, hence conditioning on path *length* \(D=d\) yields the identical expression.

Expanding \((1+u)^X(1+v)^Y\) into falling factorials gives the finite generating polynomial and therefore every conditional joint probability. The stated variance follows from \((X+Y)_{\underline2}=(X)_{\underline2}+2XY+(Y)_{\underline2}\). The covariance follows using \(\mathbb E[XY]\) and \(\mathbb EX\mathbb EY\) from the cases \((r,s)=(1,1),(1,0),(0,1)\). When \(d\le n-3\), the exponent \(n-d-2\) is positive, and \(1-2/n<(1-1/n)^2\); all remaining factors are positive. For \(d=n-2\), the exponent is zero and the covariance vanishes; when \(d=n-1\), \(X=0\) almost surely.

## Verification
The accompanying standalone `verify.py` enumerates all Prüfer codes for \(3\le n\le8\), reconstructs the tree and path independently, computes the numbers of leaves on and off the marked path, and verifies exact rational conditional factorial moments, path counts, the conditional mean, and covariance-phase algebra. In the checked run, all 280391 enumerated labeled trees and 264 exact rational comparisons passed. Enumeration is **not** a proof for unbounded \(n\); the rooted-forest deletion argument above supplies that proof.

## Relationship to prior work
Aldous and Pitman (1998, Technical Report 526, §§2–3) develop random labeled trees and refined spanning-subtree/path enumerations. Bernardi and Morales (2012, arXiv:1206.0598, §§1–3) provide Cayley degree-generating functions and forest-enumeration tools. These support the standard enumerative inputs, but the inspected arguments do not state the displayed conditional joint law of the *two distinct classes of leaves* or its strictly negative conditional cross-covariance. The marginal conditional mean of total leaves at fixed path length and the joint attachment-degree generating function for vertices of a fixed subtree have been recorded previously; these are explicitly *not* presented as new. Neither marginal statement determines the joint off-path/endpoint leaf law without additional counting.

## Limitations
The theorem requires a uniform labeled tree and the undirected degree-one definition of a leaf; nonuniform vertex weights are not treated. The known marginal mean and the known conditional root-attachment distribution are not novelty claims. Earlier general tree-enumeration machinery may admit an alternative derivation, so historical priority of this exact multivariate identity remains subject to independent literature assessment. The result is a finite exact law, not a claim about asymptotic independence or arbitrary unlabeled trees.

## References
1. D. Aldous and J. Pitman, *A family of random trees with random edge lengths*, UC Berkeley Statistics Technical Report 526, catalog date June 1, 1998; public full text https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/526.pdf.
2. O. Bernardi and A. H. Morales, *Counting trees using symmetries*, arXiv:1206.0598v1, June 4, 2012, https://arxiv.org/abs/1206.0598.
3. Cayley's enumeration of labeled trees and its rooted-forest extension formula, as described in the cited primary literature.
