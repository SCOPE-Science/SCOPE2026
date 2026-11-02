# Exact shortest cyclic binary covers for all four-bit forbidden factors through order \(15\)

## Finding

For a forbidden word \(p\in\{0,1\}^4\) and an integer \(n\ge4\), define \(A_{p,n}\) to be the set of all *finite* binary words of length \(n\) that have no occurrence of \(p\) as an ordinary (non-wrapping) substring. Let \(L_p(n)\) be the minimum positive length of a *single circular* binary word in which every member of \(A_{p,n}\) occurs as a cyclic window. Windows outside \(A_{p,n}\), as well as repeated windows, are allowed.

**Theorem.** For every \(p\in\{0,1\}^4\) and every \(4\le n\le15\), \(L_p(n)\) is given by the table below. Columns are representatives of the six classes under bit complementation and reversal.

| Order \(n\) | `0000` | `0001` | `0010` | `0011` | `0101` | `0110` |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 15 | 16 | 16 | 16 | 16 | 16 |
| 5 | 30 | 32 | 32 | 32 | 30 | 32 |
| 6 | 60 | 64 | 61 | 64 | 60 | 61 |
| 7 | 120 | 124 | 118 | 124 | 120 | 118 |
| 8 | 236 | 242 | 229 | 238 | 232 | 226 |
| 9 | 467 | 470 | 444 | 452 | 448 | 434 |
| 10 | 922 | 908 | 856 | 852 | 870 | 829 |
| 11 | 1816 | 1752 | 1645 | 1598 | 1682 | 1580 |
| 12 | 3572 | 3372 | 3153 | 2986 | 3238 | 3001 |
| 13 | 7018 | 6476 | 6031 | 5564 | 6226 | 5687 |
| 14 | 13771 | 12416 | 11513 | 10346 | 11954 | 10753 |
| 15 | 26992 | 23764 | 21939 | 19206 | 22908 | 20296 |


The symmetry classes are `0000`/`1111`; `0001`/`1000`/`0111`/`1110`; `0010`/`0100`/`1011`/`1101`; `0011`/`1100`; `0101`/`1010`; and `0110`/`1001`. These six classes exhaust all sixteen forbidden four-bit words.

At order \(15\), the number of *required* windows for the six representative classes, in the table's column order, is \((20569,12640,14305,12640,15796,14305)\). Their minimum total cover lengths are \((26992,23764,21939,19206,22908,20296)\). In particular, the shortest-cover ordering is not a simple ordering by the population of the forbidden-word language: the supplementary Eulerian augmentation is essential.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The forbidden pattern has length exactly four; a forbidden occurrence inside a *required* word is tested without wrap-around. The covering word itself is circular and may contain any four-bit pattern. There is no requirement that the covering word avoid \(p\), nor any restriction on repeated windows. One covering circle—not a family of circles—is optimized. The theorem makes 72 exact numerical assertions, one for each representative pattern and order, and extends to the other ten patterns by reversal and complementation.

## Proof

**1. de Bruijn reduction.** Fix \(p,n\). Let \(V=\{0,1\}^{n-1}\). The complete directed binary de Bruijn graph has an arc \((u,t)\) for every \(u\in V\) and \(t\in\{0,1\}\), going from \(u\) to the suffix of length \(n-1\) of \(ut\). The arc corresponds to the length-\(n\) word \(ut\). Let \(R\) be the set of arcs corresponding to \(A_{p,n}\). For each \(v\in V\), put

\[
b(v)=\deg_R^+(v)-\deg_R^-(v).
\]

Every covering circle induces a closed de Bruijn walk with every arc of \(R\) traversed at least once. After subtracting one copy of every required arc, its nonnegative additional traversal multiplicities \(x(e)\) satisfy

\[
\sum_{e\,\mathrm{out\ of}\,v}x(e)-\sum_{e\,\mathrm{into}\,v}x(e)=-b(v).
\]

Its length is \(|R|+\sum_e x(e)\).

**2. Exact lower bound from integer potentials.** If \(\pi:V\to\mathbb Z\) obeys \(\pi(\mathrm{head}(e))-\pi(\mathrm{tail}(e))\le1\) on *every* arc of the complete graph, then the flow equations give

