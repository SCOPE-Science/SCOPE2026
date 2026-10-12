# A self-similar arch factorization for all multinacci words

## Finding
Fix an integer \(m\ge2\). On \(\Sigma_m=\{0,1,\ldots,m-1\}\) define the substitution
\[
\sigma_m(j)=\begin{cases}0(j+1),&0\le j<m-1,\\0,&j=m-1.\end{cases}
\]
Let \(x=x_0x_1\cdots=\sigma_m^\omega(0)\). A scattered subsequence preserves relative order but need not be contiguous; let \(U_m(N)\) be the greatest \(k\ge0\) such that every word of length \(k\) over \(\Sigma_m\) occurs as a scattered subsequence of \(x_0\cdots x_{N-1}\), with \(U_m(0)=0\).

Put \(P=\sigma_m^{m-1}(0)\), \(Q_j=\sigma_m^{m-1}(j)\), and
\[
B_j=\begin{cases}Q_{j+1}P,&0\le j<m-1,\\ P,&j=m-1.\end{cases}
\]
The **entire greedy arch factorization** of the infinite word is the explicit, nonperiodic concatenation
\[
\boxed{x=P\,B_{x_0}B_{x_1}B_{x_2}\cdots.}
\]
Each displayed block is a *single* greedy arch, and its last letter is its unique occurrence of \(m-1\). In particular,
\[
\boxed{|P|=2^{m-1},\quad |B_j|=2^m-2^j\quad(0\le j<m).}
\]
If \(E_s\) denotes the one-based endpoint of the \(s\)-th arch, then
\[
E_1=2^{m-1},\qquad E_{r+2}-E_{r+1}=2^m-2^{x_r}\quad(r\ge0).
\]
Thus the set of arch lengths is *exactly* \(\{2^m-2^j:0\le j<m\}\), each length occurs infinitely many times, and the sequence of subsequent arch lengths uniquely recovers \(x\) by its injective letter coding.

