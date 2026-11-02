# Sharp reverse isolation and reflection complexity of the four-state Rudin–Shapiro cover

## Finding

Consider the four-letter Rudin–Shapiro precursor substitution
\[
\sigma(a)=ab,\quad\sigma(b)=ac,\quad\sigma(c)=db,\quad\sigma(d)=dc,
\]
and its one-sided fixed point \(u=\sigma^{\omega}(a)\), **before** projecting its letters to the customary binary Rudin–Shapiro sequence. For an integer \(n\ge 1\), write \(\mathcal F_n\) for all distinct contiguous factors of \(u\) of length \(n\), \(P(n)=|\mathcal F_n|\), and \(R(n)\) for the number of factor classes under ordinary literal reversal, where a reverse is not required itself to occur.

The complete factor and reflection complexities are
\[
P(1)=4,\quad P(n)=8n-8\ (n\ge2),
\]
\[
(R(1),R(2),\ldots,R(7))=(4,4,12,16,28,36,48),
\qquad R(n)=8n-8\ (n\ge8).
\]
In particular, \(\mathcal F_8\cap\{w^{\mathrm R}:w\in\mathcal F_8\}=\varnothing\). Thus there is no reflected pair (not even a palindrome) at any length \(n\ge8\). This is sharp: exactly four length-seven factors have reversals in the language, and all four are palindromes:

`acabaca`, `babdbab`, `cdcacdc`, `dbdcdbd`.

## Assumptions and scope

All factors are finite, contiguous, and drawn from the **infinite four-letter** fixed point \(u\). Positions are zero-indexed; \(u\) is the limit of increasing prefixes \(\sigma^j(a)\). Reversal means reversing the order of symbols without changing any letter. An equivalence class consists of occurring words, so when only one of \(w,w^{\mathrm R}\) occurs, it contributes one class. No claim is made here for the two-letter coded Rudin–Shapiro word, generalized paperfolding integrals, or different substitutions.

## Proof

**1. Adjacent letters and parity.** Let \(A=\{a,d\}\) and \(B=\{b,c\}\). Each substitution image starts in \(A\) and ends in \(B\); hence even positions of \(u=\sigma(u)\) belong to \(A\) and odd positions belong to \(B\). Its adjacent-pair set is exactly
\[
E=\{ab,ac,db,dc,ba,bd,ca,cd\}.
\]
Every internal pair is in \(\{ab,ac,db,dc\}\), and every pair across an image boundary is in \(\{ba,bd,ca,cd\}\). All eight actually occur in the prefix \(\sigma^4(a)\), as can be verified by applying the four displayed substitution rules four times.

**2. Exact factor-complexity recurrence.** Write \(\sigma(x)=f(x)g(x)\), with \(f(x)\in A\) and \(g(x)\in B\). On either parity class \(A\) or \(B\), each of \(f\) and \(g\) is injective. (Indeed, \(f(a)=a,f(d)=d,f(b)=a,f(c)=d\) and \(g(a)=b,g(d)=c,g(b)=c,g(c)=b\).) Adjacent letters of \(u\) have opposite parity classes.

For \(m\ge2\), length-\(2m\) windows starting at even positions are exactly \(\sigma(x_0\cdots x_{m-1})\) for \(x_0\cdots x_{m-1}\in\mathcal F_m\); they are distinct. Windows starting at odd positions are exactly
\[
g(x_0)\,\sigma(x_1\cdots x_{m-1})\,f(x_m),\qquad x_0\cdots x_m\in\mathcal F_{m+1}.
\]
They too are all distinct: the complete middle image recovers \(x_1,\ldots,x_{m-1}\), the parity class of \(x_0\) is opposite to that of \(x_1\), and the parity class of \(x_m\) is opposite to that of \(x_{m-1}\). The endpoint letters and classwise injectivity recover \(x_0,x_m\). The two types of windows have disjoint first-letter classes. Consequently
\[
P(2m)=P(m)+P(m+1)\quad(m\ge2).
\]
Likewise, for \(m\ge1\), length-\(2m+1\) windows start at even positions as \(\sigma(x_0\cdots x_{m-1})f(x_m)\), or at odd positions as \(g(x_0)\sigma(x_1\cdots x_m)\). In either case the adjacent parity classes and classwise injectivity recover the full factor \(x_0\cdots x_m\). Thus
\[
P(2m+1)=2P(m+1)\quad(m\ge1).
\]
The base cases are \(P(1)=4\) and \(P(2)=8\) from the alphabet and \(E\). Strong induction yields \(P(n)=8(n-1)\) for every \(n\ge2\), since \(8(m-1)+8m=8(2m-1)\) and \(2\cdot 8m=8(2m)\).

