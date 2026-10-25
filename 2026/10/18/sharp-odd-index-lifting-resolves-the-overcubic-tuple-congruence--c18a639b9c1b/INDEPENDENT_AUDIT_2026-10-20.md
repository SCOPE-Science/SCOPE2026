# Independent mathematical audit

## correctness

PASS

Let A=phi(-z)phi(-z^2)=F^-1=1+2T, F(z)=f4/(f1² f2), t=2^(i-3)(2k+1), M=4t-1. Binomial expansion F^4=A^-4 gives F^4=1+8C with integral C; modulo 2, C=T+T² equals sum_{r>=1} z^(r²)+sum_{r>=1}z^(4r²), so C² has even-only exponent parity and A C² has even-only exponents modulo 2 because A≡1 mod2. Then F^M=A(1+8C)^t; the j>=3 terms have valuation >= i+6 using j*C(t,j)=t*C(t-1,j-1), quadratic coefficient divisible by 2^(i+2) gains one factor at odd exponents. Therefore for every positive odd n, b_M(n) ≡ (1-t)a(n)+t b3(n) mod 2^(i+3). Coefficients a(8u+5)=a(8u+7)=0 exactly since no square+2*square equals 5 or 7 mod8; known Saikia–Sarma 2024 Theorem1.1 proves b3 at these progressions divisible 32/64, giving b_M divisibility 2^(i+2) and 2^(i+3). Sharpness at 5 and 7 follows b3(5)=1248=32*39, b3(7)=9792=64*153, and (A C²)[7]=7424 (high valuation) while remaining corrections vanish modulo 2^(i+4). Independent polynomial arithmetic independently computed these degree5/7 coefficients and verified 12 parameter pairs through degree32. The formal power series proof is for every i>=3,k,n>=0, not just the finite checks.

## originality

PASS

The stated Maity–Saikia Conjecture 1.5 targeted precisely the tuple parameter M=2^ik+2^(i-1)-1 and 8u+5/7 moduli; submitted odd-index lifting and universal sharpness give a nontrivial new resolution relative to accessible primary evidence. Prior triple congruences are fully credited. Strong plausible related papers not fully accessible are preserved as a real risk, not taken as automatic failure.

## value

PASS

Sharp 2-adic proof resolving both branches of an explicit arXiv conjecture is a clearly motivated arithmetic advance. The key formal-series parity cancellation yields an independent all-odd-index transfer congruence and uniform exact valuations, not just finite data or a routine parameter substitution. The theorem has natural all-parameter range and separates the known base triple congruences from the new lifting lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
