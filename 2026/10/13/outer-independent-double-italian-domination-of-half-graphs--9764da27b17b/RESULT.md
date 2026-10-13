# Outer-independent double Italian domination of half graphs
## Finding
Let \(n\ge4\), and let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{oidI}(H_n)=n+4.
\]

The minimum outer-independent double Italian dominating functions admit a complete classification. Choose a threshold
\[
t\in\{1,\ldots,n-1\},
\]
choose independently
\[
(f(a_1),f(b_1))\in\{(2,1),(3,0)\}
\]
and
\[
(f(a_n),f(b_n))\in\{(0,3),(1,2)\},
\]
and for the interior pairs put
\[
(f(a_i),f(b_i))=
\begin{cases}
(1,0),&2\le i\le t,\\
(0,1),&t<i\le n-1.
\end{cases}
\]
These, and only these, are minimum functions. Hence the exact number of minima is
\[
4(n-1).
\]

## Assumptions and scope
An outer-independent double Italian dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex \(v\) with \(f(v)\in\{0,1\}\) satisfies
\[
\sum_{u\in N[v]}f(u)\ge3,
\]
and the set
\[
V_0=\{v:f(v)=0\}
\]
is independent. Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{oidI}(G)\) is the minimum weight.

The theorem is stated for \(n\ge4\), where two disjoint endpoint blocks drive the sharp lower bound. Direct computation gives the smaller boundary values
\[
\gamma_{oidI}(H_2)=5,\qquad \gamma_{oidI}(H_3)=7,
\]
but their minimum-function families have additional shapes and are not part of the classification above.

## Proof
Write
\[
x_i=f(a_i),\qquad y_i=f(b_i),
\]
and define
\[
s_i=x_i+y_i-1.
\]
Since \(a_i b_i\) is an edge and the zero set is independent, \(x_i\) and \(y_i\) cannot both vanish. Therefore
\[
s_i\ge0,
\]
and
\[
\omega(f)=n+\sum_{i=1}^{n}s_i.
\tag{1}
\]

We first extract two endpoint inequalities.

The vertex \(b_1\) is a leaf with unique neighbor \(a_1\). If \(y_1\le1\), its defining inequality gives
\[
x_1+y_1\ge3,
\]
so
\[
s_1\ge2.
\]
If instead \(s_1<2\), the only remaining possibility is
\[
(x_1,y_1)=(0,2),
\]
so \(s_1=1\). Because \(a_1\) is zero and is adjacent to every vertex of \(B\), independence of the zero set forces \(y_2>0\). If \(s_2=0\), then
\[
(x_2,y_2)=(0,1),
\]
and the closed-neighborhood weight at \(b_2\) is only \(1\), a contradiction. Hence in all cases
\[
s_1+s_2\ge2.
\tag{2}
\]

By the symmetry interchanging \(a_i\) with \(b_{n+1-i}\),
\[
s_{n-1}+s_n\ge2.
\tag{3}
\]
For \(n\ge4\), the two index blocks in (2) and (3) are disjoint. Thus
\[
\sum_{i=1}^{n}s_i\ge4.
\]
Equation (1) yields
\[
\omega(f)\ge n+4.
\tag{4}
\]

The displayed threshold functions have weight \(n+4\). Their zero vertices consist of a prefix on the \(B\)-side and a suffix on the \(A\)-side, so no two zero vertices are adjacent. Every interior label \(1\) sees an endpoint label at least \(2\), and every interior zero sees its paired label \(1\) together with an endpoint label at least \(2\). The possible endpoint label \(1\) has closed-neighborhood weight exactly \(3\). Hence every displayed function is feasible, proving
\[
\gamma_{oidI}(H_n)=n+4.
\]

It remains to prove that equality has no other form.

Suppose
\[
\omega(f)=n+4.
\]
Then equality holds in both (2) and (3), and every surplus outside the two endpoint blocks is zero.

Assume first that the exceptional left case occurs:
\[
(x_1,y_1)=(0,2).
\]
Then equality in (2) forces \(s_2=1\). Since \(a_1=0\), every \(y_j\) is positive. The defining inequality at \(b_2\) rules out \((x_2,y_2)=(1,1)\), so
\[
(x_2,y_2)=(0,2).
\]
If \(n\ge5\), then \(s_3=0\), hence \((x_3,y_3)=(0,1)\), and \(b_3\) has closed-neighborhood weight \(1\), impossible.

