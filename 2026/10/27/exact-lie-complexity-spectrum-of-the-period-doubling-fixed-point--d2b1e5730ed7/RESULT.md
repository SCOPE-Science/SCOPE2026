# Exact Lie-complexity spectrum of the period-doubling fixed point

## Finding
Let \(d\) be the binary period-doubling word. Its Lie complexity is supported on precisely two geometric progressions:

\[
L_d(n)=\begin{cases}
2,&n=2^a\text{ or }n=3\cdot2^a\text{ for an integer }a\ge0,\\
0,&\text{otherwise},
\end{cases}\qquad(n\ge1).
\]

All completely represented cyclic conjugacy classes are explicitly given. For \(n=2^a\), their representatives are \(h^a(0)\) and \(h^a(1)\). For \(n=3\cdot2^a\), their representatives are \(h^a(000)\) and \(h^a(001)\). More strongly, \(h\) induces a bijection from the completely represented cyclic classes of length \(m\) to those of length \(2m\), for every integer \(m\ge1\).

## Assumptions and scope
Work over \(\{0,1\}\). Define the length-two substitution \(h(0)=01\), \(h(1)=00\), and its right-infinite fixed point \(d=\lim_{k\to\infty}h^k(0)=0100010101000100\cdots\). Let \(F_n\) be the set of finite contiguous factors of \(d\) of length \(n\). For a finite word \(v\), let \(\rho(v)\) be the left cyclic shift by one symbol, and let \([v]=\{\rho^j(v):0\le j<|v|\}\) (a set, possibly smaller than \(|v|\)). Define

\[
\mathcal C_n=\{[v]: |v|=n,\ [v]\subseteq F_n\},\qquad L_d(n)=|\mathcal C_n|.
\]

This requires **every** cyclic rotation to occur. It differs from cyclic complexity, which counts a class whenever *at least one* rotation occurs. The theorem covers all positive lengths and the indicated fixed point, without assertions about other substitution words or higher-order variants of Lie complexity.

## Proof
**1. Parity and forbidden factors.** With zero-based indexing, the substitution gives \(d_{2j}=0\) and \(d_{2j+1}=1-d_j\), for every \(j\ge0\). In particular, every occurrence of \(1\) occupies an odd global position, so \(11\notin F_2\). If \(0000\) occurred at an even starting position, its two consecutive odd positions would yield \(d_j=d_{j+1}=1\); starting at an odd position likewise uses two consecutive odd global positions. Both contradict the absence of \(11\). Therefore \(0000\notin F_4\).

**2. The exact length-doubling factor identity.** For every positive integer \(m\),

\[
F_{2m}=\{h(v):v\in F_m\}\ \cup\ \{\rho(h(v)):v\in F_m\}.
\tag{1}
\]

Indeed, a length-\(2m\) factor beginning at an even global position is the substitution of the corresponding \(m\)-letter factor; one beginning at an odd position comprises a full block with its first symbol moved to the end, giving \(\rho(h(v))\). Conversely each right-hand-side word occurs, since \(v\) occurs and substituting its occurrence provides both respective length-\(2m\) windows. (The odd-start window uses the initial symbol of the following block, which is always \(0\), equal to the first symbol of \(h(v)\).)

**3. Exact bijection of admissible conjugacy classes.** If \([v]\subseteq F_m\), then every even rotation of \(h(v)\) is \(h(\rho^j(v))\), and every odd rotation is \(\rho(h(\rho^j(v)))\). By (1), all occur: \([h(v)]\subseteq F_{2m}\). Every length-\(2m\) factor is of one of the two forms in (1), so every fully present cyclic class at length \(2m\) is the image of a class at length \(m\) *provided the reverse implication holds*.

For \(m\ge2\), a factor \(v\in F_m\) must contain a \(0\), since \(11\) is forbidden. Therefore \(h(v)\) contains a \(1\), all of whose occurrences lie at odd positions of its length-\(2m\) block. On the other hand, every \(\rho(h(u))\) has all its \(1\)'s at even positions. Hence, if the even rotation \(h(\rho^j(v))\) occurs in \(F_{2m}\), identity (1) forces it to be \(h(u)\) for some \(u\in F_m\). The substitution is injective on words, so \(\rho^j(v)=u\in F_m\). Thus \([h(v)]\subseteq F_{2m}\) implies \([v]\subseteq F_m\).

