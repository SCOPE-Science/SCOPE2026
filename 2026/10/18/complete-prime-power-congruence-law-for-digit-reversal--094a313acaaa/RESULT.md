# Complete prime-power congruence law for digit reversal

## Finding

Fix any integer base \(b\ge2\). Sample \(N_\ell\) uniformly from the \((b-1)b^{\ell-1}\) positive integers with exactly \(\ell\) base-\(b\) digits, and let \(R_b(n)\) be the integer formed by reversing those digits, allowing initial zeros in the reversed digit string. Set \(G_\ell=\gcd(N_\ell,R_b(N_\ell))\). For every prime \(p\) and integer \(a\ge1\), the limit \(F_{b,p}(a)=\lim_{\ell\to\infty}\Pr(p^a\mid G_\ell)\) exists, with the following complete classification:

\[
F_{b,p}(a)=
\begin{cases}
p^{-2a+\min(a,\nu_p(b^2-1))},&p\nmid b,\\[4pt]
\dfrac{b/p^{\min(a,\nu_p(b))}-1}{b-1}\,p^{-2a+\min(a,\nu_p(b))},&p\mid b.
\end{cases}
\]

The formula in the second line holds **exactly at every length** \(\ell\ge2\lceil a/\nu_p(b)\rceil\), without taking a limit. The first line has exponential-in-length convergence for fixed \(b,p,a\).

More precisely, when \(p\nmid b\), put \(q=p^a\) and \(u=\min(a,\nu_p(b^2-1))\). Then the normalized pair
\[
\bigl(N_\ell,\,b^{-(\ell-1)}R_b(N_\ell)\bigr)\pmod q
\]
converges exponentially to the **uniform distribution** on
\[
S_{b,p,a}=\{(x,y)\in(\mathbb Z/q\mathbb Z)^2:y\equiv x\pmod{p^u}\},
\qquad |S_{b,p,a}|=p^{2a-u}.
\]
Here the inverse power is taken modulo \(q\), and \(p^0=1\). Every finite-length pair already lies in this subgroup. In particular, the dependence between the two congruences is completely controlled by \(\nu_p(b^2-1)\), rather than by a heuristic independence assumption.

As a distributional consequence, if \(p\nmid b\), \(\tau=\nu_p(b^2-1)\), and \(W_\ell=\nu_p(G_\ell)\), then for each fixed integer \(t\ge0\)
\[
\lim_{\ell\to\infty}\Pr(W_\ell=t)=
\begin{cases}
(1-p^{-1})p^{-t},&0\le t<\tau,\\
(1-p^{-2})p^{\tau-2t},&t\ge\tau.
\end{cases}
\]
Thus the valuation tail changes from geometric ratio \(p^{-1}\) to \(p^{-2}\) at the sharp threshold \(\tau\).

## Assumptions and scope

All bases \(b\) are fixed integers at least two, all primes \(p\) and prime-power exponents \(a\) are fixed, and the digit length \(\ell\) tends to infinity. Sampling is uniform among integers with **exactly** \(\ell\) digits. The standard definition \(\nu_p(m)\) is the exponent of \(p\) in the nonzero integer \(m\). Reversed leading zeros are harmless because the congruences concern the resulting integer. Statements for \(p\nmid b\) and \(p\mid b\) are separate and cover all primes. No claim is made that different prime-power events have independent limits or that \(G_\ell\) has a global limiting distribution.

## Proof

**1. A normalized linear digit process when \(p\nmid b\).** Write the canonical digits as \(N_\ell=\sum_{j=0}^{\ell-1}d_jb^j\), with independent \(d_j\) uniform in \(\{0,\ldots,b-1\}\) for \(j<\ell-1\) and independent leading digit \(d_{\ell-1}\) uniform in \(\{1,\ldots,b-1\}\). As \(b\) is invertible modulo \(q=p^a\),
\[
\bigl(N_\ell,b^{-(\ell-1)}R_b(N_\ell)\bigr)
\equiv\sum_{j=0}^{\ell-1}d_j(b^j,b^{-j})\pmod q.
\]
Let \(v_j=(b^j,b^{-j})\) modulo \(q\). Since \(b^{2j}-1\) is divisible by \(b^2-1\), the difference of the two coordinates of every \(v_j\) is divisible by \(p^u\), where \(u=\min(a,\nu_p(b^2-1))\). Hence all sums belong to \(S_{b,p,a}\).

