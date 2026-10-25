# An exact interior-suppression window for two-strain epidemics across mutation-selective contact layers

## Finding

Consider the two-strain, two-layer Poisson branching approximation described below. At fixed total mean contact degree, one layer transmits each strain without mutation while the other changes every successful infection to the opposite strain. The epidemic reproduction threshold is a strictly convex function of the layer allocation whenever the two mutation-preserving transmissibilities differ. There is a unique *interior* allocation minimizing that threshold if and only if the geometric mean of the strain-switching transmissibilities exceeds the arithmetic mean of the mutation-preserving transmissibilities.

Specifically, for positive transmissibilities \(a,b,c,d\), overall mean contact degree \(R>0\), and allocation \(t\in[0,1]\), the two-type reproduction matrix is
\[
 M(t)=R\begin{pmatrix}c(1-t)&at\\bt&d(1-t)\end{pmatrix}.
\]
Write \(s=(c+d)/2\), \(h=|c-d|/2\), and \(q=\sqrt{ab}\). Its Perron root is
\[
 \mathcal R(t)=R\left[s(1-t)+\sqrt{h^2(1-t)^2+q^2t^2}\right].
\]
If \(c\ne d\), then \(\mathcal R(t)\) is strictly convex on \([0,1]\). It has a unique minimizer in \((0,1)\) precisely when \(q>s\). Otherwise its unique minimum is at \(t=1\). If \(c=d\), the function is affine and hence its minimum is at an endpoint unless it is constant.

For \(c\ne d\) and \(q>s\), let \(z=\sqrt{q^2-cd}\). The minimum normalized by \(R\), and its unique location, are exactly
\[
 L_* = \frac{q(sq+hz)}{q^2+h^2},\qquad
 t_* = \frac{sL_*-cd}{q^2-cd}.
\]
In this regime \(0<t_*<1\) and \(L_*<\min\{\max(c,d),q\}\). Thus there is a nonempty interval of total mean degrees
\[
 \max\left\{\frac1{\max(c,d)},\frac1q\right\}<R<\frac1{L_*}
\]
for which **both pure-layer processes have Perron root above one**, yet a nonempty interval of mixed-layer allocations has Perron root below one. For an initially present strain that can access a supercritical class in each pure layer (as in the explicit example below), this gives supercritical–subcritical–supercritical emergence behavior along increasing \(t\).

An exact rational example has \(a=b=c=1\), \(d=1/4\), and \(R=11/10\). Both endpoints have reproduction root \(11/10>1\). The mixed process is subcritical **exactly** when
\[
 \frac{14-\sqrt{109}}{33}<t<\frac{14+\sqrt{109}}{33}.
\]
The unique minimizing allocation exists strictly inside this interval. At \(t=1/2\), the Perron root is \(11(5+\sqrt{73})/160<1\). Initially seeding strain 1 yields positive survival probability at either pure endpoint but extinction almost surely throughout the displayed interval.

## Assumptions and scope

Two independent locally tree-like Poisson contact layers have limiting mean degrees \(R(1-t)\) (layer B) and \(Rt\) (layer A). Each contact is attempted independently; an individual with strain 1 or 2 transmits along layer B with probability \(c\) or \(d\), and along layer A with probability \(a\) or \(b\), respectively. Here \(a,b,c,d\in(0,1]\). A successful B-layer transmission preserves the strain; a successful A-layer transmission switches it. The newly infected individual propagates its new strain. Contacts are independent across offspring, and each infective reproduces once in the early, susceptible-rich phase. This is a two-type Poisson Galton–Watson process and, equivalently, the locally tree-like early-emergence limit of the two-layer configuration-network construction with these Poisson degrees. Recoveries confer complete cross-immunity in the underlying finite epidemic; the exact finite-population outbreak size is not asserted here.

The total mean contact degree \(R\) is held constant when \(t\) changes, so this is redistribution between two distinct settings, not the addition of new contacts. At \(t=0\) and \(t=1\), one layer is absent; the reproduction matrix can be reducible or periodic. General Perron-root statements are about existence of supercritical types; a claim about a particular initial strain additionally requires that it reach a supercritical class. In the explicit example, the initial strain 1 satisfies this accessibility requirement at both endpoints.

