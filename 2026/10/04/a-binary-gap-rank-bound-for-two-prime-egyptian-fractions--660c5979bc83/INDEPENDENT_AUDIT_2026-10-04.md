# Independent mathematical audit

## correctness

PASS

Let \(r\) be the number of terms whose denominators are pure powers of \(2\), and let \(S\) be their sum. Because the complete representation uses the odd prime \(p\), one has \(S<1\). After clearing the largest dyadic denominator, the positive dyadic gap \(1-S\) is at least \(2^{-r}\): a sum of \(r\) dyadic unit fractions below one cannot approach one more closely than the reciprocal of the product of its distinct binary place scales, and the standard common-denominator/popcount argument gives this bound exactly. Every remaining term is at most \(1/p\), so \(2^{-r}\le (R-r)/p\) and hence \(R\ge r+\lceil p/2^r\rceil\). Writing \(k=\lfloor\log_2 p\rfloor\), the cases \(r\ge k+1\), \(r=k\), and \(r\le k-1\) all yield \(R\ge k+2\). If \(p=2^k+1\) is prime, the explicit identity \(\sum_{j=1}^{k}2^{-j}+p^{-1}+(2^kp)^{-1}=1\) has rank \(k+2\), so the bound is sharp for every Fermat prime.

## originality

PASS

The motivating primary paper explicitly asks whether one can prove a logarithmic lower bound for the minimum rank with support \(\{2,p\}\); the audited theorem proves the strictly stronger base-two bound \(\lfloor\log_2 p\rfloor+2\). Its finite tables and Fermat-prime constructions do not imply the universal lower bound. A Resultary search by the same support, rank, and binary-gap formulation returned the assigned record as the exact hit and no earlier covering theorem.

## value

PASS

The result resolves an explicit published lower-bound question with a stronger quantitative answer and identifies the sharp mechanism on every Fermat-prime support. Although the proof is short, it is a motivated all-parameter extremal statement rather than a routine small-case calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