**3. Exhaustive short-factor certificate.** Every \(\sigma^3\)-block has length \(8\). Therefore every length-\(\ell\) factor with \(1\le\ell\le8\) is wholly within two consecutive such blocks, and every adjacent pair of block letters belongs to \(E\). Conversely, each \(xy\in E\) occurs in \(u\), so \(\sigma^3(xy)\) occurs in \(u\). This proves the exact finite-to-infinite identity
\[
\mathcal F_\ell=\bigcup_{xy\in E}\operatorname{Fact}_\ell(\sigma^3(xy)),\quad1\le\ell\le8.
\]
Here \(\operatorname{Fact}_\ell(v)\) denotes contiguous length-\(\ell\) windows of a finite word. The attached `verify.py` evaluates this union directly, with `factors8.txt` giving the sorted 56-element set \(\mathcal F_8\). The results, where \(U_\ell\) is the number of factors whose reversal also occurs and \(Q_\ell\) the number of palindromic factors, are:

| \(\ell\) | \(P(\ell)\) | \(U_\ell\) | \(Q_\ell\) | \(R(\ell)\) |
|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 4 |
| 2 | 8 | 8 | 0 | 4 |
| 3 | 16 | 16 | 8 | 12 |
| 4 | 24 | 16 | 0 | 16 |
| 5 | 32 | 16 | 8 | 28 |
| 6 | 40 | 8 | 0 | 36 |
| 7 | 48 | 4 | 4 | 48 |
| 8 | 56 | 0 | 0 | 56 |

The set of length-eight factors is closed under neither reversal nor palindromicity: in fact, \(U_8=0\). Its sorted ASCII newline-delimited certificate has SHA-256 `2aa97abe490366aad190ec88b638589d77046f871f0d6b69982810e4a6ec0fb4`.

**4. Passage to all lengths.** If both \(w\) and \(w^{\mathrm R}\) occurred with \(|w|\ge8\), any length-eight factor \(v\) of \(w\) would occur, and \(v^{\mathrm R}\) would occur in \(w^{\mathrm R}\). This contradicts \(U_8=0\). Hence \(U_n=Q_n=0\) for all \(n\ge8\). For any \(n\), among the \(U_n\) reversible factors, the \(Q_n\) palindromes are singleton classes and the rest form \((U_n-Q_n)/2\) two-element classes; therefore
\[
R(n)=P(n)-\frac{U_n-Q_n}{2}.
\]
Applying the exact table for \(n\le8\) and the factor-complexity formula for larger \(n\) proves the claim. The listed four palindromes at length seven establish sharpness.

## Verification

From the same directory, run `python3 verify.py`. This needs only the Python standard library and the supplied `factors8.txt`. A successful run prints `VERIFY_OK`. The verifier reconstructs all eight adjacent pairs from \(\sigma^4(a)\), reproduces the complete eight-length certificate and its digest, checks the short-length table and four length-seven palindromes, compares to an independently generated length-8192 prefix, and tests the factor-complexity formula through length 256 using exhaustive substitution block windows. The proof above—not the finite-prefix checks—establishes the infinite quantifiers.

## Relationship to prior work

The standard two-letter Rudin–Shapiro sequence is a letter-to-letter projection of \(u\); its factor language and its reflection complexity must not be conflated with those of \(u\). Allouche, Campbell, Li, Shallit and Stipulanti, *The reflection complexity of sequences over finite alphabets* (2024 preprint, arXiv:2406.09302), establish in their generalized Golay–Shapiro section the distinct **binary** threshold \(15\) and \(R(n)=8n-8\) for \(n\ge15\). Their result neither states nor implies the literal four-letter cutoff \(8\), and the factor and reflection functions differ at small lengths. Allouche, Baake, Cassaigne and Damanik (2001 preprint) discuss the finite palindromic behavior of the binary family, not the complete reversal-pair spectrum of this four-letter precursor. Rampersad and Shallit (2003 preprint) examine the general notion of words avoiding reversed subwords; their constructions do not evaluate this particular fixed point. The standard substitution itself is also exhibited in Allouche, Shallit and Yassawi's survey on automatic sequences.

## Limitations

The claim is specific to the exactly specified four-symbol substitution and ordinary letter-for-letter reversal. It makes no assertion about binary projections, other conjugate substitutions, general automatic sequences, or independent scientific certification. A published or unindexed equivalent exact four-letter reflection profile may exist; targeted bibliographic comparison did not identify one. The finite factor certificate is exhaustive because of the proved substitution-block identity, not because a long prefix was sampled.

## References

- J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first posted 2024-06-13, particularly the generalized Golay–Shapiro section. https://arxiv.org/abs/2406.09302
- J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, arXiv:math/0106121, first posted 2001-06-14, §4.1. https://arxiv.org/html/math/0106121v1
- N. Rampersad, J. Shallit, *Words avoiding reversed subwords*, arXiv:math/0311121, first posted 2003-11-07, §2. https://arxiv.org/abs/math/0311121
- J.-P. Allouche, J. Shallit, R. Yassawi, *How to prove that a sequence is not automatic*, Expositiones Mathematicae 40 (2022), 1–22, §1, DOI:10.1016/j.exmath.2021.08.001. https://doi.org/10.1016/j.exmath.2021.08.001
