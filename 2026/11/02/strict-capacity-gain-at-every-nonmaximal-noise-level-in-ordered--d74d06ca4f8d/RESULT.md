# Strict capacity gain at every nonmaximal noise level in ordered binary composite DNA

## Finding

Consider the ordered binary composite DNA channel of resolution two with two independent binary symmetric read channels of crossover probability \(p\in[0,1/2]\). Let \(C_{\mathrm{ord}}(p)\) denote its Shannon capacity in bits per composite letter. Let \(C_{\mathrm{rep}}(p)\) denote the capacity of the two-read binary repetition channel using only the composite symbols \(0\) and \(2\). **For every \(0\le p<1/2\),**

\[
C_{\mathrm{ord}}(p)>C_{\mathrm{rep}}(p).
\]

At \(p=1/2\), both capacities are zero. At \(p=0\), they equal \(\log_2 3\) and \(1\), respectively. For every \(0<p<1/2\), the capacity-achieving input distribution is unique and assigns strictly positive probability to *all three* composite symbols. Writing \(t=1-2p\) and \(\beta(t)\) for the probability assigned to the mixed symbol \(1\), its two endpoint probabilities are \((1-\beta(t))/2\), and

\[
\beta(t)=t^2-3t^4+\frac{34}{3}t^6+O(t^8),\qquad t\downarrow0.
\]

The capacity advantage has the sharper high-noise expansion

\[
C_{\mathrm{ord}}(p)-C_{\mathrm{rep}}(p)
=\frac{t^6-3t^8+\tfrac{32}{3}t^{10}+O(t^{12})}{\ln 2}
\quad (t=1-2p\downarrow0).
\]

In particular the gain is strictly positive throughout the entire nontrivial noise regime, but decays to zero at **sixth order** as the channel becomes pure noise.

## Assumptions and scope

The input alphabet is \(\{0,1,2\}\), decomposed into the *ordered* binary pairs \(00,01,11\). The two component bits are independently flipped with probability \(p\). The receiver retains the ordered pair, equivalently observing the four distinct labels \(0,1,2,?\), where \(?\) denotes the invalid reconstruction \(10\). Each channel use is independent. No constraint on the input distribution beyond the three allowed symbols is imposed.

For an alphabet of output pairs ordered as \((00,01,10,11)\), the transition matrix is

\[
W_p=\begin{pmatrix}
(1-p)^2&p(1-p)&p(1-p)&p^2\\
p(1-p)&(1-p)^2&p^2&p(1-p)\\
p^2&p(1-p)&p(1-p)&(1-p)^2
\end{pmatrix}.
\]

The comparison repetition channel restricts this matrix to its first and third rows and optimizes over its two input probabilities. Its capacity is

\[
C_{\mathrm{rep}}(p)=1+h_2(2p(1-p))-2h_2(p),
\]

where \(h_2(x)=-x\log_2 x-(1-x)\log_2(1-x)\), with the usual zero convention. All asymptotics are for the *fixed channel model* as \(p\uparrow1/2\), not a blocklength limit.

## Proof

**1. Symmetry and reduction.** The three rows of \(W_p\) have the same entropy, namely \(2h_2(p)\). Complementing and reversing both bits of the ordered output exchanges inputs \(0\) and \(2\) while fixing input \(1\). Symmetry and concavity therefore permit an optimal input law

\[
\mathbb P(X=0)=\mathbb P(X=2)=\frac{1-\beta}{2},\qquad
\mathbb P(X=1)=\beta,\qquad 0\le\beta\le1.
\]

When \(0<p<1/2\), the full two-bit binary-symmetric transition matrix is invertible, since its one-bit determinant is \(1-2p\ne0\). Thus its three selected rows are linearly independent. Distinct input laws induce distinct output laws, so strict concavity of output entropy makes the capacity-achieving input law **unique**, hence necessarily symmetric.

Set \(t=1-2p\), \(b=(1-t^2)/4\), and \(s=(1+t^2)/4\). The output probabilities in the order \((00,01,10,11)\) are \((u,v,w,u)\), where

\[
\begin{aligned}
u&=s-\frac{t^2\beta}{2},\\
v&=b+\frac{t(1+t)\beta}{2},\\
w&=b-\frac{t(1-t)\beta}{2}.
\end{aligned}
\]

With natural logarithms put

\[
F_t(\beta)=-2u\ln u-v\ln v-w\ln w.
\]

The ordered-channel capacity is \(\max_{0\le\beta\le1}F_t(\beta)/\ln2-2h_2(p)\). The repetition channel is exactly the restricted case \(\beta=0\): its equiprobable endpoints are optimal by symmetry and strict concavity. In that case \((u,v,w,u)=(s,b,b,s)\), yielding the asserted closed formula for \(C_{\mathrm{rep}}\).

**2. Interior uniqueness and strict capacity improvement.** For \(0<t<1\), every output probability is positive and direct differentiation gives

\[
F_t'(\beta)=t^2\ln u-\frac{t(1+t)}2\ln v+\frac{t(1-t)}2\ln w,
\]

and

\[
F_t''(\beta)=-\frac{t^4}{2u}-\frac{t^2(1+t)^2}{4v}-\frac{t^2(1-t)^2}{4w}<0.
\]

The endpoint derivatives simplify exactly to

\[
F_t'(0)=t^2\ln\!\left(\frac{1+t^2}{1-t^2}\right)>0,\qquad
F_t'(1)=t\ln\!\left(\frac{1-t}{1+t}\right)<0.
\]

