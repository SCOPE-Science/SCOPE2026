# A continuous–atomic limiting law for mixed Wythoff representation multiplicities

## Finding
Let \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}=(\sqrt5-1)/2\), and \(\beta=\varphi^{-2}=1-\alpha=(3-\sqrt5)/2\). Write
\[
u(h)=\lfloor h\varphi\rfloor,\quad v(k)=\lfloor k\varphi^2\rfloor,
\quad r(n)=\#\{(h,k)\in\mathbb Z_{\ge1}^{2}:u(h)+v(k)=n\}.
\]
For integer \(n\ge3\), put \(K(n)=\lfloor\beta n\rfloor\) and \(Y_n=r(n)/K(n)\). Then \(K(n)\ge1\) and \(0\le Y_n\le1\).

**Theorem.** Uniformly for every integer \(X\ge3\) and every real \(0\le y<1\),
\[
\#\{3\le n\le X:Y_n\le y\}
=2\beta y(X-2)+O\!\bigl((\log(X+2))^2\bigr).
\]
Furthermore, the exact-saturation class has the asymptotic
\[
\#\{3\le n\le X:Y_n=1\}
=(1-2\beta)(X-2)+O\!\bigl((\log(X+2))^2\bigr).
\]
Both implied constants are absolute. Consequently the empirical probability measures of \(Y_n\), for integers \(3\le n\le X\), converge weakly to
\[
\mu=2\beta\operatorname{Unif}[0,1]+(1-2\beta)\delta_1.
\]
Its cumulative distribution function is \(0\) for \(y<0\), \(2\beta y\) for \(0\le y<1\), and \(1\) for \(y\ge1\). The point mass at \(1\) is \(1-2\beta=\sqrt5-2\); the continuous component has weight \(2\beta=3-\sqrt5\). In particular, for each fixed real \(s>0\),
\[
\lim_{X\to\infty}\frac{1}{X-2}\sum_{n=3}^{X}Y_n^s
=1-2\beta+\frac{2\beta}{s+1}.
\]
For \(s=1\), this limit is \(\alpha\).

## Assumptions and scope
The pairs are **ordered by the two specified sequence roles**: \(h\) indexes the lower Wythoff sequence and \(k\) indexes the upper Wythoff sequence; both indices start at one. All counting asymptotics concern positive integers \(n\) in an initial interval and absolute error bounds uniform in the indicated real threshold. No smoothing, probabilistic independence, or restriction to a subsequence of integers is assumed. Every admissible upper Wythoff term below \(n\) supplies at most one representation, so \(K(n)\) is the natural exact upper bound.

## Proof
**1. Beatty membership and admissible summands.** For every positive integer \(m\), Beatty complementarity gives
\[
m\in\{u(h):h\ge1\}\quad\Longleftrightarrow\quad \{m\alpha\}>\beta.
\]
Indeed, the lower Wythoff terms up to \(m\) are counted by \(\lfloor (m+1)\alpha\rfloor\); their indicator is the difference of consecutive floors, which equals one precisely when \(\{m\alpha\}>1-\alpha=\beta\). Since \(\varphi^2=1/\beta\) is irrational, \(v(k)<n\) holds exactly when \(1\le k\le K(n)=\lfloor\beta n\rfloor\). Fix \(n\ge3\) and write \(t=\{n\alpha\}\) and \(s_k=\{k\alpha\}\). As \(\alpha^2+\alpha=1\), the identity
\[
v(k)\alpha-\beta s_k=k+\lfloor k\alpha\rfloor\in\mathbb Z
\]
shows that \(\{v(k)\alpha\}=\beta s_k\), where \(0<\beta s_k<\beta\).

**2. Exact three-phase formula.** Applying lower-Beatty membership to \(n-v(k)\) gives \(\{t-\beta s_k\}>\beta\). As \(\alpha\) is irrational, \(t\) never equals \(0\), \(\beta\), or \(2\beta\). A complete case split gives
\[
r(n)=\begin{cases}
\#\{1\le k\le K(n):s_k>t/\beta\},&0<t<\beta,\\
\#\{1\le k\le K(n):s_k<(t-\beta)/\beta\},&\beta<t<2\beta,\\
K(n),&2\beta<t<1.
\end{cases}
\]
In the first case, \(t-\beta s_k<0\) precisely when the fractional part wraps around to exceed \(\beta\); in the second there is no wrap and the threshold must exceed \(\beta\); in the third it always does.

**3. Uniform rotation discrepancy.** There is an absolute \(C\) such that for all integers \(M\ge1\), \(a\ge0\) and every subinterval \(I\subset[0,1)\),
\[
\left|\#\{a<k\le a+M:\{k\alpha\}\in I\}-M|I|\right|
\le C\log(M+2).
\]
For completeness, the continued-fraction coefficients of \(\alpha=[0;1,1,1,\ldots]\) are bounded; its convergent denominators are Fibonacci numbers. On a block of length a convergent denominator \(q\), the points of this rotation differ from a translated evenly spaced \(q\)-point grid by less than \(1/q\). The count discrepancy for an interval is therefore bounded independently of \(q\) and the block's starting point. Every length \(M\) decomposes into at most \(O(\log(M+2))\) such Fibonacci blocks by greedy decomposition. Summing their absolute discrepancies proves the assertion.

Define the continuous tent-with-plateau function
\[
g(t)=\begin{cases}
1-t/\beta,&0\le t\le\beta,\\
t/\beta-1,&\beta\le t\le2\beta,\\
1,&2\beta\le t\le1.
\end{cases}
\]
The exact three-phase formula and the interval discrepancy bound give, uniformly for \(n\ge3\),
\[
|r(n)-K(n)g(\{n\alpha\})|\le C\log(n+2).
\]
This is an absolute, not just average, error. Also, \(r(n)=K(n)\) exactly throughout the plateau \(\{n\alpha\}>2\beta\).

