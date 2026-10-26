# Rare giant jumps create a remote sub-gamma optimizer despite convergent low cumulants

## Finding
Fix a real exponent \(\varkappa>4\) and an intensity \(\lambda>0\). Define \(q_b=b^{-\varkappa}\), with \(b>1\). Consider a compound-Poisson variable \(X_b\) centered by its mean, with rate \(\lambda\) and iid positive jumps \(J_b\) taking the values \(1\) and \(b\) with probabilities \(1-q_b\) and \(q_b\). Fix the variance proxy at the actual variance \(V_b=\lambda\mathbb E[J_b^2]\), and denote the least admissible right sub-gamma scale by \(c_*(X_b)\).

**Theorem.** As \(b\to\infty\),
\[
c_*(X_b)\sim\frac{b}{(\varkappa-2)\log b}.
\]
For each integer \(m\) with \(2\le m<\varkappa\), its cumulant of order \(m\) tends to \(\lambda\), matching the unit-jump centered Poisson law. Nevertheless, for all sufficiently large \(b\), the variational scale profile has negative right derivative at the origin and a superior interior maximum; consequently it has at least two distinct positive stationary points. If the mixing probability \(q\) varies from zero to \(b^{-\varkappa}\) with \(b\) fixed and sufficiently large, there is a critical \(q_c(b)\in(0,b^{-\varkappa})\) at which the origin and a strictly positive argument both globally maximize the profile, although the origin remains strictly locally maximizing throughout the interval. No uniqueness of the critical probability or of interior maximizers is asserted.

## Assumptions and scope
For a centered random variable with variance \(V>0\), a right sub-gamma scale \(c\ge0\) with its **true variance proxy** means
\[
\log\mathbb E e^{tX}\le\frac{Vt^2}{2(1-ct)}\qquad(0\le t<1/c),
\]
with \(1/0=\infty\). The theorem concerns only the minimum \(c_*\) at this fixed variance proxy, not optimization over larger proxies. The jump size \(b\) is a real parameter, not necessarily an integer. All moment-generating functions are finite at every finite real argument for each fixed \(b\). The Poisson rate \(\lambda\) is arbitrary but fixed; it cancels from the normalized scale.

For \(0\le q\le1\), define \(A=1-q+qb^2\), \(B=1-q+qb^3\), \(C=1-q+qb^4\), and
\[
U\sim\operatorname{Beta}(1,2),\quad
L(z)=\mathbb E e^{zU}=\frac{2(e^z-1-z)}{z^2},\quad L(0)=1.
\]
The canonical remainder moment-generating function and profile are
\[
M_{q,b}(t)=\frac{(1-q)L(t)+qb^2L(bt)}{A},\qquad
\Psi_{q,b}(t)=\frac{1-M_{q,b}(t)^{-1}}{t}\quad(t>0).
\]
The continuous origin value is \(\Psi_{q,b}(0)=B/(3A)\). The variational theorem of Chen establishes \(c_*(X)=\sup_{t>0}\Psi_{q,b}(t)\); we use this published identity as a premise and prove the new asymptotic and phase assertions below.

## Proof
**1. Exact profile and cumulants.** Centering the compound Poisson sum gives
\[
K_{q,b}(t)=\lambda[(1-q)(e^t-1-t)+q(e^{bt}-1-bt)].
\]
Thus \(V=\lambda A\) and \(2K_{q,b}(t)/(Vt^2)=M_{q,b}(t)\), as above. For every integer \(m\ge2\), the cumulant is \(\lambda(1-q+qb^m)\). Substituting \(q=b^{-\varkappa}\) yields \(\lambda[1-b^{-\varkappa}+b^{m-\varkappa}]\to\lambda\) whenever \(m<\varkappa\). There is no claim of convergence for order \(m\ge\varkappa\).

