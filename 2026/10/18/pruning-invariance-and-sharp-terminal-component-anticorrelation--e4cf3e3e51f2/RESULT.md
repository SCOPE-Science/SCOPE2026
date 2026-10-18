# Pruning invariance and sharp terminal–component anticorrelation in random mappings

## Finding
Let \(f:[n]\to[n]\) be a uniformly random mapping, with independently uniform images, and let \(n\ge2\). Define \(L_n\) as the number of *terminal vertices* (indegree zero), \(C_n\) as the number of weakly connected components, and \(C_{n,k}\) as the number of directed cycles of length \(k\). Every component contains exactly one directed cycle. For a random mapping on \(m\) vertices, use the corresponding \(C_m\) and \(C_{m,k}\).

**Pruning identity.** For every \(0\le r\le n-1\) and every real function \(h\) on the integers,
\[
\mathbb E[(L_n)_r h(C_n)]
=(n)_r\left(\frac{n-r}{n}\right)^n\mathbb E[h(C_{n-r})],
\]
where \((x)_r=x(x-1)\cdots(x-r+1)\), with \((x)_0=1\). The same identity holds with \(h\) an arbitrary function of the entire vector of cycle-length counts. Equivalently, writing \(G_m(z)=\mathbb E[z^{C_m}]\), the entire joint probability generating polynomial is
\[
\mathbb E[t^{L_n}z^{C_n}]
=\sum_{r=0}^{n-1}\binom nr\left(\frac{n-r}{n}\right)^n(t-1)^rG_{n-r}(z).
\]

**Dependence and limits.** Set
\[
a_m=\sum_{k=1}^{m}\frac{(m)_k}{k m^k},\qquad a_{m,k}=\begin{cases}(m)_k/(k m^k),&k\le m,\\0,&k>m.\end{cases}
\]
Then, for every \(n\ge2\),
\[
\operatorname{Cov}(L_n,C_n)
=n\left(1-\frac1n\right)^n(a_{n-1}-a_n)<0,
\quad
\lim_{n\to\infty}\operatorname{Cov}(L_n,C_n)=-\frac1{2e}.
\]
For every \(1\le k\le n\),
\[
\operatorname{Cov}(L_n,C_{n,k})
=n\left(1-\frac1n\right)^n(a_{n-1,k}-a_{n,k}).
\]
The last covariance is exactly zero for \(k=1\) and strictly negative for every \(2\le k\le n\). More strongly, for every nondecreasing real \(h\), and \(1\le r\le n-1\),
\[
\operatorname{Cov}((L_n)_r,h(C_n))\le0.
\]
This last inequality does not assert general negative association between all increasing functions of \(L_n\) and \(C_n\).

## Assumptions and scope
The model includes loops and permits multiple vertices to map to the same image. All \(n^n\) maps have equal probability. Terminal means indegree zero, including absence of a loop; weak components are those of the underlying unoriented functional graph. The generating-polynomial identity and stochastic inequality hold at each finite \(n\), without a limit or an independence assumption beyond the independently chosen images. The length-specific strict inequalities require \(k\ge2\); the zero for fixed points, \(k=1\), is exact. The asymptotic constant concerns the *unstandardized* covariance.

## Proof
**1. Exact pruning and generating polynomial.** Fix an ordered selection of \(r\) distinct vertices \(S\). Let \(E_S\) be the event that none of the \(n\) arrows lands in \(S\). Then \(\Pr(E_S)=((n-r)/n)^n\). Given \(E_S\), all arrow images are independent uniform points of the complement \(T=[n]\setminus S\). Thus \(f|_T:T\to T\) is a uniform random mapping on \(n-r\) vertices. Each vertex of \(S\) points into \(T\) and cannot be in a cycle, so the cycles and weak components of \(f\) are exactly those of \(f|_T\). Summing \(\mathbf1_{E_S}h(C_n)\) over ordered distinct choices of \(S\) proves the factorial identity. Expand \(t^{L_n}=(1+(t-1))^{L_n}=\sum_r (L_n)_r(t-1)^r/r!\). Since \(L_n\le n-1\), the stated exact joint probability generating polynomial follows. The argument preserves the *complete multiset of directed cycle lengths*, establishing the vector version as well.

**2. Cycle moments and strict finite signs.** For each fixed ordered \(k\)-tuple of distinct vertices, there is exactly one specified cyclic orientation of its \(k\) arcs, and its probability is \(n^{-k}\). Correcting for the \(k\) possible roots of a cycle gives
\[\mathbb E C_{n,k}=\frac{(n)_k}{k n^k}=a_{n,k}.\]
Summing over lengths gives \(\mathbb E C_n=a_n\). Taking \(r=1\) in the pruning identity and subtracting the product of means gives the displayed covariance formulas. For \(2\le k\le n-1\), each factor \(1-j/m\), with \(1\le j\le k-1\), increases strictly with \(m\), so \(a_{n,k}>a_{n-1,k}\). For \(k=n\), \(a_{n-1,n}=0<a_{n,n}\). For \(k=1\), both expectations equal one. Therefore every nontrivial cycle-length contribution is negative and the full covariance is strictly negative.

