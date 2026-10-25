# Exact dyadic periods and sharp translation valuations for central Delannoy numbers

## Finding

Let \(D_n\) be the central Delannoy number
\[
D_n=\sum_{k=0}^{n}2^k\binom nk^2\qquad(n\ge0).
\]
For an integer \(m\ge1\), set \(s=\nu_2(m)\) and
\[
\eta(m)=\min_{n\ge0}\nu_2(D_{n+m}-D_n),
\]
where \(\nu_2(0)=+\infty\). Then
\[
\boxed{\eta(m)=
\begin{cases}
1,&s=0,\\
2,&s=1,\\
s+2,&s\ge2.
\end{cases}}
\]
The minimum is **always attained at the common witness \(n=1\)**:
\[
\nu_2(D_{m+1}-D_1)=\eta(m),\qquad D_1=3.
\]
Consequently the least global period \(P_h\) of the sequence \((D_n\bmod 2^h)_{n\ge0}\) is
\[
\boxed{P_h=
\begin{cases}
1,&h=1,\\
2,&h=2,\\
4,&h=3\text{ or }4,\\
2^{h-2},&h\ge5.
\end{cases}}
\]
One consequence relates to a published conjecture on dyadic Delannoy differences: for **every odd positive integer \(a\)** and **every \(s\ge2\)**,
\[
\boxed{\nu_2(D_{a2^{s+1}+1}-D_{a2^s+1})=s+2.}
\]
This proves the offset \(b=1\) case of Lengyel's Conjecture 4, within its stated sufficiently-large-index regime.

## Assumptions and scope

All Delannoy indices are nonnegative integers, every shift \(m\) is a positive integer, and each modulus is \(2^h\) with \(h\ge1\). The valuation of zero is taken as infinity; thus the minimum is an extended-integer minimum, made finite by the explicitly supplied witness. A global period \(P\) means \(D_{n+P}\equiv D_n\pmod{2^h}\) for **all** \(n\ge0\), rather than eventual periodicity or a period for one initial value. The central Delannoy numbers also equal \(P_n(3)\), with \(P_n\) the Legendre polynomial. The result is a statement about the fixed prime \(2\); no claim is made for arbitrary moduli.

## Proof

**1. Base residues.** The summand with \(k=0\) is \(1\), so every \(D_n\) is odd. Modulo \(4\), only \(k=0,1\) contribute, giving
\[
D_n\equiv1+2n^2\equiv1+2n\pmod4.
\]
Hence odd translations have uniform difference divisible by \(2\), and translations with even shift have uniform difference divisible by \(4\).

