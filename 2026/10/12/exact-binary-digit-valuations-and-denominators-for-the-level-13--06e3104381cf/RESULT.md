# Exact binary-digit valuations and denominators for a level-13 Apéry-like sequence

## Finding

Consider the integer sequence \(S_n\) introduced via level-13 modular parametrization in Cooper's four-term Apéry-like recurrence. For every integer \(n\ge1\), its exact 2-adic valuation is the number \(s_2(n)\) of one-bits in the binary expansion of \(n\):

\[
\boxed{\nu_2(S_n)=s_2(n).}
\]

The stronger congruence

\[
\boxed{S_n\equiv 2(-1)^{n-1}3^n C_{n-1}\pmod{2^{s_2(n)+2}}}
\]

holds for all such \(n\), where \(C_j=\frac1{j+1}\binom{2j}{j}\) is the Catalan number. Since \(2C_{n-1}\) has exact 2-adic valuation \(s_2(n)\), this determines the odd part of \(S_n\) modulo four. The modulus is genuinely sharp in general: for \(n=2\), the difference between \(S_2=182\) and the displayed Catalan expression \(-18\) equals \(200\), with valuation three.

A consequence concerns the rational coefficients \(T_n=S_n/4^n\) of Cooper's original modular expansion: **the exact 2-primary part of the denominator after reduction** is
\[
\boxed{2^{2n-s_2(n)}}.
\]

Consequently, among the indices \(0\le n<2^m\), precisely \(\binom mk\) have valuation \(k\) (where \(\nu_2(S_0)=0\)). This is a complete valuation distribution, not a finite observation.

## Assumptions and scope

Define \(S_0=1\), \(S_{-1}=S_{-2}=0\), and for every integer \(n\ge0\) let

\[
\begin{aligned}
(n+1)^3S_{n+1}={}&6(2n+1)(3n^2+3n+1)S_n\\
&+4n(148n^2+27)S_{n-1}\\
&+24(6n-5)(6n-1)(2n-1)S_{n-2}.
\end{aligned}
\]

Every resulting \(S_n\) is an integer, as follows also from the proof below. The notation \(\nu_2(a)\) is the exponent of two in a nonzero rational number \(a\). For \(n=0\), the valuation formula holds and the finer Catalan congruence is not asserted. The result treats this specific level-13 four-term sequence, not arbitrary Apéry-type recurrences or primes other than two.

## Proof

**1. Integral square and its first coefficient.** Cooper's modular parametrization (Section 6, equations (6.4) and (6.6), Theorem 6.1) identifies

\[
Z(X)=\sum_{n\ge0}\frac{S_n}{4^n}X^n,
\qquad
F(X)=Z(X)^2=1+3X+25X^2+195X^3+\cdots\in\mathbb Z[[X]].
\]

The integrality is a consequence of his identity \(Z^2=U(q)^2(1+5w(q)+13w(q)^2)\), in which \(U(q)\) and \(w(q)\) are integral series, and of \(X(q)=q+O(q^2)\in\mathbb Z[[q]]\), whose compositional inverse has integer coefficients. This also independently identifies the relevant first coefficient: from the definitions \(U(q)=1-q+O(q^2)\), \(w(q)=q+O(q^2)\), hence \(Z^2=1+3q+O(q^2)=1+3X+O(X^2)\). The cited theorem identifies this same \(Z\) with the four-term recurrence above. The identity \(F(0)=1\) chooses the formal square-root branch \(Z(0)=1\).

**2. A uniform coefficient lemma.** Let \(F(X)=1+I(X)\in\mathbb Z_2[[X]]\) with \(I(X)=aX+bX^2+\cdots\) and odd \(a\). Define \(B_n=4^n[X^n]F(X)^{1/2}\) for \(n\ge1\). The binomial theorem in the formal-series ring yields

\[
B_n=\sum_{k=1}^n4^n\binom{1/2}{k}[X^n]I(X)^k.
\]

Every numerator factor in \(\binom{1/2}{k}=\frac{(1/2)(1/2-1)\cdots(1/2-k+1)}{k!}\) has odd numerator, so Legendre's formula \(\nu_2(k!)=k-s_2(k)\) gives

\[
\nu_2\!\left(4^n\binom{1/2}{k}\right)=2(n-k)+s_2(k).
\]

Binary digit sums are subadditive, and \(s_2(n-k)\le n-k\), hence

\[
s_2(n)\le s_2(k)+s_2(n-k)\le s_2(k)+(n-k).
\]