\[
\sum_e x(e)\ge\sum_e x(e)\bigl(\pi(\mathrm{head}(e))-\pi(\mathrm{tail}(e))\bigr)=\sum_{v\in V}b(v)\pi(v).
\]

This bound applies to all covering circles, regardless of their supplementary windows or repeated factors.

**3. Exact upper bound and equality.** The self-contained integer data in `certificates.json` specify, for each of the 72 cases, (i) every positive supplementary arc multiplicity \(x(e)\), encoded by its starting vertex and appended bit, and (ii) an integer potential \(\pi(v)\) on every vertex. The standalone `verify.py` reconstructs \(R\) directly from the forbidden-word definition and checks, without calling an optimizer, all flow equations, the potential inequalities on every binary de Bruijn arc, and the exact equality

\[
\sum_e x(e)=\sum_v b(v)\pi(v).
\]

The checker also verifies that the support of \(R+x\) is strongly connected. Thus \(R+x\) is a connected balanced directed multigraph and has an Euler tour. The checker explicitly reconstructs one such tour for every case and confirms that its cyclic emitted-bit windows contain every required word. Hence the lower and upper bounds coincide. For each certificate the verified value of \(|R|+\sum_e x(e)\) is precisely the table entry.

**4. Six symmetry classes.** Complementation carries each required word and every covering circle to its bitwise complement. Reversal carries a circular covering word and all its cyclic windows to their reversals. Both operations preserve length and induce bijections between admissible covers, so the six representative classes prove the result for all sixteen patterns.

## Verification

Use only Python's standard library; no solver, network package, or external data is needed for checking. In the same directory run:

```sh
python3 verify.py certificates.json
python3 check_small.py certificates.json
```

The first program independently reconstructs all 72 required languages and primal/dual certificates, verifies strong connectivity, constructs all 72 Eulerian circles, and verifies the actual cyclic window coverage. It prints `VERIFY_OK 72 exact optima`. The second exhausts all indexed binary circles at orders of circular length \(15\) and \(16\) to cross-check the six order-four minima; it prints `CROSSCHECK_OK`. The finite verification is a complete proof only for \(4\le n\le15\), not an extrapolation.

## Relationship to prior work

Moreno and Matamala's 2007 preprint studies lexicographic minimization of an exactly-once de Bruijn sequence in the language of an irreducible subshift of finite type. Its definition of a word in the language involves periodic admissibility; it does not establish the length-minimal single-circle superstrings allowing extra factors for all ordinary finite avoiding words. Cazaux and Rivals' 2016 accepted manuscript gives a general algorithm for a shortest *collection* of cyclic strings and characterizes circumstances where one cyclic string is also optimal; it does not give this six-class, 72-value classification or its integer certificates. General Chinese-postman methods explain the optimization framework, but they are not explicit evaluations of these finite invariants. All comparisons concern mathematical implications rather than title overlap.

## Limitations

No order \(n\ge16\) is claimed. The theorem does not count all optimal covers or give an all-order recurrence. No restriction forbids the omitted pattern inside the covering circle itself. No general result for multiple forbidden patterns, other alphabets, or linear superstrings is asserted. Historical priority is subject to unindexed prior numerical tables or overlooked specializations of general algorithms.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695v1, first public arXiv posting 2007-11-12. https://arxiv.org/pdf/0711.1695
2. B. Cazaux and E. Rivals, *A linear time algorithm for Shortest Cyclic Cover of Strings*, accepted manuscript dated 2016-05-19, Journal of Discrete Algorithms 37 (2016), DOI:10.1016/j.jda.2016.05.001. https://www.researchgate.net/publication/303392809_A_linear_time_algorithm_for_Shortest_Cyclic_Cover_of_Strings
3. V. Kundeti, S. Rajasekaran, H. Dinh, *An Efficient Algorithm For Chinese Postman Walk on Bi-directed de Bruijn Graphs*, arXiv:1006.4828 (2010); a related but differently directed graph model. https://arxiv.org/abs/1006.4828
