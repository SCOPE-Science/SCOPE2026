# Parity-induced oscillation collapse on whiskered cliques

## Finding

For every integer \(n\ge2\), let \(H_n=K_n\circ K_1\) be the labelled graph obtained by attaching one private leaf to each vertex of a complete graph on \(n\) vertices. In synchronous binary open-neighbor majority dynamics, each vertex adopts the strict majority of its neighbors' current bits, and retains its bit in a tie. Let \(F_n\) denote one simultaneous update. Then
\[
F_n^5=F_n^3.
\]
All recurrent states have primitive period one or two, and the maximum first-periodic-entry time is two for \(n=2,3\) and three for every \(n\ge4\).

For even \(n=2m\), put \(B=\binom{2m}{m}\). The exact numbers of labelled fixed points and primitive temporal two-cycle orbits are
\[
Q_1=B+2,\qquad Q_2=\frac{B(B-1)}2.
\]
There are two homogeneous fixed points, each with an attraction basin of size \((4^n-B^2)/2\); the other \(B\) fixed points have singleton basins; and every two-cycle orbit has a basin of size two.

For odd \(n=2m+1\ge3\), put \(B=\binom{2m+1}{m}\). Then
\[
Q_1=2,\qquad Q_2=B(m+2).
\]
Each two-cycle orbit has an attraction basin of size \(2^{m+1}\), while each of the two homogeneous fixed points has a basin of size
\[
\frac{4^n-2^{m+1}B(m+2)}2.
\]
In particular, under uniform random initialization, the probability of eventual **genuine** two-cycle oscillation has an abrupt parity-dependent asymptotic:
\[
\mathbb P_{n\,\mathrm{even}}(\mathrm{period}\ 2)\sim\frac{2}{\pi n},\qquad
\mathbb P_{n\,\mathrm{odd}}(\mathrm{period}\ 2)\sim\sqrt{\frac{n}{\pi}}\,2^{-n/2}.
\]
Thus oscillatory basins have polynomial probability in the even subsequence but exponentially small probability in the odd subsequence.

## Assumptions and scope

The core vertices are \(v_1,\ldots,v_n\), with all core-core edges present. The leaf \(w_i\) is adjacent only to \(v_i\). Configurations are pairs \((c,\ell)\) of binary vectors of length \(n\), recording core and leaf bits. Write \(|c|\) for the Hamming weight and \(\overline c\) for bitwise complementation; set union, intersection, and set difference are taken coordinatewise on the support sets. A primitive temporal orbit is counted up to cyclic time shift, *not* up to graph automorphisms. An attraction basin includes the orbit itself and consists of every initial configuration eventually reaching it. The first-periodic-entry time is the least nonnegative integer \(t\) for which \(F_n^t(c,\ell)\) is periodic.

## Proof

**Exact one-step reduction.** Every leaf copies its core neighbor, so \(F_n(c,\ell)=(h(c,\ell),c)\). A core vertex currently carrying \(c_i\) sees \(|c|-c_i+\ell_i\) occupied neighbors among its \(n\) neighbors.

When \(n=2m\), strict majority with tie retention simplifies, for *both* values of \(c_i\), to the rule that the new bit is one exactly when \(|c|+\ell_i\ge m+1\). Consequently,
\[
h(c,\ell)=\begin{cases}
\mathbf0&|c|<m,\\
\ell&|c|=m,\\
\mathbf1&|c|>m.
\end{cases}
\]
When \(n=2m+1\), a direct two-case check gives
\[
h(c,\ell)=\begin{cases}
\mathbf0&|c|<m,\\
\overline c\cap\ell&|c|=m,\\
\overline c\cup(c\cap\ell)&|c|=m+1,\\
\mathbf1&|c|>m+1.
\end{cases}
\]
These are identities for every labelled binary configuration, with no probabilistic assumption.

