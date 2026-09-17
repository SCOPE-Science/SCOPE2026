# SCOPE-20260917-002 — Proof note

## Proposed theorem: the antidiagonal traffic anomaly ends at 495

Reference: Juan Gil, Zhenni Liang, Ayodeji Odetola, Michael Weiner, *Points of maximal traffic on a grid with obstruction*, arXiv:2609.01562v1 (2026), especially Proposition 7.2, Lemma 7.3, and Conjecture 7.4.

### Theorem
For every integer `n >= 496` and every obstruction `B=(a,n-a)` on the antidiagonal of the `n x n` grid, the maximum number of monotone `(0,0)`-to-`(n,n)` paths avoiding `B` and passing through a non-endpoint lattice point is attained at `(1,1)` and `(n-1,n-1)`.

Equivalently, in the notation of Gil--Liang--Odetola--Weiner, `rho(n)<1` for every `n>=496`.

The threshold is sharp: their computation shows an anomaly at `n=495`, and the exact certificate below gives a witness with ratio greater than one.

---

## 1. Exact one-dimensional reformulation

The paper proves that for `B=(a,n-a)` with `2a<n`, the relevant comparison is controlled by

`R_n(a)=G(n,a)/D(n)`, where

`D(n) = (1/n) * C(2n-2,n-1)`

and

`G(n,a) = ((n-2a+1)/(n-a)) * C(n,a) * C(n-2,a-1)`.

Put

`k = n-2a > 0`.

Then `k` has the same parity as `n`, and elementary binomial simplification gives

`R_n(k) = ((k+1)(n-k)(2n-1))/(n(n-1)) * C(n,(n-k)/2)^2 / C(2n,n).`  (1)

Indeed,

`C(n-2,a-1) = a(n-a)/(n(n-1)) * C(n,a)`

and

`C(2n-2,n-1) = n/(2(2n-1)) * C(2n,n)`.

The central even case `k=0` is not part of the paper's `rho(n)` because symmetry reduces the anomaly test to `2a<n`; it will be harmless under the same binomial bounds below.

---

## 2. Exact location of the discrete maximum

Translating Lemma 7.3 from `a` to `k` gives

`R_n(k+2)/R_n(k) = ((n-k)(n-k-2)(k+3))/((n+k+2)^2(k+1)).`  (2)

Subtracting denominator from numerator factors as

`(n-k)(n-k-2)(k+3) - (n+k+2)^2(k+1)`

`= -2(2k^2 n + 7kn + k - n^2 + 5n + 2).`

Define

`P_n(k) = n^2 - 5n - 2 - n(2k^2+7k) - k.`

Then

`R_n(k+2) > R_n(k)` iff `P_n(k)>0`.

For fixed `n`, `P_n(k)` is strictly decreasing in `k>=0`. Hence the admissible sequence of `R_n(k)` is unimodal. Its global maximum over positive admissible `k` occurs at the first positive `k` of the same parity as `n` satisfying

`P_n(k) <= 0`.  (3)

This reduces each finite `n` to one exact integer comparison.

---

## 3. Exact finite certificate, 496 <= n <= 2999

The accompanying script `scope_antidiagonal_threshold_verify.py` implements (3), then evaluates (1) using Python arbitrary-precision integers. It checks

`numerator(R_n(k)) < denominator(R_n(k))`

without floating point for every `496 <= n <= 2999`.

Result: no failures.

The closest finite case is

`n=497, k=15`, with

`R_497(15) = 0.999955284137033... < 1`.

Sharpness is visible immediately before the proposed threshold:

`n=495, k=15`, with

`R_495(15) = 1.000024070891585... > 1`.

For even `n`, the script also checks the central case `k=0` exactly. Its largest value in this finite window occurs at `n=496` and is about `0.10136`, far below one.

---

## 4. A uniform analytic tail bound

We now prove `R_n(k)<1` for every `n>=3000`, uniformly in admissible `k`.

### 4.1 Central binomial estimates

Use Robbins' classical factorial bounds

`sqrt(2*pi) m^(m+1/2) e^(-m+1/(12m+1)) < m! < sqrt(2*pi) m^(m+1/2) e^(-m+1/(12m))`.

They imply, for every `n>=1`,

`C(n,floor(n/2)) < 2^n sqrt(2/(pi n))`.  (4)

For even `n=2m`, this follows from

`C(2m,m) < 4^m/sqrt(pi m) * exp(1/(24m)-2/(12m+1)) < 4^m/sqrt(pi m)`.

For odd `n=2m+1`, use

`C(2m+1,m) = (1/2) C(2m+2,m+1)`

and the even bound.

The same Robbins inequalities give

`C(2n,n) > 4^n/sqrt(pi n) * exp(1/(24n+1)-1/(6n)).`

In particular,

`C(2n,n) > 4^n/sqrt(pi(n+1/2)).`  (5)

