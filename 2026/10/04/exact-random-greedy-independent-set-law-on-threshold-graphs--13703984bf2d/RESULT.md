# Exact random-greedy independent-set law on threshold graphs
## Finding
Let \(G\) be a threshold graph with vertices \(1,\ldots,n\) in a creation order. Write \(b_1=0\), and for \(j\ge2\) let \(b_j=0\) when vertex \(j\) is added isolated from all earlier vertices and \(b_j=1\) when it is added adjacent to every earlier vertex. Define
\[
Z=\{j:b_j=0\},\qquad D=\{j:b_j=1\},\qquad z_i=|\{j>i:b_j=0\}|.
\]
Run the random greedy maximal-independent-set algorithm: inspect the vertices in a uniformly random order and accept a vertex exactly when it has no previously accepted neighbor.

The complete output law is as follows. The possible outputs are exactly
\[
M_0=Z
\]
and, for every \(i\in D\),
\[
M_i=\{i\}\cup\{j>i:b_j=0\}.
\]
Their probabilities are
\[
p_0=\prod_{j\in D}\frac{j-1}{j},
\]
and
\[
p_i=\frac1i\prod_{\substack{j\in D\\ j>i}}\frac{j-1}{j}\qquad(i\in D).
\]
Consequently, if \(X=|I|\) is the random greedy output size, then its probability generating function is
\[
P_G(x)=\mathbb E[x^X]=p_0x^{|Z|}+\sum_{i\in D}p_ix^{1+z_i}.
\]
Equivalently, for the threshold graph \(G_k\) induced by the first \(k\) creation vertices,
\[
P_1(x)=x,
\]
and for \(k\ge2\),
\[
P_k(x)=
\begin{cases}
xP_{k-1}(x),&b_k=0,\\
\dfrac{x}{k}+\dfrac{k-1}{k}P_{k-1}(x),&b_k=1.
\end{cases}
\]
In particular, the entire distribution, expectation, and variance are computable in one pass through the creation sequence.

