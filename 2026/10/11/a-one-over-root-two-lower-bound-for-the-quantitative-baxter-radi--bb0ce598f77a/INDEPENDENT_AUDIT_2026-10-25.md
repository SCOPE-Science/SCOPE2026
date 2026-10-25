# Independent mathematical audit

## correctness

PASS

Let B=||b||_A1<1, m=(|b|²)^hat(0)=||b||_2², c=1-m>0, h=-(|b|²-m)/(1-m). The SU(2) identity gives |a|²=c(1+h), with |||b|²||_A1<=B² and nonnegative zero coefficient m. Therefore ||h||_A1 <=(B²-m)/(1-m)<=B²<1. Thus log|a|²=log c+log(1+h) has A1 norm <=-log(1-m)-log(1-||h||)<=-2log(1-B²). Taking u=log|a|, outerness and positive a*(0) imply log a* =u_hat(0)+2 sum_{n>=1}u_hat(n) z^n and ||log a||_A1<=2||u||_A1<=-2log(1-B²). Wiener Banach-algebra exponentiation yields ||a^-1||_A1<= (1-B²)^-2. March 2026 Proposition 2 with w=1, a* outer, and B<1/sqrt2-ε gives ||F||_l1 ≲ B/[ε(1-B²)^2]. For fixed eta>0, B<1/sqrt2-eta bounds this solely in eta; eta>=1/sqrt2 is vacuous. The October negative construction gives only tau<=1, so 1/sqrt2<=tau<=1. No proof of tau equality or of sharp inverse constant. Independently recomputed the exact Git tree and source-JSON blob SHAs; rational two-coefficient test inputs (1/3,1/4), (2/5,1/3), (1/5,1/7) satisfy the h inequality and numerically the inverse bound; these bounded checks corroborate but do not prove universality.

## originality

PASS

The published October 1 primary paper leaves 1/sqrt(3)<=tau<=1 and already uses a centered log spectral-factor method. Its §6.1 estimates the centered term by 1+||b|²||-c, rather than the sharp identity |||a|²-c||=|||b|²-m||=|||b|²||-m. The independently audited use of SU(2) cancellation bounds ||h||<=B² for every B<1 and supplies uniform ||a^-1||<= (1-B²)^-2; combining with March Proposition 2 improves the B-only radius through 1/sqrt(2). The prior papers furnish essential ingredients but do not state/prove this stronger uniform combination. Resultary queries returned the same published record as nearest hit, not an earlier independently covering result. Priority remains best-of-knowledge.

## value

PASS

The authors of the October primary paper explicitly ask for the largest radius with B-only control. A proven improvement from 1/sqrt3 to the previous method’s natural 1/sqrt2 endpoint fills a significant portion of the open parameter interval and supplies a reusable quantitative uniform spectral-factor estimate. While the proof is short and draws on the paper’s existing centered-h method, the exact cancellation that changes the admissible interval is directly relevant and not a merely cosmetic normalization, known-table computation, or arbitrary slice. Its importance is this precise threshold; no claim of solving the remaining endpoint question or of a paper-sized theorem is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
