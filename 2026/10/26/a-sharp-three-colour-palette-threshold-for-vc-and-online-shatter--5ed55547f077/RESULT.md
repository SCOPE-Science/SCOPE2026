# A sharp three-colour palette threshold for VC and online shattering of path colourings

## Finding

For each integer \(n\ge1\), fix the path \(P_n\) on vertices \(1,\ldots,n\), and a palette \([q]\) with \(q\ge2\). Regard every proper vertex colouring \(f:[n]\to[q]\) as the binary membership concept \(h_f(i,a)={\bf1}[f(i)=a]\) over queries \((i,a)\in[n]\times[q]\). Then

\[
\operatorname{Ldim}(\mathcal C_{n,q})=\begin{cases}1,&q=2,\\n,&q\ge3,\end{cases}
\qquad
\operatorname{VCdim}(\mathcal C_{n,q})=\begin{cases}1,&q=2,\\n-\lfloor n/4\rfloor,&q=3,\\n,&q\ge4.\end{cases}
\]

Thus the gap for three colours is exactly \(\lfloor n/4\rfloor\), which diverges even though every underlying graph is a single connected path. This palette-specific gap disappears when one fourth colour is available.

## Assumptions and scope

The path has \(n\ge1\) labelled vertices and edges between consecutive vertices. A colouring is *proper* if adjacent vertices receive distinct colours. The palette labels are distinguishable and need not all be used. A query asks whether one specified vertex has one specified colour; it does **not** reveal the full colour of a vertex. VC dimension means shattering a fixed set of these Boolean queries. Littlestone dimension means shattering a complete binary decision tree with adaptively chosen Boolean queries, with every leaf label string realized by some proper colouring. The concept class is nonempty. No formula for general input graphs, arbitrary constraint graphs or other query models is asserted.

## Proof

**At most one static query per vertex.** A shattered query set cannot contain two different queries \((i,a)\) and \((i,b)\), because they cannot both have label one under any colouring. It cannot contain duplicate queries because they cannot have different labels. Therefore its cardinality is at most \(n\).

**Two colours.** A connected path has exactly two proper \(2\)-colourings, which differ at every vertex. Hence both VC and Littlestone dimensions are exactly one.

**Online bound for all palettes.** Fix any nonempty subfamily of assignments on at most \(m\) currently unfixed vertices, with arbitrary restrictions on their values. Every query \((i,a)\) with a nonempty positive branch fixes vertex \(i\) and leaves at most \(m-1\) unfixed vertices; induction on \(m\) shows the positive branch has Littlestone dimension at most \(m-1\). Thus a complete shattered tree of depth \(m+1\) is impossible, since its positive child would require depth \(m\). Therefore every assignment family, and in particular \(\mathcal C_{n,q}\), has Littlestone dimension at most \(n\).

**Sharp online lower bound for \(q\ge3\).** At the root query whether vertex \(1\) has colour \(1\). On the positive branch restrict witnesses to \(f(1)=1\), and on the negative branch restrict witnesses to \(f(1)=2\). Both choices are proper extendable prefixes. After a colour is fixed at vertex \(i\), there are at least two permitted colours for vertex \(i+1\). At the next decision node query equality with one of these two colours; both answers can be represented, fixing the next vertex to the queried colour on the positive edge and to another permitted colour on the negative edge. Repeating along the path constructs a complete shattered decision tree with \(n\) levels. Consequently the dimension is \(n\).

**Four or more colours, static lower bound.** For each position \(i\), choose as its target colour \(a_i=1\) when \(i\) is odd and \(a_i=2\) when \(i\) is even. For any assignment of zero/one labels to all \(n\) queries \((i,a_i)\), give vertex \(i\) colour \(a_i\) when its label is one, and give it colour \(3\) at odd positions or colour \(4\) at even positions when its label is zero. In all four combinations of two consecutive labels, the colours of adjacent vertices differ. This realizes all \(2^n\) label strings, proving VC dimension \(n\).