There is also a closed optimality probability. Since \(\alpha(G)=|Z|\), let \(s\) be the position of the second zero in the creation sequence, taking \(s=n+1\) if no second zero exists. Then
\[
\Pr(X=\alpha(G))=\prod_{\substack{j\in D\\ j>s}}\frac{j-1}{j}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A creation sequence is fixed as above; consecutive vertices of the same creation type may be permuted without changing the graph, and the displayed law is consistent with those symmetries. The random greedy process is the standard uniformly random vertex-order greedy maximal-independent-set process.

The result concerns the exact finite distribution on a fixed threshold graph, not an asymptotic random-threshold-graph model. The formulas are expressed from a creation sequence, which is a standard structural representation of threshold graphs.

## Proof
Proceed recursively in the creation order. Suppose first that \(b_k=0\). Vertex \(k\) is isolated in \(G_k\), so it is accepted by the greedy process for every inspection order and it cannot affect any decision among vertices \(1,\ldots,k-1\). The relative order of those earlier vertices remains uniform. Therefore the output on \(G_k\) is the output on \(G_{k-1}\) with vertex \(k\) adjoined, and
\[
P_k(x)=xP_{k-1}(x).
\]

Now suppose \(b_k=1\). Vertex \(k\) is universal in \(G_k\). With probability \(1/k\), it is the first inspected vertex; then it is accepted and blocks every other vertex, so the output is the singleton \(\{k\}\). With probability \((k-1)/k\), some earlier vertex is inspected first. That vertex is accepted, immediately blocks \(k\), and the rest of the decisions among vertices \(1,\ldots,k-1\) are exactly the random greedy process on \(G_{k-1}\) under a uniform restricted order. Hence
\[
P_k(x)=\frac{x}{k}+\frac{k-1}{k}P_{k-1}(x).
\]
This proves the recurrence.

The same recursion identifies the output supports. Start from \(G_1\), whose only maximal independent set is \(M_0=\{1\}\). An isolated addition appends the new vertex to every existing maximal independent set. A dominating addition leaves every old maximal independent set maximal and creates one new maximal independent set, the singleton consisting of the new dominating vertex at that stage. Propagating these sets through later isolated additions gives exactly \(M_0=Z\) and \(M_i=\{i\}\cup\{j>i:b_j=0\}\) for \(i\in D\).

When \(M_i\) is born at a dominating step \(i\), its probability is \(1/i\). Each later isolated step preserves that probability, while each later dominating step \(j\) preserves any previously existing outcome with factor \((j-1)/j\). This gives
\[
p_i=\frac1i\prod_{\substack{j\in D\\ j>i}}\frac{j-1}{j}.
\]
The initial outcome \(M_0\) survives every dominating step, giving
\[
p_0=\prod_{j\in D}\frac{j-1}{j}.
\]
The recurrence already shows that these probabilities sum to one.

Finally, every independent set contains at most one dominating-creation vertex. The all-zero set \(Z\) is independent, and every \(M_i\) has size \(1+z_i\le |Z|\) because vertex \(1\) is a zero before every dominating vertex. Thus \(\alpha(G)=|Z|\). Equality \(|M_i|=|Z|\) holds exactly for dominating vertices before the second zero. If that second zero is at position \(s\), the probabilities of \(M_0\) and all such early \(M_i\) telescope to one before accounting for later dominating steps; every dominating step \(j>s\) preserves an already maximum output with factor \((j-1)/j\). Therefore
\[
\Pr(X=\alpha(G))=\prod_{\substack{j\in D\\ j>s}}\frac{j-1}{j}.
\]

## Verification
A standalone exact checker enumerated every binary threshold creation sequence of orders \(1\) through \(7\) with first bit zero. For each of the \(127\) sequences it enumerated all vertex permutations, ran greedy MIS directly, and compared the exact rational output distribution with the product formulas above. It also checked the probability-generating-function recurrence and the maximum-set success probability. The replay covered \(347741\) permutation checks and printed `VERIFY_OK sequences=127 permutation_checks=347741`.

## Relationship to prior work
Diaconis, Holmes, and Janson give the isolated/dominating sequential characterization of threshold graphs and study random threshold-graph models. Their creation-sequence framework is the structural input used here; their paper does not study the random greedy maximal-independent-set output law.

Gurski and Rehs explicitly count and enumerate maximal independent sets of threshold graphs and related classes. That prior result covers the support family of maximal independent sets at an algorithmic-enumeration level. The present claim does not treat that support classification as new; it assigns the exact random-greedy probability to every support, derives the full size distribution recurrence, and gives the closed probability of attaining a maximum independent set. Searches within their full text found no occurrence of “random” or “greedy”.

Krivelevich, Mészáros, Michaeli, and Shikhelman study the random greedy MIS process broadly and give the standard uniformly random-order formulation. Their inspected full text discusses paths, random graphs, trees, and sparse planar graphs; targeted searches found no threshold-graph or cograph specialization.

## Limitations
The formulas rely on the threshold-graph isolated/dominating decomposition and do not directly extend to arbitrary split graphs or cographs. The originality comparison is based on targeted database searches and inspected public literature; a differently indexed or terminology-shifted prior derivation remains a residual risk. The exhaustive computation is corroborative only: the general theorem rests on the recursive proof above.

## References
1. P. Diaconis, S. Holmes, and S. Janson, “Threshold graph limits and random threshold graphs,” arXiv:0908.2448v1, 17 August 2009.
2. F. Gurski and C. Rehs, “Counting and Enumerating Independent Sets with Applications to Knapsack Problems,” arXiv:1710.08953v1, 24 October 2017.
3. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” Random Structures & Algorithms 64 (2024), 986–1015, DOI:10.1002/rsa.21200; first published 18 December 2023.