The primary subject is network epidemiology (MSC2020 92D30). The statement concerns an epidemic *threshold*, not a claim that expected total cases must be U-shaped or that simultaneously applying two restrictions decreases each individual's infection probability.

## Proof

**Reduction to two types.** Poisson thinning gives a strain-1 parent independent Poisson numbers of type-1 B-layer children and type-2 A-layer children with respective means \(R(1-t)c\) and \(Rta\). A strain-2 parent similarly has type-1 and type-2 children of means \(Rtb\) and \(R(1-t)d\). Thus the mean offspring matrix, with parent type indexing rows, is exactly \(M(t)\). The standard multitype Galton–Watson threshold is its Perron root. For \(0<t<1\), irreducibility holds because \(a,b>0\). This is also the Poisson specialization of the four-type next-generation Jacobian: the Poisson excess-degree means coincide with ordinary means, making the Jacobian's two rows belonging to the same incoming strain identical and reducing its nonzero spectrum to \(M(t)\).

**Eigenvalue and strict convexity.** The off-diagonal product of \(M(t)/R\) equals \(ab t^2=q^2t^2\), while its diagonal entries are \(c(1-t)\) and \(d(1-t)\). Applying the quadratic formula gives \(\mathcal R(t)/R=f(t)\) as displayed. Set \(g(t)=h^2(1-t)^2+q^2t^2\). If \(h>0\), then \(g(t)>0\) on the closed interval, and differentiation gives the *exact identity*
\[
 f''(t)=\frac{h^2q^2}{\bigl(h^2(1-t)^2+q^2t^2\bigr)^{3/2}}>0.
\]
The endpoint derivatives are \(f'(0)=-s-h=-\max(c,d)<0\) and \(f'(1)=q-s\). Strict convexity now proves that an interior minimum exists uniquely exactly when \(q>s\); for \(q\le s\), \(f\) decreases until its unique endpoint minimum at 1. If \(h=0\), the square root is \(qt\) on \([0,1]\), so \(f(t)=c(1-t)+qt\) is affine.

**Closed minimum.** In the interior regime, let \(L=f(t)\). It satisfies
\[
 L^2-2s(1-t)L+cd(1-t)^2-q^2t^2=0.
\]
At the minimizer the equation is tangent in \(t\). Differentiating with fixed \(L\) gives \(sL=cd+(q^2-cd)t\). Substitution into the previous quadratic, followed by solving for \(L\), gives
\[
 L=\frac{q\bigl(sq\pm h\sqrt{q^2-cd}\bigr)}{q^2+h^2}.
\]
The minus-sign root corresponds to the other (non-Perron or inadmissible) tangency branch; the Perron branch, uniquely located by the signs of \(f'(0)\) and \(f'(1)\), is the plus-sign root \(L_*\). The displayed expression for \(t_*\) follows from the tangency identity. Strict convexity and the inward-pointing endpoint derivatives give \(L_*<f(0)=\max(c,d)\) and \(L_*<f(1)=q\). Therefore the stated open interval of \(R\) is nonempty. Inside it both endpoint Perron roots exceed one and the interior minimum is below one; continuity yields a nonempty subcritical interval.

**Exact extinction window.** For \(a=b=c=1\), \(d=1/4\), and \(R=11/10\), direct polynomial expansion gives
\[
 \det\bigl(I-M(t)\bigr)=\frac{-363t^2+308t-29}{400}.
\]
Its roots are \((14\pm\sqrt{109})/33\), both strictly inside \((0,1)\). On the open interval between the roots, the determinant is positive and \(M_{11}(t)<1\); the symmetric matrix \(I-M(t)\) is then positive definite, equivalently \(\rho(M(t))<1\). Outside the closed root interval (within \([0,1]\)) its determinant is negative, so the larger eigenvalue of the nonnegative symmetric matrix \(M(t)\) exceeds one. At either root the Perron root equals one. Explicitly, at \(t=0\) the dominant class is strain 1 and has mean \(11/10\), while at \(t=1\) the irreducible alternating-strain matrix has Perron root \(11/10\). Strain 1 therefore has a positive-probability nonextinction route at both endpoints. The mixed process is irreducible and subcritical exactly in the stated interval; it becomes extinct almost surely when started from either strain.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently reconstructs the rational coefficient polynomial for the example, verifies the two exact algebraic roots and the strict threshold inequality at the midpoint, and tests the closed minimizer formula and convex shape on a deterministic sample of admissible real parameters. These computational tests are secondary checks: the unrestricted theorem follows from the displayed algebra and derivatives, not from finite sampling.

