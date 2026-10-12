# A complete leader-property classification for identical product marginals
## Finding
Let \(\mu\) be a probability law on \(\mathbb R\), let \(d\ge2\), and let
\[
Z_i=(X_{i1},\ldots,X_{id}),\qquad i=1,2,\ldots,
\]
be i.i.d. with law \(\mu^{\otimes d}\). For each \(n\ge1\), let \(a_n\) be the probability that the sample \(Z_1,\ldots,Z_n\) contains a leader, meaning one sampled vector that is coordinatewise at least every other sampled vector.

Let \(s=\operatorname{ess\,sup}\mu\), with \(s=+\infty\) allowed. Then \(\mu^{\otimes d}\) has the leader property
\[
\liminf_{n\to\infty}a_n>0
\]
if and only if \(s<\infty\) and \(p:=\Pr\{X=s\}>0\). In the latter case,
\[
a_n\longrightarrow1.
\]
If \(s=+\infty\), or \(s<\infty\) but \(\Pr\{X=s\}=0\), then
\[
\liminf_{n\to\infty}a_n=0.
\]
In particular, for every \(d\ge2\), if \(\mu\) has unbounded infinite support then the identical-coordinate product law \(\mu^{\otimes d}\) does not have the leader property. This proves the common-marginal subcase of the infinite-value product question in Răducan--Rădulescu--Rădulescu--Zbăganu.

## Assumptions and scope
Coordinates are mutually independent and identically distributed with the same arbitrary one-dimensional law \(\mu\); no continuity, discreteness, moment, or regular-variation assumption is imposed. Ties are allowed. The theorem classifies the leader property for the symmetric product class \(\mu^{\otimes d}\), for every fixed \(d\ge2\). It does not classify heterogeneous products \(\mu_1\otimes\cdots\otimes\mu_d\).

The phrase “atom at the essential supremum” means that \(s<\infty\) and \(\Pr\{X=s\}>0\). If \(s<\infty\) but there is no atom at \(s\), the support may still contain \(s\) as a topological endpoint; the theorem treats this in the no-leader branch.

## Proof
Suppose first that \(s<\infty\) and \(p=\Pr\{X=s\}>0\). A sampled vector equal to \((s,\ldots,s)\) is automatically a leader. Since one observation equals this vector with probability \(p^d\),
\[
a_n\ge 1-(1-p^d)^n\longrightarrow1.
\]
Thus the leader property holds, indeed in the strong form \(a_n\to1\).

Now suppose there is no atom at the essential supremum. Let
\[
F(x)=\Pr\{X\le x\}.
\]
For one coordinate and one fixed observation index, write
\[
u_n=\Pr\{X_1\ge X_j\text{ for every }2\le j\le n\}.
\]
Conditioning on \(X_1\) gives the exact identity
\[
u_n=\mathbb E\!\left[F(X_1)^{n-1}\right].
\]
For each sufficiently large integer \(j\), choose a cutoff \(b_j<s\) when \(s<\infty\), or any increasing cutoff when \(s=+\infty\), such that
\[
t_j:=\Pr\{X>b_j\}>0,\qquad t_j\downarrow0.
\]
Such a sequence exists precisely because there is no terminal atom. Splitting according to \(X_1\le b_j\) or \(X_1>b_j\),
\[
u_n\le (1-t_j)^{n-1}+t_j.
\]
Set
\[
n_j=\left\lceil\frac{\log(1/t_j)}{t_j}\right\rceil+1.
\]
Then
\[
(1-t_j)^{n_j-1}\le e^{-t_j(n_j-1)}\le t_j,
\]
so
\[
u_{n_j}\le2t_j.
\]

For a fixed sample index \(i\), being a leader means being a sample maximum in every one of the \(d\) coordinate samples. Independence of the coordinates therefore gives probability \(u_n^d\) for this event. A union bound over the \(n\) sample indices yields
\[
a_n\le n u_n^d.
\]
Consequently,
\[
a_{n_j}
\le 2^d n_j t_j^d
\le 2^d\!\left(t_j^{d-1}\log(1/t_j)+2t_j^d\right),
\]
for all sufficiently large \(j\). Because \(d\ge2\), the right-hand side tends to zero. Hence
\[
\liminf_{n\to\infty}a_n=0,
\]
which excludes the leader property. This completes both directions.

## Verification
Every inequality in the proof is uniform over the one-dimensional law. The only distribution-specific quantity is the tail probability \(t_j\). The exact fixed-index maximum probability \(u_n=\mathbb E[F(X)^{n-1}]\) correctly includes ties. The bound \(a_n\le n u_n^d\) is a union bound and therefore requires no independence between different candidate leader indices; only coordinate independence for each fixed index is used.

The endpoint branch was checked separately: if a terminal atom of mass \(p>0\) exists, occurrence of \((s,\ldots,s)\) alone forces \(a_n\to1\). In the opposite branch, \(t^{d-1}\log(1/t)\to0\) for every \(d\ge2\), which proves the required subsequential decay without any unproved regularity assumption.

## Relationship to prior work
Răducan, Rădulescu, Rădulescu, and Zbăganu introduced the leader property and explicitly asked whether a product of independent components, each having infinitely many values, can possess that property. Their paper proves several sufficient conditions and the continuous-product case, but does not give the classification above. Its publisher metadata lists MSC 60E15 first, followed by 60B12 and 62H05.

A prior structural observation for two-dimensional product samples expresses leader existence through intersection of the two marginal maximizing-index sets and reduces asymptotic behavior to maximum multiplicities. That criterion does not itself decide the common-marginal infinite-support case. The tail-cutoff argument above supplies the missing uniform subsequence and works in every dimension \(d\ge2\).

The same authors' 2022 quasi-unidimensional paper studies dependent coordinates generated from one latent variable. Their 2025 paper studies samples lying on graphs of functions and explicitly restricts attention to that setting. Neither inspected follow-up states the identical-product classification above.

## Limitations
The theorem does not resolve the full heterogeneous-product question \(\mu_1\otimes\cdots\otimes\mu_d\), where different marginal maximum multiplicities can interact on different scales. It gives no rate for \(a_n\) away from the selected subsequence when there is no terminal atom; indeed earlier examples show that \(a_n\) need not converge for lacunary discrete laws. An equivalent elementary argument may exist under terminology concerning common sample maximizers rather than “leaders”; targeted searches did not locate one.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, *On the Probability of Finding Extremes in a Random Set*, Mathematics 10 (2022), 1623. DOI: 10.3390/math10101623. Published 10 May 2022.
2. A. M. Răducan and G. Zbăganu, *The Leader Property in Quasi Unidimensional Cases*, Mathematics 10 (2022), 4199. DOI: 10.3390/math10224199.
3. G. Zbăganu, A. M. Răducan, and M. Rădulescu, *Computing Probabilities of Finding Extremes in a Random Set*, Mathematics 13 (2025), 3074. DOI: 10.3390/math13193074.
