# Fair switching maximizes annealed escape through complementary binary run holes

## Finding

For each integer \(k\geq3\), let \(T(x)=2x\pmod 1\) on \([0,1)\). At each discrete time independently choose either the dyadic cylinder \(H_0=[0,2^{-k})\) with probability \(p\in[0,1]\), or \(H_1=[1-2^{-k},1)\) with probability \(1-p\). Start \(X_0\) uniformly on \([0,1)\), independently of the hole choices. Let \(P_n(k,p)\) be the **joint (annealed) probability** that \(T^j X_0\) avoids the hole active at time \(j\) for every \(0\leq j<n\). Then

\[
\gamma_k(p):=-\lim_{n\to\infty}\frac1n\log P_n(k,p)=\log\frac{2}{\lambda_k(p)},
\]

where \(\lambda_k(p)\) is the unique number in \((1,2)\) solving

\[
\mathcal A_{k,p}(\lambda)\mathcal A_{k,1-p}(\lambda)=1,
\qquad
\mathcal A_{k,w}(\lambda)=\sum_{j=1}^{k-1}\lambda^{-j}+\frac{w\lambda^{-(k-1)}}{\lambda-w}.
\]

The escape rate \(\gamma_k(p)\) depends **strictly increasingly** on \(p(1-p)\). Hence \(p=1/2\) is its unique maximum, while \(p=0,1\) give its equal minimum. At \(p=1/2\), the Perron root is equivalently the unique root \(\lambda\in(1,2)\) of

\[
(2-\lambda)(2\lambda-1)\lambda^{k-2}=1.
\]

Uniformly for \(0\leq p\leq1\) as \(k\to\infty\),

\[
\gamma_k(p)=2^{-k}\left(\frac{p}{1+p}+\frac{1-p}{2-p}\right)+O(k4^{-k}).
\]

In particular,

\[
\lim_{k\to\infty}\frac{\gamma_k(1/2)}{\gamma_k(0)}=\frac43.
\]

Thus independent fair switching of two holes of the same (shrinking) size improves their annealed escape rate by a sharp limiting factor of \(4/3\) relative to leaving either hole open permanently.

## Assumptions and scope

The binary expansion is taken uniquely except at dyadic rationals, a Lebesgue-null set. An active hole is checked *before* applying \(T\) at the indicated time. Each hole has Lebesgue measure \(2^{-k}\). The randomness in the initial point and in every choice of active hole is independent; the conclusion is about probability averaged over both, **not** about almost-sure escape rates conditioned on a fixed infinite hole schedule. Endpoints \(p=0,1\) are included. All logarithms are natural. The asserted optimization is among independent identically distributed two-hole selections parametrized by \(p\), not among all deterministic or dependent schedules.

## Proof

**1. Exact weighted symbolic encoding.** Write a typical initial state as \(X_0=0.b_0b_1b_2\ldots\) in base two. The digits \(b_j\) are independent fair bits. At check \(j\), the hole \(H_0\) is hit precisely when \(b_j\ldots b_{j+k-1}=0^k\), and \(H_1\) precisely when this block is \(1^k\). Averaging the independent hole choice therefore assigns a weight \(1-p\) to every occurrence of \(0^k\), a weight \(p\) to every occurrence of \(1^k\), and weight one to every other \(k\)-block. Overlapping occurrences multiply their weights because hole choices are independent at distinct times.

Let \(W_L\) be the sum of these products over all binary words of length \(L\), applying a factor for every fully contained \(k\)-block. The exact finite-horizon identity is

\[
P_n(k,p)=2^{-(n+k-1)}W_{n+k-1}\qquad(n\geq0).
\]

Decompose every nonempty word uniquely into maximal monochromatic runs. A run of length \(\ell<k\) of color \(c\) has weight one. A run of length \(\ell\geq k\) has weight \(w_c^{\ell-k+1}\), where \(w_0=1-p\), \(w_1=p\). Its ordinary length generating function is

\[
R_w(z)=\sum_{\ell=1}^{k-1}z^\ell+\frac{wz^k}{1-wz}.
\]

Successive runs alternate colors, yielding the exact generating function

\[
\sum_{L\geq0}W_Lz^L
=\frac{(1+R_p(z))(1+R_{1-p}(z))}{1-R_p(z)R_{1-p}(z)}.
\]

**2. Spectral root and existence of the escape rate.** A separate finite transfer construction keeps the color of the last digit and the length of its terminal run truncated at \(k-1\). It has \(2(k-1)\) states \((c,j)\), \(1\leq j\leq k-1\). Appending the opposite color moves to \((1-c,1)\) with weight one. Appending the same color moves to \((c,\min(j+1,k-1))\), with weight one if \(j<k-1\) and weight \(w_c\) if \(j=k-1\). The resulting nonnegative matrix is primitive for all \(p\in[0,1]\): its underlying directed graph is strongly connected, and a positive self-loop exists at one or both saturated states.

Consequently the Perron--Frobenius theorem gives \(W_L=C_{k,p}\lambda^L(1+o(1))\) with \(C_{k,p}>0\) and \(\lambda>0\) the Perron root. The run generating function identifies that root through \(R_p(1/\lambda)R_{1-p}(1/\lambda)=1\), which is the displayed equation in \(\mathcal A_{k,w}\). For \(\lambda>1\), each factor is strictly decreasing, their product is greater than one as \(\lambda\downarrow1\) (because \(k\geq3\)) and less than one at \(\lambda=2\). Hence the unique root lies in \((1,2)\). The finite-horizon identity then yields \(\gamma_k(p)=\log(2/\lambda_k(p))\).

