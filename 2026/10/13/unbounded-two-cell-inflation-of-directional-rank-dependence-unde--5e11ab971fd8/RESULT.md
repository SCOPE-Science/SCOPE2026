# Unbounded two-cell inflation of directional rank dependence under stochastic increase

## Finding

For every integer \(k\ge1\), define on the unit square
\[
C_k(u,v)=uv+\varepsilon_k u(1-u)[4v(1-v)]^k,\qquad \varepsilon_k=\frac1{8k}.
\]
Let \(B_k\) be the ordinary \(2\times2\) checkerboard copula with the same quadrant probabilities as \(C_k\). Denote population directional Chatterjee correlation, with the first coordinate as predictor, by \(\xi(C)=\xi(V\mid U)\). Then \(C_k\) is a polynomial, stochastically increasing, positively quadrant dependent copula with a strictly positive density satisfying \(1/2\le c_k\le3/2\). In particular, for every finite constant \(K>0\), some \(k\) satisfies \(\xi(B_k)>K\xi(C_k)\).

More precisely, put
\[
I_k=\int_0^1[4v(1-v)]^{2k}\,dv
 =\frac{4^{2k}((2k)!)^2}{(4k+1)!}.
\]
The two exact statistics and their ratio are
\[
\xi(C_k)=2\varepsilon_k^2I_k,\qquad
\xi(B_k)=\frac{\varepsilon_k^2}{2},\qquad
\frac{\xi(B_k)}{\xi(C_k)}=\frac{1}{4I_k}
\sim\sqrt{\frac{k}{2\pi}}\longrightarrow\infty.
\]
Within this family, strict checkerboard inflation begins exactly at \(k=6\), while the checkerboard statistic is smaller for \(1\le k\le5\). For \(k=6\), the exact inflation ratio is \(16900975/16777216\). The assertion is about *relative* inflation: both dependence statistics approach zero as \(k\to\infty\).

## Assumptions and scope

For a copula \(C\) with uniform margins and conditional distribution function \(F_{V\mid U=u}(v)=\partial_u C(u,v)\) almost everywhere, the population directed coefficient used here is
\[
\xi(C)=6\int_0^1\!\int_0^1\left(\partial_u C(u,v)-v\right)^2\,du\,dv
 =6\int_0^1\!\int_0^1\left(\partial_u C(u,v)\right)^2\,du\,dv-2.
\]
The equivalence uses uniform margins. The ordinary \(2\times2\) checkerboard approximant distributes each of the four cell masses uniformly on its corresponding quadrant. Stochastic increase (SI) means \(u\mapsto\partial_u C(u,v)\) is nonincreasing for every \(v\) for which this conditional CDF is defined. This statement does not assume total positivity of the density; indeed the constructed densities do not have that stronger property for \(k\ge2\).

## Proof

