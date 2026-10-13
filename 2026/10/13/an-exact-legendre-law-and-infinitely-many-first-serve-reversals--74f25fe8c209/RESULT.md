# An exact Legendre law and infinitely many first-serve reversals in fair-rally pickleball

## Finding

In conventional doubles side-out scoring, assume independent rallies and that either serving team wins each rally with probability exactly \(1/2\). The team serving first begins with its *second* server, while subsequent turns begin with the first server. A game is played to integer target \(n\ge2\) and requires a two-point winning margin, without a cap. Let \(f_n\) denote the probability that fixed Team A wins when A serves first minus the probability that A wins when Team B serves first. Let \(P_k\) be the ordinary Legendre polynomial of degree \(k\), normalized by \(P_0(t)=1\) and \(P_1(t)=t\).

For **every** integer \(n\ge2\),

\[
f_n=\frac{75P_{n-1}(3/5)+55P_{n-2}(3/5)}{86\,5^n}.
\]

Thus the first-serving team's win probability is \((1+f_n)/2\), and its advantage is exponentially small but changes sign **infinitely often** as the target increases. More precisely, with \(\theta=\arccos(3/5)\) and \(\delta=\arctan(1/13)\),

\[
f_n=\frac{10\sqrt{34}}{43\,5^n}\sqrt{\frac{5}{2\pi(n-1)}}\left[\cos\!\left((n-1)\theta-\frac{\pi}{4}+\delta\right)+O(n^{-1})\right].
\]

In particular, with \(C=(10\sqrt{34}/43)\sqrt{5/(2\pi)}\),

\[
\limsup_{n\to\infty} 5^n\sqrt n\,f_n=C,
\qquad
\liminf_{n\to\infty} 5^n\sqrt n\,f_n=-C.
\]

## Assumptions and scope

Team A and Team B are equally skilled **on serve**: every rally is won by the currently serving team with probability \(1/2\), independently of all other rallies. A winning rally scores one point and retains service; a losing rally scores no point and advances the server cyclically through A-first, A-second, B-first, B-second. The game starts at score zero for both sides, at A-second if A serves first or B-second if B serves first. One team wins when its score reaches at least \(n\) and leads by at least two. There are no timeout rules, side-quality effects, player-specific differences, rally-scoring variants, or finite deuce caps. All claims have domain \(n\in\{2,3,\ldots\}\).

The comparison \(f_n\) keeps Team A fixed; it is not a comparison between different teams' strengths. By team-swap symmetry, \(f_n=2\Pr(\text{initial server wins})-1\).

## Proof

**1. Score-event embedding.** Ignore faults that do not produce a point, and observe the state immediately following each successful serving rally. Index the serving states cyclically by \(0,1,2,3\), corresponding to A-first, A-second, B-first, B-second. A run of exactly \(r\) faults followed by a scored point has probability \(2^{-(r+1)}\). Summing over complete cycles gives the score-event transition matrix

\[
Q_{st}=\frac{q_{(t-s)\bmod4}}{15},
\qquad (q_0,q_1,q_2,q_3)=(8,4,2,1).
\]

States \(0,1\) award the point to A; states \(2,3\) award it to B. The probability vector for the next point being scored by A, conditional on the current serving state, is \(a=(4/5,3/5,1/5,2/5)^{\mathsf T}\).

**2. Exact continuation from deuce.** At score \((n-1,n-1)\), continue with the score-difference state \(d\in\{-1,0,1\}\). Write \(h_{d,s}\) for A's chance of eventual victory starting with difference \(d\) and current serving state \(s\). With terminal values \(h_{2,s}=1\), \(h_{-2,s}=0\), these values solve the twelve equations

\[
h_{d,s}=\sum_{t=0}^{3}Q_{st}\,h_{d+\varepsilon_t,t},
\qquad \varepsilon_t=\begin{cases}1&t<2,\\-1&t\ge2.\end{cases}
\]

Their unique bounded solution has rows indexed by differences \(-1,0,1\), respectively:

\[
(h_{d,s})=
\begin{pmatrix}
22/43&14/43&11/86&11/43\\
30/43&45/86&13/43&41/86\\
75/86&32/43&21/43&29/43
\end{pmatrix}.
\]

These entries satisfy every equation by direct substitution, and uniqueness follows because the finite deuce chain reaches a decisive two-point lead almost surely: at each fixed group of two scored points there is a uniform positive chance of terminating.

**3. Cancellation of the common Green-function pole.** For formal marking variables \(x,y\), put \(T(x,y)=Q\operatorname{diag}(x,x,y,y)\). The unrestricted score-state Green matrix is \(G(x,y)=(I-T(x,y))^{-1}\); its \((s,t)\) entry enumerates point-scoring histories starting at state \(s\), ending at state \(t\), with powers recording the teams' scored points. The difference between rows A-second and B-second simplifies **exactly** to

\[
G_{1,\bullet}(x,y)-G_{3,\bullet}(x,y)
=\frac{(-x,\,5-2y,\,y,\,2x-5)}{5-2x-2y+xy}.
\]

This identity is verified directly by right-multiplying the numerator row by \(I-T\): the result is \((5-2x-2y+xy)(0,1,0,-1)\). Set \(H(x,y)=(5-2x-2y+xy)^{-1}\). Weighting by the probability of an A-scored next point, or by the deuce continuation, yields

