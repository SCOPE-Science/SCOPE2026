# Exact nonzero-product commuting pairs in interval-translation rook monoids

## Finding

For the finite inverse monoid \(M_n\) of all interval-to-interval partial translations on \([n]=\{1,\ldots,n\}\), including the empty map, the number of **ordered commuting pairs of nonzero elements with nonzero common product** is, for every integer \(n\ge2\),

\[
P_n=\binom{n+1}{2}^{2}-2\binom{n+2}{4}+4\binom{n+3}{5}+2\binom{n+1}{4}
=\frac{n(n+1)(2n^3+23n^2-3n+8)}{60}.
\]

The four summands count, respectively, overlapping idempotent interval pairs (the first two terms together), pairs with exactly one nonzero translation shift, and pairs with two nonzero shifts of the same sign. **Opposite nonzero shifts never commute with a nonempty common product.** The two same-sign classes are each equinumerous with \(\binom{n+1}{4}\).

The total number of ordered commuting pairs, now without restrictions on either element or their product, is

\[
C_n=\frac{2n^6+8n^5+25n^4+50n^3+63n^2+32n+60}{60}.
\]

Writing \(N_n=|M_n|=1+n(n+1)(2n+1)/6\), this yields the sharp finite-size expansion

\[
\frac{C_n}{N_n^2}=\frac3{10}+\frac{3}{10n}+\frac{15}{8n^2}+O(n^{-3}),
\qquad \Pr(xy\ne0\mid xy=yx)=\frac1n+O(n^{-2}),
\]

where \((x,y)\) is sampled uniformly from \(M_n^2\). The previously established leading \(3/10\) limit and the mutually annihilating-pair count are treated as context, not as the new contribution.

## Assumptions and scope

Fix an integer \(n\ge2\). For each \(1\le r\le n\) and \(1\le a,b\le n-r+1\), let \(\tau_{a,b,r}\) be the partial injective map with domain \([a,a+r-1]\), defined there by \(\tau_{a,b,r}(a+j)=b+j\) for \(0\le j<r\). Set \(M_n=\{0\}\cup\{\tau_{a,b,r}\}\), where \(0\) is the empty partial map. Products are compositions, first applying the left factor and then the right factor. The integer \(d=b-a\) is the translation shift, and shift zero is equivalent to being a nonzero idempotent. The monoid is the consecutive-diagonal inverse submonoid of the rook monoid studied by G. Fikioris and G. Fikioris [1,2].

All pairs are **ordered** and no quotient by conjugation or by interchange of factors is taken. Nonzero common product requires equality \(xy=yx\ne0\), distinct from mere commutation with \(xy=yx=0\). Write \(\binom mk=0\) for \(m<k\), with \(m,k\) nonnegative integers. The asymptotics hold as integer \(n\to\infty\).

## Proof

**1. A necessary and sufficient domain criterion.** Write the source intervals of nonzero \(x,y\) as \([a,b]\), \([c,f]\), and their shifts as \(d,e\). Then \(xy\) has shift \(d+e\) and source
\[
[a,b]\cap[c-d,f-d],
\]
while \(yx\) has the same shift and source
\[
[c,f]\cap[a-e,b-e].
\]
Each nonempty intersection is an integer interval. Consequently, \(xy=yx\ne0\) if and only if the common endpoints \(u\le v\) satisfy
\[
u=\max(a,c-d)=\max(c,a-e),\qquad
v=\min(b,f-d)=\min(f,b-e).
\]
This reduction follows directly by tracing the domain of each composite; there is no assumption that a nonempty product is invertible.

**2. Two zero shifts.** An element of shift zero is the partial identity on its interval. Two such maps multiply to the partial identity on their intersection, so they commute with nonzero product exactly when the two intervals intersect. There are \(\binom{n+1}{2}\) nonempty intervals. Ordered disjoint interval pairs number \(2\binom{n+2}{4}\): order the disjoint intervals left to right, choose their two positive lengths and the three surrounding nonnegative gaps, and multiply by two for their reversal. Thus this class contains
\[
E_n=\binom{n+1}{2}^{2}-2\binom{n+2}{4}
\]
pairs.

**3. Exactly one zero shift.** Suppose \(x\) has positive shift \(d>0\), domain \([a,b]\), and \(y\) is the partial identity on \([c,f]\). In the endpoint criterion with \(e=0\), equality and nonemptiness force \(c\le a\) and \(f\ge b+d\), and conversely these inequalities suffice. Equivalently, \(y\)'s interval contains the convex hull of the source and image of \(x\). If the hull has length \(s=r+d\ge2\) and starts at \(a\), there are \(s-1\) choices of positive length and shift and \(a(n-a-s+2)\) containing intervals \([c,f]\). Summing over \(a\) gives
\[
\sum_{a=1}^{n-s+1} a(n-a-s+2)=\binom{n-s+3}{3}.
\]
The positive-shift class therefore has \(\sum_{s=2}^n(s-1)\binom{n-s+3}{3}=\binom{n+3}{5}\) pairs. Reflecting the chain changes the shift's sign and swapping the two factors changes which shift vanishes; these yield four disjoint classes. Their total is \(4\binom{n+3}{5}\).