**Even-core dynamics.** If \(|c|\ne m\), the next core vector is homogeneous, and the entire graph is homogeneous after at most one additional update. If \(|c|=m\), the first state becomes \((\ell,c)\). If also \(|\ell|=m\), the two vectors are exchanged forever. Otherwise the next core becomes homogeneous and the complete state becomes homogeneous by the third update. Hence the periodic nonhomogeneous states are precisely the ordered pairs of balanced core and leaf vectors. There are \(B^2\) such states, including \(B\) diagonal fixed points; the off-diagonal pairs form \((B^2-B)/2\) two-cycles. None of these states has a nonperiodic preimage, since the output leaf must already be balanced and the output core must be the former leaf. Thus all their basins consist exactly of their one or two periodic states. The remaining \(4^n-B^2\) states enter one of the two homogeneous fixed points; complementation exchanges their basins, so each has size \((4^n-B^2)/2\).

**Odd-core dynamics.** Let \(m\ge1\). An initial core of weight outside \(\{m,m+1\}\) becomes homogeneous in one update, followed by a homogeneous full configuration at the next. If \(|c|=m\), the successor core \(b=\overline c\cap\ell\) is disjoint from \(c\), with \(|b|\le m+1\). Whenever \(|b|\in\{m,m+1\}\), applying the displayed odd-core rule to \((b,c)\) returns core vector \(c\): if \(|b|=m\), then \(c\subseteq\overline b\); if \(|b|=m+1\), then \(b=\overline c\). If instead \(|b|<m\), it becomes homogeneous and the full configuration reaches a fixed point by the third update. Similarly, if \(|c|=m+1\), the successor core \(b=\overline c\cup(c\cap\ell)\) covers the complement of \(c\), with \(|b|\ge m\). If \(|b|=m\) or \(m+1\), the next core is again \(c\); otherwise the core becomes homogeneous and the full state reaches a fixed point within three updates. These observations prove \(F_n^5=F_n^3\) and characterize all periodic states without invoking the general period-two theorem.

For odd \(n\), two nonhomogeneous phase vectors \(c,b\) form a two-cycle precisely when one of four disjoint cases holds: (i) both weights equal \(m\) and their supports are disjoint; (ii) both weights equal \(m+1\) and their supports cover all indices; (iii) \(|c|=m, |b|=m+1\) and \(b=\overline c\); (iv) the reverse mixed-weight case. Cases (i) and (ii) contribute \(B(m+1)\) ordered periodic states each, while the mixed cases contribute \(B\) each. The resulting \(2B(m+2)\) periodic states form \(B(m+2)\) two-cycle orbits. There are no nonhomogeneous fixed points because each nonhomogeneous phase must either invert or vacate at least one occupied core bit. The only fixed points are homogeneous.

For a specified odd-core periodic target \((b,c)\), its preimage must have core exactly \(c\). In the small-weight case, the condition \(h(c,\ell)=b\) determines all leaf bits outside \(c\) but leaves its \(m\) inside bits arbitrary. In the large-weight case it determines the bits inside \(c\) while leaving the \(m\) outside bits arbitrary. Hence each periodic target has exactly \(2^m\) preimages, one of which is the predecessor on its two-cycle. Every nonperiodic preimage immediately enters that orbit; no path of length two or more enters a two-cycle because every state whose next core has intermediate weight is already periodic after that update. Thus each two-cycle orbit has exactly \(2^{m+1}\) basin states. Complementation exchanges the two homogeneous basins and all remaining states belong to them, giving the stated sizes.

**Sharp uniform entrance times.** For \(n\ge4\), take an initial core containing exactly \(\lfloor n/2\rfloor\) occupied sites and put a single occupied leaf outside that core, if \(n\) is odd; for even \(n\), put a single occupied leaf anywhere. The initial update leaves exactly one occupied core bit, the second produces zero core bits but a nonzero leaf vector, and the third reaches the all-zero state. Its least periodic entry time is therefore three. For \(n=2,3\), the intermediate noncritical core cannot be nonhomogeneous; the earlier cases give an upper bound of two, attained by an initial intermediate core with leaf bits chosen so that the first successor core is homogeneous but the leaf vector is not.

