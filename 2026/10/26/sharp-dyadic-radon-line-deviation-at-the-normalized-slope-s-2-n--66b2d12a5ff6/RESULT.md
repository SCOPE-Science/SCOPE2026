# Sharp dyadic Radon-line deviation at the normalized slope \(s/2^n\)

## Finding
Let \(n\ge1\), \(N=2^n\), and let \(\delta_s(t)\) be the integer row offset of the single-quadrant approximate discrete Radon transform (ADRT), for \(0\le s,t<N\). Define the difference from the normalized-slope continuous line by
\[
E_n(s,t)=\delta_s(t)-\frac{st}{N}.
\]
For each fixed slope index \(s\), write \(s=\sum_{i=0}^{n-1}b_i2^i\) with \(b_i\in\{0,1\}\), and set \(x_0=0\), \(x_{i+1}=(x_i+b_i)/2\). Then its **exact**, slope-specific, uniform row error is
\[
\max_{0\le t<N}|E_n(s,t)|=\frac12\sum_{i=0}^{n-1}b_i(1-x_i).
\]
An extremizing column has reversed bits: its bit in position \(n-1-i\) equals \(b_i\). Across all slopes and columns, the **sharp** bound is
\[
\boxed{\max_{0\le s,t<2^n}|E_n(s,t)|=\frac n6+\frac7{18}+\frac{(-1)^n}{9\,2^n}.}
\]
This replaces the \(n/2\) upper bound quoted for precisely this normalization in the 2026 ADRT literature. The gap is asymptotically a factor of three in the leading logarithmic coefficient. It is an exact geometry-of-sampling statement, not a stability estimate for the inverse ADRT.

## Assumptions and scope
The row and column indexes are integers, \(n\ge1\), \(N=2^n\), and \(0\le s,t<N\). The horizontal column parameter is the **pixel index** \(t\), and the target straight line has slope \(s/N\), not the endpoint-joining slope \(s/(N-1)\). The digital offset is the bit-linear realization of the standard recursive dyadic digital line:
\[
\delta_s(t)=\sum_{j=0}^{n-1}t_j\left(\left\lfloor\frac{s}{2^{n-j-1}}\right\rfloor-\left\lfloor\frac{s}{2^{n-j}}\right\rfloor\right),\qquad t=\sum_{j=0}^{n-1}t_j2^j.
\]
The row intercept can be any integer \(h\): translation changes neither the error nor the stated extrema. The result concerns this digital-line family only, not arbitrary digital lines or non-dyadic image dimensions.

## Proof
**1. Separation by column bits.** Reverse the column bits by setting \(u_i=t_{n-1-i}\). Direct substitution gives
\[
E_n(s,t)=\sum_{i=0}^{n-1}u_i e_i(s),\quad e_i(s)=\left\lfloor\frac{s}{2^i}\right\rfloor-\left\lfloor\frac{s}{2^{i+1}}\right\rfloor-\frac{s}{2^{i+1}}.
\]
Because \(s/2^{i+1}=\lfloor s/2^{i+1}\rfloor+(b_i+x_i)/2\) and \(\lfloor s/2^i\rfloor=2\lfloor s/2^{i+1}\rfloor+b_i\),
\[
e_i(s)=\frac{b_i-x_i}{2},\quad x_i=\sum_{j=0}^{i-1}\frac{b_j}{2^{i-j}}.
\]
Thus \(e_i(s)>0\) exactly when \(b_i=1\) and \(e_i(s)\le0\) when \(b_i=0\). Independence of the column bits makes the positive maximum
\[
P(s)=\max_tE_n(s,t)=\frac12\sum_{i=0}^{n-1}b_i(1-x_i),
\]
attained by \(u_i=b_i\). The absolute value of the most negative error is \(Q(s)=-\min_t E_n(s,t)\). Since \(P(s)-Q(s)=\sum_i e_i(s)=\delta_s(N-1)-s(N-1)/N=s/N\ge0\), the absolute maximum is \(P(s)\). (The identity \(\delta_s(N-1)=s\) follows immediately by telescoping the bit-linear formula.) This also proves the slope-specific formula.

**2. Exact dynamic programming over slopes.** For an initial state \(x\in[0,1]\), let \(V_m(x)\) maximize \(\frac12\sum_{i=0}^{m-1}b_i(1-x_i)\) over all \(m\) future bits, where \(x_0=x\) and \(x_{i+1}=(x_i+b_i)/2\). It satisfies
\[
V_m(x)=\max\left\{V_{m-1}(x/2),\ \frac{1-x}{2}+V_{m-1}((1+x)/2)\right\}.
\]
The base case is \(V_1(x)=(1-x)/2\). We prove by induction the two-branch formula
\[
V_m(x)=\begin{cases}a_m-u_m x,&0\le x\le\tfrac12,\\a_m+\tfrac12-u_m-(1-u_m)x,&\tfrac12\le x\le1,\end{cases}
\]
where \(a_1=u_1=1/2\), \(a_m=a_{m-1}+(1-u_{m-1})/2\), and \(u_m=1-u_{m-1}/2\). Indeed, the induction hypothesis applied at \(x/2\) and \((1+x)/2\) gives the two candidates
\[
F_0(x)=a_{m-1}-\frac{u_{m-1}x}{2},\qquad
F_1(x)=a_{m-1}+\frac{1-u_{m-1}}2-\left(1-\frac{u_{m-1}}2\right)x.
\]
Their difference is \((1-u_{m-1})(1/2-x)\). As \(0<u_{m-1}<1\), the optimum uses bit one for \(x<1/2\), bit zero for \(x>1/2\), and either at equality. This proves the induction, including both endpoints.

