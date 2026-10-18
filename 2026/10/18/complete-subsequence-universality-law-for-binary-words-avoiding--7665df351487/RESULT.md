# Complete subsequence-universality law for binary words avoiding triple runs

## Finding

A binary word is *run-two constrained* if it contains neither \(000\) nor \(111\) as a contiguous factor. Let \(\mathcal L_n\) denote all such words of length \(n\), including the empty word when \(n=0\). For a binary word \(w\), the *subsequence-universality index* \(I(w)\) is the largest integer \(k\ge0\) such that every binary word of length \(k\) occurs as an order-preserving, not necessarily contiguous, subsequence of \(w\). Write

\[A_{n,k}=\#\{w\in\mathcal L_n:I(w)=k\}.\]

**Complete counting law (all integers \(n,k\ge0\)).**

\[\boxed{\sum_{n,k\ge0}A_{n,k}t^nu^k=\frac{1+2t+2t^2+ut^3}{1-u(2t^2+t^3)}.}\]

Thus, with \([t^j]\) interpreted as zero for \(j<0\), the exact coefficients are

\[A_{n,k}=[t^{n-2k}](1+2t+2t^2)(2+t)^k+\mathbf1_{k\ge1}[t^{n-2k-1}](2+t)^{k-1}.\]

The sharp deterministic range for every \(n\ge0\) is

\[\boxed{\min_{w\in\mathcal L_n}I(w)=\lfloor n/3\rfloor,\qquad\max_{w\in\mathcal L_n}I(w)=\lfloor n/2\rfloor.}\]

**Limit law.** Let \(W_n\) be uniformly sampled from \(\mathcal L_n\) and define

\[\mu=\frac1{\sqrt5},\qquad \sigma^2=1-\frac{11\sqrt5}{25}>0.\]

Then \(\mathbb E I(W_n)=\mu n+O(1)\), \(\operatorname{Var}(I(W_n))=\sigma^2n+O(1)\), and

\[\frac{I(W_n)-\mu n}{\sigma\sqrt n}\ \xrightarrow{\mathrm d}\ N(0,1).\]

Equivalently, for each fixed real \(x\), if \(k_n=\lceil\mu n+x\sigma\sqrt n\rceil\), then

\[\lim_{n\to\infty}\Pr\{W_n\text{ is }k_n\text{-universal}\}=1-\Phi(x),\]

where \(\Phi\) is the standard normal cumulative distribution function.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\); subsequences are *scattered* (deletions may occur), whereas the forbidden triples are contiguous factors. The run bound applies to the entire word including its endpoints. All exact identities include \(n=0\) and \(k=0\). The probabilistic statements take \(n\to\infty\) and assume *uniform* sampling among all admissible length-\(n\) words, equivalently, independent fair bits conditioned on avoiding the forbidden triples. Nonuniform weighting of admissible words would define a different probability model.

The index equals the number of *greedy complete arches*: scan from left to right, increment the count whenever both letters have appeared since the last increment, then clear the set of seen letters. The equality follows from the standard arch-factorization characterization of scattered-subsequence universality (Barker et al., 2020; Adamson et al., 2023). One can also prove it directly: a concatenation of \(k\) full-letter arches contains every length-\(k\) subsequence; conversely the sequence of letters absent from the successive incomplete prefixes exhibits a missing subsequence of length one greater than the arch count.

## Proof

**1. Four-state exhaustive decomposition.** For a nonempty admissible partial word, remember two items: \(r\in\{1,2\}\), the length of its current constant suffix, and \(b\in\{0,1\}\), whether the incomplete greedy arch is empty or contains the last letter. Let \(F_{r,b}(t,u)\) be the ordinary generating series of admissible continuations, weighting each newly appended letter by \(t\), and each newly completed arch by an additional \(u\); the empty continuation contributes \(1\). If a letter equal to the last one is appended, this is allowed only for \(r=1\), and it puts the automaton in state \((2,1)\) without closing an arch. If the opposite letter is appended, the new run has size one; it either starts an incomplete arch when \(b=0\), or closes an arch and resets \(b=0\) when \(b=1\). These rules exhaust all admissible extensions, including extensions across arch boundaries, and yield

\[\begin{aligned}
F_{1,0}&=1+t(F_{1,1}+F_{2,1}),\\
F_{1,1}&=1+t(uF_{1,0}+F_{2,1}),\\
F_{2,0}&=1+tF_{1,1},\\
F_{2,1}&=1+tuF_{1,0}.
\end{aligned}\]

Eliminating \(F_{1,1}\) and \(F_{2,1}\) gives the *scalar* identity

\[F_{1,0}=1+2t+t^2+ut^2(2+t)F_{1,0},\]

hence

\[F_{1,0}=\frac{1+2t+t^2}{1-u(2t^2+t^3)},\qquad F_{1,1}=1+t+ut(1+t)F_{1,0}.\]

The empty word contributes \(1\), while a nonempty word begins with either binary letter and enters state \((1,1)\). Therefore

\[G(t,u)=1+2tF_{1,1}(t,u)=\frac{1+2t+2t^2+ut^3}{1-u(2t^2+t^3)},\]

proving the generating function. Extracting \(u^k\) by the geometric series expansion gives the stated explicit coefficient formula. Equivalently, for every \(n\ge4\),

