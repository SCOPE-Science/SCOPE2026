# All-\(k\) dual-volume bounds for simplicial and simple approximants

## Finding

Let \(d\ge2\) and \(0\le k\le d-1\). Define
\[
\Lambda_{d,k}(M)=
\begin{cases}
M,&k=0,\\
\dfrac{M+k\binom{d+1}{k+1}}{\binom d k},&1\le k\le d-2,\\
\dfrac{M+(d+1)(d-2)}{d-1},&k=d-1.
\end{cases}
\]
Set
\[
a_d=
\left(
\frac{\omega_d}{4\kappa_{d-1}}
\right)^{2/(d-1)}.
\]
For \(q\ne0\), set
\[
c_{d,q}=
\begin{cases}
\widetilde V_{|q|}(B_d),&0<|q|\le d,\\
\kappa_d,&|q|>d.
\end{cases}
\]

If \(P\subset B_d\) is a full-dimensional simplicial polytope, the origin lies in its interior, and
\[
f_k(P)\le M,
\]
then, for every \(q\ne0\),
\[
\boxed{
\widetilde\Delta_q(B_d,P)
\ge
\frac{1-e^{-1}}2 c_{d,q}
\min\!\left\{
1,
\frac{|q|}{2}a_d\Lambda_{d,k}(M)^{-2/(d-1)}
\right\}.
}
\]
For \(q=0\),
\[
\boxed{
\widehat\Delta_0(B_d,P)
\ge
\frac14 a_d\Lambda_{d,k}(M)^{-2/(d-1)}.
}
\]

If \(Q\supset B_d\) is a simple polytope and
\[
f_k(Q)\le M,
\]
put
\[
\ell=d-1-k.
\]
Then, for every \(q\ne0\),
\[
\boxed{
\widetilde\Delta_q(B_d,Q)
\ge
\frac{3(1-e^{-1})}{4}c_{d,q}
\min\!\left\{
1,
\frac{|q|}{6}a_d\Lambda_{d,\ell}(M)^{-2/(d-1)}
\right\}.
}
\]
For \(q=0\),
\[
\boxed{
\widehat\Delta_0(B_d,Q)
\ge
\frac18 a_d\Lambda_{d,\ell}(M)^{-2/(d-1)}.
}
\]

Hence the recent nonasymptotic dual-volume estimates, which are stated for only half of the \(f\)-vector for arbitrary polytopes, extend to every face dimension on the natural simplicial-inscribed and simple-circumscribed subclasses.

## Assumptions and scope

The notation \(B_d\), \(\kappa_d\), \(\omega_d\), \(\widetilde\Delta_q\), \(\widehat\Delta_0\), and \(\widetilde V_q\) is that of Hoehner--Schuett--Werner.

The inscribed result assumes that \(P\) is simplicial and that the origin lies in its interior. The circumscribed result assumes that \(Q\) is simple. These combinatorial hypotheses are essential to the proof because the argument converts a bound on an arbitrary face number to a bound on the number of vertices or facets by the classical Lower Bound Theorem.

If the numerical bound \(M\) is below the minimum possible number of \(k\)-faces of a full-dimensional polytope in the stated class, then the corresponding statement is vacuous.

The theorem does not solve the source's open all-\(k\) problem for arbitrary polytopes. It gives a complete all-\(k\) answer only on the two dual natural subclasses specified above.

## Proof

For a simplicial \(d\)-polytope with \(v\) vertices, let \(\phi_{d,j}(v)\) denote the number of \(j\)-faces of a stacked \(d\)-polytope with \(v\) vertices. The classical Lower Bound Theorem gives
\[
f_j(P)\ge \phi_{d,j}(v).
\]
For \(1\le j\le d-2\),
\[
\phi_{d,j}(v)
=
\binom d j v-j\binom{d+1}{j+1},
\]
while
\[
\phi_{d,d-1}(v)
=
(d-1)v-(d+1)(d-2).
\]
For \(j=0\), of course, \(f_0(P)=v\).

Consequently, if a simplicial \(P\) satisfies
\[
f_k(P)\le M,
\]
then
\[
f_0(P)\le\Lambda_{d,k}(M).
\]
The inequalities are tight on the stacked-polytope subsequences for which the right-hand face count is realized exactly.

Now suppose \(P\subset B_d\), the origin lies in the interior of \(P\), and \(P\) is simplicial. Write
\[
v=f_0(P).
\]
The vertex case of Theorem 3.7 of Hoehner--Schuett--Werner applies with the actual vertex count \(v\). For \(q\ne0\), it yields
\[
\widetilde\Delta_q(B_d,P)
\ge
\frac{1-e^{-1}}2 c_{d,q}
\min\!\left\{
1,
\frac{|q|}{2}a_d v^{-2/(d-1)}
\right\}.
\]
Since
\[
v\le\Lambda_{d,k}(M)
\]
and the displayed right-hand side is decreasing in its complexity argument, replacing \(v\) by \(\Lambda_{d,k}(M)\) gives the claimed inequality. The logarithmic estimate follows identically from the \(q=0\) part of the same theorem.

