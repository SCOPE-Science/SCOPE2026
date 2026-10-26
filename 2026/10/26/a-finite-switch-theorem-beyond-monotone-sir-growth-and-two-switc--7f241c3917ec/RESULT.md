# A finite-switch theorem beyond monotone SIR growth and two-switch completeness for state-dependent vaccination

## Finding

Let positive continuously differentiable rates \(\beta(S,I)\) and \(\gamma(S,I)\) define the time-optimal vaccination system
\[
\dot S=-\beta(S,I)SI-uS,\qquad
\dot I=I[\beta(S,I)S-\gamma(S,I)],\qquad 0\le u\le1.
\]
For an optimum reaching \(I=\varepsilon\) transversally, suppose \(\beta+I\partial_I\beta>0\) throughout its trajectory and \(t\mapsto G(S(t),I(t))\), where \(G=\partial_S(\beta S-\gamma)\), has at most \(q\) distinct zero instants on \((0,T)\). **Every optimum is bang-bang almost everywhere and has at most \(q+1\) switch times.** If \(G(S(T),\varepsilon)>0\), vaccination is maximal on a terminal interval. No assumption that \(G\) has one sign on the whole state space is needed.

In particular, for each of the two nonmonotone-growth parameter sets used in Section 6.5 of Park–Jang–Kim (2026), every unrestricted time-optimal vaccination control is, up to null sets, of one of the forms: constant full vaccination \(1\); a single switch \(0\to1\); or two switches \(1\to0\to1\). Thus optimizing the complete two-switch family (including its one-switch boundary) suffices for the unrestricted optimum **as a structural statement**. This does not certify numerical optimization of the switching times or prove that two switches are actually necessary.

## Assumptions and scope

The initial state satisfies \(S(0)>0\), \(I(0)>\varepsilon>0\), and \(S(0)+I(0)\le1\). Rates are strictly positive and \(C^1\) on a neighbourhood of the forward invariant population simplex, with bounded first derivatives there, and \(\beta+I\partial_I\beta>0\). The vaccination control is any measurable map into \([0,1]\). The objective is the first time \(T\) when \(I(T)=\varepsilon\). We consider an existing optimal control with \(T<\infty\) and transversal terminal exit, meaning \(\rho(S(T),\varepsilon)<0\) for \(\rho=\beta S-\gamma\). Existence under the corresponding compactness assumptions is supplied by the motivating paper and is not inferred from the switching calculation. The bound uses the actual number of distinct time zeros of \(G\), not merely its number of sign changes; in particular, it does not apply if \(G\) vanishes on an interval.

For the explicit examples take \((S_0,I_0)=(99/100,10^{-5})\), \(\varepsilon=10^{-8}\), and either
\[
\begin{aligned}
\text{B: }&\beta=48\exp(3I-3S/2),&\gamma=5+2I,\\
\text{C: }&\beta=32(1+2I)(1-67S/100),&\gamma=5+2I.
\end{aligned}
\]
Their primary mathematical subject is optimality conditions for controls governed by ordinary differential equations (MSC2020 49K15).

## Proof

**1. Normality without a globally positive growth sensitivity.** The normal Pontryagin Hamiltonian is
\[
H=1-\lambda_S S(\beta I+u)+\lambda_I I\rho.
\]
Its minimum over \(0\le u\le1\) vanishes along an optimal free-time arc and the terminal transversality condition gives \(\lambda_S(T)=0\). More generally, if the multiplier of running cost were zero, terminal transversality and \(\dot I(T)=\varepsilon\rho(S(T),\varepsilon)<0\) would force \(\lambda_I(T)=0\); uniqueness of the homogeneous adjoint system would make all multipliers zero, impossible. Normalize the nonzero cost multiplier to one. Consequently,
\[
\lambda_I(T)=-1/\dot I(T)>0.
\]
This argument needs the transversal exit, not global positivity of \(G\).

