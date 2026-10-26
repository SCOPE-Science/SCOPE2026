# Sharp exterior \(L^2\) extrapolation for two real-frequency waves

## Finding

Let \(\mathcal E_2\) denote the nonzero exponential sums with at most two real frequencies,
\[
 g(t)=a e^{i\lambda t}+b e^{i\mu t},\qquad a,b\in\mathbb C,\quad \lambda,\mu\in\mathbb R,
\]
with coincident frequencies combined. For the probability-measure norm
\[
 \|g\|_{2,\mathrm{av}}^2=\frac12\int_{-1}^{1}|g(t)|^2\,dt,
\]
the exact frequency-uniform exterior evaluation constant is
\[
 \boxed{\sup_{0\ne g\in\mathcal E_2}\frac{|g(x)|^2}{\|g\|_{2,\mathrm{av}}^2}=1+3x^2\quad\text{for every real }|x|\ge1.}
\]
The supremum is **not attained** by any nonzero finite sum with two distinct real frequencies. It is approached by pairs of coalescing frequencies; their limiting extremizer is an affine function. Thus the sharp constant is an actual supremum, not a maximum.

## Assumptions and scope

All frequencies and the extrapolation point are real, coefficients may be complex, the observation interval is \([-1,1]\), and the training measure is normalized Lebesgue measure. There is no separation or frequency-magnitude assumption. One-frequency sums are allowed. The theorem concerns a fixed exterior point \(|x|\ge1\); it makes no assertion of the same formula for interior points or for three or more frequencies. A spatial interval \([-T,T]\), \(T>0\), follows by scaling with sharp coefficient \(1+3(x/T)^2\) when \(|x|\ge T\).

## Proof

**Step 1: the exact fixed-gap reproducing kernel.** For distinct frequencies, multiplication by a carrier \(e^{i\lambda t}\) changes neither the averaged norm nor the absolute evaluation. Reflection lets us take their gap \(d=|\mu-\lambda|>0\). The basis \(1,e^{idt}\) has Gram matrix and evaluation vector
\[
 G_d=\begin{pmatrix}1&s\\s&1\end{pmatrix},\quad s=\frac{\sin d}{d},\qquad v_x=\begin{pmatrix}1\\e^{idx}\end{pmatrix}.
\]
Here \(|s|<1\). Cauchy–Schwarz in the Gram inner product, with equality for the corresponding kernel vector, gives the **exact** maximum over coefficients at that fixed gap:
\[
 K_d(x)=v_x^*G_d^{-1}v_x
       =\frac{2(1-s\cos(dx))}{1-s^2}.
\]
For a single frequency, the squared evaluation-to-average ratio is exactly \(1\).

**Step 2: large gaps.** If \(d\ge2\), then \(|s|\le1/d\le1/2\) and, more precisely, \(|s|<1/2\). Consequently
\[
 K_d(x)\le \frac{2(1+|s|)}{1-s^2}=\frac2{1-|s|}<4\le1+3x^2
\]
for every \(|x|\ge1\).

**Step 3: small gaps.** Suppose \(0<d<2\), and put \(u=d^2\in(0,4)\) and \(q=1-s\). Then \(s>0\). Alternating Taylor bounds for \(\sin d/d\) give
\[
 q_0:=\frac u6-\frac{u^2}{120}\le q\le\frac u6\le\frac23.
\]
Consider the polynomial
\[
 F_u(q)=2q(3-2q)-(1-q)u.
\]
On this allowed interval,
\[
 \frac{\partial F_u}{\partial q}=6-8q+u\ge\frac23+u>0,
\]
and a direct exact factorization gives
\[
 F_u(q_0)=\frac{u^2(20+10u-u^2)}{3600}>0\qquad(0<u<4).
\]
Thus \(F_u(q)>0\), which is the strict inequality
\[
 \frac{su}{1-s^2}+\frac{1-s}{1+s}<3.
\]
Using \(\cos(dx)\ge1-u x^2/2\), we deduce
\[
 \begin{aligned}
 K_d(x)&\le\frac2{1+s}+\frac{su}{1-s^2}x^2\\
 &=1+\frac{1-s}{1+s}+\frac{su}{1-s^2}x^2\\
 &\le1+x^2\left(\frac{1-s}{1+s}+\frac{su}{1-s^2}\right)<1+3x^2,
 \end{aligned}
\]
since \(x^2\ge1\). This establishes the claimed universal inequality, strictly for every nonzero fixed-gap space.

