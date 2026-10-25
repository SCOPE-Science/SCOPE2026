# A positive-definite hexagonal radial function outside the square-radial Schoenberg class

## Finding

Define, for \(t\geq0\),
\[
\phi(t)=e^{-t}\left(1+\frac{13}{20}t+\frac16t^2\right).
\]
On \(\mathbb R^2\) define the regular-hexagonal norm
\[
N_H(u,v)=\max\{|u|,|v|,|u+v|\},
\]
and the square norm \(N_\infty(u,v)=\max\{|u|,|v|\}\). Then \(\phi(N_H(u,v))\) is a **strictly positive-definite** translation-invariant kernel on \(\mathbb R^2\), whereas \(\phi(N_\infty(u,v))\) is **not positive definite**. Consequently, \(\phi\) admits no representation
\[
\phi(t)=\int_{[0,\infty)}m_2(st)\,d\alpha(s),\qquad
m_2(t)=\int_t^\infty\frac{\sin v}{v}\,dv,
\]
with \(\alpha\) a finite positive measure. This gives an explicit negative answer to the necessity question for the sufficient hexagonal radial representation in Xu (2015, Theorems 1.2 and 3.1). The \(m_2\)-integral uses the conventional continuous value at the origin.

## Assumptions and scope

The Fourier transform is \(\widehat f(\xi,\eta)=\int_{\mathbb R^2}f(u,v)e^{-i(\xi u+\eta v)}\,du\,dv\); no positive normalization factor affects the sign. Both functions are real, continuous, and integrable. Positive definite means that every finite matrix \([\phi(N(x_j-x_k))]_{j,k}\) is positive semidefinite. Strict positive definiteness means strict positivity for pairwise distinct sites and nonzero coefficient vectors. The conclusion concerns the two stated norms and the stated exact profile, not all hexagonal radial functions.

## Proof

**1. Hexagonal Fourier transform.** In each of the six cones bounded by consecutive rays
\[
(1,0),\ (1,-1),\ (0,-1),\ (-1,0),\ (-1,1),\ (0,1),
\]
we may write \((u,v)=s r_j+t r_{j+1}\) with \(s,t\ge0\), unit Jacobian and \(N_H(u,v)=s+t\). For real \(z>0\), integration of \(e^{-zN_H}\) over the cones gives the sum
\[
F_z(\xi,\eta)=\sum_{j=1}^6\frac1{(z+i\langle(\xi,\eta),r_j\rangle)(z+i\langle(\xi,\eta),r_{j+1}\rangle)}
=\frac{2z^2(Q+3z^2)}{z^2(z^2+Q)^2+p},
\]
where indices are cyclic and
\[
Q=\xi^2-\xi\eta+\eta^2,\qquad p=\xi^2\eta^2(\xi-\eta)^2.
\]
All transforms are absolutely integrable for \(z>0\). Differentiation under the integral (twice) gives the Fourier transform of \(\phi(N_H)\):
\[
G_H=\left[F_z-\frac{13}{20}\partial_zF_z+\frac16\partial_z^2F_z\right]_{z=1}
=\frac{P(Q,p)}{((1+Q)^2+p)^3},
\]
with the exact polynomial
\[
\begin{aligned}
15P(Q,p)={}&30Q^5+181Q^4+420Q^3+714Q^2+742Q+297\\
&-(9Q^3+201Q^2+859Q+747)p+(Q+36)p^2.
\end{aligned}
\]

**2. Global strict positivity of the hexagonal spectrum.** Direct expansion yields the exact identity
\[
4Q^3-27p=(\xi+\eta)^2(2\xi-\eta)^2(\xi-2\eta)^2\ge0,
\]
so \(Q\ge0\) and \(0\le p\le4Q^3/27\). The quadratic \(P(Q,\cdot)\) has positive leading coefficient \((Q+36)/15\).

When \(0\le Q\le21\), its derivative with respect to \(p\) is negative throughout the permitted interval: indeed
\[
15\partial_pP\le\frac8{27}Q^4+\frac53Q^3-201Q^2-859Q-747<0,
\]
since \(Q\le21\) implies \((\frac8{27}Q+\frac53)Q<201\). Hence its minimum is at \(p=4Q^3/27\), where exact factorization gives
\[
P\left(Q,\frac{4Q^3}{27}\right)
=\frac{(Q+3)^3}{10935}\left(16Q^4-540Q^3+4590Q^2+12015Q+8019\right)>0.
\]
Here \(16Q^2-540Q+4590=16(Q-135/8)^2+135/4>0\), so the quartic and remaining terms are positive for \(Q\ge0\).

