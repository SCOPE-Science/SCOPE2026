# Two universal third-cumulant sign transitions for component types in \(G(n,p)\)

## Finding
For three distinct component classes of fixed orders \(a,b,c\), the normalized mixed third cumulant has the universal sparse-graph limit
\[
\lim_{n\to\infty}\frac{n^2\operatorname{cum}(X_1,X_2,X_3)}{(\mathbb E X_1)(\mathbb E X_2)(\mathbb E X_3)}
=abc\bigl[(a+b+c)(\lambda-1)^2-1\bigr],\qquad p=\lambda/n.
\]
In particular it undergoes **two distinct sign reversals** at \(\lambda_-=1-(a+b+c)^{-1/2}\) and \(\lambda_+=1+(a+b+c)^{-1/2}\), asymptotically in the sense below.

## Assumptions and scope
Fix integers \(a,b,c\ge1\). Let \(\mathcal A_1,\mathcal A_2,\mathcal A_3\) be nonempty sets of connected simple unlabeled graphs of orders \(a,b,c\), respectively. If two orders coincide, their families must be disjoint, so no component is counted in two different random variables. In \(G(n,p)\), each of the \(\binom n2\) edges is independently present with probability \(0<p<1\). Let \(X_i\) count connected components with unlabelled type in \(\mathcal A_i\); write \(\mu_i=\mathbb E X_i>0\), \(S=a+b+c\), and define
\[
\kappa_3=\operatorname{cum}(X_1,X_2,X_3)
=\mathbb E[X_1X_2X_3]-\sum_{\{i,j,k\}=\{1,2,3\}\atop i<j}\mathbb E[X_iX_j]\mu_k+2\mu_1\mu_2\mu_3.
\]
In the summation each unordered pair appears once and \(k\) is its complement. Since the families are disjoint, products \(X_iX_j\) and \(X_1X_2X_3\) select disjoint components. We prove a finite identity whenever \(n\ge S\) and a limit at \(p=\lambda/n\) for each fixed \(\lambda>0\).

## Proof
Let \(q=1-p\). For any list of sizes \(\mathbf s=(s_1,\ldots,s_m)\) with \(\sum s_i\le n\), set
\[
R_n(\mathbf s)=\frac{\prod_{i=1}^m(n-s_i)!}{(n!)^{m-1}(n-\sum_i s_i)!}.
\]
For two distinct component families, choose ordered, disjoint vertex sets and impose their internal connected events. The external-edge conditions prohibit every edge from a chosen component to the rest. In the product of single-component probabilities, each forbidden edge between two chosen components has been counted twice instead of once. Hence
\[
\mathbb E[X_iX_j]=\mu_i\mu_j R_n(s_i,s_j)q^{-s_is_j}.
\]
Exactly the same calculation with three pairwise disjoint selected components gives
\[
\mathbb E[X_1X_2X_3]=\mu_1\mu_2\mu_3 R_n(a,b,c)q^{-(ab+ac+bc)}.
\]
These are exact for every admissible \(n\) and \(p\), irrespective of internal component shape. Consequently
\[
\frac{\kappa_3}{\mu_1\mu_2\mu_3}=R_n(a,b,c)q^{-(ab+ac+bc)}
-R_n(a,b)q^{-ab}-R_n(a,c)q^{-ac}-R_n(b,c)q^{-bc}+2.\tag{1}
\]
For each fixed positive pair of integers \(r,s\), a telescoping product gives
\[
\log R_n(r,s)=-\frac{rs}{n}-\frac{rs(r+s-1)}{2n^2}+O(n^{-3}).\tag{2}
\]
The remainder is uniform for fixed integer orders. By the factorial identity \(R_n(a,b,c)=R_n(a,b)R_n(a+b,c)\),
\[
\log R_n(a,b,c)=-\frac{ab+ac+bc}{n}
-\frac{ab(a+b-1)+ac(a+c-1)+bc(b+c-1)+2abc}{2n^2}+O(n^{-3}).\tag{3}
\]
For \(p=\lambda/n\), use \(-\log q=\lambda/n+\lambda^2/(2n^2)+O(n^{-3})\). Insert (2)--(3) into (1) and expand the exponentials through order \(n^{-2}\). Terms of order \(1\) and \(n^{-1}\) cancel. The remaining coefficient is
\[
\frac{1}{2}\left[(ab+ac+bc)^2-(ab)^2-(ac)^2-(bc)^2\right](\lambda-1)^2-abc
=abc[(a+b+c)(\lambda-1)^2-1].
\]
All expansions (and their first derivatives with respect to \(\lambda\)) are locally uniform on compact subsets of \((0,\infty)\). This proves the asserted limit, including its topology-independence.