**3. Solving the recurrences and attaining the bound.** The recurrences yield
\[
u_m=\frac23+\frac{(-1)^m}{3\,2^m},\qquad a_m=\frac m6+\frac7{18}+\frac{(-1)^m}{9\,2^m},
\]
which satisfy the base values and recurrences exactly. At the initial slope state \(x=0\), the full maximum equals \(V_n(0)=a_n\). A maximizing binary control word exists at every stage of this finite Bellman recursion, and its bits define an admissible slope index, while the bit-reversed column attains its positive error. Hence the bound is attained and exact for every \(n\ge1\). No asymptotic inference from finite enumerations is needed.

## Verification
`verify.py` implements the paper's bit-linear offset with integer shifts and an independently accumulated state-based fixed-slope formula using exact `fractions.Fraction` values. It exhaustively checks every slope through \(n=11\), each slope's bit-reversal witness, and all \((s,t)\) for \(n\le7\). It checks the symbolic closed form exactly as rational numbers. The companion `verification_output.txt` records the results; for example the maximum is \(441/256\) at \(n=8\), attained at slope indices \(171\) and \(213\). Computation is supplementary; the preceding argument proves every positive integer \(n\).

## Relationship to prior work
Kazimirov et al. (2026), whose first MSC is \(65\mathrm{R}10\), motivate quantitatively comparable Hough/Radon approximation errors and specifically discuss the classical Brady–Yong dyadic pattern. Rim (2026), Lemma 2.1, fixes the bit-linear ADRT offsets and states \(|\delta_s(t)-st/N|\le n/2\); the sharp formula above refers to exactly its \(s/N\) normalisation.

The existing sharp dyadic-line error literature is substantially stronger than this coarse inequality **for a different geometric target**: Ershov–Karpenko (2017) and Smirnov–Karpenko (2023) explicitly measure deviation from the endpoint-joining line with slope \(s/(N-1)\), and establish a logarithmic coefficient \(1/6\). The two comparison lines differ by \(st/[N(N-1)]\), varying with both slope and column. Their optimal **global** bound does not determine the sharp \(s/N\) maximum or its exact finite-size correction; it cannot simply be substituted for the value above. Neither the earlier chord result nor the 2026 coarse bound implies the slope-by-slope bit-reversal calibration as stated. This distinction is essential: the logarithmic order and the factor \(1/6\) are **not** asserted to be new.

## Limitations
The maximal error here concerns pixel-center vertical displacement, not Hausdorff distance to a continuum segment, normed forward-transform discrepancy for a function class, or accuracy/conditioning of any computed inverse. Known endpoint-joining geometry can have smaller maximum at finite sizes and must not be conflated with the stated normalized-slope geometry. Closely related older maximal-deviation work creates a residual risk of an equivalent \(s/N\) formula under alternate terminology; this work makes no claim of exhaustive literature coverage or independent certification. The practical consequences are certified row enclosures and per-slope geometric tolerances, not measured improvements in reconstruction performance.

## References
1. D. Kazimirov, V. Gulevskii, A. Kroshnin, E. Rybakova, A. Terekhin, E. Limonova, D. Nikolaev, “Universal Comparison Methodology for Hough Transform Approaches,” *Mathematics* 14 (2026), article 1136, https://doi.org/10.3390/math14071136. First published 2026-03-28.
2. D. Rim, “Explicit Oblique Inverses of the Approximate Discrete Radon Transform,” arXiv:2610.23363v1, 2026-10-16, Lemma 2.1, https://arxiv.org/abs/2610.23363.
3. E. I. Ershov, S. M. Karpenko, “Fast Hough Transform and Approximation Properties of Dyadic Patterns,” arXiv:1712.05615v1, 2017, https://arxiv.org/abs/1712.05615.
4. G. Smirnov, S. Karpenko, “Analyzing Deviations of Dyadic Lines in Fast Hough Transform,” arXiv:2311.10064v1, 2023, Proposition 1, https://arxiv.org/abs/2311.10064.
5. W. H. Press, “Discrete Radon transform has an exact, fast inverse and generalizes to operations other than sums along lines,” *PNAS* 103 (2006), 19249–19254, https://doi.org/10.1073/pnas.0609228103.
