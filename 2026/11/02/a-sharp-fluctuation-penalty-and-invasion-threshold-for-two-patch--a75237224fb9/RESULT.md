# A sharp fluctuation penalty and invasion threshold for two-patch periodic dispersal

## Finding

In a density-independent population occupying two habitats of fixed but unequal quality, temporally *alternating the dispersal fraction* reduces the long-run growth multiplier **strictly and monotonically** as the alternating amplitude grows, even if the average dispersal fraction remains unchanged. For a source–sink pair, an explicit rational inequality gives the exact critical amplitude at which the invasion verdict changes from growth to decline. The statement is finite-amplitude and applies throughout the admissible parameter region, not merely to small fluctuations.

Write \(P_s=\begin{pmatrix}1-s&s\\s&1-s\end{pmatrix}\), \(D=\operatorname{diag}(a,b)\), and
\[
L(\delta)=\rho\!\left(P_{m+\delta}D P_{m-\delta}D\right).
\]
The two-period exponent per generation is \(\frac12\log L(\delta)\). For fixed \(a,b,m\), \(L(\delta)\) is a strictly decreasing function of \(\delta^2\) when \(a\ne b\); for \(a=b\), it is identically \(a^2\).

For a source–sink pair \(a>1\), \(0<b<1/a\), define
\[
t=(a+b)(1-m),\qquad u=ab(1-2m),\qquad C=(a+b)^2-4a^2b^2.
\]
Then \(C>0\), and the exact invasion classification is
\[
\begin{array}{rcl}
L(\delta)>1 &\Longleftrightarrow& (1-t+u)(1+t+u)+C\delta^2<0,\\
L(\delta)=1 &\Longleftrightarrow& (1-t+u)(1+t+u)+C\delta^2=0,\\
L(\delta)<1 &\Longleftrightarrow& (1-t+u)(1+t+u)+C\delta^2>0.
\end{array}
\]
If \(t>1+u\), the unique threshold occurs at
\[
\delta_c^2=\frac{(t-1-u)(1+t+u)}{(a+b)^2-4a^2b^2}.
\]
The phase transition occurs within the physical model exactly when \(\delta_c^2\le\min\{m,1/2-m\}^2\). Otherwise all admissible fluctuations retain growth; if \(t\le1+u\), no fluctuation can produce growth.

## Assumptions and scope

Let \(a,b>0\), let the average exchange rate satisfy \(0\le m\le1/2\), and select \(0\le\delta\le h:=\min\{m,1/2-m\}\). At each generation organisms reproduce in habitat \(1\) by multiplier \(a\) and habitat \(2\) by multiplier \(b\), then exchange habitats independently with the same symmetric fraction \(s\) in either direction. There is no density dependence, environmental variation in \(a,b\), movement mortality, immigration, or stochastic demographic extinction. The two exchange fractions are \(s_-=m-\delta\) and \(s_+=m+\delta\), alternating indefinitely; the temporal mean is exactly \(m\). For strictly positive initial abundances, the long-term per-generation logarithmic growth is \(\frac12\log L(\delta)\). The multiplication order can be reversed because \(AB\) and \(BA\) have the same characteristic polynomial for square matrices.

The source–sink subclaim additionally assumes \(a>1\) and \(0<b<1/a\), so the poor habitat cannot persist independently and \(ab<1\). A zero migration amplitude is the only admissible value at the endpoint means \(m=0\) and \(m=1/2\), so the strict comparison there is vacuous.

## Proof

Set \(x=\delta^2\) and \(M_s=P_sD\). Direct matrix multiplication gives the trace and determinant of the two-generation map:
\[
\begin{split}
T(x)&=\operatorname{tr}(M_{m+\delta}M_{m-\delta})=T_0-(a+b)^2x,\\
U(x)&=\det(M_{m+\delta}M_{m-\delta})=U_0-4a^2b^2x,\\
T_0&=(a^2+b^2)(1-m)^2+2abm^2,\\
U_0&=a^2b^2(1-2m)^2.
\end{split}
\]
Because both exchange fractions are in \([0,1/2]\), the two-generation matrix has nonnegative entries and nonnegative determinant, with strictly positive trace. Its two eigenvalues \(\lambda_+(x)\ge\lambda_-(x)\ge0\) are real. The larger is \(L(\delta)\), the larger root of
\[
f_x(z)=z^2-T(x)z+U(x).
\]
For \(a\ne b\), put \(K=4a^2b^2/(a+b)^2\). Substitution into the characteristic polynomial yields an identity **independent of amplitude**:
\[
f_x(K)=\frac{a^2b^2(a-b)^2}{(a+b)^4}\Big[4m(a+b)^2-3(a^2+b^2)-10ab\Big].
\]
Since \(m\le1/2\), the square bracket is at most \(-a^2-b^2-6ab<0\). Therefore \(f_x(K)<0\), and \(\lambda_-(x)<K<\lambda_+(x)\) for every admissible \(x\). Differentiating the characteristic identity \(f_x(\lambda_+(x))=0\) consequently gives
\[
\frac{d\lambda_+}{dx}=
\frac{4a^2b^2-(a+b)^2\lambda_+(x)}{2\lambda_+(x)-T(x)}
=-\frac{(a+b)^2[\lambda_+(x)-K]}{\lambda_+(x)-\lambda_-(x)}<0.
\]
The denominator is nonzero because \(f_x(K)<0\) separates the two roots. For \(a=b\), both matrices are scalar multiples of symmetric stochastic matrices; their product has Perron eigenvalue \(a^2\) because both stochastic matrices preserve the all-ones vector. At \(\delta=0\), the two-generation map is \(M_m^2\), with Perron eigenvalue \(\rho(M_m)^2\). This proves the strict fixed-mean penalty including the endpoint cases.

