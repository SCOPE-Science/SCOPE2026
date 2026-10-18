# Exact maximal norms of projection-relaxation Markov semigroups

## Finding

Let \((\Omega,\mathcal F,\mu)\) be an arbitrary probability space, let \(\mathcal G\subseteq\mathcal F\) be a sub-\(\sigma\)-algebra, and let \(P=\mathbb E[\,\cdot\mid\mathcal G]\) act on real or complex \(L^2(\mu)\). Consider the positive, self-adjoint, Markov \(C_0\)-semigroup
\[
T_t=P+e^{-t}(I-P),\qquad t\ge0,
\]
and its pointwise maximal operator \(\mathcal M_P f=\operatorname{ess\,sup}_{t\ge0}|T_tf|\). For \(0\le b\le1\), put
\[
\Lambda(b)=\frac{1+b+\sqrt{(1-b)(1+3b)}}2.
\]
Then the **exact norm** is
\[
\boxed{\|\mathcal M_P\|_{L^2\to L^2}^2
=\sup_{E\in\mathcal F}\operatorname{ess\,sup}_{\omega\in\Omega}
\Lambda\bigl(\mathbb E[\mathbf1_E\mid\mathcal G](\omega)\bigr).}
\tag{1}
\]
In particular, \(\|\mathcal M_P\|\le2/\sqrt3\), with the coefficient sharp over all probability spaces and all conditional expectations. The equality criterion is that \(2/3\) lie in the closure of the union of the essential ranges of \(\mathbb E[\mathbf1_E\mid\mathcal G]\), as \(E\) varies; equivalently, for every \(\varepsilon>0\) some event \(E\) has a set of positive measure where \(|\mathbb E[\mathbf1_E\mid\mathcal G]-2/3|<\varepsilon\).

When \(P f=\int_\Omega f\,d\mu\) projects onto constants, (1) reduces to a **complete subset-mass formula**
\[
\boxed{\|\mathcal M_P\|^2=\max_{E\in\mathcal F}\Lambda(\mu(E)).}\tag{2}
\]
The maximum exists. Here the sharp universal coefficient is attained exactly when some measurable subset has mass \(2/3\). Such a subset \(E\) yields an extremizing function \(f=c(\mathbf1_{E^c}+\tfrac14\mathbf1_E)\) for every nonzero complex scalar \(c\). For every fixed nontrivial event mass \(b\in(0,1)\), a corresponding exact optimizer of its linearization is \(f=c(\mathbf1_{E^c}+r_b\mathbf1_E)\), where
\[
r_b=\frac{b(1-b)}{\Lambda(b)-b^2}.
\]

For \(n\ge2\) equip \(n\) points with uniform mass \(1/n\). With \(k_n\) the unique integer nearest to \(2n/3\),
\[
\boxed{\|\mathcal M_P\|^2=\Lambda(k_n/n),\qquad
k_n=\begin{cases}2m,&n=3m,\\2m+1,&n=3m+1,\\2m+1,&n=3m+2.\end{cases}}
\tag{3}
\]
Thus \(\|\mathcal M_P\|=2/\sqrt3\) precisely for \(3\mid n\); otherwise the inequality is strict and
\[
\frac43-\|\mathcal M_P\|^2=\frac{1}{9n^2}+O(n^{-3})\quad(n\to\infty,\ 3\nmid n).
\tag{4}
\]
All statements also apply, with the same maximal operator and exact constants, to \(\sup_{k\ge0}|R_\rho^k f|\), where \(R_\rho=P+\rho(I-P)\) and \(0\le\rho<1\).

## Assumptions and scope

The probability space is arbitrary, without separability or nonatomicity assumptions. Conditional expectations are defined in the usual \(L^2\) sense. The pointwise maximal operator uses the almost-everywhere supremum; a countable dense time set gives the same function. Scalar functions may be real or complex. Equation (1) concerns the maximal norm, not the linear norm of \(T_t\), which equals one. For the finite-atom statement the measure is uniform; for nonuniform atoms use (2). The discrete-time assertion requires \(\rho<1\), not \(\rho=1\).

