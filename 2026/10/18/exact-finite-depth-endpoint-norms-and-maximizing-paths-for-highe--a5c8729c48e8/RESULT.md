# Exact finite-depth endpoint norms and maximizing paths for higher-arity martingale sign transforms

## Finding
Fix integers \(b\ge3\) and \(d\ge1\). For the uniformly weighted rooted \(b\)-ary probability tree of depth \(d\), let \(E_j\) denote conditional expectation onto the first \(j\) coordinates and \(D_j=E_j-E_{j-1}\). Over all predictable sign families \(\varepsilon_j:\{0,\ldots,b-1\}^{j-1}\to\{-1,1\}\), consider
\[
T_\varepsilon=E_0+\sum_{j=1}^{d}M_{\varepsilon_j}D_j.
\]
The exact sharp strong endpoint norm is
\[
\boxed{\sup_\varepsilon\|T_\varepsilon\|_{L^1\to L^1}
=\frac{2(b-1)}{b+1}d+\frac{(b-1)(b+3)}{(b+1)^2}
+\frac{4}{(b+1)^2}\left(-\frac1b\right)^d.}
\]
A sign family attains this supremum if and only if **some** root-to-leaf path \(\omega\) has \(\varepsilon_j(\omega_1,\ldots,\omega_{j-1})=(-1)^j\) at every depth \(1\le j\le d\). All signs outside that path are unrestricted. The sharp slope in depth is \(2(b-1)/(b+1)\); the exact bounded correction and the equality classification hold simultaneously for every allowed arity and depth.

## Assumptions and scope
The probability space is \(\Omega_{b,d}=\{0,\ldots,b-1\}^{d}\) with equal mass \(b^{-d}\) per leaf. The real \(L^1\) norm is the sum of leaf magnitudes times \(b^{-d}\). For \(j=0,\ldots,d\), \(E_j f\) is the average over leaves sharing the first \(j\) digits with the evaluation leaf, with \(E_0 f\) the global mean. Multiplication \(M_{\varepsilon_j}\) is by the sign determined by the first \(j-1\) digits; hence each sign is predictable. Only signs \(-1\) and \(1\), **not** zero or continuous multipliers, are optimized. The initial mean \(E_0\) has fixed coefficient \(+1\). The theorem concerns finite depths \(d\ge1\) and arities \(b\ge3\); it makes no assertion about equality classifications for binary trees, unequal branch masses, arbitrary nonpredictable signs, or infinite-depth operator boundedness.

## Proof
**Column reduction.** A finite matrix acting on uniform \(L^1(\Omega_{b,d})\) has operator norm equal to its maximum absolute column sum. Fix a source leaf \(\omega\). For each \(j\), write \(e_j=\varepsilon_j(\omega_1,\ldots,\omega_{j-1})\). A target leaf that first differs from \(\omega\) at digit \(j\) has matrix entry
\[
b^{j-1-d}(y_{j-1}-e_j),\qquad
y_0=1,\quad y_j=\frac{y_{j-1}+(b-1)e_j}{b}.
\]
The diagonal entry is \(y_d\). Since the number of target leaves first differing at digit \(j\) equals \((b-1)b^{d-j}\), and since \(|y_j|\le1\), the column sum is exactly
\[
C(e_1,\ldots,e_d)=\frac{b-1}{b}\sum_{j=1}^d(1-e_j y_{j-1})+|y_d|.
\tag{1}
\]
The signs away from the source path play no part in this column. Conversely every sequence of signs along one path extends to a predictable sign family. Consequently the global operator optimum equals the maximum of (1) over \(e_j\in\{-1,1\}\).

