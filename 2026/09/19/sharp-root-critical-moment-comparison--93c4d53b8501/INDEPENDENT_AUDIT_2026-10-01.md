# Independent scientific audit — SCOPE-20260919-93c4d53b8501

Audited at: 2026-10-01T17:15:19.026518Z

Disposition: **passed**

## Correctness — PASS

After translation and dilation, let \(D=\operatorname{diag}(\lambda_i)\), \(Q=uu^*\), \(P=I-Q\), and \(A=PDP\). The Komarova-Rivin differentiator gives spectrum \(\{0,\xi_1,\ldots,\xi_{n-1}\}\) for \(A\). Splitting \(D-A=QD+PDQ\) inside the telescoping trace formula, \(AQ=QA=0\) kills the endpoint and all but \(m-1\) rank-one trace terms; each surviving term has modulus at most one. The normalization identity then yields \((m-1)/(n-1)\). For \(f(z)=((z-c)^m-R^m)^{n/m}\), direct differentiation gives equality whenever \(m\mid n\), proving sharpness for each fixed \(m\).

### Correctness sources

- assigned RESULT.md
- Zhang arXiv:2609.20256 full text, Lemma 2.5
- Komarova-Rivin differentiator representation

### Correctness risks

- The equality construction establishes the sharp universal coefficient for each fixed \(m\) along infinitely many degrees, not a classification of extremizers for every pair \((n,m)\).

## Originality — PASS

Zhang's primary Lemma 2.5 proves only \(|E\lambda^m-E\xi^m|\le5m/n\), using a rank-two perturbation estimate; the fresh full-text inspection confirms that statement and proof. Schmeisser's classical theorem weakly majorizes the moduli of zeros and critical points and therefore does not imply a centered complex power-sum discrepancy. Searches over critical-point moments, differentiator compressions, power sums, and empirical measures did not locate the sharp normalized coefficient \((m-1)/(n-1)\).

### Equivalent formulations

No equivalent normalized complex-moment inequality with the sharp coefficient was found.

### Broader coverage

Neither theorem implies the signed/complex centered power-moment discrepancy at the audited sharp constant.

### Exact database or table

The quantity is an analytic inequality rather than a tabulated invariant; this supports but does not alone prove novelty.

### Claim versus prior implication

The prior proof does not mechanically yield the \(m-1\) surviving-term count or the equality family.

### Sources inspected

- Sendov's conjecture holds for every degree n >= 10^200000 — https://arxiv.org/abs/2609.20256. NOT_COVERING: Lemma 2.5 gives \(5m/n\) by a rank-two norm/rank estimate; it does not give the audited sharp coefficient.
- Majorization of the Critical Points of a Polynomial by Its Zeros — https://doi.org/10.1007/BF03321027. NOT_COVERING: Radial weak majorization does not control complex centered power-sum differences with cancellations.

### Checked sources

- https://arxiv.org/abs/2609.20256
- https://doi.org/10.1007/BF03321027
- Resultary semantic search

### Residual risks

- An equivalent trace inequality may exist in older matrix or coefficient-theory literature under different terminology.

## Value — PASS

The result replaces a coarse \(O(m/n)\) estimate used in an active polynomial-critical-point argument by a sharp coefficient with explicit equality families. The rank-one cancellation is structural and the analytic-test consequence gives a natural deterministic \(O(1/n)\) comparison.

### Value sources

- https://arxiv.org/abs/2609.20256
- assigned RESULT.md

### Value risks

- The analytic-test corollary is not claimed optimal for every prescribed function class.

## Limitations

- The sharp coefficient is universal, but equality is exhibited only on the stated divisible-degree family.
- No exact extremizer classification for every \((n,m)\) is claimed.
- Originality remains subject to older trace-inequality literature under alternate terminology.
