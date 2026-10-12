# The exact WDLE modal staircase and fixed-origin half-circle barrier

## Finding

Fix an integer \(m\ge2\). The wrapped discrete linear-exponential (WDLE) model of Alharbi, Bengalath and Abd El-Bar [1] puts mass \(f_{m,\varphi}(r)\) on the residues \(r=0,1,\ldots,m-1\), with \(\varphi>0\) and a fixed angular origin. Its modal sector is not free to rotate across all \(m\) residues. Define

\[
H_m(\varphi)=\frac{2}{e^\varphi-1}-\frac{m}{e^{m\varphi}-1}-\frac{1}{\varphi}-\varphi^2,
\qquad k_m=\left\lfloor\frac{m-1}{2}\right\rfloor.
\]

**Exact modal staircase theorem.** For every integer \(m\ge2\), \(H_m\) is strictly decreasing on \((0,\infty)\), with limits \(m/2-1\) and \(-\infty\). If \(H_m(\varphi)\notin\{0,1,\ldots,k_m-1\}\), the unique global mode is

\[
r_{\mathrm{mode}}=\max\{0,\lceil H_m(\varphi)\rceil\}.
\]

For each \(j=0,\ldots,k_m-1\), one unique transition \(\varphi_{m,j}>0\) satisfies \(H_m(\varphi_{m,j})=j\). Precisely at that transition, both \(j\) and \(j+1\), and no other residues, maximize the probability. These transitions are strictly ordered \(\varphi_{m,k_m-1}<\cdots<\varphi_{m,0}\). Every residue \(0,\ldots,k_m\) occurs as a unique mode on an open parameter interval, and no residue above \(k_m\) can be a mode for any \(\varphi>0\). For \(m=2\), the mode is always \(0\).

## Assumptions and scope

Use the actual fixed-origin WDLE law, not an arbitrary translation of it. Its nonnegative-integer parent has survival values

\[
S(x)=\frac{e^{-\varphi x}(1+\varphi x+\varphi^3)}{1+\varphi^3},
\qquad x\in\{0,1,\ldots\},\quad \varphi>0,
\]

and mass \(p(x)=S(x)-S(x+1)\). This agrees with Eq. (2) of [1]. The wrapped law is \(f_{m,\varphi}(r)=\sum_{h\ge0}p(r+hm)\). The assertion concerns *global probability modes* over the canonical labeled residues; it does not conflate them with circular mean directions, and does not assume an independent location or origin parameter. The trivial \(m=1\) case consists only of residue \(0\).

## Proof

Write \(q=e^{-\varphi}\), \(Q=q^m\), \(A=1+\varphi^3\), and

\[
c=A(1-q)-q\varphi,\qquad d=\varphi(1-q)>0.
\]

Taking successive differences of the stated survival function gives

\[
p(x)=\frac{q^x}{A}(c+dx),
\]

and summing two absolutely convergent geometric series yields the exact normalized WDLE mass

\[
f_{m,\varphi}(r)=\frac{q^r}{A(1-Q)}\left(c+dr+\frac{dmQ}{1-Q}\right)=Kq^r(b+r),
\]

where

\[
K=\frac{d}{A(1-Q)}>0,
\qquad b=\frac{1}{\varphi}+\varphi^2-\frac{1}{e^\varphi-1}+\frac{m}{e^{m\varphi}-1}>0.
\]

Here positivity follows also from the original strictly positive mass, and normalization follows by partitioning all nonnegative integers into the \(m\) residue classes. The adjacent ratio \(q(b+r+1)/(b+r)\) is strictly decreasing with \(r\). Its sign comparison reduces *exactly* to

\[
\begin{aligned}
f_{m,\varphi}(r+1)>f_{m,\varphi}(r)
&\iff q(b+r+1)>b+r\\
&\iff r<H_m(\varphi),\qquad 0\le r<m-1.
\end{aligned}
\]

Equality holds exactly when \(r=H_m(\varphi)\). Thus there is never more than one global mode except for a pair of adjacent tied residues; when there is no tie, the first nonincreasing step locates the unique mode as claimed.

It remains to establish the *global* order and full range of transitions. Split

\[
H_m(x)=\underbrace{\left(\frac{1}{\sinh x}-\frac1x-x^2\right)}_{H_2(x)}
+\underbrace{\left(\frac{2}{e^{2x}-1}-\frac{m}{e^{mx}-1}\right)}_{D_m(x)}.
\]

The derivative of the second term is

\[
D_m'(x)=-\frac{1}{\sinh^2x}+\frac{m^2}{4\sinh^2(mx/2)}\le0,
\]

because \(t\mapsto\sinh(t)/t\) is strictly increasing for positive \(t\), and \(m\ge2\). For the first term,

\[
H_2'(x)=\frac{1}{x^2}-\frac{\cosh x}{\sinh^2x}-2x.
\]