**Step 4: sharpness and nonattainment.** Fix \(|x|\ge1\). The two-frequency sums
\[
 g_h(t)=\cos(ht)+3x\frac{\sin(ht)}h,\qquad h>0,
\]
use the distinct frequencies \(\pm h\) and converge uniformly on \([-1,1]\cup\{x\}\) to \(p_x(t)=1+3xt\) as \(h\downarrow0\). Since
\[
 \|p_x\|_{2,\mathrm{av}}^2=1+3x^2,\qquad p_x(x)=1+3x^2,
\]
their evaluation ratios tend to \(1+3x^2\). Every positive gap was strictly bounded above by the same value, and one-frequency sums have ratio \(1\). This proves sharpness and nonattainment.

## Verification

The standalone program `verify.py` checks the exact polynomial factorization and derivative identity, a positive-gap grid of the reproducing kernel, the convergence of the explicit two-frequency extremizing family, and a counterexample to naively continuing the formula into the interior. To run it in a directory containing the supplied file, execute `python verify.py` with SymPy installed. These finite numerical checks supplement rather than replace the proof for all real frequencies and extrapolation points.

## Relationship to prior work

Ruizhe Zhang's *Optimal Extrapolation Bounds for Sparse Fourier Sums* (first public version July 11, 2026; arXiv:2607.10501, inspected version 2 of October 13, 2026) gives a general Chebyshev-scale **upper bound up to constants**, not the exact coefficient \(1+3x^2\) for two frequencies. Its Section 5.3, equation (64), already gives the **standard fixed-frequency Gram representation**, so that representation is used here, not claimed as new. The new assertion is the exact **global optimization over arbitrary real frequency pairs**, including its strict nonattainment and sharp confluent limit. Earlier work of Chen and Price gives less precise sparse-Fourier extrapolation bounds; Erdélyi's 2016 theorems treat endpoint/inside-window Nikolskii inequalities, not this exact exterior coefficient. Indexed finite-group Fourier inequalities concern different domains and cannot directly imply the continuous-interval statement.

## Limitations

No full classification of all near-extremizing sequences or quantitative stability deficit is proved. The exact identity is restricted to at most two waves and the exterior region \(|x|\ge1\). In fact, the same formula does not continue into the interval: at \(x=0\), a frequency gap with \(\sin d<0\) gives \(K_d(0)=2/(1+\sin d/d)>2\), whereas \(1+3x^2=1\). The available literature survey cannot exclude an unindexed equivalent earlier result; the 2019 Chen–Price full text was not materially inspected, so its detailed scope remains a residual priority risk. The proof makes no claim about nonlinear regression guarantees beyond this evaluation constant.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first public version July 11, 2026; full revision inspected: October 13, 2026, https://arxiv.org/abs/2607.10501 and https://pdfs.assets.alphaxiv.org/2607.10501v2.pdf; especially Theorem 1.1, Section 5.3, equation (64), and Proposition 5.6.
2. Tamás Erdélyi, *Inequalities for Exponential Sums*, arXiv:1602.02315, 2016, https://arxiv.org/pdf/1602.02315; especially Theorems 2.3–2.6 on window norms and endpoint behavior.
3. Xue Chen and Eric Price, *Estimating the Frequency of a Clustered Signal*, ICALP 2019, DOI:10.4230/LIPIcs.ICALP.2019.36, https://doi.org/10.4230/LIPIcs.ICALP.2019.36; bibliographic/abstract evidence only for the present comparison.
4. Mathematical Reviews and zbMATH, MSC2020 42A05: trigonometric polynomials, inequalities and extremal problems, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=42A05.
