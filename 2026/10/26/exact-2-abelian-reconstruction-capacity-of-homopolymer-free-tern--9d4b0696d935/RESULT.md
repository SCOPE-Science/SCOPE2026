# Exact 2-abelian reconstruction capacity of homopolymer-free ternary words

## Finding
Let \(\Sigma=\{0,1,2\}\). For each integer \(n\ge1\), let \(\mathcal W_n\) be the set of length-\(n\) words over \(\Sigma\) without equal adjacent letters. Two words are 2-abelian equivalent if the number of occurrences of every contiguous factor of length one or two agrees. Write \(C_n\) for the number of equivalence classes in \(\mathcal W_n\). Then
\[
\sum_{n\ge1}C_nz^{n-1}=\frac{3}{(1-z)^4(1+z)^2}-\frac{3z^2}{1-z^2}.
\]
In particular, the values for \(1\le n\le16\) are \(3,6,12,24,39,60,87,120,162,210,270,336,417,504,609,720\), and \(C_n=n^3/8+O(n^2)\). The maximum cardinality of a code contained in \(\mathcal W_n\) whose words have pairwise distinct observations is exactly \(C_n\).

## Assumptions and scope
Words are **linear**, not cyclic; occurrences are contiguous and overlapping occurrences count separately. Homopolymer-free means \(w_i\ne w_{i+1}\) for \(1\le i<n\). There are no conditions on the first or last letter. The alphabet has exactly three labelled letters. The observation contains counts of all one- and two-letter factors, including the six off-diagonal digrams and the three single letters. The formula covers every integer \(n\ge1\), including the singleton words.

## Proof
Denote the multiplicities of the arcs \(0\to1,1\to0,1\to2,2\to1,2\to0,0\to2\) by \(x_{01},x_{10},x_{12},x_{21},x_{20},x_{02}\). Given these multiplicities and a starting letter, the endpoint is determined by the outdegree-minus-indegree vector. The singleton count of symbol \(v\) is its outdegree plus the indicator that \(v\) is the endpoint. Thus the full 2-abelian observation is equivalent to the start letter and all six arc multiplicities; conversely the observation determines the start from the singleton counts and the outdegrees. This last statement includes the case \(n=1\), in which there are no arcs.

For a nonzero arc vector, the underlying undirected support is connected: any two edges in a triangle intersect. The directed Euler-trail theorem consequently says that the vector represents a word if and only if (i) all three net vertex imbalances vanish, in which case any vertex with positive degree may be a start, or (ii) exactly one net imbalance is \(+1\), another is \(-1\), and the remaining one is zero, in which case the positive vertex is the unique start. Each admissible start produces a word by an Euler trail (repeating arcs according to their multiplicity); all such words share the specified observation. For the zero vector there are exactly three singleton words.

Set \(a=x_{01}-x_{10}\), \(b=x_{12}-x_{21}\), and \(c=x_{20}-x_{02}\). Net imbalances at \(0,1,2\) are \((a-c,b-a,c-b)\). For any prescribed integer difference \(d\) in one pair of opposite arc multiplicities, their total-weight generating series is \(z^{|d|}/(1-z^2)\). In the balanced case \(a=b=c=t\), giving the arc-count series
\[
 B(z)=\frac{\sum_{t\in\mathbb Z}z^{3|t|}}{(1-z^2)^3}=\frac{1+z^3}{(1-z^3)(1-z^2)^3}.
\]
For the specified imbalance pattern \((+1,-1,0)\), corresponding to start \(0\) and end \(1\), we have \((a,b,c)=(t,t-1,t-1)\), giving
\[
 A(z)=\frac{\sum_{t\in\mathbb Z}z^{|t|+2|t-1|}}{(1-z^2)^3}=\frac{z+z^2}{(1-z^3)(1-z^2)^3}.
\]
Cyclic relabelling and reversing arcs yield the same series for all six ordered distinct endpoint pairs, so nonzero imbalance contributes \(6A(z)\) observations.

A nonzero balanced vector admits three starting vertices unless its arcs use exactly two vertices, in which case it admits two. Precisely three balanced two-vertex vectors exist at each even positive total arc count, each consisting of an equal positive number of opposing arcs on a chosen edge. At zero arc count, there are three valid single-letter starts. Hence the balanced contribution is \(3B(z)-3z^2/(1-z^2)\). Combining both cases gives
\[
6A(z)+3B(z)-\frac{3z^2}{1-z^2}
=\frac{3}{(1-z)^4(1+z)^2}-\frac{3z^2}{1-z^2}.
\]
The coefficient of \(z^{n-1}\) is \(C_n\). The unique order-four pole at \(z=1\) has leading coefficient \(3/4\), giving \(C_n=n^3/8+O(n^2)\). Finally, a family of distinct observations has at most one representative from each equivalence class, and selecting one Euler-trail word per class attains that bound. This proves the exact reconstruction-code capacity.

## Verification
The included `verify.py` checks the rational-series coefficients by two independent finite methods: direct enumeration of all homopolymer-free words for \(1\le n\le13\), and enumeration of all six-arc multiplicity vectors of each total weight up to \(12\), applying the Euler-trail criterion. The proof above, not the finite checks, establishes all lengths. Run `python3 verify.py` in the directory containing this file.

## Relationship to prior work
2-abelian equivalence and its connection with factor multiplicities and endpoints are standard; in particular Karhumäki, Puzynina, Rao and Whiteland (2017) examine cardinalities of 2-abelian equivalence classes. Karhumäki and Whiteland (2018) show regularity for representatives of fixed-cardinality equivalence classes. Cassaigne and collaborators (2017) study rationality and unrestricted word counts. The explicit unrestricted ternary quotient sequence appears as OEIS A289658. None of these cited statements directly gives the homopolymer-free ternary quotient above; this result refines the observation by imposing a no-equal-adjacencies restriction and accounting explicitly for linear Euler-trail endpoints. The result is distinct from realizability and optimization of strict orderings of digram frequencies, which forget exact multiplicities.

## Limitations
The formula counts observation classes, not their cardinality distribution or a general decoding algorithm. It is restricted to three symbols, adjacent distinctness, and factor lengths at most two. There is no claim that the cited literature exhausts possible equivalent formulations: the 2018 chapter's full text was unavailable for inspection, leaving a residual originality risk. No independent external mathematical review has been conducted.

## References
1. J. Karhumäki and M. A. Whiteland, *Regularity of k-Abelian Equivalence Classes of Fixed Cardinality*, 2018, DOI: 10.1007/978-3-319-98355-4_4 (first publicly dated 2018-08-09).
2. J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, Theoretical Computer Science 658 (2017), 190–204; arXiv:1605.03319 (first posted 2016-05-11).
3. J. Cassaigne, J. Karhumäki, S. Puzynina and M. A. Whiteland, *k-Abelian Equivalence and Rationality*, Fundamenta Informaticae 154 (2017), 65–94; DOI: 10.3233/FI-2017-1553.
4. OEIS A289658, number of ternary 2-abelian equivalence classes of unrestricted words (different object).
