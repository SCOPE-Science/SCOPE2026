# Independent mathematical audit

## correctness

PASS

Checked the full fixed-q, k=3 theorem, including q=1 and principal/nonprincipal quadratic/nonquadratic characters. Prime-power D_3(p^j)=binom(j+2,2)/3 (j>=1) has exact local generating series (1-t)^(-1)(1-t^2)^(-1)[1+(4/3)t^3+(2/3)t^4/(1-t)], hence D_3=1*1_square*c. Since c(p)=c(p^2)=0 and c(p^3)=4/3,c(p^j)=2/3 for j>=4, G_chi converges absolutely for Re(s)>1/3. The two-region square-divisor hyperbola at y=z=X^(1/3) is exactly exhaustive, with subtraction of their intersection. Principal A_chi(Y)=theta_q Y+O_q(1) and periodic nonprincipal A=O_q(1); partial summation yields the L(1/2,chi) constants. For chi=chi0, the three X^(2/3) terms cancel (-1+2-1)theta_q^2. For nonprincipal chi^2=chi0 only theta_q L(1/2,chi)sqrt(X) remains; other chi yield O_q(X^(1/3)). Convolving with c and extending absolutely convergent tails gives O_{q,eps}(x^(1/3+eps)), and character orthogonality gives exactly theta_q/phi(q) factors. For chi_-3 the paired series for L(1/2,chi_-3) is strictly positive; G product is positive using (1-t^2)[1+t^2(3-2t)/(3(1-t)^2)] for t=chi(p)/sqrt(p) in [-1/sqrt(2),1/sqrt(2)]. Independent symbolic algebra verified both local identities; independent direct exact arithmetic matched all 20000 D3 coefficients with the square-divisor convolution; 42 direct hyperbola identities covered principal, quadratic and order-four characters of moduli 3,4,5. These finite tests are corroborations, not infinite proofs.

## originality

PASS

Best-of-knowledge full-result comparison: the primary Karras 2026 Theorem 3.1 treats the same D_k and reduced arithmetic progressions, but gives only a linear main term and error O(x^(1/2+eps)). Karras–Derbal 2020 Theorem 1 gives a global linear mean with error O(x^(1/2)(log x)^(k-2)). These do not identify the signed sqrt(x) contribution or a power-saving remainder relative to it. Bouakkaz–Derbal 2023 treats k=2; Bouderbala–Karras 2022 studies a different gcd-weighted hyperbolic double sum. OEIS A308042 records the leading Euler-product constant, not the quadratic-character residue-class contrast. Searches in Resultary and the published repository found no directly dominating theorem; no universal novelty conclusion follows from search silence.

## value

PASS

The k=3 normalized ordered-divisor mean over fixed reduced arithmetic progressions is a natural object already studied in the cited 2026 work. Showing a power-saving separation between a genuinely present sqrt(x) term and O(x^(1/3+eps)) is a nontrivial second-order arithmetic result, and the strict positive mod-3 discrepancy identifies an exact natural quadratic-character bias. This is neither a renamed leading mean nor an arbitrary small parameter slice: the square-divisor factorization explains why k=3 admits an unusually sharp explicit secondary term. No extension to growing q or error optimality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
