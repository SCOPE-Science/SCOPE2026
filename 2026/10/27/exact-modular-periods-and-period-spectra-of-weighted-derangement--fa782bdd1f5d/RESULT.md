# Exact modular periods and period spectra of weighted derangement polynomials

## Finding
For each integer \(u\), let
\[
R_n(u)=\sum_{\pi\in S_n}(1+u)^{\operatorname{fix}(\pi)}
       =\sum_{j=0}^{n}\frac{n!}{j!}u^j,\qquad n\geq0.
\]
The convention for the empty permutation gives \(R_0(u)=1\). These are the classical derangement (rencontres) polynomials evaluated at \(1+u\).

**Exact least-period theorem.** For every integer modulus \(m\geq2\) and every integer \(u\) with \(\gcd(u,m)=1\), the least positive integer \(T\) satisfying
\[
R_{n+T}(u)\equiv R_n(u)\pmod m\quad\text{for every integer }n\geq0
\]
is exactly
\[
\boxed{T_m(u)=\operatorname{lcm}\bigl(m,\operatorname{ord}_m(u)\bigr).}
\]
Here \(\operatorname{ord}_m(u)\) is the multiplicative order of \(u\) in \((\mathbb Z/m\mathbb Z)^\times\).

**Complete fixed-modulus period spectrum.** Let \(\lambda(m)\) be the Carmichael exponent of \((\mathbb Z/m\mathbb Z)^\times\), and put
\[
q_m=\frac{\lambda(m)}{\gcd(\lambda(m),m)}.
\]
When \(u\) ranges through all invertible residues modulo \(m\), the distinct least periods are precisely
\[
\boxed{\{\,m d:d\mid q_m\,\}.}
\]
Every displayed period is attained. In particular the minimum is \(m\), the maximum is \(\operatorname{lcm}(m,\lambda(m))\), and the number of distinct periods is the divisor-counting function \(\tau(q_m)\).

For ordinary derangements \(D_n=R_n(-1)\), the least period modulo \(m\) is exactly \(m\) when \(m\) is even and exactly \(2m\) when \(m\) is odd. For example, modulo \(15\), the fixed-point weights \(1+u\) with \(u=1,4,2\), respectively, produce least periods \(15,30,60\); these are all the possible least periods for unit parameters modulo \(15\).

## Assumptions and scope
The theorem is about the entire infinite sequence indexed by \(n\geq0\), not just eventual periodicity. Both parameters are integers, \(m\geq2\), and the parameter \(u\) is a unit modulo \(m\). The order \(\operatorname{ord}_m(u)\) and Carmichael exponent \(\lambda(m)\) are defined only for units or their group. The nonunit case is not classified here. The assertion is about evaluated integer polynomials modulo \(m\), not coefficientwise polynomial periodicity.

The first equality defining \(R_n(u)\) follows by expanding \((1+u)^{\operatorname{fix}(\pi)}\) and counting permutations fixing a prescribed subset. Thus the object is the ordinary fixed-point enumerator; at \(u=-1\) only fixed-point-free permutations contribute.

## Proof
**Step 1: recurrence and initial block.** Writing \(R_n(u)=\sum_{j=0}^n (n!/j!)u^j\), separate the last summand to obtain
\[
R_n(u)=nR_{n-1}(u)+u^n\qquad(n\geq1),\qquad R_0(u)=1.
\]
For any \(m\geq2\), every summand of \(R_m(u)\) except the last contains the factor \(m\); hence
\[
R_m(u)\equiv u^m\pmod m.
\]
Induction on \(n\), using the recurrence first at \(m+n\) and then at \(n\), proves the exact shift congruence
\[
\boxed{R_{m+n}(u)\equiv u^mR_n(u)\pmod m\quad(n\geq0).}
\]
The shift identity holds even when \(u\) is not a unit. Iterating it gives
\(R_{n+km}(u)\equiv u^{km}R_n(u)\pmod m\) for all integers \(k,n\geq0\).

**Step 2: a period exists.** If \(\gcd(u,m)=1\), set \(h=\operatorname{ord}_m(u)\) and \(T=\operatorname{lcm}(m,h)\). Then \(T=km\) for a positive integer \(k\) and \(u^T\equiv1\pmod m\). Step 1 implies \(R_{n+T}(u)\equiv R_n(u)\pmod m\) for every \(n\geq0\).