**1. Copula validity, smoothness, and stochastic increase.** Write \(f_k(v)=[4v(1-v)]^k\) and \(\varepsilon=1/(8k)\). The function \(C_k\) has grounded boundary values and uniform margins because \(u(1-u)=0\) when \(u=0,1\) and \(f_k(0)=f_k(1)=0\). Its polynomial density is
\[
c_k(u,v)=\partial_{uv}C_k(u,v)=1+\varepsilon(1-2u)f'_k(v).
\]
For \(0\le v\le1\),
\[
|f'_k(v)|=4k|1-2v|[4v(1-v)]^{k-1}\le4k,
\]
so \(1/2\le c_k(u,v)\le3/2\). The nonnegative density plus correct boundaries establishes that \(C_k\) is a copula. Its conditional distribution function is
\[
F_{V\mid U=u}(v)=v+\varepsilon(1-2u)f_k(v).
\]
For fixed \(0<v<1\), its derivative in \(u\) is \(-2\varepsilon f_k(v)<0\): stochastic increase is strict in the interior. Moreover \(C_k(u,v)-uv=\varepsilon u(1-u)f_k(v)\ge0\), which is positive quadrant dependence. For \(k\ge2\) the density is not TP\(_2\): near \(v=0\), \(f'_k\) increases strictly. Choosing \(u_1<u_2\) and sufficiently small \(v_1<v_2\), the TP\(_2\) minor
\[
c_k(u_1,v_1)c_k(u_2,v_2)-c_k(u_1,v_2)c_k(u_2,v_1)
=\varepsilon\big[(1-2u_1)-(1-2u_2)\big]\big[f'_k(v_1)-f'_k(v_2)\big]<0.
\]
This places the construction strictly outside the density-TP\(_2\) hypothesis of the applicable positive bound.

**2. Original coefficient.** The uniform-margin identity in the scope section and \(\int_0^1(1-2u)^2\,du=1/3\) give
\[
\xi(C_k)=6\varepsilon^2\frac13\int_0^1f_k(v)^2\,dv=2\varepsilon^2 I_k.
\]
The beta integral, valid for each integer \(k\ge1\), is
\[
I_k=4^{2k}\int_0^1v^{2k}(1-v)^{2k}\,dv
=4^{2k}\frac{((2k)!)^2}{(4k+1)!}.
\]

**3. Checkerboard coefficient.** Since \(f_k(1/2)=1\), the exact quadrant masses, in row-major order, are
\[
\Delta=\frac14\begin{pmatrix}1+\varepsilon&1-\varepsilon\\1-\varepsilon&1+\varepsilon\end{pmatrix}.
\]
Let \(s(u)=1\) for \(0<u<1/2\) and \(s(u)=-1\) for \(1/2<u<1\), and write \(g(v)=\min\{v,1-v\}\). Uniform interpolation within the two column cells gives the conditional checkerboard CDF
\[
\partial_u B_k(u,v)=v+\varepsilon s(u)g(v)
\]
away from cell boundaries. Consequently, since \(\int_0^1 g(v)^2\,dv=1/12\),
\[
\xi(B_k)=6\varepsilon^2\int_0^1s(u)^2\,du\int_0^1g(v)^2\,dv=\frac{\varepsilon^2}{2}.
\]
The ratio is exactly \(1/(4I_k)\).

**4. Divergence and first inflation index.** Since \(0\le 4v(1-v)\le1\) with equality only at \(v=1/2\), dominated convergence gives \(I_k\downarrow0\). For the rate, write \(v=(1+t)/2\) and substitute \(s=\sqrt{2k}\,t\):
\[
I_k=\frac1{2\sqrt{2k}}\int_{-\sqrt{2k}}^{\sqrt{2k}}\left(1-\frac{s^2}{2k}\right)^{2k}\,ds
\sim\frac1{2\sqrt{2k}}\int_{-\infty}^{\infty}e^{-s^2}\,ds
=\sqrt{\frac\pi{8k}}.
\]
The limit follows by domination with \(e^{-s^2}\) and pointwise convergence. Thus \(1/(4I_k)\sim\sqrt{k/(2\pi)}\to\infty\). Because \(f_k(v)^2\) decreases strictly almost everywhere as \(k\) increases, \(I_k\) is strictly decreasing. Direct exact beta evaluations give \(I_5=262144/969969>1/4\) and \(I_6=4194304/16900975<1/4\); hence the sign transition in this family is exactly between indices five and six, and the sixth ratio is \(16900975/16777216\). All quantifiers, including arbitrary \(K\), now follow.

## Verification

The standalone standard-library script `checkerboard_inflation_check.py` reproduces \(I_k\) independently as a beta/factorial value and as an alternating binomial-integral sum for \(1\le k\le16\). It obtains the checkerboard statistic from actual four-cell probabilities, then integrates their piecewise-linear conditional CDFs using exact rational arithmetic, without inserting the closed-form \(\varepsilon^2/2\) in the calculation. It verifies the first strict inflation index, four cell masses, and an exact witness. Run with `python3 checkerboard_inflation_check.py`. Sixteen exact finite checks corroborate the algebra; copula validity, the all-integer claim, and the unbounded limit follow from the proof, not from this computation.

## Relationship to prior work

Rockel, *Measures of association for approximating copulas*, arXiv:2505.08045v2, Proposition 3.3 and Theorem 4.2, gives the checkerboard formula and proves \(\xi(B)\le\xi(C)\) for absolutely continuous copulas having TP\(_2\) density. Its Example 4.3 already supplies an SI checkerboard counterexample with a twofold inflation at one grid coarsening. Neither that finite counterexample nor the stronger TP\(_2\) theorem entails or rules out the absence of **every** multiplicative bound in the weaker class. The present polynomial family establishes this unbounded phenomenon while maintaining a uniform, strictly positive density between \(1/2\) and \(3/2\), strict SI, and one fixed \(2\times2\) grid; it does not contradict the TP\(_2\) result.

Ansari and Fuchs, *On continuity of Chatterjee's rank correlation and related dependence measures*, arXiv:2503.11390, proves continuity for SI copula sequences and notes checkerboard approximation convergence. That qualitative asymptotic result for approximating a fixed copula does not place a uniform relative error bound across varying smooth SI inputs at a fixed coarse grid. Classic generalized FGM-type separable copulas are used as a construction template; the exact family, rank-dependence calculation, and unbounded comparison are the specific claims here.

## Limitations

The family shows unbounded relative inflation, not a nonvanishing absolute increase: \(\varepsilon_k\to0\) and both coefficients vanish. The result concerns the population \(2\times2\) checkerboard, not finite-sample bias of an estimated matrix, nor the rate of refinement for any individual fixed copula. It does not assert that the bound for TP\(_2\) densities fails, and does not classify the optimal ratio at a fixed smoothness/derivative norm bound. Search-based originality assessment cannot exclude unindexed equivalent calculations.

## References

1. M. Rockel, *Measures of association for approximating copulas*, arXiv:2505.08045, submitted 2025-05-12, version 2 dated 2026-05-22, especially Proposition 3.3, Theorem 4.2 and Example 4.3. https://arxiv.org/html/2505.08045v2
2. J. Ansari and S. Fuchs, *On continuity of Chatterjee's rank correlation and related dependence measures*, arXiv:2503.11390 (2025), especially Corollary 3.6 and Remark 3.7. https://arxiv.org/abs/2503.11390
3. S. Fuchs and M. Tschimpke, *Total positivity of copulas from a Markov kernel perspective*, *J. Math. Anal. Appl.* **518** (2023), 126629; for the hierarchy separating stochastic increase from density total positivity. https://arxiv.org/abs/2205.01914