For **every** integer \(N\ge0\), without exceptions,
\[
\boxed{U_m(N)=\#\{0\le i<N:x_i=m-1\}.}
\]
Write \(L_n=|\sigma_m^n(0)|\). For every \(n\ge m\),
\[
\boxed{U_m(L_n)=L_{n-m}.}
\]
Let \(\lambda_m\in(1,2)\) be the real root of \(\lambda_m^m=\lambda_m^{m-1}+\cdots+1\). Among all arches, the limiting frequency of length \(2^m-2^j\) is precisely \(\lambda_m^{-(j+1)}\). Consequently,
\[
\boxed{\lim_{N\to\infty}\frac{U_m(N)}N=\lambda_m^{-m}.}
\]

## Assumptions and scope
The alphabet is the full \(m\)-letter alphabet \(\Sigma_m\), including when a short prefix omits some symbols. An arch of a finite or infinite word is the *shortest* initial segment containing every symbol of \(\Sigma_m\); remove it and repeat. No individual arch is assumed periodic. The substitution fixed point begins in zero and all indices are zero-based except explicitly one-based arch endpoints. Powers of the substitution mean repeated morphism composition, not arithmetic powers.

## Proof
**Step 1: exact substitution images.** For \(0\le h\le m-1\), the word \(\sigma_m^h(0)\) has length \(2^h\), contains exactly one occurrence of \(h\), which is its last letter, and contains no letter exceeding \(h\). Indeed, for \(h<m-1\), each letter \(j\le h\) maps to \(0(j+1)\); the whole word doubles and the unique terminal \(h\) produces its unique terminal \(h+1\). In particular, \(P=\sigma_m^{m-1}(0)\) contains every alphabet symbol but has a unique final \(m-1\).

For \(1\le j<m\), iteration of the chain \(j\mapsto0(j+1)\) until the terminal letter \(m-1\mapsto0\) gives the *exact* concatenation
\[
Q_j=\sigma_m^{m-2}(0)\,\sigma_m^{m-3}(0)\cdots\sigma_m^{j-1}(0).
\]
Every factor on the right avoids \(m-1\), and hence so does \(Q_j\). Its length is \(\sum_{t=j-1}^{m-2}2^t=2^{m-1}-2^{j-1}\). Thus \(B_j\), for \(j<m-1\), consists of a string avoiding \(m-1\) followed by the unique-final-\(m-1\) word \(P\); \(B_{m-1}=P\) has the same property. Their lengths are \(|B_j|=2^{m-1}+(2^{m-1}-2^j)=2^m-2^j\) for \(j<m-1\), and \(|B_{m-1}|=2^{m-1}=2^m-2^{m-1}\).

**Step 2: the exact infinite factorization.** Because \(x=\sigma_m(x)\), also \(x=\sigma_m^m(x)=\sigma_m^{m-1}(\sigma_m(x))\). Expanding each image \(\sigma_m(x_r)\) reveals a leading zero followed, when \(x_r<m-1\), by \(x_r+1\). Replacing each letter with its \(\sigma_m^{m-1}\)-image yields, as an identity of one-sided infinite words,
\[
x=P\,(Q_{x_0+1}P)\,(Q_{x_1+1}P)\cdots,
\]
where the parenthetical factor is just \(P\) when the corresponding input letter is \(m-1\). This is exactly \(P B_{x_0}B_{x_1}\cdots\). Each block contains all letters, but none of its *proper prefixes* contains \(m-1\). Therefore it is precisely the next greedy arch, irrespective of its starting position or the preceding arch. Every arch finishes at, and contains exactly one, \(m-1\). This also proves the endpoint and length formulas.

**Step 3: universality index.** The standard arch-factorization theorem says the number of complete greedy arches in a finite word equals its scattered-subsequence universality index over the fixed ambient alphabet. The identity just proved places a one-to-one correspondence between completed arches in any finite prefix and occurrences of \(m-1\) in that prefix: a prefix can terminate midway through the next arch, but that unfinished piece contains no \(m-1\). This proves the formula for \(U_m(N)\), including \(N=0\) and all boundaries.

For \(n\ge m\), use the fact that \(j>0\) has precisely one immediate preimage letter \(j-1\) under \(\sigma_m\). Successively counting \(m-1,m-2,\ldots,1\) in the iterated image yields
\[
\#_{m-1}(\sigma_m^n(0))=\#_0(\sigma_m^{n-m+1}(0)).
\]
Every substituted letter contributes exactly one zero, so the right side equals \(|\sigma_m^{n-m}(0)|=L_{n-m}\). This proves the exact recurrence at substitution lengths.

**Step 4: occurrence and asymptotic frequencies.** The substitution is primitive: \(\sigma_m^m(j)\) contains every alphabet letter for each \(j\), as can be seen by first obtaining a zero then iterating until the full block \(P\) appears. Its nonnegative incidence matrix has Perron eigenvalue \(\lambda_m>1\), where the characteristic polynomial is \(z^m-z^{m-1}-\cdots-1\). If \(f_j\) is the limiting frequency of letter \(j\), then the fact that every substituted letter contributes one zero gives \(\lambda_m f_0=1\), and the unique production of letter \(j>0\) by \(j-1\) gives \(\lambda_m f_j=f_{j-1}\). Therefore \(f_j=\lambda_m^{-(j+1)}\); their sum equals one by the root identity. Each subsequent arch length is the injective image \(2^m-2^{x_r}\), so its limiting frequency is the same \(f_j\), and every type occurs infinitely often. The exact prefix formula and \(f_{m-1}=\lambda_m^{-m}\) establish the asserted asymptotic universality density.

## Verification
The supplied `verify.py` reconstructs the substitution images and their candidate arches independently for \(2\le m\le8\), directly checks the substitution templates, arch completeness, and lengths, then checks 15,000 initial positions for each alphabet size. It compares greedy arch endpoints with the actual rare-letter positions, verifies all encountered successive gap lengths and the self-similar coding, and checks the exact formula at every tested prefix. It independently evaluates the defining scattered-subsequence condition on small prefixes and verifies the substitution-length identity for six successive iterates per alphabet size. Running `python3 verify.py` gives `VERIFY_OK` and a per-parameter count table. These finite tests are corroboration only; Steps 1–4 above establish the infinite statement.

## Relationship to prior work
Schnoebelen and Veron (2023) prove the general greedy-arch characterization and study algorithmic universality for words and compressed words; the passage from complete arches to subsequence universality is credited to that literature. Justin and Vuillon (2000) develop general return-word structure for episturmian words, which includes classical multinacci words and is related to intervals between occurrences of a chosen symbol. Their general return-word methods do not themselves state the particular self-similar greedy-arch identity, the exact all-prefix universality equation, or its coding by the multinacci word; the specific identifications and implications are proved above. Jahannia and coauthors (2021) investigate a different Ziv–Lempel factorization of the same multinacci family. These nearby sources provide genuine context and methods; no claim of exhaustive global novelty is made.

## Limitations
The statement uses the standard multinacci substitution, including its specified starting point and the full alphabet; it is not asserted for arbitrary episturmian substitutions or shifted fixed points. The exact limiting frequencies rely on primitivity and the standard Perron–Frobenius frequency theorem. The computational verifier examines finitely many parameters and prefixes; it cannot independently certify all \(m\). The generic return-word theory is a meaningful prior-coverage risk for the gap-length part, so any priority claim for that subsidiary fact requires further human literature review.

## References
1. P. Schnoebelen and I. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1 (2023), https://arxiv.org/abs/2304.11932.
2. J. Justin and L. Vuillon, *Return words in Sturmian and episturmian words*, RAIRO Theoretical Informatics and Applications 34 (2000), 343–356, https://doi.org/10.1051/ita:2000121.
3. M. Jahannia, M. Mohammad-noori, N. Rampersad, and M. Stipulanti, *Closed Ziv-Lempel factorization of the m-bonacci words*, arXiv:2106.03202v1 (2021), https://arxiv.org/abs/2106.03202.
4. L. Barker, P. Fleischmann, J. Harwardt, F. Manea, and D. Nowotka, *Scattered-factor universality of words*, arXiv:2003.04629v1 (2020), https://arxiv.org/abs/2003.04629.
