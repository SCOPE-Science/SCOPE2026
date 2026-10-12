# The eight-word high-window tail of quadratic Reed–Muller \(b\)-symbol weight spectra

## Finding

Let \(m\ge3\) be an integer, \(N=2^m\), \(Q=N/4\), and \(K=1+m+\binom{m}{2}\). For the lexicographically ordered binary Reed–Muller code \(C_m=\operatorname{RM}(2,m)\), define the complete cyclic \(b\)-symbol weight enumerator by
\[
W_{m,b}(z)=\sum_{c\in C_m}z^{w_b(c)}.
\]
For every integer \(b\) in the indicated intervals,
\[
\boxed{
W_{m,b}(z)=
\begin{cases}
1+8z^{b+Q-1}+(2^K-9)z^N,&5N/8<b\le3N/4,\\
1+(2^K-1)z^N,&3N/4<b\le N.
\end{cases}}
\]
Thus the nontrivial high-width interval always has exactly eight codewords with nonfull cyclic window weight, independent of the number of variables. These codewords are precisely the indicators of eight cyclic intervals of length \(Q\) whose starting positions are multiples of \(Q/2\). The strict lower endpoint is sharp.

## Assumptions and scope

Coordinates are indexed by \(0,1,\ldots,N-1\), each interpreted as its \(m\)-bit vector over \(\mathbb F_2\), with the most significant bit varying slowest. The code consists of evaluations of all Boolean polynomials of degree at most two in these bits. In particular, the evaluation order is **fixed**; an arbitrary coordinate permutation need not preserve the \(b\)-symbol spectrum.

For a binary word \(c\) of length \(N\), \(w_b(c)\) is the number of starting positions \(i\in\mathbb Z/N\mathbb Z\) for which the cyclic block \((c_i,c_{i+1},\ldots,c_{i+b-1})\) is not all zero. The variable \(z\) is formal, and \(b\) is an integer in the specified range. No code in an unmentioned coordinate order or with degree greater than two is covered.

## Proof

**1. Every sufficiently light nonzero quadratic word is a flat indicator.** Let \(f\) be a degree-at-most-two Boolean polynomial. The alternating polar form of the quadratic part has even rank \(2r\). After an invertible affine change of variables and shifts that remove linear terms in the paired variables, the polynomial has the form
\[
f(u,v,t)=\sum_{j=1}^{r}u_jv_j+\ell(t)+\varepsilon,
\]
where \(t\) contains \(m-2r\) radical coordinates, \(\ell\) is linear, and \(\varepsilon\in\mathbb F_2\). If \(\ell\ne0\), summing \((-1)^{f}\) over a radical variable gives zero. If \(\ell=0\), the sum has absolute value \(2^{m-r}\) because each paired quadratic term contributes magnitude two. Consequently, for \(r\ge1\), any nonbalanced word has Hamming weight
\[
N/2\pm N/2^{r+1}.
\]
For \(r\ge2\), every nonzero weight is at least \(3N/8\); for \(r=1\), the lower weight is \(N/4=Q\). If \(r=0\), the word is affine and its weight is \(0,N/2\), or \(N\). Thus every nonzero degree-at-most-two word of Hamming weight strictly below \(3N/8\) has weight \(Q\) and is the indicator of an affine codimension-two flat: indeed a rank-two quadratic is, after an affine substitution, \(uv\) or its translates, and its support is the intersection of two independent affine hyperplanes. Conversely every such flat indicator is the product of its two defining affine linear forms, so it is in \(C_m\).

**2. Exactly eight flats fit into a cyclic arc shorter than \(3Q/2\).** Partition the ordered coordinates into four successive quarter blocks \(B_0,B_1,B_2,B_3\), each of length \(Q\), corresponding to the two most significant Boolean bits. Let \(F\) be any affine codimension-two flat contained in some cyclic interval with fewer than \(3Q/2\) coordinates. The projection of \(F\) onto those two high bits is an affine subspace of \(\mathbb F_2^2\), hence has size \(1,2\), or \(4\). All occupied fibers have equal cardinality.

An interval of length less than \(3Q/2\) meets at most three quarter blocks, eliminating a four-point projection. If the projection has two points corresponding to opposite quarter blocks, both occupied fibers have \(Q/2\) points. Any subset \(H\) of \(\{0,1,\ldots,Q-1\}\) with \(Q/2\) points satisfies \(\min(H)\le Q/2\) and \(\max(H)\ge Q/2-1\). In either orientation around the circle, an arc containing both opposite fibers therefore has at least \(2Q+(Q/2-1)-(Q/2)+1=2Q\) positions. This excludes opposite blocks.

