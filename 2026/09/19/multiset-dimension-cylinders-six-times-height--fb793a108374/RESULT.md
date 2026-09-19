# Three-point multiset bases for cylindrical grids at circumference six times the height

## Result

Let \(P_m\square C_n\) be the Cartesian product of the path of order \(m\) and the cycle of order \(n\), and let \(\operatorname{md}(G)\) denote the multiset dimension. For every \(m\ge 2\),

\[
\operatorname{md}(P_m\square C_n)=3
\]

in each of the following ranges:

1. \(n\ge 6m+3\);
2. \(m\) even and \(n\in\{6m-1,6m+2\}\);
3. \(m\) odd and \(n\in\{6m,6m+1\}\).

Equivalently, the uniform tail improves the previously proved sufficient condition \(n\ge 8m+1\) to \(n\ge 6m+3\), with several additional boundary families. For even \(m\), the theorem gives all \(n\ge6m+2\) and also \(n=6m-1\); for odd \(m\), it gives \(n=6m,6m+1\) and all \(n\ge6m+3\).

The case \(m=2\) is not new: prisms are already known exactly. It is included to make the construction uniform. The new range is principally relevant for \(m\ge3\).

## Definitions

For a graph \(G\), a set \(W\subseteq V(G)\) is an *m-resolving set* if the multisets

\[
r_W(v)=\{d(v,w):w\in W\}
\]

are distinct for all distinct vertices \(v\). The minimum size of such a set, when one exists, is \(\operatorname{md}(G)\).

Fix a three-set \(W\subseteq V(C_n)\). For \(x\in V(C_n)\), write its three distances to \(W\), in nondecreasing order, as

\[
a_W(x)\le b_W(x)\le c_W(x).
\]

Define the *height* and *gap code*

\[
h_W(x)=a_W(x),\qquad
\Delta_W(x)=\bigl(b_W(x)-a_W(x),\ c_W(x)-b_W(x)\bigr).
\]

For an integer \(q\ge1\), call \(W\) *q-separated* if

\[
\Delta_W(x)=\Delta_W(y),\ x\ne y
\quad\Longrightarrow\quad
|h_W(x)-h_W(y)|\ge q.
\]

This is a finite-height relaxation of the strong m-resolving condition used in earlier work: repeated gap codes are allowed, provided the corresponding distance multisets are separated by a sufficiently large common translation.

## Quantitative lifting lemma

**Lemma.** If a three-set \(W\subseteq V(C_n)\) is \(q\)-separated, then

\[
W^0=\{(0,w):w\in W\}
\]

is an m-resolving set of \(P_m\square C_n\) for every \(m\le q\).

**Proof.** For a vertex \((i,x)\), Cartesian-product distances give

\[
r_{W^0}(i,x)=
\{i+d_{C_n}(x,w):w\in W\}.
\]

After sorting, this is

\[
(a_W(x)+i,\ b_W(x)+i,\ c_W(x)+i).
\]

Thus adding the path coordinate changes the height from \(h_W(x)\) to \(h_W(x)+i\) but leaves \(\Delta_W(x)\) unchanged. If \((i,x)\) and \((j,y)\) have equal m-codes, then their gap codes are equal and

\[
h_W(x)+i=h_W(y)+j.
\]

If \(x\ne y\), q-separation gives \(|h_W(x)-h_W(y)|\ge q\), whereas
\(|i-j|\le m-1\le q-1\), a contradiction. Hence \(x=y\), and then equality of the smallest entries forces \(i=j\). \(\square\)

## A six-residue family of q-separated triples

Let \(q\ge2\), \(0\le r\le5\), and

\[
n=6q+3+r.
\]

Choose three landmarks on \(C_n\) whose successive cyclic arc lengths are \((A,B,C)\), and place them at

\[
W=\{0,A,A+B\}.
\]

For even \(q\), use