For \(k<n\), the corresponding summand therefore has 2-adic valuation at least \(s_2(n)+(n-k)>s_2(n)\). For \(k=n\), the coefficient \([X^n]I(X)^n=a^n\) is odd, and its prefactor has valuation exactly \(s_2(n)\). This is the unique summand of lowest valuation, proving \(\nu_2(B_n)=s_2(n)\) for every \(n\ge1\); in particular all \(B_n\) are integers.

**3. Two additional powers of precision.** When \(k\le n-2\), the same bound places the summand in \(2^{s_2(n)+2}\mathbb Z_2\). For \(n\ge2\), the only possible coefficient in the \(k=n-1\) term is

\[
[X^n]I(X)^{n-1}=(n-1)a^{n-2}b.
\]

Its valuation after multiplication by the binomial prefactor is at least \(2+s_2(n-1)+\nu_2(n-1)\). The identity \(s_2(n)=s_2(n-1)+1-\nu_2(n)\) and the fact that one of two consecutive integers is even show this is at least \(s_2(n)+2\). Thus only \(k=n\) remains modulo that power of two, including \(n=1\), when no \(k=n-1\) term exists. The exact identity

\[
4^n\binom{1/2}{n}=2(-1)^{n-1}C_{n-1}
\]

therefore proves the universal congruence

\[
B_n\equiv2(-1)^{n-1}a^n C_{n-1}\pmod{2^{s_2(n)+2}}.
\]

**4. Specialization and consequences.** For Cooper's level-13 series \(a=3\), and by definition \(B_n=S_n\); the first two boxed assertions follow. Because the integer \(S_n\) has exactly \(s_2(n)\) factors of two, reducing \(S_n/4^n\) leaves denominator 2-part exactly \(2^{2n-s_2(n)}\). Finally, binary words of length \(m\) with exactly \(k\) ones are counted by \(\binom mk\), giving the stated distribution including \(n=0\).

## Verification

The standalone, standard-library-only program `verify.py` reconstructs the source recurrence over exact integers, checks its initial terms, independently checks the first seven coefficients of \(Z(X)^2\) by rational arithmetic, and tests both assertions and the Catalan-leading valuation through index 350. Its output is included as `verification_output.txt`. These are finite consistency checks; unrestricted validity is supplied by the coefficient argument, not by extrapolation.

## Relationship to prior work

Cooper (2023, Section 6, Theorem 6.1) established the recurrence, integrality of \(4^nT_n\), and a square-root expansion for its modular parametrization, then left arithmetic properties of this particular level-13 sequence as an open-ended question. Those previously established identities are essential inputs, and their integrality assertion is **not** new. The precise valuation, first nontrivial unit congruence, and exact reduced 2-primary denominator are extracted here by proving the unique minimal-valuation binomial term and controlling the next term. Thus the claim is a relatively short, explicit arithmetic consequence of known modular identities, not a new modular identity or a Lucas/supercongruence theorem.

Gorodetsky's treatment of 15 sporadic Apéry-like sequences studies valuation lower bounds for three-term sporadic families; those families do not include Cooper's later level-13 four-term recurrence. Ulas's 2019 paper investigates 2-adic valuations of **integer** powers of other formal series, rather than this fractional square-root coefficient sequence. Public mathematical-result searches for the sequence parameters, alternate valuation descriptions, and binary-digit terminology did not identify the same exact statement. An equivalent unpublished, unindexed, or implicit prior formulation cannot be ruled out.

## Limitations

The claim concerns only the binary valuation and a modulo-four unit, not higher powers of two, odd primes, or other four-term sequences. It depends on Cooper's published modular-series identity and recurrence identification. Its principal originality risk is that the valuation lemma is elementary and the answer can be derived from his displayed square-root formula; whether such a derivation has been circulated elsewhere is not determined by searchable records. Finite verification cannot certify those bibliographic facts or replace the proof.

## References

1. S. Cooper, *Apéry-like sequences defined by four-term recurrence relations*, arXiv:2302.00757v1 (public 2023-02-01), Section 6 and Theorem 6.1; https://arxiv.org/html/2302.00757v2.
2. O. Gorodetsky, *New representations for all sporadic Apéry-like sequences, with applications to congruences*, arXiv:2102.11839v1 (2021), Section 2.3; https://arxiv.org/html/2102.11839v2.
3. M. Ulas, *2-Adic valuations of coefficients of certain integer powers of formal power series*, International Journal of Number Theory 15 (2019), 723–762, DOI 10.1142/S1793042119500386.
