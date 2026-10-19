# Universal quadratic Doppler-zero census for positive two-scale Gaussian pulses

## Finding

For any fixed real parameters \(0<a<b\) and \(c>0\), put
\[
f(t)=e^{-\pi a t^2}+c e^{-\pi b t^2},\qquad
\mathcal A_f(\tau,\nu)=\int_{\mathbb R} f(t+\tau/2)f(t-\tau/2)e^{-2\pi i\nu t}\,dt.
\]
For \(T>0\), let \(N_+(T)\) be the number of real Doppler zeros \(\nu>0\) of \(\mathcal A_f(T,\nu)\), counted with their analytic multiplicities. Then \(N_+(T)\) is finite and
\[
\boxed{N_+(T)=\frac{(b-a)^2}{a+b}\,T^2+O_{a,b,c}(1)\quad(T\to\infty).}
\]
The leading coefficient is **independent of the positive mixing amplitude** \(c\). More precisely, for every \(K>0\) chosen sufficiently large depending on \(a,b,c\), all sufficiently large-\(T\) positive real Doppler zeros satisfy
\[
aT-\frac K T<\nu<bT+\frac K T,
\]
whereas every negative cosine lobe completely contained in
\[
[aT+K/T,\ bT-K/T]
\]
contains exactly two simple Doppler zeros. All other positive Doppler zeros are confined to a bounded number of edge lobes, with each lobe contributing at most two zeros counted with multiplicity. The zero-delay Doppler section \(\mathcal A_f(0,\nu)\) is strictly positive for all real \(\nu\).

Thus a positive two-width Gaussian pulse has quadratically many real ambiguity-function nulls along large-delay sections, even though the individual Gaussian ambiguity functions have no real zeros. For \(a=b\) or \(c=0\), the pulse reduces to a single Gaussian and this conclusion does not apply: its ambiguity function is everywhere positive.

## Assumptions and scope

The Fourier transform uses \(e^{-2\pi i\nu t}\). Both Gaussian terms are centered, real and strictly positive; \(a,b,c\) are fixed as \(T\to\infty\). The pulse is not assumed to have unit \(L^2\) norm, since multiplying it by a positive normalizing constant changes no zeros. The ambiguity function is even in each of its two real arguments. Only **real** Doppler zeros along fixed-delay sections are counted; complex-frequency zeros, other Gaussian mixtures, and uniformity as \(a\to b\) or \(c\downarrow0\) are not asserted.

## Proof

**Step 1: exact Gaussian decomposition.** Direct completion of squares in the four bilinear Gaussian terms gives, for real \(\tau,\nu\),
\[
\begin{aligned}
\mathcal A_f(\tau,\nu)={}&\frac{e^{-\pi(a\tau^2/2+\nu^2/(2a))}}{\sqrt{2a}}
+\frac{c^2e^{-\pi(b\tau^2/2+\nu^2/(2b))}}{\sqrt{2b}}\\
&+\frac{2c}{\sqrt{a+b}}
 e^{-\pi(ab\tau^2+\nu^2)/(a+b)}
 \cos\!\left(\frac{\pi(b-a)\tau\nu}{a+b}\right).
\end{aligned}
\tag{1}
\]
In particular, setting \(\tau=0\) makes all three contributions strictly positive, since the cosine is then one.

**Step 2: the positive envelope and the interference wedge.** Fix \(T>0\), take \(\nu\ge0\), and divide (1) by its strictly positive cross-term amplitude
\[
Q(T,\nu)=\frac{2c}{\sqrt{a+b}}e^{-\pi(abT^2+\nu^2)/(a+b)}.
\]
Writing
\[
\alpha=\frac{b-a}{a+b},\qquad \beta=\frac{\pi(b-a)}{2(a+b)},\qquad k_T=\pi\alpha T,
\]
and
\[
A_0=\frac{1}{2c}\sqrt{\frac{a+b}{2a}},\qquad
B_0=\frac c2\sqrt{\frac{a+b}{2b}},
\]
we get the exact normalized zero equation
\[
\boxed{h_T(\nu)=\cos(k_T\nu)+r_T(\nu)=0,}
\]
where
\[
r_T(\nu)=A_0e^{\beta(aT^2-\nu^2/a)}
+B_0e^{\beta(\nu^2/b-bT^2)}>0.
\tag{2}
\]
The first term of \(r_T\) decreases on \(\nu\ge0\), and the second increases. Choose \(K>0\) large enough that \(A_0e^{-\beta K}\) and \(B_0e^{-\beta K}\) are each less than \(1/4\), and \(A_0e^{\beta K}\) and \(B_0e^{\beta K}\) each exceed two. Then for all sufficiently large \(T\), elementary expansion at the four edges \(aT\pm K/T\) and \(bT\pm K/T\) yields
\[
\begin{array}{ll}
r_T(\nu)>1,&0\le\nu\le aT-K/T\quad\text{or}\quad\nu\ge bT+K/T,\\[2pt]
r_T(\nu)<1/2,&aT+K/T\le\nu\le bT-K/T.
\end{array}
\tag{3}
\]
Indeed \(aT^2-(aT\pm K/T)^2/a=\mp2K+O(T^{-2})\), and \((bT\pm K/T)^2/b-bT^2=\pm2K+O(T^{-2})\). On the inner interval the monotonicity of the two summands in (2) bounds their total by the sum of their respective small edge bounds. Since \(h_T\ge r_T-1\), (3) excludes all zeros outside the enlarged wedge.