| \(r\) | \((A,B,C)\) | repeated equal-gap pairs \(x,y\), with heights \(h(x),h(y)\) |
|---:|---|---|
| 0 | \((q+2,2q-1,3q+2)\) | \((q,4q+3):(2,q+2)\); \((q+1,4q+2):(1,q+1)\); \((q+2,4q+1):(0,q)\) |
| 1 | \((q+1,2q+2,3q+1)\) | \((q+1,4q+3):(0,q)\) |
| 2 | \((q+2,2q+1,3q+2)\) | \((q+1,4q+4):(1,q+1)\); \((q+2,4q+3):(0,q)\) |
| 3 | \((q+1,2q+2,3q+3)\) | \((q+1,4q+4):(0,q+1)\) |
| 4 | \((q+2,2q+3,3q+2)\) | \((q+2,4q+5):(0,q)\) |
| 5 | \((q+1,2q+4,3q+3)\) | \((q+2,4q+6):(1,q+1)\) |

For odd \(q\), use

| \(r\) | \((A,B,C)\) | repeated equal-gap pairs \(x,y\), with heights \(h(x),h(y)\) |
|---:|---|---|
| 0 | \((q+1,2q+1,3q+1)\) | \((q+1,4q+2):(0,q)\) |
| 1 | \((q,2q+2,3q+2)\) | \((q+1,4q+3):(1,q+1)\) |
| 2 | \((q+1,2q+1,3q+3)\) | \((q+1,4q+3):(0,q+1)\) |
| 3 | \((q+2,2q+2,3q+2)\) | \((q+1,4q+5):(1,q+1)\); \((q+2,4q+4):(0,q)\) |
| 4 | \((q+3,2q+1,3q+3)\) | \((q+1,4q+6):(2,q+2)\); \((q+2,4q+5):(1,q+1)\); \((q+3,4q+4):(0,q)\) |
| 5 | \((q+2,2q+2,3q+4)\) | \((q+1,4q+6):(1,q+2)\); \((q+2,4q+5):(0,q+1)\) |

**Cycle-separation lemma.** In every row of these tables, the displayed pairs are exactly the pairs of distinct cycle vertices with equal gap code. In particular, every displayed height difference is at least \(q\), so \(W\) is q-separated.

**Verification of the table.** For a fixed triple of landmarks, each of the three raw cycle-distance functions is V-shaped and is affine with slope \(+1\) or \(-1\) between a landmark and its antipode. The landmarks and antipodes therefore split the cycle into at most six intervals on which the ordered distance triple has fixed affine formulas. On each interval \(\Delta_W\) is affine; equating the two gap coordinates for two such interval formulas gives linear equations in the two vertex positions. Substituting the listed \((A,B,C)\) and resolving the endpoint cases gives exactly the repeated pairs in the tables above; all remaining gap codes occur once. The displayed heights are obtained by direct substitution in the minimum of the three cycle distances. This is a finite calculation for the twelve parity/residue cases. The accompanying verifier independently recomputes the cycle distances from the definition and checks these exact repeated-pair descriptions over a large parameter range.

## Boundary q-separated triples

The same calculation yields four additional families. For even \(q\),

\[
\begin{array}{c|c|c}
 n & W & \text{repeated equal-gap pairs with heights}\\ \hline
6q-1 & \{0,q,3q-1\} & (q,4q-1):(0,q)\\
6q+2 & \{0,q+1,3q+1\} & (q,4q+2):(1,q+1),\ (q+1,4q+1):(0,q)
\end{array}
\]

and for odd \(q\),

\[
\begin{array}{c|c|c}
 n & W & \text{repeated equal-gap pairs with heights}\\ \hline
6q & \{0,q,3q\} & (q,4q):(0,q)\\
6q+1 & \{0,q+1,3q\} & (q,4q+1):(1,q+1),\ (q+1,4q):(0,q).
\end{array}
\]

Thus every one of these triples is q-separated.

## Proof of the theorem

For the uniform tail \(n\ge6m+3\), set