**Three colours, local four-query obstruction.** Suppose a shattered query set contains a query at each of four consecutive positions, with respective target colours \(a,b,c,d\). Realizability of the all-ones pattern forces \(a\ne b\), \(b\ne c\), \(c\ne d\). To realize labels \((1,0,1)\) on the first triple, the middle colour must be different from \(a,b,c\); with exactly three colours this is possible only if \(a=c\). The analogous triple in positions two through four forces \(b=d\). Thus the four target colours alternate as \((a,b,a,b)\), with \(a\ne b\). But the target-label pattern \((1,0,0,1)\) is impossible: the two inner vertices must both have the third colour, contradicting properness. Therefore no shattered set uses all four positions of any run of four consecutive vertices. Splitting the path into \(\lfloor n/4\rfloor\) disjoint consecutive blocks of four shows that at least one vertex in each such block must be unqueried. This yields the upper bound \(n-\lfloor n/4\rfloor\).

**Three colours, matching static lower bound.** Query the first three vertices of each successive four-vertex block, and query every vertex in the final incomplete block of length at most three. Target colours on every queried run are \((1,2,1)\) truncated to its run length. Every binary pattern on a run of at most three queries is realizable by a proper colouring of that run. For length three, this follows directly: for target colours \((1,2,1)\) the eight patterns are all realized, as explicitly checked by the accompanying standalone verifier. A shorter run is obtained by restriction. These runs are separated by one unqueried vertex. Independently choose a proper colouring of each queried run realizing any prescribed labels. The separator between neighbouring runs has at least one of three colours different from its two neighbours (whether their colours coincide or not), so the choices splice into one global proper colouring. A terminal unqueried vertex can also be filled. Thus all labels on \(n-\lfloor n/4\rfloor\) queries are realized. Together with the preceding upper bound this proves the exact formula.

## Verification

The included standalone program `color_path_verifier.py` enumerates all proper colourings and independently computes the exact recursive Littlestone dimension and the VC dimension over all vertex-colour queries for every \(1\le n\le7\) with \(q=3\), every \(1\le n\le4\) with \(q=4\), and every \(1\le n\le5\) with \(q=2\). It additionally checks the complete eight-pattern realization on a target triple and the nonshattering property for every proper target quadruple with three colours. The output `color_path_verification_output.txt` was generated by executing the embedded code. The unrestricted formula follows from the preceding symbolic proof; finite enumeration only corroborates it.

For the three queried vertices with target colours \((1,2,1)\), one can check each binary target pattern by enumerating the twelve proper triples; this certificate is also checked by the program. The on-path online lower-bound strategy, alternatively, explicitly constructs both continuations of every decision node.

## Relationship to prior work

Classical VC dimension and Littlestone dimension measure nonadaptive and adaptive binary shattering. Walker (arXiv:2203.12211, first posted March 23, 2022) develops general tree-shattering bounds and their comparison, but its inspected definitions, application and theorem sections do not classify proper colourings of paths. Blanca, Chen, Štefankovič and Vigoda (arXiv:1708.05118, first posted August 17, 2017) study graph-structure learning from random proper colourings, a different learning task: their inspected introduction and searched document do not compute the VC or Littlestone dimension of the *colouring hypotheses under vertex-colour-equality queries*. Manurangsi (arXiv:2211.01443, November 2, 2022) studies computational hardness of dimensions for general explicitly listed classes rather than the path-colouring formula here. These are comparisons by implication: general shattering principles and general hardness do not determine the particular palette threshold, and structure learning from samples of colourings is not online identification of a single unknown colouring. Dedicated search for an existing equivalent formula did not locate one; this is not proof of absolute publication priority.

## Limitations

The theorem assumes exactly the specified binary query model and proper colourings of simple paths. It does not concern learning the underlying graph, revealing the entire colour at once, or arbitrary graphs. The finite verifications stop at the listed sizes; the infinite quantifiers are justified by the elementary proofs. The originality assessment remains subject to historical-priority checks of literature not located by the searches; no independent mathematical audit has been performed.

## References

1. Antonio Blanca, Zongchen Chen, Daniel Štefankovič and Eric Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first public version August 17, 2017.
2. Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first public version March 23, 2022.
3. Pasin Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first public version November 2, 2022; ITCS 2023.