**3. Monotonicity under size and the stronger inequality.** Let \(K_m\) be the number of cyclic vertices of a uniform random mapping on \(m\) points. Choose the \(j\) cyclic vertices, place one of \(j!\) permutations on them, and attach the other \(m-j\) vertices as a directed forest flowing into these specified roots. The classical labeled rooted-forest count is \(j m^{m-j-1}\), so exactly \(inom mj j!\,j m^{m-j-1}\) of the \(m^m\) mappings have \(j\) cyclic vertices. Consequently,
\[
\Pr(K_m=j)=\frac{j}{m}\frac{(m)_j}{m^j},\qquad 1\le j\le m.
\]
Put \(A_{m,j}=(m)_j/m^j\) and \(A_{m,m+1}=0\). Since \(A_{m,j}-A_{m,j+1}=(j/m)A_{m,j}\), summing the preceding mass identity yields
\[\Pr(K_m\ge j)=A_{m,j}=\prod_{\ell=0}^{j-1}(1-\ell/m).\]
For fixed \(j\), these survival probabilities are nondecreasing in \(m\), so one can couple the \(K_m\)'s to be nondecreasing. Conditional on \(K_m=j\), the restriction to the cyclic set is a uniform permutation of \(j\) elements. Its cycle count admits a coupling as \(\sum_{i=1}^{j}B_i\), where the independent indicators satisfy \(\Pr(B_i=1)=1/i\); the sums increase pointwise with \(j\). Composing the two couplings shows that \(C_m\) increases in stochastic order as \(m\) increases. Therefore \(\mathbb E h(C_{n-r})\le\mathbb E h(C_n)\) for every nondecreasing \(h\). The factorial-pruning identity then yields
\[
\operatorname{Cov}((L_n)_r,h(C_n))
=\mathbb E(L_n)_r\left(\mathbb E h(C_{n-r})-\mathbb E h(C_n)\right)\le0.
\]

**4. Sharp constant.** Write \(A_{n,k}=(n)_k/n^k\), with \(A_{n,n+1}=0\), and \(b_n=a_n-a_{n-1}>0\). For \(1\le k<n\), define
\[
R_{n,k}=\frac{A_{n-1,k}}{A_{n,k}}
=\left(1-\frac{k}{n}\right)\left(1-\frac1n\right)^{-k},\qquad R_{n,n}=0.
\]
Then
\[
b_n=\sum_{k=2}^n\frac{A_{n,k}}{k}(1-R_{n,k}).\]
Fix \(x>0\), and let \(k/\sqrt n\to x\). Taylor expansion of the displayed products gives
\[
A_{n,k}\longrightarrow e^{-x^2/2},\qquad n(1-R_{n,k})\longrightarrow x^2/2.
\]
For \(2\le k\le n/2\), \(A_{n,k}\le\exp(-k(k-1)/(2n))\) and
\[
0\le1-R_{n,k}\le-\log R_{n,k}
=\sum_{j=1}^{k-1}\log\left(1+\frac{j}{n(n-1-j)}\right)
\le\frac{4k^2}{n^2}
\]
for all sufficiently large \(n\). These bounds dominate the rescaled sum by a constant multiple of \(x e^{-x^2/4}\), and the complementary range \(k>n/2\) contributes at most \(n\sum_{k>n/2}A_{n,k}/k=O(n\exp(-n/9))\). Dominated Riemann-sum convergence therefore gives
\[
\lim_{n\to\infty}n b_n
=\int_0^\infty\frac{x}{2}e^{-x^2/2}\,dx=\frac12.
\]
Finally \(\operatorname{Cov}(L_n,C_n)=-n(1-1/n)^n b_n\) and \((1-1/n)^n\to e^{-1}\), proving the stated \(-1/(2e)\) constant.

## Verification
The supplied standalone standard-library script `verify.py` exhaustively enumerates every mapping for sizes \(1\le n\le6\), including 46,656 mappings at size six. It checks the factorial-pruning identity for all feasible factorial orders and all component-count values, both covariance formulas, the cyclic-point survival law, and mean monotonicity through size 500 using exact rational arithmetic. It also checks a numerical instance of the limiting covariance at size 10,000; this is diagnostic only, not a proof of the limit. The universal conclusions follow from the four analytical steps above.

## Relationship to prior work
Flajolet and Odlyzko's *Random Mapping Statistics* (1990), Section 3.1, explicitly studies the marginal expectations of both terminal nodes and connected components via generating functions, and its Section 3.3 studies cycle-length marginals. These established marginal results and their counting framework are not asserted to be new. Finch's *Components and Cycles of Random Mappings* (initial preprint May 11, 2022) and Mutafchiev and Finch's *On the Deepest Cycle of a Random Mapping* (initial preprint January 31, 2023) treat component and cycle statistics. The present specific contribution is an exact **joint** terminal/component law obtained by deleting designated indegree-zero vertices, together with all-parameter negative factorial regression, the special zero fixed-point covariance, and a sharp unstandardized covariance limit. The papers inspected did not state this combined conclusion; its historical priority is not independently certified.

## Limitations
The sharp constant is for uniformly random *unrestricted* mappings and cannot be transferred without proof to random mappings with constrained indegrees or prohibited loops. The monotone-coupling conclusion concerns the distribution of component counts under size enlargement and factorial functions of terminal counts; it does not establish complete negative dependence between arbitrary increasing functions of the two counts. A general earlier marked generating-function identity, possibly in older random-mapping literature, may implicitly contain this result. The cited published sources were examined for statement-level coverage, but comprehensive historical exclusion is not possible from the inspected material. Independent verification of originality and the proof has not been performed.

## References
1. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT '89, Lecture Notes in Computer Science 434, Springer (1990), Section 3, available at https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf.
2. S. Finch, *Components and Cycles of Random Mappings*, arXiv:2205.05579 (initial version May 11, 2022), https://arxiv.org/abs/2205.05579.
3. L. Mutafchiev and S. Finch, *On the Deepest Cycle of a Random Mapping*, arXiv:2301.13829 (initial version January 31, 2023), https://arxiv.org/abs/2301.13829.
4. D. Stark, *The Component Counts of Random Functions*, Discrete Mathematics 345 (2022), 112977. Comparison limited to accessible abstract.
