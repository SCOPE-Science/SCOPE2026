# Exact equilibrium enumeration on squared-cycle public-goods networks

## Finding

Let \(G_n=C_n^2\), the graph with vertex set \(\mathbb Z/n\mathbb Z\) and edges joining vertices at cyclic distance one or two, for any integer \(n\ge5\). In the homogeneous strict binary public-goods game with best response \(T(k)=1\) exactly for \(k\in\{0,2\}\), write \(E_n\) for the number of pure Nash equilibria, counting strategies at labeled vertices separately. Then

\[
E_n=10\mathbf1_{5\mid n}+\sum_{\substack{a,b\ge0\\3a+5b=n}}\frac{n}{a+b}\binom{a+b}{a}.
\]

In particular, \(E_5=15\), \(E_6=3\), \(E_7=0\), and **every \(G_n\) with \(n\ge8\) has a pure Nash equilibrium**. Thus among these squared cycles, the seven-vertex graph is the unique obstruction. The exact ordinary generating function is

\[
\sum_{n\ge5}E_n z^n=\frac{10z^5}{1-z^5}+\frac{3z^3+5z^5}{1-z^3-z^5}-3z^3.
\]

The subtraction removes the formal length-three closed walks, since the distinct four-neighbor model is defined here only for \(n\ge5\). Moreover \(E_n\sim\rho^n\), where \(\rho=1.193859111321\ldots\) is the unique positive root of \(\rho^5-\rho^2-1=0\). Thus the labeled equilibrium set has positive exponential growth rate despite the isolated forbidden order seven.

## Assumptions and scope

The graph is finite, simple, undirected, and has exactly the four neighbors \(i-2,i-1,i+1,i+2\) at each vertex (indices modulo \(n\)); the restriction \(n\ge5\) makes these four neighbors distinct. Each agent chooses a binary action \(x_i\in\{0,1\}\) and has the **unique** best response \(T(k)=1\) if the number of active neighbors \(k\) equals zero or two, and \(T(k)=0\) otherwise. An equilibrium is exactly a cyclic binary word satisfying

\[
x_i=\mathbf1_{\{0,2\}}(x_{i-2}+x_{i-1}+x_{i+1}+x_{i+2})\qquad(i\in\mathbb Z/n\mathbb Z).
\]

The statement concerns pure (not mixed) Nash equilibria; no dynamics or convergence of asynchronous best responses is asserted. All formulas count vertex-indexed strategy profiles, not equivalence classes under rotation.

## Proof

**1. A complete finite-state encoding.** For four bits \((a,b,c,d)\), write a directed edge from state \(abcd\) to state \(bcde\), with \(e\in\{0,1\}\), precisely when

\[c=\mathbf1_{\{0,2\}}(a+b+d+e).\]

Every equilibrium word of length \(n\ge5\) gives the closed walk of length \(n\) whose consecutive states are \((x_{i-2},x_{i-1},x_i,x_{i+1})\). Conversely, the overlapping four-bit states on any indexed closed walk recover one and only one such cyclic equilibrium word. Hence \(E_n=\operatorname{tr}(A^n)\), where \(A\) is the sixteen-state adjacency matrix.

**2. Exact decomposition of the state graph.** Direct evaluation of the preceding five-bit condition yields the following complete list of nontrivial directed components, expressed by states as four-digit binary strings. There are two isolated directed five-cycles:

```
0000 -> 0001 -> 0010 -> 0100 -> 1000 -> 0000
0011 -> 0111 -> 1110 -> 1100 -> 1001 -> 0011
```

The five remaining recurrent states have all and only the edges

```
0110 -> 1101
1101 -> 1011 and 1010
1011 -> 0110
1010 -> 0101
0101 -> 1011
```

The sole remaining state, `1111`, has no outgoing edge. The third component has two simple directed cycles: one of length three and another of length five; they share vertices, so they cannot occur as disjoint cycles in a determinant expansion. Its adjacency matrix \(B\) therefore obeys \(\det(I-zB)=1-z^3-z^5\). The other two components each contribute \(\det(I-zB_j)=1-z^5\). Therefore

