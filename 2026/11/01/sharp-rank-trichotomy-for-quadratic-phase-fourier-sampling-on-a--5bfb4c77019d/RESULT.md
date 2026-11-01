# Sharp rank trichotomy for quadratic-phase Fourier sampling on a prime-field parabola

## Finding
Let \(p\ge3\) be a prime, \(\zeta=\exp(2\pi i/p)\), and \(a,b\in\mathbb F_p\). Define the \(p\)-by-\(p\) complex matrix, indexed by \(s,t\in\mathbb F_p\), by
\[
M_{p;a,b}(s,t)=\zeta^{a s t+b s^2t^2}.
\]
Here exponents are interpreted in \(\mathbb F_p\) before choosing any integer representatives. Its **exact complex rank** is
\[
\boxed{\operatorname{rank}_{\mathbb C}M_{p;a,b}=\begin{cases}
1,&a=b=0,\\
(p+1)/2,&a=0,\ b\ne0,\\
p,&a\ne0.
\end{cases}}
\]
Equivalently, the Fourier transform of a function supported on the finite-field parabola \(\{(t,t^2):t\in\mathbb F_p\}\), evaluated at the \(p\) frequencies \(\{(as,bs^2):s\in\mathbb F_p\}\), uniquely determines the function **for every** \(b\in\mathbb F_p\) exactly when \(a\ne0\); in this case \(M_{p;a,b}\) is nonsingular. The numerical normalization of the Fourier transform only rescales the matrix and does not change its rank.

## Assumptions and scope
The field is the **prime** field \(\mathbb F_p\), not an arbitrary extension field, and \(p\) is odd. The characters are complex additive characters \(\zeta^u\). The row and column orderings are arbitrary bijections with \(\mathbb F_p\); they do not affect rank. All quantified parameter pairs \((a,b)\) are included, including zero parameters. The conclusion concerns injectivity, not a quantitative condition number or orthogonality of the sampled exponentials.

## Proof
**1. Multiplicative Hankel reduction.** More generally take any function \(h:\mathbb F_p\to\mathbb F_p\) satisfying \(h(0)=0\), and put \(H_h(s,t)=\zeta^{h(st)}\). With the zero index first, the first row and column are all ones. Subtracting the first row from every other row and then deleting its first row and column shows that
\[
\det H_h=\det G_h,\qquad G_h(s,t)=\zeta^{h(st)}-1\quad(s,t\in\mathbb F_p^\times).
\]
For every multiplicative character \(\chi:\mathbb F_p^\times\to\mathbb C^\times\), define
\[
L_\chi(h)=\sum_{u\in\mathbb F_p^\times}\chi(u)(\zeta^{h(u)}-1).
\]
The operator \(G_h\), applied to the vector \(t\mapsto\chi(t)\), gives \(L_\chi(h)\) times \(s\mapsto\chi^{-1}(s)\). Character orthogonality therefore yields the exact determinant factorization
\[
\det H_h=(-1)^{(p-3)/2}\prod_{\chi\in\widehat{\mathbb F_p^\times}}L_\chi(h).
\]
The sign follows because inversion of the \(p-1\) multiplicative characters fixes exactly two (the trivial and quadratic characters) and swaps the others in \((p-3)/2\) pairs. This factorization is an identity, including in degenerate cases.

**2. A singleton-fiber nonvanishing lemma.** Assume that some \(v\in\mathbb F_p^\times\) has **exactly one** preimage \(u_0\in\mathbb F_p^\times\) under \(h\). The trivial-character factor satisfies
\[
\operatorname{Re}L_1(h)=\sum_{u\ne0}(\cos(2\pi h(u)/p)-1)<0,
\]
because \(h(u_0)=v\ne0\). For nontrivial \(\chi\), its character sum vanishes, so
\[
L_\chi(h)=\sum_{u\ne0}\chi(u)\zeta^{h(u)}=\sum_{j=0}^{p-1}c_j\zeta^j,
\qquad c_j=\sum_{u\ne0:h(u)=j}\chi(u).
\]
Every \(c_j\) belongs to \(K=\mathbb Q(\zeta_{p-1})\), since a multiplicative character has values among the \((p-1)\)-st roots of unity. The cyclotomic extensions \(K\) and \(\mathbb Q(\zeta)\) are linearly disjoint, since their conductors are coprime. Hence the minimal polynomial of \(\zeta\) over \(K\) is still \(1+z+\cdots+z^{p-1}\). If \(L_\chi(h)=0\), all \(c_j\) must coincide. But \(\sum_jc_j=\sum_{u\ne0}\chi(u)=0\), so every \(c_j\) would be zero. This contradicts \(c_v=\chi(u_0)\ne0\). Thus **all** \(L_\chi(h)\) are nonzero and \(H_h\) is nonsingular.

