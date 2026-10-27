# Sharp three-logarithm endpoint loss for the Boolean-cube Poisson Green operator

## Finding
For the unnormalized graph Laplacian \(L_d\) on the \(d\)-dimensional Boolean cube and its Moore–Penrose pseudoinverse \(G_d=L_d^{\dagger}\), the following exact and asymptotic statements hold for every integer \(d\ge1\):
\[
\|G_d\|_{\ell^\infty\to\ell^\infty}=\|G_d\|_{\ell^1\to\ell^1}=\sum_{k=0}^d\binom dk|g_d(k)|,
\qquad g_d(k)=2^{-d-1}\sum_{j=1}^d\frac{K_j^{(d)}(k)}j,
\]
where \(K_j^{(d)}(k)=\sum_{r=0}^j(-1)^r\binom kr\binom{d-k}{j-r}\), interpreted with out-of-range binomial coefficients zero. The radial entries \(g_d(0),\ldots,g_d(d)\) are strictly decreasing. The positive entries therefore form one Hamming ball, possibly with a zero boundary shell, and a row-wise sign function attains the sharp norm.

More precisely, as \(d\to\infty\), with natural logarithms,
\[
\boxed{\displaystyle \|G_d\|_{\ell^\infty\to\ell^\infty}=\frac12\log d-\frac12\log\log\log d+O(1).}
\]
The error is bounded independently of \(d\) for all sufficiently large \(d\). No explicit constant term or convergence of that remainder is asserted.

## Assumptions and scope
Let \(Q_d=\{0,1\}^d\), equipped with counting measure on its \(2^d\) vertices. For a function \(f\colon Q_d\to\mathbb R\), let
\[
(L_df)(x)=\sum_{i=1}^d\bigl(f(x)-f(x\oplus e_i)\bigr).
\]
The Moore–Penrose inverse acts as reciprocal \(1/(2j)\) on Walsh degree \(j\ge1\) and zero on constants. No normalization by the degree \(d\) is applied. The endpoint norms refer to the induced counting-measure \(\ell^1\) and maximum-coordinate \(\ell^\infty\) norms. The asymptotic is a statement for unbounded integer dimension, not a numerical fit.

## Proof
**1. Exact spectral and heat representations.** Walsh characters diagonalize \(L_d\) with eigenvalue \(2|S|\) for each subset \(S\subseteq\{1,\ldots,d\}\). Fourier inversion gives the stated Krawtchouk formula. Writing \(J_d\) for uniform averaging, the positive-time spectral identity is
\[
G_d=\int_0^\infty(e^{-tL_d}-J_d)\,dt.
\]
For \(k=\operatorname{dist}_H(x,y)\), put \(F_d(k)=2^dg_d(k)\). Independent coordinate-flip heat flow, followed by \(u=e^{-2t}\), gives
\[
F_d(k)=\frac12\int_0^1\frac{(1+u)^{d-k}(1-u)^k-1}{u}\,du.
\]
Consequently
\[
F_d(k)-F_d(k+1)=\int_0^1(1+u)^{d-k-1}(1-u)^k\,du>0
\]
for every \(0\le k<d\). The zero row sum of \(G_d\) forces both signs. Every row is a translate of the same radial row; hence its absolute row sum is the exact \(\ell^\infty\) norm, attained by the sign of that row. Symmetry of \(G_d\) gives equality with the \(\ell^1\) norm.

**2. Time-integrated extremizer and lower bound.** Let \(A_d\) be the positive portion of a fixed row, and let \(\nu_t\) be the heat-flow law from its center. Let \(U\) denote the uniform distribution. The row sum zero and the heat formula imply
\[
\|G_d\|_{\ell^\infty\to\ell^\infty}=2\int_0^\infty(\nu_t(A_d)-U(A_d))\,dt.
\]
Since the heat-flow Hamming weight has binomial law \(\operatorname{Bin}(d,(1-e^{-2t})/2)\), every lower Hamming ball has \(\nu_t(B)\ge U(B)\). More generally, for any such ball \(B\), the norm is at least \(2\int_0^\infty(\nu_t(B)-U(B))dt\).

Put \(H=\log\log d\), \(t_c=(\log d)/4\), and for sufficiently large \(d\) put
\[
t_0=t_c-\tfrac14\log H-\tfrac12\log8,
\quad B_d=\{x:\operatorname{dist}_H(x,0)\le d/2-2\sqrt{dH}\}.
\]
For every \(0\le t\le t_0\), the heat-flow expected Hamming weight is at most \(d/2-4\sqrt{dH}\). Hoeffding's binomial bound then gives \(\nu_t(B_d)\ge1-e^{-8H}\), while \(U(B_d)\le e^{-8H}\). Thus
\[
\|G_d\|\ge2t_0(1-2e^{-8H})=\tfrac12\log d-\tfrac12\log H-O(1).
\]