**First-entry-time census.** Writing \(E_t\) for the number of labelled initial configurations with first periodic entry at time \(t\), all \(E_t\) vanish for \(t>3\). For \(n=2m\), \(B=\binom nm\), the complete distribution is
\[
\begin{aligned}
E_0&=B^2+2, &E_1&=2(2^n-1),\\
E_2&=2B+(2^n-B-2)2^n, &E_3&=B(2^n-B-2).
\end{aligned}
\]
For \(n=2m+1\ge3\), \(B=\binom nm\), \(Q=B(m+2)\), it is
\[
\begin{aligned}
E_0&=2+2Q,\\
E_1&=2(2^n-1)+2Q(2^m-1),\\
E_2&=(2^n-2-2B)2^n+2B2^m,\\
E_3&=2B\bigl(2^n-2^m(m+3)\bigr).
\end{aligned}
\]
To count these, distinguish initially homogeneous, intermediate, and off-intermediate core weights. For even cores the balanced-pair swap condition gives \(E_0\); homogeneous cores with arbitrary nonmatching leaf vectors give \(E_1\); all remaining off-intermediate cores and the intermediate cores with homogeneous leaf vectors give \(E_2\); intermediate cores with nonhomogeneous off-intermediate leaf vectors give \(E_3\). For odd cores, each of the \(2Q\) periodic two-cycle states has exactly \(2^m\) immediate preimages; subtract its unique periodic predecessor to obtain the two-cycle contribution to \(E_1\). The other contributions follow from the two odd-core boundary formulas, which have exactly \(2B2^m\) initial states mapping to a homogeneous core on the first update. The displayed distributions add to \(4^n\).

Finally, the oscillation probabilities are \(B(B-1)/4^n\) for even \(n\) and \(2^{m+1}B(m+2)/4^n\) for odd \(n\). Stirling's estimate for the central binomial coefficient yields the two asserted subsequential asymptotics.

## Verification

Two standalone programs are provided. The C++17 program `verify_corona.cpp` constructs all graph-neighbor lists independently of the reduction above, builds the entire finite-state transition graph, identifies cycles by indegree peeling, and tests all orbit, basin, first-entry and iterate-identity predictions for every \(2\le n\le10\). The Python program `verify_compressed.py` independently builds a direct compressed update and solves the resulting functional graph for every \(2\le n\le8\). Reproduce by running:

```sh
c++ -std=c++17 -O2 verify_corona.cpp -o verify_corona
./verify_corona 10
python3 verify_compressed.py
```

Their captured outputs appear in `cpp_verification.txt` and `python_verification.txt`. The C++ test enumerates \(\sum_{n=2}^{10}4^n=1{,}398{,}096\) labelled initial configurations. Neither finite enumeration nor a prior period-two theorem is used to extend the proof beyond the tested sizes; the exact one-step formulas and their case analysis establish the result for every integer \(n\ge2\).

## Relationship to prior work

Goles and Olivos (1980) established the period-at-most-two property for symmetric threshold dynamics on arbitrary finite graphs. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, 11 May 2014) restate that theorem and study majority behavior on unimodular and random graphs, not exact recurrence on a fully whiskered clique. Turau (arXiv:2202.01580v1) characterizes fixed points and two-cycles on trees; it applies to the special case \(n=2\) here but not to the complete-graph corona family of arbitrary order. The present exact parity-dependent orbit and basin formulas, sharp uniform time bound and polynomial-versus-exponential distinction are not consequences of those general period restrictions. An equivalent, less easily indexed historical treatment of whiskered complete graphs is still possible.

## Limitations

The result is specifically for synchronous binary, open-neighborhood majority with retention on ties and one private leaf per core vertex. Different tie rules, asynchronous updates, multiple leaves per core vertex or a core other than a complete graph are not classified. The formulas count labelled configurations and temporal orbits; there is no quotient by spatial symmetry. The finite checks corroborate but do not themselves prove the all-order statements. The historical priority assessment is based on the accessible literature and search records, not a guarantee of novelty; the original 1980 article was not available in full text through the authorized access route.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, publicly posted 11 May 2014, later Stochastic Processes and their Applications **126** (2016), 2719–2733.
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1, posted 3 February 2022.
