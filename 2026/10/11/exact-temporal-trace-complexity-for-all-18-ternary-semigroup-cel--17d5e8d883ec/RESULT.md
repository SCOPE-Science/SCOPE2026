# Exact temporal trace complexity for all 18 ternary semigroup cellular automata

## Finding

For every rule in the 18-element classification of three-state, two-input semigroup cellular automata [1], the number of finite histories observable at a single site has an exact formula for every length. The classification determines the temporal trace entropy even where the complete spatial dynamics is very different.

| Rules \(i\) | Number \(P_i(n)\) of length-\(n\) temporal words, \(n\ge1\) | Trace entropy |
|:--|:--|:--|
| \(1\) | \(3^n\) | \(\log3\) |
| \(2,6\) | \(3\cdot2^{n-1}\) | \(\log2\) |
| \(3\) | \(3\) for \(n=1\); \(4\) for \(n\ge2\) | \(0\) |
| \(4,5\) | \(2^{n+1}-1\) | \(\log2\) |
| \(7,11,17\) | \(3\) | \(0\) |
| \(8,15\) | \(n+2\) | \(0\) |
| \(9,12,14,16,18\) | \(2n+1\) | \(0\) |
| \(10\) | \(3n\) | \(0\) |
| \(13\) | \(\binom{n+2}{2}\) | \(0\) |

The contrast between rule \(4\), which has an absorbing symbol, and its positive trace entropy is a useful warning: generic-looking stabilization does not determine worst-case temporal information capacity. Thirteen rules have polynomial or bounded trace complexity, while five have exponential trace complexity.

## Assumptions and scope

Use the exact labeled multiplication tables \(G_1,\ldots,G_{18}\) in Table 1 of [1], on the alphabet \(A=\{x,y,z\}\), and interpret their operation as \(a\odot_i b\). For each \(i\), the cellular automaton on the full two-sided shift \(A^{\mathbb Z}\) updates every position simultaneously by
\[
(F_i\xi)_j=\xi_j\odot_i\xi_{j+1}.
\]
The time trace of the origin is the one-sided infinite sequence \(\tau_i(\xi)=((F_i^t\xi)_0)_{t\ge0}\). Its image \(T_i=\tau_i(A^{\mathbb Z})\) is compact and forward-shift-invariant. For every integer \(n\ge1\), define
\[
P_i(n)=\#\{((F_i^t\xi)_0)_{0\le t<n}:\xi\in A^{\mathbb Z}\}.
\]
The trace entropy is \(h_{\mathrm{tr}}(F_i)=\lim_{n\to\infty}n^{-1}\log P_i(n)\), the ordinary topological entropy of the one-sided shift acting on \(T_i\). This is not the global topological entropy of \(F_i\) on the configuration space. No probabilistic distribution on initial states is assumed. The result includes all lengths, especially \(n=1\), and does not assume periodic boundary conditions.

## Proof

**Finite-cone and semigroup lemmas.** Because the neighborhood consists of a site and its right neighbor, the first \(n\) states at the origin depend only on the initial interval \(\xi_0,\ldots,\xi_{n-1}\). Every such finite word extends to a bi-infinite configuration. When the operation is associative and idempotent, Pascal induction on the local update yields
\[
(F^t\xi)_0=\xi_0\odot\xi_1\odot\cdots\odot\xi_t.
\]
When the operation is commutative and associative, the more general identity is the binomial product
\[
(F^t\xi)_0=\bigodot_{j=0}^t \xi_j^{\odot\binom tj},
\]
where the exponent denotes a repeated semigroup product and the factors commute. The identity follows inductively: combine the two neighboring time-\(t\) expressions and invoke Pascal's binomial identity. Neither formula assumes that an arbitrary semigroup element has an inverse.

