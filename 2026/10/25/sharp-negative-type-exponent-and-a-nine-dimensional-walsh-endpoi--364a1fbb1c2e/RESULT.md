# Sharp negative-type exponent and a nine-dimensional Walsh endpoint collapse on the folded nine-cube

## Finding
The canonical 256-vertex folded nine-cube has exact supremal powered-distance negative-type exponent \(p_*\), the unique root in \((0,1/3)\) of
\[
14\cdot4^{p_*}-28\cdot3^{p_*}+20\cdot2^{p_*}-7=0.
\]
Numerically \(p_*=0.323267128142707\ldots\). Its shortest-path metric raised to \(p\) is conditionally negative semidefinite exactly for \(0<p\le p_*\). The least dimension of a Euclidean realization with squared distances \(d^p\) is 255 below this endpoint and 246 at it. The nine lost dimensions are exactly the Walsh-weight-eight sector. The kernel \(\exp(-t d^p)\) is positive semidefinite for every \(t>0\) exactly on the same exponent interval; throughout that interval it is strictly positive definite for each \(t>0\).

## Assumptions and scope
Let \(X=\mathbb F_2^9/\langle\mathbf1\rangle\), with \(\mathbf1=(1,\ldots,1)\). For all classes \([x],[y]\in X\), define \(d([x],[y])=\min\{\mathrm{wt}(x-y),9-\mathrm{wt}(x-y)\}\), which is the graph metric of the antipodal quotient of the nine-dimensional Boolean hypercube. We adopt \(0^p=0\) for \(p>0\). A symmetric real matrix \(D\) is conditionally negative semidefinite when \(\sum_{x,y}c_xc_yD(x,y)\le0\) for every real vector \(c\) satisfying \(\sum_xc_x=0\). All exponents are real and positive; the theorem concerns all 256 quotient vertices, not an induced subgraph.

## Proof
**Walsh decomposition and exact eigenvalues.** The even-weight characters \(\chi_S([x])=(-1)^{\sum_{i\in S}x_i}\), \(|S|=k\in\{0,2,4,6,8\}\), form a complete Fourier basis on \(X\): they are precisely the characters invariant under \(x\mapsto x+\mathbf1\). The multiplicity of weight \(k\) is \(\binom9k\). For \(k\ne0\), the convolution matrix \(D_p\) has Fourier eigenvalue
\[
\lambda_k(p)=\sum_{j=1}^4 j^pK_j(k),\qquad
K_j(k)=\sum_{h=0}^j(-1)^h\binom kh\binom{9-k}{j-h}.
\]
There is no factor of two: each antipodal pair has one representative and each distance shell \(1\le j\le4\) has exactly \(\binom9j\) representatives. Evaluation of the four Krawtchouk vectors gives
\[
\begin{aligned}
\lambda_2&=5+8\cdot2^p-14\cdot4^p,\\
\lambda_4&=1-4\cdot2^p-4\cdot3^p+6\cdot4^p,\\
\lambda_6&=-3+8\cdot3^p-6\cdot4^p,\\
\lambda_8&=-7+20\cdot2^p-28\cdot3^p+14\cdot4^p.
\end{aligned}
\]
Their multiplicities are respectively \(36,126,84,9\). Thus conditional negative semidefiniteness is equivalent to all four being nonpositive.

**Uniqueness of the controlling crossing.** Set \(a=2^p\ge1\) and \(\alpha=\log_2 3\in(3/2,8/5)\). The last eigenvalue becomes \(f(a)=14a^2-28a^\alpha+20a-7\). Its derivative at 1 is \(48-28\alpha>0\); moreover
\[
f''(a)=28\bigl[1-\alpha(\alpha-1)a^{\alpha-2}\bigr]>0\quad(a\ge1)
\]
because \(\alpha(\alpha-1)<(8/5)(3/5)<1\). Hence \(f\) is strictly increasing for \(a\ge1\), starting at \(f(1)=-1\), and has a unique zero. It lies below \(p=1/3\): exact rational cubing establishes
\[
\frac{12599}{10000}<\sqrt[3]2,\quad\sqrt[3]3<\frac{14423}{10000},\quad\frac{15874}{10000}<\sqrt[3]4,
\]
so \(\lambda_8(1/3)>-7+20(12599/10000)-28(14423/10000)+14(15874/10000)=93/2500>0\).

