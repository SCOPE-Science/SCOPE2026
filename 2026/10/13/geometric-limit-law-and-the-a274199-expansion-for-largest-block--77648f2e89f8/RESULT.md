# Geometric limit law and the A274199 expansion for largest block-palindrome width
## Finding
Fix an integer \(q\ge2\). Let \(W_n\) be uniformly distributed on the \(q\)-letter words of length \(n\). In the largest block-palindrome factorization of \(W_n\), let \(M_n\) be the number of matched noncentral block pairs and let \(L_n\) be the width.

Let \(u_m(q)\) denote the number of unbordered \(q\)-ary words of length \(m\), and put
\[
s_q=\sum_{m\ge1}\frac{u_m(q)}{q^{2m}}.
\]
Then \(0<s_q<1\), and for every integer \(r\ge0\),
\[
\lim_{n\to\infty}\Pr(M_n=r)=(1-s_q)s_q^r.
\]
Thus the limiting matched-pair count is geometric. Equivalently,
\[
\lim_{n\to\infty}\Pr(L_n=2r+1)=(1-s_q)s_q^r,
\qquad
\lim_{n\to\infty}\Pr(L_n\text{ is even})=0.
\]

Consequently the limiting expected width is
\[
E_q=\lim_{n\to\infty}\mathbb E[L_n]
=\frac{1+s_q}{1-s_q}.
\]

If \(b_d\) denotes A274199 with its natural offset \(b_0=1\), then
\[
E_q
=
1+2\sum_{d\ge1} b_d q^{-d}.
\]
Hence Conjecture 5 of Gabrić and Shallit is true.

## Assumptions and scope
A border of a nonempty word is a nonempty proper prefix that is also a suffix. An unbordered word has no border. A largest block-palindrome factorization is obtained by repeatedly removing the shortest border from both ends until the remaining central word is unbordered or empty.

The source recurrence for unbordered words is
\[
u_0(q)=1,
\]
and, for \(m\ge1\),
\[
u_m(q)=
\begin{cases}
q\,u_{m-1}(q),&m\text{ odd},\\
q\,u_{m-1}(q)-u_{m/2}(q),&m\text{ even}.
\end{cases}
\]

The result concerns the uniform distribution on all \(q^n\) words of each length. It gives the full limiting width distribution and its mean. It does not give a finite-\(n\) closed form for every width probability.

## Proof
A shortest border is necessarily unbordered. Conversely, if \(v\) is unbordered and a word has the form
\[
v\,z\,v,
\]
then no border shorter than \(v\) can occur, because such a border would be a border of \(v\). Therefore \(v\) is the shortest border.

It follows that for every \(m\ge1\), the number of length-\(n\) words whose shortest border has length \(m\) is
\[
u_m(q)\,q^{n-2m}
\]
whenever \(2m\le n\). In particular,
\[
q^n-u_n(q)
=
\sum_{1\le m\le n/2}
u_m(q)\,q^{n-2m}.
\]

Now fix \(r\ge1\). The first \(r\) matched block pairs in a largest factorization have uniquely determined positive lengths \(m_1,\ldots,m_r\). Conversely, choosing an unbordered word independently at each of these lengths and then an arbitrary central word produces exactly such an \(r\)-layer prefix of the greedy factorization. Hence
\[
\Pr(M_n\ge r)
=
\sum_{\substack{m_1,\ldots,m_r\ge1\\
2(m_1+\cdots+m_r)\le n}}
\prod_{j=1}^r\frac{u_{m_j}(q)}{q^{2m_j}}.
\]
The terms are nonnegative. Letting \(n\to\infty\) gives
\[
\lim_{n\to\infty}\Pr(M_n\ge r)=s_q^r.
\]
A crude bound already gives \(s_q<1\): using \(u_m(q)\le q^m\), the first two exact terms, and the remaining geometric tail,
\[
s_q
\le
\frac1q+\frac{q-1}{q^3}+\frac{1}{q^2(q-1)}
<1
\qquad(q\ge2).
\]
Therefore
\[
\Pr(M_n=r)\longrightarrow s_q^r-s_q^{r+1}
=(1-s_q)s_q^r.
\]

The central block is empty only when the paired block lengths sum to \(n/2\). If \(e_N\) is the probability of an empty center at length \(2N\), then
\[
\sum_{N\ge1}e_N
=
\sum_{r\ge1}s_q^r
=
\frac{s_q}{1-s_q}<\infty.
\]
Thus \(e_N\to0\). Since
\[
L_n=1+2M_n-\mathbf 1_{\{\text{empty center}\}},
\]
the claimed limiting width distribution follows. Also
\[
\mathbb E[M_n]
=
\sum_{r\ge1}\Pr(M_n\ge r)
\longrightarrow
\sum_{r\ge1}s_q^r
=
\frac{s_q}{1-s_q},
\]
where the domination \(\Pr(M_n\ge r)\le s_q^r\) justifies passage through the sum. Hence
\[
E_q
=
1+\frac{2s_q}{1-s_q}
=
\frac{1+s_q}{1-s_q}.
\]

