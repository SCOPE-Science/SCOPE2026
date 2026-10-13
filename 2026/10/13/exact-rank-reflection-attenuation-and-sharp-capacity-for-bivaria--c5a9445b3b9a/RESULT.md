# Exact rank-reflection attenuation and sharp capacity for bivariate copulas

## Finding
Let \((U,V)\) have an arbitrary bivariate copula, so both coordinates are uniform on \([0,1]\). Independently of \((U,V)\), flip a Bernoulli coin with retention probability \(p\in[0,1]\) and define \(W_p=V\) on retention and \(W_p=1-V\) otherwise. Let the folded response be \(T=2\min\{V,1-V\}\), which is also uniform on \([0,1]\). Write \(\xi(Y\mid X)\) for the population Chatterjee rank correlation of the response \(Y\) on the predictor \(X\), with the response direction fixed.

**Exact attenuation identity.** For every bivariate copula, including singular copulas, and every \(p\in[0,1]\),
\[
\boxed{\xi(W_p\mid U)=(2p-1)^2\,\xi(V\mid U)+p(1-p)\,\xi(T\mid U).}
\]
Equivalently, the reflection-even conditional-rank component survives unchanged, while the reflection-odd component is multiplied by \((2p-1)^2\) in Chatterjee's coefficient. In particular,
\[
\xi(W_{1/2}\mid U)=\tfrac14\xi(T\mid U),\qquad
\xi(V\mid U)\ge\tfrac14\xi(T\mid U).
\]

**Sharp channel capacity and equality.** For every fixed \(p\), the attainable values over all bivariate copulas are exactly
\[
\boxed{0\le\xi(W_p\mid U)\le 1-3p(1-p).}
\]
The upper endpoint is attained. For \(p\ne1/2\), equality at the upper endpoint holds exactly when \(V\) is almost surely a measurable function of \(U\). For \(p=1/2\), upper equality holds exactly when \(T\) is almost surely a measurable function of \(U\); the original \(V\) need not be determined by \(U\). If \(p\ne1/2\), zero is equivalent to independence of \(U\) and \(V\); at \(p=1/2\), zero is equivalent to independence of \(U\) and \(T\).

For the fair coin, the resulting copula is invariant under reflecting its second coordinate and therefore has Kendall's tau and Spearman's rho both equal to zero. Nevertheless, its directed rank dependence can attain any value in \([0,1/4]\), even the upper endpoint. For fixed input copula, \(\xi(W_p\mid U)\) is nondecreasing in \(|2p-1|\); it is strictly increasing unless the original copula is already invariant under reflection of its second coordinate.

## Assumptions and scope
The coefficient is defined for a pair with a continuous uniform response by
\[
\xi(Y\mid U)=6\int_0^1\operatorname{Var}\bigl(\Pr\{Y\le t\mid U\}\bigr)\,dt.
\]
All conditional laws are understood up to null sets. The fair reflection of a copula \(C\) has distribution function \(S(C)(u,v)=\tfrac12[C(u,v)+u-C(u,1-v)]\). The findings make no smoothness, density, strict monotonicity or positivity-of-dependence assumptions, and include singular extremizers. Kendall and Spearman statements apply to the fair-reflected copula, not generally to the biased reflection for \(p\ne1/2\).

## Proof
**1. Reflection decomposition.** Let \(F_u(v)=\Pr\{V\le v\mid U=u\}\) and \(d(u,v)=F_u(v)-v\). This centered conditional CDF belongs to \(L^2([0,1]^2)\), and \(\xi(V\mid U)=6\|d\|_2^2\). Reflection of the response sends \(d(u,v)\) to \(-d(u,1-v)\) for almost every \((u,v)\). Define
\[
E(u,v)=\tfrac12[d(u,v)-d(u,1-v)],\qquad
O(u,v)=\tfrac12[d(u,v)+d(u,1-v)].
\]
The functions \(E\) and \(O\) are orthogonal in \(L^2([0,1]^2)\) by the change of variables \(v\mapsto1-v\). The centered conditional CDF of \(W_p\) is \(E+(2p-1)O\). Consequently,
\[
\xi(W_p\mid U)=6\|E\|_2^2+6(2p-1)^2\|O\|_2^2,
\qquad
\xi(V\mid U)=6\|E\|_2^2+6\|O\|_2^2.
\]

**2. Folding identifies the even component.** Since \(V\) is uniform, \(T=2\min(V,1-V)\) is uniform. For almost all \((u,t)\),
\[
\Pr(T\le t\mid U=u)-t=d(u,t/2)-d(u,1-t/2)=2E(u,t/2).
\]
Because \(E(u,1-v)=-E(u,v)\), its square is symmetric about \(v=1/2\). Substituting \(t=2v\) gives
\[
\xi(T\mid U)=6\int_0^1\!\int_0^1 4E(u,t/2)^2\,du\,dt
=24\|E\|_2^2.
\]
Therefore \(6\|E\|_2^2=\xi(T\mid U)/4\). Combining with step 1 proves the boxed identity and the nonnegative orthogonal difference
\[
\xi(V\mid U)-\tfrac14\xi(T\mid U)=6\|O\|_2^2\ge0.
\]
It also shows strict monotonicity in \(|2p-1|\) unless \(O=0\). The latter is equivalent to \(F_u(v)+F_u(1-v)=1\) almost everywhere, i.e. invariance of the original copula under response reflection.

