# A sharp mean–variance envelope for three-periodic weighted-shift numerical radii

## Finding

For real numbers \(a,b,c\geq0\) with \(S=a+b+c>0\), let \(W_{a,b,c}\) be the unilateral weighted forward shift on \(\ell^2(\mathbb N_0;\mathbb C)\) whose successive weights repeat \(a,b,c\). Define
\[
Q=(a-b)^2+(b-c)^2+(c-a)^2,\qquad q=Q/S^2\in[0,2].
\]
Its numerical radius obeys the **optimal, moment-constrained lower envelope**
\[
\frac{w(W_{a,b,c})}{S}\ge F(q):=
\begin{cases}
\dfrac{1-2s+\sqrt{9+12s+12s^2}}{12},&0\le q\le\tfrac12,\quad s=\sqrt{q/2},\\[6pt]
\dfrac12\sqrt{\dfrac{1+q}{3}},&\tfrac12\le q\le2.
\end{cases}
\]
For **every** \(q\in[0,2]\), equality is realized by at least one nonnegative triple. More precisely, for \(0<q<1/2\) all equality triples, up to permutations and common positive scaling, have the form \((1+s,1+s,1-2s)\) with \(s=\sqrt{q/2}\). For \(1/2<q<2\), all equality triples are, up to permutations and scaling,
\[
(1+u,1-u,0),\qquad u=\sqrt{(2q-1)/3}.
\]
At \(q=0\), equality means \(a=b=c>0\); at \(q=1/2\), the equality triples are precisely the permutations of \((1,1,0)\); and at \(q=2\), precisely the permutations of \((1,0,0)\).

The sharp **uniform quadratic stability inequality** that follows from this envelope is
\[
\boxed{\displaystyle
w(W_{a,b,c})\ \ge\ \frac S3+\left(\frac1{\sqrt2}-\frac23\right)\frac QS.}
\]
The constant \(1/\sqrt2-2/3\) is optimal, and equality holds precisely for equal positive weights or, allowing zeros, for permutations of \((t,t,0)\) with \(t>0\). In particular, unequal *strictly positive* weights have a strictly positive quantitative gap from their arithmetic mean.

## Assumptions and scope

The weights are nonnegative real numbers, not all zero. Arbitrary complex weights are covered after replacing them by their moduli, since a unilateral weighted shift is unitarily equivalent to the shift with absolute weights. The numerical radius is \(w(W)=\sup_{\|x\|_2=1}|\langle Wx,x\rangle|\). All minima are over triples with the **same** sum \(S\) and normalized squared-difference moment \(q\). The zero-weight boundary belongs to the theorem: it is essential for both the transition and sharp stability constant. These are operators on infinite-dimensional \(\ell^2\), not merely three-by-three cyclic matrices.

## Proof

**Step 1: Exact three-dimensional reduction.** Put
\[
B=\frac12\begin{pmatrix}0&a&c\\a&0&b\\c&b&0\end{pmatrix},\qquad \Lambda=\lambda_{\max}(B).
\]
For \(x\in\ell^2\), taking coordinatewise absolute values and grouping by residue modulo three gives, by Cauchy–Schwarz,
\[
|\langle W x,x\rangle|\le \sum_{j\ge0}(a|x_{3j}x_{3j+1}|+b|x_{3j+1}x_{3j+2}|+c|x_{3j+2}x_{3j+3}|)\le z^\top Bz\le\Lambda\|x\|_2^2,
\]
where \(z_i^2=\sum_{j\ge0}|x_{3j+i}|^2\). Conversely, repeat a nonnegative Perron eigenvector of \(B\) over \(N\) consecutive periods and normalize. The two end effects are bounded independently of \(N\); the Rayleigh quotient tends to \(\Lambda\). Thus \(w(W)=\Lambda\), even when some weights vanish. This also proves that the maximal algebraic eigenvalue of the weighted-triangle matrix, rather than an arbitrary spectral branch, is the relevant quantity.

**Step 2: Only the product remains undetermined by the two moments.** Write \(L=2w(W)\), \(P=a^2+b^2+c^2\), and \(R=abc\). Expanding the determinant gives
\[
L^3-PL-2R=0,\qquad P=\frac{S^2+Q}{3}.
\]
The positive largest root is at least \(\sqrt P\). For fixed \(S,Q\), it is strictly increasing as a function of \(R\ge0\): the derivative of \(L^3-PL\) is \(3L^2-P\ge2P>0\) at the relevant root. Therefore the desired minimum of \(w(W)\) is obtained by minimizing the product \(abc\) under the fixed first and second moments.

