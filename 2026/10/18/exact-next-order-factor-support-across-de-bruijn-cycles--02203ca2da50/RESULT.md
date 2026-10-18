# Exact next-order factor support across de Bruijn cycles

## Finding
For a labelled alphabet \(\Sigma\) with \(|\Sigma|=q\), write \(\mathcal U_{q,n}\) for the union of length-\(n+1\) cyclic factors of **all** de Bruijn cycles of order \(n\). For every \(n\ge2\),
\[
\mathcal U_{q,n}=\begin{cases}
\Sigma^{n+1}\setminus\{a^{n+1}:a\in\Sigma\},&q\ge3,\\
\{0,1\}^{n+1}\setminus\{0^{n+1},1^{n+1},01^{n-1}0,10^{n-1}1\},&q=2.
\end{cases}
\]
In particular, \(|\mathcal U_{q,n}|=q^{n+1}-q\) for \(q\ge3\), and \(|\mathcal U_{2,n}|=2^{n+1}-4\). The result concerns occurrence in **some** de Bruijn cycle, not every cycle or the probabilities of occurrence.

## Assumptions and scope
A cyclic de Bruijn sequence of order \(n\) is a cyclic word of period \(q^n\) in which each of the \(q^n\) length-\(n\) words appears exactly once as a cyclic factor. No identification of alphabet symbols is imposed. The integers satisfy \(q\ge2\) and \(n\ge2\). Repeated positions across the wraparound count in the usual cyclic manner. A factor is *attainable* when at least one cyclic order-\(n\) de Bruijn word contains it. The statement is exact for all such parameters, not an asymptotic assertion.

## Proof
Let \(H\) be the order-\(n\) de Bruijn directed graph: vertices are \(\Sigma^{n-1}\), and its arcs, each used once, are the words \(x_1\cdots x_n\in\Sigma^n\), directed from \(x_1\cdots x_{n-1}\) to \(x_2\cdots x_n\). Every vertex has in- and outdegree \(q\). Euler circuits of \(H\) correspond to the desired de Bruijn cycles.

**Connectivity lemma.** Deleting any single vertex \(v\), together with its incident arcs, leaves a weakly connected graph on the remaining vertices. Indeed, a cyclic de Bruijn sequence of order \(n-1\) exists for every alphabet size \(q\ge2\). Its consecutive length-\(n-1\) factors form a directed Hamilton cycle through the vertices of \(H\). Removing \(v\) from that Hamilton cycle leaves a spanning directed path through every remaining vertex. This also covers \(n=2\), when the Hamilton cycle is on the individual alphabet symbols.

Fix a candidate word \(w=x_1\cdots x_{n+1}\), and set \(e=x_1\cdots x_n\), \(f=x_2\cdots x_{n+1}\). Their arcs are consecutive through the vertex \(v=x_2\cdots x_n\). If \(e=f\), then \(w\) is constant. Two successive copies of the same arc cannot occur in an Euler circuit, so all \(q\) constant candidates are excluded. Assume now \(e\ne f\), and let \(u=x_1\cdots x_{n-1}\) and \(z=x_3\cdots x_{n+1}\) be the first and last vertices of the two-arc walk \(u\xrightarrow{e}v\xrightarrow{f}z\).

Construct a directed multigraph \(H_w\) by deleting the distinct arcs \(e,f\) of \(H\) and inserting one *shortcut* arc \(u\to z\). Each vertex remains balanced. An Euler circuit in \(H_w\), with the shortcut replaced by \(e,f\), is an Euler circuit of \(H\) in which \(e\) is immediately followed by \(f\). Conversely, any Euler circuit of \(H\) containing this consecutive pair contracts to an Euler circuit in \(H_w\). Thus \(w\) is attainable if and only if \(H_w\) has an Euler circuit.

By the connectivity lemma, all vertices other than \(v\) remain weakly connected in \(H_w\): no arc with both endpoints outside \(v\) was removed, and adding the shortcut cannot disconnect them. We therefore need only decide whether \(v\) is connected to this subgraph. The only loops in \(H\) occur at constant vertices \(a^{n-1}\), where the loop is the arc \(a^n\). At a **nonconstant** vertex, there are no loops. After removal of one entering and one leaving arc, at least \(q-1\ge1\) entering and \(q-1\ge1\) leaving arcs remain, all connecting \(v\) to another vertex. Hence \(H_w\) is weakly connected.

