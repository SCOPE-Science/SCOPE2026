# Exact shortest cyclic covers of run-limited words over arbitrary alphabets

## Finding

Fix integers \(q\ge 2\), \(r\ge 2\), \(n\ge r\), an alphabet \(\Sigma\) of \(q\) symbols, and a distinguished symbol \(a\). Let \(\mathcal L_{q,r}(n)\) be the set of all length-\(n\) words over \(\Sigma\) with no *linear* occurrence of \(a^r\). A cyclic cover is a nonempty cyclic word whose every cyclic length-\(r\) factor differs from \(a^r\), and whose cyclic length-\(n\) factors include all of \(\mathcal L_{q,r}(n)\). Define \(M_{q,r}(n)\) to be the minimum cyclic-cover length, \(E_{q,r}(n)=|\mathcal L_{q,r}(n)|\), and \(C_{q,r}(n)=M_{q,r}(n)-E_{q,r}(n)\).

Put \(D_j(z)=1-(q-1)\sum_{i=1}^j z^i\). Then, simultaneously for **every** \(q,r\ge2\),

\[
\boxed{\sum_{n\ge r} C_{q,r}(n)z^{n-r}=\frac{(q-1)\sum_{i=1}^{r-1}iz^i}{D_{r-1}(z)D_r(z)}.}
\]

Also \(\sum_{n\ge0} E_{q,r}(n)z^n=(1+z+\cdots+z^{r-1})/D_r(z)\). The proof gives an explicit optimal augmentation, a matching integral dual potential, and an Eulerian construction of an optimal cyclic cover, without solving an optimization program.

For the binary restriction against three consecutive zeroes, the exact optimal lengths for \(n=3,4,\ldots,10\) are \(7,14,28,53,102,194,367,692\). The corresponding unavoidable repetitions of length-\(n\) windows are \(0,1,4,9,21,45,93,188\).

## Assumptions and scope

Strings and their forbidden factors are linear unless called cyclic. A cyclic length-\(n\) factor may wrap around the end of its cyclic word. Cyclic words are counted by positions, not by distinct rotations. All parameters are integers with \(q\ge2\), \(r\ge2\), and \(n\ge r\). There are no asymptotic or random assumptions. Relabeling the distinguished letter does not alter the answer. At length \(n=r\), the excess is zero.

## Proof

**1. Overlap graph and imbalance.** Set \(m=r-1\) and \(L=n-1\). Form the directed overlap graph \(G\) with vertices all length-\(L\) words avoiding \(a^r\), and one edge for every \(w\in\mathcal L_{q,r}(n)\), from its length-\(L\) prefix to its length-\(L\) suffix. Every edge represents exactly one legal window. The graph is strongly connected: from any vertex, append \(L\) copies of a chosen symbol \(b\ne a\), and from \(b^L\) append the target vertex. Neither route can introduce \(a^r\).

For each vertex \(v\), an outgoing edge is lost exactly when the last \(m\) symbols of \(v\) are all \(a\), and an incoming edge is lost exactly when its first \(m\) symbols are all \(a\). Hence

\[
\deg^+(v)-\deg^-(v)=\mathbf{1}_{v\text{ begins with }a^m}-\mathbf{1}_{v\text{ ends with }a^m}.
\]

Let \(S\) be the vertices ending, but not beginning, with \(a^m\), and \(T\) those beginning, but not ending, with \(a^m\). The vertices of \(S\) have imbalance \(-1\); those of \(T\) have imbalance \(+1\); all remaining vertices are balanced.

**2. Sharp lower bound from a potential.** For a length-\(L\) vertex \(v\), define \(\phi(v)\) to be the *leftmost* zero-based start index of \(a^m\) in \(v\), or \(L-m+1\) if it does not occur. Under any legal overlap edge \(u\to v\), an existing occurrence moves one position to the left. If a new earliest occurrence is introduced at the right endpoint, its index is \(L-m\). Therefore always \(\phi(u)-\phi(v)\le1\). All vertices of \(T\) have \(\phi=0\).

Any cyclic cover induces a closed edge walk visiting all original edges. Subtracting one compulsory traversal of each original edge leaves nonnegative extra traversals \(x_e\) that balance the original imbalances. Summing the potential differences over all extra traversals gives exactly \(\sum_{s\in S}\phi(s)-\sum_{t\in T}\phi(t)=\sum_{s\in S}\phi(s)\). Since every added edge contributes at most one, their count is at least

\[
C_{q,r}(n)\ge\sum_{s\in S}\phi(s).
\]

The same argument applies to repeated edges and loops; no assumption on a particular Euler tour is needed.

**3. Optimal integral augmentation.** Each \(s\in S\) has a first occurrence of \(a^m\) at a unique position \(j=\phi(s)\ge1\). Decompose \(s=P Q\), where \(|P|=j\) and \(Q\) starts with \(a^m\). Necessarily \(P\) avoids \(a^m\) and ends in a symbol different from \(a\). Since \(s\) ends in \(a^m\), so does \(Q\). From \(s\), append the letters of the reversal \(P^{\rm rev}\), successively. All \(j\) overlap edges are legal: the first appended letter differs from \(a\), and \(P^{\rm rev}\) contains no \(a^m\). The path ends at \(f(s)=Q P^{\rm rev}\). This word begins in \(a^m\) and does not end in \(a^m\), so \(f(s)\in T\).

The map \(f:S\to T\) is bijective. Indeed, in \(f(s)\) the *last* occurrence of \(a^m\) is precisely the terminal occurrence in \(Q\): its right neighbor, when present, is the first (non-\(a\)) symbol of \(P^{\rm rev}\), and \(P^{\rm rev}\) itself avoids \(a^m\). For a given \(t\in T\), let \(\ell\) be the zero-based start of its last occurrence of \(a^m\), set \(j=L-m-\ell\ge1\), split \(t=Q R\) with \(|R|=j\), and reconstruct \(P=R^{\rm rev}\). The word \(P Q\) is a legal vertex in \(S\), and this is the inverse of \(f\). In particular, the endpoints of the paths from distinct sources are distinct sinks.