## Proof

**Endpoint reduction.** For each \(f\) and almost every \(\omega\),
\[
T_tf(\omega)=e^{-t}f(\omega)+(1-e^{-t})Pf(\omega).
\]
Convexity of complex modulus on a line segment, together with the limits \(t\downarrow0\) and \(t\uparrow\infty\), gives
\[
\mathcal M_Pf=\max\{|f|,|Pf|\}\quad\text{a.e.}\tag{5}
\]
The same argument applies to \(R_\rho^k=P+\rho^k(I-P)\), as \(k\to\infty\) and at \(k=0\).

**Exact linearization.** For each event \(E\in\mathcal F\), put \(A_Ef=\mathbf1_{E^c}f+\mathbf1_E Pf\). Pointwise, \(|A_Ef|\le\mathcal M_Pf\); taking \(E_f=\{|Pf|\ge|f|\}\) gives equality. Consequently,
\[
\|\mathcal M_P\|_{2\to2}=\sup_{E\in\mathcal F}\|A_E\|_{2\to2}.\tag{6}
\]
This identity holds for complex \(f\) without a positivity reduction.

**Conditional two-dimensional calculation.** Fix \(E\), and set \(b=\mathbb E[\mathbf1_E\mid\mathcal G]\), \(a=1-b\). For any \(f\), define the nonnegative \(\mathcal G\)-measurable quantities
\[
u^2=\mathbb E[\mathbf1_{E^c}|f|^2\mid\mathcal G],\qquad
v^2=\mathbb E[\mathbf1_E|f|^2\mid\mathcal G].
\]
Conditional Cauchy--Schwarz on the two pieces yields \(|Pf|\le\sqrt a\,u+\sqrt b\,v\). Hence
\[
\mathbb E[|A_E f|^2\mid\mathcal G]
=u^2+b|Pf|^2
\le u^2+(\sqrt{ab}\,u+bv)^2
=\left\|\begin{pmatrix}1&0\\\sqrt{ab}&b\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}\right\|_2^2.
\]
The displayed real matrix has squared singular values equal to the roots of \(z^2-(1+b)z+b^2=0\). Its largest squared singular value is \(\Lambda(b)\). Therefore
\[
\|A_E\|_{2\to2}^2\le\operatorname{ess\,sup}\Lambda(b).\tag{7}
\]
This is sharp. On \(0<b<1\), define \(r_b=b(1-b)/(\Lambda(b)-b^2)\), a bounded measurable \(\mathcal G\)-function there. For any \(H\in\mathcal G\) contained in \(\{0<b<1\}\), take \(f=\mathbf1_H(\mathbf1_{E^c}+r_b\mathbf1_E)\). The two conditional Cauchy--Schwarz steps are equalities, and the vector of conditional two-piece energies is a top right singular vector of the displayed matrix. Thus
\[
\mathbb E[|A_Ef|^2\mid\mathcal G]=\Lambda(b)\,\mathbb E[|f|^2\mid\mathcal G]\quad\text{on }H\cap\{0<b<1\}.
\]
Choosing \(H\) where \(\Lambda(b)\) is within any prescribed positive tolerance of its essential supremum proves the reverse inequality whenever this supremum exceeds one. Otherwise both sides equal one, because every \(A_E\) fixes every nonzero \(\mathcal G\)-measurable function. Combining with (6) establishes (1).