**Every competing character stays strictly negative.** On \(0\le p\le1/3\), put \(a=2^p\le2^{1/3}<A=63/50\). The weight-two multiplier \(5+8a-14a^2\) strictly decreases from \(-1\) for \(a\ge1\). For weight four, \(3^p=a^\alpha\ge a^{3/2}\), hence \(\lambda_4\le P(a)=1-4a-4a^{3/2}+6a^2\). Since \(P'(a)=-4-6\sqrt a+12a>0\) for \(a\ge1\), and \(\sqrt A>28/25\),
\[
\lambda_4\le P(a)\le P(A)<1-4A-4A(28/25)+6A^2=-199/1250<0.
\]
For weight six, \(\beta=\log_4 3<9/10\). Concavity of \(s^\beta\) gives \(3^p=(a^2)^\beta\le1+\beta(a^2-1)\le 1/10+9a^2/10\), whence
\[
\lambda_6\le-11/5+(6/5)a^2\le-11/5+(6/5)A^2=-1843/6250<0.
\]
The elementary inequalities \(3^2>2^3\), \(3^5<2^8\), \(3^{10}<4^9\) justify the rational exponent bounds. The displayed rational root bounds are certified by cubing positive rational endpoints. Therefore precisely \(\lambda_8\) changes sign at \(p_*\), and for \(p>p_*\) it is positive. This proves the complete negative-type classification.

**Ranks and Gaussian kernels.** With \(H=I-\mathbf1\mathbf1^{\mathsf T}/256\), the centered Gram matrix \(-HD_pH/2\) has strictly positive eigenvalues on all 255 nonconstant Walsh characters for \(p<p_*\), and loses exactly \(\binom98=9\) dimensions at the endpoint. The standard squared-Euclidean distance criterion then yields dimensions 255 and 246, respectively. For \(p\le p_*\), these 256 distinct metric points admit an injective squared-Euclidean embedding, so the Gaussian kernel \(e^{-t\|v_x-v_y\|^2}\) is strictly positive definite for every \(t>0\). Conversely, when \(p>p_*\), a zero-sum weight-eight character \(c\) satisfies \(c^{\mathsf T}D_pc>0\), giving \(c^{\mathsf T}e^{-tD_p}c<0\) for sufficiently small positive \(t\) by the Taylor expansion. For each fixed \(p>0\), sufficiently large \(t\) makes \(e^{-tD_p}\) strictly diagonally dominant, hence positive definite. No sharp supercritical scale interval is asserted.

## Verification
The accompanying standalone `checker.py` uses Python's standard library. Run `python3 checker.py`. It verifies every displayed Krawtchouk coefficient, the precise rational cubing/inequality certificates, multiplicity sum, and independently computes 256-character Fourier eigenvalues at several powers using explicit coset representatives. It numerically locates the unique analytic root and checks its endpoint multiplicity. The command prints `CHECK_PASS`; finite diagnostics supplement, rather than replace, the all-exponent analytic proof above.

## Relationship to prior work
Murugan's 2011 treatment of generalized roundness in vertex-transitive graphs supplies a general spectral-determinant framework and discusses ordinary Boolean hypercubes; it does not give the present antipodal quotient's four powered-distance multipliers, exact exponent, or endpoint Walsh rank. Koolen, Hayat and Iqbal's 2015 study concerns distance spectra of ordinary hypercubes, primarily the unpowered distance, rather than this 256-point folded metric. These broad results motivate the Fourier approach without themselves settling the new exact classification. Related folded-cube topological results and Hamming-scheme sampling laws concern different operators and do not imply the stated Schoenberg criterion.

## Limitations
The result applies to the folded nine-cube alone, not to every folded hypercube dimension. It gives the criterion for positive definiteness at every bandwidth, not a complete characterization of individual supercritical bandwidths. The proof establishes mathematical correctness within its stated model; external independent validation has not been performed. Unindexed association-scheme literature could contain an equivalent specialization of the same Fourier calculation.

## References
1. S. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (first public 2011-12-23), https://arxiv.org/abs/1112.5657.
2. J. H. Koolen, J. Hayat and M. Iqbal, *Hypercubes are determined by their distance spectra*, arXiv:1512.04160v1 (first public 2015-12-14), https://arxiv.org/abs/1512.04160.