Add one copy of all the \(\phi(s)\) edges on each path \(s\to f(s)\), for each \(s\in S\). The paths compensate the imbalance by one unit at every source and sink. Intermediate vertices have matched additional in- and out-degrees. Thus the augmented strongly connected graph is Eulerian. Its Euler tour gives a legal cyclic cover with exactly \(E_{q,r}(n)+\sum_{s\in S}\phi(s)\) windows. This meets the lower bound and proves

\[
\boxed{C_{q,r}(n)=\sum_{s\in S}\phi(s).}
\]

**4. Enumeration of the excess.** Let \(F_h(z)\) be the generating series for finite \(q\)-ary words avoiding \(a^h\), including the empty word. Splitting into a final run of at most \(h-1\) copies of \(a\), preceded by optional blocks \(a^ib\) with \(b\ne a\), yields

\[
F_h(z)=\frac{1+z+\cdots+z^{h-1}}{D_h(z)}.
\]

For \(s\in S\), write \(s=P\,a^mR\) at its *first* occurrence of \(a^m\). The nonempty prefix \(P\) has no \(a^m\) and ends in a non-\(a\) letter. Its unweighted generating series is \((q-1)zF_m(z)=(1/D_m(z))-1\). Weighting by the length \(|P|=\phi(s)\) gives

\[
J(z)=z\frac{d}{dz}\big((q-1)zF_m(z)\big)
=\frac{(q-1)\sum_{i=1}^m i z^i}{D_m(z)^2}.
\]

The suffix \(R\) is either empty or begins with a non-\(a\) letter, ends in \(a^m\), and contains no \(a^{m+1}\). For the nonempty case, before the terminal run \(a^m\) there is a word beginning and ending in non-\(a\), with each intervening run of \(a\)'s having length at most \(m\). This word has generating series \((q-1)z/D_{m+1}(z)\); appending \(a^m\) yields the suffix series

\[
T(z)=1+\frac{(q-1)z^{m+1}}{D_{m+1}(z)}=\frac{D_m(z)}{D_{m+1}(z)}.
\]

The decomposition is unique and conversely describes exactly the sources. A source has total length \(L=m+|P|+|R|\) and therefore \(n-r=|P|+|R|\). Multiplying the weighted prefix series and the suffix series gives

\[
\sum_{n\ge r} C_{q,r}(n)z^{n-r}=J(z)T(z)
=\frac{(q-1)\sum_{i=1}^{r-1} i z^i}{D_{r-1}(z)D_r(z)}.
\]

The displayed expression for \(E_{q,r}(n)\) is the same avoidance-word series \(F_r(z)\). This completes the proof.

## Verification

The standalone Python 3 file `CHECK.py` enumerates the legal overlap graph, verifies the source–sink bijection, confirms each added edge has potential drop exactly one, reconstructs a closed Euler tour, and checks its cyclic windows against the complete legal language. It independently computes the rational-series coefficients by formal power-series inversion and confirms six small cases by exhaustive rejection of all shorter candidate cycles. The checks cover 47 parameter choices across \(q=2,3,4\) and \(r=2,3,4\), with the full deterministic output recorded in `CHECK_OUTPUT.txt`. These finite tests independently check implementations and examples; the preceding combinatorial proof is the proof for all parameters.

## Relationship to prior work

Sawada and Gabrić (arXiv:2510.16545; first public 2025-10-18), in their definition and Section 4.5, construct universal cycles of length-\(n\) windows that avoid \(a^r\) **cyclically within each window**. Here every window need only avoid it linearly, including windows such as \(00100\) for the binary three-zero restriction. That window is excluded from the cyclically restricted family, because its cyclic rotation has three consecutive zeroes. The linearly admissible collection is not generally Eulerian and requires repeated windows; the present theorem optimizes and counts precisely those repeats.

Chee, Etzion, Nguyen, Ta, Tran, and Vu (arXiv:2403.01454) examine maximum-length run-length-limited sequences and distinct-window objectives rather than a minimum-length full linear-language cover. Bernardini, Chen, Loukides, Pissis, Stougie, and Sweering (CPM 2022) develop general graph Eulerization methods without giving this all-parameter run-limited exact excess series. The binary restriction against two consecutive distinguished letters admits a previously established Fibonacci specialization; it is included here for completeness, not claimed as new. The new contribution is the uniform arbitrary-alphabet, arbitrary-forbidden-run optimal construction, dual certificate, and explicit excess generating function.

## Limitations

This concerns a single forbidden run \(a^r\) and \(n\ge r\), not general forbidden-factor sets, arbitrary regular languages, or the total number of distinct optimal cycles. The optimal construction can repeat legal windows; it is not a de Bruijn cycle in the usual one-appearance sense except when the original overlap graph is balanced. Searches cannot exclude every unindexed or differently presented prior result; independent external review remains outstanding.

## References

1. J. Sawada and D. Gabrić, *Las Vegas algorithms to generate universal cycles and de Bruijn sequences uniformly at random*, arXiv:2510.16545 (first posted 2025-10-18), https://arxiv.org/abs/2510.16545 .
2. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454 (2024), https://arxiv.org/abs/2403.01454 .
3. G. Bernardini et al., *Making de Bruijn Graphs Eulerian*, CPM 2022, DOI:10.4230/LIPIcs.CPM.2022.12, https://doi.org/10.4230/LIPIcs.CPM.2022.12 .
