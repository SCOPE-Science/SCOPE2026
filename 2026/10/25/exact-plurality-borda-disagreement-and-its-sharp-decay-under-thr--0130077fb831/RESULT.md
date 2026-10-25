# Exact plurality–Borda disagreement and its sharp decay under three-candidate Walsh voting

## Finding
Fix three alternatives in the known single-peaked order \(A-B-C\). Each of \(n\ge1\) voters independently chooses uniformly among the four permitted strict preference orders \(ABC,BAC,BCA,CBA\). Let \(Q_n\) be the probability that plurality and Borda (positional scores \(2,1,0\)) both have unique winners and these winners are different. Write \(a,b,c,d\) for the numbers of the four votes in the order displayed. Then, for every integer \(n\ge1\),
\[
Q_n=\frac{2}{4^n}\sum_{\substack{a+b+c+d=n\\a>\max\{b+c,d\}\\a<d+b+2c}}\frac{n!}{a!b!c!d!}.
\]
Put \(Z=1+2\sqrt2\), \(\rho=Z/4\), and \(\sigma^2=2\sqrt2/Z\). Then
\[
Q_n\sim\frac{2(1+\sqrt2)}{\sqrt{2\pi\sigma^2}}\frac{\rho^n}{\sqrt n}\qquad(n\to\infty),
\]
with \(\rho\approx0.9571067812\), exponential rate \(-\log\rho\approx0.0438403147\), and multiplicative prefactor approximately \(2.241059785\). The first strict disagreement occurs at \(n=4\): \(Q_1=Q_2=Q_3=0\) and \(Q_4=3/32\). Every such disagreement is between a plurality-winning *extreme* alternative and the Borda-winning *middle* alternative; the reverse direction never occurs.

## Assumptions and scope
Voters are independent and identically distributed according to Walsh's uniform distribution on the four single-peaked strict rankings of the fixed three-alternative axis. Candidate names are fixed, and the social-choice rules are the usual plurality rule and Borda rule with scores \((2,1,0)\). A draw is counted only when both winner sets are singletons and those singleton winners differ. Thus ties are *excluded*, not arbitrarily broken. The theorem holds for every integer \(n\ge1\); the asymptotic statement is as \(n\to\infty\). No claims are made for other cultures or larger candidate sets.

## Proof
**1. The exact mismatch domain.** Under the four vote multiplicities, the plurality scores of \((A,B,C)\) are \((a,b+c,d)\). Their Borda scores are
\[
(2a+b,\ n+b+c,\ c+2d).
\]
If Borda uniquely selects \(A\), comparison with \(B\) requires \(a>d+b+2c\); in particular \(a>d\) and \(a>b+c\), so plurality also uniquely selects \(A\). The symmetric statement holds for \(C\). Consequently, a strict mismatch occurs only when Borda uniquely selects \(B\) and plurality selects either \(A\) or \(C\). In the \(A\)-plurality case, the necessary and sufficient strict inequalities are
\[
a>b+c,\qquad a>d,\qquad n+b+c>2a+b,
\]
i.e. \(a>\max\{b+c,d\}\) and \(a<d+b+2c\). Under these inequalities the remaining comparison \(n+b+c>c+2d\) follows from \(a>d\). Reflection of the axis gives an equal-probability, disjoint \(C\)-plurality event. Each four-count vector has multinomial weight \(4^{-n}n!/(a!b!c!d!)\). Summation yields the exact formula. Direct enumeration gives no solutions for \(n\le3\) and \(24\) labeled four-voter profiles when \(n=4\), including a witness \((a,b,c,d)=(2,0,1,1)\).

**2. Exponential change of measure.** Let \(Y_i\) be \(+1\) if voter \(i\) chooses \(ABC\), \(-1\) if the choice is \(BAC\) or \(BCA\), and \(0\) if it is \(CBA\). Then \(S_n=\sum_{i=1}^nY_i=a-b-c\), with moment-generating function
\[
M(t)=\frac{e^t+2e^{-t}+1}{4}.
\]
The unique minimizer satisfies \(t_*=\tfrac12\log2\), with \(M(t_*)=\rho=(1+2\sqrt2)/4<1\). Exponential tilting by \(e^{t_*S_n}/\rho^n\) gives a product law \(\mathbb P_*\) with individual probabilities, in vote order,
\[
q=\frac1Z\left(\sqrt2,\frac1{\sqrt2},\frac1{\sqrt2},1\right).
\]
Under this tilted law \(\mathbb E_*Y_i=0\) and \(\mathrm{Var}_*(Y_i)=\sigma^2=2\sqrt2/Z\). In particular, the tilted expected frequencies satisfy the two strict inequalities \(q_A>q_D\) and \(q_A<q_D+q_B+2q_C\). By exponential concentration for bounded independent random variables, under \(\mathbb P_*\) either inequality failing has probability at most \(Ce^{-\gamma n}\) for some positive constants \(C,\gamma\) independent of \(n\). Hence, if \(E_A\) denotes the first mismatch event in part 1,
\[
\mathbb P(E_A)=\rho^n\left(\mathbb E_*[e^{-t_*S_n}\mathbf1_{\{S_n>0\}}]+O(e^{-\gamma n})\right).
\]
Indeed, the absolute error inside the parentheses is bounded by the tilted probability of the two auxiliary-inequality failures, since \(e^{-t_*S_n}\le1\) when \(S_n>0\).