Consequently there is a unique \(\beta(t)\in(0,1)\) satisfying \(F_t'(\beta(t))=0\). Its strict improvement over \(\beta=0\) proves the capacity inequality. This also gives an exact one-equation, unique-root characterization for the full positive-noise regime without relying on numerical optimization. At \(p=0\), the channel transmits three different ordered pairs noiselessly, so the optimal law is uniform and the capacities are \(\log_2 3\) and \(1\). At \(p=1/2\), all rows are uniform and both capacities vanish.

**3. Sharp high-noise law.** Because the four output probabilities are analytic and positive near \((t,\beta)=(0,0)\), the function \(t^{-2}F_t'(\beta)\) extends analytically across \(t=0\). Its value at \(t=0\) is \(-2\beta\), with derivative \(-2\) in \(\beta\), and \(t^{-2}F_t'(0)=\ln((1+t^2)/(1-t^2))\). The analytic implicit-function theorem therefore yields a unique small real-analytic solution \(\beta(t)\) with \(\beta(0)=0\). Direct formal expansion of the displayed derivative, with \(\beta(t)=c_2t^2+c_4t^4+c_6t^6+O(t^8)\), gives successively

\[
c_2=1,\qquad c_4=-3,\qquad c_6=\frac{34}{3}.
\]

The channel is unchanged in capacity by replacing \(t\) with \(-t\), which corresponds to complementing both received bits, so the optimized entropy and input probabilities are even in \(t\). Substituting the coefficients in \(F_t(\beta(t))-F_t(0)\) and expanding \(\ln(1+x)\) gives

\[
F_t(\beta(t))-F_t(0)=t^6-3t^8+\frac{32}{3}t^{10}+O(t^{12}).
\]

Division by \(\ln2\) completes the proof. All Taylor coefficients used here can also be checked using the independent, rational-arithmetic coefficient computation in `series_certificate.py`, but the analytic argument is not conditioned on finite numerical experiments.

## Verification

Run `python3 verify.py` and `python3 series_certificate.py` in the directory containing the supplied files (Python 3.11 or later; no third-party packages). The first program checks the complete \(3\times4\) channel matrix using exact rational arithmetic, compares all four output probabilities against independent direct mixtures, verifies conditional entropy, numerically locates unique roots by high-precision bisection at six noise levels, and tests the high-noise scaling. It prints `VERIFY_OK`. The second program carries out exact truncated formal-series arithmetic over \(\mathbb Q\), checks the stationary derivative coefficients and the entropy gain through degree ten, and prints `SERIES_CERTIFICATE_OK`. Output transcripts of these actual runs are included. These checks corroborate, but do not replace, the continuous-parameter proof.

## Relationship to prior work

Dollma, Elishco and Yaakobi introduce this ordered composite DNA channel, reduce its binary resolution-two capacity optimization to a symmetric one-variable distribution, and compare numerically with a two-copy binary channel; Section VI reports that the capacities are nearly equal for crossover probabilities above about \(0.3\). This work uses their model and reduction. The new assertions are the strict inequality for **all** \(p<1/2\), interior uniqueness for all positive nonmaximal noise, and the explicitly quantified sixth-order high-noise advantage and maximizing-input expansion. The source's numerical curves and unsolved capacity maximization are not presented as exact proofs of these assertions.

Mitzenmacher's multiple-version channel gives the comparison restricted to two identical binary inputs; it does not include the mixed input \(01\). The multinomial composite-DNA model of Kobovich, Yaakobi and Weinberger samples letters from a probability vector rather than transmitting two deterministically ordered component bits through independent BSCs. General finite-channel capacity formulas justify the entropy maximization but do not by themselves state the strict all-noise comparison or this high-order cancellation.

## Limitations

This is an analytic comparison and asymptotic characterization, **not** an elementary closed form for \(\beta(t)\) or the full capacity function at arbitrary noise. It concerns exactly binary ordered composite letters of resolution two, two independent equal-noise BSCs, and their binary repetition subchannel. Different read noise levels, unordered multinomial reads, larger resolutions, insertions, deletions, and operational coding complexities are outside the claim. The priority comparison is based on accessible literature and does not constitute exhaustive independent publication-priority certification.

## References

1. B. Dollma, O. Elishco, and E. Yaakobi, *Coding for Ordered Composite DNA Sequences*, arXiv:2509.26119, first public version dated 2025-09-30, especially Sections II and VI. https://arxiv.org/abs/2509.26119
2. M. Mitzenmacher, *On the Theory and Practice of Data Recovery with Multiple Versions*, 2006, bibliography and available abstract: https://www.eecs.harvard.edu/~michaelm/ListByYear.html
3. A. Kobovich, E. Yaakobi, and N. Weinberger, *M-DAB: An Input-Distribution Optimization Algorithm for Composite DNA Storage by the Multinomial Channel*, arXiv:2309.17193, first version dated 2023-09-29. https://arxiv.org/abs/2309.17193
4. A. Kobovich and N. Weinberger, *Input Optimization in the Composite DNA Storage Channel*, IEEE Journal on Selected Areas in Information Theory, 6 (2025), 248–260, DOI: 10.1109/JSAIT.2025.3595005. The accessible abstract describes a different multinomial model. https://cris.technion.ac.il/en/publications/input-optimization-in-the-composite-dna-storage-channel/
