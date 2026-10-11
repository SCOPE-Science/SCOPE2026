# Independent mathematical audit

## correctness

PASS

The normalization gives \(\operatorname{tr}S=n\), and rank-one expansion gives \(\operatorname{tr}(S^2)=n+\sum_{j\ne k}a_{jk}a_{kj}\). For nonnegative eigenvalues, Cauchy gives \(n^2/d\le\operatorname{tr}(S^2)\). The triangle inequality and definition of \(M\) give \(n^2/d-n\le\sum_{j\ne k}|a_{jk}a_{kj}|\le n(n-1)M^2\). At the Welch value the endpoints coincide, so equality holds throughout. Equal eigenvalues plus diagonalizability gives \(S=(n/d)I\). Every one of the \(n(n-1)\) nonnegative summands must equal \(M^2\), and since each factor has modulus at most \(M\), both factors equal \(M\); the \(n=d\) case has \(M=0\). A fresh symbolic check verified the endpoint identity \(n(n-1)\gamma^2=n^2/d-n\).

## originality

PASS

The motivating primary paper explicitly poses as Question 3.12(i) whether equality in its first-order maximum-correlation Welch bound forces equiangularity. The audited trace-equality argument answers that question affirmatively under exactly the paper's spectral/normalization hypotheses and additionally forces tightness. The classical Hilbert-space equality theorem does not imply the dual-pair Banach statement. Resultary found no earlier answer under equivalent terminology.

## value

PASS

The theorem answers an explicit published equality-case question and strengthens the requested equiangularity conclusion by forcing tightness. Equality rigidity is central to Welch-bound geometry, and extending it from Hilbert vectors to normalized Banach dual pairs under the source's hypotheses is substantively motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