\[
q=\left\lfloor\frac{n-3}{6}\right\rfloor,
\qquad
r=n-(6q+3).
\]

Then \(0\le r\le5\) and \(q\ge m\). The six-residue construction gives a q-separated three-set on \(C_n\), and the lifting lemma gives an m-resolving three-set on \(P_m\square C_n\). Hence \(\operatorname{md}(P_m\square C_n)\le3\).

For the boundary cases, take \(q=m\) in the appropriate boundary construction and apply the same lifting lemma.

Finally, \(P_m\square C_n\) is connected and is not a path. It is known that no connected graph has multiset dimension 2 and that a nontrivial connected graph has multiset dimension 1 exactly when it is a path. Therefore every constructed upper bound of 3 is exact.

## Relation to prior work

Marcelo, Tolentino, Garciano and Buot proved in 2025 that all cylindrical graphs have finite multiset dimension and, in particular,

\[
\operatorname{md}(P_m\square C_n)=3
\quad\text{for }m\ge2,\ n\ge8m+1.
\]

They explicitly left the remaining cylindrical cases open. Their paper also uses strong m-resolving sets and gap-code (\(\Delta d\)) arguments to lift resolving sets through Cartesian products. The present result uses the same basic distance-code language but a different quantitative mechanism: equal gap codes are permitted when their common-translation offsets are separated by at least the path height. This allows three landmarks where a globally strong three-set is unavailable and reduces the uniform circumference coefficient from 8 to 6.

The exact prism case \(m=2\) was already known: \(\operatorname{md}(P_2\square C_n)=3\) for \(n\ge11\), except \(n=13\). Accordingly, no originality is claimed for the individual \(m=2\) instances recovered here.

A 2026 survey still records the \(n\ge8m+1\) cylindrical three-basis range and does not contain the constructions above. Searches under multiset dimension, m-resolving sets, ID-coloring, strong ID-coloring, cylindrical grids, Cartesian products, and equivalent threshold formulations found no prior \(6m\)-scale three-basis theorem. The originality assessment is therefore to the best of our knowledge.

## Verification

`artifacts/verify.py` uses only exact integer cycle distances. It checks the asserted repeated-gap pairs and q-separation for all six tail residues for \(2\le q\le500\), checks the four boundary families over the same q range, and directly verifies pairwise distinct cylindrical m-codes for the stated constructions for \(2\le m\le30\) over representative tail and boundary instances. The recorded output is in `artifacts/verification.txt`.

These finite checks support the symbolic proof but do not replace it.

## Limitations

The theorem gives a substantially improved sufficient region, not an exact transition for every \((m,n)\). Cases below the stated ranges can also have multiset dimension 3; the already known prism classification demonstrates that phenomenon. No necessity claim is made for the \(6m\)-scale thresholds. The precise remaining cylindrical cases therefore stay open.

The literature search cannot exclude a differently phrased older result or a very recent unindexed parallel result. No specific inaccessible source was identified as especially likely to contain the same \(6m\)-scale theorem.

## References

1. R. M. Marcelo, M. A. C. Tolentino, A. D. Garciano, J. C. Buot, “On multiset dimension of cylindrical graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 126 (2025), 225–240. https://doi.org/10.61091/jcmcc126-15
2. R. Marcelo, M. Tolentino, A. Garciano, M. Ruiz, J. Buot, “On the Vertex Identification Spectra of Grids,” *Journal of Interconnection Networks* 25(1) (2025), 2450002. https://doi.org/10.1142/S0219265924500026
3. R. M. Marcelo, A. D. Garciano, J. C. Buot, M. A. C. Tolentino, “Multiset dimension of prisms,” *Communications in Combinatorics and Optimization* (2025). https://doi.org/10.22049/cco.2025.29101.1852
4. A. Albejani, Y. Lin, J. Ryan, K. A. Sugeng, “A Survey on Multiset Dimension and Its Variations,” arXiv:2607.08128 (2026). https://arxiv.org/abs/2607.08128
