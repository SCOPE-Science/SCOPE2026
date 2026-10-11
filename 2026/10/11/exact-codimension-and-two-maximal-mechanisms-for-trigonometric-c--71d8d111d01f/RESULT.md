# Exact codimension and two maximal mechanisms for trigonometric composition centers

## Finding

For an integer \(n\geq1\), write \(V_n\) for the \(4n\)-dimensional real vector space of pairs \((a,b)\) of zero-mean trigonometric polynomials whose harmonic degrees are at most \(n\). Let \(C_n\subset V_n\) consist of pairs admitting **one common trigonometric composition factor**:
\[
a(t)=P(h(t))h'(t),\qquad b(t)=Q(h(t))h'(t),
\]
where \(h\) is a real trigonometric polynomial and \(P,Q\) are real ordinary polynomials. Include the zero pair.

Define two distinguished subsets of \(V_n\): the **proportional branch** \(L_n\), consisting of linearly dependent pairs \((a,b)\) in the real vector space of trigonometric polynomials, and the **common-reflection branch** \(R_n\), consisting of pairs for which a single \(\tau\in\mathbb R/(2\pi\mathbb Z)\) makes both \(a(\tau+s)\) and \(b(\tau+s)\) odd functions of \(s\).

**Theorem.** For every \(n\geq1\), the semialgebraic dimension and codimension of \(C_n\) are exactly
\[
\dim C_n=2n+1,\qquad \operatorname{codim}_{V_n} C_n=2n-1.
\]
For every \(n\geq2\), \(L_n\) and \(R_n\) are distinct, closed, semialgebraic subsets of \(C_n\), each of dimension \(2n+1\); **they exhaust its top-dimensional part**. Their intersection has dimension \(n+2\). The union of all compositions with a common factor of harmonic degree strictly between \(1\) and \(n\) has dimension at most \(2n-1\). In particular, for the first genuinely two-harmonic case,
\[
\boxed{C_2=L_2\cup R_2.}
\]
For \(n=1\), the two mechanisms coincide, and \(C_1=L_1=R_1\).

Equivalently, for zero-mean coefficients of harmonic degree at most two, the composition condition holds **exactly** when either \(a,b\) are proportional or they share an axis of odd time-reflection. Thus, as soon as the second harmonic is allowed, nonproportional global-center-producing coefficients form a second maximal-dimensional family.

## Assumptions and scope