**2. Exact subgroup generation.** Both \(v_0=(1,1)\) and \(v_1=(b,b^{-1})\) belong to the generated subgroup. The difference \(v_1-b^{-1}v_0=(b-b^{-1},0)\) has first coordinate a unit multiple of \(p^u\) modulo \(p^a\). Consequently \(v_0,v_1\) generate every diagonal pair \((z,z)\) and every pair \((p^u w,0)\); their sum is precisely the displayed subgroup \(S_{b,p,a}\). It follows immediately that \(|S_{b,p,a}|=p^{2a-u}\). This argument works also when \(u=a\), in which case \(v_1\) is redundant and the subgroup is diagonal.

**3. Exponential uniformization.** Let \(T=\operatorname{ord}_{q}(b)\). The sequence of vectors \(v_j\) is periodic modulo \(q\) with period \(T\). For \(T>1\), the vectors \(v_0,v_1\) occur among the independent unrestricted digits at least \(\lfloor(\ell-1)/T\rfloor-1\) times each; when \(T=1\), \(v_0\) alone generates the subgroup and occurs at every position. For any nontrivial additive character \(\chi\) of \(S_{b,p,a}\), at least one of \(\chi(v_0)\) and \(\chi(v_1)\) is nontrivial. A uniform digit \(d\in\{0,\ldots,b-1\}\) has average \(\frac1b\sum_{d=0}^{b-1}\chi(v_j)^d\) of modulus strictly less than one when \(\chi(v_j)\ne1\), since digits zero and one both occur. Finitely many characters imply a common contraction factor \(\rho_{b,q}<1\). Independence makes every nontrivial Fourier coefficient of the pair distribution \(O_{b,q}(\rho_{b,q}^{\lfloor(\ell-1)/T\rfloor-1})\); the one constrained leading digit contributes a factor of modulus at most one. Fourier inversion on the finite group gives uniform distribution on \(S_{b,p,a}\) with the stated exponential rate. In particular, the limiting probability of the single pair \((0,0)\) is \(|S_{b,p,a}|^{-1}=p^{-2a+u}\). Multiplication of the second coordinate by \(b^{\ell-1}\), a unit, fixes the zero pair, so this is the common-divisibility probability for the unnormalized reversal as well.

**4. Exact finite-length law when \(p\mid b\).** Put \(e=\nu_p(b)\ge1\), \(h=\lceil a/e\rceil\), and \(t=\min(a,e)\). Because \(p^a\mid b^h\), the residue \(N_\ell\pmod{p^a}\) depends only on its \(h\) least significant digits, whereas \(R_b(N_\ell)\pmod{p^a}\) depends only on its \(h\) most significant digits. When \(\ell\ge2h\), these digit blocks are independent. The low block is uniform in a complete range of \(b^h\) integers, a multiple of \(p^a\), so \(\Pr(p^a\mid N_\ell)=p^{-a}\).

Let \(d\in\{1,\ldots,b-1\}\) be the leading digit. In the reversed integer it is the lowest digit. If \(a\le e\), divisibility of the reverse by \(p^a\) means exactly \(p^a\mid d\), which has probability \((b/p^a-1)/(b-1)\). If \(a>e\), divisibility first forces \(p^e\mid d\), with probability \((b/p^e-1)/(b-1)\). Conditional on this, divide the remaining congruence by \(p^e\); the next \(h-1\) leading-block digits form an integer uniform modulo \(p^{a-e}\), because \(b^{h-1}\) is a multiple of \(p^{a-e}\) and \(b/p^e\) is invertible there. The conditional probability is \(p^{-(a-e)}\). Combining these two cases gives \(\Pr(p^a\mid R_b(N_\ell))=((b/p^t-1)/(b-1))p^{-(a-t)}\). Independence of the blocks yields the second line of the theorem.