**Strict dynamic-programming choice.** Because \(b-1>1\) and \(|y_{j-1}|\le1\), the sign of \(y_j\) equals \(e_j\), for every possible sign choice and every \(j\ge1\). Thus
\[
C=(b-1)d-(b-1)\sum_{j=1}^{d-1}|y_j|-(b-2)|y_d|.
\tag{2}
\]
We minimize the weighted absolute-value cost in (2). Let \(F_m(y)\) be the minimum remaining cost for \(m\) steps, with weight \(b-1\) on its first \(m-1\) generated absolute states and weight \(b-2\) on its final absolute state. The minimum is taken over all \(2^m\) subsequent signs. Every fixed-sign cost is Lipschitz in the initial state \(y\) with constant at most
\[
(b-1)\sum_{k=1}^{m-1}b^{-k}+(b-2)b^{-m}=1-2b^{-m}<1,
\]
so their minimum \(F_m\) has that same bound. Reversing the initial state and every future sign shows that \(F_m\) is even. At the next decision the two possible generated state magnitudes are \((b-1+y)/b\) and \((b-1-y)/b\); the smaller is obtained by choosing the next sign opposite to \(\operatorname{sgn}(y)\). For \(m\ge2\), the next-step objective is \((b-1)|y_1|+F_{m-1}(y_1)\), whose value is strictly smaller at the smaller absolute state, because \(F_{m-1}\) is even and has Lipschitz constant less than \(1<b-1\). For \(m=1\), its objective is \((b-2)|y_1|\), also strictly increasing for \(b\ge3\). Therefore the minimizing action is uniquely the sign opposite to \(y\) whenever \(y\ne0\).

Starting from \(y_0=1\), the optimal states are nonzero and their unique sign choices are \(e_j=(-1)^j\). Solving the recurrence gives
\[
y_j=\frac{b-1}{b+1}(-1)^j+\frac{2}{b+1}b^{-j},\qquad
|y_j|=\frac{b-1}{b+1}+\frac{2}{b+1}\left(-\frac1b\right)^j\quad (j\ge1).
\]
Inserting these states into (2) and summing the finite geometric progression yields the displayed sharp norm. Finally, a matrix attains its induced \(L^1\) norm at a point mass supported on a maximizing source column. Such a column exists exactly when its path signs are the unique maximizing alternating sequence. This proves both attainment and the complete sign-family equality classification.

## Verification
The accompanying standalone Python program `check_martingale.py` uses exact rational arithmetic and builds conditional-expectation matrices independently of the shell formula. It exhausts all \(2^d\) path sign sequences for \(3\le b\le8\) and \(1\le d\le9\), checks optimal values and uniqueness, and compares selected full matrices (including all small sign families and deterministic sampled larger ones) against both the column formula and the optimizer criterion. The analytical proof is valid for all \(b\ge3,d\ge1\); finite computations are reproducibility checks, not a substitute for the strict Bellman argument.

## Relationship to prior work
Sharp martingale-transform inequalities of Burkholder and their higher-dimensional applications concern \(L^p\) norms for \(1<p<\infty\), not the present exact finite-height strong \(L^1\) norm. Osękowski's investigations of Haar inequalities address distributional/weak-type estimates for the usual dyadic basis. Astashkin and coauthors analyze optimal rearrangement bounds and symmetric target spaces for dyadic transforms. Neither the cited source results nor the related finite dyadic whole-scale projection norm determines this higher-arity full predictable-sign optimization or its equality characterization. The binary endpoint is not asserted to be new. A complete priority determination would require broader bibliographic verification, particularly for historical finite-filtration norm results.

## Limitations
The result is for uniform branching, integer arity at least three, real scalar \(L^1\), fixed initial coefficient \(+1\), predictable signs only, and finite depth. No extension to weighted branches or infinite depth is proved. An equivalent formula could occur in older finite-horizon martingale or Banach-space literature not identified by the searches; no independent audit has been performed.

## References
1. O. Dragičević, S. Petermichl, A. Volberg, “Sharp estimates of martingale transforms in higher dimensions and applications to the Ahlfors–Beurling operator,” arXiv:math/0606006 (first public version 31 May 2006).
2. A. Osękowski, “Sharp inequalities for the Haar system and Fourier multipliers,” *Journal of Function Spaces* (2013), DOI: 10.1155/2013/646012.
3. A. Osękowski, “Some sharp estimates for the Haar system and other bases in \(L^1(0,1)\),” *Math. Scand.* 115 (2014), 123–142, DOI: 10.7146/math.scand.a-18006.
4. S. Astashkin, J. Huang, M. Pliev, F. Sukochev, D. Zanin, “Optimal range of Haar martingale transforms and its applications,” arXiv:2202.07154 (2022).
