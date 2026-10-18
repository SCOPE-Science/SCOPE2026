# Exact singular mass and conditional atoms of the clipped Bernoulli-correlation copula

## Finding

For the bivariate correlation-based copula of Miralles-Dolz, Gray, Patelli and Ferson, every parameter \(0<|\rho|<1\) produces a measure with **both an absolutely continuous and a singular component**. The exact singular fraction is

\[
\boxed{\Pr(\text{singular component})=-\frac{\rho^2\log(\rho^2)}{1-\rho^2}.}
\]

At positive correlation the singular component is supported on two curves that are **not** the main diagonal. Its conditional atoms and a complete continuous-density formula are given below. For \(|\rho|=1/2\), the singular fraction is \(\frac23\log 2\), approximately \(0.462098120373297\). At zero correlation it is zero, and at \(|\rho|=1\) it is one. The singular fraction is strictly increasing in \(|\rho|\).

## Assumptions and scope

For \(u,v\in[0,1]\), put

\[
W(u,v)=\max(0,u+v-1),\qquad M(u,v)=\min(u,v),
\]
\[
G_\rho(u,v)=uv+\rho\sqrt{u(1-u)v(1-v)},\qquad
C_\rho(u,v)=\min\bigl(M(u,v),\max(W(u,v),G_\rho(u,v))\bigr).
\]

The previously introduced function \(C_\rho\) is a copula for \(-1\le\rho\le1\). Let \((U,V)\) have joint distribution function \(C_\rho\); its two marginals are uniform on \([0,1]\). The statements below concern the **joint probability measure** and a conditional distribution of \(V\) given \(U=u\), for almost every \(u\in(0,1)\). No absolute-continuity assumption is made.

For \(0<r=\rho<1\) and \(s=r^2\), define

\[
L_r(u)=\frac{s u}{1-u+s u},\qquad
H_r(u)=\frac{u}{s+(1-s)u},
\]
\[
j_L(u)=\frac{s}{2(1-u+s u)},\qquad
j_H(u)=\frac{s}{2(s+(1-s)u)}.
\]

The conditional law of \(V\) given \(U=u\) has an atom of probability \(j_L(u)\) at \(v=L_r(u)\), another of probability \(j_H(u)\) at \(v=H_r(u)\), and continuous conditional density

\[
c_r(u,v)=1+\frac{r(1-2u)(1-2v)}{4\sqrt{u(1-u)v(1-v)}}
\]

when \(L_r(u)<v<H_r(u)\), with zero density elsewhere. Consequently the singular part of the planar joint law is the sum of two graph-supported measures, each of mass \(-s\log(s)/[2(1-s)]\). The continuous part has total mass \(1+s\log(s)/(1-s)\). In logit coordinates, the two graphs obey

\[
\operatorname{logit}(v)=\operatorname{logit}(u)\pm2\log(1/r),\qquad
\operatorname{logit}(t)=\log\!\frac{t}{1-t}.
\]

For \(\rho=-r\), reflect the positive-correlation law across \(v=1/2\): the graph locations become \(1-L_r(u)\) and \(1-H_r(u)\), with their corresponding masses unchanged. All endpoint parameter values are understood directly through the copulas \(C_0(u,v)=uv\), \(C_1(u,v)=M(u,v)\), and \(C_{-1}(u,v)=W(u,v)\).

## Proof

**1. Locate the clipping boundaries.** Fix \(0<r<1\) and \(0<u<1\). Comparison of \(G_r(u,v)\) with the upper Fréchet bound gives the exact three-region formula

\[
C_r(u,v)=
\begin{cases}
v,&0\le v\le L_r(u),\\
G_r(u,v),&L_r(u)<v<H_r(u),\\
u,&H_r(u)\le v\le1.
\end{cases}
\]

Indeed, the equations \(G_r(u,v)=v\) and \(G_r(u,v)=u\) in the respective regions \(v<u\) and \(v>u\) reduce, after squaring nonnegative terms, to \(v=L_r(u)\) and \(v=H_r(u)\); both inequalities reverse at their respective crossings. In particular \(0<L_r(u)<u<H_r(u)<1\).

**2. Extract the conditional jumps.** The conditional distribution function is the almost-everywhere partial derivative \(F_{V\mid U=u}(v)=\partial_u C_r(u,v)\). Its formula is zero for \(v<L_r(u)\), equals

\[
\partial_u G_r(u,v)=v+\frac{r(1-2u)\sqrt{v(1-v)}}{2\sqrt{u(1-u)}}
\]

between the two boundaries, and equals one for \(v>H_r(u)\). Taking the one-sided limits at each boundary produces the positive jumps

