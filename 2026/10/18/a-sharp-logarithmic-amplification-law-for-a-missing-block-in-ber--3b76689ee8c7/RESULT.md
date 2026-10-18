# A sharp logarithmic amplification law for a missing block in Berrut interpolation

## Finding
Fix an integer \(k\ge 1\) and a sequence of integers \(h_N\) such that \(0\le h_N\le N-k-1\) and \(h_N/N\to\theta\in(0,1)\). Starting with the equally spaced real nodes \(0,1,\ldots,N\), delete the \(k\) consecutive nodes \(h_N+1,\ldots,h_N+k\). Let \(y_0<\cdots<y_{N-k}\) be the remaining nodes, let the Berrut weights be \((-1)^j\) in this *new* increasing order, and let \(\Lambda_{N,k}\) denote the Lebesgue constant of the rational interpolation operator
\[
(B_{N,k}f)(x)=\frac{\sum_{j=0}^{N-k}(-1)^j f(y_j)/(x-y_j)}{\sum_{j=0}^{N-k}(-1)^j/(x-y_j)},\qquad 0\le x\le N,
\]
with continuous interpolation values at the nodes. Put \(L=k+1\) and
\[
\Delta_k=2\int_0^1\frac{t^{L/2-1}}{1+t}\,dt
=\psi\!\left(\frac{k+3}{4}\right)-\psi\!\left(\frac{k+1}{4}\right),
\]
where \(\psi\) is the digamma function. Then
\[
\boxed{\lim_{N\to\infty}\frac{\Lambda_{N,k}}{\log N}=\frac{2}{\Delta_k}.}
\]
Moreover, every maximizing location \(x_N\in[0,N]\) satisfies
\[
\boxed{x_N-\left(h_N+\frac{k+1}{2}\right)\longrightarrow 0.}
\]
The amplification coefficient is strictly increasing with the number of consecutively deleted samples and satisfies \(2/\Delta_k\sim k+1\) as \(k\to\infty\) *after* the \(N\to\infty\) limit. For one deleted node, \(\Delta_1=2\log2\), giving the explicit coefficient \(1/\log 2\).

## Assumptions and scope
The integer \(k\) is fixed as \(N\to\infty\). The missing block stays a positive proportion away from both endpoints. Alternating barycentric weights are re-indexed after deletion; preserving the old signs is a different interpolation rule. All logarithms are natural. The result concerns the \(C([0,N])\to C([0,N])\) uniform operator norm, equivalently the Lebesgue constant; it is invariant under affine rescaling of the nodes to \([0,1]\). The theorem makes no assertion when \(k\) grows with \(N\) or when the missing block approaches an endpoint.

## Proof
For any strictly increasing node set \(y_0<\cdots<y_m\), the alternating-denominator interpolation has no poles on its convex hull. Indeed, if \(y_j<x<y_{j+1}\), splitting at this interval gives
\[
\left|\sum_{i=0}^m\frac{(-1)^i}{x-y_i}\right|
=\sum_{r=0}^j\frac{(-1)^r}{x-y_{j-r}}
+\sum_{r=0}^{m-j-1}\frac{(-1)^r}{y_{j+1+r}-x}.
\]
Each sum is a positive finite alternating series with strictly decreasing term magnitudes. The continuous Lebesgue function equals the sum of reciprocal distances divided by this positive denominator, and equals \(1\) at a node.

**Ordinary unit-length cells.** Suppose adjacent retained nodes are one unit apart, and write \(u=x-y_j\in(0,1)\). Because all other consecutive spacings are at least one, the alternating-series bound on the two tails yields
\[
D_N(x)\ge \frac1u-\frac1{u+1}+\frac1{1-u}-\frac1{2-u}
=F(u)\ge\frac83.
\]
The last inequality follows because \(u\mapsto 1/[u(u+1)]\) is strictly convex, so its symmetrization is minimized at \(u=1/2\). The positive numerator satisfies
\[
A_N(x)\le\frac1u+\frac1{1-u}+2H_N,
\]
where \(H_N=\sum_{r=1}^N1/r=\log N+O(1)\). Since \(\{1/u+1/(1-u)\}/F(u)\) is uniformly bounded (its limiting value at either endpoint is one), uniformly across all ordinary cells
\[
\frac{A_N(x)}{D_N(x)}\le\frac34\log N+O(1).
\]
This strict \(3/4\) coefficient will be smaller than the missing-gap coefficient for every \(k\ge1\).

