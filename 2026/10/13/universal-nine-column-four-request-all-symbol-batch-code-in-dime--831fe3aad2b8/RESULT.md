# Universal nine-column four-request all-symbol batch code in dimension four

## Finding

For every prime power \(q\), the minimum lengths of four-request all-symbol private-information-retrieval (PIR) and all-symbol batch codes of dimension four over \(\mathbb F_q\) are equal:

\[
\operatorname{ASP}(4,4,q)=\operatorname{ASB}(4,4,q)=9.
\]

The new content is the upper bound of nine in **every odd characteristic**. The characteristic-two case and the universal lower bound were previously established; see the references.

In the following displayed generator matrix, the first four columns form an identity matrix. The columns are numbered from left to right:

\[
G=\begin{pmatrix}
1&0&0&0&1&1&0&0&1\\
0&1&0&0&1&0&1&0&1\\
0&0&1&0&0&1&0&1&1\\
0&0&0&1&0&0&1&1&1
\end{pmatrix}.
\]

In fact, this one integer matrix is a four-request all-symbol batch code over **every** field, not merely the finite fields. Its four nontrivial intermediate columns encode the edges of a four-cycle. Up to invertible row and nonzero column scalings, this is the four-dimensional instance of the single-parity construction in Boruchovsky–Gruica–Niemann–Yaakobi. The previously unestablished property is its full four-request batch recovery in odd characteristic.

## Assumptions and scope

A generator matrix \(G\in\mathbb F_q^{k\times n}\) defines an all-symbol batch code for \(t\) requests when, for every multiset of \(t\) indices among its \(n\) columns, one can choose \(t\) pairwise disjoint, nonempty subsets of column indices, each spanning the respective requested column. This permits each stored symbol to be reconstructed from a separate subset of storage nodes. An all-symbol PIR code requires only the subcase of \(t\) identical requests. The symbols requested here are exactly the stored columns, not arbitrary linear combinations of the information symbols.

The functions \(\operatorname{ASB}(k,t,q)\) and \(\operatorname{ASP}(k,t,q)\) minimize the column count among rank-\(k\) generator matrices satisfying the indicated property. The claim concerns \(k=t=4\), all prime powers \(q\), and the displayed nine-column construction. No claim about all-dimensional or functional batch parameters is made.

## Proof

**Lower bound.** Proposition 18 of Boruchovsky et al. proves \(\operatorname{ASP}(k,3,q)=k+r\), where \(r\) is the least positive integer with \(\binom r2\ge k\). For \(k=4\), one has \(r=4\), so the three-request optimum is eight. Their Proposition 10(iii) proves strict monotonicity of the optimum in the number of requests. Therefore

\[
9=\operatorname{ASP}(4,3,q)+1\leq\operatorname{ASP}(4,4,q)\leq\operatorname{ASB}(4,4,q).
\]

**Upper bound: finite certificate.** Write \(g_1,\ldots,g_9\in\mathbb Z^4\) for the displayed integer columns. The accompanying `certificates.json` contains two complete families of disjoint signed recovery identities, using only coefficients \(-1\) and \(+1\):

1. For every index \(i\in\{1,\ldots,9\}\), four pairwise disjoint identities \(g_i=\sum_{j\in R_{i,s}}\varepsilon_{i,s,j}g_j\), one for each \(s\in\{1,2,3,4\}\).
2. For every unordered pair \(i<j\), four pairwise disjoint identities recovering the ordered targets \((g_i,g_i,g_j,g_j)\).

For illustration, the four disjoint recoveries of the first column are

\[
\begin{split}
g_1&=g_1,\\
g_1&=-g_2+g_5,\\
g_1&=-g_3+g_6,\\
g_1&=g_4-g_7-g_8+g_9.
\end{split}
\]

These are identities in the free abelian group \(\mathbb Z^4\), not merely identities checked in a sample of finite fields. The accompanying `verify.py` checks every coefficient, target, and disjointness condition in the entire \(9+\binom92=45\)-case certificate using exact integer arithmetic. Consequently every identity remains true after reduction to any field.

**Reduction to all request multisets.** An arbitrary multiset of four column requests has one of the multiplicity partitions \(4\), \(3+1\), \(2+2\), \(2+1+1\), or \(1+1+1+1\). The all-equal and two-pair certificates immediately settle the first and third partitions. With one target occurring three times, at most one of its four disjoint recovery sets contains the distinct singly requested column, so at least three recovery sets avoid that singleton. With one target occurring twice and two other singly requested columns, at most two of its four disjoint recovery sets contain either singleton, leaving at least two. In either case the distinct requested columns are served by their singleton indices. All-distinct requests use four singleton indices. Thus the 45 certified cases imply the all-symbol batch property for every four-request multiset.

The initial identity block ensures \(\operatorname{rank}_{\mathbb F_q}(G)=4\) for every \(q\), and there are nine columns. Hence \(\operatorname{ASB}(4,4,q)\le9\). Together with the preceding lower bound this proves the claim.

## Verification

The package contains self-contained `certificates.json` and a Python 3 standard-library verifier `verify.py`; run `python3 verify.py` in the directory containing both files. The verifier checks all 45 primitive certificate bundles, then constructs and validates recovery sets for all \(\binom{12}{4}=495\) possible four-request multisets. It checks exact identities over the integers and disjointness of supports. Its observed output is:

`VERIFY_OK: 9 column targets, 36 two-pair targets, all 495 request multisets, exact integer identities`

The lower bound is deduced from two precise published propositions cited below; the verifier independently establishes the field-independent upper bound. No floating-point arithmetic, solver status, or extrapolation from a finite sample of characteristics is needed.

## Relationship to prior work

Boruchovsky, Gruica, Niemann and Yaakobi, in arXiv:2601.04041v2, Proposition 18 and Proposition 10, already give the lower bound nine for every field. Their Theorem 23 gives only \(9\le\operatorname{ASP}(4,4,q)\le\operatorname{ASB}(4,4,q)\le10\) for odd \(q\), while Proposition 24 establishes nine in characteristic two. Their dimension-five example proves a different characteristic-three parameter and does not assert the dimension-four all-odd-field result. The present certificate supplies the missing odd-characteristic upper bound for the four-dimensional single-parity construction, and thus makes the optimal length uniform across characteristics.

A separate prior finite classification concerns dimension three, not dimension four; it does not imply the new identity. Matrices related by invertible row changes and nonzero column scalings are considered equivalent for recovery purposes. The novelty claimed here is not an unrelated new construction but the universal-field recovery proof and the sharp odd-characteristic parameter value.

## Limitations

The result is restricted to four requests and dimension four, with requests drawn from stored column symbols. It does not determine optimal lengths in other dimensions, prove uniqueness of optimal matrices, or imply functional batch recoverability for arbitrary target vectors. A previous unindexed note or finite-field computation of the same characteristic-independent conclusion cannot be entirely excluded by the consulted sources. The correctness certificate proves only the specified finite family of integer identities; the general-field consequence follows algebraically.

## References

1. Avital Boruchovsky, Anina Gruica, Jonathan Niemann and Eitan Yaakobi, *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041, submitted 7 January 2026, revised 22 April 2026; especially Propositions 10, 18 and 24, Theorem 23, Remark 25 and Example 27. https://arxiv.org/html/2601.04041v2
2. *Exact dimension-three four-request all-symbol code lengths*, published mathematical research record dated 17 September 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-dimension-three-four-request-all-symbol-lengths--a938eedf9b5f (abstract metadata inspected; full text not available during comparison).
