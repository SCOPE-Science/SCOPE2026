# Exact size-refined enumeration of every diameter-two Hamming anticode

## Finding

Let \(q\ge2\) and \(n\ge1\) be integers. A diameter-two anticode is any subset \(A\subseteq[q]^n\) with \(d_{\mathrm H}(x,y)\le2\) for all \(x,y\in A\), including the empty set. Put \(r=q-1\), and let \(c_{q,n}(k)\) count anticodes of cardinality \(k\). Their complete size-generating polynomial \(F_{q,n}(z)=\sum_{k\ge0}c_{q,n}(k)z^k\) satisfies \(F_{q,n}(0)=1\) and

\[
\boxed{\begin{aligned}
q^{-n}F'_{q,n}(z)={}&(1+nr)(1+z)^{nr}+\binom n2(1+z)^{r^2+2r}\\
&-\left(\binom n2+nr(n-1)\right)(1+z)^{2r}\\
&+nr(n-2)(1+z)^r+\binom n3r^3z^3.
\end{aligned}}
\]

In particular, for \(k\ge1\), with binomial coefficients interpreted as zero outside their range,
\[
\begin{aligned}
c_{q,n}(k)=\frac{q^n}{k}\bigg[&(1+nr)\binom{nr}{k-1}+\binom n2\binom{r^2+2r}{k-1}\\
&-\Big(\binom n2+nr(n-1)\Big)\binom{2r}{k-1}
+nr(n-2)\binom r{k-1}\\
&+\mathbf 1_{k=4}\binom n3r^3\bigg],\qquad c_{q,n}(0)=1.
\end{aligned}
\]

This is a counting identity for all sizes, not merely a maximum or an asymptotic order. For fixed \(q\) as \(n\to\infty\), it also gives
\[
|\mathcal A_q(n,2)|=q^n2^{1+(q-1)n}\left(1+O_q\bigl(n^3 2^{-(q-1)n}\bigr)\right).
\]
Almost every such anticode lies in a unique Hamming ball of radius one, and its cardinality is asymptotically binomial with parameters \(1+(q-1)n\) and \(1/2\), in total variation. The total binary count alone is known from OEIS A295922; the target here is the full alphabet-uniform size spectrum and its refined asymptotic consequence.

## Assumptions and scope

The alphabet \([q]=\{0,1,\ldots,q-1\}\) is labeled; no field operation is needed. Coordinates are labeled, and subsets, not multisets or linear subspaces, are counted. Hamming distance is the number of unequal coordinates. The convention \(\binom ab=0\) when \(b<0\) or \(b>a\) applies, and \(\operatorname{diam}(\varnothing)=0\). Parameters are all integers \(q\ge2\) and \(n\ge1\); the asymptotic statement fixes \(q\) and takes \(n\to\infty\).

## Proof

**1. Reduce to a rooted family.** Coordinatewise permutations of the alphabet act transitively on \([q]^n\) and preserve Hamming distance, so fix an arbitrary distinguished word and rename it \(0^n\). Let \(G_{q,n}(z)\) count anticodes containing \(0^n\), with each such anticode weighted by \(z^{|A|-1}\). Double-count pairs \((A,x)\) where \(x\in A\): if \(F_{q,n}(z)=\sum_k c_{q,n}(k)z^k\), then
\[
F'_{q,n}(z)=q^n G_{q,n}(z).
\]

**2. Classify descendants of the anchor.** Every other word of a diameter-two anticode containing \(0^n\) has weight one or two. Denote the selected weight-one words by \(S\) and selected weight-two words by \(T\). Two weight-two words with disjoint two-coordinate supports have distance four. If their supports meet in exactly one coordinate, they have distance at most two if and only if their two nonzero symbols agree in the shared coordinate. A weight-one word is compatible with every word in \(T\) if and only if its coordinate belongs to every support represented in \(T\); its nonzero symbol is unrestricted.

The family of distinct two-element supports in \(T\) must therefore be pairwise intersecting. Such a family is either a star (all supports share one coordinate), or exactly the three edges of a triangle. Indeed, take distinct supports \(\{a,b\}\) and \(\{a,c\}\): any support not containing \(a\) must be \(\{b,c\}\), and if it occurs no other support is compatible with all three.

**3. Four exhaustive, disjoint cases.** Write \(u=1+z\) and \(r=q-1\). If \(T\) is empty, any of the \(nr\) weight-one words can be selected, contributing \(u^{nr}\).

If \(T\) uses exactly one two-coordinate support, choose the support in \(\binom n2\) ways, a nonempty subset of the \(r^2\) words supported there, and any subset of the \(2r\) weight-one words on those coordinates. The contribution is \(\binom n2(u^{r^2}-1)u^{2r}\).

If there are at least two different supports forming a star, their common coordinate is unique. Choose its coordinate (\(n\) choices) and common nonzero value (\(r\) choices). Choose at least two partner coordinates, with a nonempty subset of the \(r\) allowable weight-two words for each partner. The only allowable weight-one words are the \(r\) words on the center coordinate. This gives
\[
nr u^r\left[u^{r(n-1)}-1-(n-1)(u^r-1)\right].
\]

