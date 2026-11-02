# Fixed-content enumeration of binary circular three-gram spectra

## Finding

Let \(H_{p,q}\) be the number of distinct **complete circular three-gram multiplicity vectors** of nonempty binary circular words containing \(p\) zeros and \(q\) ones. Rotation is ignored, but reversal and complementation are not identified. Multiplicities, not merely three-gram supports, are observed. Then the following bivariate generating function holds as an identity of formal power series:

\[
\begin{aligned}
\mathcal H(x,y)&=\sum_{p,q\ge0,\ p+q\ge1}H_{p,q}x^py^q\\
&=\frac{x}{1-x}+\frac{y}{1-y}+\frac{xy}{1-xy}\\
&\quad+\frac{x^2y}{(1-x)(1-x^2y)(1-xy)}
+\frac{xy^2}{(1-y)(1-xy^2)(1-xy)}\\
&\quad+\frac{x^2y^2}{(1-x)(1-y)(1-x^2y^2)(1-xy)}
\left(\frac{1}{1-x^2y}+\frac{xy^2}{1-xy^2}\right).
\end{aligned}
\]

Writing \(A_n=\sum_{p+q=n}H_{p,q}\), the exact length-only generating function is

\[
\sum_{n\ge1}A_nz^n=\frac{2z}{1-z}+\frac{z^2}{1-z^2}
+\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}
+\frac{z^4+z^7}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}.
\]

In particular, \(A_n=n^4/288+O(n^3)\). The initial values for lengths \(1\) through \(18\) are

`2, 3, 4, 6, 8, 13, 18, 27, 38, 53, 72, 98, 128, 167, 214, 271, 338, 419`.

These numbers also give the largest possible codes of binary necklaces distinguishable by their full circular three-gram multiplicity observations. All necklaces are distinguishable for lengths at most five. At length six, precisely one spectrum is shared by two necklaces, `001011` and `001101`; all other spectra identify a unique necklace. For every length at least six there is a collision.

## Assumptions and scope

A nonempty circular word is a nonempty finite sequence of zeroes and ones with positions indexed modulo its positive length \(n\). For each \(a,b,c\in\{0,1\}\), let \(h_{abc}\) be the number of indices \(i\in\{0,\ldots,n-1\}\) at which the circular length-three block is \(abc\). This definition includes wraparound and applies unchanged to lengths one and two, where positions are revisited within a block. Two such words have the same observation if all eight integers coincide. The observation determines both length and symbol content; a circular word and any rotation have identical observations. \(H_{p,q}\) counts possible observations, not distinct words, and \(H_{0,0}=0\).

The result concerns binary, circular, full-multiplicity, exact three-gram observations. It makes no statement about incomplete reads, errors, arbitrary alphabet sizes, or longer read lengths.

## Proof

**Flow reduction.** Interpret each length-three block \(abc\) as an edge from vertex \(ab\) to vertex \(bc\) in the binary order-two de Bruijn directed graph. A circular word yields a directed Eulerian circuit in the positive-edge multigraph. Equality of indegrees and outdegrees at the four vertices is equivalent to

\[
h_{001}=h_{100}=:t,\qquad h_{011}=h_{110}=:s,\qquad h_{010}+s=t+h_{101}.
\]

Set \(a=h_{000}\), \(h=h_{111}\), \(f=h_{101}\), and \(c=h_{010}=t+f-s\). Thus the full ordered vector, indexed by `000,001,010,011,100,101,110,111`, is

\[
(a,t,t+f-s,s,t,f,s,h).
\]

Every parameter is a nonnegative integer, with \(t+f-s\ge0\). The exact content constraints are

\[
p=a+2t+f,\qquad q=h+t+s+f.
\]

Conversely, nonnegative parameters meeting these conditions produce a circular word exactly when the vertices incident to positive edges are connected in the underlying undirected multigraph. Indeed, a finite balanced directed graph whose positive-edge support is connected has an Eulerian circuit, and reading the first symbol along that circuit recovers the required circular word. Loops at isolated vertices cannot be combined into one circuit. The proof consequently counts connected integer flows rather than walks or their possible multiple realizations.

**Exhaustive support classification.** The following five cases are mutually exclusive and exhaust all nonempty connected flows.

1. If \(t=s=0\), the equality \(c=f\) holds. Connectedness leaves precisely pure zero loops (\(a>0,h=f=0\)), pure one loops (\(h>0,a=f=0\)), or alternating cycles (\(f=c>0,a=h=0\)). Their bivariate series is \(x/(1-x)+y/(1-y)+xy/(1-xy)\).
2. If \(t>0,s=0\), the nontrivial component contains vertices `00,01,10`, so \(h=0\), while \(a\ge0\), \(t\ge1\), \(f\ge0\), and \(c=t+f\). The content is \((p,q)=(a+2t+f,t+f)\). Its series is \(x^2y/((1-x)(1-x^2y)(1-xy))\).
3. If \(t=0,s>0\), its complemented counterpart forces \(a=0\), with \(s\ge1\), \(c\ge0\), \(h\ge0\), and \(f=c+s\). Its series is \(xy^2/((1-y)(1-xy^2)(1-xy))\).
4. If \(t,s>0\) and \(t\ge s\), all four vertices lie in one connected component regardless of loops. Write \(s=r\ge1\), \(t=r+j\) with \(j\ge0\), \(f=k\ge0\), \(a,h\ge0\). The contribution is \(\frac{x^2y^2}{(1-x)(1-y)(1-x^2y^2)(1-x^2y)(1-xy)}\).
5. If \(t,s>0\) and \(s>t\), write \(t=r\ge1\), \(s=r+j\) with \(j\ge1\), and \(f=j+k\) with \(k\ge0\), so \(c=k\). The contribution is \(\frac{x^2y^2}{(1-x)(1-y)(1-x^2y^2)(1-xy)}\frac{xy^2}{1-xy^2}\).

