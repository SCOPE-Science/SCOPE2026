# Two-term frequency law for residues two modulo four in odd strongly unimodal sequences

## Finding

Let \(u(n)\) be the number of strongly unimodal sequences of total weight \(n\) all of whose entries are odd, and define, for real \(X\ge3\),
\[
N_2(X)=\#\{1\le n\le X:n\text{ odd},\ u(n)\equiv2\pmod4\}.
\]
Then, as \(X\to\infty\),
\[
N_2(X)=\frac{\pi^2}{12}\frac{X}{\log X}
+\frac{\pi^2}{36}\left(3+4\log2-\frac{15}{4}\log3
-6\frac{\zeta'(2)}{\zeta(2)}\right)\frac{X}{(\log X)^2}
+O\!\left(\frac{X}{(\log X)^3}\right).
\]
The two disjoint arithmetic families described below contribute, respectively,
\[
N_1(X)=\frac{\pi^2}{36}\frac{X}{\log X}
+\frac{\pi^2}{36}\left(1+2\log2-\frac54\log3
-2\frac{\zeta'(2)}{\zeta(2)}\right)\frac{X}{(\log X)^2}
+O\!\left(\frac{X}{(\log X)^3}\right)
\]
and
\[
N'_2(X)=\frac{\pi^2}{18}\frac{X}{\log X}
+\frac{\pi^2}{18}\left(1+\log2-\frac54\log3
-2\frac{\zeta'(2)}{\zeta(2)}\right)\frac{X}{(\log X)^2}
+O\!\left(\frac{X}{(\log X)^3}\right).
\]
Here \(\zeta\) is the Riemann zeta function. Thus the two disjoint families have limiting leading-term ratio \(1:2\). The displayed error bounds have absolute implied constants.

## Assumptions and scope

A strongly unimodal sequence is a finite list of positive integers strictly increasing to a unique peak and then strictly decreasing. Every entry is required to be odd. Sequences with unequal left and right sides are permitted. Write \(u(n)=\mathrm{ou}^{*}(n)\) in the notation of Bringmann--Lovejoy and Banerjee--Ghosh Dastidar. The generating function is
\[
\sum_{n\ge0}u(n)q^n=\sum_{j\ge0}q^{2j+1}\prod_{h=0}^{j-1}(1+q^{2h+1})^2.
\]
Only positive **odd** indices are counted, since the required available mod-four classification applies to those indices. Denote by \(\mathcal P_1\) the primes congruent to \(5\) or \(23\) modulo \(24\), and by \(\mathcal P_2\) those congruent to \(7\) or \(13\) modulo \(24\). Put
\[
\mathcal M_1=\{m\ge1:2\mid m,\ 3\nmid m\},\qquad
\mathcal M_2=\{m\ge1:3\nmid m\}.
\]
The function \(N_1(X)\) counts the qualifying indices with \(3n-1=p^{4k+1}m^2\), where \(p\in\mathcal P_1\), \(m\in\mathcal M_1\), \(p\nmid m\), and \(k\ge0\). The function \(N'_2(X)\) counts those with \(3n-1=2p^{4k+1}m^2\), where \(p\in\mathcal P_2\), \(m\in\mathcal M_2\), \(p\nmid m\), and \(k\ge0\). Every index has at most one such representation.

## Proof

**1. Arithmetic parametrization.** By Theorem 1.5 of Banerjee--Ghosh Dastidar (2026), for odd \(n\), the condition \(u(n)\equiv2\pmod4\) is equivalent to
\[
3n-1=\varepsilon p^{4k+1}m^2,
\quad \varepsilon\in\{1,2\},\quad k\ge0,\quad
p\text{ prime},\quad p\nmid m,\quad \left(\frac{-2}{p}\right)=-1.
\]
The Kronecker-symbol condition means \(p\equiv5,7\pmod8\). Because \(3n-1\equiv2\pmod3\), we must have \(3\nmid m\), and \(p\equiv2\pmod3\) for \(\varepsilon=1\), or \(p\equiv1\pmod3\) for \(\varepsilon=2\). Thus the respective prime classes modulo \(24\) are \(\{5,23\}\) and \(\{7,13\}\). For odd \(n\), \(3n-1\) is even; if \(\varepsilon=1\) this further forces \(2\mid m\), whereas for \(\varepsilon=2\) it imposes no restriction on the parity of \(m\). Conversely, each permitted representation yields a positive odd integer \(n\) whenever \(\varepsilon p^{4k+1}m^2\le3X-1\). The exponent of the distinguished prime is odd and all other odd-prime valuations are even, so this representation is unique; the parity of the valuation at \(2\) determines \(\varepsilon\). The families are disjoint.

**2. Removing higher exponents and forbidden square factors.** For each \(\varepsilon\), summing over \(k\ge1\), primes \(p\ge5\), and the possible \(m\), while dropping congruence and coprimality constraints, gives at most
\[
\sqrt{3X}\sum_{p\ge5}\sum_{k\ge1}p^{-2k-1/2}
=O(\sqrt X).
\]
At \(k=0\), the representations with \(p\mid m\) have \(m=ph\), so \(p^3h^2\le3X\); their number is at most
\[
\sqrt{3X}\sum_{p\ge5}p^{-3/2}=O(\sqrt X).
\]
Both convergent prime sums are valid uniformly in \(X\). Hence, with \(\pi_{\mathcal P}(y)=\#\{p\le y:p\in\mathcal P\}\) and \(a_1=3\), \(a_2=3/2\),
\[
N_{\varepsilon}(X)=\sum_{m\in\mathcal M_{\varepsilon}}
\pi_{\mathcal P_{\varepsilon}}\!\left(\frac{a_\varepsilon X}{m^2}\right)
+O(\sqrt X).
\]
Here \(N_{\varepsilon}\) denotes \(N_1\) for \(\varepsilon=1\) and \(N'_2\) for \(\varepsilon=2\). Replacing \(3X-1\) by \(3X\) in the upper cutoff can change at most one integer value for each \(m\le\sqrt{3X}\), so the additional error is \(O(\sqrt X)\).

**3. Prime-number-theorem summation.** Each class set has two of the eight reduced residue classes modulo \(24\). The prime number theorem in fixed arithmetic progressions gives, for every fixed \(A>0\),
\[
\pi_{\mathcal P_{\varepsilon}}(y)=\tfrac14\operatorname{Li}(y)
+O_A\!\left(\frac{y}{(\log y)^A}\right)
\]
for \(y\ge3\). Write \(L=\log X\). For \(m\le X^{1/6}\), uniformly in the relevant fixed positive values of \(a_\varepsilon\), the standard expansion is
\[
\pi_{\mathcal P_{\varepsilon}}(a_\varepsilon X/m^2)=
\frac{a_\varepsilon X}{4m^2}\left(
\frac1L+\frac{1-\log a_\varepsilon+2\log m}{L^2}
\right)
+O\!\left(\frac{X(1+\log m)^2}{m^2L^3}\right).
\]
Indeed \(\log(a_\varepsilon X/m^2)\ge(2/3)L+O(1)\) and the error in the logarithmic-integral expansion is uniform. Summation of the displayed error is \(O(X/L^3)\) because \(\sum_{m\ge1}(1+\log m)^2/m^2\) converges. For \(m>X^{1/6}\), the trivial bound \(\pi_{\mathcal P}(aX/m^2)\le aX/m^2\) gives a total \(O(X^{5/6})\). Extending the weighted reciprocal-square sums from \(m\le X^{1/6}\) to all \(m\in\mathcal M_\varepsilon\) also incurs \(O(X^{5/6}\log X)\), which is absorbed by \(O(X/L^3)\). Therefore, defining
\[
S_\varepsilon=\sum_{m\in\mathcal M_\varepsilon}m^{-2},
\qquad T_\varepsilon=\sum_{m\in\mathcal M_\varepsilon}(\log m)m^{-2},
\]
we obtain
\[
N_{\varepsilon}(X)=\frac{a_\varepsilon S_\varepsilon}{4}\frac{X}{L}
+\frac{a_\varepsilon}{4}
\left((1-\log a_\varepsilon)S_\varepsilon+2T_\varepsilon\right)
\frac{X}{L^2}
+O(X/L^3).
\]

**4. Evaluating both constants.** An Euler-product restriction at \(2\) and \(3\) yields
\[
S_1=2^{-2}(1-3^{-2})\zeta(2)=\frac{\pi^2}{27},
\qquad S_2=(1-3^{-2})\zeta(2)=\frac{4\pi^2}{27}.
\]
Logarithmic differentiation of the same restricted Dirichlet series gives
\[
T_1=S_1\left(-\frac{\zeta'(2)}{\zeta(2)}+\log2-\frac{\log3}{8}\right),
\quad
T_2=S_2\left(-\frac{\zeta'(2)}{\zeta(2)}-\frac{\log3}{8}\right).
\]
Insert these four expressions and \(a_1=3\), \(a_2=3/2\) into the preceding formula. This gives the two displayed asymptotic expansions, including their respective second-order coefficients. Adding them gives the claimed expansion for \(N_2(X)\), since the two families are disjoint and exhaustive. \(\square\)

## Verification

The accompanying standalone Python program `verification/verify.py` uses integer arithmetic to build the coefficients of the generating function modulo four and independently factor the corresponding integers in the published characterization. It checked all \(1250\) odd positive indices at most \(2500\), then counted the two disjoint prime-power families exactly for \(X=100,1000,10000,100000\). The corresponding pair counts are \((7,14)\), \((52,100)\), \((398,740)\), and \((3061,5724)\). The final output was `VERIFY_OK`. These finite checks do not prove the asymptotic; the unrestricted proof is Steps 1–4 above.

## Relationship to prior work

Banerjee and Ghosh Dastidar (arXiv:2610.20135v1, October 14, 2026) establish an exact **pointwise** residue characterization in their Theorem 1.5, which is used here as a premise. Their Theorem 1.5 and Corollaries 1.6–1.8 do not state a weighted prime-density expansion, a leading residue-frequency constant, a second-order coefficient, or a quantitative split of the two representing forms. This result performs a separate analytic summation using the prime number theorem in progressions and explicit logarithmically weighted Euler products. It is therefore an analytic consequence of that stronger arithmetic classification, **not** an independent reproof of the classification.

Bringmann and Lovejoy (arXiv:2308.11556, 2023) give generating functions, asymptotics for the **sizes** of individual sequence counts, and congruences on arithmetic progressions; their asymptotics do not address the number of indices with a prescribed residue. Standard prime number theory in arithmetic progressions supplies the analytic input but not the specialized constants without the coefficient classification and weighted enumeration.

## Limitations

The claim counts only odd weights \(n\), not all positive indices. It depends on the published Theorem 1.5 and the standard prime number theorem in fixed arithmetic progressions. The asymptotic does not give an effective threshold at which the leading approximation dominates. The finite verifier corroborates arithmetic parametrization but cannot independently certify infinitely many terms. An exact prior treatment of the same two-term frequency statistic was not located; implicit coverage via the published pointwise classification and standard prime-counting arguments remains the main originality risk. Independent validation of the present derivation has not been performed.

## References

1. K. Banerjee and M. Ghosh Dastidar, *Congruences for odd unimodal sequences and a problem of Bringmann and Lovejoy*, arXiv:2610.20135v1 (first public posting October 14, 2026), Theorem 1.5 and Section 4. https://arxiv.org/html/2610.20135v1
2. K. Bringmann and J. Lovejoy, *Odd unimodal sequences*, arXiv:2308.11556 (first public posting August 22, 2023), Theorems 1.3–1.5 and Section 6. https://arxiv.org/abs/2308.11556
3. Prime number theorem in fixed arithmetic progressions and the classical asymptotic expansion of the logarithmic integral (standard analytic-number-theory results).