**Step 3: two roots per interior negative lobe.** Consider the disjoint open negative lobes
\[
I_j(T)=\left(\frac{(2j+1/2)\pi}{k_T},\frac{(2j+3/2)\pi}{k_T}\right),\qquad j=0,1,2,\ldots .
\]
At either endpoint of any such lobe, \(h_T=r_T>0\). Its cosine midpoint satisfies \(\cos(k_T\nu)=-1\). If the whole lobe lies in the inner interval of (3), its midpoint has \(h_T<-1/2\); therefore there are at least two roots. To prove no more, differentiate (2). The decreasing exponential has
\[
\frac{d^2}{d\nu^2}e^{-\beta\nu^2/a}=
\left(\frac{4\beta^2\nu^2}{a^2}-\frac{2\beta}{a}\right)e^{-\beta\nu^2/a},
\]
which is strictly positive for \(\nu\ge aT/2\) once \(T\) is large; the increasing exponential has everywhere positive second derivative. Hence \(r_T''(\nu)>0\) throughout the enlarged wedge for large \(T\). On the negative part of each cosine lobe,
\[
h_T''(\nu)=-k_T^2\cos(k_T\nu)+r_T''(\nu)>0.
\]
Thus \(h_T\) is strictly convex there. An interior negative lobe contains exactly two roots and they are simple: strict convexity, positive endpoints and a negative midpoint force one simple crossing on each side. More generally any negative lobe meeting the enlarged wedge contains at most two roots counted with analytic multiplicity, including a possible double tangency. No zeros occur where the cosine is nonnegative.

**Step 4: sharp counting.** Negative lobes are spaced by exactly \(2\pi/k_T\), so their number fully contained in the inner wedge and their number meeting the enlarged wedge are both
\[
\frac{k_T}{2\pi}(b-a)T+O_{a,b,c}(1).
\]
The difference is bounded because the total width of the two edge layers is \(O(1/T)\), while the lobe spacing is \(\asymp1/T\). Combining the two-per-lobe lower and upper estimates yields
\[
N_+(T)=\frac{k_T}{\pi}(b-a)T+O_{a,b,c}(1)
=\frac{(b-a)^2}{a+b}T^2+O_{a,b,c}(1).
\]
This also establishes finiteness and the full real-zero localization asserted above. By evenness the number of nonzero real Doppler zeros of either sign is twice \(N_+(T)\), counted with multiplicity.

## Verification

The standalone file `check.py` requires `numpy`, `scipy`, and `mpmath`. Run `python check.py` in a Python environment with the versions noted in `requirements.txt`. It independently evaluates the defining even real integral at five parameter points with 55-decimal working precision and compares it to (1); all five relative discrepancies were below \(2\times10^{-55}\). It also counts real Doppler roots numerically across negative cosine lobes for five choices of \((a,b,c)\) and delays \(T=6,12,24\). For \((a,b)=(1,3)\), the predicted leading count is \(T^2\): with \(c=1\), the observed positive-Doppler counts were \(36,144,576\), and with \(c=0.1\), they were \(38,146,578\). All fifteen count discrepancies from the leading asymptotic were smaller than three in absolute value; these finite computations are not an exhaustive root census or an infinite proof. The exact integral, envelope, convexity and lobe-count argument establish the theorem for all parameters.

## Relationship to prior work

The bilinear Gaussian ambiguity identity and single-Gaussian zero-freeness are standard. Faulhuber (2015 preprint) develops Gaussian ambiguity functions in the geometry of Gabor systems; Gröchenig, Jaming and Malinnikova explicitly give the cross-ambiguity of two unequal-width Gaussians and study broader zero-free questions. The formula (1) follows from these elementary ingredients by bilinearity. The present claim is **not** novelty of the Gaussian integral or of its algebraic expansion: it concerns the sharp **real-zero asymptotic**, the two-sided Doppler wedge and the universality of the quadratic coefficient across all fixed positive weights. Neither inspected full-text source states those conclusions. Korevaar and coauthors give broader Hermite time-frequency identities; the accessible abstract does not resolve this particular zero census, but full-text access was unavailable during the comparison. Searches of mathematical records and relevant prior findings identified no claim that explicitly covers the asymptotic. An unindexed or inaccessible equivalent treatment remains possible.

## Limitations

This is a real-Doppler asymptotic for fixed unequal widths and strictly positive fixed mixing amplitude. The \(O(1)\) bound is not claimed uniform as either Gaussian component disappears, as the widths coalesce, or across arbitrarily many Gaussian scales. Individual finite-delay zero counts may vary with all parameters and include double tangencies; no universal exact formula for each finite delay is asserted. Bibliographic comparisons cannot prove publication priority. Independent mathematical validation has not been performed.

## References

1. M. Faulhuber, *Gabor Frame Sets of Invariance: A Hamiltonian Approach to Gabor Frame Deformations*, arXiv:1509.04603, first posted 2015-09-15; subsequently *J. Pseudo-Differ. Oper. Appl.* 7 (2016), 213–235. https://arxiv.org/abs/1509.04603
2. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner distribution and the short-time Fourier transform*, *Rev. Mat. Complut.* (published online 2019). https://doi.org/10.1007/s13163-019-00335-w
3. C. W. Korevaar, M. S. Oude Alink, P.-T. de Boer, A. B. J. Kokkeler and G. J. M. Smit, *Closed-Form Expressions for Time-Frequency Operations Involving Hermite Functions*, *IEEE Trans. Signal Process.* 64 (2016), 1383–1390. https://doi.org/10.1109/TSP.2015.2488580
