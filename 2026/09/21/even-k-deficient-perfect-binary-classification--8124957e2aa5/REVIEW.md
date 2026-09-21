# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was rederived from the definition. For \(n=2^ap^b\), with \(M=2^{a+1}-1\) and \(t=p-M\), the deficiency is
\[
\Delta=2n-\sigma(n)=t+(t-1)(p+\cdots+p^{b-1}).
\]
Exact deficient-perfectness requires \(\Delta>0\), which forces \(p>M\), while \(\Delta<p^b\) prevents any chosen deficient divisor from containing \(p^b\). Grouping chosen divisors by their \(p\)-adic exponent gives coefficients \(A_j\in[0,M]\). Since \(M<p\), the resulting expression for \(\Delta\) is a genuine base-\(p\) expansion. Base-\(p\) uniqueness then forces \(A_0=t\) and \(A_j=t-1\) for \(j\ge1\), yielding \(t\le M\) and hence \(M<p<2M\). Conversely, this interval makes both digits representable by unique subsets of \(1,2,\ldots,2^a\), proving existence and uniqueness of the deficient-divisor set.

Boundary cases were checked explicitly. When \(b=1\), the second block is empty and the argument reduces to \(\Delta=t\). The parity of \(p\) and \(M\) makes \(t\) positive even, so the binary-weight bounds \(1\le s_2(t),s_2(t-1)\le a\) are valid. The \(k=1\) specialization recovers the published Tang--Ren--Li two-prime family, providing a strong consistency check.

The standalone exact verification enumerates all relevant proper-divisor subsets through dynamic programming for 672 parameter triples with \(1\le a\le6\), \(1\le b\le4\), \(p<200\), and \(2^ap^b\le2{,}000{,}000\). It found 92 qualifying triples, exactly one representation for every qualifying triple, and zero mismatches with the theorem.

## Originality

PASS, qualified as to the best of our knowledge.

The closest primary sources were inspected at theorem level. Tang--Ren--Li (2013) determine all deficient-perfect numbers with at most two distinct prime factors, i.e. the one-deficient-divisor case. Chen (2019) studies exactly \(k\)-deficient-perfect numbers but its main classification is the odd exactly-2 case with two distinct prime divisors. Aursukaree--Pongsriiam (2021) classify the odd exactly-3 case with at most two distinct prime factors.

OEIS A331627, A331628, and A331629 were checked as current sequence/database summaries. Targeted searches covered “even exactly k-deficient-perfect”, “two distinct prime factors/divisors”, the form \(2^ap^b\), and synonymous deficient-divisor subset-sum formulations. No arbitrary-\(k\) theorem for the even two-prime slice, no equivalent base-\(p\) digit criterion, and no uniqueness statement for the deficient-divisor set was located. The current SCOPE archive was searched by object and terminology immediately before publication and no semantic overlap was found.

Residual risk remains from poorly indexed divisor-partition literature or later papers using different terminology. This is an elementary structural theorem, so hidden prior art is plausible in principle; no concrete evidence of prior coverage was found.

## Value

PASS.

The result closes an entire natural two-prime-support slice for all \(k\), rather than adding a finite example or a single small-\(k\) case. It explains the structure through a canonical base-\(p\) expansion followed by binary expansion, proves uniqueness of the deficient-divisor set, recovers the known classical \(k=1\) family, gives immediate complete \(k=2\) and \(k=3\) even classifications, and yields a nonempty family for every exponent pair \((a,b)\) via Bertrand's postulate. These are structural consequences with direct connections to the existing literature.
