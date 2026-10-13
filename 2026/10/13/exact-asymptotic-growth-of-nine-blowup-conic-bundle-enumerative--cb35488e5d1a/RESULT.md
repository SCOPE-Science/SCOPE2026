# Exact asymptotic growth of nine-blowup conic-bundle enumerative invariants
## Finding
For a smooth real rational surface \(X\) carrying a real conic bundle with \(K_X^2=0\), eight singular conic fibers, and \(X(\mathbb R)\ne\varnothing\), use the deformation-independent bidegree invariants of Finashin–Kharlamov. Write \(G_n=GW_{1,n}\) for their aggregate genus-zero Gromov–Witten count, \(M_n=GW^{[2]}_{1,n}\) for its root-weighted second moment, and \(W_n=\mathscr N_{2,2n}=M_n/4\) for the corresponding wall-crossing-invariant signed real count. Then, as \(n\to\infty\) through all nonnegative integers,
\[
G_n\sim \frac{e^{2\pi\sqrt{n+1}}}{2(n+1)^{7/4}},\qquad
W_n\sim \frac{e^{2\pi\sqrt{n+1}}}{8\pi(n+1)^{5/4}},\qquad
\frac{W_n}{G_n}\sim\frac{\sqrt{n+1}}{4\pi}.
\]
In particular, neither sequence exhibits an even/odd leading-term oscillation despite the doubled-argument partition product in its generating function. The exact exponential rate and both leading constants hold uniformly throughout this deformation class.
## Assumptions and scope
All enumerative invariants and bidegrees are in the normalization of Finashin–Kharlamov, *On wall-crossing invariant combinations of Welschinger numbers for rational surfaces with a conic bundle*, arXiv:2610.02445v1, Sections 1 and 7. The surface is smooth, projective and rational over \(\mathbb C\), defined over \(\mathbb R\), with nonempty real locus and a real conic-bundle structure. For its fiber class \(C\), the bidegree of a curve class \(\alpha\) is \((-K_X\cdot\alpha,C\cdot\alpha)\). Set \(q=e^{\pi iz}\) for \(\operatorname{Im}z>0\) and let
\[
\theta_3(q)=\sum_{a\in\mathbb Z}q^{a^2},\quad
\theta_4(q)=\theta_3(-q),\quad
\theta_2(q)=\sum_{a\in\mathbb Z}q^{(a+1/2)^2},\quad
P(q)=\prod_{j\ge1}(1-q^{2j})^{-12}.
\]
Fractional powers occurring in \(\theta_2\) disappear from the fourth and eighth powers in the identities below. The source's deformation-invariance theorem identifies the sequences for all such conic bundles. The result concerns the particular first-anticanonical-degree row as the conic-bundle degree tends to infinity; it does not give asymptotics in the first degree simultaneously.
## Proof
**Step 1: Fix the complete generating functions and their normalization.** Sections 7.1 and 7.2 of the initiating paper provide
\[
\sum_{n\ge0}G_nq^{n+1}=F(q)P(q),\qquad
\sum_{n\ge0}M_nq^{n+1}=\tfrac14(q\partial_qF(q))P(q),
\]
where \(F(q)=(\theta_3(q)^8-\theta_4(q)^8+\theta_2(q)^8)/2\). The second equality follows directly from the paper's root-moment theta derivatives (its Equations (7.2.2)–(7.2.4)), including the \(1/4\) factor. It also follows independently from the shell description: in either coordinate-parity lattice shell of squared norm \(N\), coordinate symmetry gives \(\sum x_1^2=(N/8)\#\{\text{shell points}\}\), and the root normalization multiplies this coordinate moment by \(2\). Hence the weighted shell series is \(\tfrac14 q\partial_qF\), without relying on any tabulated coefficients. The Jacobi quartic theta identity \(\theta_3^4=\theta_2^4+\theta_4^4\) gives the useful exact factorization
\[
F(q)=\theta_2(q)^4\theta_3(q)^4.
\]
The real count is \(W_n=M_n/4\) by the paper's even-index comparison theorem at first degree. Both sequences therefore have strictly positive coefficients, and the following analytic coefficient calculation is legitimate.