\[
\partial_u G_r(u,L_r(u))=\frac{L_r(u)}{2u}=j_L(u),
\]
\[
1-\partial_u G_r(u,H_r(u))=\frac{1-H_r(u)}{2(1-u)}=j_H(u).
\]

Differentiating the middle expression in \(v\) gives the stated \(c_r(u,v)\). For fixed \(u\), integrating this continuous term plus the two jumps gives total conditional probability exactly one, since the CDF runs from zero to one.

**3. Check positivity of the continuous component.** Set \(a=\sqrt{u/(1-u)}\) and \(b=\sqrt{v/(1-v)}\). In the middle strip, \(r<b/a<1/r\). When \((1-2u)(1-2v)\ge0\), the mixed derivative is at least one. Otherwise, after possibly swapping coordinates, \(a<1<b\). The identity

\[
(b-a)^2-(1-a^2)(b^2-1)=(ab-1)^2\ge0
\]

and \(1<b/a<1/r\) give

\[
c_r(u,v)\ge1-\frac r4\left(\frac ba+\frac ab-2\right)
\ge1-\frac{(1-r)^2}{4}>0.
\]

Thus the continuous density is nonnegative everywhere in its support, and the two positive jumps define the only additional conditional mass.

**4. Integrate both graph components.** Since the marginal law of \(U\) is uniform, the two graph masses are

\[
\int_0^1 j_L(u)\,du=\int_0^1 j_H(u)\,du
=-\frac{s\log s}{2(1-s)}.
\]

Both graphs have two-dimensional Lebesgue measure zero, whereas the middle-strip density is absolutely continuous. Hence these are exactly the singular and absolutely continuous pieces of the joint law. The aggregate singular mass is \(-s\log(s)/(1-s)\). The complementary mass is its complement.

**5. Negative and endpoint parameters.** The elementary copula-reflection identity

\[
C_{-r}(u,v)=u-C_r(u,1-v)
\]

reflects all conditional atoms and the continuous component, preserving their total masses. The copulas at \(\rho=0,1,-1\) have the stated pure absolutely continuous or pure singular forms. Finally, for \(0<s<1\),

\[
\frac{d}{ds}\!\left(-\frac{s\log s}{1-s}\right)
=\frac{-\log s-1+s}{(1-s)^2}>0,
\]

which proves strict monotonicity and the endpoint limits.

## Verification

Run `python3 verify_copula_decomposition.py` with Python 3 and no external dependencies. The accompanying verifier checks exact rational identities for clipping curves and jump weights over a grid, evaluates boundary derivative identities, tests continuous density positivity, and numerically integrates the conditional densities and singular curve masses. It passes 20,814 supplementary checks. These finite checks test the stated formulas, not the general theorem; the universal proof is the calculation above.

## Relationship to prior work

Miralles-Dolz, Gray, Patelli and Ferson introduced the correlation-clipped Boolean-operator copula in their 2022 contribution; their copula formula and clipping mechanism are **prior work**, not claimed here. Their open preprint provides a lawful complete-text version. The 2023 proof paper establishes the copula property and derives the interior mixed partial derivative and boundary curves. Neither inspected text states the conditional atomic probability measures, the Lebesgue decomposition, or the integrated singular fraction obtained here. General studies of copulas with singular components include the 2017 transformed-copula family of Xie, Yang and Zhu, whose distinguished singular support lies on the main diagonal rather than the two non-diagonal graph supports in this result. These distinctions describe known coverage, not proof of absolute priority.

## Limitations

This is an exact result for the clipped correlation-based copula, not for every copula parameterized by Pearson correlation or for arbitrary multidimensional extensions. The dependence parameter is the Bernoulli-correlation parameter of the construction and should not be reinterpreted as Pearson correlation of the continuous uniform pair. The result characterizes measure structure, not a universal statistical estimator. An earlier equivalent derivation outside the inspected publications or research records cannot be excluded. Independent validation has not been performed.

## References

1. E. Miralles-Dolz, A. Gray, E. Patelli, S. Ferson, *Correlated Boolean Operators for Uncertainty Logic* (first online July 4, 2022), DOI: 10.1007/978-3-031-08971-8_64; open preprint `arXiv:2207.10583v1` (July 21, 2022), https://arxiv.org/html/2207.10583v1.
2. E. Miralles-Dolz et al., *Correlation-Based And-Operations Can Be Copulas: A Proof* (January 13, 2023), `arXiv:2301.05507v1`, https://arxiv.org/html/2301.05507v1.
3. J. Xie, Y. Yang, W. Zhu, *A family of transformed copulas with singular component* (2017), `arXiv:1710.01200v1`, https://arxiv.org/abs/1710.01200.
4. F. Durante and P. Jaworski, *A New Characterization of Bivariate Copulas* (2010), DOI: 10.1080/03610920903151459.