**4. Two nonzero shifts.** If \(d>0\) and \(e<0\), write \(u\) for a nonempty common left endpoint. Because \(a-e>a\), the equality \(u=\max(c,a-e)\) implies \(a<u\). Then \(u=\max(a,c-d)\) forces \(c-d=u\), hence \(c>u\), contradicting \(u\ge c\). Reflection handles \(d<0<e\). Thus opposite signs are impossible.

If \(d,e>0\), the two left-endpoint equations give \(a=c=u\): the second maximum must be attained at \(c\) because \(a-e<a\), and the first at \(a\) because \(c-d<c\). The right-endpoint equations then give \(b=v+e\) and \(f=v+d\). Conversely, for arbitrary integers \(u,v,d,e\) with \(1\le u\le v\), \(d,e\ge1\), and \(v+d+e\le n\), the two maps with source intervals \([u,v+e]\) and \([u,v+d]\) and shifts \(d\) and \(e\) commute with nonzero product on \([u,v]\). This is a unique parametrization. Put \(t=v-u+1\ge1\); its count is
\[
\sum_{\substack{d,e,t\ge1\\d+e+t\le n}}(n-d-e-t+1)=\binom{n+1}{4}.
\]
Reflection gives the identical negative-negative count. Summing the disjoint classes proves the formula for \(P_n\); elementary binomial simplification gives its polynomial form.

**5. From nonzero products to all commuting pairs.** For completeness, the mutually annihilating-pair count is
\[
Z_n=\#\{(x,y)\in(M_n\setminus\{0\})^2:xy=yx=0\}
=\sum_{\substack{r,s\ge1\\r+s\le n}}
[(n-r-s+1)(n-r-s+2)]^2
=\frac{n(n-1)(n+1)(n+2)(n^2+n-1)}{30}.
\]
Indeed, fixing the source and image lengths \(r,s\) of \(x,y\), the condition \(xy=0\) requires the image interval of \(x\) to be disjoint from the source interval of \(y\), and independently \(yx=0\) requires the image of \(y\) to be disjoint from the source of \(x\). The number of ordered disjoint placements of lengths \(r,s\) is \((n-r-s+1)(n-r-s+2)\), and the two choices are independent. This is included to make the all-pair count self-contained; neither \(Z_n\) nor its leading-order consequence is asserted as newly discovered. Precisely \(2N_n-1\) ordered pairs have a zero factor, and all commute. Thus \(C_n=Z_n+P_n+2N_n-1\). Substitution yields the displayed degree-six polynomial. Division by \(N_n^2\) gives the exact asymptotic coefficients. Since \(P_n\sim n^5/30\) and \(C_n\sim n^6/30\), the conditional probability is \(1/n+O(n^{-2})\).

## Verification

The accompanying standalone `verify.py` constructs every partial map as a length-\(n\) tuple (using `-1` for undefined), composes all ordered pairs directly, and compares the resulting counts with the closed formulas and the four shift-sign classes. It exhaustively verifies every \(1\le n\le10\), including the empty map and small-size boundary cases, reporting `VERIFY_OK 10 exact direct-map enumerations; four nonzero-product shift classes`. This test does not use the interval-domain derivation and hence separately checks it at those finite sizes. The proof above, rather than these finite cases, covers arbitrary \(n\).

Selected exact outputs are \((N_2,P_2,C_2)=(6,11,26)\), \((N_5,P_5,C_5)=(56,409,1332)\), and \((N_{10},P_{10},C_{10})=(386,7843,51778)\). Reproduce with `python3 verify.py` from the extracted package directory; only Python's standard library is needed.

## Relationship to prior work

Fikioris and Fikioris introduced and analyzed the consecutive-diagonal rook submonoid, including its triple product and its idempotent/nilpotent decomposition [1]. Their later extension [2] studies a larger real-parameter monoid and related structural properties, rather than this exact commuting-pair enumeration. Earlier counting information for the integer monoid determines \(Z_n\) and the limiting commutation probability \(3/10\); that information does **not** supply the exact \(P_n\), the nonzero-product sign classification, or the two explicit finite-size correction coefficients. These latter conclusions are the findings assessed here, not a restatement of the earlier limit.

The broader literature on centralizers of the full symmetric inverse semigroup includes Konieczny [3]. That paper was identifiable by abstract, but its complete proof was not accessible for comparison. The full semigroup permits arbitrary partial injective maps, whereas the present theorem concerns a proper inverse submonoid with consecutive translated intervals; an indirect implication from [3] cannot be excluded without further inspection.

## Limitations

The results concern ordered pairs in the specified integer interval-translation monoid only, not the full rook monoid, the full order-preserving partial-injection monoid, or the real-parameter extension. The formulas do not enumerate commuting tuples of length at least three or classify centralizers of individual elements. Exhaustive computational tests end at \(n=10\); the unrestricted conclusions follow from the provided proof. Published equivalence or indirect implication from a general centralizer result remains a publication-priority risk. No external independent mathematical audit has been carried out.

## References

[1] G. Fikioris and G. Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863 (first publicly posted 2 November 2021); *Semigroup Forum* 105 (2022), 191–216. https://arxiv.org/abs/2111.01863

[2] G. Fikioris and G. Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496 (first posted 19 February 2023); *Semigroup Forum* 107 (2023), 637–650. https://arxiv.org/abs/2302.09496 ; https://doi.org/10.1007/s00233-023-10393-8

[3] J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, *Communications in Algebra* 48 (2020), 5181–5194. https://doi.org/10.1080/00927872.2020.1782926