**3. All nonzero linear parameters.** Set \(h(u)=a u+b u^2\). If \(a\ne0\) and \(b=0\), then every nonzero phase \(v\) has exactly one nonzero preimage. If \(a b\ne0\), take \(u_0=-a/(2b)\ne0\) and \(v=-a^2/(4b)\ne0\). Completing the square yields
\[
h(u)-v=b(u-u_0)^2,
\]
so \(u_0\) is the unique preimage of \(v\), even over the full field. The lemma proves rank \(p\) for every \(a\ne0\) and every \(b\).

**4. Vanishing linear parameter.** If \(a=b=0\), the matrix is all ones and has rank one. If \(a=0\), \(b\ne0\), the rows and columns depend only on \(s^2\) and \(t^2\). Their square values range over \(Q=\{0\}\cup\{u^2:u\in\mathbb F_p^\times\}\), with \(|Q|=(p+1)/2\). Therefore the rank equals the rank of the square submatrix \((\zeta^{bxy})_{x,y\in Q}\) of the prime-order discrete Fourier matrix (with row indices \(bQ\) and column indices \(Q\)). Chebotarev's prime Fourier minor theorem guarantees every such minor is nonzero; hence this matrix has rank \((p+1)/2\). This completes the classification.

## Verification
The attached standalone `checker.py` constructs \(M_{p;a,b}\), computes numerical singular-value ranks for all coefficient pairs at primes \(3,5,7,11\), and for six representative pairs at primes \(13,17,19\); it also checks the exact singleton-fiber identity modulo each prime and the symbolic rank predictions. The numerical tests passed. These finite checks support the algebra; the proof above, using cyclotomic disjointness and Chebotarev's theorem, is the argument for **all** odd primes.

## Relationship to prior work
Mockenhaupt and Tao established the finite-field restriction/extension framework for paraboloids, especially its global \(\ell^p\)-to-\(\ell^q\) norm bounds, whereas the present question fixes a sharply constrained set of exactly \(p\) observation points and asks about rank. Tao's treatment of Chebotarev's theorem gives the necessary nonvanishing Fourier minor in the degenerate \(a=0\) case. The more recent finite-field parabola extension work of González-Riquelme and Oliveira e Silva determines sharp extension norms and extremizers rather than these restricted sampling ranks. Zhou's principal-minor results concern Fourier matrices on groups with distinct prime factors and do not entail this principal submatrix over \(\mathbb F_p^2\). No claim is made to invent the cyclotomic or character-diagonalization methods. See the limitations and references below.

## Limitations
The prime-field restriction is essential to the proof; no extension-field assertion is made. Nonsingularity does not provide an effective uniform stability or inverse-norm bound. The comparison against earlier literature is bounded: full indexing of older results on finite Fourier submatrices and quadratic curves was not established, and an equivalent rank statement could exist. The result has received no independent mathematical audit.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, first available as arXiv:math/0204234 (2002), especially sections 2–5; https://arxiv.org/abs/math/0204234.
2. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286 (2003), Lemma 1.3 (Chebotarev's nonvanishing minors); https://arxiv.org/abs/math/0308286.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024), sections 1–2; https://arxiv.org/abs/2405.16647.
4. W. Zhou, *Principal Non-singularity of Fourier Matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189 (2025), introduction and theorem 1; https://arxiv.org/abs/2505.01189.