\[
(G_{1,\bullet}-G_{3,\bullet})a=(1-y)H,
\qquad
(G_{1,\bullet}-G_{3,\bullet})h_{0,\bullet}
=\frac{11x-32y+10}{43}H.
\]

**4. Hitting decomposition and diagonal extraction.** No score pair below \((n,n)\) with both coordinates at most \(n-1\) could already have ended the game. A winning A point is scored from \((n-1,j)\), with \(0\le j\le n-2\), or the game first reaches deuce \((n-1,n-1)\) and continues according to \(h_0\). Write \(c_{ij}=[x^iy^j]H(x,y)\), with negative indices interpreted as zero. Using the preceding weighted Green functions, telescoping \(1-y\) over \(j\) gives

\[
\begin{aligned}
f_n
&=c_{n-1,n-2}
 +\frac{11c_{n-2,n-1}-32c_{n-1,n-2}+10c_{n-1,n-1}}{43}\\
&=\frac{22c_{m,m-1}+10c_{m,m}}{43},\qquad m=n-1.
\end{aligned}
\]

The symmetry \(c_{ij}=c_{ji}\) and the coefficient identity from \((5-2x-2y+xy)H=1\) give \(4c_{m,m-1}=5c_{m,m}+c_{m-1,m-1}\) for \(m\ge1\). Hence

\[
f_n=\frac{75c_{m,m}+11c_{m-1,m-1}}{86}.
\]

For the diagonal coefficients, the constant-term identity (obtained by expanding the geometric series and choosing equal numbers of positive and negative powers of an auxiliary variable) gives

\[
\sum_{m\ge0}c_{m,m}t^m
=\operatorname{CT}_x H(x,t/x)
=\frac1{\sqrt{(5+t)^2-16t}}
=\frac15\sum_{m\ge0}P_m(3/5)(t/5)^m.
\]

Thus \(c_{m,m}=5^{-m-1}P_m(3/5)\), and substitution establishes the stated exact formula for all \(n\ge2\).

**5. Oscillation and sharp envelope.** The fixed-angle Legendre asymptotic for \(0<\theta<\pi\) is

\[
P_m(\cos\theta)=\sqrt{\frac{2}{\pi m\sin\theta}}
\left[\cos\!\left((m+\tfrac12)\theta-\tfrac\pi4\right)+O(m^{-1})\right].
\]

Here \(\sin\theta=4/5\), and combining the two adjacent cosine terms has amplitude \(20\sqrt{34}\) and phase shift \(\delta=\arctan(1/13)\). This gives the displayed uniform-in-index expansion and envelope. Finally, \(\theta/\pi\) is irrational: otherwise \(2\cos\theta=6/5\) would be both a rational number and an algebraic integer, hence an integer, which it is not. The irrational-rotation sequence of cosine phases is dense modulo \(2\pi\). Along subsequences the cosine tends to \(+1\) and \(-1\); the error vanishes. The two sharp extremal limits follow, giving infinitely many strictly positive and strictly negative advantages.

## Verification

Run `python3 verify.py` with the Python standard library. The verifier checks all twelve deuce equations using exact fractions, six polynomial identities involving the rational Green row and weighted reductions, and thirty independent exact dynamic-programming evaluations for targets \(2\le n\le31\). It also checks the Legendre recurrence through degree \(31\). The exact calculations reproduce \(f_{11}\approx-4.95577\times10^{-9}\) and \(f_{15}\approx1.00593\times10^{-11}\). Finite computations are corroboration; the unrestricted all-target formula and asymptotic sign changes are consequences of the analytic derivation.

## Relationship to prior work

DeFord and Ethier, *Does the first-serving team have a structural advantage in pickleball?* (arXiv:2303.02942, first posted March 6, 2023), supplied the independent-rally model and a general absorbing-chain rational evaluation, examining in depth targets \(11\) and \(15\). Their explicit calculations show opposite signs at commonly used targets. The present result specializes to equal on-serve rally probability \(1/2\), makes the dependence on **every** integer target explicit through Legendre polynomials, proves a sharp asymptotic envelope, and proves infinitely many further reversals. The published modeling framework implies a finite-matrix route to any fixed target; it does not itself state this all-target closed law or its sign-oscillation theorem.

Standard Legendre polynomial identities and interior asymptotics are used as classical mathematical tools, not claimed as discoveries. Contemporary numerical pickleball comparisons do not supply an exact all-target expression. The risk of an earlier equivalent scoring-model derivation cannot be excluded without independent bibliographic review.

## Limitations

The theorem does not cover unequal rally-win probabilities, modified rally scoring, a cap on games after deuce, per-player heterogeneity, position effects, or the sizes and signs of the first-serve bias for every target at other parameters. The oscillation assertion concerns infinitely many integer targets, **not** monotonic alternation at consecutive targets.

## References

1. D. R. DeFord and S. N. Ethier, *Does the first-serving team have a structural advantage in pickleball?*, arXiv:2303.02942v1 (March 6, 2023), revised v2 (August 22, 2023). https://arxiv.org/abs/2303.02942 ; full open preprint https://arxiv.org/pdf/2303.02942 .
2. NIST Digital Library of Mathematical Functions, Chapter 14, §14.15(iii), large-degree fixed-order Legendre asymptotics. https://dlmf.nist.gov/14.15 .
3. M. Wright and W. Figary, *Should You Choose to Serve First in a Pickleball Match?*, Mathematical Association of America. https://maa.org/math-values/should-you-choose-to-serve-first-in-a-pickleball-match/ .
