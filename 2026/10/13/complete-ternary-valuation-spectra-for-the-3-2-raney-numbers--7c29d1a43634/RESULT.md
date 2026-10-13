# Complete ternary valuation spectra for the \((3,2)\)-Raney numbers

## Finding

For every integer \(n\ge0\), define the positive integer
\[
T_n=R_{3,2}(n)=\frac{1}{n+1}\binom{3n+1}{n}.
\]
For each integer \(m\ge0\) define the full three-adic valuation polynomial
\[
V_m(q)=\sum_{n=0}^{3^m-1}q^{\nu_3(T_n)},
\]
where \(\nu_3(t)\) is the exponent of the prime \(3\) in a positive integer \(t\). Then, **as an identity of formal power series** in \(z\) with coefficients in \(\mathbb Z[q]\),
\[
\boxed{\displaystyle\sum_{m\ge0}V_m(q)z^m
=\frac{(1-qz)^2}{(1-z)\bigl(1-2(1+q)z+(1+q+q^2)z^2\bigr)}.}
\]
This one identity gives every exact valuation frequency on every complete ternary prefix. In particular, for every fixed \(j\ge0\),
\[
[q^j]V_m(q)\sim \frac{m^{2j+2}}{(2j+2)!}\qquad(m\to\infty),
\]
and for every fixed integer \(r\ge1\),
\[
\#\{0\le n<3^m:3^r\nmid T_n\}\sim \frac{m^{2r}}{(2r)!}.
\]
For every \(m\ge2\), the largest three-adic valuation in this prefix is exactly \(m-1\), and it occurs at exactly \(m+1\) indices. The cases \(m=0\) and \(m=1\) instead have valuation polynomials \(1\) and \(3\), respectively.

## Assumptions and scope

All indices and scale parameters are nonnegative integers. The polynomial variable \(q\) is formal and does not denote a prime. The prime in the valuation is fixed at \(3\). The asymptotics are for \(m\to\infty\) with \(j\) or \(r\) fixed; no uniformity is asserted as those parameters grow. The binomial-coefficient convention is \(\binom ab=0\) for integers \(a\ge0\) and \(b>a\). The result does not assert the residues of \(T_n\) modulo a power of three, only their valuations.

## Proof

**1. Exact digit valuation.** Let \(s_3(h)\) be the sum of the base-three digits of \(h\ge0\). By Legendre's factorial formula, and because \(s_3(3n+1)=s_3(n)+1\),
\[
\begin{aligned}
\nu_3(T_n)
&=\nu_3\!\binom{3n+1}{n}-\nu_3(n+1)\\
&=\frac{s_3(n)+s_3(2n+1)-s_3(3n+1)}{2}-\nu_3(n+1)\\
&=\frac{s_3(2n+1)-1}{2}-\nu_3(n+1).
\end{aligned}
\]
Writing \(n+1=3^ku\) with \(3\nmid u\), one has
\(2n+1=3^k(2u-1)+(3^k-1)\); its two summands occupy disjoint blocks of ternary digits, and \(s_3(3^k-1)=2k\). Hence
\[
\boxed{\displaystyle \nu_3(T_n)=\frac{s_3(2u-1)-1}{2}.}
\]
The right side is a nonnegative integer because \(2u-1\) is odd, its ternary digit sum is odd, and its digit sum is at least one. Pointwise digit/carry information of this type is available in the motivating source; the new assertion here concerns simultaneous frequency distributions over all complete ternary prefixes.

**2. Partition the prefix.** For every integer \(L\ge1\), let
\[
A_L(q)=\sum_{\substack{1\le u<3^L\\3\nmid u}} q^{(s_3(2u-1)-1)/2}.
\]
For \(0\le n<3^m\), the positive integers \(n+1\le3^m\) consist of the single endpoint \(3^m\) and, for \(L=1,\dots,m\), the disjoint sets \(3^{m-L}u\) with \(1\le u<3^L\) and \(3\nmid u\). The endpoint has valuation zero. Therefore
\[
V_m(q)=1+\sum_{L=1}^m A_L(q)
\]
for all \(m\ge0\), including the empty sum when \(m=0\).

