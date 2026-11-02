# Exactly \(24\) orientation-distinguishable ternary windows over a four-symbol position code

## Finding

The maximum possible period of a negative orientable sequence of order \(3\) over \(\mathbb Z_4\) is exactly \(24\). Equivalently, a circular four-symbol position code in which each three-symbol window unambiguously distinguishes position even when the observation may be reversed and additive-negated modulo \(4\) has at most \(24\) positions, and this is attained by the explicit circular word `003122113232010233313033`.

## Assumptions and scope

The alphabet is \(\mathbb Z_4=\{0,1,2,3\}\), with addition modulo \(4\). For a triple \(e=(a,b,c)\), let \(\tau(e)=(-c,-b,-a)\). A cyclic word of period \(m\) is **negative orientable of order three** if its \(m\) cyclic triples are distinct, no triple is fixed by \(\tau\), and no two triples are exchanged by \(\tau\). Its period is its number of indexed positions. The forbidden self-negative-reversed triples are excluded even when the positions are the same. The reported maximum is for this precise error-free, length-three position-identification condition.

## Proof

**1. The quotient graph.** For every nonfixed triple, pair \(e\) and \(\tau(e)\); these are \(28\) two-element orbits, because among the \(64\) ternary words, exactly \(8\) satisfy \(e=\tau(e)\). Similarly, length-two words under \(\tau(a,b)=(-b,-a)\) form \(10\) orbits. Construct an undirected multigraph \(H\) on these \(10\) vertices, with one edge for every nonfixed triple orbit and endpoints represented by the prefix and suffix two-letter orbits. This is well-defined since applying \(\tau\) reverses the two endpoints. A quotient loop contributes two to its vertex degree.

For every allowable cyclic position code, consecutive triple windows overlap in two symbols. Therefore its selected quotient edges form a closed walk in \(H\). No quotient edge is used twice, by negative orientability. Thus the selected edges form an Eulerian multigraph, so all their vertex degrees are even.

Direct enumeration of the explicitly defined \(28\) edge orbits gives exactly six odd-degree vertices in \(H\), represented by
\[
(0,0),\ (0,1),\ (0,3),\ (1,2),\ (2,1),\ (2,2).
\]
The other four vertices have even degree. This degree calculation can also be obtained from the directed degree counts \(4-\mathbf 1_{\{b=0\text{ or }2\}}\) leaving \((a,b)\), and \(4-\mathbf 1_{\{a=0\text{ or }2\}}\) entering \((a,b)\), for nonfixed triples, after quotienting.

**2. Parity eliminates periods above \(25\).** Any omitted edges must change the degree parity of all six odd vertices, so at least three quotient edges must be omitted. Hence \(m\le25\). In the equality case, the three omitted edges must constitute a perfect matching of the six odd vertices. Enumerating the ten edges between distinct odd vertices gives only two such matchings, identified by their lexicographically least triple representatives:
\[
A=\{001,032,122\},\qquad B=\{003,012,221\}.
\]
Here `001` denotes the triple \((0,0,1)\), not an integer. The complete enumeration and these two matchings are independently reproducible by `verify_nos.py`.

**3. An orientation-independent flux obstruction rules out \(25\).** For any two-letter word \(v\) not fixed by negative reversal, define
\[
p_v(z)=\begin{cases}1&z=v,\\-1&z=\tau(v),\\0&\text{otherwise},\end{cases}
\qquad
\phi_v(a,b,c)=p_v(a,b)-p_v(b,c).
\]
Since \(p_v(\tau z)=-p_v(z)\), one checks \(\phi_v(\tau e)=\phi_v(e)\), so \(\phi_v\) is unambiguously associated with a quotient edge. For a cyclic sequence, the sum of \(\phi_v\) over its directed triples telescopes to \(0\), and thus the sum over its distinct quotient edges is also \(0\).

Let \(E\) be all \(28\) quotient edges. By the fixed-triple exclusion and the directed input/output counts from Step 1, for \(v=(a,b)\) not fixed by \(\tau\),
\[
\sum_{e\in E}\phi_v(e)
=\mathbf 1_{\{a\in\{0,2\}\}}-\mathbf 1_{\{b\in\{0,2\}\}}.
\]
For omission matching \(A\), choose \(v=(1,2)\). The complete sum is \(-1\), whereas the three omitted edges contribute \(0+0+1=1\), leaving sum \(-2\ne0\). For matching \(B\), choose \(v=(0,3)\). The complete sum is \(+1\), whereas its omitted edges contribute \(-1+0+0=-1\), leaving sum \(+2\ne0\). Both cases contradict the telescoping condition. Hence \(m\le24\).

**4. Attainment.** For the cyclic word `003122113232010233313033` of length \(24\), direct inspection of all its \(24\) length-three cyclic windows confirms that every window is nonfixed under \(\tau\), and no two windows belong to the same \(\tau\)-orbit. This gives \(m\ge24\), completing the proof.

## Verification

Run `python3 verify_nos.py` from the directory containing that file. It constructs the \(28\)-edge, \(10\)-vertex graph without reference tables, computes degrees and all odd-vertex perfect matchings, evaluates both flux obstructions, and checks every cyclic window of the explicit witness. The accompanying `verification_output.txt` records the actual successful run. The proof of the infinite optimization claim relies on Steps 1–4; enumeration is exhaustive over an explicit \(64\)-triple finite universe, not a truncated search over cyclic words. No nonlinear solver result is needed.

## Relationship to prior work

Mitchell and Wild, *New upper bounds for the period of a negative orientable sequence*, first posted February 4, 2026, report \(22\) as the largest known period for the four-symbol, order-three case and \(26\) as their upper bound, and identify this as the smallest open instance. Their subsequent *Constructing orientable and negative orientable sequences with asymptotically optimal period* (first posted March 19, 2026) provides constructions, not an exact maximum \(24\) for this case. Earlier constructions by Alhakim and collaborators give relevant general background. The present theorem provides both a longer circular position code and a tight quotient-parity/flux upper bound. The reversal-only orientability condition is different from negative-reversal orientability and does not imply this theorem.

## Limitations

The result is limited to a four-symbol alphabet, exact three-symbol windows, and the indicated reversal-and-negation ambiguity. It does not enumerate all optimal words, handle noisy windows, or give sharp maxima for other alphabet sizes or window lengths. Literature searching cannot rule out unpublished or unindexed prior discoveries. Independent mathematical audit has not been performed.

## References

1. C. J. Mitchell and P. R. Wild, *New upper bounds for the period of a negative orientable sequence*, arXiv:2602.04433, first public February 4, 2026; https://arxiv.org/abs/2602.04433.
2. C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646, first public March 19, 2026; https://arxiv.org/abs/2603.18646.
3. *Constructing orientable sequences*, arXiv:2409.00672, first public September 2024; https://arxiv.org/abs/2409.00672.