**4. Quantitative empirical distribution.** For \(0\le y<1\), the set of phases with \(g(t)\le y\) is exactly the single interval
\[
I_y=[\beta(1-y),\,\beta(1+y)]\subset[0,2\beta],
\qquad |I_y|=2\beta y.
\]
For \(n\) in a dyadic block \(2^j\le n<2^{j+1}\) with \(j\ge3\), the estimate in step 3 and \(K(n)\asymp n\) show that \(|Y_n-g(\{n\alpha\})|\le C(j+1)/2^j\). The plateau cannot contribute to a discrepancy between the indicators \(\mathbf1_{\{Y_n\le y\}}\) and \(\mathbf1_{\{g(\{n\alpha\})\le y\}}\), because both values equal one there and \(y<1\). Off the plateau, the two indicators can differ only if \(g(\{n\alpha\})\) is within \(C(j+1)/2^j\) of \(y\). Because \(g\) is affine with slopes of magnitude \(1/\beta\) on each of its other two pieces, this exceptional phase set is contained in at most two intervals whose total length is \(O((j+1)/2^j)\). Applying the uniform rotation discrepancy bound to the length-\(O(2^j)\) index block shows there are \(O(j+1)\) possible exceptional integers, uniformly in \(y\). Summing over \(O(\log(X+2))\) dyadic blocks yields \(O((\log(X+2))^2)\) exceptions. Finally, the same rotation discrepancy applied to \(I_y\) on the whole integer interval \([3,X]\) gives
\[
\#\{3\le n\le X:\{n\alpha\}\in I_y\}
=2\beta y(X-2)+O(\log(X+2)),
\]
which proves the first assertion. The cases \(y<0\) and \(y\ge1\) are exact and establish uniform convergence of the full empirical cumulative distribution function at the claimed rate.

**5. Positive density of exact saturation.** The plateau itself contributes
\[
\#\{3\le n\le X:\{n\alpha\}>2\beta\}
=(1-2\beta)(X-2)+O(\log(X+2)).
\]
It remains to bound possible saturation outside that interval. Rotation discrepancy shows that among \(s_1,\ldots,s_K\), for every \(K\ge2\), there are points within \(C\log(K+2)/K\) of both zero and one. The first line of the exact formula forces \(t=O(\log(n+2)/n)\) if \(r(n)=K(n)\) and \(t<\beta\); the second line forces \(2\beta-t=O(\log(n+2)/n)\) if \(r(n)=K(n)\) and \(\beta<t<2\beta\). Each dyadic block therefore contains at most \(O(j+1)\) such n, by the same uniform rotation discrepancy argument for the two short intervals at \(0\) and \(2\beta\). Over all blocks this is \(O((\log(X+2))^2)\), proving the saturation formula.

**6. Moments.** Every \(Y_n\) lies in \([0,1]\). Weak convergence to the stated measure implies convergence against every continuous function on that compact interval. Taking \(f(y)=y^s\) for any fixed real \(s>0\) gives the displayed moment identity. This finishes the proof.

## Verification
The independent integer-arithmetic check in `verify.py` enumerates the exact representation count directly and via the three-phase rotation formula for every integer from \(3\) through \(2400\), inclusive, and checks five additional larger integers. It uses exact arithmetic in \(\mathbb Q(\sqrt5)\), including integer-square-root formulas for floor operations, rather than floating-point comparisons. Its successful output is `VERIFY_OK exact_two_way_checks=2398 additional_large_checks=5`. These checks test the formulas but do not prove the infinite asymptotics; those follow from steps 1–6.

## Relationship to prior work
A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words* (2026), Section 3, proves the exact classifications of the cases \(r(n)=1\) and \(r(n)=2\), crediting the earlier \(r(n)=0\) result. The present theorem studies instead the distribution of **linearly growing** representation counts, including a positive-density class where every available upper summand works. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond* (2020), Section 11.2, gives a rank-19 linear representation for evaluating the pointwise count, but does not state the continuous–atomic limiting law, the complete-saturation density, or the uniform counting error proved here. OEIS A259598 lists the exact count sequence and earlier special-case conjectures, without the present limiting measure. Kawsumarng, Khemaratchatakumthorn, Noppakaew and Pongsriiam (2021) address sumset membership; no stronger covering result was identified in the available material. The newly established analytic distribution requires the rotation identity and discrepancy argument above; it is not claimed to follow directly from a database table or an explicit finite automaton.

## Limitations
This result concerns only the mixed lower-plus-upper Wythoff count and normalization by the exact number \(K(n)\) of available upper terms. It does not determine an exact finite formula for every saturation exception outside the plateau, optimize the absolute discrepancy constants, or classify analogous sums of two terms from the same Wythoff sequence. Prior-work comparisons are limited by accessible sources; an equivalent unpublished or differently indexed result cannot be excluded. The scientific analysis and finite checks are not independent external validation.

## References
1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (October 4, 2026), Section 3.
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177v1 (June 7, 2020), Sections 7 and 11.2; also *Periodica Mathematica Hungarica* 84 (2022), 37–46.
3. OEIS Foundation, A259598, "Number of representations of n as u(h) + v(k)", https://oeis.org/A259598 (examined October 15, 2026).
4. S. Kawsumarng, T. Khemaratchatakumthorn, P. Noppakaew and P. Pongsriiam, *Sumsets associated with Wythoff sequences and Fibonacci numbers*, *Periodica Mathematica Hungarica* 82 (2021), 98–113, DOI:10.1007/s10998-020-00343-0.