For \(Q\ge21\), the discriminant of the quadratic \(P(Q,\cdot)\) equals
\[
-\frac{(Q+3)^2}{225}H(Q),\qquad
H(Q)=39Q^4+1192Q^3-35622Q^2-92424Q-57249.
\]
Writing \(Q=21+t\) with \(t\ge0\) gives
\[
H(21+t)=39t^4+4468t^3+142668t^2+1433184t+916416>0.
\]
Thus the discriminant is negative and the positive-leading-coefficient quadratic is positive for every real \(p\). Combining the ranges, \(G_H(\xi,\eta)>0\) at every real frequency. Fourier inversion and Bochner's theorem give positive definiteness. Strict positive definiteness follows because a nonzero finite exponential sum cannot vanish on any open frequency set, while \(G_H\) is everywhere positive.

**3. A negative square-norm Fourier band.** Substitute \(u=s+t\), \(v=s-t\) (Jacobian \(2\)). Then \(N_\infty(u,v)=|s|+|t|\), and
\[
F_z^\square(\xi,\eta)=\frac{8z^2}{[z^2+(\xi+\eta)^2][z^2+(\xi-\eta)^2]}.
\]
At \(\xi=0\) and \(\eta^2=T\), differentiation as above produces
\[
G_\square(0,\sqrt T)
=\frac{4(T-9)(T-11)}{15(T+1)^4}.
\]
This is negative for every \(9<T<11\); at \(T=10\), it is exactly \(-4/219615\). Because the Fourier transform is continuous and negative on an open set, Bochner's theorem excludes positive definiteness on the square. Finally, the sufficient \(m_2\)-mixture representation from Xu (2015) also yields a positive-definite square-radial function (via the \(\ell_1\)-radial representation under a linear change of coordinates). The square obstruction therefore rules out any such positive mixing measure.

## Verification

The accompanying `check.py` independently reconstructs the six-cone identity, the sharp hexagonal invariant identity, the differentiated numerator, endpoint factorization, quadratic discriminant, and exact negative square-frequency value in symbolic arithmetic. It also compares four direct six-cone numerical sums with the rational transform. Run `python check.py` with SymPy installed. The analytic inequalities in the proof certify the continuum of frequencies; numerical spot checks are not used for that step.

## Relationship to prior work

Xu, *Positivity and Fourier integrals over regular hexagon* (arXiv:1508.07615v1, public 2015-08-30), proves a sufficient representation of positive-definite hexagonal radial functions using \(m_2\) and explicitly leaves necessity open in the introduction and Section 3. Berens and Xu (1997) establish a representation in the \(\ell_1\)-radial setting, which in dimension two is affinely equivalent to square-radial functions; Xu (2015) explains this implication. The present example lies in the hexagonal positive cone but outside the square positive cone, so it cannot be deduced from the earlier sufficient subclass. No statement of this exact separation or this explicit polynomial profile was found in the sources inspected; this is a bounded literature comparison, not an assertion of exhaustive novelty.

## Limitations

The result is an explicit separating example and does not characterize the full positive-definite hexagonal radial cone. The 1997 source was accessible only at abstract level in the literature check; the relevant 2015 paper was read through its complete public HTML version. Other, possibly equivalent results outside the inspected literature cannot be excluded. Independent scientific audit has not been performed.

## References

1. Yuan Xu, *Positivity and Fourier integrals over regular hexagon*, arXiv:1508.07615v1, submitted 2015-08-30. https://arxiv.org/abs/1508.07615 ; complete text https://arxiv.org/html/1508.07615 .
2. H. Berens and Y. Xu, *l-1 summability of multiple Fourier integrals and positivity*, Mathematical Proceedings of the Cambridge Philosophical Society **122** (1997), 149–172. https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/issue/99DD26A2E27DE2DEF1D4C7F3EBB11FA5 .
3. W. zu Castell, *Fractional derivatives and the inverse Fourier transform of \(\ell_1\)-radial functions*, Integral Transforms and Special Functions **15** (2004), 209–223, DOI:10.1080/1065246042000210412 (abstract-level contextual comparison).
