# Zero-density regions for integers supporting conjugate power-base partitions

## Finding

For integers \(m,q\ge2\), let \(A_{m,q}(X)\) count positive integers \(n\le X\) that admit a partition into powers of \(m\) whose conjugate has parts that are powers of \(q\). Write \(a=1/\log m\), \(b=1/\log q\) and
\[\alpha(m,q)=(a+b)\log(a+b)-a\log a-b\log b.\]
For real \(X\ge1\), put \(K=\lfloor\log_m X\rfloor\), \(T=\lfloor\log_q X\rfloor\). Then the following bound is exact as a count of all admissible operator words:
\[A_{m,q}(X)\le\binom{K+T+2}{K+1}-1.\]
Consequently, as \(X\to\infty\),
\[A_{m,q}(X)=O_{m,q}\!\left(\frac{X^{\alpha(m,q)}}{\sqrt{\log X}}\right).\]
In particular, if \(\alpha(m,q)\le1\) the represented integers have natural density zero. This includes the critical case \((m,q)=(4,4)\), where \(\alpha=1\), and every coordinatewise enlargement of \((2,11)\), \((3,6)\), or \((4,4)\). The criterion applies to the same set after swapping \(m,q\), by conjugation. The exponent bound is an upper bound, not an assertion of its optimality.

## Assumptions and scope

All bases \(m,q\) are integers at least two; partitions are finite partitions of positive integers with unrestricted multiplicities. The conjugate is the Ferrers-diagram transpose. \(\log\) is the natural logarithm. The counting function counts distinct integers, not partitions. For \(X=1\), both sides equal one. The asymptotic estimate is for fixed bases.

## Proof

Dietz, Flowers and Lockard (2026), Theorem II.10 and Corollary II.13, establish that every such partition has a unique word in the operators \(R\) (raise) and \(M\) (migrate), starting at the one-cell partition. If the word has \(t\) symbols \(R\) and \(k\) symbols \(M\), the resulting partition has exactly \(q^t\) parts and greatest part exactly \(m^k\). These also follow directly from the operators: \(R\) multiplies the number of parts by \(q\), whereas \(M\) replaces a single largest part of size \(m^j\) with one of size \(m^{j+1}\), preserving part count.

If the partition has area \(n\le X\), its number of parts and its greatest part cannot exceed \(n\); therefore \(q^t\le X\) and \(m^k\le X\). Hence \(0\le t\le T\) and \(0\le k\le K\). For each ordered pair \((k,t)\), there are exactly \(\binom{k+t}{k}\) words with these letter counts. Thus the number of partitions of area at most \(X\), and a fortiori the number of distinct integers represented, is at most
\[\sum_{k=0}^{K}\sum_{t=0}^{T}\binom{k+t}{k}=\binom{K+T+2}{K+1}-1.\]
The identity follows by applying the hockey-stick binomial identity twice. Notice that all of these words are counted even when their area exceeds \(X\), so the estimate is an upper bound rather than an equality for partitions.

Set \(L=\log X\), so \(K=aL+O_m(1)\) and \(T=bL+O_q(1)\). Stirling's formula for \(\binom{K+T+2}{K+1}\), with both binomial arguments proportional to \(L\), gives
\[\log\binom{K+T+2}{K+1}=\alpha(m,q)L-\tfrac12\log L+O_{m,q}(1).\]
Exponentiation proves the claimed estimate. If \(\alpha<1\), division by \(X\) tends to zero by a power. If \(\alpha=1\), it still tends to zero by the square-root logarithmic factor. For \(m=q=4\), the two parameters are \(a=b=1/\log4\), so \(\alpha=2\log2/\log4=1\). The strict inequalities \(\alpha(2,11)<1\), \(\alpha(3,6)<1\) follow from ordinary numerical bounds on natural logarithms; \(\alpha\) decreases as either base increases because its partial derivative with respect to \(a\) is \(\log((a+b)/a)>0\) and \(a=1/\log m\) decreases with \(m\). Hence the indicated coordinatewise ranges are covered.

## Verification

The accompanying Python 3 script independently generates partitions by their nested powers-of-\(q\) tail multiplicities and separately generates all finite \(R,M\) words up to a given area. The two enumeration methods agree for the tested pairs \((2,3)\), \((3,2)\), \((4,4)\), \((3,6)\), \((2,11)\), and \((5,5)\). For every test it checks the exact operator-word binomial envelope. Run `python3 density_verify.py`. This finite verification does not substitute for the all-base combinatorial argument and Stirling estimate.

## Relationship to prior work

The operator-word uniqueness and operator-count identities are previously proved in Dietz, Flowers and Lockard (2026, Theorem II.10 and Corollary II.13). The same paper explicitly asks in Question IV.15 for densities of integers supporting conjugate \((m,q)\)-ary partitions; it does not state the polynomial counting bound or the resulting zero-density region. The present claim is an asymptotic consequence obtained by restricting the two word counts by the area and applying binomial asymptotics. The 2021 paper of Flowers and Lockard treats equal bases and provides structural conditions rather than this base-pair density region. A short or unindexed prior counting argument may exist; source priority has not been independently established.

## Limitations

No conclusion is asserted for base pairs with \(\alpha>1\), including \((2,2)\) and \((4,3)\). The estimate may not be sharp for any fixed pair. Uniqueness and symbol-count facts are imported from the cited 2026 theorem, which is publicly available; the proof of the new bound is otherwise elementary. The asymptotic result supplies a partial answer to Question IV.15, not a complete density classification for all bases.

## References

1. G. D. Dietz, T. B. Flowers and S. R. Lockard, *A study of \(m\)-ary partitions whose conjugates are \(q\)-ary*, J. Algebra Comb. Discrete Appl. 13 (2026), 385–407, DOI: 10.13069/jacodesmath.v13i3.393; arXiv:2609.08799, first publicly available 2026-09-06.
2. T. B. Flowers and S. R. Lockard, *Conjugate \(m\)-ary partitions*, Australasian Journal of Combinatorics 81 (2021), 458–473.
