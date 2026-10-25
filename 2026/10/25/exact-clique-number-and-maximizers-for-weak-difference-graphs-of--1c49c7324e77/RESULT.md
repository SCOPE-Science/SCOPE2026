# Exact clique number and maximizers for weak difference graphs of homogeneous finite-field products

## Finding
For every prime power \(q\ge3\) and every integer \(t\ge5\), let \(R=(\mathbb F_q)^t\), and let \(\mathcal D(R)\) be the weak zero-divisor difference graph: its vertices are the nonzero zero-divisors, and its edges are the edges of the weakly zero-divisor graph that are absent from the ordinary zero-divisor graph. Put \(a=q-1\). Then
\[
\omega(\mathcal D(R))=
\begin{cases}
 t+\displaystyle\sum_{j=(t+1)/2}^{t-2}\binom{t}{j} a^j,&t\text{ odd},\\[6pt]
 t+\displaystyle\frac12\binom{t}{t/2}a^{t/2}
       +\sum_{j=t/2+1}^{t-2}\binom{t}{j} a^j,&t\text{ even}.
\end{cases}
\]
Every maximum clique is obtained by including all vertices in every support class of size strictly greater than \(t/2\) and at most \(t-2\), taking exactly one vertex from each of the \(t\) coatom support classes, and, when \(t\) is even, taking all vertices from exactly one of each complementary pair of support classes of size \(t/2\). Every such selection is a maximum clique. Consequently the number of distinct maximum vertex cliques is
\[
N_{t,q}=
\begin{cases}
a^{t(t-1)},&t\text{ odd},\\
2^{\binom{t}{t/2}/2}a^{t(t-1)},&t\text{ even}.
\end{cases}
\]

## Assumptions and scope
The ring is a direct product of \(t\ge5\) copies of the **same** finite field of order \(q\ge3\), not an arbitrary product with unequal field orders. For an element \(x=(x_1,\dots,x_t)\), its support is \(\operatorname{supp}(x)=\{i:x_i\ne0\}\). Every graph vertex has nonempty proper support \(A\subsetneq[t]\). Write \(X_A\) for the class of vertices with support \(A\). Every such class has cardinality \(a^{|A|}\). A coatom means a subset of size \(t-1\). All graphs are simple (no loops), and a clique is a set of pairwise adjacent **distinct vertices**. The weakly zero-divisor graph joins distinct \(x,y\) if nonzero annihilators \(u,v\) exist with \(ux=vy=uv=0\).

## Proof
**1. Exact support reduction.** For any nonempty proper supports \(A,B\), ordinary zero-divisor adjacency is equivalent to \(A\cap B=\varnothing\). Nonzero annihilators of a vertex supported on \(A\) have supports in \(A^c\); thus weak adjacency holds exactly when one can select distinct indices from \(A^c\) and \(B^c\), equivalently \(|A^c\cup B^c|\ge2\). Consequently distinct support classes \(X_A,X_B\) are completely adjacent in \(\mathcal D(R)\) exactly when \(A\cap B\ne\varnothing\). Inside a fixed class \(X_A\), distinct vertices are adjacent exactly when \(|A|\le t-2\); the coatom classes are internally independent. In maximizing a clique, each selected class of size at most \(t-2\) is therefore fully taken, and each selected coatom class contributes exactly one vertex. The clique-number problem becomes the weighted intersecting-family maximum with weights
\[
f(A)=\begin{cases}a^{|A|},&1\le|A|\le t-2,\\1,&|A|=t-1.\end{cases}
\]

**2. Families without singletons.** Suppose the selected support family contains no singleton. Every coatom meets every support of size at least two (since \(t\ge5\)), so all \(t\) coatom classes may be added without violating pairwise intersection. For every complementary pair \(\{A,A^c\}\) with \(2\le|A|,|A^c|\le t-2\), an intersecting family contains at most one of its members. Its weight contribution is at most \(\max(a^{|A|},a^{t-|A|})=a^{\max(|A|,t-|A|)}\). Summing once over all those complementary pairs and adding \(t\) bounds the clique weight by the displayed formula for \(\omega(\mathcal D(R))\): each level strictly above the middle occurs exactly once per pair, while for even \(t\) there are \(\frac12\binom{t}{t/2}\) middle pairs.

This bound is attained by taking every support with \(t/2<|A|\le t-2\), every coatom, and, if \(t\) is even, exactly one member of every complementary middle pair. The selected supports pairwise meet: two supports larger than half meet; a support of size exactly half meets every larger support; any two distinct middle supports that are not complements meet; every coatom meets every selected support of size at least two. Thus the bound is sharp among singleton-free families.