**Step 3: no shorter period exists.** Suppose an arbitrary positive \(P\) is a period of the entire sequence. Subtracting the recurrences at indices \(n+P\) and \(n\) yields
\[
P R_{n-1}(u)\equiv u^n(1-u^P)\pmod m\qquad(n\geq1).
\]
At \(n=1\), since \(R_0(u)=1\), this reads \(P\equiv u(1-u^P)\pmod m\). At \(n=2\), since \(R_1(u)=1+u\), it reads \(P(1+u)\equiv u^2(1-u^P)\pmod m\). Multiplying the first congruence by \(1+u\) and subtracting the second gives
\[
u(1-u^P)\equiv0\pmod m.
\]
Because \(u\) is a unit, \(u^P\equiv1\pmod m\), and the first congruence then forces \(P\equiv0\pmod m\). Consequently \(h\mid P\) and \(m\mid P\), so \(\operatorname{lcm}(m,h)\mid P\). Combined with Step 2, this proves the least-period formula. Note that neither subtraction divided by a possibly nonunit quantity.

**Step 4: the period spectrum.** The unit group \(G=(\mathbb Z/m\mathbb Z)^\times\) is finite abelian and has exponent \(\lambda(m)\). It therefore contains an element of order \(\lambda(m)\); its powers realize every positive divisor \(h\mid\lambda(m)\). Conversely every element order divides \(\lambda(m)\). The periods from Steps 2--3 are \(\operatorname{lcm}(m,h)\) for precisely those divisors \(h\). For each prime \(\ell\), the exponent of \(\ell\) in the ratio \(\operatorname{lcm}(m,h)/m\) can be any integer from \(0\) through \(\max\{0,\nu_\ell(\lambda(m))-\nu_\ell(m)\}\). Therefore the ratios run through exactly the positive divisors of \(q_m\). This proves the spectrum, extrema, and count.

**Step 5: the derangement specialization.** For \(u=-1\), \(\operatorname{ord}_m(-1)=1\) if \(m=2\), and is \(2\) otherwise. Thus \(T_m(-1)=\operatorname{lcm}(m,2)\), equal to \(m\) for even \(m\) and \(2m\) for odd \(m\).

## Verification
The standalone standard-library program `verify.py` implements the recurrence modulo \(m\), obtains multiplicative orders by independent modular multiplication, checks all proper divisors of the predicted least period for mismatches, and constructs period spectra directly from all unit parameters. For every integer modulus \(2\leq m\leq50\), it verifies every unit-parameter residue. It also independently enumerates all permutations for \(0\leq n\leq7\) and seven integer values of \(u\), comparing weighted fixed-point sums with the recurrence.

On execution, it reports `VERIFY_OK: 773 coprime parameter/modulus combinations; 271888 shift comparisons; 5908 proper-divisor obstructions; 49 full modular period spectra; 56 direct weighted-permutation sums; maximum checked least period 2162`. This is finite evidence, not a proof of the universal statement; Steps 1--5 supply the infinite proof.

## Relationship to prior work
Sun, Wu, and Zhuang (first publicly posted September 15, 2010; arXiv:1009.2929v1) define the same derangement polynomials \(\mathcal D_n(x)\), give \(\mathcal D_n(x)=n\mathcal D_{n-1}(x)+(x-1)^n\), and establish congruences involving Bell and derangement polynomials. Their Corollary 3.2 includes \(D_{pn+r}\equiv(-1)^nD_r\pmod p\) for ordinary derangements and prime \(p\). These definitions and prime-modulus upper-period congruences are acknowledged inputs, not new claims. The inspected paper does not state the least-period theorem for unit evaluations modulo all integers or classify its fixed-modulus period spectrum.

OEIS A000166 includes Peter Bala's November 21, 2017 observation that the derangement sequence has a period dividing \(m\) for even \(m\), or \(2m\) for odd \(m\); that is an upper-period statement, and it does not assert least periods or address nontrivial fixed-point weights. The specialization here establishes sharpness, while the general theorem gives the arithmetic unit-order law and exact possible period spectrum. Searches for formulations in terms of Charlier / rencontres / derangement polynomials and modular minimal periods located no stronger explicit coverage; this is evidence of a literature gap, not proof of novelty.

## Limitations
The classification is restricted to invertible \(u\) modulo \(m\). Nonunit evaluations may exhibit a transient and are not covered. No equidistribution of residues, bounds on the frequencies of individual values, or minimal-period formulas for other permutation statistics are claimed. Although the proof is elementary, a general theorem in unlocated literature on polynomially recursive sequences could subsume the exact-period statement; independently check before any novelty-dependent publication claim.

## References
1. Y. Sun, X. Wu, J. Zhuang, *Congruences on the Bell polynomials and the derangement polynomials*, arXiv:1009.2929v1, first posted 2010-09-15, https://arxiv.org/abs/1009.2929 .
2. OEIS Foundation, *A000166: Subfactorial or rencontres numbers, or derangements*, comment by P. Bala dated 2017-11-21 concerning modular upper periods, https://oeis.org/A000166 .
