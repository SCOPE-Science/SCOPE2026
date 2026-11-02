# Unique interior degree distribution for three-bit symmetric random access

## Finding
Let three binary information symbols be stored by a fully symmetric linear generator: each nonzero vector of Hamming weight one has the same sampling probability \(a\), each weight-two vector has probability \(b\), and the weight-three vector has probability \(c=1-3a-3b\). Samples are independent with replacement. An information symbol is recovered at the first draw count for which its coordinate vector belongs to the linear span of the sampled columns; arbitrary linear decoding is allowed.

**Theorem.** On the probability simplex \(a,b,c\ge0\), \(3a+3b+c=1\), this random-access expectation has a **unique global minimum distribution**. The minimizer has \(a>0\), \(b>0\), and \(c>0\); hence all three column weights are indispensable at the optimum. It is the unique interior solution of
\[
\frac{1}{(1-2a-b)^2}=\frac{1}{(1-a)^2}+\frac{1}{3(a+b)^2},
\]
\[
\frac{1}{(1-2a-b)^2}+\frac{3}{(1-3b)^2}=\frac{3}{(1-b)^2}+\frac{2}{3(a+b)^2}.
\]
With \(a_0=238169545370/10^{12}\) and \(b_0=78518646238/10^{12}\), the exact minimizing pair obeys the **certified** Euclidean error bound
\[
\sqrt{(a-a_0)^2+(b-b_0)^2}<2\cdot10^{-9}.
\]
The minimum expectation is approximately \(2.7788495899\) draws. This statement concerns the unique optimum among probability distributions, equivalently the infimum over finite fully symmetric generator matrices of arbitrary length; it does **not** assert that some finite length realizes the optimizer exactly.

There is also a fully explicit finite comparison: a thirteen-column generator with three copies of each weight-one column and one copy of each of the other four nonzero columns has expectation \(167/60\), while **every** fully symmetric generator using at most two nonzero column weights has expectation strictly larger than \(279/100\). The three coordinate-weight classes therefore cannot be discarded in a minimizing sequence.

## Assumptions and scope
Work over \(V=\mathbb F_2^3\). The three information symbols are the coordinates of the information vector; a sampled nonzero column \(v\in V\) returns its binary linear form. The generator may repeat columns; the sample distribution is its empirical column multiplicity distribution. Full symmetry means that probabilities depend only on the column Hamming weight. Zero columns are excluded, as in the cited fully symmetric model. The number of samples \(\tau_i\) needed for coordinate \(i\) is the least positive integer \(t\) such that \(e_i\in\langle V_1,\ldots,V_t\rangle\), with \(\tau_i=\infty\) if this never occurs. Symmetry makes \(\mathbb E\tau_i\) independent of \(i\).

Write \(c=1-3a-3b\). The expectation is finite precisely when \(a+b>0\) and \(b<1/3\). At either excluded simplex vertex, the observed supports cannot span any requested unit coordinate. All optimization and strict convexity assertions refer only to the finite-expectation domain.

## Proof
**1. Exact access functional.** For a subspace \(U\le V\), denote by \(p(U)\) its one-draw probability. The lattice of subspaces of \(\mathbb F_2^3\) contains the zero subspace, seven lines and seven planes. Among the subspaces not containing \(e_1\) there are the zero subspace, six lines and four planes. Subspace-lattice Möbius inversion gives, for every integer \(t\ge0\),
\[
\Pr(e_1\notin\langle V_1,\ldots,V_t\rangle)
=3\,p(\{0\})^t-\sum_{\substack{L\text{ a line}\\e_1\notin L}}p(L)^t
+\sum_{\substack{P\text{ a plane}\\e_1\notin P}}p(P)^t,
\]
where \(p(\{0\})=0\) and we interpret \(0^0=1\). The six lines have masses \(a,a,b,b,b,c\). The four planes have masses \(2a+b\), \(3b\), \(a+b+c\), \(a+b+c\). Sum this identity over \(t\ge0\), use the geometric series, and substitute \(c=1-3a-3b\) to obtain
\[
T(a,b)=3-\frac{2}{1-a}-\frac{3}{1-b}
+\frac{2}{3(a+b)}+\frac{1}{1-2a-b}+\frac{1}{1-3b}.
\]
This rational expectation formula is also a specialization of Wang and Yaakobi's published symmetric three-dimensional expression; **the formula itself is not asserted as new**.

**2. Strict convexity.** Set \(x=(1-a)^{-3}\) and \(y=(1-b)^{-3}\). Since \(1-2a-b\le1-a\) and \(1-3b\le1-b\), direct differentiation gives the symmetric-matrix inequality
\[
\nabla^2T(a,b)\succeq
\begin{pmatrix}4x&4x\\4x&2x+12y\end{pmatrix}=:B.
\]
The discarded term \(4[3(a+b)^3]^{-1}(1,1)^\mathsf T(1,1)\) is positive semidefinite. On the simplex \(1\le x,y\le27/8\) and
\[
\det B=8x^2\left(6\left(\frac{1-a}{1-b}\right)^3-1\right)
\ge\frac{56}{9},\qquad \operatorname{tr}B\le\frac{243}{4}.
\]
Here \((1-a)/(1-b)\ge2/3\). Thus \(\lambda_{\min}(B)\ge\det B/\operatorname{tr}B\ge224/2187>1/10\). In particular, \(T\) is strictly (indeed uniformly strongly) convex on its finite domain.