**Free-group regimes, rules \(1,2,6\).** For \(G_1\), the table is the cyclic group of order three, with \(x\) as zero. The new input \(\xi_t\) appears with coefficient one in the time-\(t\) output, so the mapping from the input interval to its complete observed history is triangular and bijective; hence all \(3^n\) histories occur. The tables \(G_2\) and \(G_6\) factor through the parity operation on two classes: for \(G_2\), take \(\phi(x)=\phi(z)=1\), \(\phi(y)=0\), with products labeled \(y\) and \(z\); for \(G_6\), take \(\phi(x)=1\), \(\phi(y)=\phi(z)=0\), with products labeled \(z\) and \(x\). All states from time one onward belong to the resulting two-symbol group. For any fixed initial symbol, the newest freely chosen right-neighbor class controls each subsequent group output bijectively. Thus each of the three initial symbols admits exactly \(2^{n-1}\) continuation words.

**Absorber and identity with a two-element group, rules \(4,5\).** In \(G_4\), \(y\) is absorbing and \(\{x,z\}\) is the cyclic group of order two. Before the first initial \(y\) encountered in the advancing observation cone, the trace is an arbitrary binary history; afterwards it is permanently \(y\). If the binary prefix length is \(k\), with \(0\le k\le n\), all \(2^k\) binary prefixes occur by the same triangular group argument. The number is \(\sum_{k=0}^{n}2^k=2^{n+1}-1\). In \(G_5\), \(y\) is the identity and \(\{x,z\}\) is again a two-element group. The history consists of \(k\) initial symbols \(y\), followed by an arbitrary binary history of length \(n-k\). Here \(0\le k\le n\), giving \(\sum_{k=0}^n2^{n-k}=2^{n+1}-1\). The words in each description are distinct, and their constructions give both inequalities.

**Immediate stabilization, rules \(3,7,11,17\).** For \(G_3\), the only product not equal to \(z\) is \(x\odot x=y\). Every time-two observation is \(z\). When \(n\ge2\), exactly the four histories starting with \((x,y)\), \((x,z)\), \((y,z)\), and \((z,z)\) occur, each followed by \(z\)'s. For \(G_7\), the output is always \(z\) after time zero. For \(G_{11}\), the output from time one onward is \(y\) exactly when the initial symbol is \(y\), and is \(z\) otherwise. For \(G_{17}\), the initial symbol remains forever. The final three cases each have exactly three histories at every positive length.

**One switching threshold, rules \(8,9,12,14,15,16,18\).** Directly reading the corresponding multiplication tables gives the following exhaustive and attainable patterns, where each displayed power means repetition, and counts include the unchanged history. For \(G_8\), an initially \(y\) site stays \(y\) until the first other symbol, then is permanently \(z\); an initial \(x\) or \(z\) is followed only by \(z\). Hence \(n+2\) histories. For \(G_9\), an initial \(y\) persists, while either initial \(x\) or \(z\) is followed by \(z\) until the first spatial \(y\) enters, at which time it becomes \(y\) permanently; this gives \(2n+1\). For \(G_{12}\), initial \(x\) and \(z\) each have one permanently \(z\) future; initial \(y\) can remain \(y\), switch directly to \(z\), or display one \(x\) between its initial run of \(y\)'s and its permanent \(z\) tail. These alternatives give \(2n+1\). For \(G_{14}\), \(x\) and \(y\) are incomparable idempotents with common absorbing join \(z\). A trace starts with one of the first two and changes only once to \(z\), or starts at \(z\); hence \(2n+1\). For \(G_{15}\), initial \(x\) and \(y\) are fixed forever, whereas initial \(z\) persists until the first right-hand non-\(z\), then becomes fixed at \(x\); this gives \(n+2\). For \(G_{16}\), initial \(x\) and \(y\) persist until the first spatial \(z\) forces an absorbing \(z\) tail; an initial \(z\) is fixed, giving \(2n+1\). For \(G_{18}\), initial \(x\) and \(y\) are fixed, while initial \(z\) persists until the first non-\(z\) spatial symbol, which can be independently \(x\) or \(y\); hence \(2n+1\). Each delay is realized by putting the trigger at the required spatial distance, and all possibilities follow from the stated tables.