**5. Valuation law.** When \(p\nmid b\), let \(F_{b,p}(0)=1\). For each \(t\ge0\), \(\Pr(\nu_p(G_\ell)=t)=\Pr(p^t\mid G_\ell)-\Pr(p^{t+1}\mid G_\ell)\). Taking the two proven fixed-exponent limits and subtracting gives the stated two-phase distribution, including the boundary \(t=\tau\). This completes the proof.

## Verification

The accompanying `verify_reversal_local.py` executes exact, integer-based enumeration for ten prime-power cases with \(p\mid b\) at and above the stabilization length. For twelve further cases with \(p\nmid b\), it enumerates the image of the two-generator modular map and verifies equality with the announced subgroup and its size. An independent exact modular dynamic program checks the joint-congruence distribution and its convergence to the theoretical mass at \((0,0)\) in four instances. The program uses rational arithmetic for probabilities; its finite checks corroborate, but do not replace, the Fourier proof for unbounded \(\ell\).

For the decimal base, examples of the exact limiting probabilities are \(F_{10,3}(3)=1/81\), \(F_{10,11}(2)=1/1331\), \(F_{10,2}(1)=2/9\), and \(F_{10,5}(1)=1/45\).

## Relationship to prior work

OEIS A055483, first listed in 2000, defines and tabulates exactly \(\gcd(n,R_{10}(n))\) and records the decimal implications \(3\mid n\Rightarrow3\mid\gcd(n,R_{10}(n))\) and \(9\mid n\Rightarrow9\mid\gcd(n,R_{10}(n))\). The record does not state a limiting local valuation law or a joint congruence subgroup theorem. OEIS A161825 tabulates the binary analogue without such a limiting theorem. Banks, Hart, and Sakata (2004) prove equidistribution statements for *palindromic integers* in residue classes, subject to restrictions involving \(b(b^2-1)\). Their objects are integers already fixed by digit reversal, rather than joint congruences for arbitrary integers and their reversals. Dartyge, Martin, Rivat, Shparlinski, and Swaenepoel (2023) study joint divisibility of *binary* integers and their reversals as part of sieve estimates for reversible primes and squarefree pairs. Their Theorem 1.4 includes the factor \(22/27\) for joint squarefreeness at the prime three; this contains a single local prime-square consequence compatible with the present formula. Their explicitly stated sieve count and squarefree-modulus estimates do not supply the all-base, arbitrary-prime-power congruence subgroup classification or the sharp \(p\mid b\) stabilization formula. These sources establish strong antecedents, and the present statement does not claim priority for any local special case that follows from them.

## Limitations

The theorem gives fixed-prime-power local laws and a fixed-length cutoff for primes dividing the base; it does not establish the global density of relatively prime reversal pairs, an asymptotic count with growing modulus, uniformity as \(p\) or \(a\) increases with digit length, or independence across primes. Existing local squarefree factors may be known in particular bases. An unindexed or implicit generalization in earlier work cannot be excluded without independent literature review.

## References

1. OEIS Foundation, *A055483: GCD of n and its digit reversal*, initial author E. Friedman, 2000-06-27, https://oeis.org/A055483.
2. OEIS Foundation, *A161825: GCD of n and its binary reversal*, initial author L. Quet, 2009-06-20, https://oeis.org/A161825.
3. W. D. Banks, D. N. Hart, and M. Sakata, *Almost All Palindromes Are Composite*, arXiv:math/0405056v1, publicly posted 2004-05-04, https://arxiv.org/pdf/math/0405056.
4. C. Dartyge, B. Martin, J. Rivat, I. E. Shparlinski, and C. Swaenepoel, *Reversible primes*, arXiv:2309.11380v1, publicly posted 2023-09-20, https://arxiv.org/pdf/2309.11380; see especially Theorem 1.4 and Section 5.
