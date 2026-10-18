# Hidden quadratic dependence between adjacent repeats and two-step matches in uniform words

## Finding
For an iid uniform word over \(q\ge2\) letters, the adjacent-repeat count \(A\) and lag-two match count \(B\) are **exactly uncorrelated but not independent**. Their entire conditional mean is a quadratic polynomial in \(A\), and the fraction of variance of \(B\) optimally explained by \(A\) is exactly
\[\eta^2(B\mid A)=\frac{\operatorname{Var}(\mathbb E[B\mid A])}{\operatorname{Var}(B)}=\frac{2}{(q-1)(n-1)}.\]
The formula holds at every finite word length \(n\ge3\) and alphabet size \(q\ge2\), not only asymptotically. At \(q=2,n=3\), the nonlinear predictor is perfect even though the covariance is zero.

## Assumptions and scope
Fix integers \(n\ge3\), \(q\ge2\), and iid letters \(U_1,\ldots,U_n\) uniformly sampled from \(\{1,\ldots,q\}\). Set \(L=n-1\) and \(p=q^{-1}\). Define
\[A=\sum_{i=1}^{L} a_i,\qquad a_i=\mathbf1\{U_i=U_{i+1}\},\]
\[B=\sum_{i=1}^{L-1} b_i,\qquad b_i=\mathbf1\{U_i=U_{i+2}\}.\]
An adjacent-repeat is a length-two equality; a lag-two match is a length-three pattern with equal endpoints (the middle letter is unrestricted). The correlation ratio \(\eta^2(B\mid A)\) refers to explained variance by the optimal square-integrable predictor of \(B\) based on \(A\), and is well-defined since \(\operatorname{Var}(B)>0\).

## Proof
**Step 1 (marginal laws and zero covariance).** For a collection of comparisons \(\mathbf1\{U_u=U_v\}\) whose undirected comparison graph is a forest, all comparison indicators are independent Bernoulli variables with success probability \(p\). Indeed, for any subset of its edges, the simultaneous equality event has probability \(q^{-e}\), since a forest with \(e\) selected edges has exactly that many independent equality constraints; these joint success probabilities imply mutual independence. The edges \((i,i+1)\) form a path, and the edges \((i,i+2)\) form two disjoint paths. Therefore \(A\sim\operatorname{Bin}(L,p)\) and \(B\sim\operatorname{Bin}(L-1,p)\). Each individual pair \(a_i,b_j\) corresponds to two distinct edges and hence is independent, proving
\[\operatorname{Cov}(A,B)=0,\quad \mathbb EA=Lp,\quad \mathbb EB=(L-1)p.\]

**Step 2 (local conditional regression).** For each \(i=1,\ldots,L-1\), condition on the *entire* adjacent-indicator vector \((a_1,\ldots,a_L)\). Since the word is uniform, successive choices after each letter are independently of type equal (probability \(1/q\)) or different (probability \((q-1)/q\)); conditional on a different choice, its new letter is uniform among the other \(q-1\) letters. Thus
\[\mathbb E[b_i\mid a_1,\ldots,a_L]=\begin{cases}1,&a_i=a_{i+1}=1,\\\frac1{q-1},&a_i=a_{i+1}=0,\\0,&a_i\ne a_{i+1}.\end{cases}\]
The \(a_i\) are iid Bernoulli \(p\); conditional on \(A=k\), their locations are a uniformly chosen \(k\)-subset of the \(L\) positions. Hence the probabilities that a specified neighboring pair is \((1,1)\) and \((0,0)\) are respectively
\[\frac{k(k-1)}{L(L-1)},\qquad\frac{(L-k)(L-k-1)}{L(L-1)}.\]
Summing the \(L-1\) local conditional expectations gives, for **every** \(k=0,1,\ldots,L\),
\[\boxed{\mathbb E[B\mid A=k]=\frac{k(k-1)+(L-k)(L-k-1)/(q-1)}{L}}.\]