For injectivity on conjugacy classes, if \(h(v')\) and \(h(v)\) are cyclically conjugate, the parity of positions containing \(1\) again forces the conjugating shift to be even (for \(m\ge2\)). Dividing the even shift by two and applying injectivity of \(h\) shows that \(v'\) and \(v\) are cyclically conjugate. At \(m=1\), the two classes \([0]\), \([1]\) map to the two distinct classes \([01]\), \([00]\), and the same conclusion holds. Thus

\[
[v]\longmapsto[h(v)]\quad\text{is a bijection }\mathcal C_m\overset{\sim}{\longrightarrow}\mathcal C_{2m},\qquad L_d(2m)=L_d(m).
\tag{2}
\]

**4. Odd lengths.** Fix odd \(n\ge5\) and suppose \([w]\subseteq F_n\). All occurrences of \(1\) in \(w\) lie in the same parity class, because it is a factor of \(d\). If \(w\) contains at least two \(1\)'s at positions \(i<j\), then \(j-i\) is even. Rotate at a cut strictly between these two occurrences. Their new positional difference, taken across the cut, is \(n-(j-i)\), which is odd. The rotated word then has \(1\)'s in opposite parity classes and cannot be a factor. Hence \(w\) has at most one \(1\). If it has none, it contains \(0000\); if it has one, a rotation contains \(0^{n-1}1\), again containing \(0000\). Both are impossible. Therefore \(\mathcal C_n\) is empty and \(L_d(n)=0\) for all odd \(n\ge5\).

**5. Two base lengths and final classification.** Both letters occur, so \(\mathcal C_1=\{[0],[1]\}\). The complete set of length-three factors, obtainable from the prefix \(01000101\) together with the forbidden \(11\), is

\[
F_3=\{000,001,010,100,101\}.
\]

The only fully present length-three conjugacy classes are \([000]\) and \([001]=\{001,010,100\}\); the class of \(101\) includes the forbidden word \(011\). Thus \(L_d(1)=L_d(3)=2\). Every positive integer is uniquely an odd integer times a power of two. Iterating (2), together with the odd-length classification, gives the displayed formula and the explicit representatives. This proves all assertions.

## Verification
The accompanying standalone `verify_period_doubling_lie.py` independently enumerates the factors in two nested fixed-point prefixes, computes complete conjugacy orbits, and checks the formula at every \(1\le n\le192\). For all 96 even lengths in that range it additionally checks identity (1) and the bijection on fully present conjugacy classes. The checker compares factor sets in prefixes of lengths \(2^{14}\) and \(2^{15}\), so its observations are bounded computations, not a proof of factor-set stabilization or of the infinite theorem. The five-step symbolic proof above supplies the all-length guarantee. Execute the verification using Python 3 and the standard library:

```sh
python3 verify_period_doubling_lie.py
```

## Relationship to prior work
Bell and Shallit introduced Lie complexity, proved general boundedness results and automaticity for automatic words, and computed explicit examples (Thue–Morse, Cantor, Fibonacci, Tribonacci, and others), without this period-doubling formula [1]. Cassaigne, Fici, Sciortino and Zamboni studied the *different* cyclic complexity invariant and proved that the period-doubling word has exactly two nonempty circular classes represented among factors at powers-of-two lengths [2, Proposition 17 and Example 1]. That concerns classes with at least one factor present, rather than classes with **every** rotation present, and gives neither the full Lie spectrum nor its renormalization bijection. Li investigated Lie and extended Lie complexity and Rauzy-graph structures, without this exact period-doubling result [3]. De Luca and Fici obtained an exact Lie-complexity formula for Sturmian words, a different family [4].

The present formula also has support overlapping some values of Bell–Shallit's *Thue–Morse* example, but the words, resulting multiplicities, and constructive conjugacy classes are different. Shared support alone does not imply this exact statement.

## Limitations
This is a self-review, not independent validation. The literature comparisons cover the explicitly inspected accessible primary sources and targeted mathematical-record searches; equivalent formulations in additional publications, software, or unindexed results remain an originality risk. The finite checks through length 192 are supportive only; the complete infinite conclusion rests on the substitution and parity proof. No assertion is made about arbitrary morphic sequences or other cyclic-complexity variants.

## References
[1] J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821 (first publicly submitted 7 February 2021), https://arxiv.org/abs/2102.03821 .

[2] J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, https://arxiv.org/abs/1402.5843 .

[3] S. Li, *A Note on the Lie Complexity and Beyond*, arXiv:2207.05859, https://arxiv.org/abs/2207.05859 .

[4] A. De Luca and G. Fici, *On the Lie Complexity of Sturmian Words*, arXiv:2206.00995, https://arxiv.org/abs/2206.00995 .