**3. Lattice local limit and prefactor.** The tilted \(Y_i\) takes each of \(-1,0,1\) with positive probability, so it is centered, aperiodic of lattice span one, and has variance \(\sigma^2>0\). Fourier inversion of its characteristic function gives, for each fixed integer \(k\),
\[
\sqrt n\,\mathbb P_*(S_n=k)\longrightarrow\frac1{\sqrt{2\pi\sigma^2}},
\qquad\sup_{n\ge1,k\in\mathbb Z}\sqrt n\,\mathbb P_*(S_n=k)<\infty.
\]
For completeness, on the circle its characteristic function has modulus strictly less than one outside a neighborhood of zero; near zero it equals \(1-\sigma^2\theta^2/2+O(|\theta|^3)\). Splitting the Fourier integral into those regions, then scaling \(\theta\) by \(\sqrt n\), proves both assertions by domination with a Gaussian majorant. Thus
\[
\begin{aligned}
\sqrt n\,\mathbb E_*[e^{-t_*S_n}\mathbf1_{\{S_n>0\}}]
&=\sum_{k=1}^{\infty}e^{-t_*k}\sqrt n\,\mathbb P_*(S_n=k)\\
&\longrightarrow\frac1{\sqrt{2\pi\sigma^2}}\sum_{k=1}^{\infty}e^{-t_*k}\\
&=\frac{1+\sqrt2}{\sqrt{2\pi\sigma^2}}.
\end{aligned}
\]
The uniform lattice bound and summable geometric weights justify exchanging the limit and sum. The exponentially small change-of-measure error is negligible compared with \(n^{-1/2}\). Multiplying the one-extreme result by two proves the theorem.

## Verification
The self-contained `check_disagreement.py` uses only Python 3 standard-library modules. It checks independently, by generating all \(4^n\) labeled ballots, that the exact multinomial formula reproduces all outcomes for \(1\le n\le8\); checks the first threshold \(Q_4=3/32\); computes further exact integer counts; verifies the centered tilted parameters; and prints numerical finite-size comparisons with the analytical asymptotic approximation. Run with `python3 check_disagreement.py`. Its finite computations corroborate, but cannot replace, the all-\(n\) derivation or the Fourier local-limit proof. The program was run successfully and reported `ALL EXACT COMBINATORIAL CHECKS PASSED`.

## Relationship to prior work
Mousseau, Surugue, and Wilczynski study agreement of positional scoring rules under Walsh's and other single-peaked cultures. Their Corollary 10 establishes asymptotic agreement, and Proposition 11 provides convergence lower bounds using expected winners and concentration. Those findings are assumed, acknowledged, and sharpened only in the *specific* three-candidate, plurality-versus-Borda, distinct-singleton statistic here: an exact finite-size enumeration and exact exponential rate including its lattice prefactor. Their Proposition 24 concerns the different Pólya–Eggenberger urn model, not this Walsh event. Walsh's original work defines the uniform single-peaked distribution. Earlier general impartial-culture agreement formulas concern a different probability space. The distinction between a set-valued agreement event and the strict two-singleton mismatch is essential. No claim of priority beyond the examined sources is made.

## Limitations
The theorem excludes profiles where either rule has a tie, and gives neither a rate for tie-breaking conventions nor rates for general positional scoring vectors. The asymptotic formula does not assert a finite-\(n\) relative-error bound, and the finite verification covers only the named enumerations. The use of a standard lattice local-limit method is mathematical background, not claimed as a new general probability theorem. Earlier publications not accessible in full, including potentially relevant theses or localized proceedings, may contain equivalent special-case calculations; historical priority requires further independent examination. The conference dating of the motivating work identifies a verified 2025 dissemination context rather than a certified earliest upload timestamp.

## References
1. V. Mousseau, H. Surugue, A. Wilczynski, *Agreement among Voting Rules under Single-Peaked Preference Distributions*, ECAI 2025 proceedings, DOI: 10.3233/FAIA251226, https://journals.sagepub.com/doi/10.3233/FAIA251226 (open full text; SAGE online posting 2026-08-25).
2. V. Mousseau, H. Surugue, A. Wilczynski, *Accord entre Règles de Vote sous des Distributions de Préférences “Single-Peaked”*, JIAF–JFPDA 2025 short proceedings, https://pfia2025.u-bourgogne.fr/conferences/jiaf/publications/JIAF2025_12.pdf (JIAF–JFPDA Dijon, July 2–4, 2025).
3. T. Walsh, *Generating Single Peaked Votes*, arXiv:1503.02766 (2015), https://arxiv.org/abs/1503.02766.
4. JIAF–JFPDA 2025 conference bibliographic record, https://dblp.org/rec/conf/jiaf/2025 (event dates July 2–4, 2025).
