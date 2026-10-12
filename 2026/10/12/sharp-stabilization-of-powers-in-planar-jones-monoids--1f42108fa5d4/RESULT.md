# Sharp stabilization of powers in planar Jones monoids

## Finding

Let \(J_n\) be the monoid of noncrossing perfect matchings between \(n\) numbered top sites and \(n\) numbered bottom sites, with vertical concatenation and all closed middle loops discarded (loop value one). For \(n\ge2\), put \(m=\lfloor n/2\rfloor\) and \(s(x)=\min\{k\ge1:x^{k+1}=x^k\}\). Then

\[
\max_{x\in J_n}s(x)=m,
\qquad x^{m+1}=x^m\ \text{for every }x\in J_n.
\]

For even \(n\ge4\), exactly two diagrams have \(s(x)=m\). For odd \(n\ge5\), exactly six diagrams have \(s(x)=m\). For \(n=2,3\), all diagrams already satisfy \(x^2=x\).

For each \(1\le i,j<n\), define \(c_{i,j}\) to have exactly the top cap joining \(i,i+1\), the bottom cup joining \(j,j+1\), and the other \(n-2\) propagating strands in increasing order. Its exact power profile is

\[
s(c_{i,j})=1+\left\lfloor\frac{|i-j|}{2}\right\rfloor=:K_{i,j},
\qquad
\operatorname{rank}(c_{i,j}^k)=n-2k\quad(1\le k\le K_{i,j}).
\]

In particular, the diagrams reaching the maximal cutoff are precisely those \(c_{i,j}\) with \(\lfloor |i-j|/2\rfloor=m-1\), provided \(m\ge2\).

## Assumptions and scope

The rank of a diagram is its number of propagating top-to-bottom strands. Planarity means that the matching admits a drawing in the rectangle with no crossings. Internal loops in a product are discarded without weights. The result concerns this finite diagram monoid itself, not the generic Temperley–Lieb algebra, the Kauffman monoid with a nontrivial loop generator, or a nonplanar Brauer monoid. Indices are one-based and the statements hold for all integers \(n\ge2\), without field or characteristic assumptions.

## Proof

**1. A rank plateau is equality.** Multiplication never increases rank. A top cap of the left factor remains a top cap of the product; a bottom cup of the right factor remains a bottom cup of the product. Thus, in the power sequence, the sets of top caps and bottom cups are nondecreasing under inclusion: compare \(x^k\) with \(x^kx\) for top caps and with \(xx^k\) for bottom cups. If \(\operatorname{rank}(x^{k+1})=\operatorname{rank}(x^k)\), their numbers of caps and cups are unchanged, so both cap and cup sets are equal. The remaining propagating strands must join the remaining sites in increasing order by planarity. Consequently \(x^{k+1}=x^k\).

**2. Uniform cutoff.** Every diagram other than the identity has at least one cap and one cup, so its initial rank is at most \(n-2\). Whenever powers differ, the preceding paragraph forces a strict rank loss, necessarily by at least two since ranks have the parity of \(n\). Starting from \(n-2\) and ending no lower than \(n-2m\in\{0,1\}\), there are at most \(m-1\) strict losses after the first power. Therefore \(x^{m+1}=x^m\). If the initial rank is at most \(n-4\), stabilization happens at or before exponent \(m-1\); an extremizer for \(m\ge2\) must therefore have rank exactly \(n-2\).

**3. Full powers of one-cap diagrams.** Suppose \(i\le j\) and write \(K=1+\lfloor(j-i)/2\rfloor\). Directly tracing the middle connections in the concatenation of planar matchings gives, for \(1\le k\le K\): the top caps of \(c_{i,j}^k\) join

\[
(i+2t,i+2t+1),\quad 0\le t<k,
\]

and the bottom cups join

\[
(j-2t,j-2t+1),\quad 0\le t<k.
\]

