# The finite-to-Poisson optimizer transition for binomial atom reversal

## Finding
For each integer \(r\geq1\), allow both the trial count \(n\geq r\) and the common success probability \(0<p<1\) to vary in \(S\sim\operatorname{Bin}(n,p)\). Define the least mean needed for strict reversal of the endpoint and the \(r\)-th atom by
\[
\Theta_r=\inf\bigl\{np:\Pr(S=r)>\Pr(S=0),\ n\in\mathbb Z,\ n\ge r,\ 0<p<1\bigr\}.
\]
The exact result is
\[
\Theta_r=\begin{cases}
 r/2,&1\le r\le4,\\
 n_r/(1+\binom{n_r}{r}^{1/r}),&5\le r\le10,\\
 (r!)^{1/r},&r\ge11,
\end{cases}
\]
where
\[
(n_5,n_6,n_7,n_8,n_9,n_{10})=(7,10,15,25,51,294).
\]
For \(r\le10\), the unique trial count attaining the *equality boundary* at the minimal mean is \(n_r\) (with \(n_r=r\) for \(1\le r\le4\)). For \(r\ge11\), no finite trial count has the minimal boundary mean; it is approached only in the Poisson rare-event limit \(n\to\infty\), \(p\downarrow0\). In every regime strict reversal requires mean strictly above \(\Theta_r\), and means arbitrarily close from above are achievable. Consequently the finite-to-Poisson transition occurs exactly between \(r=10\) and \(r=11\).

## Assumptions and scope
Only independent identically distributed Bernoulli trials are considered: \(n\) is a positive integer, \(n\ge r\), and every trial has the same \(p\in(0,1)\). Both \(n\) and \(p\) are decision variables. No fixed-\(n\) constraint, restriction \(p\le1/2\), or statement about heterogeneous Poisson-binomial sums is asserted. The objective is a strict comparison of the *point probabilities* at \(r\) and \(0\), not a tail probability or a modal inequality.

Let \(B_r(x)=(\prod_{j=0}^{r-1}(x-j)/r!)^{1/r}\), defined for real \(x\ge r\), and let \(F_r(x)=x/(1+B_r(x))\). These are positive real-valued functions, with the conventional product for \(r=1\).

## Proof
**1. Exact fixed-count boundary.** The binomial formula yields
\[
\frac{\Pr(S=r)}{\Pr(S=0)}=\binom nr\left(\frac p{1-p}\right)^r.
\]
This ratio increases strictly in \(p\). Equality occurs uniquely at
\[
p_{n,r}=\frac1{1+\binom nr^{1/r}},\qquad np_{n,r}=F_r(n).
\]
The strict reversal is equivalent to \(p>p_{n,r}\). Since \(p_{n,r}<1\), any boundary mean can be approached from above with strict reversal. Therefore \(\Theta_r=\inf_{n\ge r}F_r(n)\).