**2. One-zero lemma for the infected costate.** At any time \(t_1\) when \(\lambda_I(t_1)=0\), the minimum Hamiltonian condition says
\[
0=\min_{0\le u\le1}\{1-\lambda_S(t_1)S(t_1)(\beta I+u)\}.
\]
Hence \(\lambda_S(t_1)>0\). Differentiating the Hamiltonian with respect to the infected state gives, at such a zero,
\[
\dot\lambda_I(t_1)=\lambda_S(t_1)S(t_1)
 [\beta+I\partial_I\beta](t_1)>0.
\]
The value at a zero is well-defined despite a merely measurable optimal control: all terms involving the control cancel from this evaluation, and the surviving coefficients are continuous. Every infected-costate zero is therefore a strict crossing from negative to positive. Two different such crossings are impossible by continuity and the intermediate value theorem. Thus \(\lambda_I\) has at most one zero and is positive near \(T\).

**3. Switching-zero count.** Set \(\psi=-S\lambda_S\), so the minimum principle chooses \(u=0\) if \(\psi>0\) and \(u=1\) if \(\psi<0\). Direct differentiation cancels the measurable control:
\[
\dot\psi=(\partial_S\beta)SI\psi+\lambda_I SI G.
\]
With \(\mu(t)=\exp[-\int_0^t (\partial_S\beta)S I\,ds]>0\) and \(\Theta=\mu\psi\),
\[
\Theta'(t)=\mu(t)\lambda_I(t)S(t)I(t)G(S(t),I(t)),
\qquad \Theta(T)=0.
\]
The right side is continuous, and it vanishes at no more than \(q+1\) distinct times in \((0,T)\): at most \(q\) zeros of \(G\) and at most one zero of \(\lambda_I\). If \(\Theta\) had \(q+2\) or more distinct zeros before \(T\), Rolle's theorem applied between consecutive zeros, including the terminal zero \(T\), would produce at least \(q+2\) distinct zeros of \(\Theta'\), contradiction. Thus there are at most \(q+1\) switching zeros; \(\Theta\) cannot vanish on an interval. The control is bang-bang almost everywhere and has at most \(q+1\) switches. When \(G(S(T),\varepsilon)>0\), \(\Theta'(T)>0\), so \(\Theta(t)<0\) for all \(t<T\) sufficiently close to \(T\), giving terminal \(u=1\).

**4. The exponential and affine-power benchmark models.** In either example, \(S\) is strictly decreasing while \(S,I>0\). For B,
\[
G=48e^{3I-3S/2}(1-3S/2),\qquad S_{\mathrm{crit}}=2/3.
\]
For any \(2/3\le S\le99/100\),
\[
\beta(S,\varepsilon)S\ge32e^{-3/2}>64/11>5+2\varepsilon=\gamma(S,\varepsilon).
\]
The strict elementary estimate uses \(e<3\), implying \(e^{3/2}<3\sqrt3<11/2\). Hence a first downward exit through \(I=\varepsilon\) cannot occur with \(S\ge2/3\), where \(\dot I=I\rho>0\). Consequently every exit crosses \(S=2/3\) beforehand and \(G\) has exactly one zero along the trajectory, with positive terminal value.

For C,
\[
G=32(1+2I)(1-134S/100),\qquad S_{\mathrm{crit}}=50/67.
\]
For every \(50/67\le S\le99/100\), use \(S>1/2\), \(1-67S/100\ge33/100\), and \(1+2\varepsilon>1\) to obtain
\[
\beta(S,\varepsilon)S>32\,(1/2)(33/100)=132/25>5+2\varepsilon.
\]
Thus every first exit has \(S(T)<50/67\), and again \(G\) has exactly one zero, followed by positive \(G(T)\). For both families, \(\beta+I\partial_I\beta>0\) on the population simplex.

**5. Verify transverse exit rather than assume it for these examples.** Since \(I(t)>\varepsilon\) for \(t<T\), one has \(\rho(S(T),\varepsilon)\le0\). The preceding inequalities ensure \(G(S(T),\varepsilon)>0\). Suppose equality \(\rho(S(T),\varepsilon)=0\). Then \(\dot I(T)=0\) and \(I(t)-\varepsilon=o(T-t)\) as \(t\uparrow T\). Positivity of \(\beta,S,I\) gives \(S(t)-S(T)\ge c(T-t)\) just before \(T\) for some \(c>0\); positivity of \(G\) near the exit and boundedness of \(\partial_I\rho\) imply
\[
\rho(S(t),I(t))\ge g c(T-t)-L|I(t)-\varepsilon|>0
\]
for \(t<T\) sufficiently near \(T\). Then \(\dot I(t)>0\) immediately before the first *downward* hitting time, impossible. Hence \(\rho(S(T),\varepsilon)<0\), verifying transversality and completing the unconditional (for optimal controls) two-switch claim in B and C.

Finally, the control is terminally \(1\) and has no more than two transitions between the values \(0\) and \(1\); the only possible (nondegenerate) patterns are \(1\), \(0\to1\), and \(1\to0\to1\). These are the full admissible structural classes for the two benchmarks.

## Verification

The stand-alone `checker.py` runs direct symbolic differentiation of the two displayed \(G\) formulas and verifies the threshold arithmetic, \(e^{3/2}<11/2\), the source initial/threshold inequalities, and the positive infected-incidence derivative. The universal zero budget follows from the Pontryagin sign argument and Rolle's theorem; no finite computational sample is offered as a substitute for it. All comparisons use the stated first-hit convention and exact control range.

## Relationship to prior work

Park, Jang and Kim (2026, arXiv:2610.23095), Sections 3 and 6.5, prove a one-switch policy under \(G>0\) on the whole state simplex and numerically compare one-switch with two-switch controls outside this regime. Their own discussion says that outside \(G>0\), singular arcs are not excluded and the unrestricted optimal switching structure is not established. Their costate identity and one-zero argument are essential inputs here; this note does not claim them as new. The new steps are a finite-zero extension of that argument plus analytic endpoint transversality and the resulting complete two-switch structural classification for the specific violating benchmarks.

Bolzoni and coauthors (2017, arXiv:1706.04447) and Hynd, Ikpe and Pendleton (2021, arXiv:2008.12744) concern constant transmission and recovery rates. Their one-switch results do not imply the claimed two-switch bound for \(G\) crossing zero. Grigorieva, Khailov and Korobeinikov (2015, DOI:10.3934/proc.2015.0549; 2016, DOI:10.1051/mmnp/201611407) consider maximum-switch estimates for different fixed-terminal-time infection objectives; those works provide important historical precedent for zero counting but their identified objective and model do not directly give this first-hitting-time theorem. Full copies of those last two sources were not obtained, so an implicit prior analogue remains a bibliographic risk.

## Limitations

The general count requires finitely many **distinct temporal zeros** of \(G\) and a transversal first exit. It makes no assertion where \(G\) vanishes on intervals or oscillates infinitely often. For the two specified models the hypotheses are independently verified, but the theorem does not determine which of the three permitted profiles attains the minimum, whether the numerical two-switch candidates are globally optimal, or any bounds on clinical outcomes. The original numerical time comparisons are not promoted to proofs. No independent audit or external mathematical certification has been performed.

## References

1. Y. Park, J. Jang, Y. Kim, *Time-optimal vaccination in state-dependent SIR models: a single switch criterion and numerical examples outside its regime*, arXiv:2610.23095v1 (first public 2026-10-16), Sections 3, 6.1 and 6.5. https://arxiv.org/html/2610.23095v1
2. L. Bolzoni, E. Bonacini, C. Soresina, M. Groppi, *Time-optimal control strategies in SIR epidemic models*, arXiv:1706.04447 (2017). https://arxiv.org/pdf/1706.04447
3. R. Hynd, D. Ikpe, T. Pendleton, *An eradication time problem for the SIR model*, arXiv:2008.12744 (2020/2021). https://arxiv.org/pdf/2008.12744
4. E. Grigorieva, E. Khailov, A. Korobeinikov, *Optimal control for an epidemic in populations of varying size*, Discrete Contin. Dyn. Syst. Conf. Publ. 2015, 549–561, DOI:10.3934/proc.2015.0549.
5. E. Grigorieva, E. Khailov, A. Korobeinikov, *Optimal Control for a SIR Epidemic Model with Nonlinear Incidence Rate*, Mathematical Modelling of Natural Phenomena 11 (2016), 89–104, DOI:10.1051/mmnp/201611407.