A one-point projection forces \(F\) to be the full occupied quarter block, giving four possibilities. A two-point projection onto neighboring quarter blocks gives two local affine hyperplanes \(H_0,H_1\subseteq\{0,1,\ldots,Q-1\}\) with the **same direction** (possibly different cosets). The shortest interval crossing their common boundary has length
\[
Q+\max(H_1)-\min(H_0)+1.
\]
If the defining linear functional of these hyperplanes involves any bit below the highest local bit, then each hyperplane has \(Q/4\) points in each local half. Therefore \(\min(H_0)\le Q/4\) and \(\max(H_1)\ge3Q/4-1\), giving interval length at least \(3Q/2\). This argument applies whenever lower local bits exist; when \(Q=2\), the only nonzero local functional is the highest local bit. For the remaining direction, each hyperplane equals the lower or upper local half. Of the four possibilities, only \(H_0=\) upper half and \(H_1=\) lower half has span strictly shorter than \(3Q/2\); its span is exactly \(Q\). There are four neighboring quarter boundaries, hence four such bridging flats. Together with the four aligned quarters these are exactly the eight asserted flats, all consecutive length-\(Q\) blocks starting at multiples of \(Q/2\).

**3. Translate short supports into cyclic window weights.** Fix \(b>5N/8\). Suppose \(w_b(c)<N\) for a nonzero word. Then at least one cyclic window of length \(b\) is zero, so the support of \(c\) is contained in the complementary interval of length \(N-b<3N/8=3Q/2\). By Steps 1–2, it is one of the eight flat indicators. Each has a unique cyclic zero gap of length \(3Q\), so its number of zero windows of length \(b\) is
\[
\max\{3Q-b+1,0\}.
\]
Its \(b\)-symbol weight is therefore \(b+Q-1\) if \(b\le3Q\), and \(N\) otherwise. Every other nonzero codeword has weight \(N\). The monomials of degree at most two are linearly independent Boolean functions, giving dimension \(K\) and \(2^K\) words. The zero word contributes the leading constant one. This proves the two formulas.

**4. Strictness of the lower endpoint.** At \(b=5N/8\), the complement has length \(3Q/2\). The set formed by the lower half of \(B_0\) and the lower half of \(B_1\) is an affine codimension-two flat of cardinality \(Q\), spanning precisely \(3Q/2\) successive coordinates. It is not among the eight length-\(Q\) supports and still leaves a length-\(b\) zero window. Therefore the eight-word count fails at the excluded endpoint for every \(m\ge3\).

## Verification

Run `python3 verify_quadratic_tail.py` from the directory containing the accompanying code. The program enumerates all degree-at-most-two Boolean evaluation words for \(3\le m\le5\), computes every cyclic \(b\)-window independently, and compares complete coefficient dictionaries for every integral width satisfying \(5N/8<b\le N\). It also enumerates all affine codimension-two flat cosets and their shortest circular spans for \(3\le m\le8\). The exact concluding marker is `VERIFY_OK quadratic_tail_m3_to_m5 affine_flats_m3_to_m8`. These finite checks are reproducibility tests of the general argument, not a substitute for it.

## Relationship to prior work

Pan, Ling and Liu, *New bounds for \(b\)-Symbol Distances of Matrix Product Codes* (arXiv:2309.08920, first public 16 September 2023), Theorem 4.6, proved the minimum \(b\)-symbol distance of every generalized Reed–Muller code. In the binary quadratic case their minimum is \(\min\{N/4+b-1,N\}\), in agreement with the smallest nonzero exponent here. Their theorem does not specify the complete distribution or multiplicities, which are the new subject of this result.

Zhu, Li, Shi, Xia and Solé, *Some bounds on the cardinality of the \(b\)-symbol weight spectrum of codes* (arXiv:2404.02471, first public 3 April 2024), establishes general bounds on the **number of distinct weights** and discusses cyclic codes; it does not determine this coordinate-ordered quadratic code's full enumerator. Vega, *The \(b\)-symbol weight distributions of all semiprimitive irreducible cyclic codes* (2023), obtains exact enumerators for a different, cyclic-code family. The first-order Reed–Muller case is distinct from the quadratic family treated here.

## Limitations

The theorem is confined to fixed binary-integer coordinate order, quadratic degree, and the stated large-window range. It does not evaluate the full \(b\)-spectrum at smaller window widths. Published distance formulas alone do not supply an independent priority certificate for the complete enumerator; undiscovered equivalent prior work remains possible. The computational checks cover finite dimensions and widths only; the proof handles all listed integers.

## References

1. X. Pan, S. Ling and H. Liu, *New bounds for \(b\)-Symbol Distances of Matrix Product Codes*, arXiv:2309.08920, first public 2023-09-16. https://arxiv.org/abs/2309.08920
2. H. Zhu, S. Li, M. Shi, S.-T. Xia and P. Solé, *Some bounds on the cardinality of the \(b\)-symbol weight spectrum of codes*, arXiv:2404.02471, first public 2024-04-03. https://arxiv.org/abs/2404.02471
3. G. Vega, *The \(b\)-symbol weight distributions of all semiprimitive irreducible cyclic codes*, Designs, Codes and Cryptography 91 (2023), 2213–2221, DOI:10.1007/s10623-023-01193-w. https://doi.org/10.1007/s10623-023-01193-w