**2. The continuous optimizer has only one turning point.** For \(r\ge2\) put \(a_j(x)=1/(x-j)\), \(j=0,\dots,r-1\). Logarithmic differentiation gives
\[
\frac{B'_r(x)}{B_r(x)}=\frac1r\sum_{j=0}^{r-1}a_j(x),\qquad
\frac{B''_r(x)}{B_r(x)}=
\left(\frac1r\sum_{j=0}^{r-1}a_j(x)\right)^2-
\frac1r\sum_{j=0}^{r-1}a_j(x)^2<0.
\]
The inequality is strict by Cauchy--Schwarz because the \(a_j(x)\) are not all equal. Thus \(B_r\) is strictly concave. Write \(Q_r(x)=xB'_r(x)-B_r(x)\). Then
\[
Q'_r(x)=xB''_r(x)<0,\qquad
F'_r(x)=\frac{1-Q_r(x)}{(1+B_r(x))^2}.
\]
Therefore \(F_r\) is strictly increasing, strictly decreasing, or first strictly decreasing and then strictly increasing; it can have at most one interior minimum.

**3. Endpoint signs.** At \(x=r\), \(B_r(r)=1\) and \(B'_r(r)=H_r/r\), where \(H_r=\sum_{j=1}^r1/j\). Hence
\[
Q_r(r)=H_r-1.
\]
The product expansion as \(x\to\infty\) gives
\[
B_r(x)=(r!)^{-1/r}\left(x-\frac{r-1}{2}+O(x^{-1})\right),
\quad \lim_{x\to\infty}Q_r(x)=L_r:=\frac{r-1}{2(r!)^{1/r}}.
\]
For \(r=2,3\), \(H_r-1<1\), so \(F_r\) increases and its least integer argument is \(n=r\). The case \(r=1\) follows directly from \(F_1(x)=x/(1+x)\). For \(r=4,\dots,10\), \(H_r-1>1\) but \(L_r<1\); thus a unique real \(x_r>r\) satisfies \(Q_r(x_r)=1\), and the minimizing integer lies among \(\lfloor x_r\rfloor,\lceil x_r\rceil\), truncated at \(r\).

The inequalities \(L_r<1\) for \(1\le r\le10\) are equivalent to
\[
(r-1)^r<2^r r!,
\]
all ten of which have exact integer certificates in `verify.py`. At \(r=11\), the reverse strict inequality holds: \(10^{11}>2^{11}11!\). It persists for all larger \(r\) by induction: if \(r!<((r-1)/2)^r\), then
\[
\frac{(r+1)!}{(r/2)^{r+1}}
<2\left(1+\frac1r\right)\left(1-\frac1r\right)^r
<\frac{2(1+1/r)}e<1\qquad(r\ge11).
\]
Consequently \(L_r>1\) for \(r\ge11\). Since \(Q_r\) decreases toward \(L_r\), \(Q_r(x)>1\) for every finite \(x\ge r\). Thus \(F_r\) strictly decreases, with infimum \(\lim_{x\to\infty}F_r(x)=(r!)^{1/r}\), never achieved at a finite count.

**4. Exact finite discrete optimization.** Strict concavity reduces each \(r=4,\dots,10\) to checking the one or two neighbors of a proposed minimizing integer. The exact comparisons (using only integer powers and binomial coefficients) establish

| \(r\) | unique minimizing \(n\) | boundary mean \(\Theta_r\) (approximate) |
|---|---:|---:|
| 4 | 4 | 2.0000000000 |
| 5 | 7 | 2.4661639772 |
| 6 | 10 | 2.9086543047 |
| 7 | 15 | 3.3332717261 |
| 8 | 25 | 3.7431836880 |
| 9 | 51 | 4.1409866362 |
| 10 | 294 | 4.5285056655 |

Specifically, let \(M=10^{40}\) and define the integer \(J_{n,r}=\lfloor M\binom nr^{1/r}\rfloor\). Its validity is checked by the integer inequality \(J_{n,r}^r\le M^r\binom nr<(J_{n,r}+1)^r\). The exact integer comparison
\[
a(M+J_{b,r}+1)<b(M+J_{a,r})
\]
implies \(F_r(a)<F_r(b)\) by interval bounds. `verify.py` checks this strict inequality for each listed optimum against both existing adjacent counts (only the right neighbor when \(n=r\)). The single-turning-point proof then makes these finitely many integer certificates global, without any numerical extrapolation. For \(r=1,2,3\), monotonicity already gives \(n=r\). This proves the stated classification and uniqueness. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 and the standard library only. It checks the ten factorial inequalities, the exact base inequality at \(r=11\), the decisive neighbor inequalities for each \(r=4,\ldots,10\) using rigorous 40-decimal-place integer enclosures, and 513 independent exact-rational binomial ratio identities. All checks passed on the packaged file. The unbounded-index and unbounded-real-variable portions follow from the written strict concavity and induction arguments; finite checks alone do not establish those steps.

## Relationship to prior work
Kleiner, *Why Distance Two Is Exceptional for Poisson--Binomial Point Probabilities* (arXiv:2610.10664v1, 7 October 2026), proves unrestricted heterogeneous-Bernoulli point-mass reversal thresholds \(T_{k,r}\) and gives the shifted-binomial boundary formula in Section 3. That formula supplies the fixed-count starting identity but does **not** minimize the homogeneous zero-versus-\(r\) boundary over the variable number of identical trials. Indeed, for \(r\ge3\) the unrestricted threshold \(T_{0,r}=1\) is driven by deterministic support shifts that cannot occur in a nondegenerate homogeneous binomial law. The present claim is the complete optimal-trial-count classification for the homogeneous family, including the previously unresolved finite-to-Poisson boundary at \(r=11\).

Gnedin, *Cross Modality of the Extended Binomial Sums* (arXiv:2408.06477), analyzes modes and likelihood maxima of binomial and extended Bernoulli sums. Its modal-ridge and trial-count comparisons concern different extrema and do not state the joint least-mean optimization for nonadjacent atoms at \(0\) and \(r\). The fixed-count binomial identity is elementary and is not claimed as new.

## Limitations
The theorem is exclusively about homogeneous binomial sums with a variable integer trial count, not all Poisson-binomial laws. It does not optimize gaps between two arbitrary positive indices, a fixed trial count, or a prescribed lower bound on the common success probability. The probability distributions at the equality boundary have tied atoms, not strict reversal. For \(r\ge11\), the Poisson law appears only as a limit of finite binomial experiments and is not itself one of the permitted experiments. The classification is self-reviewed, not independently audited; equivalence to a less readily indexed older extremal-binomial identity remains a literature risk.

## References
1. I. Kleiner, *Why Distance Two Is Exceptional for Poisson--Binomial Point Probabilities*, arXiv:2610.10664v1, first submitted 7 October 2026. https://arxiv.org/html/2610.10664v1.
2. A. Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477, first submitted 12 August 2024. https://arxiv.org/abs/2408.06477.
