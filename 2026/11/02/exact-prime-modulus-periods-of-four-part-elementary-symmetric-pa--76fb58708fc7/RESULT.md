# Exact prime-modulus periods of four-part elementary-symmetric partition sums

## Finding

Let \(\mathcal P_4(n)\) consist of partitions of \(n\) into exactly four positive parts, and define
\[
a(n)=\sum_{\lambda\in\mathcal P_4(n)} e_2(\lambda),\qquad
 e_2(\lambda)=\sum_{1\le i<j\le4}\lambda_i\lambda_j.
\]
For every prime \(p\ge5\), the sequence \(a(n)\bmod p\) is **purely periodic**, starting at \(n=0\), and its **least positive period** is
\[
\pi_p=\begin{cases}300,&p=5,\\12p,&p\ge7.\end{cases}
\]
This includes every prime-modulus entry in the conjectural period table of Ballantine, Beck and Merca, and establishes the whole uniform prime family.

## Assumptions and scope

All partitions are unordered with positive integer parts, repetitions allowed; the empty set \(\mathcal P_4(n)\) gives \(a(n)=0\) for \(0\le n<4\). Here \(p\) is any ordinary rational prime at least five and \(n\) any nonnegative integer. "Least" means the minimum positive integer \(T\) such that \(a(n+T)\equiv a(n)\pmod p\) for **every** \(n\ge0\), not just eventually.

## Proof

Put \(q\) for a formal indeterminate. Every partition into four parts can be written uniquely as
\[
(a,a+u,a+u+v,a+u+v+w),\qquad a\ge1,\ u,v,w\ge0,
\]
with weight \(4a+3u+2v+w\). Direct expansion gives
\[
e_2=6a^2+9au+6av+3aw+3u^2+4uv+2uw+v^2+vw.
\]
For \(m\in\{1,2,3,4\}\), the geometric series \(G_m(z)=1/(1-q^m z)\) satisfies
\[
\left.(z\partial_z)^jG_m(z)\right|_{z=1}
=\sum_{t\ge0}t^jq^{mt},\qquad j=0,1,2.
\]
For the positive variable \(a\), instead use \(H_4(z)=q^4z/(1-q^4z)\), with the analogous sum over \(a\ge1\). Applying the nine displayed quadratic terms as differential operators to \(H_4(z_a)G_3(z_u)G_2(z_v)G_1(z_w)\), then setting all auxiliary variables to one and simplifying rationally, gives the **exact identity in \(\mathbb Z[[q]]\)**
\[
\sum_{n\ge0}a(n)q^n=\frac{N(q)}{D(q)},
\]
where
\[
\begin{split}
N(q)=q^4(&11q^{12}+25q^{11}+50q^{10}+72q^9+106q^8+126q^7\\
&+146q^6+121q^5+95q^4+57q^3+34q^2+15q+6),\\
D(q)&=(1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3.
\end{split}
\]
The displayed identity is also independently checked by symbolic polynomial reduction in `verify_prime_periods.py`. Notice that \(D(0)=1\), \(\deg N=16\), and \(\deg D=22\).

Crucially, the four exact integer resultants of \(N\) with \(q-1\), \(q+1\), \(q^2+1\), and \(q^2+q+1\), respectively, are
\[
864,\quad32,\quad144,\quad36.
\]
Each has prime factors only two and three. It follows that **for every prime \(p\ge5\)**, \(N\) and \(D\) are relatively prime in \(\mathbb F_p[q]\). Thus no cyclotomic denominator factor disappears modulo an eligible prime.

A positive integer \(T\) is a pure period of the coefficient sequence modulo \(p\) if and only if \((1-q^T)N(q)/D(q)\) is a polynomial of degree less than \(T\) over \(\mathbb F_p\): this is exactly the coefficientwise identity \(a(n+T)=a(n)\), including the initial terms. Coprimality forces \(D\mid 1-q^T\). Conversely, whenever \(D\mid1-q^T\), the product is a polynomial of degree \(T+16-22=T-6<T\), so \(T\) is indeed a pure period.

Write \(T=p^su\) with \(p\nmid u\). In characteristic \(p\), \(1-q^T=(1-q^u)^{p^s}\). The factor \(1-q^u\) is separable, and the irreducible-root orders represented by the four factors of \(D\) are exactly \(1,2,4,3\). Because \(p\ge5\), all occur as roots of \(1-q^u\) precisely when \(12\mid u\). Their multiplicities in \(1-q^T\) are \(p^s\); the largest multiplicity required by \(D\) is six. Hence
\[
D\mid1-q^T\quad\Longleftrightarrow\quad12\mid u\ \text{and}\ p^s\ge6.
\]
When \(p=5\), this first holds for \(s=2\), giving least period \(12\cdot25=300\). When \(p\ge7\), it first holds for \(s=1\), giving least period \(12p\). This proves the theorem for every \(n\ge0\) and every prime \(p\ge5\).

## Verification

Run `python3 verify_prime_periods.py` with Python 3 and SymPy installed. The script independently reconstructs the formal generating function from the partition parametrization and differentiations, checks the exact rational identity and all four resultants, compares coefficients against a separate direct enumeration of partitions for 68 sizes, and tests the predicted periods plus proper divisors for eight primes. The proof for all primes is the algebraic argument above, not extrapolation from the finite checks.

## Relationship to prior work

Ballantine, Beck and Merca (first posted 23 August 2024) introduce \(e_2p_4(n)\), conjecture its order-22 recurrence, and tabulate **conjectural** minimum periods including \(300\) for modulus five and \(12p\) for listed primes \(p\ge7\). Their proved congruences cover moduli two, three, and four (Theorem 2); their argument does not claim the prime family proved here. Nijenhuis–Wilf and Kwong concern **unweighted counts** of partitions into a prescribed number of parts: their exact periods for \(p_4(n)\) do not directly give those of the \(e_2\)-weighted sequence. The related paper *Elementary symmetric partitions* (arXiv:2409.11268) studies a different partition map and the sizes of image parts.

## Limitations

The theorem is restricted to prime moduli at least five and does not determine least periods modulo composite moduli, two, or three. The literature comparison supports novelty among inspected sources but cannot exclude an unindexed equivalent computation or subsequent unpublished proof; no independent scientific audit has been performed. The explicit numerator is necessary for the no-cancellation argument, so a denominator-only heuristic would not suffice.

## References

1. C. Ballantine, G. Beck and M. Merca, *Partitions and elementary symmetric polynomials: an experimental approach*, arXiv:2408.13346v1 (2024), https://arxiv.org/pdf/2408.13346 ; *Ramanujan Journal* 66, article 34 (2025), https://doi.org/10.1007/s11139-024-01001-6 .
2. A. Nijenhuis and H. S. Wilf, *Periodicities of partition functions and Stirling numbers modulo p*, *Journal of Number Theory* 25 (1987), 308–312 (cited in reference 1).
3. Y. H. H. Kwong, *Minimum periods of partition functions modulo M*, *Utilitas Mathematica* 35 (1989), 3–8 (cited in reference 1).
4. C. Ballantine, G. Beck, M. Merca and B. Sagan, *Elementary symmetric partitions*, arXiv:2409.11268v1 (2024), https://arxiv.org/abs/2409.11268 .
