# Spectral-coupling growth rates for positive two-sided similarity orbits in every Schatten quasi-ideal

## Finding

Let \(H,K\) be nonzero complex Hilbert spaces. Let \(A\in\mathcal B(K)\) and \(B\in\mathcal B(H)\) be positive, self-adjoint, bounded, and boundedly invertible. Denote their projection-valued spectral measures by \(E_A,E_B\), and choose \(T\in\mathcal B(H,K)\setminus\{0\}\).

Define the **spectral-coupling support**
\[
\Gamma_{A,B}(T)=\{(a,b)\in\sigma(A)\times\sigma(B):
 E_A(U)T E_B(V)\ne0\text{ for every pair of relatively open neighborhoods }U\ni a,\ V\ni b\}.
\]
This is a nonempty compact set. Put
\[
R_+(T)=\max_{(a,b)\in\Gamma_{A,B}(T)}\frac ba,
\qquad
R_-(T)=\max_{(a,b)\in\Gamma_{A,B}(T)}\frac ab.
\]
For every \(0<p<\infty\) such that \(T\in\mathcal S_p(H,K)\), the ordinary limits exist and satisfy
\[
\boxed{\lim_{n\to\infty}\|A^{-n}TB^n\|_p^{1/n}=R_+(T)},
\qquad
\boxed{\lim_{n\to\infty}\|A^nTB^{-n}\|_p^{1/n}=R_-(T)}.
\]
The same identities hold for the operator norm and every bounded \(T\ne0\). The rates are independent of the Schatten exponent even for \(0<p<1\), where \(\|\cdot\|_p\) is a quasi-norm.

It follows that
\[
\boxed{\lim_{n\to\infty}\max\{\|A^{-n}TB^n\|_p,\|A^nTB^{-n}\|_p\}^{1/n}
=\exp\left(\max_{(a,b)\in\Gamma_{A,B}(T)}|\log(a/b)|\right).}
\]
In particular, this rate is exactly \(1\) if and only if \(AT=TB\). Thus two-sided subexponential orbit growth forces exact intertwining; positive exponential rate quantifies the largest spectral mismatch actually coupled by \(T\), rather than the full ratio of the extreme spectra of \(A,B\).

## Assumptions and scope

Both Hilbert spaces may be infinite-dimensional or nonseparable. No compactness, finite spectrum, commuting assumption, or spectral-gap hypothesis is imposed on \(A,B\). The requirement \(T\ne0\) is necessary because the root rates of the zero operator are zero and its coupling support is empty. For finite \(p\), the claim is asserted only when \(T\) belongs to the corresponding Schatten ideal. The \(p=\infty\) notation is used here only informally for the operator norm on all bounded operators; no identification of all bounded operators with compact \(\mathcal S_\infty\) is intended. Invertibility gives compact spectra contained in a common bounded interval away from zero, so all spectral ratios are finite and positive.

## Proof

**1. Compact nonempty coupling support.** Let \(X=\sigma(A)\), \(Y=\sigma(B)\). If \((a,b)\notin\Gamma_{A,B}(T)\), there are relatively open neighborhoods \(U\subseteq X\), \(V\subseteq Y\) with \(E_A(U)TE_B(V)=0\). The same zero compression holds at every point of \(U\times V\). Thus the complement of \(\Gamma_{A,B}(T)\) in compact \(X\times Y\) is open, so the coupling support is compact.

To prove nonemptiness, suppose every point of \(X\times Y\) has such a zero rectangle. Choose a finite subcover of these rectangles. A sufficiently fine finite partition of \(X\) and \(Y\) by Borel spectral intervals has every product cell contained in a zero rectangle (take a Lebesgue number for the finite open cover in the product metric). Every rectangular compression in the resulting finite spectral block decomposition of \(T\) is therefore zero, implying \(T=0\), a contradiction. Exactly the same argument gives the localization principle: whenever \(I\subseteq X\) and \(J\subseteq Y\) are relatively Borel spectral intervals with \(E_A(I)TE_B(J)\ne0\), then \((\overline I\times\overline J)\cap\Gamma_{A,B}(T)\ne\varnothing\), where closures are taken relative to \(X,Y\). Otherwise the compact product of the closures admits a finite zero-rectangle cover, and a refined finite spectral grid annihilates this block.

