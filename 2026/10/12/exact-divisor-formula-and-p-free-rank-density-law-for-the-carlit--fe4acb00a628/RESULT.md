# Exact divisor formula and p-free rank-density law for the Carlitz twist family
## Finding
Let \(q=p^s\ge 3\), put \(L=q-q/p\), and let \(r_{q,n}\) be the analytic rank of the Carlitz twist by \(P_{q,n}=(\theta^{q^n}-\theta)^{q-2}\). For every \(n\ge1\),
\[
r_{q,n}=\frac1{p-1}\sum_{d\mid n}\frac{p^{v_p(d)}}d\sum_{e\mid d}\mu(e)\gcd(e,p-1)L^{d/e}.
\]
For \(n\ge2\),
\[
\left|r_{q,n}-\frac{p^{v_p(n)}}{(p-1)n}L^n\right|\le (\tau(n)^2+\tau(n))L^{n/2}.
\]
Consequently, for each fixed \(m\ge1\) with \(\gcd(m,p)=1\),
\[
\frac{r_{q,p^a m}}{L^{p^a m}}\longrightarrow\frac1{(p-1)m}\qquad(a\to\infty).
\]

The first identity evaluates the orbit formula for the entire explicit family, not only when the exponent length is a power of the characteristic. The asymptotic statement shows that the normalized ranks have a different limiting density for each fixed \(p\)-free part \(m\).

## Assumptions and scope
Let \(q=p^s\ge3\) be a prime power. Following Giraudin, set
\[
P_{q,n}=(\theta^{q^n}-\theta)^{q-2}
\]
and let \(r_{q,n}\) denote the analytic rank of the corresponding Carlitz twist. The published rank theorem expresses \(r_{q,n}\) as a weighted count of cyclic rotation orbits in \(E^n\), where
\[
E=\{\ell\in\{0,\ldots,q-2\}:p\nmid \ell+1\},\qquad |E|=L=q-q/p,
\]
the orbit weight is the product of the residues \(\ell+1\) in \(\mathbb F_p^\times\), and an orbit of least period \(d\) contributes \(p^{v_p(d)}\) exactly when that product is \(1\).

The new argument assumes this published orbit/rank theorem. It evaluates that orbit count exactly for arbitrary \(n\) by character orthogonality and Möbius inversion.

## Proof
Put \(G=\mathbb F_p^\times\), so \(|G|=p-1\). The map
\[
E\longrightarrow G,\qquad \ell\longmapsto \ell+1\pmod p,
\]
is exactly \(q/p\)-to-one. Hence for every multiplicative character \(\chi\) of \(G\), the one-letter character sum is
\[
\sum_{\ell\in E}\chi(\ell+1)=
\begin{cases}
L,&\chi=1,\\
0,&\chi\ne1.
\end{cases}
\]
For words of length \(d\), let \(W_d(\chi)\) be the sum of \(\chi\) of the total product over all words, and let \(S_d(\chi)\) be the same sum restricted to words of least period exactly \(d\). Then
\[
W_d(\chi)=
\begin{cases}
L^d,&\chi=1,\\
0,&\chi\ne1.
\end{cases}
\]
Every length-\(d\) word is uniquely the \(e\)-fold repetition of a primitive word of length \(d/e\). Its product is the \(e\)-th power of the primitive product, so
\[
W_d(\chi)=\sum_{e\mid d}S_{d/e}(\chi^e).
\]
Möbius inversion on the divisor lattice gives
\[
S_d(\chi)=\sum_{e\mid d}\mu(e)W_{d/e}(\chi^e).
\]
Let \(C_d\) be the number of primitive length-\(d\) words whose product is \(1\) in \(G\). Character orthogonality gives
\[
C_d=\frac1{p-1}\sum_\chi S_d(\chi).
\]
For fixed \(e\), exactly \(\gcd(e,p-1)\) characters satisfy \(\chi^e=1\). Therefore
\[
C_d=\frac1{p-1}\sum_{e\mid d}\mu(e)\gcd(e,p-1)L^{d/e}.
\]
Each primitive rotation orbit of length \(d\) contains exactly \(d\) words, so the number of weight-one orbits of least period \(d\) is \(C_d/d\). A length-\(n\) orbit has least period some \(d\mid n\), and the published rank theorem assigns it weight \(p^{v_p(d)}\). Thus
\[
r_{q,n}=\sum_{d\mid n}p^{v_p(d)}\frac{C_d}{d},
\]
which is the stated divisor formula.

For the error bound, isolate the term \((d,e)=(n,1)\). Since \(p^{v_p(d)}/d\le1\), since \(\gcd(e,p-1)/(p-1)\le1\), every proper divisor \(d<n\) satisfies \(d\le n/2\), and every \(e>1\) satisfies \(n/e\le n/2\). Bounding the remaining divisor pairs in absolute value gives
\[
\left|r_{q,n}-\frac{p^{v_p(n)}}{(p-1)n}L^n\right|
\le(\tau(n)^2+\tau(n))L^{n/2}.
\]
Finally, if \(n=p^a m\) with fixed \(\gcd(m,p)=1\), then \(p^{v_p(n)}/n=1/m\), while \(\tau(p^a m)^2L^{-p^a m/2}\to0\). Dividing by \(L^n\) proves the limiting-density law.

## Verification
The standalone verifier implements the divisor formula using exact integer arithmetic, independently enumerates cyclic word orbits for small parameters, and checks all forty rank values displayed in the motivating paper's table. It also checks the published closed form on four successive \(p\)-power lengths for eight prime powers \(q\).

The replay result is recorded in `verification_output.txt`. Finite computation is corroborative: the universal formula follows from the symbolic character-orthogonality and Möbius-inversion proof above.

## Relationship to prior work
Giraudin proves the orbit factorization and weighted orbit formula that are the starting point here, and derives the closed rank formula
\[
r_{q,n}=\frac{L^n}{p-1}
\]
when \(n\) is a power of \(p\). The paper also tabulates small values for general \(n\), but the inspected theorem, corollary, proof, and table do not give an all-\(n\) divisor evaluation or the fixed-\(p\)-free-part density law.

A recent survey of analytic ranks of Carlitz twists discusses the boundedness problem and earlier constructions but predates this explicit family. Targeted searches for the exact family, primitive-necklace formulations, Möbius divisor sums, and normalized rank densities found no statement implying the theorem above. General necklace Möbius inversion is a classical combinatorial technique; the contribution here is its character-weighted evaluation of this newly introduced analytic-rank family and the resulting asymptotic structure.

## Limitations
The proof depends on the published orbit/rank theorem for this Carlitz-twist family and does not rederive the underlying \(L\)-function factorization. The displayed error term is intentionally elementary and is not claimed to be optimal. The density statement concerns subsequences with fixed \(p\)-free part and does not assert a single limit over all \(n\).

## References
1. D. Niedbala Giraudin, *An explicit family of twists of the Carlitz module with unbounded analytic rank*, arXiv:2610.00379v1, 2026.
2. D. Niedbala Giraudin, *Analytic ranks of twists of Carlitz modules -- a survey of results*, arXiv:2509.16160, 2025.
