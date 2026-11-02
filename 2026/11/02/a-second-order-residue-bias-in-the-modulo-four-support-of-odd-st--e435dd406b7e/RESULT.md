# A second-order residue bias in the modulo-four support of odd strongly unimodal sequences

## Finding

Let \(\mathrm{ou}^{*}(n)\) count strongly unimodal sequences of total weight \(n\) whose every part is odd, as in the generating series below. For \(r\in\{1,3,5,7\}\) and \(X\geq 1\), let
\[
N_r(X)=\#\{1\leq n\leq X:n\equiv r\pmod 8,\ \mathrm{ou}^{*}(n)\equiv2\pmod4\}.
\]
Write \(Z=\zeta(2)=\pi^2/6\), \(Z'=\zeta'(2)\), and
\[
B=-\frac{Z'}4+Z\left(\frac18+\frac{\log2}{24}-\frac{5\log3}{32}\right),\qquad
\delta_1=\delta_5=0,\quad\delta_7=1,\quad\delta_3=3.
\]
Then, **unconditionally**, for all four residue classes,
\[
\boxed{N_r(X)=\frac{\pi^2}{48}\frac{X}{\log X}
+\left(B+\delta_r\frac{\pi^2\log2}{48}\right)\frac{X}{(\log X)^2}
+O\!\left(\frac{X}{(\log X)^3}\right)}\qquad(X\longrightarrow\infty).
\]
In addition, for every fixed \(A>0\),
\[
N_1(X)-N_5(X)=O_A\!\left(\frac{X}{(\log X)^A}\right).
\]
Consequently the four exceptional classes have the same first-order density (relative to \(X/\log X\)), but the second-order coefficients satisfy a strict ranking: class \(3\) exceeds class \(7\), which exceeds classes \(1\) and \(5\), for all sufficiently large \(X\). Their second-order offsets are in the proportions \(3:1:0:0\).

## Assumptions and scope

The generating function defining the integer \(\mathrm{ou}^{*}(n)\) is
\[
\sum_{n\ge0}\mathrm{ou}^{*}(n)q^n
=\sum_{j\ge0}q^{2j+1}\prod_{h=0}^{j-1}(1+q^{2h+1})^2.
\]
We rely on the exact modulo-four characterization of Banerjee and Ghosh Dastidar [1, Theorem 1.5]: for positive **odd** \(n\), the congruence \(\mathrm{ou}^{*}(n)\equiv2\pmod4\) holds precisely when
\[
3n-1=\varepsilon p^{4k+1}m^2,
\quad \varepsilon\in\{1,2\},\ k\ge0,\ m\ge1,\ p\nmid m,
\quad p\text{ an odd prime},\quad\left(\frac{-2}{p}\right)=-1.
\]
The exact congruence characterization is prior work, *not* asserted here as new. The additional input is the classical fixed-modulus prime number theorem in arithmetic progressions modulo \(24\), including its standard zero-free-region error term. No unproved hypothesis, generalized Riemann hypothesis, or numerical heuristic is used.

## Proof

**1. Unique arithmetic parametrization.** For odd \(n\), put \(M=(3n-1)/2\), so \(M\equiv1\pmod3\) and \(M\le Y=(3X-1)/2\). The condition \(\left(\frac{-2}{p}\right)=-1\) for odd primes is equivalent to \(p\equiv5,7\pmod8\). Splitting the two values of \(\varepsilon\), and writing \(m=2u\) when \(\varepsilon=1\) (forced because \(3n-1\) is even), gives the disjoint types
\[
\begin{array}{lll}
\mathrm{A}:&M=p^{4k+1}u^2,&p\equiv7,13\pmod{24},\quad3\nmid u,\ p\nmid u;\\
\mathrm{B}:&M=2p^{4k+1}u^2,&p\equiv5,23\pmod{24},\quad3\nmid u,\ p\nmid u.
\end{array}
\]
Types A and B have respectively even and odd valuations at \(2\), so cannot overlap. Within either type, \(p\) is the unique prime with exponent congruent to \(1\pmod4\) (all other prime exponents are even), hence each eligible \(M\) has exactly one representation. The congruence \(n=(2M+1)/3\pmod8\) gives the following exact residue splitting:

* \(r=1\): type A, \(u\) odd, \(p\equiv13\pmod{24}\).
* \(r=5\): type A, \(u\) odd, \(p\equiv7\pmod{24}\).
* \(r=7\): type B, \(u\) odd, \(p\equiv5,23\pmod{24}\).
* \(r=3\): type A, \(u\) even, \(p\equiv7,13\pmod{24}\), **or** type B, \(u\) even, \(p\equiv5,23\pmod{24}\).

Here the congruence classification is obtained from \(M\pmod4\), using that all odd squares are \(1\pmod8\); no cases are omitted.

**2. Removing lower-order prime-power constraints.** The contributions with \(k\ge1\) are bounded by
\[
O\!\left(\sqrt Y\sum_{p\ge5}\sum_{k\ge1}p^{-(4k+1)/2}\right)=O(\sqrt Y).
\]
For \(k=0\), reinstating tuples with \(p\mid u\) changes each count by at most
\[
O\!\left(\sqrt Y\sum_{p\ge5}p^{-3/2}\right)=O(\sqrt Y).
\]
Both errors are negligible compared with \(X/(\log X)^A\) for any fixed \(A>0\). Thus only sums over primes \(p\) in fixed residue classes modulo \(24\) with \(p\le Y/(cu^2)\) remain, where \(c=1\) (A) or \(c=2\) (B). Each admissible residue class of primes has natural prime density \(1/8\).

**3. A uniform two-term prime-counting expansion.** Set \(L=\log Y\). For \(c\in\{1,2\}\) and \(u\le Y^{1/8}\), the prime number theorem modulo \(24\), followed by an integration-by-parts expansion, gives for any chosen collection \(R\) of reduced residue classes
\[
\pi_R\left(\frac{Y}{cu^2}\right)
=\frac{|R|Y}{8cu^2}\left[
\frac1L+\frac{1+\log(cu^2)}{L^2}
+O\!\left(\frac{1+\log^2(cu^2)}{L^3}\right)
\right]+O\!\left(\frac{Y}{cu^2}e^{-a\sqrt L}\right)
\]
for a positive constant \(a\). In the tail \(u>Y^{1/8}\), use the elementary bound \(\pi_R(t)\le t\) (and zero if \(t<2\)). Since \(\sum_{u>Y^{1/8}}u^{-2}=O(Y^{-1/8})\), the total tail is \(O(Y^{7/8})\), and the above error terms are summable because \(\sum_{u\ge1}(1+\log^2u)u^{-2}<\infty\). Hence a two-term expansion holds with total error \(O(Y/L^3)\). Moreover, replacing the displayed two-term expansion by any fixed-order logarithmic expansion makes its error \(O_A(Y/L^A)\), a fact used below.

**4. Exact square-weight moments.** Put
\[
S_o=\sum_{\substack{u\ge1\\u\equiv1,5\pmod6}}\frac1{u^2}=\frac{2Z}{3},\qquad
S_e=\sum_{\substack{u\ge1\\2\mid u,\ 3\nmid u}}\frac1{u^2}=\frac{2Z}{9},
\]
and \(T_o=\sum_{(u,6)=1}(\log u)/u^2\), \(T_e=\sum_{2\mid u,\,3\nmid u}(\log u)/u^2\). Differentiating the Euler products
\(\zeta(s)(1-2^{-s})(1-3^{-s})\) and \(2^{-s}\zeta(s)(1-3^{-s})\) at \(s=2\) yields
\[
T_o=-\frac{2Z'}3-Z\left(\frac{2\log2}{9}+\frac{\log3}{12}\right),\qquad
T_e=-\frac{2Z'}9+Z\left(\frac{2\log2}{9}-\frac{\log3}{36}\right).
\]
In particular \(S_o=3S_e\), but their logarithmic moments differ in a controlled, \(2\)-adic way.

**5. Assemble the four classes.** The effective prime weights \(|R|/(8c)\) are \(1/8\) for class \(1\) (and class \(5\)); \(1/8\) for class \(7\); and \(1/4+1/8\) for class \(3\) on even \(u\). Consequently all four leading coefficients are \(Z/8=\pi^2/48\) after substituting \(Y=3X/2+O(1)\). The class-\(1\) second coefficient is
\[
\frac{3}{16}\left[S_o\left(1-\log\frac32\right)+2T_o\right]
=-\frac{Z'}4+Z\left(\frac18+\frac{\log2}{24}-\frac{5\log3}{32}\right)=B.
\]
Class \(5\) has the same coefficient because it exchanges one prime class of density \(1/8\) for another. Class \(7\) introduces an additional \(\log2\) inside \(\log(cu^2)\), giving an increment of \((Z/8)\log2\). Class \(3\) combines three-eighths of the even-square weight, including one-eighth with \(c=2\); inserting \(S_e,T_e\) gives the increment \((3Z/8)\log2\). This proves all four displayed formulas and the strict second-order ordering.

Finally, the difference between the class-\(1\) and class-\(5\) sums is exactly the difference of the prime counting functions for \(13\) and \(7\pmod{24}\), weighted by odd \(u^{-2}\), up to the negligible \(O(\sqrt Y)\) exceptional contributions. The fixed-modulus prime number theorem gives \(\pi_{13}(t)-\pi_7(t)=O_A(t/(\log t)^A)\) for every fixed \(A>0\). The preceding small/large \(u\) split yields \(N_1(X)-N_5(X)=O_A(X/(\log X)^A)\). This completes the proof.

## Verification

The standalone `verify.py` uses integer arithmetic to expand the generating function modulo \(4\) through weight \(1400\), verifies the exact prime-exponent characterization for all \(700\) positive odd indices in that range, and cross-checks two independent constructions of the exceptional sets for the \(20000\) odd indices at most \(40000\). It reports the exact residue counts \(899,1138,893,954\) in the residue order \(1,3,5,7\). These finite checks corroborate arithmetic setup and residue splitting; the asymptotic formulas rely on the proof and the prime number theorem.

## Relationship to prior work

Banerjee and Ghosh Dastidar [1] prove the exact coefficient-congruence support used in Step 1 and establish arithmetic progressions of divisibility. Their Theorem 1.5 and corollaries do **not** state residue-class counts, a prime-number-theorem distribution, a second-order bias, or the all-logarithmic-order coincidence of classes \(1\) and \(5\). Bringmann and Lovejoy [2] establish generating functions, large-\(n\) coefficient-size asymptotics, and congruences; their coefficient asymptotics concern \(\mathrm{ou}^{*}(n)\) itself, not the frequency of its value \(2\pmod4\). He and Liu [3] study rank/shape distributions for odd unimodal sequences, a different measure and statistic. The prime-counting estimates here are classical; the new arithmetic output is the explicit combination of prime-square densities and the resulting bias.

## Limitations

Only **odd** indices with coefficient congruent to \(2\pmod4\) are counted; the result makes no assertion about even indices, other coefficient residues or moduli, or asymptotics of coefficient magnitudes. Its proof depends on the published exact support theorem [1]; it does not reprove that theorem. The special-index count has an \(O(X/(\log X)^3)\) two-term remainder, so finite thresholds for the ordering are not supplied. The priority assessment is a same mathematical model literature comparison, not independent mathematical validation; a general prime-square counting theorem might yield the constants after a specialization that has not been identified.

## References

1. K. Banerjee and M. Ghosh Dastidar, *Conguences for Odd Unimodal Sequences and a Problem of Bringmann And Lovejoy*, arXiv:2610.20135v1 (first public October 14, 2026), especially Theorem 1.5, Corollaries 1.6–1.8, and Section 4. https://arxiv.org/abs/2610.20135
2. K. Bringmann and J. Lovejoy, *Odd unimodal sequences*, arXiv:2308.11556v1 (August 22, 2023), especially Theorems 1.3–1.5, Proposition 6.1, and Theorem 6.2. https://arxiv.org/abs/2308.11556
3. B. He and G. Liu, *Asymptotic Statistics of Odd Unimodal Sequences: Rank Distributions and Probabilistic Structures*, arXiv:2605.06459v1 (May 7, 2026), introduction and rank/shape theorems. https://arxiv.org/abs/2605.06459
4. Classical prime number theorem in arithmetic progressions for fixed modulus \(24\), with a de la Vallée Poussin-type error bound; standard fixed-modulus corollary of zero-free regions for Dirichlet \(L\)-functions.
