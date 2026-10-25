# Exact cyclic trigram-profile count for binary circular words

## Finding
For an integer \(n\geq1\), let \(\mathcal P_n\) consist of the vectors of multiplicities of all eight binary circular factors of length three in a binary circular word of length \(n\), counted with multiplicity at each of the \(n\) marked starting positions. Indices wrap modulo \(n\), including for \(n=1,2\). Put \(f(n)=|\mathcal P_n|\). Then

\[
\sum_{n\geq1}f(n)z^n=\frac{2z}{1-z}+\frac{z^2}{1-z^2}
+\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}
+\frac{z^4(1+z^3)}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}.
\]

In particular, \(f(n)=n^4/288+O(n^3)\), and the values for \(1\leq n\leq16\) are
\(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271\).

For a channel that reveals only this cyclic-trigram multiplicity vector, the maximum cardinality of a zero-error reconstruction code chosen from length-\(n\) binary circular words is exactly \(f(n)\): choose one representative from each distinct profile.

## Assumptions and scope
A circular word is a binary word considered up to rotation, not reversal or bit complementation. The observation counts each length-three block starting at each marked position, including blocks crossing the chosen representative's boundary and repetitions arising from periodic words. Thus the result is not the number of necklaces and is not the ordinary linear \(3\)-Abelian class-counting problem. All integers are nonnegative unless indicated; all generating functions are formal power series.

## Proof
Order the eight component counts as \((g_{000},g_{001},g_{010},g_{011},g_{100},g_{101},g_{110},g_{111})\). Regard each triple \(abc\) as a directed edge from the vertex \(ab\) to \(bc\) in the order-two binary de Bruijn digraph. Each circular word traces a closed walk using edge \(abc\) exactly \(g_{abc}\) times. Conversely, a nonzero integer edge-multiplicity vector is attained by a circular word precisely when it is balanced at each vertex and its positive-edge directed multigraph admits an Eulerian circuit, equivalently its nonzero-degree vertices lie in one connected component of the underlying undirected graph (for a balanced finite digraph).

Write \(a=g_{000}\), \(h=g_{111}\). Balance at \(00\) and \(11\) gives \(g_{001}=g_{100}=t\) and \(g_{011}=g_{110}=u\). Balance at \(01\), equivalently at \(10\), gives \(g_{010}+u=t+g_{101}\). Hence there is a unique \(j\geq0\) with
\[
g_{010}=\max(t-u,0)+j,\qquad g_{101}=\max(u-t,0)+j.
\]
The length is
\[
n=a+h+3\max(t,u)+\min(t,u)+2j.\tag{1}
\]
All five parameters \(a,h,t,u,j\) are nonnegative integers; they determine the complete eight-component vector without collisions.

There are exactly five disjoint connected-support cases. First, \(t,u>0\): the nonzero edges \(001,100,011,110\) join all four vertices, so \(a,h,j\) are unrestricted. Second, \(t>0,u=0\): the edges connect vertices \(00,01,10\), so the loop at \(11\) is forbidden, i.e. \(h=0\), and \(a,j\) are unrestricted. Third, \(t=0,u>0\): the symmetric case requires \(a=0\). Fourth, \(t=u=0,j>0\): the edges \(010,101\) form the two-vertex alternating cycle; both self-loops must be absent, \(a=h=0\). Fifth, \(t=u=j=0\): only the two isolated self-loops are possible, so exactly one of \(a,h\) is positive.

The two pure-loop cases contribute \(2z/(1-z)\); the alternating cycle contributes \(z^2/(1-z^2)\). In each of the two one-sided cases, the positive parameter contributes a factor \(z^3/(1-z^3)\), the freely inserted alternating two-cycle a factor \(1/(1-z^2)\), and the one allowed self-loop a factor \(1/(1-z)\); together they contribute \(2z^3/((1-z)(1-z^2)(1-z^3))\).

When \(t,u>0\), free self-loops and alternating insertions contribute \((1-z)^{-2}(1-z^2)^{-1}\). If \(t=u=s\geq1\), equation (1) gives core weight \(4s\), contributing \(z^4/(1-z^4)\). If \(t\ne u\), put \(s=\min(t,u)\geq1\) and \(d=|t-u|\geq1\); the core weight is \(4s+3d\), with two orientations, contributing \(2z^7/((1-z^4)(1-z^3))\). Their sum equals \(z^4(1+z^3)/((1-z^4)(1-z^3))\). Multiplication by the free factors and addition over the five disjoint cases proves the generating-function identity.

The final rational summand has its sole pole of order five on the unit circle at \(z=1\), with principal part \(\frac1{12}(1-z)^{-5}\). Other summands and other roots-of-unity poles have order at most four. Therefore \(f(n)=\frac1{12}\binom{n+4}{4}+O(n^3)=n^4/288+O(n^3)\). The coding statement follows because two different source words with the same observed vector cannot both belong to a zero-error code, while one representative of each possible vector can.

## Verification
The included standalone \(\texttt{verify.py}\) uses no external dependencies. Running \(\texttt{python\ verify.py}\) enumerates all \(2^n\) binary input words for each \(1\leq n\leq16\), computes cyclic three-factor histograms directly, and compares the complete sets of attainable vectors against an independently implemented nonnegative-flow parameter enumeration. It checks the predicted coefficients at these lengths, and compares independently generated vector counts and coefficient sums at lengths \(20,24,30\). The expected output begins with \(\texttt{VERIFY_OK}\). These finite checks support but do not replace the unrestricted proof above.

At length six, \(f(6)=13\) while there are fourteen binary necklaces; distinct necklaces \(001011\) and \(001101\) share the same profile. The loss of injectivity makes the profile count a genuine reconstruction-channel invariant rather than an ordinary necklace census.

## Relationship to prior work
Karhumäki, Saarela and Zamboni (2013), §2.3, establish polynomial growth of the number of **linear** \(k\)-Abelian equivalence classes, and Karhumäki, Puzynina, Rao and Whiteland (2016), §§2–5, use weighted de Bruijn graphs to analyze **sizes** and singletons of such linear classes. Their framework motivates the graph representation here; their counting problems retain finite-word boundaries and do not directly state the exact binary **cyclic** length-three profile function. The later paper by Cassaigne, Karhumäki, Puzynina and Whiteland establishes rationality for class counts of linear finite words, a general result that does not by itself determine this cyclic-profile formula. The distinction is in the quantified objects and observations, not merely terminology.

## Limitations
This is an exact enumeration of **attainable observation vectors**, not of the number of necklaces realizing each vector or the size of the largest ambiguity class. No uniform general-alphabet or greater-window-length formula is claimed. Literature comparisons establish no mathematical priority guarantee; in particular, the later rationality paper was inspected at the abstract level rather than throughout its full text.

## References
1. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, 22 January 2013, https://arxiv.org/abs/1301.5104.
2. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of \(k\)-Abelian equivalence classes*, arXiv:1605.03319v1, 11 May 2016, https://arxiv.org/abs/1605.03319.
3. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *\(k\)-Abelian Equivalence and Rationality*, *Fundamenta Informaticae* **154** (2017), 65–94, DOI:10.3233/FI-2017-1553.