**3. A singleton cannot maximize.** If an intersecting family contains \(\{i\}\), it has no other singleton, and every other support must contain \(i\). Its weight is at most the full \(i\)-star, of weight \(a+(t-1)+\sum_{j=2}^{t-2}\binom{t-1}{j-1}a^j\). The singleton and coatom contribution to the full star is \(a+t-1\), compared with \(t\) for the singleton-free construction, a potential advantage of \(a-1\). Among every complementary pair of sizes between two and \(t-2\), the star chooses precisely the side containing \(i\), whereas the singleton-free construction chooses the side of greater cardinality. Hence the latter never loses weight on such a pair. Choose \(j\ne i\) and the particular pair \(A=\{i,j\}\), \(A^c=[t]\setminus\{i,j\}\). Since \(t\ge5\), its gain relative to the star is \(a^{t-2}-a^2\ge a^3-a^2=a^2(a-1)>a-1\) for \(a\ge2\). The singleton-free construction is therefore strictly better than **every** intersecting family containing a singleton. This finishes the sharp upper bound.

**4. All equality cases and their number.** At optimality no singleton occurs. All \(t\) coatom classes must be present, each represented by one vertex; adding a missing coatom would otherwise increase the weight. Every complementary pair of non-coatom/non-singleton classes must contribute its maximum possible weight: omitting a pair would decrease the sum. Since \(a>1\), if its two sizes differ, equality forces the strictly larger support, so every class above half and at most \(t-2\) is included. For even \(t\), the equal-size pairs contribute one class each, independently selectable. The intersection argument in Step 2 shows that every such selection is valid. Each of the \(t\) independent coatom classes contains \(a^{t-1}\) possible representative vertices; those choices give \(a^{t(t-1)}\) distinct cliques. For even \(t\), the \(\frac12\binom{t}{t/2}\) complementary middle pairs each give two choices. Multiplication gives the stated count.

## Verification
A standalone finite integer-optimization checker is supplied as `verify.py`. It forms the support classes independently and solves the weighted maximum independent-set formulation of disjointness constraints using exact integer variables, checking \((t,q)=(5,2),(5,3),(5,4),(5,5),(6,2),(6,3),(6,4),(7,2)\). All instances return the predicted clique number with a certified optimal solver status. The cases with \(q=2\) are extra boundary sanity checks and are **not** included in the theorem's quantified hypothesis. The proof above, rather than the finite checks, establishes the unrestricted result. The checker also constructs the middle-level choices and verifies their complement-pair compatibility and their count for \(t=6\).

## Relationship to prior work
Wani's *The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring* (arXiv:2607.17677, first public 20 July 2026), Theorem 3.1 and Proposition 3.3 supply the support decomposition. Its Theorem 6.2 gives the clique number for \(t=4\); Propositions 6.1, 6.5, 6.7 and 6.8 give lower and upper bounds for larger \(t\), and Question 6.11 asks for the exact value. These bounds do not imply the present uniform-field formula for \(q\ge3\): the source's refined complementary-pair bound still permits a singleton/coatom contribution of \(a+t-1\) instead of the attainable \(t\), while the star lower bound generally misses the majority construction. The strict comparison in Step 3 resolves that gap for equal fields. In particular, the proof also classifies and counts **all** maximum cliques, not merely one construction.

Filmus, *Ahlswede–Khachatrian Theorems: Weighted, Infinite, and Hamming* (arXiv:1610.00756), Theorem 2.2, treats weighted intersecting families on a full Boolean lattice. The present weights are different: the full-support class is absent and coatom classes are assigned weight one even though their cardinalities grow as \(a^{t-1}\). Therefore the classical full-lattice optimization does not directly give this graph-specific statement. Its extremal-set principles inform the complementary-pair argument. The extension to unequal field orders is not claimed.

## Limitations
Only direct products of equal finite fields with \(q\ge3\) and \(t\ge5\) are classified. For \(q=2\), the same clique-number expression happens to hold but different optimal support families can occur, so the stated classification of **all** maximizers does not extend unchanged. For unequal field orders, the weight is support-dependent and the exact maximum is not determined here. The verification checks finitely many small instances and cannot replace the proof. No independent mathematical validation has been performed.

## References
1. B. A. Wani, *The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring*, arXiv:2607.17677 (first posted 20 July 2026). https://arxiv.org/abs/2607.17677
2. Y. Filmus, *Ahlswede–Khachatrian Theorems: Weighted, Infinite, and Hamming*, arXiv:1610.00756 (2016), especially Theorem 2.2. https://arxiv.org/abs/1610.00756