Finally, a triangle requires exactly three weight-two words. Their shared-symbol conditions uniquely prescribe one nonzero symbol at each of the three coordinates. No weight-one word is compatible with all three. This yields \(\binom n3 r^3z^3\).

Summing gives the **nonnegative case partition**
\[
\begin{aligned}
G_{q,n}(z)={}&u^{nr}+\binom n2(u^{r^2}-1)u^{2r}\\
&+nr u^r\left[u^{r(n-1)}-1-(n-1)(u^r-1)\right]+\binom n3r^3z^3.
\end{aligned}
\]
Expanding and collecting powers of \(u\) gives the displayed five-term identity. This is a polynomial identity, valid at all stated parameters including \(n=1,2\). Extracting coefficients in \(F'=q^nG\) proves the formula for every size.

**4. Sharp leading asymptotic and typical geometry.** Integrate the five-term identity from zero to one. The first term integrates to \(2^{nr+1}-1\); for fixed \(q\), the other terms contribute \(O_q(n^3)\), since their exponential bases have fixed exponents and their coefficients have degree at most three in \(n\). Therefore the total is \(q^n2^{nr+1}+O_q(q^n n^3)\).

Every anchored anticode in the empty-\(T\) or nontrivial-star cases lies in a radius-one Hamming ball (centered respectively at the anchor or at the distinguished star symbol). Any anchored anticode using a single two-coordinate support lies in a two-coordinate plane containing only \(q^2\) words; a triangle case has just four words. Thus **every anticode not contained in a radius-one ball has size at most \(q^2\)**, and their total number is \(O_q(q^n n^3)\) by counting the two exceptional case families for each anchor.

Two distinct radius-one balls meet in at most \(q\) words: for centers at distance one their intersection is a coordinate line of \(q\) words, for centers at distance two it has two words, and for larger distances it is empty. Each center has \(O_q(n^2)\) other centers within distance two. Hence the number of anticode subsets counted at least twice among all radius-one balls is at most \(O_q(q^n n^2 2^q)\). All \(q^n\) balls have \(1+nr\) words. Therefore sampling an anticode uniformly differs, in total variation by \(O_q(n^3 2^{-nr})\), from sampling a uniformly random subset of a uniformly chosen radius-one ball. This latter subset has cardinality \(\operatorname{Binomial}(1+nr,1/2)\). A random subset of the ball is unique to that ball with probability tending to one. This proves both final consequences.

## Verification

The standalone standard-library program `verify_diameter2_anticodes.py` enumerates all subsets that are cliques in the Hamming-distance-at-most-two graph by an independent ascending-vertex backtracking algorithm. It compares the complete cardinality histograms with the formula for all binary lengths \(1\) through \(8\), ternary lengths \(1\) through \(4\), quaternary lengths \(1\) through \(3\), and quinary lengths \(1\) through \(2\). It also checks integer coefficients and edge counts for \(q=2,\ldots,8\), \(n=1,\ldots,20\), and checks the previously known OEIS binary total through length \(20\). Run `python3 verify_diameter2_anticodes.py`; exact expected output is supplied in `verify_diameter2_anticodes_output.txt`.

These finite checks corroborate the formula and boundary cases; the all-parameter proof is the structural four-case partition above.

## Relationship to prior work

Horlemann and Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces* (arXiv:2610.31618v1, first submitted 2026-10-22), Proposition 3.4, prove only \(2^{\Theta_q(n)}\) growth for diameter two while giving an exact expression for diameter one. Their argument does not enumerate the size-refined diameter-two family. Classical diametric theorems determine the largest possible size, not the total counts by every size.

**Important existing coverage:** OEIS A295922 (2017) already gives the exact total number of binary diameter-two anticodes, expressed as cliques of the halved \((n+1)\)-cube (equivalently the square of the \(n\)-cube). That established total-count specialization is recovered but is not a new claim. The new claim is the all-size generating polynomial for every alphabet size, together with the all-alphabet sharp leading constant and typical-structure result. Searches for a q-ary clique polynomial, diameter-two anticode histograms and equivalent Hamming-graph-square formulations did not identify broader covering coverage.

## Limitations

The complete count concerns diameter at most two, not diameter exactly two. It counts arbitrary subsets of a labeled product alphabet, not linear anticodes or codes with prescribed minimum distance. It does not enumerate diameter-three anticodes. Asymptotic conclusions assume the alphabet size remains fixed. The absence of an identified equivalent formula does not establish exhaustive publication priority. Independent mathematical validation has not been performed.

## References

- A.-L. Horlemann and A. Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (2026-10-22), https://arxiv.org/html/2610.31618v1 , especially Proposition 3.4.
- OEIS Foundation, A295922, *Number of (not necessarily maximal) cliques in the n-halved cube graph*, entry created 2017-11-30, https://oeis.org/A295922 .
- *Halved cube graph*, https://en.wikipedia.org/wiki/Halved_cube_graph , equivalent description as a cube-square graph.
- E. W. Weisstein, *Clique Polynomial*, MathWorld, https://mathworld.wolfram.com/CliquePolynomial.html , definition of the size-resolved graph invariant.