It remains to identify the power-series coefficients. Put \(x=q^{-1}\) and define, as formal power series,
\[
a_m(x)=x^{2m}u_m(x^{-1}),
\qquad
S(x)=\sum_{m\ge1}a_m(x).
\]
Every bordered length-\(m\) word has a unique shortest border, so the preceding shortest-border count gives the triangular identity
\[
a_m(x)
=
x^m\left(
1-\sum_{1\le j\le m/2}a_j(x)
\right).
\]

Let \(C_d\) be the number of compositions
\[
(c_1,\ldots,c_t)
\]
of \(d\) satisfying
\[
c_i<2c_{i+1}
\]
for every adjacent pair, and let
\[
B(x)=\sum_{d\ge1}C_d x^d.
\]
For \(m\ge1\), let \(F_m(x)\) count such compositions whose first part is \(m\). Then
\[
F_m(x)
=
x^m\left(
1+\sum_{j>m/2}F_j(x)
\right).
\]
Writing
\[
H_m(x)=\frac{F_m(x)}{1+B(x)}
\]
gives
\[
H_m(x)
=
x^m\left(
1-\sum_{1\le j\le m/2}H_j(x)
\right).
\]
This is the same triangular recursion as for \(a_m(x)\), so \(H_m(x)=a_m(x)\) for every \(m\). Summing over \(m\) yields
\[
\frac{B(x)}{1+B(x)}=S(x),
\qquad
B(x)=\frac{S(x)}{1-S(x)}.
\]
Therefore
\[
E_q=1+2B(q^{-1})
=
1+2\sum_{d\ge1}C_d q^{-d}.
\]

Finally, the defining triangular array \(g(N,K)\) for A274199 satisfies
\[
g(N,0)=1,\qquad
g(N,K)=g(N-1,K-1)+g(N-1,2K).
\]
Let \(C(d,m)\) count the same admissible compositions of \(d\), but with last part at most \(m\), with the empty composition counted when \(d=0\). Splitting according to whether the last part is at most \(K\) or exactly \(K+1\) gives
\[
C(d,K+1)
=
C(d,K)+C(d-K-1,2K+1).
\]
Consequently, by induction,
\[
g(N,K)=C(N-K,K+1).
\]
For fixed \(d=N-K\), once \(N\ge2d-1\), the bound \(K+1\ge d\) is vacuous, so the reverse row stabilizes at
\[
C_d.
\]
Thus \(C_d\) is exactly A274199 at index \(d\). This proves the conjectured expansion.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently checks the unbordered-word recurrence by exhaustive word enumeration for binary and ternary alphabets at small lengths. It checks the shortest-border counting identity for several alphabet sizes and forty lengths.

It then brute-forces the exact finite identity for the tail probability \(\Pr(M_n\ge r)\) for binary and ternary words through length \(8\), independently computes the A274190 triangular array, enumerates the constrained compositions defining the coefficient proof, and confirms their equality through index \(16\).

Finally it constructs the formal series through degree \(16\) and checks that the coefficients are
\[
1,2,3,5,8,12,19,29,44,67,101,152,228,342,511,763
\]
after the initial offset, and numerically reproduces the published limiting-width table for \(2\le q\le10\).

These computations validate finite instances and the algebraic bookkeeping. The infinite geometric law and coefficient identity follow from the proofs above, not from extrapolation.

## Relationship to prior work
Gabrić's 2022 thesis proves that the expected width has a finite limit and tabulates numerical values. The 2023 paper with Shallit repeats that theorem and explicitly conjectures that the limiting mean has the A274199 expansion. Neither source gives the geometric limiting distribution or a proof of the coefficient identity.

Goto, I, Bannai, and Inenaga establish the structural fact that the largest block palindrome is unique and is obtained by greedily peeling shortest borders. That result supplies the factorization mechanism but does not study the random-word limiting law.

OEIS A330886 records the binary total shortest-border-factorization length and the numerical asymptotic constant \(6.468626906\ldots\). It does not give the all-alphabet formula, the geometric limiting distribution, or the A274199 proof.

OEIS A274199 defines the coefficient sequence through a limiting reverse row and records the constrained-composition interpretation as an observation. The proof above derives that composition model and connects it to the unbordered-word renewal law, thereby proving the expansion conjectured in the 2023 paper.

## Limitations
The theorem concerns uniform random words over a fixed finite alphabet. It does not treat nonuniform letter distributions.

The limiting distribution is explicit through \(s_q\), but no simpler elementary closed form for \(s_q\) is claimed.

The finite-\(n\) distribution remains governed by truncated renewal sums or the published exact recurrence; no new finite-\(n\) closed form is claimed.

## References
1. D. Gabrić, *On the Properties and Structure of Bordered Words and Generalizations*, Ph.D. thesis, University of Waterloo, public repository date 2022-10-12, handle 10012/18874.
2. D. Gabrić and J. Shallit, “Smallest and Largest Block Palindrome Factorizations,” arXiv:2302.13147v1, first public 2023-02-25; WORDS 2023, DOI 10.1007/978-3-031-33180-0_14.
3. K. Goto, T. I, H. Bannai, and S. Inenaga, “Block Palindromes: A New Generalization of Palindromes,” arXiv:1806.00198v1, 2018.
4. OEIS A274199, “Limiting reverse row of the array A274190.”
5. OEIS A330886, “Sum of lengths of SB (shortest border) factorizations over all binary strings of length \(n\).”