**2. Upper exponential bound, including quasi-norms.** Fix \(\varepsilon>0\). Partition \(X\) and \(Y\) into finitely many disjoint Borel intervals \(I_i\), \(J_j\) such that
\[
\frac{\sup I_i}{\inf I_i}\le1+\varepsilon,
\qquad
\frac{\sup J_j}{\inf J_j}\le1+\varepsilon.
\]
Discard zero spectral projections and let \(P_i=E_A(I_i)\), \(Q_j=E_B(J_j)\), \(T_{ij}=P_i TQ_j\). For every nonzero block, the localization principle supplies \((a,b)\in\Gamma_{A,B}(T)\cap(\overline{I_i}\times\overline{J_j})\). Therefore
\[
\frac{\sup J_j}{\inf I_i}
\le (1+\varepsilon)^2\frac ba\le(1+\varepsilon)^2R_+(T).
\]
The two-sided ideal inequality, valid for Schatten quasi-norms at every \(p>0\), gives
\[
\|A^{-n}T_{ij}B^n\|_p
\le\left(\frac{\sup J_j}{\inf I_i}\right)^n\|T_{ij}\|_p,
\qquad\|T_{ij}\|_p\le\|T\|_p.
\]
There are finitely many blocks. For \(p\ge1\), sum their norms; for \(0<p<1\), use \(\|\sum X_k\|_p^p\le\sum\|X_k\|_p^p\). Either way, for a constant \(C_{\varepsilon,p,T}<\infty\) independent of \(n\),
\[
\|A^{-n}TB^n\|_p\le C_{\varepsilon,p,T}\bigl((1+\varepsilon)^2R_+(T)\bigr)^n.
\]
For the operator norm, the usual triangle inequality is sufficient. Taking upper limits of the \(n\)-th roots and letting \(\varepsilon\downarrow0\) yields \(\limsup_{n\to\infty}\|A^{-n}TB^n\|_p^{1/n}\le R_+(T)\).

**3. Matching lower bound and existence of the limit.** Fix \((a,b)\in\Gamma_{A,B}(T)\). For arbitrarily small relatively open spectral intervals \(U\ni a\), \(V\ni b\), the operator \(S=E_A(U)TE_B(V)\) is nonzero. Since spectral projections commute with functional calculus,
\[
S=A^nE_A(U)\,[E_A(U)A^{-n}TB^nE_B(V)]\,E_B(V)B^{-n}.
\]
The ideal inequality and spectral bounds imply
\[
0<\|S\|_p\le
\left(\frac{\sup U}{\inf V}\right)^n\|A^{-n}TB^n\|_p,
\]
where for \(p=\infty\) all norms are operator norms. Thus
\[
\liminf_{n\to\infty}\|A^{-n}TB^n\|_p^{1/n}
\ge \frac{\inf V}{\sup U}.
\]
Letting the neighborhoods shrink to \((a,b)\) gives the lower bound \(b/a\); maximizing over compact \(\Gamma_{A,B}(T)\) gives \(R_+(T)\). This proves the first limit. Exchanging positive powers and negative powers in steps 2–3 gives the second limit with ratios \(a/b\), with no different assumptions.

**4. Sharp two-sided intertwining criterion.** The maximum of the two root limits is \(\max\{R_+(T),R_-(T)\}=\exp\max_{(a,b)\in\Gamma_{A,B}(T)}|\log(a/b)|\ge1\). If \(AT=TB\), then \(A^{-n}TB^n=A^nTB^{-n}=T\) for every \(n\), so the rate equals one. Conversely, if the rate is one, both ratios \(b/a\) and \(a/b\) are at most one on \(\Gamma_{A,B}(T)\), and hence the support lies on the diagonal \(a=b\). Every compression between strictly separated spectral intervals is therefore zero by the localization principle. For every real \(t\), use separated half-line intervals with a gap of size \(\delta>0\) and let \(\delta\downarrow0\) in the strong operator topology to obtain
\[
E_A(( -\infty,t])T=T E_B((-\infty,t]).
\]
Finally, approximate the identity function uniformly by step functions of these half-line spectral projections; the spectral theorem then gives \(AT=TB\).