\[\sum_k A_{n,k}u^k=u\left(2\sum_k A_{n-2,k}u^k+\sum_k A_{n-3,k}u^k\right),\]

with base polynomials \(1,\ 2,\ 2+2u,\ 6u\) for \(n=0,1,2,3\). Their sum at \(u=1\) is the usual count \(|\mathcal L_n|=2F_{n+1}\) for \(n\ge1\), with Fibonacci convention \(F_1=F_2=1\).

**2. Sharp deterministic bounds.** Each completed greedy arch contains at least two letters. Since the final incomplete arch has at most two equal letters, and every completed greedy arch contains at most three letters (the first run has length at most two and the first opposite symbol closes it), if there are \(k\) completed arches then

\[2k\le n\le3k+2.\]

Consequently \(\lfloor n/3\rfloor\le k\le\lfloor n/2\rfloor\). The alternating word of length \(n\) attains the maximum. Writing \(n=3m+r\) with \(r\in\{0,1,2\}\), the admissible word \((001)^m0^r\) has exactly \(m\) complete arches and attains the minimum (including \(m=0\)). Both bounds are sharp at all lengths.

**3. Gaussian law and sharp threshold.** Put \(P_n(u)=[t^n]G(t,u)\). For \(u\) in a complex neighborhood of \(1\), the denominator of \(G\) has a unique simple zero of smallest modulus \(t(u)=1/\lambda(u)\), where the analytic positive branch \(\lambda(u)\) satisfies

\[\lambda(u)^3=u(2\lambda(u)+1),\qquad\lambda(1)=\varphi=(1+\sqrt5)/2.\]

At \(u=1\), the other denominator roots are \(-1\) and \(-\varphi\), both strictly farther from the origin than \(1/\varphi\); the numerator does not vanish at \(1/\varphi\). Simple-root analytic continuation and a compact contour separating this root from the others imply, uniformly for \(u\) near \(1\),

\[P_n(u)=C(u)\lambda(u)^n(1+O(\theta^n)),\qquad 0<\theta<1,\]

for a nonzero analytic \(C(u)\). Since \(\Pr\{I(W_n)=k\}=A_{n,k}/P_n(1)\), the moment-generating function satisfies

\[\log\mathbb E e^{sI(W_n)}=n\bigl(\log\lambda(e^s)-\log\lambda(1)\bigr)+O(1)\]

locally uniformly in complex \(s\). Implicit differentiation of the displayed cubic gives

\[\frac{u\lambda'(u)}{\lambda(u)}=\frac{2\lambda(u)+1}{4\lambda(u)+3}.\]

Evaluating the first logarithmic derivative at \(u=1\) gives \(\mu=1/\sqrt5\); differentiating once more gives

\[\sigma^2=\left.\frac{2\lambda(u)(2\lambda(u)+1)}{(4\lambda(u)+3)^3}\right|_{u=1}=1-\frac{11\sqrt5}{25}>0.\]

The local analytic expansion, applied at \(s=it/(\sigma\sqrt n)\) and centered by \(\mu n\), makes the characteristic functions converge to \(e^{-t^2/2}\), proving the normal limit by the continuity theorem. Uniform analyticity also justifies differentiation of the error, proving the \(O(1)\) mean and variance remainders. The threshold follows by continuity of the Gaussian CDF and the fact that integer rounding changes the normalized threshold by at most \(1/(\sigma\sqrt n)\).

## Verification

The included Python 3 program `CHECK.py` (standard library only) independently checks actual scattered-subsequence universality by exhaustive pattern testing of every legal word for \(0\le n\le14\). It separately checks a four-state extension automaton against the scalar recurrence and the coefficient formula for \(0\le n\le120\), including finite-size extremal bounds. Run it with `python3 CHECK.py` from the extracted directory. It reports `ALL CHECKS PASSED` when these checks succeed. These finite tests corroborate but do not replace the infinite derivations above.

## Relationship to prior work

Barker et al. (2020) develop scattered-factor universality and arch factorization, supplying the interpretation of the index. Adamson et al. (2023), Section 4 and Theorem 26/Corollary 28, count \(k\)-universal words in arbitrary deterministic regular languages by general dynamic programming. Their full inspected version does **not** state the special rational two-variable law for the language excluding \(000\) and \(111\), nor the explicit limiting mean, strictly positive variance, or Gaussian threshold above. Those general algorithms could compute any fixed finite-length marginal but do not directly furnish these closed infinite-family identities. Unrestricted-binary formulas refer to a different language and do not imply the constrained counts. No assertion of absolute publication uniqueness is made.

## Limitations

All claims concern binary words with **both** length-three constant factors forbidden; no assertion extends without further work to larger alphabets, other run caps, or nonuniform probability distributions. Asymptotic normality does not assert an exact normal distribution at finite length. The coefficient identity is exact for all lengths, whereas computer enumeration is limited to the stated lengths. Although the specified literature and targeted searches found no equivalent statement, earlier unpublished, differently named or unindexed derivations remain possible. The exact asymptotic constants are not claimed for any other sampling law.

## References

1. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea and Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first posted March 10, 2020; sections 2 and 4. https://arxiv.org/html/2003.04629v1.
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea and Dirk Nowotka, *\(k\)-Universality of Regular Languages*, arXiv:2311.10658v1, first posted November 17, 2023; sections 2 and 4. https://arxiv.org/html/2311.10658v1.
