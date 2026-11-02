# Exact two-file retrieval latencies for repeated rank-one mixed parity columns

## Finding
Let \(G=[I_{u+v}\mid \lambda_1g\mid\cdots\mid\lambda_Mg]\) be a systematic generator matrix, where \(g\) combines both files and all \(\lambda_j\) are nonzero. Put \(n=u+v+M\). If \(g\) has precisely \(a\) nonzero entries in the first file and \(b\) in the second, then the expected numbers of uniform independent draws with replacement required to recover either file are
\[
\begin{aligned}
E_1&=n\left[H_u-a\left(\frac{1}{u+b}-B(u+b,M+1)\right)\right],\\
E_2&=n\left[H_v-b\left(\frac{1}{v+a}-B(v+a,M+1)\right)\right].
\end{aligned}
\]
Here \(H_s=\sum_{j=1}^{s}j^{-1}\) and \(B(s,M+1)=(s-1)!M!/(s+M)!\) for positive integers \(s,M\). For every \(u+v\ge3\),
\[
\frac{u}{E_1}+\frac{v}{E_2}<1.
\]
The strict inequality holds for every finite field and arbitrarily large \(M\), including \(M>(u+v-2)/2\).

## Assumptions and scope
Let \(q\) be any prime power. Fix positive integers \(u,v,M\) with \(u+v\ge3\), and \(1\le a\le u\), \(1\le b\le v\). The vector \(g\in\mathbb F_q^{u+v}\) has exactly \(a\) nonzero first-file and \(b\) nonzero second-file coordinates; the scalars \(\lambda_1,\ldots,\lambda_M\) are nonzero. Every column index, including repeated proportional columns, is sampled independently with replacement at probability \(1/n\). Recovery of file \(i\) means that its complete coordinate subspace is contained in the span of observed columns. Expectations count individual discrete samples, not distinct sampled columns. No assumption of maximum-distance-separability or distinct projective parity directions is made.

## Proof
Since every parity column is proportional to \(g\), their joint span contributes at most one extra dimension. For recovery of the first file, all \(u\) systematic first-file columns always suffice. If one first-file coordinate is missing, recovery is additionally possible precisely when (i) this coordinate belongs to the support of \(g\), (ii) all \(b\) second-file support coordinates are present, and (iii) at least one parity column has appeared. Missing two first-file coordinates cannot be repaired by a single extra direction. This exhausts all recovery cases, and the second-file statement follows symmetrically.

Poissonize the discrete draws using a rate-\(n\) Poisson process whose marks are the \(n\) uniformly chosen column labels. Each systematic label has an independent exponential first-arrival time of rate one; the first arrival among the \(M\) parity labels has exponential rate \(M\), independent of the systematic times. Write \(x=1-e^{-t}\). The probability of having recovered the first file by time \(t\) is
\[
(1-e^{-t})^u+a e^{-t}(1-e^{-t})^{u+b-1}(1-e^{-Mt}).
\]
The second term is a disjoint union indexed by the single missing supported first-file coordinate. Integrating the failure probability gives
\[
\begin{aligned}
\mathbb E[T_1]
&=H_u-a\int_0^\infty e^{-t}(1-e^{-t})^{u+b-1}(1-e^{-Mt})\,dt\\
&=H_u-a\int_0^1 y^{u+b-1}(1-(1-y)^M)\,dy\\
&=H_u-a\left(\frac{1}{u+b}-B(u+b,M+1)\right).
\end{aligned}
\]
Here \(T_1\) is continuous-time recovery; since Poisson arrival times have mean interarrival \(1/n\) and are independent of sampled labels, \(E_1=n\mathbb E[T_1]\). Interchanging the two files proves the formula for \(E_2\).

For the strict inequality, abbreviate \(A=E_1/n\), \(C=E_2/n\). Positivity of the beta term gives
\[
A>H_u-\frac{a}{u+b},\qquad C>H_v-\frac{b}{v+a}.
\]
For every integer \(s\ge2\) and \(1\le t\le s\), \(r\ge1\), one has
\[
H_s-\frac{t}{s+r}\ge H_s-\frac{s}{s+1}>\frac{2s}{2s+1}.
\]
At \(s=2\) the middle expression is \(5/6>4/5\); for \(s\ge3\) it exceeds one. Consequently, for \(u,v\ge2\), \(u/A<u+1/2\) and \(v/C<v+1/2\), so \(u/A+v/C<u+v+1\le n\).

If \(u=1\) and \(v\ge2\), necessarily \(a=1\). The first bound gives \(1/A<1+1/b\). When \(b\ge2\), combine this with \(v/C<v+1/2\) to obtain \(1/A+v/C<v+2\le n\). When \(b=1\), the second bound yields \(C>H_v-1/(v+1)>1\), hence \(1/A+v/C<2+v\le n\). The case \(v=1\) is symmetric. Dividing by \(n\) proves \(u/E_1+v/E_2<1\).

## Verification
The accompanying standalone `verify.py` performs rational-arithmetic comparison of the closed forms with an independent subset-state expected-hitting-time recurrence over 297 parameter tuples, as well as an extended exact-rational inequality sweep for both file dimensions up to 11 and mixed-column multiplicities in \(\{1,2,3,5,9,20,50\}\). `verification_output.txt` records passing assertions. These finite checks independently test the formulas but do not replace the all-parameter probability and inequality arguments above.

## Relationship to prior work
Bar-Lev, *Coded Information Retrieval for Block-Structured DNA-Based Data Storage* (first public 17 March 2026), defined the two-file retrieval-time tradeoff and proposed the universal hyperbolic inequality. Vlachos and Bar-Lev, *A Hyperbolic Bound for File Retrieval in DNA-Based Data Storage* (first public 28 September 2026), proved that inequality for systematic codes with at most \((u+v-2)/2\) mixed columns and treated the single-mixed-column setting separately. Those results cover the applicable small-\(M\) part of this claim. The present exact formulas use the one-dimensional dependence of all mixed columns; they imply the inequality also when the number of mixed columns exceeds the published threshold, without a bound on their multiplicity. We do not claim priority for the previously covered cases or for elementary coupon-collector identities.

## Limitations
The classification assumes all non-systematic columns are proportional, both files have at least one supported coordinate in the common mixed vector, and samples are uniform and noiseless. The theorem does not cover several independent mixed directions, nonuniform column sampling, noisy channels, nonsystematic codes, or the boundary case \(u=v=1\). The general conjecture remains unresolved. Earlier or unindexed coverage of this special family cannot be categorically excluded.

## References
1. D. Bar-Lev, *Coded Information Retrieval for Block-Structured DNA-Based Data Storage*, arXiv:2603.17154 (first submitted 17 March 2026), https://arxiv.org/abs/2603.17154.
2. C. V. A. Vlachos and D. Bar-Lev, *A Hyperbolic Bound for File Retrieval in DNA-Based Data Storage*, arXiv:2609.36067 (first submitted 28 September 2026), https://arxiv.org/abs/2609.36067.
