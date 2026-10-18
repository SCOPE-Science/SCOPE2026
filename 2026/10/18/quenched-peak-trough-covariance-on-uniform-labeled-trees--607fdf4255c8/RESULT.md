# Quenched peak–trough covariance on uniform labeled trees

## Finding
Let \(T_n\) be a uniformly random labeled tree on \(\{1,\ldots,n\}\), independently decorated with i.i.d. observations having a common continuous distribution. Write \(A_n\) and \(B_n\) for the numbers of vertices whose observations are, respectively, strictly larger and strictly smaller than the observations at *every adjacent vertex*. Leaves qualify. Let
\[
Q_n=\mathbb E_{T_n}\!\left[\operatorname{Cov}(A_n,B_n\mid T_n)\right].
\]
The expectation outside the covariance is over the random tree only; the covariance inside is over the independently resampled vertex observations on that fixed tree. For every \(n\ge4\), the finite-sample formula below determines \(Q_n\) exactly. Moreover,
\[
\boxed{\lim_{n\to\infty}\frac{Q_n}{n}=c,\qquad -0.03934225<c<-0.03934110.}
\]
In particular, the tree-averaged *conditional* peak–trough covariance is strictly negative for all sufficiently large \(n\). The behavior genuinely depends on the geometry: on the path \(P_n\), for every \(n\ge4\),
\[
\boxed{\operatorname{Cov}(A_n,B_n\mid T_n=P_n)=\frac{8n-37}{180},}
\]
which is positive for all \(n\ge5\). This is **not** a claim about the unconditional covariance over both trees and vertex observations.

Define, for positive integers \(a,b\),
\[
\begin{aligned}
H_1(a,b)&=\frac1{ab}-\frac{(a-1)!(b-1)!}{(a+b)!}-\frac1{(a+1)(b+1)},\\
H_2(a,b)&=\frac{1-\frac1{a+1}-\frac1{b+1}+\frac{a!b!}{(a+b+1)!}}{ab}-\frac1{(a+1)(b+1)}.
\end{aligned}
\]
For each \(n\ge4\), let \(Z\sim\operatorname{Bin}(n-2,1/n)\). Let \((I_v,I_w)\) be uniformly distributed over \(\{(1,0),(0,1)\}\), and let \((N_v,N_w)\) count visits to two distinguished labels among \(n-3\) independent draws from \(\{1,\ldots,n\}\). Let \((J_v,J_w)\) take \((1,0),(0,1),(0,0)\), each with probability \(1/3\), and let \((M_v,M_w)\) count visits to two distinguished labels among \(n-4\) independent uniform draws. Each pair of random ingredients within a term is independent. Then
\[
\boxed{Q_n=-n\mathbb E\frac1{(2+Z)^2}
 +2(n-1)\mathbb E H_1(1+I_v+N_v,1+I_w+N_w)
 +\frac{3(n-1)(n-2)}{n}\mathbb E H_2(1+J_v+M_v,1+J_w+M_w).}
\]
All expectations are finite, elementary binomial/multinomial sums.

For an explicit limiting constant let \(P_1,P_2\) be independent \(\operatorname{Pois}(1)\) variables, \(I_v+I_w=1\) with the same fair distribution as above, and \((J_v,J_w)\) have the same three-point distribution as above, independently of the Poisson variables. Then
\[
\boxed{c=-\mathbb E\frac1{(2+P_1)^2}
 +2\mathbb EH_1(1+I_v+P_1,1+I_w+P_2)
 +3\mathbb EH_2(1+J_v+P_1,1+J_w+P_2).}
\]

## Assumptions and scope
The tree is uniform among the \(n^{n-2}\) labeled trees; the observations are independent of the tree and i.i.d. with any atomless common law. Both endpoints of an edge count as potential extrema, as do all leaves. The result concerns the expected covariance *conditional on the random tree*. It is different from \(\operatorname{Cov}(A_n,B_n)\), since the law of total covariance adds \(\operatorname{Var}_{T_n}(\mathbb E[A_n\mid T_n])\). The exact tree-average formula holds for \(n\ge4\); the limit holds as \(n\to\infty\). No claim is made that \(Q_n<0\) for every finite \(n\), nor that the empirical conditional covariance concentrates around its mean.

## Proof
**Local indicator decomposition.** The probability integral transform reduces the observations to i.i.d. uniform variables \(U_v\) on \((0,1)\). At a vertex of degree \(a\), the probability of being a strict local maximum or strict local minimum is \(1/(a+1)\). Since a vertex of a nontrivial tree cannot be both, its same-site peak/minimum indicator covariance is \(-1/(a+1)^2\).

For distinct adjacent vertices \(v,w\) of degrees \(a,b\), the event that \(v\) is a maximum and \(w\) a minimum has probability
\[
\int_0^1 x^{a-1}\int_0^x(1-y)^{b-1}\,dy\,dx
=\frac1{ab}-\frac{(a-1)!(b-1)!}{(a+b)!}.
\]
Subtracting the product of marginals gives \(H_1(a,b)\). If \(v,w\) are at graph distance two, they have one common neighbor and otherwise disjoint closed neighborhoods (because the graph is a tree). Conditioning on the common neighbor's value \(t\) gives joint probability
\[
\frac1{ab}\int_0^1(1-t^a)(1-(1-t)^b)\,dt
=\frac{1-1/(a+1)-1/(b+1)+a!b!/(a+b+1)!}{ab},
\]
so their covariance is \(H_2(a,b)\). At distance at least three the disjoint closed neighborhoods make the indicators independent. Hence for every fixed tree \(T\) with degree sequence \(d_v\),
\[
\operatorname{Cov}(A_n,B_n\mid T)
=-\sum_v\frac1{(d_v+1)^2}
 +\sum_{(v,w):\operatorname{dist}(v,w)=1}H_1(d_v,d_w)
 +\sum_{(v,w):\operatorname{dist}(v,w)=2}H_2(d_v,d_w),
\]
where both pair sums run over ordered distinct vertices.

