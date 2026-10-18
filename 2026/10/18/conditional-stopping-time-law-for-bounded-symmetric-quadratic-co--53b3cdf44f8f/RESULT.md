# Conditional stopping-time law for bounded symmetric quadratic Collatz orbits

## Finding

Define \(S:\mathbb N_0\to\mathbb N_0\) by \(S(n)=n/2\) for even \(n\), and \(S(n)=(n^2-1)/4\) for odd \(n\). For each positive integer eventually reaching zero, let \(T(n)\) be its least zero-hitting time (counting every individual iteration), and define \(\mathcal B(X)=\{1\le n\le X:T(n)<\infty\}\). All logarithms in the theorem below are base two unless otherwise indicated.

**Theorem.** For every integer \(L\ge7\), the complete dyadic bounded-orbit census and its first stopping-time moment are
\[
|\mathcal B(2^L)|=L^2+2L-12,
\qquad
\sum_{n\in\mathcal B(2^L)}T(n)
=\frac{L^4+8L^3+23L^2+1144L-7548}{12}.
\]
More generally, if \(X\to\infty\) is real and \(L=\lfloor\log_2X\rfloor\), then \(|\mathcal B(X)|=L^2+O(L)\). Choose \(N_X\) uniformly from \(\mathcal B(X)\), and set \(Z_X=T(N_X)/L^2\). The distribution of \(Z_X\) converges to the distribution with continuous cumulative distribution function
\[
F(z)=\begin{cases}
0,&z<0,\\
2\sqrt{2z}-2z,&0\le z\le1/2,\\
1,&z>1/2.
\end{cases}
\]
The Kolmogorov distance satisfies the **sharp rate**
\[
\sup_{z\in\mathbb R}|\mathbb P(Z_X\le z)-F(z)|=\Theta(L^{-1/2}).
\]
More precisely, uniformly for \(2^L\le X<2^{L+1}\),
\[
\sqrt L\Big(F(1/L)-\mathbb P(Z_X\le1/L)\Big)
\longrightarrow\frac{2\sqrt2}{3}.
\]
For every fixed nonnegative integer \(r\), the moments satisfy
\[
\mathbb E[Z_X^r]\longrightarrow
\frac{1}{2^r(r+1)(2r+1)}.
\]
In particular the limiting mean is \(1/12\) and limiting variance is \(7/720\).

## Assumptions and scope

The domain is the nonnegative integers, though \(\mathcal B(X)\) deliberately excludes zero. Results for nonzero starting values with unbounded orbits are not asserted. The source of the exhaustive bounded-seed classification is Ye's 2026 theorem; the terminal stopping-time recurrences are also visible in Sedaghat's 2020 Lemma 6. This theorem concerns **the counting measure conditional on eventual termination**, not natural-density random integers (the conditional population has zero natural density). The asymptotic constants and the sharp distributional rate are unconditional given the cited classification theorem.

## Proof

**1. Terminal times and exceptional seeds.** Write \(C_m=\binom{m+1}{2}\). Ye's classification [1, Theorem 3] says a positive seed reaches zero if and only if its odd part is among \(2^m-1\), \(2^m+1\) (\(m\ge1\)) and \(11,23,181\). For every \(m\ge2\), one step of \(S\) at \(2^m\pm1\), followed by \(m-1\) halving steps, reaches \(2^{m-1}\pm1\). The base cases are \(T(1)=1\), \(T(3)=3\). Thus for all \(m\ge1\) and \(\ell\ge0\),
\[
T(2^\ell(2^m-1))=\ell+C_m,\qquad
T(2^\ell(2^m+1))=\ell+C_m+2.
\]
These formulas also follow from [2, Lemma 6]. The overlap between the two families is exactly the odd part \(3=2^2-1=2^1+1\); its two formulas both give \(\ell+3\). Finally \(11\to30\to15\), \(23\to132\to66\to33\), and \(181\to8190\to4095\). Since \(15=2^4-1\), \(33=2^5+1\), and \(4095=2^{12}-1\), these give respectively \(T(11)=12\), \(T(23)=20\), \(T(181)=80\). Each initial factor \(2^\ell\) adds precisely \(\ell\) steps.

**2. Exact dyadic census.** For \(X=2^L\), the minus family has \(L+1\) representatives with \(m=1\), and \(L-m+1\) with each \(2\le m\le L\). The plus family has \(L-m\) with each \(1\le m\le L-1\). Their common odd part \(3\) occurs in \(L-1\) powers-of-two multiples. For \(L\ge7\), the exceptional odd parts \(11,23,181\) contribute respectively \(L-3\), \(L-4\), and \(L-7\) representatives (the last is zero at \(L=7\)). Therefore
\[
|\mathcal B(2^L)|=(L+1)+2\frac{L(L-1)}2-(L-1)+(L-3)+(L-4)+(L-7)
=L^2+2L-12.
\]

**3. Exact first moment.** Put
\[
\begin{aligned}
M_-(L)&=\frac{(L+1)(L+2)}2+\sum_{m=2}^{L}\left[(L-m+1)C_m+\frac{(L-m)(L-m+1)}2\right],\\
M_+(L)&=\sum_{m=1}^{L-1}\left[(L-m)(C_m+2)+\frac{(L-m-1)(L-m)}2\right],\\
D(L)&=3(L-1)+\frac{(L-2)(L-1)}2,\\
E_{b,t}(L)&=(L-b+1)t+\frac{(L-b)(L-b+1)}2.
\end{aligned}
\]
The two \(M\) terms sum the stopping times of the two terminal families, \(D\) removes the duplicated odd part \(3\), and \(E_{b,t}\) counts one exceptional odd part with threshold \(2^{b-1}<q<2^b\) and base hitting time \(t\). Direct polynomial summation gives
\[
M_-(L)+M_+(L)-D(L)+E_{4,12}(L)+E_{5,20}(L)+E_{8,80}(L)
=\frac{L^4+8L^3+23L^2+1144L-7548}{12}.
\]
No numerical interpolation is used for this identity.