**2. Sharp rare-jump scale.** Write \(q=b^{-\varkappa}\) and \(A_b=1-b^{-\varkappa}+b^{2-\varkappa}\to1\). Since \(U\in[0,1]\) and \(\mathbb E U=1/3\),
\[
0\le L(z)-1=\mathbb E(e^{zU}-1)\le ze^z/3\qquad(z\ge0).
\]
Since \(M_{q,b}\ge1\), for all \(t>0\),
\[
0\le\Psi_{q,b}(t)\le\min\left\{\frac1t,\frac{e^t+qb^3e^{bt}}{3A_b}\right\}.
\]
Fix \(\varepsilon\) with \(0<\varepsilon<\varkappa-2\), and let \(s_-=\varkappa-2-\varepsilon\). For \(0<t\le s_-\log b/b\), the second bound is \(O(1+b^{1-\varepsilon})=o(b/\log b)\), uniformly in \(t\). For \(t\ge s_-\log b/b\), the first bound gives \(\Psi_{q,b}(t)\le b/(s_-\log b)\). Therefore
\[
\limsup_{b\to\infty}\frac{c_*(X_b)\log b}{b}\le\frac1{\varkappa-2-\varepsilon}.
\]
For the reverse inequality, set \(s_+=\varkappa-2+\varepsilon\) and \(t_b=s_+\log b/b\). The rare-jump contribution alone gives
\[
M_{q,b}(t_b)\ge\frac{2b^{-\varkappa}(e^{bt_b}-1-bt_b)}{A_b t_b^2}
\sim\frac{2b^{\varepsilon}}{s_+^2(\log b)^2}\longrightarrow\infty.
\]
Hence \(\Psi_{q,b}(t_b)\sim1/t_b\) and
\[
\liminf_{b\to\infty}\frac{c_*(X_b)\log b}{b}\ge\frac1{\varkappa-2+\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) on both sides proves the asymptotic. No asymptotic statement about a unique maximizing argument is needed.

**3. Strict local control is not global control.** The Taylor coefficients of \(L\) give
\[
M_{q,b}(t)=1+\frac{B}{3A}t+\frac{C}{12A}t^2+O_{q,b}(t^3),\qquad
\Psi_{q,b}'(0)=\frac{3AC-4B^2}{36A^2}.
\]
Uniformly for \(0\le q\le b^{-\varkappa}\), the three quantities \(A,B,C\) tend to one as \(b\to\infty\): this uses \(\varkappa>4\). Consequently \(\Psi'_{q,b}(0)\to-1/36\) uniformly. For all large \(b\), the origin is a strict local maximum for every mixing probability in that interval. At its right endpoint \(q=b^{-\varkappa}\), Part 2 gives \(c_*\to\infty\), whereas \(\Psi(0)=B/(3A)\to1/3\). Hence an interior argument strictly exceeds the origin. For each fixed \(b\), \(\Psi(t)\to0\) as \(t\to\infty\) because \(0\le\Psi(t)\le1/t\), and \(\Psi\) is analytic for \(t>0\). Its maximum is therefore attained at some finite positive \(t\). A negative derivative near zero followed by a superior interior peak forces at least two distinct positive zeros of \(\Psi'\), one along its descent-to-ascent transition and one at the peak (by the extreme value theorem and Fermat's rule).

**4. Coexistence at a remote onset.** Fix such a sufficiently large \(b\), and now vary \(q\in[0,b^{-\varkappa}]\). At \(q=0\), \(M=L\) and
\[
L(t)=\sum_{n\ge0}\frac{2t^n}{(n+2)!}\quad\text{with}\quad\frac2{(n+2)!}\le3^{-n},
\]
where equality holds only for \(n=0,1\). Thus \(L(t)<(1-t/3)^{-1}\) when \(0<t<3\), implying \(\Psi_{0,b}(t)<1/3=\Psi_{0,b}(0)\). For \(t\ge3\), \(\Psi_{0,b}(t)<1/t\le1/3\). The origin is therefore the **unique** global maximizer at \(q=0\).

For all \(q\) in the specified interval, \(\Psi_{q,b}(0)=B/(3A)\ge1/3\), whereas \(\Psi_{q,b}(t)\le1/t\le1/4\) for \(t\ge4\). Thus every global maximizing argument is in \([0,4]\). The extended profile is jointly continuous in \((q,t)\) on the compact rectangle \([0,b^{-\varkappa}]\times[0,4]\), and its origin derivative is strictly negative, uniformly over the same probability interval. There is consequently \(\delta>0\) such that \(\Psi_{q,b}(t)<\Psi_{q,b}(0)\) for every \(0<t\le\delta\) and all these \(q\). At \(q=0\) strict inequality also holds for every \(t\in[\delta,4]\), uniformly by compactness. Continuity shows this strict global origin control persists for all sufficiently small positive \(q\).

Define
\[
h_b(q)=\max_{0\le t\le4}\Psi_{q,b}(t)-\Psi_{q,b}(0),\qquad
q_c(b)=\inf\{q\in[0,b^{-\varkappa}]:h_b(q)>0\}.
\]
The function \(h_b\) is continuous, nonnegative, zero near zero, and strictly positive at \(q=b^{-\varkappa}\). Therefore \(0<q_c(b)<b^{-\varkappa}\) and \(h_b(q_c)=0\). Choose \(q_n\to q_c\) from the nonempty set where \(h_b(q_n)>0\), and choose maximizing \(t_n\in[\delta,4]\). A subsequence tends to \(t_c\in[\delta,4]\). By continuity, \(\Psi_{q_c,b}(t_c)=\Psi_{q_c,b}(0)\), and both attain the global maximum, while the uniform negative derivative preserves the origin as a strict local maximum. This proves coexistence and the discontinuous change in possible maximizing arguments, without asserting a unique global branch or any monotonicity of \(h_b\).

## Verification
The auxiliary standalone script `verify_rare_jump.py` separately reconstructs the \(\operatorname{Beta}(1,2)\) MGF coefficients with exact fractions, confirms exact low-order cumulant identities, verifies negative origin derivatives, and evaluates explicit interior witnesses at four finite jump sizes for the exponent \(\varkappa=5\). The analytic asymptotic bounds and compactness argument, not any finite numerical search, establish the statements for all sufficiently large real \(b\). Running `python verify_rare_jump.py` requires only Python's standard library.

## Relationship to prior work
Chen (arXiv:2610.00032v1, first public 2026-09-02) proves the canonical remainder variational formula, the equilibrium jump interpretation, and an interior-maximizing **single fixed** two-point example with jumps \(1\) and \(5\). Chen and Wang (arXiv:2609.02590v1, first public 2026-09-02) derive a rare-adverse-jump law for **signed** unit Skellam jumps, where the right optimal scale decays as the rare-jump probability tends to zero. Their companion feasible-frontier paper (arXiv:2609.23069v1, first public 2026-09-19) analyzes the effect of **relaxing the variance proxy for a fixed law**, and repeats the fixed \(1,5\) example. None of those inspected results states the present joint regime of **increasing positive jump magnitude, shrinking contamination probability, unchanged low cumulants and a remote, locally stable phase coexistence**. The exact variational formula itself is prior work and is not claimed as new.

## Limitations
This result fixes the variance proxy at the true variance and the Poisson intensity at a positive constant. It gives first-order growth of the least scale, not a second-order expansion of the optimizing argument or a sharp numerical value of the onset probability \(q_c(b)\). The presence of at least two stationary points does not imply there are exactly two. The coexistence threshold is defined as the first onset of interior superiority; no global monotonicity in \(q\) is claimed. Its distinctness from prior named sources is based on explicit implication comparisons; historical priority cannot be settled from database searches alone. No independent validation is claimed.

## References
1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public 2026-09-02), https://arxiv.org/abs/2610.00032. Relevant: Theorems 2.1 and 3.1, Section 6, and Section 7.2.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1 (first public 2026-09-02), https://arxiv.org/abs/2609.02590. Relevant: Sections 6--7.
3. Y. Chen and X. Wang, *Feasible Frontiers for Sub-Gamma Envelopes: the Variance--Pole Trade-off for Infinitely Divisible Laws*, arXiv:2609.23069v1 (first public 2026-09-19), https://arxiv.org/abs/2609.23069. Relevant: Theorem 3.3, Section 5 and Example 7.8.
