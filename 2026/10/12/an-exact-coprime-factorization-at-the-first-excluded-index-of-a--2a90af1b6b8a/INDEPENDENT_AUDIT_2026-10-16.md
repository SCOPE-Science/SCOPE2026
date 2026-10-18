# Independent mathematical audit

## correctness

PASS

For n≥1 with 3∤n, set z=2^n and epsilon=(-1)^n. The Jacobsthal closed form produces C=z²+epsilon z+1, E=z^6+epsilon z³+1 and F=z^18+epsilon z^9+1 with T_n=CE/171 and T_(3n)=EF/171. C,F are divisible by 3; -8 mod 19 has order 3, so w=(-8)^n is a nontrivial cube root for 3∤n, which gives 19|E. Thus H=E/57, U=C/3, V=F/3 are integers and the quotient factors are HU and HV. Mod C, z³≡epsilon, hence z^9≡epsilon, F≡3, gcd(C,F)=3 and gcd(U,V)=1. Therefore gcd(T_n,T_(3n))=H=J_(9n)/(57J_(3n)). For n=1 U=1; for all n≥2 C>3 so T_n∤T_(3n). Independent arbitrary-precision test n=1..25 checked original J-values, gcd and all factors; unbounded proof is modular algebra, not enumeration.

## originality

PASS

Panraksa–Tangboonduangjit (JIS 2022) prove Δ-almost strong divisibility for normalized Lucas quotients under gcd(mn,Δ)=1. Here the Jacobsthal discriminant Δ=9 and the pair (n,3n) violates the hypothesis, so their Theorem 7 does not imply this gcd. General Sanna p-adic Lucas valuations can rederive prime-wise behavior, but the inspected source summary does not give this pairwise normalized-quotient factorization. No inspected Resultary cyclotomic/Jacobsthal result states the exceptional gcd and exact missing factor. Best-of-knowledge PASS, with potential implicit corollary risk.

## value

PASS

The exact factorization resolves the first excluded local family of a published almost-strong divisibility theorem and identifies precisely why the naive extension fails. The independent coprime factors and sharp n=1 versus all n≥2 boundary are natural arithmetic information, beyond a table of small Jacobsthal integers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
