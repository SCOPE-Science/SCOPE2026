# Minority-letter enumeration and Gaussian law for circular antisquare-avoiding binary words

## Finding

A binary word \(w\) of length \(n\ge 1\) is **circularly good** if its bi-infinite periodic extension \(w^{\mathbb Z}\) contains no antisquare \(x\overline{x}\) with \(|x|\ge 2\), where \(\overline{x}\) exchanges zero and one. The two order-one antisquares \(01\) and \(10\) are permitted. Coordinates are labeled: different rotations are counted as different words unless their actual symbol strings coincide. Let \(C_{n,k}\) be the number of circularly good binary words with exactly \(k=\min(|w|_0,|w|_1)\) copies of their less frequent symbol. Then, for all \(n\ge1\), \(C_{n,0}=2\), and for all \(k\ge1\),

\[
C_{n,k}=2n\sum_{r=0}^{\lfloor k/2\rfloor}\frac{1}{k-r}\binom{k-r}{r}\binom{n-3k+r-1}{k-r-1},
\]

where the binomial term vanishes unless \(n-4k+2r\ge0\). Equivalently, the **complete joint generating function**, as a formal power series, is

\[
\boxed{\displaystyle \sum_{n\ge1}\sum_{k\ge0}C_{n,k}z^n u^k=\frac{2z(1+4uz^3+6u^2z^5)}{1-z-uz^4-u^2z^6}.}
\]

There is a structural classification: every nonconstant circularly good word has a unique minority symbol; its cyclic successive-occurrence gaps are all either \(2\) or at least \(4\), and no two successive gaps equal \(2\). Conversely every marked cyclic set of positions obeying these conditions, colored with a minority symbol against its opposite background, is circularly good. Thus \(C_{n,k}=0\) for \(k>n/3\); when \(n\ge6\) is divisible by \(6\), exactly \(12\) labeled words attain \(k=n/3\) (the shifts and complements of the period-six pattern \(101000\)).

In particular the total labeled cyclic count \(C_n=\sum_k C_{n,k}\) has generating function

\[
\sum_{n\ge1}C_nz^n=\frac{2z(1+4z^3+6z^5)}{1-z-z^4-z^6}.
\]

Let \(\psi>1\) be the real root of \(\psi^3=\psi^2+1\). Then

\[
C_n=2\psi^n+2(-1)^n+4\cos(n\pi/3)+O(\psi^{-n/2}).
\]

For a uniformly chosen circularly good length-\(n\) word, let \(K_n\) be its minority-symbol count. Write \(\rho=1/\psi\), \(F(z,u)=1-z-uz^4-u^2z^6\), and let \(\rho(u)\) be the positive solution of \(F(\rho(u),u)=0\) near \(u=1\). Then

