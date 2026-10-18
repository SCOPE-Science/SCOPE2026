# Sharp three-adic valuations of Motzkin numbers at ternary predecessor indices

## Finding
For each integer \(r\ge1\), put \(q=3^r\) and let \(M_n\) be the classical Motzkin number. Then
\[
M_{q-3}\equiv 2^{-2(q-1)} C_{q-2}\pmod{3^r}, \qquad \nu_3(M_{3^r-3})=r-1,
\]
where \(C_m=\frac{1}{m+1}\binom{2m}{m}\). The reciprocal is taken in the units modulo \(3^r\). In particular \(\sup_{n\ge0}\nu_3(M_n)=\infty\). This answers the unboundedness half of Rowland and Yassawi's Open Question 3.15.

## Assumptions and scope
\(M_0=1\), and \(M_n\) counts Motzkin paths of length \(n\). We use \(\nu_3\) on nonzero integers, \(\nu_3(0)=+\infty\), and standard Catalan numbers. The theorem covers every positive integer \(r\), including \(r=1\), for which \(M_0=1\). It does not claim that the complete valuation sequence is three-regular.

## Proof
The Motzkin generating function satisfies
\[
F(z)=\sum_{n\ge0}M_nz^n=\frac{1-z-\sqrt{(1-3z)(1+z)}}{2z^2}.
\]
Fix \(r\ge1\), set \(q=3^r\), \(N=q-1\), and extract the coefficient of \(z^{q-3}\):
\[
M_{q-3}=-\frac12\sum_{j=0}^{N}(-3)^j\binom{1/2}{j}\binom{1/2}{N-j}.\tag{1}
\]
Every half-binomial coefficient is three-adically integral, since for \(k\ge1\),
\[
\binom{1/2}{k}=(-1)^{k-1}\frac{C_{k-1}}{2^{2k-1}}.
\]
Consequently all terms of (1) indexed by \(j\ge r\) vanish modulo \(3^r\). The \(j=0\) contribution, using even \(N\), is precisely
\[
-\frac12\binom{1/2}{N}=2^{-2N}C_{N-1}=2^{-2(q-1)}C_{q-2}.\tag{2}
\]

It remains to eliminate \(1\le j<r\). Put \(k=N-j\ge1\), \(m=k-1=q-j-2\), and \(t=\lceil\log_3(j+2)\rceil\). Since \(j+2\le r+1<3^r=q\) whenever \(1\le j<r\), we have \(t<r\). The base-three expansion of \(m=3^r-(j+2)\) has digit \(2\) in each position \(t,t+1,\dots,r-1\). Thus adding \(m\) to itself generates at least \(r-t\) carries. Kummer's theorem and the factorial formula for Catalan numbers give
\[
\nu_3(C_m)=\nu_3\binom{2m}{m}-\nu_3(m+1)
\ge r-t-\nu_3(j+1),\tag{3}
\]
where \(\nu_3(m+1)=\nu_3(q-j-1)=\nu_3(j+1)\), because \(j+1<3^r\).

For \(j=1\), \(t=1\) and \(\nu_3(j+1)=0\), so \(j+\nu_3(C_m)\ge r\). For \(j=2\), necessarily \(r\ge3\): the ternary digits of \(m=q-4\) are \(2,1,2,\ldots,2\) from lowest to highest place, generating exactly \(r\) carries on doubling; as \(\nu_3(m+1)=1\), \(\nu_3(C_m)=r-1\), again sufficient. For \(j=3\), \(t=2\) and \(\nu_3(j+1)=0\), so (3) suffices. For \(j\ge4\), the elementary bounds
\[
\lceil\log_3(j+2)\rceil\le\lfloor j/2\rfloor,\qquad
\nu_3(j+1)\le\lfloor j/2\rfloor
\]
hold: \(3^{\lfloor j/2\rfloor}\ge j+2\) follows from the two initial cases \(j=4,5\) and induction increasing \(j\) by two; the valuation bound follows since \(j+1<3^{\lfloor j/2\rfloor+1}\). Therefore \(t+\nu_3(j+1)\le j\). In every case \(j+\nu_3(C_m)\ge r\). Together with three-adic integrality of the remaining factors in the \(j\)-th term of (1), all \(j\ge1\) contributions vanish modulo \(3^r\), proving the asserted congruence by (2).

Finally \(q-2\) has base-three digits \(1,2,\ldots,2\), from lowest to highest, so adding \(q-2\) to itself produces exactly \(r-1\) carries. Also \(3\nmid q-1\). Kummer's theorem yields
\[
\nu_3(C_{q-2})=r-1.
\]
Since the congruence is modulo \(3^r\), this forces \(\nu_3(M_{q-3})=r-1\). The valuation tends to infinity with \(r\), as claimed. \(\square\)

## Verification
The accompanying standalone `VERIFY.py` computes Motzkin numbers using the exact recurrence and checks the valuation and congruence for \(1\le r\le8\). It also checks the Catalan valuations and supporting carry-bound cases. Running it produces `VERIFY_OK`. These are finite consistency checks; the infinite conclusion rests solely on the proof above.

## Relationship to prior work
Rowland and Yassawi, *Automatic congruences for diagonals of rational functions* (public arXiv version dated 2013-10-31), Open Question 3.15, explicitly ask whether the Motzkin three-adic valuations are unbounded, and whether they are three-regular. Their methods establish congruence schemes, not this explicit family. Straub's congruence-scheme paper discusses Motzkin congruences and several modular properties but does not provide the evaluated valuation on the indices above. Mikić's generalized-Motzkin theorem using a nontrivial parameter excludes the classical specialization in the relevant result. Sun's binomial-sum identities and Kohen's prime-modulus symmetry do not imply an all-exponent three-adic valuation at these indices. An equivalent formula in unindexed literature remains possible.

## Limitations
The theorem addresses only the subsequence at indices \(3^r-3\) and unboundedness. It does not determine valuations at arbitrary indices or prove three-regularity of the valuation sequence. No independent audit has been performed. Novelty is based on inspected relevant literature and the explicitly compared results, not an exhaustive guarantee across all publications.

## References
1. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (public 2013-10-31), Open Question 3.15. https://arxiv.org/abs/1310.8635 ; full text https://ericrowland.github.io/papers/Automatic_congruences_for_diagonals_of_rational_functions.pdf
2. A. Straub, *On congruence schemes for constant terms and their applications*. https://arminstraub.com/downloads/pub/congruenceschemes-ct.pdf
3. M. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623. https://arxiv.org/pdf/2311.14623
4. Z.-W. Sun, *On Motzkin numbers and central trinomial coefficients*, arXiv:1801.08905. https://arxiv.org/pdf/1801.08905
5. I. Kohen, *Density and Symmetry in Generalized Motzkin Numbers Modulo p*. https://math.colgate.edu/~integers/aa22/aa22.pdf
6. OEIS A001006, *Motzkin numbers*. https://oeis.org/A001006
