# The exact radical-discriminant Dold multiplier for Lucas even-power subsequences

## Finding

Let \(P,Q\in\mathbb Z\), and define the Lucas sequence of the first kind by
\[
U_0=0,\qquad U_1=1,\qquad U_{j+2}=PU_{j+1}-QU_j\quad(j\ge0).
\]
Put \(\Delta=P^2-4Q\). For a nonzero integer \(t\), let \(\operatorname{rad}(|t|)\) be the product of its distinct prime divisors, with \(\operatorname{rad}(1)=1\). An integer sequence \((a_n)_{n\ge1}\) is *Dold* if
\[
\sum_{d\mid n}\mu(n/d)a_d\equiv0\pmod n
\quad\text{for every }n\ge1.
\]
Here \(\mu\) is the Möbius function.

**Theorem (exact multiplier, all even powers).** For every choice of integers \(P,Q\), every integer \(s\ge1\), and every **positive** integer \(M\), the sequence \((M U_{n^{2s}})_{n\ge1}\) is Dold **if and only if**
\[
\boxed{\Delta\ne0\quad\text{and}\quad \operatorname{rad}(|\Delta|)\mid M.}
\]
Thus, when \(\Delta\ne0\), its least positive Dold multiplier is exactly \(\operatorname{rad}(|\Delta|)\), independently of the even index exponent \(2s\). When \(\Delta=0\), **no** positive integer multiplier works.

The bound can be arbitrarily sharper than the discriminant multiplier of Luca and Ward. For example, for every \(k\ge2\), the nondegenerate pair \(P=2\), \(Q=1-2^{2k-2}\) has \(\Delta=2^{2k}\); the least Dold multiplier is \(2\), rather than \(|\Delta|=2^{2k}\). In particular, for \((P,Q)=(2,-15)\) the minimal multiplier is \(2\), rather than \(64\).

## Assumptions and scope

The parameters \(P,Q\) are arbitrary integers: no coprimality, distinct-root, positivity, or nonvanishing-term assumptions are imposed. The exponent \(s\) is an arbitrary fixed positive integer. The scalar \(M\) is required to be a positive integer. The conclusion concerns the **Dold congruences only**. It does not assert the sign condition required for realization as nonnegative periodic-point counts.

This is an exact classification of integer multipliers, not a claim about negative or rational multipliers. The case \(\Delta=0\) is included explicitly, and the prime \(2\) receives no exception. The restriction to even index powers matters: the odd-power Fibonacci subsequences in Moss and Ward have fundamentally different behavior.

## Proof

**1. A companion-matrix encoding.** Put
\[
C=\begin{pmatrix}P&-Q\\1&0\end{pmatrix}\in M_2(\mathbb Z).
\]
The defining recurrence, including \(U_1=1\) and \(U_2=P\), gives
\[
U_j=(C^j)_{21}\quad(j\ge1).
\]
The characteristic polynomial is \(T^2-PT+Q\), with discriminant \(\Delta\).

**2. A matrix lifting observation.** Suppose \(p\) is any prime and \(X,Y\) are *commuting* integral square matrices. For each integer \(h\ge1\),
\[
X\equiv Y\pmod{p^h}\ \Longrightarrow\
X^{p^e}\equiv Y^{p^e}\pmod{p^{h+1}}
\quad(e\ge1).
\]
It suffices to take \(e=1\) and write \(X=Y+p^hZ\). Since \(Z\) commutes with \(Y\), expand the binomial. The first term past \(Y^p\) is divisible by \(p^{h+1}\); the intermediate binomial coefficients carry a factor of \(p\), and the final term has valuation at least \(hp\ge h+1\). This argument also works for \(p=2\), \(h=1\). Repeated powering cannot reduce divisibility, so all \(e\ge1\) follow.

**3. Good primes \(p\nmid\Delta\).** Modulo \(p\), the characteristic polynomial of \(C\) is separable of degree \(2\). Its roots lie in \(\mathbb F_{p^2}\), and \(C\) is diagonalizable over that field. Frobenius fixes each root under its \(p^2\)-th power, including a possible zero root. Consequently,
\[
C^{p^{2s}}\equiv C\pmod p\quad(s\ge1).
\]
Set \(e=2s\). Iterating the lifting observation on the commuting powers of \(C\) gives, for all \(r\ge1\),
\[
C^{p^{er}}\equiv C^{p^{e(r-1)}}\pmod{p^r}.
\]
Raising both sides to the positive power \(m^e\) preserves this congruence. Extracting the \((2,1)\) entry proves
\[
U_{(mp^r)^e}-U_{(mp^{r-1})^e}\equiv0\pmod{p^r}
\quad\text{for every }m\ge1.
\]

**4. Bad primes \(p\mid\Delta\).** Modulo such a prime, the characteristic polynomial has a repeated root \(\alpha\in\mathbb F_p\). This includes \(p=2\): there \(p\mid\Delta\) forces \(P\) even, and the quadratic has a double root in \(\mathbb F_2\). By Cayley–Hamilton,
\[
C\equiv\alpha I+N\pmod p,\qquad N^2=0.
\]
Since \(e=2s\ge2\), in characteristic \(p\) we have
\[
C^{p^e}\equiv\alpha I\pmod p,
\qquad C^{p^{2e}}\equiv\alpha I\pmod p.
\]
The second relation uses \(\alpha^{p^e}=\alpha\). Applying the lifting observation recursively now yields
\[
C^{p^{er}}\equiv C^{p^{e(r-1)}}\pmod{p^{r-1}}
\quad(r\ge2).
\]
As before, after raising to \(m^e\) and extracting the \((2,1)\) entry,
\[
U_{(mp^r)^e}-U_{(mp^{r-1})^e}\equiv0\pmod{p^{r-1}}
\quad(r\ge2,m\ge1).
\]
For \(r=1\), the difference is simply integral; multiplying by any multiple of \(p\) makes it divisible by \(p\). Thus **one** factor of each prime dividing \(\Delta\) repairs *all* prime-power levels.