**4. Conditional distribution and upper convergence rate.** For arbitrary \(2^L\le X<2^{L+1}\), compare the distinct bounded seeds to the two labeled triangular arrays \(\{(\ell,m):\ell\ge0,m\ge1,\ell+m\le L\}\). Each labeled array contains \(L(L+1)/2\) pairs. The plus-family admissibility condition can differ from its triangle only on \(\ell+m=L\); the minus family only on \(\ell+m=L+1\). The duplicated odd part and the three exceptional families alter the census by \(O(L)\). Hence \(|\mathcal B(X)|=L^2+O(L)\), uniformly in the location of \(X\) within this dyadic interval.

For all admissible triangle pairs the exact time formulas give
\[
\frac{T}{L^2}=\frac12\left(\frac mL\right)^2+O(L^{-1}),
\]
uniformly. The weighted triangular-lattice distribution of \(m/L\) has cumulative law \(2u-u^2+O(L^{-1})\), uniformly for \(0\le u\le1\), by summing the weights \(L-m+1\). Substituting \(u=\sqrt{2z}\) gives the stated \(F\). This cumulative law is globally one-half-Hölder continuous, so a horizontal perturbation of size \(O(L^{-1})\) moves the cumulative probability by at most \(O(L^{-1/2})\). The \(O(L)\) exceptional and boundary pairs contribute \(O(L^{-1})\). Thus the Kolmogorov error is \(O(L^{-1/2})\). Boundedness of \(Z_X\), together with the same weighted-lattice summation, gives the displayed moment formula; explicitly
\[
\lim_{X\to\infty}\mathbb E[Z_X^r]
=\int_0^1 2(1-u)\left(\frac{u^2}{2}\right)^rdu
=\frac{1}{2^r(r+1)(2r+1)}.
\]

**5. Sharpness of the distributional rate.** Every bounded positive seed obeys \(T(n)\ge\log_2 n\). This follows immediately from the terminal-time formulas since \(C_m\ge m\), and from \(T(11)=12\), \(T(23)=20\), \(T(181)=80\). Thus every seed with \(T(n)\le L\) already satisfies \(n\le2^L\), independently of the chosen cutoff \(X\in[2^L,2^{L+1})\). Writing \((w)_+=\max\{w,0\}\), their number is exactly
\[
H_L=\sum_{m\ge1}(L-C_m+1)_+
+\sum_{m\ge1}(L-C_m-1)_+
-(L-2)_+ +(L-11)_+ +(L-19)_+ +(L-79)_+.
\]
(The three last terms are from the exceptional odd parts.) Comparison with \(\int_0^{\sqrt{2L}}(L-t^2/2)\,dt\) yields
\[
H_L=\frac{4\sqrt2}{3}L^{3/2}+O(L).
\]
Since the exact normalizing population has size \(L^2+O(L)\), at the argument \(z=1/L\) we obtain
\[
\mathbb P(Z_X\le1/L)=\frac{4\sqrt2}{3\sqrt L}+O(L^{-1}).
\]
On the other hand \(F(1/L)=2\sqrt{2/L}-2/L\). Their difference is \(2\sqrt2/(3\sqrt L)+O(L^{-1})\), establishing both the displayed pointwise sharpness and the global \(\Theta(L^{-1/2})\) Kolmogorov rate.

## Verification

The standalone script `verify.py` uses exact integer arithmetic to (a) generate the classified bounded seeds, (b) independently iterate the map to zero for every generated seed at dyadic cutoffs in a finite test range, (c) compare the resulting census and total hitting times to the two closed polynomials, and (d) check the sharp-rate point-count formula against finite direct enumeration. Run with `python3 verify.py` from the extracted directory. The script verifies finite cases only; the displayed infinite statements rely on the arguments above and on the cited exhaustive bounded-seed classification.

## Relationship to prior work

Ye [1, Theorem 3] proves the complete bounded-seed classification, and [1, Corollary 1] supplies a quadratic-logarithmic **upper bound**, not the exact dyadic census, stopping-time moment polynomial, limiting conditional distribution, or its sharp Kolmogorov rate. Sedaghat [2, Lemma 6] already establishes the individual terminal-seed hitting-time formulas; these are cited inputs and are not claimed as new. The new result combines that deterministic orbit geometry with an exact dyadic census, a global conditional law, and a provably optimal slow convergence scale. Other Collatz-map stopping-time statistics concern different dynamics; no assertion about the original \(3n+1\) map is made.

## Limitations

The population is conditioned on eventual hitting of zero, and it has natural density zero. The theorem does not bound the stopping time of divergent orbits, does not remove reliance on Ye's Diophantine classification, and does not claim any independent computer certification. The Kolmogorov bound is order-sharp; an exact optimal leading constant for the global supremum is not determined. Novelty relative to implicitly derivable older finite sums remains a residual literature risk.

## References

[1] Xuda Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps*, arXiv:2610.10660v1, first publicly submitted 7 October 2026, Theorem 3, Corollary 1, and Lemma 1. https://arxiv.org/html/2610.10660v1

[2] H. Sedaghat, *Bounded Orbits of Quadratic Collatz-type Recursions*, arXiv:2004.07357, first publicly submitted 15 April 2020, Section 3 and Lemma 6. https://arxiv.org/abs/2004.07357