**3. Sharp range and equality classifications.** For any continuous uniform response \(Y\), the total-variance identity yields \(0\le\xi(Y\mid U)\le1\); the upper endpoint occurs if and only if the response is a measurable function of \(U\), while zero occurs if and only if the response is independent of \(U\). Applying these facts to both \(V\) and \(T\) in the attenuation identity gives
\[
0\le \xi(W_p\mid U)\le (2p-1)^2+p(1-p)=1-3p(1-p).
\]
If \(p\ne1/2\), the coefficient of \(\xi(V\mid U)\) is positive, so upper equality implies \(\xi(V\mid U)=1\), which also forces \(\xi(T\mid U)=1\). At \(p=1/2\), only the folded coefficient survives, giving the different equality condition. The zero conditions follow from the nonnegative coefficients; in particular, for \(p\ne1/2\), \(\xi(V\mid U)=0\) is necessary and sufficient.

For attainability, fix \(a\in[0,1]\), let \(U,U'\) be independent uniform variables and let \(B\) be an independent Bernoulli variable with success probability \(a\). Take \(V=U\) when \(B=1\) and \(V=U'\) otherwise. Then, for all \(v,t\in[0,1]\),
\[
\Pr(V\le v\mid U)=v+a(\mathbf1_{\{U\le v\}}-v),
\]
and, since \(2\min(U,1-U)\) is uniform,
\[
\Pr(T\le t\mid U)=t+a\bigl(\mathbf1_{\{2\min(U,1-U)\le t\}}-t\bigr).
\]
Thus \(\xi(V\mid U)=\xi(T\mid U)=a^2\), and
\[
\xi(W_p\mid U)=a^2[1-3p(1-p)].
\]
As \(a\) varies from zero to one, this attains every value in the asserted sharp interval. At \(a=1\) both responses are measurable functions of \(U\), and at \(a=0\) both are independent of \(U\). At \(p=1/2\) the law of \((U,W_p)\) is reflection-invariant. Reflecting its second coordinate reverses the signs of Kendall's tau and Spearman's rho without changing its law, forcing both coefficients to be zero. This completes the proof.

## Verification
The analytic proof covers all measurable copulas and every real \(p\in[0,1]\); no finite test is used as a universal argument. The standalone `verify.py` checks the exact attenuation identity and capacity bound using Python rational arithmetic on 840 nonsymmetric biased-reflection checkerboard cases and the fair-reflection identity on 240 additional checkerboards. It also checks exact closed-form checkerboard families and the continuous construction's rational identities. Run `python verify.py` with Python 3; the reported run passed 2,752 exact-rational assertions. All calculations are finite corroboration only.

## Relationship to prior work
Rockel (2026, arXiv:2606.22074v1) proves \(\xi(C)\le\tau(C)\) for stochastically increasing copulas and exhibits directional failures outside that class. The present identity instead concerns a response-reflection channel without any stochastic-increasingness assumption. For its fair output, \(\tau=0\) while \(\xi\) can be positive, so the cited positive-dependence theorem does not supply this identity. Ansari and Rockel (2025, arXiv:2506.15897) characterize the unrestricted joint region of Chatterjee's coefficient and Spearman's rho; the full region at \(\rho=0\) cannot itself yield the channel-specific sharp interval or attenuation law. Ansari and Rockel (2024, arXiv:2310.17307v3), Table 6, provide exact rank-correlation formulas for the Fréchet mixture family, which already covers the extremal fair mixture and its value \(1/4\); that special-family value is not claimed as new. General data-processing inequalities anticipate a ceiling under added reflection noise, but not the displayed exact universal two-component identity or its equality phase transition.

## Limitations
The random reflection coin is independent of the input, and the response is uniformized before reflection; nonuniform transformations or a coin whose bias depends on the original observation need not obey the identity. The result is about the population coefficient, not finite-sample bias or sampling distributions. It does not classify the full joint attainable region of Chatterjee's coefficient with Kendall's tau or Spearman's rho for general copulas. The zero-concordance statement holds for the fair coin. Earlier unpublished or unindexed formulations of the identity cannot be ruled out; no independent scientific audit is represented.

## References
1. Marcus Rockel (2026), *Kendall and Spearman bounds for Chatterjee's rank correlation under positive dependence*, arXiv:2606.22074v1, first publicly posted 20 June 2026. https://arxiv.org/abs/2606.22074
2. Jonathan Ansari and Marcus Rockel (2025), *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, arXiv:2506.15897, initially posted 18 June 2025. https://arxiv.org/abs/2506.15897
3. Jonathan Ansari and Marcus Rockel (2024), *Dependence properties of bivariate copula families*, arXiv:2310.17307v3, especially Table 6 and Section 3.2; first publicly posted 26 October 2023. https://arxiv.org/abs/2310.17307