**Step 3: Exact product minimizers.** Normalize \(S=1\). The feasible triples satisfy
\[
a+b+c=1,\qquad a^2+b^2+c^2=(1+q)/3.
\]
For \(0<q<1/2\), the intersection of this circle with the nonnegative simplex does not reach a coordinate plane, so every product minimizer is an interior stationary point. Lagrange multipliers for \(\log(abc)\) give \(1/a=\lambda+2\mu a\), and likewise for \(b,c\), so at least two coordinates coincide. The two possible families are
\[
\left(\frac{1+s}{3},\frac{1+s}{3},\frac{1-2s}{3}\right),\qquad
\left(\frac{1-s}{3},\frac{1-s}{3},\frac{1+2s}{3}\right),\quad s=\sqrt{q/2}.
\]
Their products are respectively \((1-3s^2-2s^3)/27\) and \((1-3s^2+2s^3)/27\). Thus the first family uniquely minimizes the product up to permutation. At \(q=0\) the sole feasible triple is uniform. For \(1/2\le q\le2\), the feasible set meets the coordinate planes: \((a,b,c)=((1+u)/2,(1-u)/2,0)\) with \(u=\sqrt{(2q-1)/3}\) has the required moments. Hence the minimum product is zero and all product minimizers have a zero coordinate. This gives the asserted equality classifications, including the endpoints.

**Step 4: Evaluation of the two branches.** In the first range put \(a=b=S(1+s)/3\), \(c=S(1-2s)/3\). The relevant triangle adjacency eigenvalue is
\[
L=\frac{c+\sqrt{c^2+8a^2}}{2},
\]
so division by \(2S\) gives the first displayed branch of \(F\). For \(q\ge1/2\), the minimizing product vanishes; the cubic reduces to \(L^2=P=S^2(1+q)/3\). This gives the second branch. Both equal \(1/(2\sqrt2)\) at \(q=1/2\), proving continuity there. (Their first derivatives need not agree.)

**Step 5: Best coefficient of the variance gap.** For \(0<q\le1/2\), writing \(s=\sqrt{q/2}\) and rationalizing yields
\[
\frac{F(q)-1/3}{q}=\frac{1}{3\left(\sqrt{9+12s+12s^2}+3+2s\right)},
\]
which strictly decreases in \(s\in(0,1/2]\). For \(1/2\le q\le2\), write \(t=\sqrt{3(1+q)}\in[3/\sqrt2,3]\). Then
\[
\frac{F(q)-1/3}{q}=\frac{t-2}{2(t^2-3)},
\]
whose derivative has the sign of \(-(t-1)(t-3)\) and is positive before \(t=3\). Consequently the unique minimum of the ratio over nonzero \(q\) occurs at \(q=1/2\), where it equals
\[
\frac1{12+9\sqrt2}=\frac1{\sqrt2}-\frac23.
\]
The equality statements follow from Steps 3 and 4. This completes the proof.

## Verification

The included standard-library script `verify_period3.py` recomputes the Perron root by bisection from the exact cubic, checks the exact rational moment identity and the two inequalities on all 4,912 nonzero integer triples in \(\{0,\ldots,16\}^3\), and exercises eight equality families across the transition. It printed `PASS: 4912 nonzero rational weight triples` and an extremal constant of approximately \(0.040440114519881\). This is a floating-point diagnostic, not a proof of universal validity; the preceding five steps are the proof. Boundary equality and the full infinite-dimensional statement require the exact argument, not finite tests.

## Relationship to prior work

The 2023 paper of Sharif, building on Ridge's periodic-shift formula, proves that a period's arithmetic mean is a lower bound for the numerical radius and notes equality for period two. Its finite-dimensional variational description and general bounds do not state the optimal tradeoff at *fixed sum and second moment*. Related work of Stout and Chien–Sheu develops exact numerical-radius computations, including periodic shifts and finite perturbations, without asserting the above sharp moment-constrained envelope. An independently published classification of strict convexity and differentiability for weighted graph-edge numerical-radius norms includes three-periodic shifts, but does not determine a fixed-variance lower envelope or its extremizing boundary triples. The new claim is the two-phase constrained optimization and optimal stability coefficient, **not** the periodic finite-dimensional reduction or the cubic characteristic polynomial themselves.

## Limitations

The classification fixes exactly three repeating weights and the standard Hilbert-space numerical radius. It makes no claim for higher periods, other \(\ell^p\) spaces, alternative definitions of variance or sums of nonperiodic weights. The zero-weight minimizers require permitting vanishing weights; positive-weight sequences can approach but not attain that part of the envelope for \(q\ge1/2\). Although relevant accessible literature and an indexed nearby result were compared, an earlier algebraically equivalent spectral-optimization inequality under different terminology cannot be completely excluded. Independent mathematical validation has not been performed.

## References

1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876, first public 2023-03-02, especially Example 1.6, Corollary 2.4 and Remark 2.5; https://arxiv.org/abs/2303.00876.
2. W. C. Ridge, *Numerical range of a weighted shift with periodic weights*, Proc. Amer. Math. Soc. 55 (1976), 107–110, DOI 10.2307/2041852.
3. Q. F. Stout, *The numerical range of a weighted shift*, Proc. Amer. Math. Soc. 88 (1983), 495–502, DOI 10.1090/S0002-9939-1983-0699421-1.
4. M.-T. Chien and H.-A. Sheu, *The numerical radii of weighted shift matrices and operators*, Operators and Matrices 7 (2013), 197–204, DOI 10.7153/oam-07-11; https://files.ele-math.com/articles/oam-07-11.pdf.
