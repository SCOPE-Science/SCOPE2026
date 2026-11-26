# The five-vertex fluctuation shared by directed cycles in fair tournaments

## Finding

Orient the edges of the labeled complete graph on \(n\) vertices independently and fairly. Let \(C_{k,n}\) count directed simple cycles of length \(k\), identifying cyclic rotations but not reversal, and let \(T_n=C_{3,n}\). For each fixed \(k\ge5\),
\[
1-\operatorname{Corr}(T_n,C_{k,n})=\frac{1}{2n^2}+O_k(n^{-3}).
\]
For any two fixed lengths \(k,\ell\ge5\), the faster bound
\[
1-\operatorname{Corr}(C_{k,n},C_{\ell,n})=O_{k,\ell}(n^{-3})
\]
holds. The extra cancellation occurs because the same signed sum of four-edge paths on five vertices is the entire next fluctuation shared by these cycle counts after division by their triangle coefficients. More precisely, define \(a_{k,n}=(n-3)_{\underline{k-3}}/2^{k-3}\), where \((m)_{\underline j}\) is the falling factorial. Write \(Y_{uv}=1\) for an arc \(u\to v\) and \(-1\) otherwise. Let
\[
W_{5,n}=\sum_{p}\prod_{i=0}^3Y_{v_i v_{i+1}},
\]
where the sum is over undirected four-edge paths \(p=(v_0,\ldots,v_4)\) on distinct vertices, each taken once modulo reversal. Then for all \(n\ge k\ge5\),
\[
\frac{C_{k,n}-\mathbb EC_{k,n}}{a_{k,n}}
=T_n-\mathbb ET_n+\frac{W_{5,n}}{4(n-3)(n-4)}+U_{k,n}.
\]
The centered residual \(U_{k,n}\) is orthogonal in \(L^2\) to both displayed terms, vanishes for \(k=5\), and has variance \(O_k(1)\) as \(n\to\infty\). In particular, for every \(n\ge5\),
\[
\operatorname{Corr}(T_n,C_{5,n})=\left(1+\frac{1}{(n-3)(n-4)}\right)^{-1/2}.
\]

## Assumptions and scope

The cycle count is non-induced: edges outside the selected cyclic word are unrestricted. The exact identities apply over the full stated range of \(n\) and \(k\); the variance and asymptotic correlation estimates keep lengths fixed. No joint limiting law or growth-in-length estimate is asserted.

## Proof

Use the independent Rademacher signs \(Y_{uv}\) for \(u<v\) as coordinates. Products over subsets of the unordered edges, with each edge in a fixed orientation, are an orthonormal Walsh basis. A directed cyclic word has indicator \(2^{-k}\prod_{uv\text{ along the word}}(1+Y_{uv})\), so its contribution to a Walsh coefficient is zero unless its underlying undirected cycle contains the support. Pairing a directed word with its reversal shows that odd coefficients of the count vanish.

For an adjacent pair of edges directed along a two-edge path, the sum of the two possible path orientations gives coefficient \(2^{1-k}(n-3)_{\underline{k-3}}\) in the sign convention of the path: choose its \(k-3\) other vertices and arrange them in order after the oriented path, then close the cycle. This holds also for \(k=3\). For disjoint edges the coefficient is zero: exchanging the endpoints of one edge while fixing the other preserves the count and reverses that monomial's sign. Consequently the entire degree-two component is \(a_{k,n}(T_n-\mathbb ET_n)\). There are \((n)_{\underline 3}/2\) adjacent-pair supports, giving \(\operatorname{Var}(T_n)=(n)_{\underline3}/32\) by squaring the triangle coefficient \(1/4\). This triangle projection is used as groundwork, not claimed as new.

For \(k\ge5\), a subset of edges of the underlying cycle cannot have a cycle component unless it is the full cycle. No residual Walsh support on four or fewer vertices can contribute: a residual support has at least four edges, and the only degree-at-most-two graph with four or more edges on at most four vertices is a four-cycle. On five vertices the only contributing even residual support is a four-edge path; a five-cycle is odd and there cannot be six edges. For a four-edge path, fixing its orientation and ordering the remaining \(k-5\) vertices counts \((n-5)_{\underline{k-5}}\) directed cyclic words containing the path in that orientation. Reversal contributes the same Walsh coefficient because there are four edges. Hence the coefficient of the path's oriented monomial is \(2^{1-k}(n-5)_{\underline{k-5}}\), whose ratio to \(a_{k,n}\) is \(1/[4(n-3)(n-4)]\). This proves the displayed exact projection onto supports of at most five vertices.

Every remaining support has \(v\ge6\) incident vertices and at most \(k\) edges, and its coefficient before division by \(a_{k,n}\) is \(O_k(n^{k-v})\) by counting possible containing cyclic words. There are \(O_k(n^v)\) such supports at each \(v\le k\), so Parseval bounds their squared sum by \(O_k(n^{2k-6})\). Dividing by \(a_{k,n}^2=\Theta_k(n^{2k-6})\) proves the stated variance bound. For \(k=5\) this support class is empty. The sign product on a four-edge path is unchanged by reversal and defines a distinct Walsh monomial up to its fixed sign for each of the \((n)_{\underline5}/2\) undirected paths, so \(\operatorname{Var}(W_{5,n})=(n)_{\underline5}/2\).

Let \(V=(n)_{\underline3}/32\) be the triangle variance. The variance of \(W_{5,n}/[4(n-3)(n-4)]\) is exactly \(V/[(n-3)(n-4)]\); this term and \(U_{k,n}\) are both orthogonal to triangles. Hence the triangle–cycle correlation is \((1+[(n-3)(n-4)]^{-1}+\operatorname{Var}(U_{k,n})/V)^{-1/2}\). Taylor expansion proves the sharp coefficient \(1/2\), and setting \(U_{5,n}=0\) proves the exact five-cycle case. For two lengths at least five, the normalized counts share the same first two terms, whose total variance is \(B=V(1+[(n-3)(n-4)]^{-1})\). Their covariance is \(B+O_{k,\ell}(1)\) by Cauchy–Schwarz, and their variances are each \(B+O_{k,\ell}(1)\); since \(B=\Theta(n^3)\), the other correlation bound follows.

## Relationship to prior work and limitations

The exact triangle coefficient and its orthogonal projection onto the linear span of the score-profile counts are already present in *Score-profile projection rigidity and square-root covariance phases for directed cycles*, Resultary record `4b9c5be28426`. The distinct four-cycle decomposition in Resultary record `3b4b1b16fef5` has a residual supported on four vertices and gives an exact correlation gap of order \(n^{-1}\). The present comparison starts at length five, where that support cannot occur and the five-vertex term contributes order \(n^{-2}\) relative to the triangle variance. Komarov and Mackey, arXiv:1410.6828, give a deterministic formula for the five-cycle count in terms of edge scores; no priority is claimed for the isolated five-cycle identity independently of the all-length result. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament* (1998), is a potentially encompassing comparison whose full text was not available for a decisive historical comparison. The proof here is exact and analytic; it does not rely on finite enumeration.