**3. Every boundary is inferior.** The explicit thirteen-column distribution \((a,b,c)=(3/13,1/13,1/13)\) gives \(T=167/60<279/100\). To prove that no weight class can be absent at an optimum, compare all three boundary edges to \(279/100\). For \(c=0\), put \(t=3a\) and obtain
\[
T(a,1/3-a)-279/100=\frac{P_c(t)}{900a(a-1)(3a-2)(3a+2)},
\]
where \(P_c(t)=221t^4-1163t^3+3616t^2-3748t+1200\). For \(b=0\), put \(t=3a\) and obtain
\[
T(a,0)-279/100=\frac{P_b(t)}{8100a(a-1)(2a-1)},
\]
where \(P_b(t)=-1074t^3+8733t^2-12933t+5400\). For \(a=0\), put \(t=3b\) and obtain
\[
T(0,b)-279/100=\frac{P_a(t)}{8100b(b-1)(3b-1)},
\]
where \(P_a(t)=-1611t^3+12744t^2-14733t+5400\). The denominators are positive on their finite-expectation boundary domains.

All three polynomials are **strictly positive for \(0\le t\le1\)**. Here is an exact finite certificate, not a numerical plot: subdivide this interval into the sixteen closed dyadic cells \(t=(j+u)/16\), \(0\le j\le15\), \(0\le u\le1\), and express each polynomial in the degree-\(d\) Bernstein basis
\[
P((j+u)/16)=\sum_{h=0}^{d}\beta_{j,h}\binom dh u^h(1-u)^{d-h}.
\]
Taking the minimum over all \(j,h\) yields \(8873/12288\) for \(P_c\), \(24521/512\) for \(P_b\), and \(1557633/2048\) for \(P_a\), all positive. The standalone exact-arithmetic program recomputes every coefficient and checks the polynomial identities. Hence every feasible boundary point has access expectation above \(279/100\), whereas the finite witness is below it. The two nonrecoverable vertices have infinite expectation. By compactness an interior minimum exists, and strict convexity makes it unique. The two displayed critical-point equations follow by differentiation.

**4. Certified localization.** At the rational center \((a_0,b_0)\) in the finding, direct fraction arithmetic shows
\[
|\partial_aT(a_0,b_0)|+|\partial_bT(a_0,b_0)|<1/(5\cdot10^9).
\]
The proven Hessian bound \(\nabla^2T\succeq I/10\) and stationarity of the interior minimum imply
\[
\|(a,b)-(a_0,b_0)\|_2\le10\|\nabla T(a_0,b_0)\|_2<2\cdot10^{-9}.
\]
Rational empirical distributions arising from finite fully symmetric generators are dense in this probability simplex, so the same minimum is the infimum of actual finite-code expectations, though exact attainment by finite multiplicities is not asserted.

## Verification
Run `python3 verify.py` in the same directory. It uses only the Python standard library: it independently reconstructs all sixteen binary subspaces and the exact rational expected hitting time for seven distributions, checks the thirteen-column witness, checks the three algebraic boundary identities at rational samples, recomputes all \(16(5+4+4)=208\) Bernstein coefficients and their certified positive minima, and checks the rational gradient localization bound. The all-distribution formula, Hessian inequality, polynomial identities and compactness argument are given above; finite spot checks alone would not prove them.

## Relationship to prior work
Wang and Yaakobi (2026, arXiv:2601.07053), Example 3 and Table III, **already** give the rational three-dimensional symmetric access expression and a **numerical** binary three-weight allocation (approximately \(0.2382,0.0785,0.0500\) per column). Their table therefore already suggests a full-degree optimum. The contribution here is the rigorous **global uniqueness and strict-interiority theorem**, a rational all-boundary exclusion certificate, and a rigorously localized minimizing distribution; none is claimed for their already-published numerical estimate or functional formula. Hofmeister, Bitar and Yaakobi (2026, arXiv:2605.10919) analyze a different large-information-dimension limit under peeling decoding. Boruchovsky and collaborators (2025, arXiv:2501.12274) study random access more generally, with large-field weight-one/weight-two constructions. These results do not directly imply this finite-three-bit optimality characterization.

## Limitations
This theorem concerns fully symmetric nonzero-column binary sampling distributions, three information bits, ideal independent draws with replacement, and unrestricted linear-span decoding. It does not prove fully symmetric matrices globally optimal among asymmetric matrices; does not optimize separately at each prescribed finite generator length; and does not address finite-sample peeling decoding or larger dimensions. The published Wang--Yaakobi formula and numerical value are prior results, not new findings. Independent mathematical validation and complete publication-priority confirmation remain outstanding.

## References
1. C. Wang and E. Yaakobi, *Random Access in DNA Storage: Algorithms, Constructions, and Bounds*, arXiv:2601.07053, first posted 11 January 2026. https://arxiv.org/abs/2601.07053
2. C. Hofmeister, R. Bitar and E. Yaakobi, *Random Access Expectation in DNA Storage and Fountain Codes*, arXiv:2605.10919, first posted 11 May 2026. https://arxiv.org/abs/2605.10919
3. A. Boruchovsky, O. Elishco, R. Gabrys, A. Gruica, I. Tamo and E. Yaakobi, *Making it to First: The Random Access Problem in DNA Storage*, arXiv:2501.12274. https://arxiv.org/abs/2501.12274
