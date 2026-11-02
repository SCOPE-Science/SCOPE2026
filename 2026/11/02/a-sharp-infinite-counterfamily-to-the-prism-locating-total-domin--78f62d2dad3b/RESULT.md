# A sharp infinite counterfamily to the prism locating-total domination conjecture

## Finding
For every integer \(t\ge 0\), let \(n=8+5t\) and let \(P_n=C_n\square K_2\) be the circular ladder (prism graph). Then its locating-total domination number is
\[
\boxed{\gamma_t^L(P_n)=7+4t=\left\lceil\frac{4n}{5}\right\rceil.}
\]
In particular, the \(n\equiv3\pmod5\) branch, for \(n\ge8\), of Conjecture 2 in Raza, Iqbal, Khan, and Botmart (2021) is false: that conjecture predicts one additional selected vertex at each of these orders. The first counterexample is \(\gamma_t^L(C_8\square K_2)=7\), not \(8\).

## Assumptions and scope
All graphs are finite and simple. The vertices of \(P_n\) are \((i,s)\), where \(i\in\mathbb Z/n\mathbb Z\) is a column index and \(s\in\{0,1\}\) is a row index, with open neighborhoods
\[
N(i,s)=\{(i-1,s),(i+1,s),(i,1-s)\}.
\]
A set \(S\) is locating-total dominating (LTD) if every vertex, including vertices of \(S\), has a neighbor in \(S\), and the nonempty fingerprints \(N(v)\cap S\) are pairwise different for distinct vertices \(v\notin S\). The invariant \(\gamma_t^L\) is the minimum size of such a set.

Encode the selection in column \(i\) by a digit \(w_i\in\{0,1,2,3\}\): digit \(0\) selects neither vertex, \(1\) selects only \((i,0)\), \(2\) selects only \((i,1)\), and \(3\) selects both. Define words
\[
B=(3,1,0,3,0,3,0,0),\qquad Q=(3,0,3,0,0).
\]
The candidate set for \(n=8+5t\) is represented by the cyclic word \(BQ^t\); the order of the digits is the order of columns modulo \(n\).

## Proof
**Lower bound.** Let \(S\) be any LTD-set of a cubic graph on \(2n\) vertices, and put \(s=|S|\) and \(q=2n-s\). Every selected vertex has a selected neighbor by total domination, so at most two of its three incident edges join \(S\) to its complement. Thus the number \(E_\times\) of such edges satisfies \(E_\times\le2s\). Every unselected vertex has a nonempty fingerprint, and no two unselected vertices have the same singleton fingerprint. Consequently at most \(s\) of the \(q\) fingerprints are singletons; counting their sizes gives \(E_\times\ge2q-s\) (also valid when \(q<s\)). Therefore \(2(2n-s)-s\le2s\), or \(s\ge\lceil4n/5\rceil\).

**Five-column locality lemma.** In \(P_n\), for \(n\ge8\), distinct vertices with a common open neighbor are precisely pairs \((i,s),(i+2,s)\) and pairs \((i,s),(i+1,1-s)\), allowing cyclic shifts and either choice of \(s\). Distinct outside vertices with equal nonempty fingerprints must have a common selected neighbor, so these pairs are the only possible location collisions.

For the first pair, the only common neighbor is \((i+1,s)\). If both endpoints are outside \(S\), equality of their nonempty fingerprints would require this common neighbor to be selected and all four private neighbors \((i-1,s),(i,1-s),(i+3,s),(i+2,1-s)\) to be absent. For the second pair, the common neighbors are \((i+1,s)\) and \((i,1-s)\); equality would require both private neighbors \((i-1,s)\) and \((i+2,1-s)\) to be absent. The total-domination condition for column \(i\) depends only on columns \(i-1,i,i+1\). Thus total domination and all possible collisions involving a vertex in column \(i\) and a forward partner can be decided by the five consecutive digits for columns \(i-1,\ldots,i+3\).

**Finite factor certificate.** The following table lists *every distinct* five-column factor that occurs in the cyclic word \(BQ^t\), over all integers \(t\ge0\). Each row checks total domination for the two vertices of the factor's second column and tests all eligible forward outside pairs at column offsets one and two. The last column reports the number of eligible pairs; no row contains a collision.

