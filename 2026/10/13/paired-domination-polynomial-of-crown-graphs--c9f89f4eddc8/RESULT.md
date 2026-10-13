# Paired-domination polynomial of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M\), where the bipartition classes are \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), and the deleted perfect matching is \(M=\{a_i b_i:1\le i\le n\}\). For a vertex set \(S\), write \(p=|S\cap A|\) and \(q=|S\cap B|\).

Then \(S\) is paired-dominating if and only if
\[
p=q=t\quad\text{for some}\quad 2\le t\le n.
\]
Therefore the paired-domination polynomial is
\[
D_{\mathrm{pr}}(\operatorname{Cr}_n;x)=\sum_{t=2}^n \binom{n}{t}^2x^{2t}.
\]
In particular,
\[
\gamma_{\mathrm{pr}}(\operatorname{Cr}_n)=4,
\qquad
\#\{\text{minimum paired-dominating sets}\}=\binom{n}{2}^2,
\]
every inclusion-minimal paired-dominating set has size \(4\), and hence \(\Gamma_{\mathrm{pr}}(\operatorname{Cr}_n)=4\). The total number of paired-dominating sets is
\[
\binom{2n}{n}-n^2-1.
\]

## Assumptions and scope
A paired-dominating set is a dominating set whose induced subgraph contains a perfect matching. The result uses ordinary finite simple undirected graphs and the standard crown graph \(K_{n,n}\) with one perfect matching deleted. The restriction \(n\ge3\) matches the crown-family range used in the closest same-object source and avoids the degenerate disconnected graph at \(n=2\).

The polynomial counts vertex sets by cardinality: the coefficient of \(x^k\) is the number of paired-dominating sets of size \(k\).

## Proof
Let \(P=\{i:a_i\in S\}\) and \(Q=\{j:b_j\in S\}\), with \(p=|P|\) and \(q=|Q|\).

If \(S\) is paired-dominating, then \(\operatorname{Cr}_n[S]\) is bipartite with sides \(S\cap A\) and \(S\cap B\) and has a perfect matching. A perfect matching saturates both sides, so necessarily \(p=q=t\).

The case \(t=1\) is impossible. If \(P=Q=\{i\}\), then \(a_i b_i\) is the deleted matching edge, so the induced pair has no perfect matching. If \(P=\{i\}\) and \(Q=\{j\}\) with \(i\ne j\), then \(a_i b_j\) is an edge, but the unselected vertex \(a_j\) has no neighbor in \(S\cap B=\{b_j\}\); hence \(S\) is not dominating. Thus every paired-dominating set has \(t\ge2\).

Conversely, suppose \(p=q=t\ge2\). Every vertex outside \(S\) on the \(A\)-side is adjacent to all selected vertices of \(B\) except possibly its indexed partner, so it has at least \(t-1\ge1\) selected neighbors. The same argument holds on the \(B\)-side. Hence \(S\) dominates the graph.

It remains to show that \(\operatorname{Cr}_n[S]\) has a perfect matching. Apply Hall's theorem to the selected \(A\)-vertices. A singleton \(\{a_i\}\) has either \(t\) selected neighbors or \(t-1\) selected neighbors, and the latter is at least one. If \(X\subseteq S\cap A\) has at least two vertices, then every selected \(b_j\) is adjacent to some vertex of \(X\): the only \(A\)-vertex that \(b_j\) can miss is \(a_j\). Thus \(N(X)=S\cap B\), so \(|N(X)|=t\ge|X|\). Hall's condition holds and the induced subgraph has a perfect matching. This proves the characterization.

For a fixed \(t\), choose \(t\) vertices independently from each bipartition side, giving \(\binom{n}{t}^2\) sets of size \(2t\), which proves the polynomial. The minimum occurs at \(t=2\). If \(t>2\), choosing any two selected vertices from each side gives a proper paired-dominating subset, so no such set is inclusion-minimal; every size-
\(4\) paired-dominating set is minimal because no smaller paired-dominating set exists. Finally, Vandermonde's identity gives
\[
\sum_{t=0}^n\binom{n}{t}^2=\binom{2n}{n},
\]
and subtracting the \(t=0\) and \(t=1\) terms yields the stated total.

## Verification
A standalone exhaustive checker constructs \(\operatorname{Cr}_n\), tests domination directly, tests perfect matchability by an augmenting-path bipartite matcher, and compares the resulting truth table against the criterion \(p=q\ge2\). It also compares every coefficient with \(\binom{n}{t}^2\), verifies the minimum count and total count, and checks inclusion-minimality. The packaged run covers every vertex subset for \(3\le n\le8\), a total of \(87{,}360\) subsets, with maximum order \(16\). The computation is a finite stress test; the proof above supplies the all-
\(n\) argument.

## Relationship to prior work
Haynes and Slater introduced paired domination in 1998. Puttaswamy and S. R. Nayaka study the same crown graph \(S_n^0\) in their 2016 paper on minimum paired-dominating energy. Their Theorem 3.3 uses \(\{u_1,u_2,v_1,v_2\}\) as a minimum paired-dominating set, thereby covering the scalar minimum size \(4\) and one witness but not the classification or enumeration of all paired-dominating sets.

A 2016 proceedings abstract by Puttaswamy, Anwar Alwardi, and S. R. Nayaka introduces the paired-domination polynomial and says that polynomials are computed for unspecified standard graph families. Targeted searches for the crown terminology, the notation \(S_n^0\), and the coefficient pattern in the present theorem did not locate a crown formula. The publicly retrievable document is only the one-page abstract, so a fuller proceedings version remains an access-related residual risk rather than evidence of coverage.

## Limitations
The theorem is only about the standard crown graph and ordinary paired domination. It does not classify the perfect matchings inside each paired-dominating set, weighted variants, or paired domination under graph modifications. The exhaustive checker is not an infinite proof; it is used only to stress-test the proved characterization on \(3\le n\le8\). A fuller version of the 2016 paired-domination-polynomial proceedings contribution was not publicly retrievable during the comparison, so exact historical priority for the crown polynomial cannot be absolutely excluded.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32(3), 199–206 (1998). DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. First published online 1998-12-07.
2. Puttaswamy and S. R. Nayaka, “The Minimum Paired Dominating Energy of a Graph,” *International Journal of Mathematics And its Applications* 4(2-A), 59–69 (2016). Theorem 3.3 treats the crown graph \(S_n^0\).
3. Puttaswamy, Anwar Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” ICMAGT 2016 proceedings abstract, September 2016.
4. W. Ulatowski, “All graphs with paired-domination number two less than their order,” *Opuscula Mathematica* 33(4), 763–783 (2013), MSC 05C69.
