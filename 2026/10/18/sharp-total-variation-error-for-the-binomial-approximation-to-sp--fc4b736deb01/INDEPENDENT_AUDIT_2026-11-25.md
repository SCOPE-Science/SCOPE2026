# Independent mathematical audit

## correctness

PASS

The Stirling generating function is the mgf of the Irwin–Hall sum after division by t^k, giving exactly E Z^r=S(k+r,k)/binom(k+r,k). Taking the binomial weight outside the expectation and tilting by (φ+Z)^R normalizes the mixture. Since Q=Z/(φ+Z) is strictly increasing on the support of a nondegenerate tilted law, the variance excess R(R−1) Var(Q) is strictly positive for R≥2, against the binomial at the same exact mean. The endpoint moment expansion uses the exact density v^(k−1)/(k−1)! for v=k−Z in (0,1), and a complete beta integral with exponentially small relative tail error outside a fixed neighborhood. Centered Taylor expansion at E Q in L1 has O(R) second derivative norm on a compact parameter interval (expectation of the absolute binomial second score) and O(R²) globally by the signed finite differences of binomial masses. This leaves O(1/R) distance to the mean-matched binomial. The remaining first score at q has L1 norm E|B_R−Rq|/[q(1−q)], whose CLT limit after division by √R follows from uniform integrability. For an independent check, take R+k independent trials with k named outcomes of weight 1 and one null of weight φ. Counting onto assignments shows that spillage equals the total active count minus k conditional on seeing all k names; the unconditional shifted Bin(R+k,q) differs in TV by at most k(1−1/(k+φ))^(R+k). Write that shifted binomial as Bin(R,q) minus an independent L distributed as Bin(k,1−q). If b is the Bin(R,q) mass function, E[b(·+L)]−b=E L Δb+O_L1(R^(-1)), because Δ²b factors into the convolution of first differences of two roughly equal binomials, each of L1 norm twice its modal mass by unimodality. Thus TV is k(1−q) max b + O(R^(-1)), yielding exactly the stated constant by Stirling. The same conditioning argument gives the stated variance correction, since the unconditional variance is (R+k)q(1−q) and conditioning changes the bounded second moment by only exponentially small terms times a polynomial in R.

## originality

PASS

O’Neill already defines the law, identifies the binomial approximation through its asymptotic moments, and supplies the exact finite moments. The sharp first-order TV coefficient relative to the specific ordinary unshifted Bin(R,q) is not supplied by those moment statements. None of the strongest inspected primary or indexed statements covers that coefficient; the continuous tilted binomial mixture is not O’Neill's mixture with the component and target laws reversed. The originality judgment is on the sharp TV theorem, not on the Stirling moment identity or binomial-mixture variance formula.

## value

PASS

For the natural binomial already proposed for this distribution, the result quantifies precisely how good the approximation is and identifies the mechanism: an order-one count displacement produces the leading TV loss, while matching the mean removes that first-order loss. The exact mixture makes the finite-size spread distinction interpretable. This separates two practical approximations that asymptotic first moments alone cannot distinguish in TV.

The dated certificate retains the supplied scientific assessment, sources and limitations.