For the circumscribed statement, let \(Q\supset B_d\) be simple and consider its polar \(Q^\circ\), which is simplicial. Polarity reverses face dimensions, so
\[
f_{d-1}(Q)=f_0(Q^\circ)
\]
and
\[
f_k(Q)=f_{d-1-k}(Q^\circ).
\]
With
\[
\ell=d-1-k,
\]
the Lower Bound Theorem applied to \(Q^\circ\) therefore gives
\[
f_{d-1}(Q)
\le
\Lambda_{d,\ell}(M).
\]
Apply the facet case of Theorem 3.8 of Hoehner--Schuett--Werner to \(Q\) with its actual number of facets, and then replace that number by the displayed upper bound. This gives the two asserted circumscribed inequalities.

## Verification

The source's Theorems 3.7 and 3.8 were checked in the full arXiv text, including their endpoint cases \(k=0\) and \(k=d-1\), their constants, and the \(q=0\) formulas. The same text explicitly asks whether the dual-volume estimate can be extended to every \(k\) for arbitrary polytopes.

The bundled checker verifies the algebraic inverse relationship between the stacked-polytope face formulas and \(\Lambda_{d,k}\) for all
\[
2\le d\le40,
\]
all face dimensions, and a range of vertex counts. It also verifies the polarity index conversion \(k\mapsto d-1-k\) and the endpoint formulas.

These finite checks are supplementary. The all-dimensional proof rests on the classical Lower Bound Theorem and direct substitution into the two endpoint theorems of the recent source.

## Relationship to prior work

Hoehner--Schuett--Werner prove nonasymptotic dual-volume lower bounds for arbitrary inscribed polytopes when
\[
0\le k\le\left\lfloor\frac d2\right\rfloor
\]
and for arbitrary circumscribed polytopes when
\[
\left\lceil\frac d2\right\rceil-1\le k\le d-1.
\]
Their discussion explicitly asks for the remaining face dimensions. Their proof passes from endpoint vertex or facet bounds to intermediate face numbers using general \(f\)-vector inequalities.

The same authors' intrinsic-volume paper proves analogous arbitrary-polytope results only over those half-vector ranges. Its full text also recalls older simplicial asymptotic results that cover only
\[
0\le k\le\left\lfloor\frac d2\right\rfloor
\]
for inscribed polytopes and a high-dimensional terminal range for circumscribed simplicial polytopes.

Besau--Hoehner--Kur likewise derived earlier simplicial asymptotic consequences only over restricted ranges using the ``75% unimodality'' of the \(f\)-vector. None of these inspected approximation results uses the full classical Lower Bound Theorem to invert an arbitrary simplicial face count into an endpoint vertex count.

The new step is to insert the sharp stacked-polytope Lower Bound Theorem formula before applying the recent endpoint estimates. This supplies every \(k\) on the simplicial/simple subclasses, with an explicit effective complexity \(\Lambda_{d,k}(M)\) rather than merely replacing \(M\) by itself.

## Limitations

The result is conditional on simpliciality in the inscribed model and simplicity in the circumscribed model. It does not settle the source's open all-face problem for general polytopes.

The Lower Bound Theorem conversion is sharp as a combinatorial relation on stacked-polytope subsequences, but this does not imply that stacked polytopes are geometrically optimal approximants of the ball for the dual-volume deviations.

A residual bibliographic risk is that the same combination of the Lower Bound Theorem with endpoint approximation estimates may have appeared as an unstated or poorly indexed corollary elsewhere. Targeted searches of the recent approximation literature and source-specific terms did not locate such a statement.

## References

1. Steven Hoehner, Carsten Schuett, Elisabeth M. Werner, *Dual volume approximation of the Euclidean ball by polytopes with a fixed number of \(k\)-faces*, arXiv:2608.02554v1, 3 August 2026.
2. Steven Hoehner, Carsten Schuett, Elisabeth M. Werner, *Approximation of the Euclidean ball by polytopes with a fixed number of \(k\)-faces*, arXiv:2510.22771; International Mathematics Research Notices, 2026, rnag186.
3. Florian Besau, Steven Hoehner, Gil Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, International Mathematics Research Notices 2021 (22), 17456--17513, DOI: 10.1093/imrn/rnz277.
4. Gil Kalai, *Rigidity and the Lower Bound Theorem I*, Inventiones Mathematicae 88 (1987), 125--151; the stacked-polytope face formulas are also summarized in his survey on the combinatorial theory of convex polytopes.
