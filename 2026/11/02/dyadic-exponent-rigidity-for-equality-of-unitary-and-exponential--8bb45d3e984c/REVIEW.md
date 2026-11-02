# Scientific review: dyadic-exponent equality theorem

## Correctness — PASS
The equality of the two divisor sums is exactly the integer divisibility condition \(D_t(p)\mid p^{2^t}+1\), since the prime appearing to exponent one contributes \(q+1\) on the unitary side and \(q\) on the exponential side. The \(t=1\) quotient is integer only for bases \(2,3\). For \(t=2\), the explicit reduced representative \((p-1)^2+1\) lies strictly between \(0\) and the positive denominator. For \(t\ge3\), the auxiliary upper bound \(3u\le y\) is proved inductively; the representative \((y+u)^2+1\) lies strictly between \(D\) and \(2D\), excluding divisibility. These computations fully cover all integer bases and unbounded exponents. Finite arithmetic checks corroborate but are not used to infer the theorem.

## Originality — PASS, with risk
Trudgian's section 4 raises the general equality problem and gives examples but no dyadic-exponent theorem. The particularly close published finite classification covers **all** exponents \(2\le a\le49\), including dyadic \(2,4,8,16,32\); these small cases are explicitly **not new**. Its theorem cannot imply exclusion of dyadic exponents \(64,128,256,\ldots\), whereas the presented argument proves the entire unbounded family. OEIS A236474 supplies examples, not an infinite-range classification. Equivalent unlocated specialist results remain possible.

## Mathematical value — PASS
The equality question is motivated by an explicitly posed problem about two classical multiplicative divisor sums. The new result rules out an infinite, structurally natural exponent family in the two-prime support and sharpens the previously bounded \(a\le49\) classification to every power-of-two exponent, with a uniform arithmetic mechanism rather than a moving finite cutoff. It neither addresses unrelated exponent patterns nor claims a global theorem.

## Limits
Only distinct two-prime numbers with singleton cofactor and dyadic exponent are classified; the general global infinitude problem remains open in this proof. Full-prior-literature equivalence cannot be ruled out solely by searches.

Self-review: passed. Independent audit: not yet performed.
