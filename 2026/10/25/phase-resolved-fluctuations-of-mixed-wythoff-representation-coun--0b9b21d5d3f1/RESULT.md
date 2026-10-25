# Phase-resolved fluctuations of mixed Wythoff representation counts

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(\delta=\varphi^{-2}=(3-\sqrt5)/2\), and define the ordered mixed Wythoff representation function
\[
r(n)=\#\left\{(h,k)\in\mathbb Z_{\ge1}^{2}:
\lfloor h\varphi\rfloor+\lfloor k\varphi^2\rfloor=n\right\}.
\]
For \(0\le y\le1\), put
\[
F(y)=\begin{cases}
\delta,&0\le y\le1-2\delta,\\
1-\delta-y,&1-2\delta\le y\le1-\delta,\\
y-1+\delta,&1-\delta\le y\le1.
\end{cases}
\]
The formulas agree at their breakpoints and satisfy \(F(0)=F(1)=\delta\), so \(F\) defines a continuous function on the circle.

**Theorem.** There exists an absolute constant \(C\) such that, for every integer \(n\ge1\),
\[
\left|r(n)-nF(\{n\delta\})\right|\le C\log(2n).
\]
For \(X\ge2\), let \(N_X\) be uniform on the integers \(1,\ldots,X\). The random variable \(r(N_X)/N_X\) converges in distribution to the probability measure
\[
\nu=(1-2\delta)\operatorname{Dirac}_{\delta}
+2\,\mathbf1_{(0,\delta)}(t)\,dt.
\]
More strongly, in one-dimensional Wasserstein distance,
\[
W_1\left(\mathcal L(r(N_X)/N_X),\nu\right)
=O\left(\frac{\log^2(2X)}{X}\right).
\]
Thus the limiting measure has an atom of mass \(1-2\delta=\sqrt5-2\) at \(\delta\) and an absolutely continuous component with constant density \(2\) on \((0,\delta)\). Its mean is \(\delta(1-\delta)=\sqrt5-2\).

## Assumptions and scope

The slopes are the golden ratio and its square, the two indices \(h,k\) are positive integers, and each **ordered index pair** is counted once. Here \(\{x\}=x-\lfloor x\rfloor\) is the fractional part; \(\operatorname{Dirac}_a\) denotes a unit point mass at \(a\). The law samples the **normalized value \(r(n)/n\) at a uniformly chosen integer \(n\le X\)**; it does not normalize all counts by \(X\). The integral term in \(\nu\) has total mass \(2\delta\), and \((1-2\delta)+2\delta=1\). Implicit constants are absolute.

## Proof

**1. Exact Beatty reduction.** The classical complementary Beatty theorem applies because \(\varphi\) and \(\varphi^2\) are irrational and \(\varphi^{-1}+\varphi^{-2}=1\). Consequently, each positive integer lies in exactly one of
\[
A=\{\lfloor h\varphi\rfloor:h\ge1\},\qquad
B=\{\lfloor k\varphi^2\rfloor:k\ge1\}.
\]
The indicator of membership in \(B\) at a positive integer \(m\) is
\[
\mathbf1_B(m)=\lfloor\delta(m+1)\rfloor-\lfloor\delta m\rfloor.
\]
Indeed, this floor increment equals \(1\) exactly when the interval \((\delta m,\delta(m+1)]\) contains an integer, equivalently when \(m=\lfloor k/\delta\rfloor\) for some \(k\ge1\); irrationality rules out endpoint coincidences. By Beatty complementarity, \(\mathbf1_A(m)=1-\mathbf1_B(m)\).

