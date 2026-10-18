# All minimum circular attractors of a one-gap perturbation of a periodic binary word

## Finding

For all integers \(m\ge 2\), \(q\ge 1\), and \(s\ge 1\), consider the binary word
\[
W_{m,q,s}=(1 0^{q-1})^m0^s,\qquad N=mq+s.
\]
Treat positions as \(0,\ldots,N-1\), read cyclically. The circular string-attractor number of this word is exactly \(2\). All its minimum attractors, with no exceptions, are the unordered pairs
\[
\{jq,(m-1)q+t\},\qquad
0\le j<m,\quad 1\le t<q+s,
\]
that satisfy both
\[
(j=m-1\ \text{or}\ t\le q)
\quad\text{and}\quad
(j=0\ \text{or}\ t\ge s).
\]
The total number of minimum attractors is exactly
\[
\boxed{2q+(m-2)\max\{q-s+1,0\}}.
\]
More strongly, for every position subset (of any cardinality), being a circular string attractor is *equivalent* to crossing some circular occurrence of each of the following four factors:
\[
1,\qquad 0^q,\qquad 10^q,\qquad 0^q1.
\]
This constant-size testing basis is part of the theorem, not merely an experimental observation.

## Assumptions and scope

A nonempty circular factor is a word of length between \(1\) and \(N\) read from consecutive cyclic positions of \(W_{m,q,s}\). For such a factor \(u\), define its *coverage set* \(C(u)\) to be the union of the positions crossed by **all** of its circular occurrences. A position set \(\Gamma\) is a circular string attractor precisely when \(\Gamma\cap C(u)\ne\varnothing\) for every nonempty circular factor \(u\). One occurrence may be chosen separately for each factor. Coordinates are zero-based; words are not required to be considered up to rotation when specifying the positions. The parameters \(m,q,s\) range over **all integers** satisfying the inequalities above.

Set \(L=(m-1)q\). The positions occupied by the \(1\)s and by the unique longest zero-run are, respectively,
\[
O=\{jq:0\le j<m\},\qquad R=\{L+1,\ldots,N-1\}.
\]
These sets are disjoint and nonempty; the long zero-run has length \(q+s-1\), while the other zero-runs have length \(q-1\), possibly zero.

## Proof

**Step 1: the four required coverage sets.** The single-letter factor \(1\) has \(C(1)=O\). The factor \(0^q\) occurs only in the long zero-run, and its length-\(q\) windows cover that entire run, so \(C(0^q)=R\). The factor \(10^q\) has exactly one circular occurrence, beginning at the final \(1\) at position \(L\); thus
\[
C(10^q)=P=\{L,L+1,\ldots,mq\}.
\]
Similarly, \(0^q1\) occurs uniquely at the boundary before the initial \(1\), giving
\[
C(0^q1)=Q=\{N-q,N-q+1,\ldots,N-1,0\}.
\]
The uniqueness follows because every other gap between consecutive \(1\)s has only \(q-1\) zeros; the exceptional cyclic gap has \(q+s-1\ge q\) zeros.

**Step 2: completeness of the four-factor basis.** We show that, for every nonempty circular factor \(u\), the set \(C(u)\) contains at least one of \(O,R,P,Q\). If \(u\) consists only of zeros, its length cannot exceed \(q+s-1\); sliding an occurrence of \(u\) across the exceptional zero-run shows \(C(u)\supseteq R\). If \(u\) contains \(10^q\), the unique occurrence of that subfactor forces every occurrence of \(u\) to cover \(P\); hence \(C(u)\supseteq P\). Likewise, if \(u\) contains \(0^q1\), then \(C(u)\supseteq Q\).

The remaining case has at least one \(1\) but contains neither boundary factor. Write \(h\) for the number of \(1\)s in \(u\). Such a factor cannot cross the exceptional gap between the last and first \(1\)s. Any two consecutive \(1\)s inside it are separated by exactly \(q-1\) zeros, and its leading and trailing zero blocks have lengths at most \(q-1\). Therefore, with \(1\le h\le m\) and \(0\le a,b\le q-1\),
\[
u=0^a1(0^{q-1}1)^{h-1}0^b.
\]
For every \(j=0,\ldots,m-h\), this factor occurs at cyclic start position \(jq-a\pmod N\), spanning the consecutive \(1\) positions \(jq,(j+1)q,\ldots,(j+h-1)q\). These occurrences jointly cross *every* position in \(O\), because every \(1\) belongs to at least one length-\(h\) block among the \(m\) displayed \(1\)s. Hence \(C(u)\supseteq O\).