**Step 2: Dominant cusp.** Put \(q=e^{-w}\), with \(\operatorname{Re}w>0\) and \(|\operatorname{Im}w|=o(\operatorname{Re}w)\). Poisson summation for the shifted and unshifted lattice theta sums gives, uniformly on such sectors,
\[
\theta_2(e^{-w})\sim(\pi/w)^{1/2},\qquad
\theta_3(e^{-w})\sim(\pi/w)^{1/2}.
\]
The Dedekind eta transformation, applied to \(P\), gives
\[
P(e^{-w})=\left(\frac{w}{\pi}\right)^6
\exp\left(\frac{\pi^2}{w}-w\right)
\bigl(1+O(e^{-c\operatorname{Re}(1/w)})\bigr)
\]
for a fixed \(c>0\) on a sufficiently narrow sector. Consequently
\[
F(e^{-w})P(e^{-w})\sim\frac{w^2}{\pi^2}e^{\pi^2/w},\quad
\tfrac14(q\partial_qF)(e^{-w})P(e^{-w})\sim\frac{w}{\pi^2}e^{\pi^2/w}.
\]
For the second equivalence use \(q\partial_q=-\partial_w\), which differentiates the dominant \(\pi^4w^{-4}\) into \(4\pi^4w^{-5}\).

**Step 3: Exclude the competing cusp and all minor arcs.** The partition product \(P\) is invariant under \(q\mapsto-q\), so the angle \(\pi\) might otherwise produce a second leading contribution. Instead, the Jacobi identity gives the *exact* cancellation
\[
F(-q)=-\theta_2(q)^4\theta_4(q)^4.
\]
For \(q=e^{-w}\) near the positive radial axis, the Poisson transformation of \(\theta_4\) gives \(\theta_4(e^{-w})=O(|w|^{-1/2}e^{-\pi^2\operatorname{Re}(1/w)/4})\). Thus \(F(-e^{-w})\) and its logarithmic derivative are exponentially small compared with their positive-cusp counterparts; multiplying by \(P(e^{-w})\) leaves only polynomial growth, not the \(e^{\pi^2/w}\) growth of the positive cusp.