**3. Position of the sharp sign boundary.** Put \(m=\lfloor d/2\rfloor\) and \(H_m=\sum_{r=1}^m1/r\). Directly from the integral formula,
\[
F_{2m}(m)=-\tfrac14H_m,
\qquad F_{2m+1}(m)=-\tfrac14H_m+\tfrac12\int_0^1(1-u^2)^mdu.
\]
In either parity, \(F_d(m)\le-\tfrac14H_m+\tfrac12\). Moreover, for \(0\le j<d\), the exact increment equals
\[
I_{d,j}:=F_d(j)-F_d(j+1)=2^d\int_0^{1/2}x^j(1-x)^{d-j-1}dx
\le\frac{2^d}{d\binom{d-1}{j}}.
\]
The elementary central-binomial product estimate (obtainable by dividing the \(j\)-th binomial coefficient by the central one and bounding the logarithms of its factors) supplies an absolute \(c>0\) such that, uniformly for \(|j-m|\le s\ll d\),
\[
\binom{d-1}{j}\ge c\frac{2^{d-1}}{\sqrt d}\exp\!\left(-16\frac{(s+1)^2}{d}\right).
\]
Take \(s=\lfloor\sqrt{dH}/8\rfloor\). Summing the increments from \(m-s\) to \(m-1\) yields
\[
0\le F_d(m-s)-F_d(m)\le C\sqrt H\,e^{H/4+o(H)}=o(\log d),
\]
since \(\log d=e^H\). Meanwhile \(F_d(m)\le-\tfrac14\log d+O(1)\). Hence \(F_d(m-s)<0\) for all sufficiently large \(d\), so strict radial monotonicity implies, with \(\beta=1/16\),
\[
A_d\subseteq\{x:\operatorname{dist}_H(x,0)\le d/2-\beta\sqrt{dH}\}.
\]

**4. Upper bound from a tail estimate.** Define \(t_1=t_c-\tfrac14\log H+\tfrac12\log(1/\beta)\). For all sufficiently large \(d\), \(t_1<t_c\). For \(t\ge t_1\), the mean Hamming weight is at least \(d/2-(\beta/2)\sqrt{dH}\), so Hoeffding gives \(\nu_t(A_d)\le e^{-\beta^2H/2}\). The integral over \([0,t_1]\) is at most \(t_1\). The portion \([t_1,t_c]\) is at most \((t_c-t_1)e^{-\beta^2H/2}=o(1)\). Finally, writing \(u=e^{-2t}\), the exact chi-square divergence of the product Bernoulli heat law from \(U\) is \((1+u^2)^d-1\). Hence for \(t\ge t_c\),
\[
0\le\nu_t(A_d)-U(A_d)\le\|\nu_t-U\|_{\mathrm{TV}}
\le\tfrac12\sqrt{\exp(e^{-4(t-t_c)})-1}.
\]
Its integral on \([t_c,\infty)\) is bounded by an absolute constant. Combining these bounds,
\[
\|G_d\|\le2t_1+O(1)=\tfrac12\log d-\tfrac12\log H+O(1).
\]
The lower and upper bounds agree because \(\log H=\log\log\log d\), completing the proof.

## Verification
The included standard-library script `check.py` reconstructs every Krawtchouk coefficient using exact integers, computes the rational Green entries, checks strict radial monotonicity and vanishing row sums, checks the exact norm identity, and independently inverts \(L_d+J_d\) for dimensions one through five to test \(G_d=(L_d+J_d)^{-1}-J_d\). It passes 3,810 exact-rational assertions over dimensions one through thirty. All-dimensional asymptotics follow from the preceding estimates, not from these finite tests.

## Relationship to prior work
Ellis's 2003 full-text treatment gives spectral Green operators for Cartesian products of regular graphs, including a general product spectral formula; it provides the underlying Green-operator framework but does not assert an endpoint norm or its three-logarithm correction. Cox–Peres–Steif (arXiv:1408.5122, first public version 21 August 2014) discusses cutoff for independent-coordinate hypercube dynamics at time \((\log d)/4\) with bounded mixing window. Cutoff for each fixed time does not determine a common extremizing sign pattern for the time-integrated Green kernel. The present norm asymptotics require the sign-boundary estimate above. Diaconis–Graham–Morrison's 1990 hypercube-walk paper is relevant historical background, but its complete text was unavailable in this review; no priority assertion about its complete contents is made.

## Limitations
The \(O(1)\) error is not resolved into a limit or exact third term. The normalization is crucial: using the degree-normalized Laplacian multiplies the stated inverse norm by \(d\). Historical priority remains provisional, particularly for inaccessible older random-walk sources and synonymous terminology for Green operators or deviation matrices. No independent validation has been performed.

## References
1. Robert B. Ellis, *Discrete Green's functions for products of regular graphs*, arXiv:math/0309080v2 (first public version 4 September 2003), Sections 2, 4, 5, https://arxiv.org/html/math/0309080v2.
2. J. T. Cox, Y. Peres and J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122 (first public version 21 August 2014), https://arxiv.org/abs/1408.5122.
3. P. Diaconis, R. L. Graham and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72, doi:10.1002/rsa.3240010105 (historical comparison, full text not accessible).
