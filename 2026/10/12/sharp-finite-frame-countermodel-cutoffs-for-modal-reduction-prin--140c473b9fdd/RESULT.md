# Sharp finite-frame countermodel cutoffs for modal reduction principles

## Finding
For integers \(m\ge1\) and \(k\ge1\), consider the modal reduction principle
\[\rho_{m,k}:=\Box^{m+k}p\longrightarrow\Box^m p.\]
Define \(d(k)=\min\{r\ge2:r\nmid k\}\); this minimum exists because \(k+1\nmid k\). Among all nonempty finite Kripke frames, the minimum number of worlds in a frame *not* validating \(\rho_{m,k}\) is exactly
\[b_{\mathbf K}(m,k)=\min\{m+1,d(k)\}.\]
Among all nonempty **serial** finite frames (every world has an outgoing edge), the corresponding minimum is
\[b_{\mathbf{KD}}(m,k)=\min\{m+2,d(k)\}.\]
Both minima are attained by functional accessibility relations (outdegree at most one for \(\mathbf K\), exactly one for \(\mathbf{KD}\)). Thus seriality raises the least countermodel size by one exactly when \(d(k)>m+1\), equivalently \(\operatorname{lcm}(1,\ldots,m+1)\mid k\). This occurs for infinitely many positive \(k\) for every fixed \(m\).

Equivalently, for every integer \(n\ge1\), *every* nonempty \(n\)-world Kripke frame validates \(\rho_{m,k}\) precisely when \(m\ge n\) and \(\operatorname{lcm}(1,\ldots,n)\mid k\). Every serial \(n\)-world frame validates it precisely when \(m\ge n-1\) and \(\operatorname{lcm}(1,\ldots,n)\mid k\). These assertions concern validity of the one formula across all valuations on an individual frame, rather than satisfiability of arbitrary formulas in an extension of modal logic.

## Assumptions and scope
A Kripke frame is a pair \(F=(W,R)\) with \(W\ne\varnothing\) and \(R\subseteq W\times W\). An \(R\)-walk of length \(t\) has exactly \(t\) edges; \(R^t(u,v)\) denotes existence of such a walk. Repeated vertices and edges are allowed. The operator \(\Box\) has its usual universal-successor semantics, including vacuous truth at dead ends. Serial means \(\forall w\in W\,\exists v\in W\ (wRv)\). All parameters \(m,k,n\) are positive integers; no reflexivity, transitivity, symmetry, or branching bound is assumed unless stated. The least number of worlds is taken only over *finite nonempty* frames.

The frame correspondence is
\[F\vDash\rho_{m,k}\quad\Longleftrightarrow\quad R^m\subseteq R^{m+k}.\]
For the reverse direction, if \((u,v)\in R^m\setminus R^{m+k}\), assign \(p\) true precisely to the worlds accessible from \(u\) in exactly \(m+k\) steps. Then \(u\vDash\Box^{m+k}p\) but \(u\not\vDash\Box^m p\). Thus the graph-theoretic inclusion exactly captures modal validity and is not merely a sufficient condition.

## Proof
**Common cycle-insertion lemma.** Let \(n=|W|\) and put \(L_n=\operatorname{lcm}(1,\ldots,n)\). Suppose \(L_n\mid k\). Whenever an \(m\)-edge walk contains a closed subwalk of length \(\ell\) with \(1\le\ell\le n\), its starting and ending vertex coincide, and \(\ell\mid k\). Inserting \(k/\ell\) additional copies of this closed segment into the walk yields a walk with the **same beginning and end**, now of length \(m+k\). This proves \(R^m\subseteq R^{m+k}\) whenever \(m\ge n\): by pigeonhole, two of the *first* \(n+1\) vertices of any such walk coincide, giving a closed subwalk of length at most \(n\).

**Serial improvement.** Assume \(R\) serial, \(m=n-1\), and \(L_n\mid k\). If an \(m\)-edge walk repeats a vertex, apply the lemma. Otherwise, its \(m+1=n\) vertices are distinct and exhaust \(W\). Seriality gives a successor of the terminal vertex, which must be one of those \(n\) vertices. Follow that edge and the original walk segment returning to the terminal vertex. This is a closed walk of length at least one and at most \(n\), based at the terminal vertex. Repeat it enough times to add exactly \(k\) edges. Thus \(R^m\subseteq R^{m+k}\) also holds at \(m=n-1\) for every serial \(n\)-world frame. For \(m>n-1\), use the repeated-vertex lemma. (The case \(n=1\) is included: every one-world serial frame has a loop.)

**Sharp obstruction when \(L_n\nmid k\).** There is some integer \(r\) with \(1\le r\le n\) and \(r\nmid k\), necessarily \(r\ge2\). A directed \(r\)-cycle has precisely one walk of each length from each starting vertex, and the endpoints of its \(m\)-walk and \((m+k)\)-walk differ because \(r\nmid k\). Hence it fails \(\rho_{m,k}\). If an exactly \(n\)-world example is desired, add isolated vertices in the unrestricted class, or isolated looped vertices in the serial class. These additions preserve the counterexample. Thus \(L_n\mid k\) is necessary for either universal claim.