**Linear and quadratic regimes, rules \(10,13\).** In \(G_{10}\), \(y\) is the identity, \(z\) absorbing, and \(x\odot x=z\). The time word from initial \(x\) consists of an initial run of \(x\)'s followed by \(z\)'s (\(n\) choices); from initial \(z\) it is fixed (one choice). From initial \(y\), a first spatial \(z\) yields a direct switch to permanent \(z\), while a first \(x\) produces exactly one observed \(x\) before permanent \(z\): Pascal's coefficient \(\binom{k+1}{k}=k+1\ge2\) squares that \(x\) at the next observation. The resulting \(y\)-starting histories comprise \(n\) direct-switch/constant choices and \(n-1\) one-\(x\) choices; thus \(n+1+n+(n-1)=3n\). Every listed word is realized by placing its trigger at the matching distance. In \(G_{13}\), the operation is the maximum on the three-element chain; the successive observations are exactly the weakly increasing words of length \(n\) on three letters, because the next input can always be chosen to achieve the next allowed value. Stars and bars counts these words as \(\binom{n+2}{2}\).

**Entropy.** The above finite-word descriptions are exhaustive for every positive integer \(n\). Taking logarithmic growth rates yields the values in the first table. Compactness and invariance of the trace space justify the usual identification with the trace-shift topological entropy.

## Verification

The included independent-replay script `verify.py` specifies all 18 multiplication tables in the \((x,y,z)\) order from [1]. It checks each table is associative; enumerates every finite initial word of length \(n\) for short horizons; computes its successive observed symbols by direct simultaneous local updates; and checks the resulting distinct-history cardinalities against all nine formula groups. It also tests the Table 1 representatives at \(n=1\) and the exceptional rule-3 boundary. This is a finite consistency check, not a proof for unbounded lengths. The preceding structural classification is the proof for all \(n\ge1\).

## Relationship to prior work

Fukś [1] classifies the same 18 semigroup rules and obtains explicit formulas for the state of a cell after any fixed time, including binomial-product and idempotent-product cases. The complete all-length cardinality of the *set of possible temporal histories*, and its resulting nine growth formulas and entropy trichotomy, are not stated in its full accessible text (including its appendix). The trace-factor viewpoint and its importance for reconstructing spatial dynamics are established by Cervelle, Formenti and Guillon [2], who study ultimate traces, traceability and undecidability for general cellular automata. Their theorems do not enumerate these specific 18 temporal trace languages. The exact finite-language classification adds a distinct observable invariant while making explicit use of the source's existing semigroup structure. Isomorphic and anti-isomorphic representatives have the same trace cardinality: relabeling symbols or reversing the spatial axis conjugates their observations.

## Limitations

This theorem is confined to exactly the 18 three-element associative operations listed in [1] and the full bi-infinite initial configuration space. The full-space cellular-automaton entropy, invariant measures, distribution of traces under randomized initial conditions, and finite periodic-lattice effects are not established. Some formulas can also be recovered by assembling known explicit one-time update identities, so an unindexed equivalent trace enumeration remains a scientific priority risk. A later 2026 submitted manuscript by Fukś with a closely related title was identifiable bibliographically, but its contents could not be inspected; no claim is made that it lacks this result. The finite verifier does not certify infinite-length formulas or independent scientific review.

## References

[1] H. Fukś, *Ternary cellular automata induced by semigroups of order 3 are solvable*, AUTOMATA 2025, pp. 88–106, DOI: 10.1007/978-3-032-01570-9_7; open manuscript arXiv:2601.00486v1, https://arxiv.org/html/2601.00486v1. Earliest documented public presentation: Tuesday, 2025-07-01, 13:45, AUTOMATA 2025 program, https://automata-wan-2025.univ-lille.fr/schedule.

[2] J. Cervelle, E. Formenti, P. Guillon, *Ultimate Traces of Cellular Automata*, STACS 2010, pp. 155–166, DOI: 10.4230/LIPIcs.STACS.2010.2451, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2010.2451.
