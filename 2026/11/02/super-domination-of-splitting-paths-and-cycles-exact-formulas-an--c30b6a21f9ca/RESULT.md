# Super domination of splitting paths and cycles: exact formulas and an eight-step obstruction

## Finding
Let \(S'(G)\) be the **splitting graph** obtained from a finite simple graph \(G\) by adjoining, for every original vertex \(v\), a vertex \(v'\) adjacent to all original neighbors of \(v\), with no edges among the new vertices. Equivalently \(S'(G)=G\star K_1\), the neighborhood corona with single-vertex second factor. A super dominating set \(D\) has the property that every vertex outside \(D\) is the unique vertex outside \(D\) adjacent to some vertex in \(D\). Write \(\gamma_{\mathrm{sp}}\) for its minimum cardinality.

**Theorem.** For every integer \(n\ge2\),
\[
\gamma_{\mathrm{sp}}(S'(P_n))=
\begin{cases}
8,&n=6,\\[2pt]
\left\lceil\frac{5n-2}{4}\right\rceil,&n\ne6.
\end{cases}
\]
For every integer \(n\ge4\),
\[
\gamma_{\mathrm{sp}}(S'(C_n))=
\left\lceil\frac{5n}{4}\right\rceil+
\mathbf 1_{\{n\equiv4\pmod8\}}.
\]
The period-eight correction for cycles comes from the fact that all tight cycles in the exact local potential certificate have length eight. Both formulas address natural instances of a previously stated open case for neighborhood-corona super domination.

## Assumptions and scope
The path \(P_n\) and cycle \(C_n\) are labeled simple graphs with respectively \(n\) vertices; a simple cycle has at least four vertices in the stated result. The graph \(S'(G)\) has \(2n\) vertices when \(G\) has order \(n\). The neighborhood condition uses **open** neighborhoods. Each outside vertex must have a (possibly different) inside witness adjacent to no other outside vertex. The theorem concerns the optimum cardinality, not the number of optimal sets. It asserts nothing about arbitrary graph factors or \(C_3\).

## Proof
### 1. Local complement alphabet
Write \(W=V(S'(G))\setminus D\). At a base position, use symbol `0` when neither original nor duplicate is in \(W\), symbol `1` when only the original is in \(W\), and symbol `2` when only its duplicate is in \(W\). **Both cannot belong to \(W\):** a selected original witness for the duplicate would also be adjacent to the omitted original, while duplicate vertices never witness another duplicate. This eliminates the fourth symbol for every valid super domination complement.

Let \((a,b,c,d,e)\) be five successive symbols, and use `X` for a nonexisting position outside the ends of a path. For a nonempty center, the potential witnesses lie at positions \(b,d\); they are original or duplicate vertices in those neighboring positions. Exactly the following rule characterizes whether a center is properly witnessed:

```
center c=0: valid;
center c=2: for at least one side (neighbor j, outer o),
            j exists, j!=1, and o is 0 or X;
center c=1: for at least one side (neighbor j, outer o),
            j exists and either [j!=1 and o in {0,X}]
                            or [j!=2 and o!=1].
```

For the left side take \((j,o)=(b,a)\), and for the right side \((j,o)=(d,e)\). To see sufficiency, the first clause selects an original neighbor whose **only** omitted neighbor is the center; the second clause selects a duplicate neighbor (which only sees original vertices). Necessity follows by exhausting these two possible witness types. For a cycle the positions are read modulo \(n\); for a path, pad two `X` symbols on either side. Thus a symbol word is valid precisely when every length-five center passes the displayed rule. Its number of nonzero symbols equals \(|W|\).

### 2. A finite potential giving both upper bounds
There are \(3^4=81\) four-letter states in lexicographic order. An arc
\[
(a,b,c,d)\longrightarrow(b,c,d,e)
\]
exists when the five-letter word passes the local test at center \(c\), and its weight is \(w=\mathbf1_{\{e\ne0\}}\). Exactly \(178\) arcs exist. The following integer potential \(h\), ordered lexicographically by four-letter states and displayed in nine consecutive rows of nine entries, is a finite certificate:

```
0 1 1 0 2 2 0 2 2
0 1 1 0 4 4 0 4 4
0 1 1 0 3 3 1 3 3
0 1 1 0 3 3 0 4 4
0 2 3 2 5 6 3 6 6
0 0 0 0 0 0 3 0 0
0 1 1 0 3 3 0 3 3
0 1 1 1 4 5 1 4 4
0 2 2 0 4 4 1 4 4
```

Every one of the \(178\) arcs satisfies the **exact integer inequality**
\[
4w-3\le h(\mathrm{destination})-h(\mathrm{source}).
\]
The included standalone checker evaluates the local rule for every possible five-symbol window, reconstructs all arcs, and checks each inequality. It also derives the displayed potential without input from the table: initialize all \(81\) entries to zero and repeatedly replace each destination value by the maximum of its old value and each predecessor value plus \(4w-3\). Stabilization occurs after \(12\) passes, so the table and the inequalities are independently reconstructible from short integer arithmetic.

For a valid cyclic word of length \(n\), the corresponding closed walk has total weight \(|W|\). Summing the potential inequality yields \(4|W|\le3n\). Exactly \(90\) arcs are tight. Exhaustively checking **all** simple directed cycles of this tight subgraph gives exactly three cycles, each of length eight (the associated cyclic symbol words can be chosen as `11120021`, `11220022`, and `10220111`). Every closed tight walk decomposes into these simple cycles, so its length is divisible by eight. If \(n\equiv4\pmod8\), equality \(4|W|=3n\) is impossible, forcing \(|W|\le3n/4-1\). Otherwise \(|W|\le\lfloor3n/4\rfloor\).

For paths with \(n\ge4\), use two `X` symbols at each end. An initial four-letter state \(s=(a,b,c,d)\) is permitted exactly when the first two padded centers pass; a terminal state is permitted exactly when the last two padded centers pass. There are \(46\) states of each kind. Summing arc inequalities over interior transitions gives
\[
4|W|-3n \le
\bigl(4\#\{x\in s:x\ne0\}-12-h(s)\bigr)+h(t),
\]
where \(t\) is the terminal state. Exhaustive evaluation of the permitted boundary states gives respective maxima \(-2\) and \(4\), hence
\[
|W|\le\left\lfloor\frac{3n+2}{4}\right\rfloor.
\]
For \(n=6\), an exhaustive check of the \(4^6\) labeled original/duplicate omission choices shows \(|W|\le4\), improving the general upper bound of five by one. The case \(n=2,3\) is checked directly.

### 3. Matching constructions for all orders
In the following finite strings, the nonzero symbols are exactly the omitted vertices. The complete base list is provided literally in `verify_split_super.py`. For path orders \(n=2,3,\ldots,15\), it starts with the strings `11`, `011`, `2201`, `22011`, `220120`, `2201110`, and then lists one optimum for every \(n=8,\ldots,15\). For cycle orders \(n=4,\ldots,11\), its optima are, in order, `0021`, `00111`, `001111`, `0011112`, `00211112`, `000211112`, `0021111022`, `00221101122`. Every base word is checked against **all** of its local windows and attains the corresponding upper bound (including both exceptional cases).

Each base word of path length \(8\) through \(15\), and each base cyclic word of length \(4\) through \(11\), contains a consecutive four-letter state belonging to one of the three tight eight-cycles. At such a state, follow that tight directed cycle for eight steps before resuming the original state sequence. This inserts precisely eight extra positions, with exactly six additional omissions, and returns to the same state. It preserves every length-five constraint, including both boundary conditions for paths; cyclically rotate a cycle word when necessary. The checker constructs and tests each insertion explicitly. Repeating the insertion proves existence for every larger order in the same residue class modulo eight. Every claimed upper bound is therefore attained, and subtracting the optimal omission count from \(2n\) proves the theorem.

## Verification
Run `python3 verify_split_super.py` from the extracted package. The verifier has **no third-party dependencies** and checks \(81\) states, \(178\) transitions, the integer potential, all tight directed cycles, boundary maxima, all base words and insertions, and sample insertions through length \(64\). Its second, independent graph-level implementation constructs the actual splitting graphs and exhaustively checks **174672 vertex subsets across 12 instances**, covering paths of lengths \(2\) through \(8\) and cycles of lengths \(4\) through \(8\). The finite certificate proves the unbounded claims by the explicitly stated potential and insertion induction; finite graph enumeration alone would not.

## Relationship to prior work
Ghanbari, Jäger, and Lehtilä, *Super Domination: Graph Classes, Products and Enumeration* (first public arXiv version September 5, 2022), Section 7(a), explicitly identify \(\gamma_{\mathrm{sp}}(G\star K_1)\) as a case outside their main neighborhood-corona formula and suggest determining it. Their Section 3 gives a general upper bound, but not these exact path/cycle values. Vaidya and Kothari, *Domination Integrity of Splitting Graph of Path and Cycle* (2013), study these same splitting graph families under **ordinary** domination and domination integrity, not super domination. Ordinary domination results do not imply these formulas, particularly the period-eight obstruction. No equivalent formula emerged from the specified research-record and literature searches, but this does not establish absolute publication priority.

## Limitations
The result treats only path factors \(n\ge2\) and simple cycle factors \(n\ge4\). It does not determine the invariant for an arbitrary first factor, does not enumerate all optimum sets, and has no independent publication-priority certification. The critical-cycle enumeration is a finite computer-reproducible lemma whose exhaustive integer implementation is included; the broader conclusions follow by the mathematical potential inequality and induction. Relevant unindexed or inaccessible literature could affect the novelty assessment.

## References
1. N. Ghanbari, G. Jäger, and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795v1 (September 5, 2022), Sections 3 and 7(a). https://arxiv.org/abs/2209.01795
2. S. K. Vaidya and N. J. Kothari, *Domination Integrity of Splitting Graph of Path and Cycle*, International Scholarly Research Notices (2013), article 795427. https://doi.org/10.1155/2013/795427
