# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof reduces the mode displacement to Jefferson--D'Hondt seat excess, then applies Janson's fixed-proportion random-house-size limit theorem with \(\beta=1\). Janson explicitly states the marginal limit as a sum of independent centered uniforms and, because seat excess is bounded, proves convergence of all moments. This justifies averaging every fixed Bernoulli polynomial appearing in Elezović's coefficient formula.

The generating-function cancellation was checked algebraically:
\[
\frac{z}{e^z-1}e^{z/2}\frac{\sinh(z/2)}{z/2}=1.
\]
The remaining generating function is
\[
e^w((e^w-1)/w)^{n-2},
\]
whose coefficients follow directly from the standard exponential generating function for Stirling numbers of the second kind. Substitution cancels all dependence on \(p\) because \(p_i^{-k}p_i^{k+1}=p_i\) and \(\sum_i p_i=1\). The first four closed forms were checked against the general Stirling formula. A direct mode computation for a generic three-category vector agrees numerically with the first four predicted averages.

## Originality

Elezović's arXiv:2609.20229v1 explicitly says that passage from its off-slice floor reference to an on-slice reference such as the mode is open and that on-slice averages require a different computation. The same paper identifies the mode with Jefferson--D'Hondt apportionment. Janson's 2014 work already provides the missing asymptotic distribution of Jefferson seat excesses for fixed rationally independent proportions and uniform house size, including convergence of all moments. The Janson paper was not located in Elezović's reference list.

Accordingly, the originality claim is deliberately narrow: **to the best of our knowledge**, the all-orders modal Cesàro formula, its Stirling-number closed form, and the resulting universality in \(p\) have not been stated previously. The underlying seat-excess distribution, Bernoulli-polynomial expansion, and Stirling generating function are prior art. This finding is therefore an overlooked-literature bridge plus a closed coefficient extraction, not a new apportionment limit theorem.

Two older papers are the main residual literature risk. Schwingenschlögl--Drton (2006), DOI 10.1016/j.spl.2006.04.014, studies conditional seat-excess variances under random vote proportions; its abstract and bibliographic record were inspected, but the full text was not inspected. Drton--Schwingenschlögl (2004), DOI 10.1016/j.laa.2003.09.005, studies volumes of rounding polytopes and average properties of rounding methods; its abstract and bibliographic record were inspected, but the full text was not inspected. Either could contain related low-order moment identities, but Janson explicitly distinguishes his fixed-proportion/random-house-size regime from earlier random-proportion work, and neither inspected abstract indicates an all-orders Bernoulli/Stirling specialization. The residual risk is therefore real but limited.

Searches using combinations of “multinomial mode”, “Jefferson/D'Hondt”, “seat excess”, “Bernoulli polynomial”, “Cesàro”, and “on-slice” did not locate the displayed all-orders formula or an equivalent statement.

## Value

The result closes a concrete question left open in a recent probability paper and does so without new equidistribution geometry: the needed stochastic law was already available in the apportionment literature. The final formula is explicit at every order and unexpectedly universal in the category probabilities. It also exposes a useful mechanism: Bernoulli-polynomial expectations scale by exactly the power needed to collapse Elezović's weighted sum.

## Limitations

The theorem covers the generic rationally independent regime only; resonant rational vectors and tie rules are not classified. It concerns logarithmic coefficients \(c_k\), not arbitrary multiplicative Bell-polynomial coefficients after exponentiation. No uniformity in coefficient order or as \(p\) approaches a resonance is proved. The numerical artifact is confirmatory and is not used in place of the analytic proof.
