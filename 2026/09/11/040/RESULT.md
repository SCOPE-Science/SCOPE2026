# Complete affine integral-point determination for C4: y^2 = x^5 - 5x^3 + 4x^2 + x - 1

## Context

This is an emergent finding from the investigation of the admitted target
`C4(Q) = {infinity, (1,0), (2,3), (2,-3)}` via Coleman bound at p=11 and
Mordell-Weil sieve at 23 and 41. That full rational closure is blocked in a
stdlib-only environment (hand-rolled genus-2 Jacobian arithmetic failed
validation; elementary denominator analysis stops at integral x). The exact
integral slice on the same curve was isolated and closed completely by an
elementary proof. No claim about non-integral rational points is made.

## Definitions

- `C4: y^2 = f(x)` with `f(x) = x^5 - 5x^3 + 4x^2 + x - 1` over Q (odd-degree
  quintic model, one point at infinity).
- `g(x) = x^4 + x^3 - 4x^2 + 1`, so `f(x) = (x-1) g(x)`.
- `A(x) = 2x^2 + x - 4`, `B(x) = 2x^2 + x - 3 = A(x)+1`,
  `A2(x) = 2x^2 + x - 5 = A(x)-1`.
- `M(x) = 4x^2 + 3x - 8`, so `g'(x) = x M(x)`.
- Affine integral locus means integer solutions `(x,y)` in Z^2 to `y^2=f(x)`.

## Result

**Theorem.** The affine integral locus of
`C4: y^2 = x^5 - 5x^3 + 4x^2 + x - 1` over Z is exactly three points:
`(1,0)`, `(2,3)`, `(2,-3)`.

In particular `f(1)=0`, `f(2)=9`, and `f(x)` is negative or strictly between
consecutive squares (up to the coprime-factor reduction) for every other
integer `x`.

## Proof / evidence

Exact integer arithmetic throughout; replay script checks every clause.

1. **Factor and smoothness.** `f(x)=(x-1)g(x)` as polynomials. Exact
   Bareiss elimination on the 9x9 Sylvester matrix of `(f,f')` gives
   `Res(f,f') = disc(f) = 1957 = 19 x 103 != 0`; the affine model is smooth.
2. **Coprimality.** `g(1)=-1`, i.e. `g(x)=(x-1)q(x)-1`, so for every integer
   `x`, `gcd(x-1,g(x))=1`. For `x-1>0` both factors are positive (for x>=2),
   so if `f(x)=(x-1)g(x)` is a square then each factor is a square.
3. **Sandwich identities** (exact polynomial identities):
   `4g-A^2 = -(x-2)(x-6)`,
   `B^2-4g = 5x^2-6x+5` (discriminant `-64`, hence always positive),
   `4g-A2^2 = 3x^2+10x-21`.
4. **Integral x>=2.** `x=2`: `f=9`. For `x in {3,4,5}`:
   `A(x)^2 < 4g(x) < B(x)^2=(A(x)+1)^2` strictly with `A>0`, so `g` (hence
   `f`) is nonsquare. `x=6`: `g(6)=37^2` but `f(6)=6845` with
   `82^2 < 6845 < 83^2`. For integer `x>6`: `3x^2+10x-21>0` and
   `-(x-2)(x-6)<0` give `A2(x)^2 < 4g(x) < A(x)^2=(A2(x)+1)^2` with
   `A2>0`, so `g` and hence `f` are nonsquare.
5. **Integral x<=1.** For `x<=-3`, `M'(x)=8x+3<0`, `M(-3)=19>0`, so
   `M>0` and `g'(x)=xM(x)<0`; `g` is strictly decreasing there with
   `g(-3)=19>0`, so `g>0` while `x-1<0`, hence `f(x)<0`. Remaining
   `x in {-2,-1,0,1}` give `f=21,6,-1,0` with `16<21<25`, `4<6<9`,
   leaving only `(1,0)`.

Replay: `python3 output/artifacts/verify_integral.py` prints `VERIFY_OK`
(stdlib only, exact integer arithmetic).

Supporting numerics (not part of the proof):
`python3 output/artifacts/point_counts.py` gives `#C(Fp)=14,21,46` and
`#C(Fp^2)=118,589,1726`, `#J(Fp)=98,636,1544` for `p=11,23,41` (good primes;
`19,103` are the bad primes).

## Limitations

Integral points only. The full rational set `C4(Q)` (non-integral
`x=a/b`) is explicitly left open: denominator analysis leaves `s>1`
denominators a priori possible and the sandwiches grip integers only.
No rank certificate, Coleman bound, or sieve elimination is claimed.

## Reproducibility

- `output/artifacts/verify_integral.py` — complete proof replay (`VERIFY_OK`).
- `output/artifacts/point_counts.py` — Fp/Fp^2 counts and Jacobian orders.
- Both stdlib-only; verified in seconds.

## References

- M. Stoll, The Mordell-Weil Sieve.
- S. Siksek, Chabauty and the Mordell-Weil Sieve (notes; different example).
- N. Bruin, M. Stoll and related rank-1 Chabauty+sieve method literature
  (method sources; no C4 closure).
- LMFDB genus-2 curves (no entry for this polynomial in fused results).