Consequently, any set intersecting \(O,R,P,Q\) intersects the coverage set of *every* factor; conversely, every circular attractor intersects these four particular factor-coverage sets. This proves the claimed exact four-factor basis for arbitrary position subsets.

**Step 3: optimum and all minimizers.** Since \(O\cap R=\varnothing\), any attractor has at least two positions. An attractor with exactly two positions must choose one from each set. Thus it has the unique form
\[
\Gamma=\{jq,L+t\},\qquad 0\le j<m,\quad 1\le t<q+s.
\]
The pair meets \(P\) exactly when \(j=m-1\) or \(t\le q\), and meets \(Q\) exactly when \(j=0\) or \(t\ge s\). Step 2 proves that these two conditions are sufficient as well as necessary. Such pairs always exist (choose \(j=0\), \(t=1\)), proving the optimum is exactly two. For \(j=0\), exactly \(q\) values of \(t\) are allowed; for \(j=m-1\), exactly \(q\); for each of the \(m-2\) other values of \(j\), there are \(\max\{q-s+1,0\}\) choices. Summing gives the displayed formula. \(\square\)

## Verification

Run `python3 checker.py` using only the Python standard library. The program literally enumerates every distinct circular factor of every word for all \(2\le m\le7\), \(1\le q\le6\), and \(1\le s\le7\): a total of \(252\) parameter triples and \(79,142\) factor instances after deduplication per word. It checks that each factor-coverage set contains at least one of the four witness coverage sets. It independently enumerates all position pairs and compares the successful pairs, *not merely their number*, against the theorem's classification. The exact recorded output is in `check_output.txt`; the verification reports all checks passed. This computation supports the proof but cannot, by itself, establish the theorem for all parameters.

For example, \((m,q,s)=(5,4,3)\) has \(N=23\), attractor size \(2\), and exactly \(14\) optimum pairs. For fixed \(m\ge3\) and \(q\), the count has a strict linear-to-constant transition at \(s=q+1\): for smaller \(s\) it is \(2q+(m-2)(q-s+1)\), and for \(s\ge q+1\) it equals \(2q\).

## Relationship to prior work

Mantaci, Restivo, Romana, Rosone, and Sciortino introduced circular string attractors and proved that the existence of an attractor formed by *consecutive* positions characterizes the conjugacy class of a standard Sturmian word among primitive words (Theorem 34). That statement neither classifies *all* optimal position pairs for the present three-parameter family nor proves the four-factor testing basis. In the boundary case \(s=1\), the present word is a conjugate of a Christoffel word; the present enumeration specifies all optimal pairs, including nonconsecutive ones, and the parameter \(s>1\) covers the non-Christoffel gap perturbations. Romana's subsequent circular-attractor work concerns checking complexity and general hardness, not this exact family.

Banbara et al. (first circulated February 18, 2026) characterize all minimum *ordinary, noncircular* string attractors of Fibonacci and period-doubling words (the later version also treats Thue–Morse). Their exact multiplicity viewpoint motivates seeking a corresponding complete enumeration for circular words, but their objects and their occurrence convention differ. Other published studies of exact optimal-attractor counts concern distinct morphic or pseudostandard families rather than the one-exceptional-gap words analyzed here.

## Limitations

The theorem concerns **circular** factors (not linear substrings) and precisely the family \((10^{q-1})^m0^s\); it does not assert a corresponding result for multiple exceptional gaps, arbitrary binary words, or ordinary string attractors. No independent external scientific audit was performed. Priority comparisons cover the inspected primary literature and available indexed research records; an equivalent result in unindexed or unpublished literature cannot be excluded.

## References

1. S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino. *A combinatorial view on string attractors*. Theoretical Computer Science 850 (2021), 236–248. DOI: 10.1016/j.tcs.2020.11.006. Public postprint: https://iris.unipa.it/handle/10447/463264.
2. G. Romana. *Algorithmic View on Circular String Attractors*. ICTCS 2023, pp. 169–180. https://ceur-ws.org/Vol-3587/9885.pdf.
3. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto. *The Smallest String Attractors of Fibonacci and Period-Doubling Words*. arXiv:2602.16152, first submission February 18, 2026; CPM 2026. https://arxiv.org/abs/2602.16152.