\[
\frac{K_n-\mu n}{\sqrt{n}}\;\Longrightarrow\;\mathcal N(0,\sigma^2),\quad
\mu=-\frac{\rho'(1)}{\rho}=\frac{\rho^3+2\rho^5}{1+4\rho^3+6\rho^5}\approx0.1942540040,
\]

\[
\sigma^2=\mu+\mu^2-\frac{\rho''(1)}{\rho}\approx0.0495615175>0.
\]

## Assumptions and scope

All periodic factors are tested across wraparound and across arbitrarily many periods, not merely inside one displayed copy of \(w\). An antisquare has the precise form \(x\overline{x}\), not \(x\overline{x}^{\mathrm{rev}}\). The count is for labeled binary words, not necklaces; \(k\) counts whichever letter is less frequent and equals zero for the two constant words. The theorem applies to every \(n\ge1\), with the explicit classification of nonconstant words valid at any length where such a word exists (first at \(n=4\)). It does not assert a count of arbitrary finite linear good words.

## Proof

**Step 1: reduction to a finite forbidden list for periodic words.** Baranwal, Currie, Mol, Ochem, Rampersad and Shallit [1, Theorem 11 and Proposition 18] establish the minimal forbidden antisquares and prove that a bi-infinite good word containing \(001011\) must be \({}^\omega0\,101\,1^\omega\); its complement handles \(110100\). Neither exceptional two-sided word is periodic. Consequently a periodic binary word is good if and only if it avoids, cyclically, the eight factors

\[
\mathcal F=\{0011,1100,0110,1001,010101,101010,001011,110100\}.
\]

For completeness, the essential exceptional-word obstruction is local: if a two-sided good word contains \(0^k101^k\), \(k\ge2\), at a maximal finite symmetric run, either permitted right extension produces the order-two antisquare \(1100\), or the longer antisquare \(0^k101^k01\). Thus the symmetric run must extend indefinitely. The minimal-antisquare theorem gives the other implication: every forbidden antisquare of order at least five contains \(001011\) or \(110100\), while minimal orders two and three already occur in the remaining six factors. Both claims and the proof of the nonstandard local obstruction are explicitly checked against the full text of [1].

**Step 2: cyclic first-difference coding.** Put \(p_i=w_i\oplus w_{i+1}\), indices taken modulo \(n\). The eight forbidden factors in Step 1 correspond respectively to the difference-pattern set

\[
\mathcal P=\{010,101,11111,01110\}.
\]

The map from a cyclic binary word to its cyclic differences is two-to-one onto even-parity cyclic difference sequences. Avoiding \(010\) and \(101\) forces every nontrivial run of zeros and ones to have length at least two. Avoiding \(11111\) forces each one-run to have length at most four; avoiding \(01110\) excludes one-runs of length three. Hence every nonzero permitted cyclic difference sequence consists of alternating zero-runs of length at least two and one-runs of length exactly two or four. Such difference sequences automatically have even parity and admit exactly two binary lifts; the all-zero sequence admits the two constant lifts. A cyclic difference sequence consisting entirely of ones violates \(11111\), even when its displayed period has fewer than five entries.

**Step 3: the unique minority and the gap grammar.** All zero-runs of the difference word carry the same background letter \(b\), since each intervening one-run has even length and returns to \(b\). A one-run of length two visits \(\overline b\) once; a one-run of length four visits it twice with separation exactly two. Between distinct one-runs, the next \(\overline b\) is at distance at least four, because the separating zero-run has length at least two. Therefore the successive gaps between copies of \(\overline b\) are \(2\) or \(\ge4\), with two-gaps isolated. Conversely these gap conditions group adjacent two-gaps into one-runs of length four and all other minority visits into one-runs of length two, with at least two zero differences between groups, giving exactly the permitted grammar. Each period of a difference word is assembled from \(0^a1^b\) blocks with \(a\ge2\) and \(b=2\) or \(4\). A block contributes \(b/2\) minority symbols in length \(a+b\), at most a third of the length. Hence the minority is strict and unique. Equality is possible only for blocks \(0^21^4\), producing the period-six word \(101000\) up to rotation and complement; there are six shifts per binary choice, for a total of \(12\), at lengths divisible by six.

**Step 4: coefficient formula.** Fix \(k\ge1\) minority positions and distinguish one of them as the start of a cyclic gap tuple \((d_1,\ldots,d_k)\). If exactly \(r\) gaps are short (equal to two), cyclic nonadjacency allows

\[
\frac{k}{k-r}\binom{k-r}{r}
\]

ordered marked gap-position configurations; the remaining \(k-r\) gaps are all \(\ge4\). Their excess over four has sum \(n-4k+2r\), which has

\[
\binom{n-3k+r-1}{k-r-1}
\]

nonnegative compositions if the excess is nonnegative. There are \(n\) placements of the distinguished minority marker, each unmarked word is represented \(k\) times, and the background color has two choices. Multiplication and summation yield the stated exact formula, including the \(k=1\) case.

**Step 5: rational generating function.** Mark every minority letter by \(u\), every physical position by \(z\). The length series for a long gap is \(L=z^4/(1-z)\), and for a short gap it is \(S=z^2\). The two-state cyclic gap transfer matrix is

\[
T=\begin{pmatrix}uL&uS\\uL&0\end{pmatrix},\qquad
\det(I-T)=\frac{1-z-uz^4-u^2z^6}{1-z}.
\]

The trace of \(T^k\) enumerates gap tuples around \(k\) minority letters. The factor \(n/k\) from the preceding paragraph is implemented by \(z\partial_z/k\). Thus the nonconstant contribution is

\[
-2z\partial_z\log\det(I-T)
=2z\partial_z\log\frac{1-z}{F(z,u)}.
\]

Adding \(2z/(1-z)\) for constant words and simplifying gives \(-2z\partial_z\log F(z,u)\), exactly the announced rational expression. This calculation is a formal-power-series identity and does not rely on asymptotic approximations.

**Step 6: total growth and fluctuations.** At \(u=1\), the characteristic polynomial corresponding to \(F\) is

\[
x^6-x^5-x^2-1=(x+1)(x^2-x+1)(x^3-x^2-1).
\]

The log-derivative identity expresses \(C_n\) as twice the power sum of the six roots at exponent \(n\): \(C_n=2\sum_{j=1}^6\lambda_j^n\) where roots are counted with multiplicity. The cubic has positive real root \(\psi\) and two conjugates of modulus \(\psi^{-1/2}\); the other factors supply \((-1)^n\) and \(2\cos(n\pi/3)\). This proves the displayed exact-asymptotic expansion.

For \(u>0\) near one, \(F(z,u)\) has a unique smallest-modulus zero \(\rho(u)>0\), which is simple; uniqueness follows from the positive renewal lengths \(1,4,6\), with gcd one. The other roots stay uniformly separated in modulus near \(u=1\). The log derivative hence yields, uniformly for real or complex \(u\) in a neighborhood of one,

\[
\sum_k C_{n,k}u^k=2\rho(u)^{-n}\bigl(1+O(\eta^n)\bigr)
\]

for some \(0<\eta<1\). Substitute \(u=e^{t/\sqrt n}\), divide by the \(u=1\) value and subtract the linear term \(\mu t\sqrt n\); the Taylor expansion of \(-\log\rho(e^s)\) yields convergence of moment generating functions to \(\exp(\sigma^2t^2/2)\). Implicit differentiation of \(F(\rho(u),u)=0\) gives the displayed constants. The positivity of \(\sigma^2\) is verified from explicit rational root bounds in the accompanying program (and structurally follows because the equal-length gap blocks \(0^41^2\) and \(0^21^4\) have distinct minority counts). This proves the Gaussian limit without treating numerical enumerations as an infinite proof.

## Verification

The self-contained standard-library script `verify.py` independently tests cyclic antisquare avoidance, rather than merely the eight-factor presentation, for every binary word of lengths \(1\) through \(15\). It compares the resulting counts by minority multiplicity to two independently implemented exact expressions (the closed binomial sum and the bivariate rational-function recurrence), the latter compared through length \(19\). It also verifies the twelve extremizers at all multiples of six through \(114\), and brackets the dominant positive root. Run from the package directory using `python3 verify.py`. All checks reported `ALL CHECKS PASSED`. The proof for unbounded lengths is Steps 1–6, not these finite computations.

## Relationship to prior work

The exact subject is motivated by [1], which defines good words, classifies their minimal forbidden antisquares, develops the Pansiot first-difference code, and proves a supergolden-ratio exponential growth rate for *linear* good words. Section 7 of [1] even identifies the unweighted run grammar used here. The present contribution is instead a **complete circular, composition-refined** enumeration: its explicit \(n,k\) count, rational bivariate period-point series, exact period-six oscillation, extremal-minority rigidity, and limiting minority-frequency law are not supplied by its published \(\Theta\)-estimate. These quantitative results build directly on [1]'s structural theorem rather than claiming an unrelated discovery. The earlier paper [2] treats simultaneous bounds on distinct squares and antisquares and constructions of infinite words, without the circle-composition count. Targeted searches did not locate another source providing the stated bivariate circular enumeration or normal limit; unpublished or unindexed overlap remains possible.

## Limitations

The count concerns labeled cyclic words and the minority-letter statistic, not inequivalent rotation classes or arbitrary linear words. The Gaussian limit describes a uniformly chosen circularly good word, not uniform sampling from all binary words. The structural reduction uses the published minimal-antisquare and exceptional bi-infinite-word lemmas from [1]; it does not independently reprove their full general classifications. Although computer tests are exhaustive for the specified small lengths, they are not proofs for all lengths. 

## References

[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223 (first public version 19 September 2022), *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), Theorem 11, Proposition 18 and Section 7. https://arxiv.org/pdf/2209.09223

[2] T. Ng, P. Ochem, N. Rampersad and J. Shallit, *New results on pseudosquare avoidance*, arXiv:1904.09157 (2019), Sections 1–3. https://arxiv.org/pdf/1904.09157