Here is an explicit global minor-arc estimate. On the circle \(|q|=e^{-t}\) put \(\delta=\operatorname{dist}(\arg q,\pi\mathbb Z)\in[0,\pi/2]\), \(a=e^{-2t}\). Expanding the logarithm of the product and keeping only the nonnegative summand with logarithmic index one yields
\[
\log\frac{P(e^{-t})}{|P(e^{-t+i\arg q})|}
\ge12\sum_{j\ge1}a^j(1-\cos(2j\delta))
=\frac{12a(1+a)(1-\cos(2\delta))}{(1-a)((1-a)^2+2a(1-\cos(2\delta)))}.
\]
For all sufficiently small \(t\), this is at least \(c\delta^2/[t(t^2+\delta^2)]\) for a constant \(c>0\). Thus, outside \(t^{3/2-\varepsilon}\)-neighborhoods of angles zero and \(\pi\), \(P\) loses a factor \(e^{-c't^{-2\varepsilon}}\). Since \(F\) and \(q\partial_qF\) have nonnegative coefficients, their absolute values on the circle are bounded by \(O(t^{-4})\) and \(O(t^{-5})\), respectively. Their minor-arc integrals are negligible against the main saddle. The negative cusp is negligible by the preceding theta cancellation.

**Step 4: Evaluate the saddle with the exact constants.** Write \(N=n+1\) and take the Cauchy coefficient circle at \(t=\pi/\sqrt N\). In the central arc, put \(w=t-i\vartheta\). For any fixed \(0<\varepsilon<1/6\), throughout the window \(|\vartheta|\le t^{3/2-\varepsilon}\), which contains the entire Gaussian saddle scale, the phase \(Nw+\pi^2/w\) has the uniform expansion
\[
Nt+\frac{\pi^2}{t}-\frac{\pi^2\vartheta^2}{t^3}+o(1),
\]
where the linear term vanishes because \(Nt^2=\pi^2\), and the omitted cubic term is uniformly \(O(t^{1/2-3\varepsilon})=o(1)\). Outside the displayed window, the explicit product bound from Step 3 makes the remaining contour exponentially negligible. The Gaussian integral \(\int_{\mathbb R}e^{-\pi^2\vartheta^2/t^3}\,d\vartheta=\sqrt\pi\,t^{3/2}/\pi\), including the \(1/(2\pi)\) coefficient-extraction factor, gives the general leading term
\[
[q^N]c\,w^\beta e^{\pi^2/w}
\sim \frac{c\,\pi^{\beta+1/2}}{2\sqrt\pi}\,
N^{-\beta/2-3/4}e^{2\pi\sqrt N}.
\]
The two established dominant expansions have respectively \((c,\beta)=(\pi^{-2},2)\) and \((\pi^{-2},1)\). Their constants become \(1/2\) and \(1/(2\pi)\). Finally divide the latter by four for \(W_n\); taking the quotient proves the third displayed equivalence.
## Verification
The accompanying standalone `verify.py` computes the theta coefficients by direct power-series multiplication and independently by the eight-square/divisor-sum formula; it then compares the two paths with the \(12\)-colored partition recurrence and the derivative-weighted moment. All integer checks are exact. It also prints ratios of exact coefficients to the claimed asymptotic expressions for growing indices; those ratios are only numerical sanity checks and are not substitutes for the circle argument. Execute `python3 verify.py` in a directory containing this document and the script.
## Relationship to prior work
Finashin–Kharlamov, arXiv:2610.02445v1, prove deformation invariance and the theta–Euler-product formulas at \(K^2=0\) (Theorems 7.1.5 and 7.2.2 and Section 1), but do not give large-conic-degree asymptotics. Their earlier arXiv:2203.10503v2 treats del Pezzo surfaces with positive \(K^2\) and growth in anticanonical degree, a different limiting regime. Bryan–Leung, arXiv:alg-geom/9711031, provide the fixed-section partition product that is used in the later work. General theta, eta and partition circle methods are classical; the exact geometric normalization, the cancellation of the second cusp, and the resulting asymptotic constants for these specific wall-crossing-invariant sequences are the additional conclusions here.
## Limitations
The result is an asymptotic as the **second** grading grows while the first grading is fixed. It does not classify individual curve classes, establish an error term with an explicit universal constant, or extend to surfaces with empty real locus or other canonical self-intersections. Although the analysis is a proof for every sufficiently large index, numerical coefficient checks are finite. The originality comparison covers identified primary sources and indexed research; unindexed treatments of similar eta-quotient asymptotics remain a bibliographic risk. Independent external audit has not been performed.
## References
1. S. Finashin and V. Kharlamov, *On wall-crossing invariant combinations of Welschinger numbers for rational surfaces with a conic bundle*, arXiv:2610.02445v1 (2026), especially Sections 1, 7, 8: https://arxiv.org/html/2610.02445v1.
2. S. Finashin and V. Kharlamov, *On wall-crossing invariance of certain sums of Welschinger numbers*, arXiv:2203.10503v2 (first public 2022): https://arxiv.org/html/2203.10503v2.
3. J. Bryan and N. C. Leung, *The enumerative geometry of K3 surfaces and modular forms*, J. Amer. Math. Soc. 13 (2000), 371–410, arXiv:alg-geom/9711031: https://arxiv.org/abs/alg-geom/9711031.
4. Classical Jacobi theta, Poisson summation and Dedekind eta transformation identities, with the standard product-expansion proof of the minor-arc bound reproduced above.