To verify the last step, set

`A = 1/(6n)-1/(24n+1)`.

The elementary inequality `log(1+x) >= 2x/(2+x)` for `x>=0` gives

`(1/2)log(1+1/(2n)) >= 1/(4n+1)`,

while

`1/(4n+1)-A = (72n^2-16n-1)/(6n(4n+1)(24n+1)) > 0`.

### 4.2 Off-centre decay

Let `delta_n=0` for even `n` and `delta_n=1` for odd `n`. For every admissible `k>=0`,

`C(n,(n-k)/2) / C(n,floor(n/2))`

`<= exp(-(k^2-delta_n)/(2(n+1))).`  (6)

For `n=2m`, `k=2r`, the ratio is

`prod_{j=1}^r (m-j+1)/(m+j)`.

Writing `M=m+1/2` and `d=j-1/2`,

`log((M-d)/(M+d)) = -2 artanh(d/M) <= -2d/M`.

Summing `d` gives (6). For `n=2m+1`, `k=2r+1`, use

`prod_{j=1}^r (m-j+1)/(m+j+1)`

and the same argument with `M=m+1`.

Squaring (6) and combining it with (4)--(5) yields

`C(n,(n-k)/2)^2 / C(2n,n)`

`< (2/sqrt(pi n)) sqrt(1+1/(2n)) exp(-(k^2-delta_n)/(n+1)).`  (7)

### 4.3 Uniform envelope

Insert (7) into (1), use `(n-k)/n<1`, and bound `delta_n<=1`. Then

`R_n(k) < [4 C_n e^(1/(n+1))/sqrt(pi n)] (k+1)e^(-k^2/(n+1))`,  (8)

where

`C_n = (1+1/(2(n-1))) sqrt(1+1/(2n)).`

For real `x>=0`, the function

`h_n(x)=(x+1)e^(-x^2/(n+1))`

has its maximum at

`kappa_n = (sqrt(2n+3)-1)/2`,

because `2 kappa_n(kappa_n+1)=n+1`. Therefore

`max h_n = (sqrt(2n+3)+1)/2 * exp(-1/2 + 1/(sqrt(2n+3)+1)).`

Consequently every admissible `k` satisfies

`R_n(k) < E(n)`,

where

`E(n) = [2/sqrt(pi e)] * [(sqrt(2n+3)+1)/sqrt(n)]`

`       * (1+1/(2(n-1))) sqrt(1+1/(2n))`

`       * exp(1/(sqrt(2n+3)+1) + 1/(n+1)).`  (9)

Every `n`-dependent factor in (9) is strictly decreasing: the first square-root ratio equals `sqrt(2+3/n)+1/sqrt(n)`, the two elementary correction factors decrease, and so does the exponent. Hence `E(n)` decreases.

At `n=3000`, a completely elementary outward-rounded estimate is enough:

- `2/sqrt(pi e) < 0.6847` (using `pi>3.1415`, `e>2.718`, and `2.921^2<3.1415*2.718`);
- `(sqrt(6003)+1)/sqrt(3000) < 1.433` (because `sqrt(6003)<77.48` and `sqrt(3000)>54.77`);
- `(1+1/5998)sqrt(1+1/6000) < 1.000251`;
- `c:=1/(sqrt(6003)+1)+1/3001 < 0.01308`, so `e^c <= 1/(1-c) < 1/(1-0.01308)`.

Thus

`E(3000) < 0.6847 * 1.433 * 1.000251 / (1-0.01308) < 0.995 < 1.`

Since `E` decreases,

`R_n(k)<1` for every `n>=3000` and every admissible positive `k`.

For the even central case `k=0`, (7) and (1) give an even smaller `O(n^(-1/2))` bound; in particular it is also below one throughout `n>=496`.

Combining the exact finite certificate with the analytic tail proves the theorem.

---

## 5. Conceptual corollary

The envelope has the limit

`lim_{n->infinity} E(n) = sqrt(8/(pi e)) ≈ 0.968... < 1`.

Thus the disappearance of the anomaly is not merely a finite computational accident: the relevant near-central hypergeometric mass has a uniform asymptotic ceiling strictly below the flip threshold.

This note only claims the upper-bound consequence

`limsup rho(n) <= sqrt(8/(pi e))`;

it does **not** claim that this bound is the exact asymptotic limit of `rho(n)`.

---

## 6. Reproducibility

Run:

```bash
python scope_antidiagonal_threshold_verify.py
```

Expected summary:

```text
Exact finite certificate: PASS
Checked all n = 496,...,2999 using integer arithmetic.
Tightest finite case: n=497, k=15, R=0.999955284137033
Sharpness witness: n=495, k=15, R=1.000024070891585 > 1
Analytic tail envelope at n=3000: E(3000)=0.993774873143844 < 0.995
```

The finite certificate is exact; the displayed decimals are informational only.