Suppose next \(v=a^{n-1}\) is constant. If either \(e\) or \(f\) is its loop \(a^n\), then the inserted shortcut is incident to \(v\) and a different vertex, because \(e\ne f\); hence \(H_w\) is weakly connected. If neither is a loop, then the loop remains at \(v\), and \(q-2\) additional nonloop incoming and \(q-2\) additional nonloop outgoing arcs remain. When \(q\ge3\), this connects \(v\) to the other vertices, so \(H_w\) is weakly connected. For \(q=2\), no nonloop arc remains incident to \(v\). In that case \(v\) forms an isolated loop component and \(H_w\) cannot have an Euler circuit. Because the two removed arcs must be the unique nonloop incoming and outgoing arcs at \(a^{n-1}\), the forbidden word is exactly \(ba^{n-1}b\), where \(\{a,b\}=\{0,1\}\). The two choices yield \(01^{n-1}0\) and \(10^{n-1}1\).

Finally, a finite directed graph with balanced in- and outdegrees has an Euler circuit precisely when its nonisolated vertices lie in one weakly connected component. In all cases not already excluded, \(H_w\) is balanced and weakly connected, so the circuit exists. Expanding its shortcut gives the required order-\(n\) de Bruijn word containing \(w\). The listed forbidden words are distinct for \(n\ge2\), yielding the stated cardinalities. \(\square\)

## Verification
The standalone `verify.py` implements the shortcut contraction, constructs an Euler tour by Hierholzer's algorithm whenever possible, expands the shortcut, and independently checks that the resulting cyclic word has every length-\(n\) factor exactly once and contains the prescribed length-\(n+1\) word. It tested all candidates for binary \(2\le n\le7\), ternary \(2\le n\le4\), and quaternary \(2\le n\le3\), amounting to 1,175 candidate checks. Independently, the program enumerated all binary de Bruijn cycles through order four and computed their complete next-order factor union, giving 1, 2, and 16 cycles at orders two, three, and four respectively. The recorded execution is in `verification_output.txt`; run `python3 verify.py` using Python 3 standard library only. These finite checks support, but are not the proof of, the quantified infinite assertion.

## Relationship to prior work
Sawada and Gabrić, *Random generation of universal cycles and de Bruijn sequences* (first posted October 18, 2025), use the same Eulerian graph framework to sample de Bruijn cycles uniformly; their results motivate asking which length-\(n+1\) motifs have positive support. Their algorithmic existence and sampling statements do not on their own give the exact support classified here. Nellore and Ward (2022) discuss factor frequencies past the de Bruijn order and explicitly illustrate length-four factors in a binary order-three cycle, but that illustrative one-cycle example is not a quantified union over all cycles. Moreno (2005) studies universal cycles for restricted *sets of length-\(n\) arcs*, as opposed to prescribing a pair of consecutive arcs in the unrestricted graph. Classical existence of de Bruijn cycles and the Euler-tour characterization are used as known inputs, not claimed as discoveries.

## Limitations
This statement does not count how many de Bruijn cycles contain a given next-order word, compute any motif's exact probability under random sampling, or classify simultaneous prescriptions of several factors. Originality is assessed relative to accessible literature; the potentially relevant 1984 article by Dayhoff on independently prescribable word sets could not be examined in full, so an unrecognized equivalent earlier formulation remains a risk. The proof treats \(n\ge2\); the order-one case is not asserted. Independent scientific audit has not been performed.

## References
1. J. Sawada and D. Gabrić, *Random generation of universal cycles and de Bruijn sequences*, arXiv:2510.16545, first posted 2025-10-18. https://arxiv.org/abs/2510.16545
2. A. Nellore and R. Ward, *Arbitrary-length analogs to de Bruijn sequences*, CPM 2022; arXiv:2108.07759. https://arxiv.org/abs/2108.07759
3. E. Moreno, *De Bruijn sequences and De Bruijn graphs for a general language*, Information Processing Letters 96 (2005), 214–219. DOI:10.1016/j.ipl.2005.05.028.
4. J. E. Dayhoff, *Independently prescriable sets of n-letter words*, Discrete Mathematics 50 (1984), 193–219. DOI:10.1016/0012-365X(84)90048-7. Full text not inspected.