Write \(b_k=\lfloor k\varphi^2\rfloor\). Since \(k\varphi^2\) is irrational, \(b_k<n\) if and only if \(k<\delta n\). Thus the valid indices are exactly \(1\le k\le K_n:=\lfloor\delta n\rfloor\). Let \(y_n=\{\delta n\}\) and \(u_k=\{k\varphi\}=\{k\varphi^2\}\). From \(b_k=k/\delta-u_k\),
\[
\delta(n-b_k)=\delta n-k+\delta u_k.
\]
Inserting this into the Beatty membership formula gives the exact identity
\[
r(n)=\sum_{k=1}^{K_n} H_{y_n}(u_k),\qquad
H_y(u):=1-\bigl(\lfloor y+\delta u+\delta\rfloor-\lfloor y+\delta u\rfloor\bigr).
\tag{1}
\]
All arguments \(n-b_k\) in this identity are positive integers.

**2. Uniform rotation discrepancy.** For every interval \(I\subseteq[0,1)\), every starting index \(s\ge0\), and every integer \(N\ge1\),
\[
\left|\#\{1\le j\le N:\{(s+j)\varphi\}\in I\}-N|I|\right|
\le C_0\log(2N),
\tag{2}
\]
with an absolute constant \(C_0\), uniformly in \(s\) and \(I\). Here is a direct justification. The continued-fraction denominators of \(\varphi\) are Fibonacci numbers \(q\), and their reduced approximants \(p/q\) satisfy \(|\varphi-p/q|<q^{-2}\). In any length-\(q\) block, re-anchor at its first phase. The \(q\) phases are within circular distance \(1/q\) of a translated complete grid \(\{jp/q:0\le j<q\}\). A translated grid counts any circular interval with error at most \(2\), and perturbing all points by at most \(1/q\) changes the count only for a bounded number of grid points near the two endpoints. Thus each Fibonacci-length block has an absolute constant discrepancy, independent of the block's starting index. Greedy decomposition of \(N\) into distinct Fibonacci denominators has \(O(\log(2N))\) blocks, proving (2). The same estimate, with a doubled constant, holds for the union of at most two intervals and for complements thereof.

**3. Compute the phase integral.** For each fixed \(y\), the function \(u\mapsto H_y(u)\) is the indicator of a union of at most two intervals in \([0,1)\), apart from harmless endpoints. Set
\[
h(y)=\int_0^1 H_y(u)\,du.
\]
The interval \([y,y+\delta]\) intersects the forbidden windows \([1-\delta,1)\) and \([2-\delta,2)\) in a total length of, respectively,
\[
0\quad(0\le y\le1-2\delta),\qquad
y+2\delta-1\quad(1-2\delta\le y\le1-\delta),
\]
\[
1-y\quad(1-\delta\le y\le1).
\]
It follows by the substitution \(t=y+\delta u\) that \(h(y)=F(y)/\delta\). Applying (2) to (1), uniformly in \(y_n\), yields
\[
r(n)=K_n h(y_n)+O(\log(2K_n+2))
=n\delta\frac{F(y_n)}{\delta}+O(\log(2n)),
\]
because \(K_n=\delta n+O(1)\) and \(0\le h\le1\). This proves the uniform formula, including the finitely many small values with \(K_n=0\).

**4. Limiting measure and effective rate.** Irrationality of \(\delta\) implies equidistribution of \(\{n\delta\}\) on \([0,1]\). Under uniform phase, \(F\) has a plateau of length \(1-2\delta\) at height \(\delta\), while each of the remaining two intervals of length \(\delta\) maps linearly and bijectively onto \([0,\delta]\) with slope of absolute value \(1\). Their pushforward density is therefore \(2\), proving the asserted \(\nu\).