**Universal constant.** Direct differentiation gives, for \(0<b<1\),
\[
\Lambda''(b)=-\frac2{((1-b)(1+3b))^{3/2}}<0,
\]
with \(\Lambda'(2/3)=0\) and \(\Lambda(2/3)=4/3\). Therefore \(\Lambda\) has the unique global maximizer \(b=2/3\), proving the bound and the stated equality criterion from (1).

**Trivial conditioning and finite atoms.** For projection onto constants, \(b=\mu(E)\), so (2) follows. The set of achievable probabilities is closed: its atomic part is a compact set of subsums of a summable, at most countable atom-mass sequence; its nonatomic part contributes the whole interval from zero to the nonatomic mass, and their Minkowski sum is compact. The formula for \(r_b\) gives \(r_{2/3}=1/4\).

For uniform \(n\) points, \(\mu(E)=k/n\). Strict unimodality first restricts maximizing \(k\) to \(\lfloor2n/3\rfloor\) or \(\lceil2n/3\rceil\). To resolve the asymmetric sides, put \(\delta=b-2/3\) and observe the exact deficit identity
\[
\frac43-\Lambda(b)=\frac{2\delta^2}{D(\delta)},\qquad
D(\delta)=1-\delta+\sqrt{1-2\delta-3\delta^2}.
\]
On \(-2/3\le\delta\le1/3\), \(D\) decreases from \(8/3\) to \(2/3\) (differentiate and square the sole potentially positive term). The candidate offsets for \(n\not\equiv0\pmod3\) are \((-2/(3n),1/(3n))\) or \((-1/(3n),2/(3n))\). In both cases the candidate with the smaller absolute offset has strictly smaller deficit: for the first pair use \(D(-2/(3n))<4D(1/(3n))\); for the second use \(D(-1/(3n))>D(2/(3n))\). This proves (3), including uniqueness. Taylor expansion at \(b=2/3\), where \(\Lambda'(2/3)=0\) and \(\Lambda''(2/3)=-2\), yields (4).

## Verification

All identities can be checked using the standalone `verify.py`, which computes finite Markov-chain maximal quotients and checks the singular-value polynomial and finite-atom formulas, including the \(n\bmod3\) transition. The infinite-dimensional and arbitrary conditional-expectation claims follow from the conditional Cauchy--Schwarz argument, not from finite numerical testing. The proof requires no external computational certificate.

## Relationship to prior work

Palai and Ray, *Maximal Ergodic Theorems for Operators with Finite Peripheral Spectrum* (2026), establish broad boundedness of power maximal operators for positive contractions; their Theorem 1.1 and classical operator Theorem 3.30 give existence of a constant but do not determine (1)--(4) for the projection-relaxation model. Ciccone, Hormozi, Madrid, Niksiński and Wróbel, *On \(L^p\) norms of maximal operators* (2026), give the general \(L^2\) semigroup maximal bound \(2\), and identify when the bound is attained under a local compactness hypothesis on nonatomic spaces. The present semigroup generally fails that hypothesis on nonatomic spaces because \(T_t\) contains \(e^{-t}I\); on finite atomic spaces their nonatomic hypothesis fails. Neither result asserts the conditional event-mass formula or its finite-atom arithmetic. Earlier Stein--Doob maximal theory supplies broader inequalities and does not by itself give the sharp values here.

## Limitations

The exact formula concerns the special projection-relaxation semigroup and powers of its lazy Markov step, not all positive symmetric Markov semigroups or all Ritt operators. The universal upper bound is sharp over the class but need not be attained for a particular probability space; the conditional event-mass spectrum determines attainment. The formula is for the \(L^2\) operator norm only. The inequality does not claim improvement of general sharp Stein--Doob constants. A priority risk remains that an older formulation of the two-step martingale norm or a conditional-expectation Bellman inequality could already imply the exact constants; no publication-priority certification is asserted.

## References

1. S. Palai and S. K. Ray, *Maximal Ergodic Theorems for Operators with Finite Peripheral Spectrum*, arXiv:2606.16506, initially posted 15 June 2026. https://arxiv.org/abs/2606.16506
2. P. Ciccone, B. Hormozi, J. Madrid, M. Niksiński and B. Wróbel, *On \(L^p\) norms of maximal operators*, arXiv:2610.10247v1, initially posted 7 October 2026. https://arxiv.org/html/2610.10247v1
3. Q. Xu, *\(H^\infty\) functional calculus and maximal inequalities for semigroups of contractions on vector-valued \(L_p\)-spaces*, arXiv:1402.2344 (2014). https://arxiv.org/abs/1402.2344