## Relationship to prior work

Sood et al., *Spreading Processes with Mutations over Multi-layer Networks* (arXiv:2210.05051, first publicly posted 10 October 2022; subsequently PNAS 2023), establish the two-strain, two-layer branching-framework threshold from a four-type Jacobian, including independent layer-specific mutation matrices. Their Poisson case and Theorem 2 supply the model connection. The present statement instead gives a sharp optimization phase classification for a fixed **total** Poisson contact budget in the opposing mutation-identity/mutation-swap regime, together with a mathematically exact reentrant subcritical allocation interval. Their main case studies particularly emphasize identical mutation matrices between layers; no corresponding allocation theorem was identified in the inspected source sections.

Min et al., *Layer-switching cost and optimality in information spreading on multiplex networks* (2016), establish nonmonotone epidemic thresholds in a different path-dependent-transmissibility model where the transmission probability depends on the previous and next network layers, rather than on a pathogen strain mutated by the traversed layer. Their qualitative nonmonotonicity is relevant prior art; the current claim is **not** novelty of nonmonotonic epidemic thresholds in general. Karlin-type reduction principles establish monotonic growth reduction under a common mixing kernel applied to fixed type-specific growth. The present example deliberately falls outside that separated form: with the two layers, strain-2 reproduction changes from \(d\) to \(b\) as the mutation mechanism switches. If one imposes the separated kernel form \(a=d\), \(b=c\), then \(q=\sqrt{cd}\le(c+d)/2\), so the strict interior-suppression regime cannot occur. Sejunti, Taylor and Masuda (2024) study Parrondo-type suppression by **temporal alternation** of two SIS contact networks, distinct from the simultaneous layer-budget redistribution and biological strain transitions studied here.

## Limitations

The two-state algebra has standard matrix-theoretic components; the contribution claimed is the precise epidemiological reduction, sharp iff allocation criterion, and exact reentrant window for a concrete mutation-selective two-layer model, not a new general Perron–Frobenius theorem. These specialized results should not be mistaken for uniqueness among all models of nonmonotone transmission. Mutations fixed to identity/swap are extreme choices; general stochastic layer-dependent mutation matrices are not classified. The conclusion is for early branching emergence on independent Poisson layers, not the exact finite-size epidemic, and the optimizer concerns the Perron root, not arbitrary outbreak probability or attack rate. Publication priority may be affected by broader spectral interpolation or strain-structured branching results not identified in the inspected materials. Independent validation has not been performed.

## References

1. M. Sood, A. Sridhar, R. Eletreby, C. W. Wu, S. A. Levin, O. Yağan, H. V. Poor, *Spreading Processes with Mutations over Multi-layer Networks*, arXiv:2210.05051 (2022), doi:10.1073/pnas.2302245120 (2023).
2. B. Min, S.-H. Gwak, N. Lee, K.-I. Goh, *Layer-switching cost and optimality in information spreading on multiplex networks*, Scientific Reports 6, 21392 (2016), doi:10.1038/srep21392.
3. L. Altenberg, *Karlin Theory On Growth and Mixing Extended to Linear Differential Equations*, arXiv:1006.3147 (2010). Comparison restricted to its documented separated growth–mixing principle.
4. M. I. Sejunti, D. Taylor, N. Masuda, *A Parrondo paradox in susceptible-infectious-susceptible dynamics over periodic temporal networks*, arXiv:2406.16787 (2024). Temporal-model contrast.
