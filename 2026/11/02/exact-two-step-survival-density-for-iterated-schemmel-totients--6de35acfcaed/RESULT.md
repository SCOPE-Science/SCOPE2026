# Exact two-step survival density for iterated Schemmel totients

## Finding

For every fixed even integer \(m\ge4\), define the squarefree primorial
\[
Q_m=\prod_{\substack{\ell\le m\\\ell\ \mathrm{prime}}}\ell,
\qquad
\beta_m=\prod_{\substack{\ell\le m\\\ell\nmid m}}\frac{\ell-2}{\ell-1}.
\]
Then \(0<\beta_m<1\). Put
\[
S_m(X)=\#\{1\le n\le X:L_m(L_m(n))>0\},
\qquad E_m(X)=\#\{1\le n\le X:D_m(n)\ge n\}.
\]
There is an explicit positive constant \(\kappa_m\) such that, as \(X\to\infty\),
\[
\boxed{S_m(X)=\kappa_m\frac{X}{(\log X)^{1-\beta_m}}
+O_m\!\left(\frac{X}{(\log X)^{5/4-\beta_m}}\right).}
\]
Furthermore \(E_m(X)\le S_m(X)\), whence
\[
\boxed{E_m(X)=O_m\!\left(\frac{X}{(\log X)^{1-\beta_m}}\right).}
\]
The density-one conclusion applies simultaneously to the complement of all \(D_m\)-perfect and \(D_m\)-abundant integers. Defant separately proved there are infinitely many \(D_m\)-abundant integers for every even positive \(m\); infinitude itself is not claimed as new.

## Assumptions and scope

The parameter \(m\) is a **fixed even integer at least four**; all asymptotic constants and thresholds may depend on \(m\). Logarithms are natural. The Schemmel totient is specified by \(L_m(0)=0\), \(L_m(1)=1\), and for \(n>1\)
\[
L_m(n)=\begin{cases}
0,&\text{if some prime }p\mid n\text{ satisfies }p\le m,\\
\displaystyle\prod_{p^a\parallel n}p^{a-1}(p-m),&\text{otherwise}.
\end{cases}
\]
For \(n>1\), the iteration sum \(D_m(n)\) is the sum of successive terms \(L_m(n),L_m(L_m(n)),\ldots\) up to and including the first term equal to zero or one, and \(D_m(1)=0\). Every iterate of an integer greater than one is strictly smaller and nonnegative, so the process terminates.

Set
\[
\mathcal P_m=\{p\text{ prime}:p>m,\ \gcd(p-m,Q_m)=1\},
\qquad
\mathcal A_m=\{a\pmod{Q_m}:\gcd(a,Q_m)=\gcd(a-m,Q_m)=1\}.
\]
For \(\Re(s)>1\), let
\[
F_m(s)=\prod_{p\in\mathcal P_m}(1-p^{-s})^{-1},\qquad
\kappa_m=\frac1{\Gamma(\beta_m)}\lim_{s\downarrow1}(s-1)^{\beta_m}F_m(s).
\]
This limit exists and is strictly positive by the cited fixed-modulus Selberg–Delange theorem.

## Proof

**1. Exact prime-support characterization.** Let \(n\ge2\). If a prime \(p\le m\) divides \(n\), the first iterate vanishes. Otherwise the displayed product for \(L_m(n)\) is positive. Its prime divisors are drawn from factors \(p\) and \(p-m\), over primes \(p>m\) dividing \(n\). Such a \(p\) is automatically coprime to \(Q_m\). Hence \(L_m(L_m(n))>0\) if and only if no prime \(\ell\le m\) divides any \(p-m\) with \(p\mid n\); that is, if and only if every prime divisor of \(n\) belongs to \(\mathcal P_m\). The equivalence includes \(n=1\), since \(L_m(L_m(1))=1\) and the factor condition is vacuous.

**2. Arithmetic-progression density.** The set \(\mathcal P_m\) consists of the primes in the reduced residue classes \(\mathcal A_m\) modulo \(Q_m\). The Chinese remainder theorem counts admissible residues: for each prime \(\ell\mid m\) there are \(\ell-1\) admissible classes modulo \(\ell\); for each prime \(\ell\nmid m\), \(\ell\le m\), there are \(\ell-2\), since the two distinct residues zero and \(m\) are forbidden. Thus
\[
\frac{|\mathcal A_m|}{\varphi(Q_m)}
=\prod_{\substack{\ell\le m\\\ell\nmid m}}\frac{\ell-2}{\ell-1}=\beta_m.
\]
All factors are positive: if \(m\) is even then the prime two divides \(m\), so every prime in the second product is odd. Bertrand's postulate gives a prime \(m/2<\ell<m\), which cannot divide \(m\), so at least one factor is less than one. Therefore \(0<\beta_m<1\).

