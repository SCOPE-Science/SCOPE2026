# Squarefree prime-product factorial quotients through \(2^{16384}\)

## Finding

Define, for every integer \(n\geq 0\),
\[
Q_n=\frac{1}{(n+1)!}\prod_{p\leq n+1\atop p\text{ prime}}p^{\lfloor n/(p-1)\rfloor}.
\]
The integer sequence \((Q_n)\) is OEIS A363596, obtained by dividing the prime product of Bedhouche and Farhi by \((n+1)!\). An integer is *squarefree* if no square of a prime divides it; in particular, \(1\) is squarefree.

**Finite-range classification.** For all integers \(n\) with \(0\leq n<2^{16384}\), the number \(Q_n\) is squarefree if and only if \(n\) belongs to the following explicit set of \(35\) indices:
\[
\begin{aligned}
\mathcal T=\{&0,1,2,3,4,5,7,8,9,11,15,17,19,23,31,32,33,35,39,47,\\
&63,65,71,95,135,143,191,255,257,263,287,515,575,767,1055\}.
\end{aligned}
\]
In particular, the entry at index \(1055\) is the last squarefree entry **within this verified range**. No claim is made that it is the last squarefree entry for all \(n\geq0\).

## Assumptions and scope

The product runs over ordinary rational primes, including \(2\), with no terms when \(n=0\). The parameter \(16384\) is the exact exponent of the finite cutoff, so the statement covers every integer index below \(2^{16384}\), not merely a random sample or all indices representable in machine precision.

For an integer \(m\geq1\), write \(s_b(m)\) for its ordinary base-\(b\) digit sum and \(\nu_p(m)\) for its prime-adic valuation. The proof uses only integer arithmetic, Legendre's factorial valuation formula, a finite digit filter, and finite certified divisibility checks.

## Proof

**1. Valuations and integrality.** By the prime product definition and Legendre's formula, for each prime \(p\) and \(n\geq0\),
\[
\nu_p(Q_n)=\left\lfloor\frac n{p-1}\right\rfloor-\sum_{j\geq1}\left\lfloor\frac{n+1}{p^j}\right\rfloor.
\tag{1}
\]
Equivalently, with \(m=n+1\),
\[
\nu_p(Q_n)=\left\lfloor\frac{m-1}{p-1}\right\rfloor-\frac{m-s_p(m)}{p-1}\geq0,
\]
because \(s_p(m)\geq1\) for \(m\geq1\) and the second summand is an integer. Thus \(Q_n\) is a positive integer. Specializing to \(p=2,3\) gives the exact formulas
\[
\nu_2(Q_n)=s_2(m)-1,
\qquad
\nu_3(Q_n)=
\begin{cases}
(s_3(m)-1)/2,&m\text{ odd},\\
(s_3(m)-2)/2,&m\text{ even}.
\end{cases}
\tag{2}
\]
Consequently, squarefreeness forces \(s_2(m)\leq2\) and \(s_3(m)\leq3\) for odd \(m\), or \(s_3(m)\leq4\) for even \(m\).

**2. Exhaustive candidate reduction.** Each positive integer with \(s_2(m)\leq2\) has exactly one form \(m=2^a\) or \(m=2^a+2^b\) with \(a>b\geq0\). Since \(n<2^{16384}\), one needs only exponents \(0\leq a\leq16384\), retaining \(m\leq2^{16384}\). No other indices can be squarefree by equation (2).

For any nonnegative integer \(m\),
\[
s_3(m\bmod3^{24})\leq s_3(m).
\tag{3}
\]
The included program computes the \(3^{24}\)-residues of the powers of two, using a complete lookup of ternary digit sums for each of the two blocks of length \(12\). It discards a candidate only when the low \(24\) digits already exceed the necessary bound \(4\), then independently computes the *full* ternary sum of every survivor against its parity-specific bound. Inequality (3) proves this filter has no false negatives. Exhausting all powers and pairs leaves exactly \(42\) candidate indices, all at most \(65663\).

**3. Exact square-divisor resolution.** For each of the \(42\) candidates, equation (1) is evaluated for every prime \(p\leq n+1\) using a complete integer sieve of primes through \(65664\). Prime factors greater than \(n+1\) have valuation zero directly from equation (1). Exactly seven candidates have square-divisor witnesses:
\[
\begin{array}{c|ccccccc}
n&271&512&513&1025&2303&32831&65663\\\hline
p\text{ with }p^2\mid Q_n&7&5&5&7&5&5&5
\end{array}
\]
Every other candidate has \(\nu_p(Q_n)\leq1\) for all primes, hence is squarefree. These are precisely the \(35\) indices in \(\mathcal T\). This completes the finite classification.

## Verification

Run `python3 verify.py` using standard Python 3. The program rederives equation (1) against directly constructed prime products for the first \(80\) indices, checks that candidate enumeration agrees with direct exhaustive inspection of every index below \(2^{12}\), enumerates all binary one-/two-digit patterns through exponent \(16384\), and checks full factorial valuations for every final candidate. Its deterministic assertions require exactly \(42\) candidates, the seven displayed obstructions, and the \(35\)-element set \(\mathcal T\). All assertions passed in the recorded test run. Verification does not use probable primes, sampling, floating-point comparisons, network access, or outside data files.

The mathematical soundness of the finite result depends on the exhaustive parameter reduction and the necessary-character of the low-digit sieve; it is not inferred from a small sample. The standalone checker is supplied so its finite steps can be independently replayed.

## Relationship to prior work

Bedhouche and Farhi introduced the relevant prime product, proved factorial divisibility, and provided factorial valuation identities. OEIS A363596 records the quotient and reports \(1055\) as the largest squarefree index seen in its investigation of indices through \(20737\), while explicitly leaving open the possibility of later examples. Neither source establishes the stated enormous finite cutoff and exact complete index set for that cutoff.

A separate classical theorem of Senge and Straus (1973) proves that \(s_2(m)+s_3(m)\) tends to infinity. Coupled with equation (2), this **already implies** that \(Q_n\) has only finitely many squarefree terms globally. That qualitative finiteness is thus **not claimed as an original discovery**. It does not provide the explicit index-by-index classification up to \(2^{16384}\) obtained here; this finite census is the new claim.

## Limitations

The exhaustive classification is strictly finite: it does not rule out squarefree terms at indices \(n\geq2^{16384}\). The Senge--Straus theorem separately implies global finiteness but does not identify the final squarefree index. The computational steps are exact integer arithmetic but remain an executable finite certificate rather than a formal proof-assistant derivation.

## References

1. A. Bedhouche and B. Farhi, *On Some Products Taken over Prime Numbers*, arXiv:2207.07957v1 (public July 16, 2022); *Journal of Integer Sequences* 26 (2023), Article 23.1.5. https://arxiv.org/abs/2207.07957 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Farhi/farhi32.pdf
2. OEIS Foundation, A363596, *Prime-product factorial quotient*, https://oeis.org/A363596 (original entry August 3, 2023).
3. H. G. Senge and E. G. Straus, *PV-numbers and sets of multiplicity*, *Periodica Mathematica Hungarica* 3 (1973), 93--100, https://doi.org/10.1007/BF02018464 .
4. C. L. Stewart, *On the representation of an integer in two different bases*, *Journal für die reine und angewandte Mathematik* 319 (1980), 63--72, https://doi.org/10.1515/crll.1980.319.63 .
5. OEIS Foundation, A096288, *Sum of digits in bases 2 and 3*, https://oeis.org/A096288 (statement of the Senge--Straus theorem).