## Verification

The four analytic steps above establish the claim for arbitrary dimension, every admissible Schatten exponent, and all positive invertible spectra. A standalone supplementary program, `verify.py`, constructs two finite spectral data sets, checks their exact spectral-coupling rate from the nonzero matrix entries, computes Schatten quasi-norms numerically for several exponents, and confirms the claimed limits and intertwining boundary. These finite experiments are not used as proofs of the infinite-dimensional conclusions.

For a fully explicit finite example, let \(A=\operatorname{diag}(1,2,5)\), \(B=\operatorname{diag}(3,4)\), and let \(T\) be the \(3\times2\) matrix with exactly three nonzero entries \(T_{11}=1\), \(T_{22}=2\), and \(T_{31}=3\). Then \(\Gamma_{A,B}(T)=\{(1,3),(2,4),(5,3)\}\), giving \(R_+(T)=3\) and \(R_-(T)=5/3\), in all Schatten quasi-norms.

The result is not restricted to pure point spectra: take \(K=L^2([1,2])\), \(H=L^2([3,4])\), \(A=M_x\), \(B=M_y\), and the rank-one operator \(Tf=\langle f,\mathbf1\rangle\mathbf1\). The coupling support is the whole rectangle \([1,2]\times[3,4]\), and the one-sided rates are \(4\) and \(2/3\), respectively, in every Schatten norm. This follows independently from the factorization of the rank-one singular value as \(\|x^{-n}\mathbf1\|_2\,\|y^{n}\mathbf1\|_2\) and its reverse.

## Relationship to prior work

Kittaneh, Kubrusly, and Moslehian [1, Theorems 2.3–2.4] revisit Radjabalipour's qualitative equivalence between bounded two-sided conjugation orbits of positive invertible operators and commutation, and prove spectral-gap block decoupling. That work motivates quantifying what happens when an orbit is not bounded. Its statement does not supply the individual exact exponential rates of noncommuting or nonintertwining operators.

Mustafayev [2, Sections 1–2] gives growth-class characterizations for conjugation orbits, and recalls the general local spectral-radius formula when an operator has single-valued extension property. These are substantive prior ingredients: in the ordinary operator norm, existence of a root growth rate can alternatively be approached through local spectral theory. The present asserted addition is an explicit formula entirely in terms of the nonzero spectral couplings of two potentially different positive operators, together with a direct proof that the rate remains unchanged across all Schatten quasi-ideals, including \(0<p<1\). No conclusion about that explicit formula or quasi-ideal invariance is claimed for [2] without proof.

Huang, Estaremi, and Shimi [3, Sections 1–2] examine Deddens and spectral-radius algebras of rank-one, quasi-isometric, and related operators, not the present two-operator coupling-rate formula. The classical spectral radius theorem and finite-dimensional diagonal calculations are acknowledged as elementary ingredients, not claimed as discoveries.

## Limitations

The theorem determines exponential rates, not finite-time norms, polynomial corrections, or existence of norm-attaining vectors. It requires positive, boundedly invertible operators; no extension to arbitrary invertible nonnormal implementers is claimed. In the finite Schatten regime \(T\) must belong to the stated ideal; for general bounded noncompact \(T\) only the operator-norm assertion applies. Related older local-spectral, spectral-operator and Deddens-algebra formulations may contain equivalent results; bibliographic priority is not independently certified.

## References

[1] F. Kittaneh, C. S. Kubrusly, M. S. Moslehian, *On the Commutant of Invertible Positive Operators*, arXiv:2609.21023v1, publicly submitted 2026-09-17, Sections 1–3. https://arxiv.org/abs/2609.21023

[2] H. Mustafayev, *Growth Conditions for Conjugation Orbits of Operators on Banach Spaces*, Journal of Operator Theory **74** (2015), 281–306, especially Section 2. https://doi.org/10.7900/jot.2014jun14.2059

[3] Z. Huang, Y. Estaremi, S. Shimi, *On the Deddens Algebras of a Class of Bounded Operators*, arXiv:2310.05435v1, 2023, Sections 1–2. https://arxiv.org/abs/2310.05435