**3. Exact count.** From step 1, the indicator of positive second iterates is precisely the multiplicative indicator of integers all of whose prime divisors lie in \(\mathcal A_m\) modulo \(Q_m\). Apply the fixed-modulus case of Chang and Martin [2, Theorem 3.4], which is a Selberg–Delange counting theorem for *arbitrary fixed sets of reduced residue classes*. Its hypotheses require a fixed modulus, a nonempty proper set of reduced classes, and \(0<\beta_m<1\), all verified in step 2. In the source theorem, the main constant equals \(G_{\mathcal A_m}(1)/\Gamma(\beta_m)\), with \(G_{\mathcal A_m}(s)=\zeta(s)^{-\beta_m}F_m(s)\). As \(s\downarrow1\), \((s-1)\zeta(s)\to1\), so this is exactly \(\kappa_m\). The theorem provides the error \(O_m(X(\log X)^{\beta_m-5/4})\). Its analyticity and nonvanishing lemmas for the Euler product imply \(0<\kappa_m<\infty\).

**4. Abundance obstruction.** If \(L_m(L_m(n))=0\), then either \(L_m(n)=0\) or the first iterate is positive with its second iterate zero. In both cases every subsequent iterate is zero, and \(D_m(n)=L_m(n)<n\) for \(n>1\). Also \(D_m(1)=0<1\). Therefore every \(n\) with \(D_m(n)\ge n\) must be counted by \(S_m(X)\). The bound on \(E_m(X)\) follows from step 3. Because \(\beta_m<1\), its quotient by \(X\) tends to zero.

## Verification

The standalone standard-library program `verify.py` uses independent prime factorization to compute \(L_m\), the second iterate, and \(D_m\). For each \(m\in\{4,6,8,10,12,16\}\), it checks every \(1\le n\le40000\), verifies the exact prime-support equivalence, CRT residue counts, and the implication from a forbidden prime divisor to deficiency. Its recorded output is:

```text
VERIFY_OK tested_pairs=240000 forbidden_factor_checks=75498
EXCEPTIONAL_COUNTS_N_40000 {4: 2853, 6: 4470, 8: 1502, 10: 2010, 12: 2830, 16: 1189}
DEPTH_TWO_POSITIVE_TESTS 20241
CRT_RESIDUES_CHECKED_FOR m=4,6,8,10,12,16
```

Run `python3 verify.py`. Finite enumeration checks only the elementary correspondence; the infinite asymptotic relies on the cited Selberg–Delange theorem, not numerical extrapolation.

## Relationship to prior work

Defant [1, equations (1)–(2), Proposition 1, Definition 12, Theorems 13 and 18, Corollary 19] introduced these iterates, proved all positive integers deficient for odd \(m>1\), and proved that for every even \(m>0\) infinitely many \(D_m\)-abundant integers exist. His full paper does not state the above positive-second-iterate support characterization, its exact asymptotic, or the resulting density-zero bound for nondeficient integers when \(m\ge4\).

Landau's general counting principle and Chang–Martin's precise fixed-residue-class theorem [2] already cover the *analytic prime-semigroup counting step*. Accordingly no novelty is claimed for the Selberg–Delange method or the general formula for an arbitrary union of progressions. The contribution here is the exact identification of the Schemmel second-iterate support with the particular CRT-defined prime semigroup, the resulting explicit \(\beta_m\), and its uniform mathematical consequence for \(D_m\)-deficiency. The inference is short but connects two previously distinct results. Earlier equivalent applications may exist and historical originality is not certified independently.

## Limitations

The theorem makes no claim for \(m=2\), nor for odd parameters beyond Defant's existing classification. It counts the integers with a positive second iterate exactly to leading asymptotic order, not the \(D_m\)-abundant integers themselves. The bound on abundance/perfection need not have a sharp exponent. The main asymptotic depends on a published general analytic counting theorem, not a new proof of it.

## References

[1] Colin Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, Journal of Integer Sequences **18** (2015), Article 15.2.1, first published January 13, 2015. https://cs.uwaterloo.ca/journals/JIS/VOL18/Defant/defant5.html ; https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.pdf ; arXiv:1506.05426.

[2] Ben Chang and Greg Martin, *The smallest invariant factor of the multiplicative group*, arXiv:1908.00035, first public July 31, 2019, Section 3, Theorem 3.4 and its lemmas. https://arxiv.org/pdf/1908.00035.

[3] F. Ben Saïd and J.-L. Nicolas, *Sur une application de la formule de Selberg–Delange*, Colloquium Mathematicum **98** (2003), 223–247, which notes Landau's classical asymptotic for integers whose prime factors lie in fixed arithmetic progressions. https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/98/22/87987/sur-une-application-de-la-formule-de-selberg-8211-delange.