For the claimed rate, let \(g:\mathbb R\to\mathbb R\) be any \(1\)-Lipschitz test function. The uniform estimate and the triangle inequality give
\[
\frac1X\sum_{n\le X}
|g(r(n)/n)-g(F(\{n\delta\}))|
\ll\frac1X\sum_{n\le X}\frac{\log(2n)}n
\ll\frac{\log^2(2X)}X.
\]
The periodic function \(g\circ F\) has total variation at most \(2\delta\), uniformly in \(g\). By (2), interval empirical-count discrepancies for the \(X\) rotation points are \(O(\log(2X))\). Integrating a bounded-variation function against the difference of empirical and Lebesgue measures, or equivalently using interval decomposition, shows
\[
\left|\frac1X\sum_{n\le X}g(F(\{n\delta\}))-\int_0^1g(F(y))\,dy\right|
\ll\frac{\log(2X)}X.
\]
Taking the supremum over \(1\)-Lipschitz \(g\) proves the Wasserstein bound by its Kantorovich-Rubinstein dual characterization. Finally, direct integration yields the mean
\[
(1-2\delta)\delta+2\int_0^\delta t\,dt
=\delta-\delta^2=\sqrt5-2.
\]
This finishes the proof.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It computes every \(\lfloor j\varphi\rfloor\) exactly as \(\left\lfloor\frac{j+\lfloor j\sqrt5\rfloor}{2}\right\rfloor\) and \(\lfloor j\sqrt5\rfloor=\operatorname{isqrt}(5j^2)\), and sets \(\lfloor j\varphi^2\rfloor=j+\lfloor j\varphi\rfloor\). Independent pair-convolution and direct membership tests agree with the phase-rotation formula for all \(1\le n\le4500\). The verifier also checks the complementarity partition, the OEIS initial terms, the profile error, and the limiting measure's mass. A sample run returned:

`VERIFY_OK exact_convolution_n=4500 rotation_n=4500 Beatty_partition=PASS profile=PASS max_error=1.821120@3025 law_mass=PASS`

Only exact integer arithmetic and high-precision decimal arithmetic enter the finite tests. These tests do **not** prove uniform asymptotics or weak convergence; those follow from the mathematical argument above. No auxiliary dataset is required.

## Relationship to prior work

Ashburn [1, Section 1] proves the cases \(r(n)=1,2\) and credits the classification of \(r(n)=0\) to Kawsumarng and collaborators. These statements describe exceptional small representation counts, whereas the theorem here describes the all-index linear-scale profile, an explicit atom-plus-uniform limiting law, and its effective convergence in Wasserstein distance. Shallit [2, Section 11.2] previously constructed a rank-\(19\) Fibonacci-automatic linear representation for the **same entire function \(r(n)\)**. This exact computational encoding is an important stronger antecedent in algorithmic coverage and must not be confused with an absence of previous formulas. The inspected sections of [2] state neither the phase profile nor the limiting distribution or the rate; the new proof exposes these quantitative statistics using circle rotations rather than automaton matrices. The OEIS entry [3] records the counting function and exceptional values but not the stated distribution. The later sumset paper [4] focuses on additive-basis thresholds for powers of the golden ratio rather than the mixed representation-count distribution; only its publicly retrieved abstract was inspected. An indexed or unindexed earlier theorem might imply the present conclusions and should be checked in an independent literature review.

## Limitations

The conclusion holds specifically for the complementary slopes \(\varphi\) and \(\varphi^2\). It does not classify all exact small values of \(r(n)\), prove a bounded absolute error, establish a sharper rate, or treat general irrational Beatty pairs. The \(O(\log n)\) estimate is intentionally an upper bound, not a claim of sharpness. The law has an atom: it is **not** fully continuous or Gaussian. The original work [2] already provides a finite-state exact representation of \(r(n)\); only the particular closed-form asymptotic profile, limit measure, and quantitative distributional consequence are asserted here. Bibliographic priority is subject to external verification; independent audit has not been performed.

## References

1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (first posted 2026-10-04 UTC), https://arxiv.org/abs/2610.04842.
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177v1 (2020), https://ar5iv.labs.arxiv.org/html/2006.04177.
3. C. Kimberling and contributors, OEIS A259598, *Number of representations of n as u(h) + v(k)*, https://oeis.org/A259598.
4. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, Electronic Research Archive 30 (2022), 2385–2405, https://doi.org/10.3934/era.2022121.
5. S. Kawsumarng, T. Khemaratchatakumthorn, P. Noppakaew, P. Pongsriiam, *Sumsets associated with Wythoff sequences and Fibonacci numbers*, Periodica Mathematica Hungarica 82 (2021), 98–113, https://doi.org/10.1007/s10998-020-00343-0.