**3. A two-state exact digit transfer.** Let \(x\) be a new formal variable and write the \(L\) ternary digits of \(u\) with leading zeros allowed, but with unit digit either \(1\) or \(2\). To compute \(2u-1\) digitwise, start with carry \(-1\). The units digit gives either emitted digit \(1\) and outgoing carry \(0\) (input digit \(1\)), or emitted digit \(0\) and outgoing carry \(1\) (input digit \(2\)). Thus the initial weighted row is \((x,1)\). Every remaining input digit lies in \(\{0,1,2\}\), and, with incoming and outgoing carries indexed by \(0,1\), the sum of \(x^{\text{emitted digit}}\) over the three choices is
\[
M(x)=\begin{pmatrix}1+x^2&x\\x&1+x^2\end{pmatrix}.
\]
An outgoing carry \(0\) adds no leading digit, whereas carry \(1\) adds a leading digit \(1\), giving terminal column \((1,x)^\mathsf T\). The ternary digit sum of \(2u-1\) is odd; consequently
\[
\boxed{xA_L(x^2)=(x,1)M(x)^{L-1}\binom{1}{x}.}
\]
This is an identity of polynomials, not an approximation. The characteristic polynomial of \(M(x)\) has trace \(2(1+x^2)\) and determinant \(1+x^2+x^4\). Cayley--Hamilton, with \(q=x^2\), implies
\[
A_{L+2}(q)=2(1+q)A_{L+1}(q)-(1+q+q^2)A_L(q)
\]
for every \(L\ge1\). Direct initialization gives
\(A_1(q)=2\) and \(A_2(q)=3+3q\).

**4. The rational generating function.** Set
\(D(z,q)=1-2(1+q)z+(1+q+q^2)z^2\). The recurrence and initials yield
\[
\sum_{L\ge1} A_L(q)z^L
=\frac{2z-(1+q)z^2}{D(z,q)}.
\]
Summing \(V_m=1+\sum_{L\le m}A_L\) over \(m\) gives
\[
\sum_{m\ge0}V_m(q)z^m
=\frac1{1-z}\left(1+\frac{2z-(1+q)z^2}{D(z,q)}\right)
=\frac{(1-qz)^2}{(1-z)D(z,q)},
\]
which proves the boxed identity. Both denominators have constant term \(1\) in \(z\), so the formal identity is unambiguous over \(\mathbb Z[q][[z]]\).

**5. Fixed-valuation and prime-power counts.** Rewrite
\[
D(z,q)=(1-z)^2-qz(2-z)+q^2z^2.
\]
For each fixed \(j\ge0\), the coefficient of \(q^j\) in the rational generating function is a rational function of \(z\) with sole pole at \(z=1\). The term obtained by taking \(j\) factors of \(qz(2-z)/(1-z)^2\) from the geometric expansion of \(1/D\), and the constant term of the numerator \((1-qz)^2\), is
\[
\frac{z^j(2-z)^j}{(1-z)^{2j+3}}.
\]
Every other selection yielding total \(q\)-degree \(j\) has a pole at \(z=1\) of order at most \(2j+1\), because it uses at least one factor of \(q^2z^2\) from \(D\) or a positive power of \(q\) from the numerator. Since \(z^j(2-z)^j=1\) at \(z=1\), the leading pole coefficient is exactly one. Coefficient extraction using \([z^m](1-z)^{-h}=\binom{m+h-1}{h-1}\) gives
\[
[q^j]V_m(q)=\frac{m^{2j+2}}{(2j+2)!}+O_j(m^{2j+1}).
\]
The number of terms not divisible by \(3^r\) is \(\sum_{j=0}^{r-1}[q^j]V_m(q)\), whose highest-degree contribution is the \(j=r-1\) term; this proves its stated asymptotic.

