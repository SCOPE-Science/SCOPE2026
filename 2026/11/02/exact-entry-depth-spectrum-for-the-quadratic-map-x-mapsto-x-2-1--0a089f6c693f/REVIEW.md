# Independent mathematical audit

## correctness

PASS

For each k>=3, f(x)=x²+1 reverses parity; its square on even 2-adics is a contraction with ratio <=1/4 because g(x)-g(y)=(x-y)(x+y)(x²+y²+2) and both last factors contribute one 2-adic digit. Unique even fixed point e≡2 (mod 8) and o=f(e)≡5 (mod16) give the unique attracting 2-cycle. Near even and odd cycle vertices, valuations of f(y)-f(vertex) gain alternately 2 and 1 digits. Separate input parity classes x odd, x≡2 mod4, x≡0 mod4 give stated exact depth and valuation formulas. Odd-square congruences have four roots modulo 2^h when h>=3, giving piecewise O_k and E_k counts. Summing disjoint classes establishes B_k(t) exactly for every t<=D_k=floor((2k+1)/3); precisely x≡0 mod4 attain D_k, a quarter of residues. Independently enumerated complete functional digraphs for every k=3..13 and checked cumulative counts and maximal-depth class against the formula, without using repo verifier. Finitary checks do not prove the all-k statement; 2-adic valuation induction does.

## originality

PASS

Best-of-knowledge PASS for the full finite-modulus entry-depth histogram, exact maximum and maximizing quarter-class. Fan--Liao 2010 Theorem 6.1(4) expressly covers x²+1 as x²-lambda with lambda=-1 ≡3 mod4 and proves the qualitative all-2-adic attracting two-cycle, which is prior and not claimed new. Fan--Liao 2014 and Somer--Krizek concern unshifted x²; prime modulus digraphs differ. Searches and relevant primary theorem reading did not find the sharp tail-count law, but older p-adic graph work may overlap.

## value

PASS

Preperiodic first-entry depth is a standard intrinsic invariant of a finite functional digraph. This theorem classifies every tail length at every dyadic precision for a basic shifted quadratic map, with a sharp depth and positive-density extremal class, quantifying what the known 2-adic basin theorem omits. Natural exact all-level structure rather than a small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