The limiting quadratic is strictly positive outside the interval \((1-S^{-1/2},1+S^{-1/2})\) and strictly negative inside. Both roots are positive because \(S\ge3\) and are simple. By the intermediate value theorem and local uniform convergence, for all sufficiently large \(n\) equation (1) has a zero in each disjoint neighborhood of these two roots. By derivative convergence the zeros in sufficiently small fixed neighborhoods are unique there; choosing them gives \(np_n^\pm\to 1\pm S^{-1/2}\). The theorem does not exclude additional finite-\(n\) zeros elsewhere.

## Verification
The standalone `verify.py` uses only the Python standard library. It exhaustively enumerates all \(2^{15}=32{,}768\) graphs on six labeled vertices and checks the exact pairwise and triple moment formulas for the three component statistics: isolated vertices, isolated edges, and isolated three-vertex paths, at three rational edge probabilities. It also checks 40 high-precision asymptotic instances for several triples of orders and twelve finite sign tests. Execute `python verify.py` in the extracted artifact directory; success prints `VERIFY_OK`. Finite enumeration and numerical approximation are secondary checks, not proofs of the limit or of the two asymptotic zero sequences.

## Relationship to prior work
Classical random graph enumeration and factorial-moment identities furnish the component-counting foundation, which is not claimed as novel. Janson--Knuth--Łuczak--Pittel analyze joint counts of component cyclic orders near the sparse critical regime in their 1993 article; their Section 12 addresses limiting numbers of complex components with prescribed cyclic excess, rather than the normalized three-way cumulant of arbitrary fixed connected component types in \(G(n,\lambda/n)\). Krivelevich--Sudakov establish the giant-component threshold, not the third-cumulant sign profile. Bhamidi--Broutin--Sen--Wang study critical component scaling limits in more general random graph models. Pittel's 1990 tree census is a particularly relevant historical source; full text was inaccessible here, so an implicit prior derivation remains a risk. The contribution assessed is the explicit cancellation to a universal quadratic with two sign reversals and their limiting locations, not the underlying joint-moment counting formulas.

## Limitations
This is an asymptotic result for fixed component orders and fixed positive \(\lambda\); it says nothing about component orders increasing with \(n\), nor about a sign statement uniform over arbitrary \(\lambda=\lambda_n\). The cumulant is normalized by three positive (possibly small) means. No finite-\(n\) global two-zero uniqueness is proved. Inferences about independent publication priority remain provisional: the 1990 source could not be fully inspected, and general enumeration formulas may permit indirect derivations of the stated quadratic.

## References
- S. Janson, D. E. Knuth, T. Łuczak, and B. Pittel, *The Birth of the Giant Component* (initial public arXiv release 1993-10-01), https://arxiv.org/abs/math/9310236, particularly Sections 11--12.
- B. Pittel, *On Tree Census and the Giant Component in Sparse Random Graphs*, Random Structures & Algorithms **1** (1990), 311--342, https://doi.org/10.1002/rsa.3240010306.
- M. Krivelevich and B. Sudakov, *The Phase Transition in Random Graphs -- A Simple Proof* (initial public arXiv release 2012-01-31), https://arxiv.org/abs/1201.6529.
- S. Bhamidi, N. Broutin, S. Sen, and X. Wang, *Scaling Limits of Random Graph Models at Criticality: Universality and the Basin of Attraction of the Erdős--Rényi Random Graph* (initial public arXiv release 2014-11-13), https://arxiv.org/abs/1411.3417. The manuscript lists \(60C05\) as a primary mathematical subject classification.