A trigonometric polynomial of harmonic degree at most \(n\) has a unique real Fourier expansion
\[
f(t)=f_0+\sum_{k=1}^{n}(u_k\cos kt+v_k\sin kt).
\]
The mean-zero condition is \(f_0=0\). Dimension here means real semialgebraic dimension; the bound concerns finite Fourier coefficients, not a functional-analytic topology. The statement concerns **composition centers**. Every \((a,b)\in C_n\) gives a globally periodic equation \(x'=a(t)|x|+b(t)\). The converse for arbitrary global centers is not asserted: Bravo and Trinidad-Forte prove it under their additional two-zero Hypothesis 1.

The source first appeared publicly as arXiv:2503.03247v1 on 2025-03-05, within the relevant recent literature; the subsequent open-access journal article has primary MSC 34C25. Its composition criterion is used as motivation and terminology, not claimed here as new.

## Proof

**1. The factor-degree bound.** Fix a nonzero pair in \(C_n\), with a nonconstant factor \(h\) of harmonic degree \(d\). Suppose a nonzero ordinary polynomial \(F\) has degree \(r\), with leading coefficient nonzero. The highest positive Laurent term of \(h(t)\) has Fourier frequency \(d\) and nonzero coefficient, while differentiation multiplies that coefficient by \(id\). Consequently, \(F(h(t))h'(t)\) has nonzero Fourier coefficient at frequency \((r+1)d\); lower powers of \(h\) cannot cancel it. Its harmonic degree is exactly \((r+1)d\). Therefore, with \(m=\lfloor n/d\rfloor\), the degrees of both \(P,Q\), unless zero, are at most \(m-1\); also \(1\leq d\leq n\).

**2. Uniform dimension bound.** There are \(2d+1\) real coefficients in \(h\), including its mean. An affine change \(h\mapsto c h+e\) with \(c\ne0\) is absorbed by changing \(P,Q\). We can therefore normalize the mean of \(h\) to zero and the Euclidean norm of its leading sine/cosine coefficient pair to one. This leaves a smooth parameter family of dimension \(2d-1\); the two outer polynomials contribute at most \(2m\) coefficients. Their image has semialgebraic dimension at most
\[
D_d=2d+2\lfloor n/d\rfloor-1.
\]
All these images are semialgebraic, because the Fourier coefficient maps are polynomial in the parameters and the normalization equations are semialgebraic; projection preserves semialgebraicity.

For \(2\leq d\leq n-1\), the elementary inequality
\[
d+\lfloor n/d\rfloor\leq n
\]
holds. To see it, write \(n=dq+r\) with \(q\geq1\) and \(0\leq r<d\). If \(q=1\), then \(r\geq1\) since \(d<n\); if \(q\geq2\), then \((d-1)(q-1)+r-1\geq0\). In either case \(n-d-q\geq0\). Thus intermediate-degree factors contribute dimension at most \(2n-1\).

**3. The two maximal families.** If \(d=n\), then \(m=1\) and \(P,Q\) are constants: \((a,b)\) is proportional. Conversely every proportional mean-zero pair has this representation, because any mean-zero trigonometric polynomial is the derivative of a periodic trigonometric polynomial. (If one of the coefficients is zero, choose the other as the common derivative.) Hence the degree-\(n\) branch, combined with its lower-degree limits, is \(L_n\).

If \(d=1\), write \(h(t)=c+r\cos(t-\tau)\) with \(r>0\). Then \(P(h)h'\) and \(Q(h)h'\) are simultaneously odd about \(t=\tau\). Conversely any two such odd trigonometric polynomials can be written as
\[
\sum_{k=1}^{n}A_k\sin(k(t-\tau)),\qquad
\sum_{k=1}^{n}B_k\sin(k(t-\tau)).
\]
The Chebyshev identity \(\sin(k s)=\sin(s)U_{k-1}(\cos s)\) expresses both as polynomial multiples of \(h'(t)\), with \(h(t)=\cos(t-\tau)\). Thus the degree-one branch is precisely \(R_n\).

For \(L_n\), choosing a nonzero \(a\) freely and setting \(b=\lambda a\) shows dimension \(2n+1\). For \(R_n\), the common phase plus the \(2n\) sine coefficients gives an upper bound of \(2n+1\). It is attained: at \(a(t)=\sin t\), \(b(t)=0\), changing the phase produces a first-harmonic cosine perturbation independent of all \(2n\) sine-coefficient perturbations. Thus \(\dim R_n=2n+1\). Both sets are closed: for \(L_n\), the rank-one equations are polynomial; for \(R_n\), any convergent sequence of pairs has a convergent subsequence of phases on the compact circle, after which oddness passes to the limit. They are semialgebraic by their Fourier parametrizations.

For \(n\geq2\), \(a=\sin t, b=\sin2t\) belongs to \(R_n\setminus L_n\). Taking \(a=\sin t+\cos2t, b=2a\) gives a pair in \(L_n\setminus R_n\): its nonzero first harmonic fixes the possible oddness axis modulo \(\pi\), but its second cosine harmonic is then even. Hence the two maximal branches are distinct. Their intersection consists of proportional pairs whose common nonzero function is odd about some phase; its generic parameter count is \(n\) sine coefficients plus one phase plus one relative proportionality parameter, giving dimension \(n+2\). A nonzero trigonometric polynomial has only finitely many oddness axes in a period, so there is no continuous excess in this count.

The intermediate-degree images have dimension at most \(2n-1\), so no other subset of the composition-center locus can have top dimension \(2n+1\). This proves the dimension, codimension, and two maximal mechanisms. For \(n=2\) the possible factor degrees are only \(1\) and \(2\), yielding the exact union. For \(n=1\), every pair on the degree-one reflection branch is proportional, as both are multiples of the same shifted sine.

**4. A finite coefficient test at harmonic cutoff two.** Write the Fourier coefficients in complex form \(z_{f,k}=u_{f,k}-iv_{f,k}\), where \(f=a,b\), \(k=1,2\), and \(f(t)=\operatorname{Re}(z_{f,1}e^{it}+z_{f,2}e^{2it})\). First check proportionality of the two four-component real Fourier coefficient vectors. If it fails, select a nonzero first-harmonic complex coefficient \(u\) from either \(a\) or \(b\). The pair belongs to \(R_2\) precisely when the other first-harmonic coefficient \(w\) and both second-harmonic coefficients satisfy
\[
\operatorname{Im}(w\overline u)=0,\quad
\operatorname{Re}(z_{a,2}\overline u^{\,2})=0,\quad
\operatorname{Re}(z_{b,2}\overline u^{\,2})=0.
\]
If both first harmonics vanish, the remaining condition is \(\operatorname{Im}(z_{a,2}\overline {z_{b,2}})=0\). These are polynomial equalities in real Fourier coordinates. They are exact because choosing a phase which makes \(ue^{i\tau}\) purely imaginary forces the same property for \(w e^{i\tau}\) and precisely the displayed real-part conditions for both second harmonics. This completes an explicit decision procedure for \(C_2\), including degenerate coefficients.

**5. Dynamical connection.** Given the composition factor, solve the nonautonomous equation in its factor variable: for \(s\) in the compact range of \(h\), let \(Y'(s)=P(s)|Y(s)|+Q(s)\), with \(Y(h(0))=x(0)\). Global Lipschitz dependence in \(Y\) on this compact \(s\)-interval gives a unique solution there. Then \(x(t)=Y(h(t))\) solves the original equation, and \(h(t+2\pi)=h(t)\) makes every solution \(2\pi\)-periodic. This sufficiency is established in the motivating work; it is included only to explain why the algebraic locus matters dynamically.

## Verification

The analytic proof above establishes the unrestricted integer-\(n\) statement. The supplementary `CHECKER.py` uses only Python's standard library, executes rational Fourier phase identities and checks explicit independent tangent directions on both two-harmonic branches. It also verifies finite samples of the elementary integer degree inequality. Those finite checks are not asserted to prove the general dimension theorem; the dimension bound, semialgebraic argument, and Fourier-leading-term lemma are proved above.

## Relationship to prior work

Bravo and Trinidad-Forte's arXiv:2503.03247v1 (public 2025-03-05), later published in *Qualitative Theory of Dynamical Systems* 25 (2026), article 26, characterizes all global centers under a specific two-simple-zero hypothesis via the composition condition. That paper gives the representation, not the Fourier-truncated semialgebraic dimension, two maximal mechanisms, exact two-harmonic decomposition, or coefficient decision test.

Bravo, Fernández and Ojeda (2024) prove a proportionality characterization at harmonic degree one. The present first nontrivial cutoff \(n=2\) distinguishes a second family not possible at \(n=1\). Pakovich (2017, Theorem 1.1) classifies equalities between different polynomial compositions of trigonometric factors; Briskin–Pakovich–Yomdin (2016, Theorem 1.1) bounds the dimensions of composition sets for polynomial Abel equations with a fixed polynomial coefficient. Neither statement gives the dimension or two maximal branches of the present *paired real trigonometric* coefficient locus. Earlier trigonometric Abel work studies related composition conditions, but not necessarily the same piecewise-linear dynamical equation.

## Limitations

This theorem does not classify **all** global centers outside the additional hypothesis of Bravo and Trinidad-Forte, and it does not assert that the lower-dimensional intermediate-degree compositions are absent for \(n\geq3\). It does not classify singularities of the whole composition locus or supply a global list of its lower-dimensional irreducible components. Semialgebraic dimension is not the measure of dynamical stability under perturbation. An older trigonometric-Abel composition paper was accessible only at abstract level; equivalent formulations under different coordinates remain possible. Independent validation has not been performed.

## References

1. J. L. Bravo and R. Trinidad-Forte, *Global Centers in Piecewise Linear Equations in the Cylinder*, arXiv:2503.03247v1 (first public 2025-03-05); *Qualitative Theory of Dynamical Systems* 25 (2026), article 26, doi:10.1007/s12346-025-01425-5. Open full text: https://link.springer.com/article/10.1007/s12346-025-01425-5.
2. J. L. Bravo, M. Fernández and I. Ojeda, *Hilbert Number for a Family of Piecewise Nonautonomous Equations*, *Qualitative Theory of Dynamical Systems* 23 (2024), article 119, doi:10.1007/s12346-023-00922-9. Open full text: https://link.springer.com/article/10.1007/s12346-023-00922-9.
3. J. Giné, M. Grau and X. Santallusia, *Composition Conditions in the Trigonometric Abel Equation*, *Journal of Applied Analysis & Computation* 3 (2013), 133–144, doi:10.11948/2013011.
4. F. Pakovich, *On Decompositions of Trigonometric Polynomials*, *Israel Journal of Mathematics* 217 (2017), 337–353; arXiv:1307.5594. Open author copy: https://pakovich.github.io/detri.pdf.
5. M. Briskin, F. Pakovich and Y. Yomdin, *Algebraic Geometry of the Center-Focus Problem for Abel Differential Equations*, *Ergodic Theory and Dynamical Systems* 36 (2016), 714–744, doi:10.1017/etds.2014.94. Open author copy: https://pakovich.github.io/alab.pdf.