**2. Dyadic translation lemma.** For every \(s\ge2\) and \(n\ge0\), put \(M=2^s\). We claim
\[
D_{n+M}\equiv D_n\pmod{2^{s+2}}.\tag{1}
\]
Write \(B_k=\binom nk\) and \(\Delta_k=\binom{n+M}k-\binom nk\), interpreting binomial coefficients with \(k>n\) as zero. The difference is
\[
D_{n+M}-D_n
=\sum_{k\ge1}2^k(2B_k\Delta_k+\Delta_k^2),\tag{2}
\]
a finite sum (both binomial sequences vanish for sufficiently large \(k\)). Terms with \(k\ge s+2\) are zero modulo \(2^{s+2}\). If \(1\le k\le s+1\), then \(k<M\), and Vandermonde gives
\[
\Delta_k=\sum_{j=1}^{k}\binom Mj\binom n{k-j}.
\]
For \(1\le j<M\), the integer \(\binom{M-1}{j-1}\) is odd (the binary digits of \(M-1\) are all ones, by Lucas' theorem), and the identity \(j\binom Mj=M\binom{M-1}{j-1}\) yields
\[
\nu_2\!\binom Mj=s-\nu_2(j).
\]
Putting \(r=\lfloor\log_2k\rfloor\), we obtain \(2^{s-r}\mid\Delta_k\). Since \(k\ge r+1\) and \(k\ge2r\) for every positive integer \(k\),
\[
\nu_2\bigl(2^{k+1}B_k\Delta_k\bigr)\ge k+1+s-r\ge s+2
\]
and
\[
\nu_2\bigl(2^k\Delta_k^2\bigr)\ge k+2s-2r\ge2s\ge s+2.
\]
Therefore (2) proves (1), uniformly in \(n\).

**3. A sharp universal witness.** We prove for every \(s\ge2\) that
\[
D_{2^s+1}-3\equiv2^{s+2}\pmod{2^{s+3}}.\tag{3}
\]
For \(s=2\), direct evaluation gives \(D_5=1683\), so \(D_5-3=1680\equiv16\pmod{32}\). For \(s\ge3\), set \(M=2^s\). In the defining sum for \(D_{M+1}\), the \(k=1\) term differs from the corresponding term in \(D_1\) by
\[
2((M+1)^2-1)=4M+2M^2\equiv4M\pmod{2^{s+3}}.
\]
For \(k=2\), \(\nu_2\binom{M+1}{2}=s-1\), so the \(k=2\) summand has valuation \(2s\ge s+3\). For \(3\le k\le M\), the identities
\[
\binom{M+1}k=\frac{M+1}{k}\binom M{k-1},\qquad
\nu_2\binom M{k-1}=s-\nu_2(k-1)
\]
give
\[
\nu_2\binom{M+1}k=s-\nu_2(k(k-1)).
\]
Exactly one of \(k,k-1\) is even, so \(\nu_2(k(k-1))\le\lfloor\log_2k\rfloor\); since \(k\ge2\lfloor\log_2k\rfloor\) for \(k\ge3\),
\[
\nu_2\!\left(2^k\binom{M+1}k^2\right)
\ge k+2s-2\lfloor\log_2k\rfloor\ge2s\ge s+3.
\]
The final \(k=M+1\) summand is \(2^{M+1}\), also divisible by \(2^{s+3}\). Summing proves (3). In particular
\(\nu_2(D_{2^s+1}-3)=s+2\).

For any odd positive \(u\), the shift \((u-1)2^s\) is divisible by \(2^{s+1}\). Applying (1) with \(s+1\) repeatedly shows
\[
D_{u2^s+1}\equiv D_{2^s+1}\pmod{2^{s+3}}.
\]
Together with (3), this gives \(\nu_2(D_{u2^s+1}-3)=s+2\). Repeating (1) with shift \(2^s\) gives the matching lower bound for every starting index \(n\). Hence \(\eta(m)=s+2\) whenever \(s\ge2\).

For odd \(m\), the base residues imply \(D_{m+1}-D_1\equiv1-3\equiv2\pmod4\), so \(\eta(m)=1\). If \(m\equiv2\pmod4\), (1) with \(s=2\) implies period \(4\) modulo \(8\), and \(D_3-D_1=60\equiv4\pmod8\). Thus \(D_{m+1}-D_1\equiv4\pmod8\), and the base residue bound gives \(\eta(m)=2\).

**4. Exact minimal periods.** All terms are odd, so the period modulo \(2\) is \(1\); the base formula gives least period \(2\) modulo \(4\). Equation (1) with \(s=2\) provides period \(4\) modulo both \(8\) and \(16\). A shorter period must divide \(4\), but \(D_2-D_0=12\not\equiv0\pmod8\), excluding the candidate period \(2\). Thus \(P_3=P_4=4\). For \(h\ge5\), (1) with \(s=h-2\) provides period \(2^{h-2}\) modulo \(2^h\). But the half-period \(2^{h-3}\) fails at \(n=1\), since its difference has valuation \(h-1\), strictly below \(h\). The least period of any everywhere-periodic one-sided sequence divides every period (by the Euclidean algorithm on periods). The only possible proper periods dividing a power of \(2\) divide its half, so none survives. Hence \(P_h=2^{h-2}\).

**5. One offset in a difference conjecture.** Let \(a\) be odd and \(s\ge2\). Uniform congruence (1) with exponent \(s+1\) gives
\[
D_{a2^{s+1}+1}\equiv D_1\pmod{2^{s+3}}.
\]
Also \(a-1\) is even, so the same congruence gives
\[
D_{a2^s+1}\equiv D_{2^s+1}\pmod{2^{s+3}}.
\]
Their difference is congruent to \(3-D_{2^s+1}\equiv-2^{s+2}\pmod{2^{s+3}}\), by (3). Its valuation is therefore exactly \(s+2\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) computes central Delannoy numbers exactly from the standard three-term recurrence, checks thousands of translations and sharp common witnesses, verifies the candidate least periods over a finite prefix for moduli through \(2^{10}\), and checks the offset-\(1\) difference. It is executable as \(\texttt{python3 verify.py}\) using the Python standard library. These finite tests are consistency checks, not the reason the infinite congruences hold; the latter are proved by the binomial valuation arguments above.

## Relationship to prior work

Sun's 2010 preprint (later published in 2011) develops congruences for central Delannoy numbers, primarily for odd-prime weighted sums; it supplies an archive-eligible source and the arithmetic setting but no global dyadic-period classification. Noe's 2006 paper places the same sequence among generalized central trinomial coefficients and establishes digitwise divisibility criteria, not the claimed prime-power translation moduli. Lengyel (2021), Theorem 3, proves large valuations of \(D_{a2^s}-1\); Theorem 4 treats certain shifted values, while Conjecture 4 explicitly predicts \(\nu_2(D_{a2^{s+1}+b}-D_{a2^s+b})\). The present result proves its \(b=1\) case and, independently, the exact global periods. It does not prove Lengyel's conjecture for arbitrary offsets. Djadi and Belbachir (2026) study generalized triangle congruences and odd-prime Wolstenholme analogues; their stated results do not supply the dyadic translation law here.

## Limitations

The period formula is only for powers of \(2\) and is global in the nonnegative index. Only offset \(1\) of Lengyel's broader difference conjecture is proved. The supplied exact arithmetic checks cover only finitely many indices and moduli; all unbounded assertions require the preceding proof. Novelty against unknown or unindexed mathematical literature cannot be guaranteed.

## References

1. Zhi-Wei Sun, *On Delannoy numbers and Schröder numbers*, first publicly submitted 13 September 2010, arXiv:1009.2486v1; *Journal of Number Theory* 131 (2011), 2387–2397. https://arxiv.org/abs/1009.2486
2. Tony D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, *Journal of Integer Sequences* 9 (2006), article 06.2.7, published 5 July 2006. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf
3. Tamás Lengyel, *On Some p-Adic Properties and Supercongruences of Delannoy and Schröder Numbers*, *INTEGERS* 21 (2021), A86, especially Theorem 3, Theorem 4 and Conjecture 4. https://math.colgate.edu/~integers/v86/v86.pdf
4. Chahinaze Djadi and Hacène Belbachir, *Congruence Properties for the Delannoy Triangle Coefficients*, *Journal of Integer Sequences* 29 (2026), article 26.5.2. https://cs.uwaterloo.ca/journals/JIS/VOL29/Djadi/djadi6.pdf