For the last two cases, the positive edges \(001\), \(011\), \(110\), and \(100\) already form a directed four-vertex cycle. Therefore the displayed lower bounds are both necessary and sufficient for connectedness. Summing the five geometric series gives the stated bivariate identity. Setting \(x=y=z\) and simplifying gives the univariate identity, directly preserving the two pure-word series and the alternating series.

**Growth.** The final univariate term has a pole of order five at \(z=1\), with leading principal part \(1/[12(1-z)^5]\). Other terms have poles of order at most three there; nontrivial roots of unity are poles of order at most two. Therefore its coefficients satisfy \(A_n=(1/12)\binom{n+4}{4}+O(n^3)=n^4/288+O(n^3)\).

**Sharp reconstruction boundary.** The counting formula gives \((A_1,\ldots,A_6)=(2,3,4,6,8,13)\). The usual binary necklace count \(\frac1n\sum_{d\mid n}\varphi(d)2^{n/d}\) gives \((2,3,4,6,8,14)\) for these lengths. Since each observation comes from at least one necklace, equality of these two numbers through length five implies injectivity. For length six, the two distinct necklaces `001011` and `001101` share the vector \((0,1,1,1,1,1,1,0)\). Their single collision accounts for the whole one-unit discrepancy between fourteen necklaces and thirteen observations, so all remaining classes are singletons. For each length \(n\ge6\), add \(n-6\) zeroes to the unique two-zero run in each displayed word; the two circular three-gram histograms remain equal, since every added zero increases only the `000` count. Their necklaces remain distinct: their circular zero-gap triples, read between consecutive ones, are respectively distinct cyclic arrangements of \((n-4,0,1)\). This constructs collisions at every greater length.

Finally, selecting one necklace from each observable class gives a zero-error code of size \(A_n\), and no larger code can exist by pigeonhole principle. The fixed-content version has size \(H_{p,q}\).

## Verification

The included `verify_profiles.py` is standalone Python 3 code using only the standard library. Run `python3 verify_profiles.py`. It exhaustively enumerates all binary words through length eighteen, computing their cyclic three-gram histograms directly and independently comparing every fixed-content count to the five-case flow formula. It also constructs an Eulerian circuit for each feasible histogram with length at most twenty-two, tests the complete length-six collision classification, and tests the explicit padded collisions through length twenty-six. The actual replay produced:

`VERIFY_OK; direct_words=524286; constructed_profiles=4654; n<=18; constructions<=22; padded_pairs<=26`

These finite checks corroborate the all-length combinatorial proof; they are not substitutes for it.

## Relationship to prior work

The graph-flow observation is classical. Arnoux's *Note on occurrences of factors in circular words* (2016) establishes the Kirchhoff constraints and sufficiency of connected balanced multigraphs for circular factor counts. The present contribution is the **explicit fixed-symbol-content enumeration of all binary circular length-three observations**, its rational bivariate series, resulting asymptotics, and the first complete reconstruction-collision boundary. The existence criterion itself is not claimed as new.

Karhumäki, Saarela and Zamboni (2013) develop the general framework of linear \(k\)-abelian equivalence; Karhumäki, Puzynina, Rao and Whiteland (2016) investigate cardinalities of linear \(k\)-abelian equivalence classes, including Eulerian representations for fixed factor counts. Their linear boundary constraints and class-cardinality questions differ from counting feasible cyclic multiset observations by both length and composition. Cassaigne, Karhumäki, Puzynina and Whiteland (2016) analyze rational class-count sequences in the linear setting. A full version of this last specialized contribution was not available for line-by-line comparison; therefore historical priority for the precise rational functions remains a residual uncertainty.

## Limitations

Only length-three contiguous circular binary factor multiplicities are counted. The code bound assumes complete noise-free histograms, exact length, and all circular windows, and is a combinatorial packing statement rather than a practical sequencing protocol. The result does not classify the number of distinct necklaces per histogram at all lengths, nor does it generalize the generating function to arbitrary alphabet size or observation length. No independent mathematical audit or historical-priority certification has been performed.

## References

1. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104, first version 2013-01-22. https://arxiv.org/abs/1301.5104
2. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319, first version 2016-05-11. https://arxiv.org/abs/1605.03319
3. P. Arnoux, *Note on occurrences of factors in circular words*, RAIRO—Theoretical Informatics and Applications (2016). https://doi.org/10.1051/ita/2016019
4. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *k-Abelian Equivalence and Rationality*, DLT 2016. https://doi.org/10.1007/978-3-662-53132-7_7