All remaining strands join the remaining top sites and bottom sites in increasing order. To verify the gluing step, draw the top cap and bottom cup of the additional \(c_{i,j}\), identify the corresponding middle sites, and follow each maximal path from a surviving outer endpoint. The existing top caps survive; while \(k<K\), the two next free top endpoints \(i+2k,i+2k+1\) become paired, and likewise the next free bottom endpoints \(j-2k,j-2k+1\); every other outer path joins the remaining endpoints in the unique increasing order. At \(k=K\), the two middle matching patterns interlock into internal loops or propagating paths without an additional outer cap or cup, giving \(c_{i,j}^{K+1}=c_{i,j}^K\). The case \(i>j\) follows by vertical reflection combined with reversing the site order (equivalently, the same tracing with top cap positions \(i-2t,i-2t+1\) and bottom cups \(j+2t,j+2t+1\)). The displayed explicit patterns give exactly \(k\) caps and \(k\) cups and hence rank \(n-2k\). Since that rank strictly falls until \(k=K\), this is its least stabilization exponent.

**4. Sharpness and exact extremizer count.** Every rank-\(n-2\) diagram has one adjacent top cap and one adjacent bottom cup, so is a unique \(c_{i,j}\) with \(1\le i,j<n\). The formula from Step 3 gives \(s(c_{i,j})=m\) exactly when \(|i-j|\) is \(2m-2\) or \(2m-1\). If \(n=2m\), the largest possible distance is \(2m-2\), realized by two ordered pairs. If \(n=2m+1\), the two distances are realized by four and two ordered pairs, respectively. Step 2 rules out extremizers of smaller rank. The boundary cases \(n=2,3\) have only rank \(n\) or \(n-2\), and the one-cap formula gives exponent one in all cases. This proves every assertion.

## Verification

The self-contained Python program `verify_jones.py` generates all planar noncrossing matchings on \(2n\) boundary points, calculates products by disjoint-set connectivity in a three-level gluing, compares every element with its powers, and independently checks the explicit one-cap power matchings for all \(1\le i,j<n\). Run `python verify_jones.py` with a standard Python 3 interpreter. It exhaustively checks all \(6916\) elements for \(2\le n\le9\), yielding full stabilization-count histograms. This is a finite check of examples; the argument above proves the unrestricted statement.

## Relationship to prior work

Kauffman's September 2026 paper studies idempotents in Temperley–Lieb and related diagram monoids through planar-curve and meander combinatorics. The present claim instead gives a sharp *uniform power-stabilization exponent*, the complete one-cap power profile, and the exact number of extremizers. Shahzamanian's 2021 classification of identities of \(J_5\) explicitly contains \(x^3=x^2\) and failure of \(x^2=x\) for that single size (Corollary 4.7); **the size-five specialization of the exponent claim is therefore not new**. The all-size sharp cutoff and extremizer counts require a separate argument and are not implied by a statement only about \(J_5\). Prior enumerations of idempotents concern elements already stable under squaring, not the least time at which arbitrary diagrams become idempotent.

## Limitations

The result does not enumerate stabilization indices of every arbitrary diagram below the maximal index. The 2026 Kauffman manuscript's later sections were not accessible in full during comparison, so a pre-existing equivalent all-size statement cannot be excluded solely from available excerpts. The same applies to potentially older synonymous semigroup-identity literature. No independent external audit has been performed.

## References

1. L. H. Kauffman, *Idempotents in the Temperley–Lieb Monoid and Other Categories*, arXiv:2609.34282v1 (submitted 2026-09-28), https://arxiv.org/abs/2609.34282.
2. M. H. Shahzamanian, *Identities of the Jones Monoid* \(\mathcal J_5\), arXiv:2111.05591v1 (2021), https://arxiv.org/html/2111.05591v1, especially Corollary 4.7.
3. J. East et al., *Enumeration of idempotents in planar diagram monoids*, arXiv:1507.04838 (2015), https://arxiv.org/abs/1507.04838.