**Tree averaging.** The weighted Cayley spanning-tree identity, obtained by contracting any fixed forest \(F\), is
\[
\sum_{T\supset F}\prod_i x_i^{d_T(i)}
=\left(\prod_{\{i,j\}\in F}x_ix_j\right)
 \left(\prod_{C\in\operatorname{comp}(F)}\sum_{i\in C}x_i\right)
 \left(\sum_i x_i\right)^{|\operatorname{comp}(F)|-2}.
\]
It follows from the weighted Cayley identity \(\sum_T\prod_i x_i^{d_T(i)}=(\prod_i x_i)(\sum_i x_i)^{n-2}\) on the contracted complete graph with component weights \(\sum_{i\in C}x_i\). With no forced edges, the degree of one specified vertex is \(1+\operatorname{Bin}(n-2,1/n)\). With a specified edge forced into the tree, its probability is \(2/n\), and the two endpoint degrees have the law \(1+I_v+N_v\), \(1+I_w+N_w\) stated above. With a specified length-two path forced, its probability is \(3/n^2\), and its endpoint degrees have law \(1+J_v+M_v\), \(1+J_w+M_w\). The last representation uses \(n\ge4\).

There are \(n(n-1)\) ordered candidate adjacent pairs and \(n(n-1)(n-2)\) ordered candidate length-two paths. Multiplying their incidence probabilities and the local covariance terms proves the displayed exact finite-sample formula for \(Q_n\).

**Limit and strict sign.** The binomial variable and the two counts in each multinomial allocation converge to independent unit-mean Poisson variables, while the bounded functions \(H_1,H_2\) permit passage of expectations to the limit. Division by \(n\) proves the formula for \(c\).

For a rigorous sign certificate, truncate every Poisson variable at \(K=10\) and condition it to be at most \(K\). Put \(E_K=\sum_{j=0}^K1/j!\); the truncated law has rational probabilities \(1/(j!E_K)\). Evaluate the resulting rational expression \(c_K\) by the provided `check.py`. Its Poisson-tail mass satisfies \(\delta\le T_K=(K+2)/((K+1)(K+1)!)\). Total variation between a Poisson variable and its truncation is \(\delta\), and that of two independent variables is at most \(2\delta\). Because \(0\le1/(2+P)^2\le1/4\) and \(|H_1|,|H_2|\le1\), \(|c-c_K|\le21T_K\). Exact rational evaluation gives \(-0.03934225<c<-0.03934110<0\).

**Path comparison.** For \(P_n\), two vertices have degree one and the others degree two. Substitution in the fixed-tree covariance identity, classifying the finitely many endpoint-adjacent and interior pairs at distance one or two, simplifies to \((8n-37)/180\) for every \(n\ge4\).

## Verification
The self-contained `check.py` uses `fractions.Fraction`, permutation enumeration and Prüfer sequences. It checks local indicator covariances against brute-force labelings for every labeled tree on up to five vertices and selected six-vertex trees. It checks the Cayley averaging formula by enumerating all labeled trees through six vertices and computes an exact rational interval certifying the negative limiting constant. It also checks finite-size values \(Q_4=-31/192\), \(Q_5=-1537/7500\), and \(Q_6=-3193/12960\). The last two identities are independent consistency checks of the exact formula; finite enumeration is not a proof of the limit.

Run: `python3 check.py` (Python standard library).

## Relationship to prior work
Majumdar and Martin (2006) analyze local-minimum counts in i.i.d. vertex landscapes on fixed lattices and regular branching trees; their discussion of local moment calculations motivates the present joint-extrema question. Their "Cayley tree" in the relevant section is a fixed-branching tree, not a uniformly sampled labeled tree on \(n\) vertices. Clark (2005) counts rooted *three-vertex path* extrema in uniform labeled trees, a different observable. Burdzy and Pal (2016) study random graph labelings conditioned on having one or two peaks. Diaz-Lopez and collaborators (2017) enumerate peak sets on fixed graphs, excluding degree-one peaks in their convention; the present observable counts leaves and involves both minima and maxima. None of their inspected stated results gives this averaged conditional peak–trough covariance and its negative linear coefficient. Inference from generic enumeration algorithms remains a historical-priority risk.

## Limitations
The theorem concerns disorder-averaged *quenched covariance*, not the unconditional covariance or a limiting distribution. The limiting constant is given by an absolutely convergent Poisson series and a certified rational interval, not a proposed elementary closed form. The signed local decomposition on a fixed tree is elementary once the right neighborhoods are isolated; the nontrivial averaging uses the conditioned weighted-tree enumeration. Prior implicit derivations in broader generating-function work cannot be excluded. No external independent scientific audit has been performed.

## References
1. S. N. Majumdar and O. C. Martin, *The Statistics of the Number of Minima in a Random Energy Landscape*, arXiv:cond-mat/0609735 (first posted 2006-09-28), especially Sections I–II and IV. https://arxiv.org/abs/cond-mat/0609735
2. L. Clark, *Local extrema in random trees*, International Journal of Mathematics and Mathematical Sciences 2005, 3867–3882, DOI:10.1155/IJMMS.2005.3867. https://doi.org/10.1155/IJMMS.2005.3867
3. K. Burdzy and S. Pal, *Twin peaks*, arXiv:1606.08025 (2016), especially Section 6. https://arxiv.org/abs/1606.08025
4. A. Diaz-Lopez et al., *Counting peaks on graphs*, arXiv:1708.08493 (2017). https://arxiv.org/abs/1708.08493