**6. The extremal valuation.** The transfer recurrence and initials show inductively that \(\deg A_L=L-1\) and its leading coefficient is \(L+1\) for every \(L\ge1\). Indeed the top coefficients for \(L=1,2\) are \(2,3\), and the top coefficient in \(A_{L+2}\) is twice that in \(A_{L+1}\) minus that in \(A_L\), giving \(L+3\). For \(m\ge2\), the unique largest degree among the summands of \(V_m=1+\sum_{L=1}^m A_L\) comes from \(A_m\), and its coefficient is \(m+1\). This proves the extremal assertion.

As exact special cases, evaluating at \(q=0\) gives
\([q^0]V_m(q)=\binom{m+2}{2}\); extracting the linear coefficient gives
\[
[q]V_m(q)=3\binom{m+2}{4}-2\binom{m+1}{4}.
\]
Thus the count of terms not divisible by \(9\) is the sum of these two exact quantities.

## Verification

The standalone standard-library program `verify.py` checks two independent valuation evaluations (factorial valuations and digit sums) for all \(0\le n<3^8\), compares direct large-integer Raney values for \(0\le n<220\), verifies every valuation-frequency polynomial for \(0\le m\le8\), and checks the proposed rational identity coefficientwise to degree \(12\) in the scale variable. It also checks the exact coefficient for valuation one through scale \(12\). The recorded output is `verification_output.txt`. Those finite computations corroborate, but do not replace, the preceding all-index proof.

## Relationship to prior work

Eu, Huang and Kao [1] study the same \((3,2)\)-Raney sequence modulo primes. Their Lemma 4.1 gives an explicit pointwise three-adic valuation/carry criterion, and Theorem 6.1 gives the exact valuation-zero count \(\binom{m+2}{2}\) on the first \(3^m\) indices. The latter is precisely the \(q=0\) specialization of the present identity and is **not** claimed as new. The new contribution is a simultaneous rational enumeration of every valuation stratum, including exact counts modulo arbitrary fixed powers \(3^r\) and the extremal multiplicity law. The original zero-run spectral polynomials record lengths of consecutive zeros modulo the prime; they do not record the individual values of \(\nu_3(T_n)\).

Bobrowski, He and Shiue [2] give divisibility statements for selected classes of generalized Catalan and Raney numbers; their theorems do not give the all-prefix valuation-frequency identity. Krattenthaler and Müller [3] give general prime-power congruence machinery and its applications to certain Fuss--Catalan numbers, not the \((3,2)\) valuation-frequency distribution. OEIS A006013 [4] identifies and tabulates the underlying integer sequence without the bivariate valuation generating function.

## Limitations

Only the fixed prime \(3\) and the specific \((3,2)\)-Raney family are covered. The theorem counts valuations, not exact nonzero residues modulo higher powers of three. The fixed-\(r\) asymptotic does not justify replacing \(r\) by a function growing with \(m\). The pointwise valuation identity and valuation-zero count already occur in or follow from [1], and the transfer-matrix derivation uses elementary digit arithmetic; no priority is asserted against unindexed equivalent valuations-of-generalized-Catalan distributions.

## References

[1] S.-P. Eu, Z.-T. Huang and L. Kao, *Zero-Run Spectra of the \((3,2)\) Raney numbers Modulo Primes*, arXiv:2609.25742v1, first released 2026-09-22. https://arxiv.org/abs/2609.25742

[2] J. Bobrowski, T.-X. He and P. J.-S. Shiue, *Divisibility of Generalized Catalan Numbers and Raney Numbers*, Journal of Computational Analysis and Applications 26 (2019), 1047–1058. https://scholars.iwu.edu/ws/portalfiles/portal/39724414/144%20divisibility%20of%20generalized%202019.pdf

[3] C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, Aequationes Mathematicae 99 (2025), 2505–2547. https://doi.org/10.1007/s00010-025-01195-0

[4] OEIS Foundation, entry A006013, *\(a(n)=\binom{3n+1}{n}/(n+1)\)*. https://oeis.org/A006013