If \(x\ge1\), this is negative since \(1/x^2-2x<0\). If \(0<x\le1\), use the coefficientwise factorial bound \((2h+1)!\ge6^h\) and the elementary estimates

\[
\frac{\sinh x}{x}\le\frac{1}{1-x^2/6},\qquad
\cosh x\ge1+\frac{x^2}{2}\ge\frac{1}{(1-x^2/6)^2}.
\]

The last inequality follows, setting \(z=x^2\in(0,1]\), from

\[
\left(1+\frac z2\right)\left(1-\frac z6\right)^2-1
=\frac z6-\frac{5z^2}{36}+\frac{z^3}{72}\ge\frac z{36}>0.
\]

Hence \(\cosh x/\sinh^2x>1/x^2\) on this range, proving \(H_2'(x)<0\) everywhere, and therefore \(H_m'(x)<0\).

The standard expansion \(1/(e^y-1)=1/y-1/2+O(y)\) as \(y\downarrow0\) gives \(H_m(0+)=m/2-1\), whereas \(H_m(x)\to-\infty\) as \(x\to\infty\), due to \(-x^2\). Strict monotonicity and the intermediate value theorem give precisely the unique crossings at \(j=0,\ldots,k_m-1\). For positive \(x\), the ceiling of \(H_m(x)\) cannot exceed \(k_m\); the adjacent-ratio classification gives the sharp upper barrier, all attainable modal residues, and the stated transition ordering. This proves the theorem for all integer \(m\ge2\) and all \(\varphi>0\).

## Verification

The self-contained `verify_wdle_mode.py` uses only Python 3's standard library. Run `python3 verify_wdle_mode.py`. It independently compares the finite closed form with long direct sums of the original wrapped parent masses, checks normalization and predicted modal indices for multiple dimensions and shapes, and computes transition roots by bisection. It prints `CHECK_OK` on success. These are finite numerical cross-checks, **not** the proof of strict monotonicity or of the infinite parameter-range claim.

For example, the unique transition at \(m=3\) is \(\varphi_{3,0}=0.48078153605493\ldots\). At \(m=9\), the transitions \((\varphi_{9,0},\varphi_{9,1},\varphi_{9,2},\varphi_{9,3})\) are approximately

\[
(0.71211839499782,\ 0.43471723426633,\ 0.23579457294878,\ 0.07567261369589).
\]

Accordingly, the mode walks through residues \(4,3,2,1,0\) as \(\varphi\) increases from zero to infinity, with adjacent ties at the four transition shapes.

## Relationship to prior work

The parent and wrapped PMFs, geometric and gamma-mixture representation, and circular moments are already derived in [1]; they are used as premises and are **not** claimed as new. What is established here is the complete all-\(m\) modal phase diagram, strict ordering of its shape thresholds, and the sharp fixed-origin upper bound on the possible modal sector. The source illustrates shape changes graphically but does not give these analytical mode thresholds in the examined distributional and applied sections. Its explicit discussion of angular-origin sensitivity supplies an application-level reason to distinguish a fixed-origin modal constraint from unrestricted circular rotation.

Related weighted-geometric and discrete wrapped-exponential models in [2] and [3] establish general shape or distributional properties for *different* probability laws; in particular, generic unimodality does not give the parameter-dependent WDLE thresholds or the sharp sector ceiling. Other algebraic log-linear mass functions may share elementary adjacent-ratio techniques; originality here is restricted to the precise WDLE family and its complete sharp phase classification.

## Limitations

The theorem says nothing about a WDLE family enlarged by an independent location parameter; such a change could rotate which physical direction carries the mode. A global mode is different from a circular mean direction or local cyclic extrema. Decimal thresholds are approximations; their existence and uniqueness follow from the proof, not the decimals. Primary-publisher PDF access was restricted during checking, so unexamined appendices remain a literature-comparison risk.

## References

1. Y. F. Alharbi, J. Bengalath, A. M. T. Abd El-Bar, “A New Wrapped Discrete Linear Exponential Distribution for Circular Data: Theory, Estimation, and Applications,” *Axioms* **15** (2026), 631. DOI: https://doi.org/10.3390/axioms15090631 (publicly published 2026-08-25; primary MSC 60E05).
2. M. Shakhatreh, H. Al-Mofleh, “On a Two-Parameter Weighted Geometric Distribution: Properties, Computation and Applications,” *Statistics, Optimization & Information Computing* **13** (2025), 642–663. DOI: https://doi.org/10.19139/soic-2310-5070-2139 (first published 2024-08-25).
3. G. V. L. N. Srihari, S. V. S. Girija, A. V. Dattatreya Rao, “On Discrete Wrapped Exponential Distribution—Characteristics,” *International Journal of Scientific Research in Mathematical and Statistical Sciences* **5** (2018), 57–64, https://ijsrmss.isroset.org/index.php/j/article/view/51.