| Factor | Selected mask in second column | Eligible outside-pair tests | Total domination | Equal fingerprints |
| --- | ---: | ---: | --- | --- |
| `00303` | 0 | 2 | yes | none |
| `00310` | 0 | 1 | yes | none |
| `03003` | 3 | 0 | yes | none |
| `03030` | 3 | 0 | yes | none |
| `03103` | 3 | 0 | yes | none |
| `10303` | 0 | 2 | yes | none |
| `30030` | 0 | 2 | yes | none |
| `30031` | 0 | 2 | yes | none |
| `30300` | 0 | 2 | yes | none |
| `31030` | 1 | 1 | yes | none |

The ten rows are verified directly by substituting the indicated four possible masks into the displayed formula for \(N(i,s)\). The standalone `verify_prism.py` reconstructs this same finite Boolean test and, separately, checks the original global definition.

For completeness, the factor list is exhaustive for *every* \(t\), not extrapolated from finitely many prism sizes. For \(t=0\), use the cyclic factors of \(B\). For \(t=1\), use those of \(BQ\). For \(t\ge2\), a five-column window lies wholly within a block or crosses one of the four interface types (within \(B\), from \(B\) to \(Q\), from \(Q\) to \(B\), or from \(Q\) to \(Q\)); because \(|B|=8\) and \(|Q|=5\), it cannot cross more than one of these interfaces. Every such interface is represented among the cyclic five-column factors of \(BQQ\). The union of the factors of \(B\), \(BQ\), and \(BQQ\) is exactly the ten-factor table above. Hence the locality lemma certifies that \(BQ^t\) is LTD for every integer \(t\ge0\).

Finally, \(B\) selects \(7\) vertices, and each \(Q\) selects \(4\). Thus \(|S|=7+4t=\lceil4(8+5t)/5\rceil\), attaining the general lower bound. This proves the theorem. \(\square\)

## Verification
Run `python3 verify_prism.py` using Python 3 standard library only. It verifies the exact ten-factor table, its local domination and collision tests, and global LTD feasibility of the displayed words at \(n=8,13,\ldots,63\). It also independently exhausts all smaller cardinalities on \(n=8\). Those finite direct-graph checks corroborate the theorem; the proof of the infinite quantifier is the locality lemma plus the exhaustive block-interface factor argument, not enumeration of finitely many graph orders.

## Relationship to prior work
Raza, Iqbal, Khan, and Botmart (2021), Theorem 5, give the same sharp value for residue classes \(0,2,4\pmod5\) and upper bounds for the other two residue classes. Their Conjecture 2 explicitly predicts \(\lceil4n/5\rceil+1\) for \(n\equiv1,3\pmod5\). The present theorem disproves its entire \(3\pmod5\) branch from \(n=8\) onward while proving the exact, smaller value. Earlier work by Henning and Rad investigates locating-total domination, including ordinary ladder graphs; those are not the cyclic ladders studied here. Chakraborty and collaborators (2022/2024) prove general upper bounds for subcubic graphs but do not give this residue-class equality or address this prism conjecture in the inspected text.

## Limitations
This theorem does not determine the remaining \(1\pmod5\) residue class, the small prism \(n=3\), or the exceptional order \(n=6\). It does not enumerate all minimum LTD-sets, and it does not claim that no alternative proof or earlier unindexed resolution exists. The table is a finite, fully specified symbolic certificate for a local infinite-family proof; separate automated tests are supporting evidence rather than substitutes for it. No independent mathematical audit has been performed.

## References
1. H. Raza, N. Iqbal, H. Khan, T. Botmart, *Computing locating-total domination number in some rotationally symmetric graphs*, Science Progress 104 (2021), DOI: 10.1177/00368504211053417. First online 2021-11-17. Theorem 5 and Conjecture 2.
2. M. A. Henning, N. J. Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), DOI: 10.1016/j.dam.2012.04.004.
3. D. Chakraborty, F. Foucaud, A. Hakanen, M. A. Henning, A. K. Wagler, *Progress towards the two-thirds conjecture on locating-total dominating sets*, arXiv:2211.14178 (submitted 2022-11-25; revised 2024-08-07).
4. F. Foucaud, M. A. Henning, *Locating-total dominating sets in twin-free graphs: a conjecture*, Electron. J. Combin. 23(3) (2016), DOI: 10.37236/5147.
