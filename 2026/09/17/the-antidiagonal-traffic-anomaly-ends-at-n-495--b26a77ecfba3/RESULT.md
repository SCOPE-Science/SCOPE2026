# The antidiagonal traffic anomaly ends at n=495

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review. This is not independent verification. Originality is claimed only to the best of our knowledge.

## Claim

The source report proposes a proof of Conjecture 7.4 of Gil--Liang--Odetola--Weiner, arXiv:2609.01562v1:

`rho(n) < 1` for every integer `n >= 496`.

Consequently, for every obstruction `B` on the antidiagonal `x+y=n`, the maximum number of `B`-avoiding monotone paths is attained at `(1,1)` and `(n-1,n-1)`.

The threshold is reported as sharp:

`rho(495)>1`.

## Reparameterization and unimodality

Put `k=n-2a`. From the paper's explicit ratio the source report obtains

`R_n(k)=((k+1)(n-k)(2n-1))/(n(n-1)) * C(n,(n-k)/2)^2/C(2n,n)`,

and

`R_n(k+2)/R_n(k)=((n-k)(n-k-2)(k+3))/((n+k+2)^2(k+1))`.

The numerator minus denominator factors as

`-2(2k^2 n + 7kn + k - n^2 + 5n + 2)`.

Define

`P_n(k)=n^2-5n-2-n(2k^2+7k)-k`.

Then `R_n(k+2)>R_n(k)` exactly when `P_n(k)>0`. Since `P_n(k)` strictly decreases in `k`, the admissible sequence is unimodal. For each `n`, only the first parity-compatible positive `k` at which `P_n(k)<=0` can maximize the sequence.

## Exact finite bridge

The source verifier performs exact integer comparisons for every

`496 <= n <= 2999`.

It reports zero failures. The closest case is

`R_497(15)=0.999955284137033... < 1`,

while the sharpness witness is

`R_495(15)=1.000024070891585... > 1`.

## Analytic tail

For `n>=3000`, the source report combines Robbins factorial bounds

`C(n,floor(n/2)) < 2^n sqrt(2/(pi n))`

and

`C(2n,n) > 4^n/sqrt(pi(n+1/2))`

with an off-centre product estimate

`C(n,(n-k)/2)/C(n,floor(n/2)) <= exp(-(k^2-delta_n)/(2(n+1)))`,

where `delta_n=0` for even `n` and `1` for odd `n`.

This yields an explicit decreasing envelope

`R_n(k)<E(n)`

with

`E(3000)<0.995<1`.

Together with the finite exact certificate, the source report concludes the all-`n>=496` statement.

It additionally reports

`limsup rho(n) <= sqrt(8/(pi e)) < 1`

as an asymptotic explanation for why the anomaly cannot recur.

## Reproducibility

The archival package includes the source proof note and exact-arithmetic verifier as compact artifacts:

- `artifacts/research_note.md`
- `artifacts/verify.py`

The computation supports the finite bridge; it does not replace the analytic tail proof.

## Closest prior work

Gil, Liang, Odetola and Weiner, arXiv:2609.01562v1, state Conjecture 7.4 and report exact computation only through `n=2000`. The source report searched the exact conjecture number, the `496` threshold, `rho(n)`, the paper title and arXiv identifier, and found no subsequent proof.

The main originality threats identified are an unindexed or not-yet-public author revision, a simultaneous independent preprint, or an older sharp binomial/hypergeometric inequality that reduces novelty of the analytic method.

## Limitations

The analytic tail has not been independently proof-checked or formally verified. Search coverage cannot certify absolute novelty.