**The enlarged cell.** Center coordinates at \(h_N+L/2\), writing \(x=h_N+L/2+s\) with \(-L/2<s<L/2\), and set \(a=L/2\). The surviving nodes to the left are \(h_N,h_N-1,\ldots,0\), those to the right are \(h_N+L,h_N+L+1,\ldots,N\). By the same alternating-series decomposition, for \(p_N=h_N+1\), \(q_N=N-h_N-L+1\),
\[
D_N(s)=\sum_{r=0}^{p_N-1}\frac{(-1)^r}{a+s+r}
+\sum_{r=0}^{q_N-1}\frac{(-1)^r}{a-s+r},
\]
\[
A_N(s)=\sum_{r=0}^{p_N-1}\frac1{a+s+r}
+\sum_{r=0}^{q_N-1}\frac1{a-s+r}.
\]
For \(v>0\), the infinite alternating reciprocal sum has the integral representation
\[
\sum_{r=0}^\infty\frac{(-1)^r}{v+r}=\int_0^1\frac{t^{v-1}}{1+t}\,dt.
\]
The alternating-series remainder is at most \(1/(v+p_N)\) or \(1/(v+q_N)\); since \(p_N,q_N\) are comparable with \(N\), it follows uniformly for \(|s|<a\) that
\[
D_N(s)=D_\infty(s)+O(N^{-1}),\qquad
D_\infty(s)=2\int_0^1\frac{t^{a-1}\cosh(s\log t)}{1+t}\,dt.
\]
The integral is strictly minimized at \(s=0\), with value \(\Delta_k>0\), and tends to infinity when \(s\to\pm a\). For every sequence \(s_N\to s\) with \(|s|<a\), the harmonic-series estimate gives \(A_N(s_N)=2\log N+O(1)\), and hence
\[
\frac{A_N(s_N)}{D_N(s_N)\log N}\longrightarrow\frac{2}{D_\infty(s)}\le\frac2{\Delta_k},
\]
with equality only at \(s=0\). If instead \(s_N\to a\) (or \(-a\)), write \(v_N=a-s_N\to0\): the nearest reciprocal term is \(1/v_N\), both remaining positive sums are bounded by \(2H_N+O_k(1)\), and the alternating denominator is \(1/v_N+O_k(1)\). Consequently its Lebesgue quotient divided by \(\log N\) tends to zero. This covers all sequences in the enlarged cell.

At its midpoint \(s=0\), \(A_N(0)=2\log N+O_{k,\theta}(1)\) and \(D_N(0)\to\Delta_k\), furnishing the matching lower bound. Finally \(\Delta_k\le\Delta_1=2\log2\), whence \(2/\Delta_k\ge1/\log2>3/4\): no ordinary cell can asymptotically maximize. Compactness of the enlarged interval and strict minimization of \(D_\infty\) give the claimed localization of *every* maximizer.

For the digamma identity, apply the classical alternating Hurwitz sum identity
\[
\sum_{r=0}^\infty\frac{(-1)^r}{r+a}
=\frac12\left[\psi\!\left(\frac{a+1}{2}\right)-\psi\!\left(\frac a2\right)\right].
\]
The integral representation shows \(\Delta_k\) strictly decreases with \(k\). Finally, the substitution \(t=e^{-u/a}\) or a one-term Laplace estimate shows \(\Delta_k\sim 2/(k+1)\), proving the large-fixed-gap asymptotic.

## Verification
The companion standalone \`verify.py\` evaluates the finite Lebesgue function using the *reindexed* signs, compares the two independent forms of the missing-cell denominator, checks the regular-cell lower bound at rational test points, and compares successive system sizes with the predicted logarithmic coefficient. This finite evidence checks arithmetic and implementation but is not used to infer the limit. The proof is analytical and contains all required uniform estimates.

## Relationship to prior work
Bos, De Marchi, and Hormann (2010 preprint; 2011 journal publication) established logarithmic bounds for Berrut interpolation on an intact uniform grid. Bos, De Marchi, Hormann, and Sidon (2012 preprint; 2013 journal publication) proved logarithmic bounds for much more general well-spaced node arrays. These works supply the stability framework and confirm that bounded local gaps preserve logarithmic growth, but the inspected theorem descriptions do not state the precise coefficient \(2/\Delta_k\) or the missing-gap concentration law. The general-nodes text is not fully accessible here, so equivalent historical coverage remains a bibliographic risk. The claim is the sharp deleted-block coefficient and localization, *not* logarithmic growth or pole-freeness alone.

## Limitations
The special-function identity is exact but the result does not specify a uniform error term when \(k\) grows. The date on the 2010 cited manuscript is an author-preprint date, not a claim of independently verified first digital dissemination. Unavailable full-text material may contain an equivalent result; scientific independence has not been externally established. No statement about interpolation approximation accuracy, optimal deletion patterns, or nonconsecutive deletions follows.

## References
1. L. Bos, S. De Marchi, and K. Hormann, *On the Lebesgue constant of Berrut's rational interpolant at equidistant nodes*, author preprint dated 2010-10-25, later J. Comput. Appl. Math. 236 (2011), 504–510, DOI 10.1016/j.cam.2011.04.004. Author preprint: https://www.math.unipd.it/~demarchi/papers/lebesgue2.pdf.
2. L. Bos, S. De Marchi, K. Hormann, and J. Sidon, *Bounding the Lebesgue constant for Berrut's rational interpolant at general nodes*, author preprint dated 2012-05-10, later J. Approx. Theory 169 (2013), 7–22, DOI 10.1016/j.jat.2013.01.004. Author preprint: https://www.math.unipd.it/~demarchi/papers/Lebesgue-Berrut-General.pdf.
3. J.-P. Berrut, *Rational functions for guaranteed and experimentally well-conditioned global interpolation*, Comput. Math. Appl. 15 (1988), 1–16, DOI 10.1016/0898-1221(88)90067-3.