For the source–sink classification, \(ab<1\). As \(0\le U(x)\le (ab)^2<1\), the smaller eigenvalue satisfies \(0\le\lambda_-(x)<1\), even if the larger one exceeds one. Hence the sign of
\[
f_x(1)=(1-\lambda_+(x))(1-\lambda_-(x))
\]
is exactly the sign of \(1-\lambda_+(x)\). Since
\[
f_x(1)=(1-t+u)(1+t+u)+\big[(a+b)^2-4a^2b^2\big]x,
\]
the asserted trichotomy follows. Moreover \(a+b\ge 2\sqrt{ab}>2ab\), so \(C>0\). This proves uniqueness and the formula for the critical squared amplitude, subject to admissible amplitude bounds. If \(t\le1+u\), the zero-amplitude multiplier does not exceed one and the strict penalty prevents dispersal fluctuations from improving it.

For a fully rational example, take \(a=7/5\), \(b=1/10\), and \(m=1/4\). The fixed-rate annual matrix is
\[
M_{1/4}=\begin{pmatrix}21/20&1/40\\7/20&3/40\end{pmatrix}
\]
with \(\det(I-M_{1/4})=-11/200\), so its Perron eigenvalue exceeds one. Alternating between \(m-\delta=0\) and \(m+\delta=1/2\) gives
\[
M_{1/2}M_0=\begin{pmatrix}49/50&1/200\\49/50&1/200\end{pmatrix},
\qquad L(1/4)=197/200<1.
\]
The critical squared amplitude is \(\delta_c^2=4829/86864<1/16\), verifying a strict threshold reversal with unchanged average dispersal. No numerical approximation is needed for either side of this comparison.

## Verification

The accompanying standalone `check.py` recomputes the two-generation trace and determinant with exact rational matrix arithmetic across a parameter grid, checks the amplitude-independent characteristic identity, verifies the rational example and threshold formula, and provides supplementary finite monotonicity tests. Run `python3 check.py` with the standard library. These computations check specified instances and symbolic-formula substitutions, not an infinite quantifier by enumeration; the preceding inequalities prove the full theorem.

## Relationship to prior work

Temporal variation of marine connectivity and its effect on metapopulation growth are established research topics. Watson et al. (2012) studied stochastic changing seascapes, with analytical and biophysical comparisons between variable and constant connectivity. Its publicly accessible abstract describes stochastic outcomes as generally, but not uniformly, smaller; its full argument and appendices could not be inspected here. Snyder, Paris and Vaz (2014), whose openly available full article was inspected, analyze a perturbative, small-fluctuation penalty and numerical marine connectivity models, rather than giving an exact two-season monotonicity and a source–sink threshold for this specified two-patch law. Schreiber and Li (2010) analyze evolutionarily stable dispersal phenotypes when *habitat fitnesses vary in time*, distinct from the present fixed habitat fitnesses with externally alternating dispersal fractions. The 2023 review by Peniston and coauthors explicitly documents both decreasing and increasing growth under differing connectivity covariances; it does not state this fixed-mean exact two-patch classification.

The mathematical novelty asserted here is consequently limited to the exact finite-amplitude two-patch monotonicity, closed source–sink threshold, and associated strict invasion reversal, not to the qualitative insight that temporal dispersal fluctuations can be harmful. Broader matrix-product and older connectivity theorems might subsume the result; historical priority has not been independently established.

## Limitations

This is a deterministic density-independent linear approximation, not a model of finite stochastic extinction, density regulation, directional migration, multiple life stages or varying habitat quality. The strict penalty need not generalize to arbitrary numbers of patches or arbitrary connectivity matrices, particularly when dispersal correlations can be negative. The full text and enhancement of the directly relevant Watson et al. (2012) paper were not inspected, and independent historical-priority confirmation remains outstanding. The formula identifies growth when rare, not a sustainable equilibrium biomass or management optimum.

## References

- Watson, J. R., Kendall, B. E., Siegel, D. A., and Mitarai, S. (2012). *Changing Seascapes, Stochastic Connectivity, and Marine Metapopulation Dynamics*. The American Naturalist 180, 99–112. First public online 2012-05-24. https://doi.org/10.1086/665992
- Snyder, R. E., Paris, C. B., and Vaz, A. C. (2014). *How Much Do Marine Connectivity Fluctuations Matter?* The American Naturalist 184, 523–530. https://doi.org/10.1086/677925
- Schreiber, S. J., and Li, C.-K. (2010/2011). *Evolution of unconditional dispersal in periodic environments*. https://arxiv.org/abs/1007.5267
- Peniston, J. H., and colleagues (2023). *Ecological and evolutionary consequences of temporal variation in dispersal*. Ecography, e06699. https://doi.org/10.1111/ecog.06699