If \(n=4\), then \(y_3>0\). Equality in the right block gives \(s_3+s_4=2\). The case \(s_3=0\) again fails at \(b_3\). If \(s_3=1\), feasibility at \(b_3\) forces \((x_3,y_3)=(0,2)\), while \(s_4=1\) forces the right leaf exception
\[
(x_4,y_4)=(2,0).
\]
But then \(a_1\) and \(b_4\) are adjacent zero vertices, contradicting outer independence. The remaining allocation \(s_3=2,s_4=0\) is impossible at the leaf \(a_4\). Thus the left exception never occurs.

By symmetry the right exception never occurs. Consequently
\[
s_1=s_n=2
\]
and
\[
s_i=0\qquad(2\le i\le n-1).
\]
Thus every interior pair contains exactly one label \(1\) and one label \(0\).

Outer independence now forces a single threshold: if \(a_i\) is zero and \(b_j\) is zero, then necessarily \(i>j\), because \(a_i b_j\) is an edge exactly when \(i\le j\). Hence for a unique
\[
t\in\{1,\ldots,n-1\},
\]
the interior pairs are
\[
(1,0)\quad\text{through index }t,
\]
followed by
\[
(0,1)\quad\text{after index }t.
\]

Finally,
\[
x_1+y_1=3.
\]
The choices \((0,3)\) and \((1,2)\) fail at \(b_2\), according as the threshold leaves \(b_2\) positive or zero. Therefore
\[
(x_1,y_1)\in\{(2,1),(3,0)\}.
\]
The symmetric right-end argument gives
\[
(x_n,y_n)\in\{(0,3),(1,2)\}.
\]
This is exactly the stated family. There are \(n-1\) threshold choices and two independent choices at each end, giving
\[
4(n-1)
\]
minimum functions.

## Verification
The included checker evaluates the definition directly on the half graph.

It exhausts all
\[
4^{8}+4^{10}=1{,}114{,}112
\]
labelings for \(H_4\) and \(H_5\). It finds no feasible function below the claimed weight and confirms that every minimum function is one of the stated threshold functions: \(12\) minima for \(H_4\) and \(16\) for \(H_5\).

It also constructs the full stated family for every
\[
4\le n\le50
\]
and directly checks outer independence, all closed-neighborhood inequalities, the weight, and the count.

## Relationship to prior work
The 2021 primary paper defining and developing this parameter proves general bounds and exact values for complete multipartite graphs. In particular, for the balanced complete bipartite graph \(K_{n,n}\) with \(n\ge3\), it gives
\[
\gamma_{oidI}(K_{n,n})=n+2.
\]
The half graph \(H_n\) is a sparse nested-neighborhood spanning subgraph of \(K_{n,n}\), not a complete multipartite graph. The theorem here shows that the Ferrers deletion pattern raises the optimum by exactly two and, more strongly, forces a complete threshold description of every optimum.

The inspected 2021 full text contains no half-graph or chain-graph specialization. A 2022 continuation studies tree comparisons and degree-based bounds. A 2023 characterization paper addresses computational complexity and graphs with small or near-maximal values, while a separate 2023 paper studies graph products. None of the inspected or indexed statements supplies the half-graph formula or its minimum-function classification.

## Limitations
The complete minimum-function classification is proved for \(n\ge4\). The smaller half graphs have extra equality patterns.

The theorem concerns the minimum layer only; it does not enumerate all feasible outer-independent double Italian functions by weight.

Finite computation is corroborative only. The arbitrary-order result follows from the endpoint-surplus proof.

A differently phrased or non-indexed treatment of the same half-graph family may exist; the graph-products paper was identifiable but its full text was not accessible in the inspected route.

## References
1. L. Volkmann, “Remarks on the outer-independent double Italian domination number,” Opuscula Mathematica 41(2) (2021), 259–268, DOI 10.7494/OpMath.2021.41.2.259; published online 17 March 2021.
2. N. A. Abd Aziz, H. Kamarulhaili, F. Azvin, N. Jafari Rad, “On the outer-independent double Italian domination number,” Electronic Journal of Graph Theory and Applications 10(2) (2022), 365–374, DOI 10.5614/ejgta.2022.10.2.2.
3. R. Jalaei, D. A. Mojdeh, “Outer independent double Italian domination: Complexity, characterization,” Discrete Mathematics, Algorithms and Applications 15(3) (2023), article 2250085, DOI 10.1142/S1793830922500859.
4. R. Jalaei, D. A. Mojdeh, “Outer Independent Double Italian Domination of Some Graph Products,” Theory and Applications of Graphs 10(1) (2023), article 5, DOI 10.20429/tag.2023.100105.