**Step 3 (orthogonal second-order projection).** Write
\[Q_2(k)=k(k-1)-2(L-1)pk+L(L-1)p^2.\]
Expanding the previous expression gives the identity
\[\mathbb E[B\mid A]-(L-1)p=\frac{Q_2(A)}{L(1-p)}.\]
With \(Z_i=a_i-p\), the same polynomial has the exact representation
\[Q_2(A)=2\sum_{1\le i<j\le L}Z_iZ_j.\]
These products are mutually orthogonal in \(L^2\): terms on different unordered index pairs have zero covariance by independence and centering, including pairs sharing one index. Consequently,
\[\operatorname{Var}(Q_2(A))=4\binom{L}{2}p^2(1-p)^2=2L(L-1)p^2(1-p)^2.\]
Since \(B\sim\operatorname{Bin}(L-1,p)\),
\[\operatorname{Var}(\mathbb E[B\mid A])=\frac{2(L-1)}{L}p^2,\qquad \operatorname{Var}(B)=(L-1)p(1-p).\]
Their ratio is
\[\boxed{\eta^2(B\mid A)=\frac{2p}{L(1-p)}=\frac{2}{(q-1)(n-1)}}.\]
This is strictly positive at every allowed parameter. By the orthogonal-projection property of conditional expectation, this ratio is the largest explained-variance fraction among all square-integrable predictors based on \(A\). The ratio is at most one, with equality precisely at \((q,L)=(2,2)\); in all cases its strict positivity proves nonindependence. When \(q=2,n=3\), \(B=1\) if and only if \(A\in\{0,2\}\), demonstrating exact nonlinear predictability with zero covariance.

**Step 4 (a detecting mixed third moment).** Expanding \((A-Lp)^2(B-(L-1)p)\), every expectation of a product of three centered edge indicators vanishes except those involving the three edges of the triangle \((i,i+1),(i+1,i+2),(i,i+2)\). Each of the \(L-1\) triangles contributes two ordered terms from the square, and
\[\mathbb E[(a_i-p)(a_{i+1}-p)(b_i-p)]=p^2-p^3=p^2(1-p).\]
Therefore
\[\boxed{\mathbb E[(A-\mathbb EA)^2(B-\mathbb EB)]=2(n-2)p^2(1-p)>0}.\]
This independent witness of nonlinear dependence also shows that the Krawtchouk projection has a genuinely nonzero coefficient.

## Verification
The accompanying standalone `verify.py` enumerates complete word spaces for 18 \((q,n)\) pairs with \(2\le q\le5\), independently tallies exact joint distributions, and checks the binomial marginals, covariance cancellation, conditional expectation at every attainable count, the orthogonal-polynomial formula, the exact explained-variance ratio and the centered third mixed moment using rational arithmetic. It passed all included identities. These finite checks supplement, but cannot replace, the proof for arbitrary \(q,n\).

## Relationship to prior work
Mansour, Rastegar and Roitershtein (arXiv:1905.05646v1, 2019) investigate occurrence counts of word and permutation patterns, including limit theorems for their marginal random counts. Their pattern relation is generally subsequence order-isomorphism, rather than the paired local equality statistics considered here. Louchard, Schachinger and Ward (arXiv:2203.14773v1, 2022) study the number of **distinct types** of adjacent pairs in geometrically distributed words, with probabilistic and generating-function moment analysis. Unlike those questions, the present finite-size theorem concerns the joint conditional expectation of *total* adjacent equalities and lag-two equalities, together with its exact nonlinear explained-variance constant. No claim is made that the binomial forest property or the separate word-pattern models are new.

## Limitations
This theorem assumes iid **uniform** letters, not an arbitrary alphabet distribution, dependent letters or cyclic boundary conditions. It computes the conditional mean and one dependence coefficient, not the complete joint distribution of \((A,B)\). The correlation-ratio asymptotic \(2/[(q-1)(n-1)]\to0\) does not assert the random variables are independent at finite size or quantify total-variation distance. Earlier combinatorial probability or pattern-enumeration work could contain an equivalent implicit identity; historical priority has not been independently established.

## References
1. T. Mansour, R. Rastegar and A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, arXiv:1905.05646v1 (first public version, 2019-05-14), https://arxiv.org/html/1905.05646v1.
2. G. Louchard, W. Schachinger and M. D. Ward, *The number of distinct adjacent pairs in geometrically distributed words: a probabilistic and combinatorial analysis*, arXiv:2203.14773v1 (first public version, 2022-03-28), https://arxiv.org/abs/2203.14773.