**5. Dold congruences from local differences.** Assume \(\Delta\ne0\) and \(\operatorname{rad}(|\Delta|)\mid M\). Let \(a_n=M U_{n^e}\). The previous two steps show, for every prime \(p\), every \(r\ge1\), and every \(m\ge1\),
\[
a_{mp^r}\equiv a_{mp^{r-1}}\pmod{p^r}.
\]
Fix \(n\ge1\), take any prime power \(p^r\Vert n\), and put \(m=n/p^r\). Pairing the terms with \(p\)-exponent \(r\) and \(r-1\) in the Möbius sum gives the exact identity
\[
\sum_{d\mid n}\mu(n/d)a_d
=\sum_{j\mid m}\mu(m/j)\bigl(a_{jp^r}-a_{jp^{r-1}}\bigr).
\]
The right side is divisible by \(p^r\). Since this holds for each prime power dividing \(n\), the entire sum is divisible by \(n\). This proves sufficiency simultaneously for every \(s\ge1\).

**6. Optimality and the repeated-root boundary.** Conversely, if \(p\mid\Delta\), step 4 shows \(C^{p^e}\equiv\alpha I\pmod p\). Hence
\[
U_{p^e}\equiv0\pmod p,
\quad U_1=1,
\quad U_{p^e}-U_1\equiv-1\pmod p.
\]
The Dold congruence at the index \(n=p\) forces \(p\mid M\). Thus every prime divisor of \(\Delta\) is unavoidable: \(\operatorname{rad}(|\Delta|)\mid M\). If \(\Delta=0\), this same argument holds for **every** prime \(p\), and no positive integer \(M\) is divisible by them all. Necessity follows, completing the proof.

## Verification

The self-contained script `verify.py` uses exact modular matrix powering and integer arithmetic, independently of the symbolic valuation argument. Run `python3 verify.py` in the directory containing this file and the script. Its observed output is embedded as `verification_output.txt`.

The finite checks cover 220 nonzero-discriminant signed parameter pairs and 18,700 exact Möbius congruences for square indices, with 14,268 additional Möbius congruences at index exponents \(4\), \(6\), and \(8\). It separately checks 104 prime obstructions when \(\Delta=0\) and finite prime-index sharpness for each tested bad prime. These computations support—but **do not substitute for**—the unrestricted matrix proof above.

## Relationship to prior work

Moss and Ward (first public 2020) proved that \((5F_{n^{2s}})_{n\ge1}\) is realizable for every \(s\ge1\) and established the sharp multiplier \(5\) for Fibonacci even-power subsequences (their Corollary 3). They proposed a general discriminant-scaled Lucas Dold conjecture. Luca and Ward (first public 2022; Journal of Integer Sequences 2023) **already proved** that conjecture: their Theorem 5 shows that \((\Delta U_{n^2})\) satisfies the Dold congruences, and their proof shows \((|P|U_{n^2})\) suffices when \(Q=0\). Their Theorem 1 covers a broad class of higher even index powers with sufficient discriminant factors. Those results are not claimed as new here.

The present statement strengthens those **sufficient** multipliers to an **if-and-only-if** classification, removes all repeated prime factors of \(\Delta\), proves one fixed minimal factor works for **every** even exponent, and settles the no-positive-multiplier case \(\Delta=0\). Their Theorem 5 does not imply this radical reduction merely by integer scaling: an integer multiple of a Dold sequence is Dold, but division by a prime factor is not generally Dold-preserving. The matrix Frobenius/lifting argument establishes the missing local improvement and the prime-index obstruction establishes necessity.

The broad survey of Byszewski, Graff, and Ward provides the general Dold definition, equivalent formulations, and matrix-trace examples, but does not formulate this exact minimal multiplier for the nonlinearly indexed Lucas subsequence. A published result on local Dold properties of companion Lucas sequences concerns \(V_n\), rather than the square-/even-power-indexed \(U_n\) considered here.

## Limitations

Only Dold integrality, **not** the periodic-orbit nonnegativity condition, is established. The theorem applies to even powers of the index, not odd powers or arbitrary integer-valued index functions. The finite verifier is not an exhaustive proof over integer parameters, primes, or exponents; the proof above supplies the unrestricted quantifiers. An equivalent formulation in literature not covered by the inspected sources remains possible and merits independent bibliographic review.

## References

1. P. Moss and T. Ward, *Fibonacci along even powers is (almost) realizable*, first public 2020-11-26, arXiv:2011.13068v1, later *Fibonacci Quarterly* 60 (2022), 40–47. https://arxiv.org/abs/2011.13068
2. F. Luca and T. Ward, *On (almost) realizable subsequences of linearly recurrent sequences*, first public 2022-04-06, arXiv:2204.02711v1, later *Journal of Integer Sequences* 26 (2023), Article 23.4.6, especially Theorems 1 and 5 and the proof of Theorem 5. https://cs.uwaterloo.ca/journals/JIS/VOL26/Ward/ward9.pdf
3. J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, *Bulletin of the London Mathematical Society* (2021), DOI: 10.1112/blms.12531, especially Definitions 2.1 and the survey of trace sequences. https://doi.org/10.1112/blms.12531