**3. Strict optimization.** Fix \(\lambda>1\) and abbreviate

\[
S=\sum_{j=1}^{k-1}\lambda^{-j},\quad c=\lambda^{-(k-1)},\quad x=p(1-p).
\]

Since \(0<c\leq S\), a direct algebraic identity gives

\[
\mathcal A_{k,p}(\lambda)\mathcal A_{k,1-p}(\lambda)
=S^2+\frac{Sc(\lambda-2x)+c^2x}{\lambda^2-\lambda+x}.
\]

Its derivative with respect to \(x\) is

\[
\frac{c\big[(c-2S)(\lambda^2-\lambda)-S\lambda\big]}
{(\lambda^2-\lambda+x)^2}<0.
\]

Because the left-hand side is also strictly decreasing in \(\lambda\), the unique solution \(\lambda_k(p)\) decreases strictly as \(x\) increases. Therefore \(\gamma_k(p)\) increases strictly with \(p(1-p)\), giving the asserted unique maximum and endpoint minima.

At \(p=1/2\), the two positive factors in the root equation agree, so each must equal one. Simplifying \(\mathcal A_{k,1/2}(\lambda)=1\) gives the displayed polynomial equation; the characterization \(\lambda\in(1,2)\) removes its extraneous boundary root \(\lambda=1\).

**4. Uniform shrinking-hole asymptotics.** For \(\lambda>1\), summation of the run series gives the exact identity

\[
\mathcal A_{k,w}(\lambda)
=\frac1{\lambda-1}\left[1-\lambda^{-(k-2)}\frac{1-w}{\lambda-w}\right].
\]

Set \(\varepsilon=2^{-k}\), \(\delta=2-\lambda_k(p)\). Uniformly over \(p\in[0,1]\), the root equation first implies \(\delta=O(\varepsilon)\): for \(k\geq3\), at \(\lambda=3/2\) the sum \(\sum_{j=1}^{k-1}\lambda^{-j}\) exceeds one, so the root belongs to \((3/2,2)\). Throughout this interval, the derivative of the product of the two run functions with respect to \(\lambda\) has absolute value at least \(1/4\). At \(\lambda=2\) that product differs from one by \(O(\varepsilon)\), uniformly in \(p\). Expanding the exact identity there then gives

\[
0=2\delta-4\varepsilon\left[\frac{p}{1+p}+\frac{1-p}{2-p}\right]
+O(k\varepsilon^2).
\]

Therefore \(\delta=2\varepsilon B(p)+O(k\varepsilon^2)\), with \(B(p)=p/(1+p)+(1-p)/(2-p)\), and

\[
\gamma_k(p)=-\log(1-\delta/2)
=\varepsilon B(p)+O(k\varepsilon^2)
\]

uniformly. Since \(B(1/2)=2/3\) and \(B(0)=1/2\), the ratio tends to \(4/3\).

## Verification

The included standalone `check_random_hole_depth.py` performs 160 exact-rational finite-horizon comparisons between direct enumeration of binary words and a separately implemented truncated-run transfer recurrence, for depths three through six and five rational switching probabilities. It also numerically checks the spectral root against 36 independently assembled transfer-matrix Perron eigenvalues, checks strict optimality and the fair-switching polynomial equation for representative depths, and tests the shrinking-hole asymptotic coefficient. These tests are corroborative; the proof above establishes the statements for every integer depth and every switching bias.

## Relationship to prior work

Atnip, Froyland, González-Tokman and Vaienti (2021, arXiv:2103.04712v1) establish a quenched pressure/escape framework for random interval maps with holes (especially Sections 13 and 15); this finding instead determines **annealed** survival and optimizes a specified iid hole law. Cheriyath and Agarwal (2019, arXiv:1905.11767v1) investigate escape into **fixed** unions of forbidden cylinders and the correlation-polynomial method. Georgiou, Dettmann and Altmann (2012, arXiv:1207.7000v1, Section II) explicitly describe averaged transfer matrices for independently randomized Markov-hole placements, a general principle that encompasses the finite-matrix calculation here. The present additional assertions are the all-depth strict optimal bias and its sharp \(4/3\) rare-hole gain, supported by a direct run-renewal argument.

For depth two, the deterministic complementary-hole scheduling problem has previously been treated separately; the theorem here deliberately assumes \(k\geq3\) and does not claim that a random schedule is globally optimal among deterministic schedules.

## Limitations

The escape rate is annealed, not quenched; averaging survival before taking the logarithm is essential. No assertion is made about almost-sure survivor dimensions or the optimal schedule among dependent/nonstationary hole rules. The correction \(O(k4^{-k})\) is uniform in switching bias but does not assert an explicit effective constant. General averaged-transfer formulations in earlier work may allow an alternative derivation of the specialized spectral equation; the claimed substantive extension is the sharp optimization and asymptotic comparison, not the general existence of a finite transfer matrix. Independent validation and exhaustive publication-priority assessment have not been performed.

## References

1. J. Atnip, G. Froyland, C. González-Tokman, and S. Vaienti, *Thermodynamic Formalism for Random Interval Maps with Holes*, arXiv:2103.04712v1 (first public March 8, 2021), https://arxiv.org/abs/2103.04712 . Sections 13 and 15.
2. H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767v1 (first public May 28, 2019), https://arxiv.org/abs/1905.11767 . Sections 2--4.
3. O. Georgiou, C. P. Dettmann, and E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, arXiv:1207.7000v1 (first public July 30, 2012), https://arxiv.org/abs/1207.7000 . Sections II--III.