**Sharp transient obstruction in the unrestricted class.** If \(m<n\), a directed path \(0\to1\to\cdots\to m\) with \(m+1\le n\) vertices (plus isolated vertices if needed) has \((0,m)\in R^m\) but \((0,m)\notin R^{m+k}\), because its terminal vertex is a dead end. Therefore universal validity on \(n\)-world unrestricted frames requires \(m\ge n\).

**Sharp transient obstruction in the serial class.** If \(m<n-1\), take \(m+2\le n\) distinct vertices \(0,1,\ldots,m+1\), edges \(i\to i+1\) for \(0\le i\le m\), and the terminal loop \((m+1)\to(m+1)\); give any remaining vertices self-loops. This is serial. The unique length-\(m\) walk from \(0\) ends at \(m\), whereas the unique length-\((m+k)\) walk from \(0\) ends beyond \(m\) since \(k\ge1\). Thus universal serial validity requires \(m\ge n-1\).

The universal \(n\)-world criteria follow from the four preceding arguments. Their equivalent least-countermodel formulas follow because a directed \(d(k)\)-cycle is a countermodel in both classes, while the transient counterexamples have \(m+1\) and \(m+2\) vertices, respectively. Conversely, if \(n\) is smaller than both candidate sizes, \(n\le m\) in the unrestricted class, or \(n\le m+1\) in the serial class, and every \(1\le r\le n\) divides \(k\); hence the corresponding universal criterion gives validity. The strict-gap and least-common-multiple equivalences follow directly from these formulas.

## Verification
The self-contained accompanying `verify.cpp` uses only ISO C++17 and its standard library. Compile and run, from the directory containing the file:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

It enumerates **every labeled directed graph on 1, 2, 3, and 4 vertices**, including loops (\(2+16+512+65536=66066\) frames), of which 50,978 are serial. For each graph, it computes Boolean reachability powers and compares the \(R^m\subseteq R^{m+k}\) property with both universal criteria for every \(1\le m\le6\), \(1\le k\le12\). The total is 4,756,752 frame/parameter instances; the expected output begins `VERIFY_OK frames=66066 serial=50978`. The program separately aggregates unrestricted and serial universally validating properties to test both directions of the thresholds. All-size assertions are proved above, **not** inferred from finite testing.

## Relationship to prior work
Knudstorp (arXiv:2510.00864, publicly posted 1 October 2025; later in *Journal of Symbolic Logic*) establishes the finite model property for extensions of \(\mathbf K\) by generalized reduction principles, via frame representation and filtration. The present result concerns a different, sharper finite invariant: the *minimum* size of a frame **violating an individual principle**, distinguishing the ambient unrestricted and serial frame classes. It neither reproves nor strengthens the paper's finite-model property, which concerns formulas consistent with an axiomatized logic.

The classical theory of Boolean matrix powers includes eventual-period and equality identities. In particular, the Boolean-matrix identity at exponent \((n-1)^2+1\) with period \(L_n\), reported in Proposition 2.7 of arXiv:2607.09677 from earlier work, is about **equality of powers at a larger exponent**, not the sharp **one-sided inclusion** \(R^m\subseteq R^{m+k}\) beginning at \(m=n\), or at \(m=n-1\) under seriality. De Schutter and De Moor's 1999 preprint studies eventual behavior of consecutive Boolean-matrix powers; its bounds and eventual-period framework do not in themselves specify these two least-countermodel cutoffs. Standard cycle pumping underlies the proof; earlier equivalent formulations remain a substantive possibility.

## Limitations
The result applies to the one specified reduction axiom, not to all formulas of an associated logic. Seriality is required *globally* for the serial bound; requiring only that the witness root have a successor is insufficient. The finite enumerator is a consistency check through four worlds and does not establish the universal theorem. No independent audit has been performed, and potential overlap with older Boolean-matrix or finite-automata formulations remains a literature risk.

## References
1. Søren Brinck Knudstorp, *Knocking Down Boxes: The FMP for \(\mathbf K\oplus\Box^{m+k}p\to\Box^mp\)*, arXiv:2510.00864 (public preprint October 1, 2025); later *Journal of Symbolic Logic*, doi:10.1017/jsl.2026.10248. https://arxiv.org/abs/2510.00864
2. B. De Schutter and B. De Moor, *On the Sequence of Consecutive Powers of a Matrix in a Boolean Algebra*, publicly accessible 1999 preprint. https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/97_67.pdf
3. *The finite basis problem for matrix semirings \(\mathbf M_n(S_7)\)*, arXiv:2607.09677, Proposition 2.7 (Euler–Fermat Boolean-matrix periodic identity and earlier references). https://arxiv.org/html/2607.09677