\[\det(I-zA)=(1-z^5)^2(1-z^3-z^5).\]

**3. Count the closed walks.** As a formal power-series identity for a finite adjacency matrix,

\[
\sum_{n\ge1}\operatorname{tr}(A^n)z^n
=-z\frac{d}{dz}\log\det(I-zA)
=\frac{10z^5}{1-z^5}+\frac{3z^3+5z^5}{1-z^3-z^5}.
\]

Expanding \(-\log(1-z^3-z^5)=\sum_{k\ge1}(z^3+z^5)^k/k\) and differentiating gives, for each \(n\ge1\), the coefficient \(\sum_{3a+5b=n} n\binom{a+b}{a}/(a+b)\) for the nontrivial five-state component. The two directed five-cycles contribute \(10\) if \(5\mid n\), and zero otherwise. This proves the displayed count for every \(n\ge5\). The first nonzero term from the third component is \(3z^3\), which is excluded from the restricted \(n\ge5\) generating function, giving the stated subtraction.

**4. Existence cutoff and growth.** The coefficient is strictly positive if and only if \(n=3a+5b\) for nonnegative integers \(a,b\), not both zero. For \(n\ge5\), precisely \(n=7\) is not of this form: positive representations are given by multiples of three, by \(5+3a\), and by \(10+3a\), covering all orders \(n\ge8\) and also \(n=5,6\). Finally the five-state component is irreducible with directed cycle lengths three and five, whose greatest common divisor is one. Its Perron root \(\rho>1\) is simple and strictly dominates its remaining eigenvalues; the determinant gives \(\rho^5-\rho^2-1=0\). The contributions of the two five-cycles are bounded. Thus \(E_n/\rho^n\to1\), as asserted.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently rebuilds all sixteen transition rows from the original five-bit condition; matches them with the explicit component decomposition; compares exact transfer-matrix traces and binomial coefficients through order 120; and exhaustively checks every one of the \(2^n\) strategy profiles for each \(5\le n\le17\). Every check passes. Exhaustive finite checking supplements, but does not replace, the universal generating-function proof above.

## Relationship to prior work

Klimm and Stahlberg [1] formulate strict binary public-goods games by best-response patterns and prove that equilibrium existence is NP-complete for the picky pattern \(T=10100\ldots\) on arbitrary undirected graphs. Their result is a worst-case complexity theorem and does not supply this exact squared-cycle equilibrium count. Gilboa [2] independently gives a general hardness classification and discusses the simpler ordinary cycle, not its square. Gilboa and Nisan [3] develop related pattern-complexity theory. Koller, Behrens, and Zdeborová [4] study typical fixed-point counts of outer-totalistic rules on random regular graphs, not an exact finite-size formula for deterministic squared cycles. The finite-state argument here is standard in symbolic dynamics, but the explicitly evaluated spectrum, exceptional order, and count in this precise strategic model are not consequences of the cited general complexity results without additional analysis.

## Limitations

This result is specific to the four-neighbor squared-cycle graph and the strict \(0\)-or-\(2\) response rule. It does not establish the same enumeration for arbitrary four-regular graphs, other response patterns, or dynamics. Published and indexed literature was searched for matching fixed-point or periodic-word counts; unindexed equivalent symbolic-dynamics enumerations remain possible. The source theory concerns pure equilibria, so there is no claim about selection or learning.

## References

1. M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849 (first public version 2023-01-27); https://arxiv.org/abs/2301.11849.
2. M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580 (2023); https://arxiv.org/abs/2301.11580.
3. M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238 (2022); https://arxiv.org/abs/2207.04238.
4. C. Koller, F. Behrens, and L. Zdeborová, *Counting and Hardness-of-Finding Fixed Points in Cellular Automata on Random Graphs*, arXiv:2406.01710 (2024); https://arxiv.org/abs/2406.01710.
