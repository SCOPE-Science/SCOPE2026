# Reentrant pole spectra and a monotone third-order cusp for coherent qubit work

## Finding

A two-level system with pure dephasing by exponential-memory dichotomous noise admits a *reentrant* change in the pole structure underlying extractable coherent work. In a coupling interval strictly above the memoryless overdamping boundary, changing the bath-memory decay rate produces the sequence **one real pole and one conjugate pair, three real poles, one real pole and one conjugate pair**. The entire pole phase diagram is exact. The two fold curves meet at a unique third-order pole at which coherent ergotropy decays strictly monotonically for **every physical initial noise imbalance**, despite the nontrivial Jordan-order relaxation.

Write the switching rate as \(\lambda>0\), the bath memory-decay rate as \(\kappa>0\), the dephasing coupling as \(v>0\), and the real initial noise imbalance as \(a\in[-1,1]\). Set \(K=\kappa/\lambda\), \(u=v/\lambda\), and \(w=u^2\). Define the decoherence transform

\[
\widehat F_a(s)=\frac{s^2+(\kappa+iav)s+\kappa(2\lambda+iav)}{P(s)},\quad
P(s)=s^3+\kappa s^2+(2\kappa\lambda+v^2)s+\kappa v^2.
\]

For an initially equatorial pure qubit with unit energy gap, the total extractable ergotropy is \(W_a(t)=|F_a(t)|/2\). All roots of \(P\) have negative real part and remain actual poles of \(\widehat F_a\) for every real \(a\).

The complete classification for \(\kappa,v,\lambda>0\) is:

- If \(0<u\le1\), there is one finite critical \(K_-(u)>0\). Below it there is one negative real pole and one nonreal conjugate pair; at it there is a negative double pole and a distinct negative simple pole; above it all three poles are real, negative and distinct.
- If \(1<u<3\sqrt3/4\), two critical values \(0<K_-(u)<K_+(u)\) exist. The three poles are real and distinct exactly for \(K_-(u)<K<K_+(u)\); elsewhere away from the two boundary values there is one real pole and a conjugate pair. Each boundary is a double-pole exceptional point.
- If \(u=3\sqrt3/4\), the only repeated-pole point is \(K=27/4\), where \(P(s)=(s+9\lambda/4)^3\). At every other positive \(K\), there is one real pole and one conjugate pair.
- If \(u>3\sqrt3/4\), there is one real pole and one conjugate pair at every positive \(K\).

The two fold curves are specified *exactly without radical branch ambiguities* by

\[
K(t)=\frac{(t+2)^3}{(t+1)^2},\qquad
u(t)^2=\frac{t(t+2)^3}{(t+1)^4},\qquad t>0.
\]

For \(0<u<3\sqrt3/4\), \(K_-(u)\) is the value at the unique \(t\in(0,1)\) with \(u(t)=u\). For \(1<u<3\sqrt3/4\), \(K_+(u)\) is the value at the unique \(t>1\) with \(u(t)=u\). The endpoint \(u=1\) has no finite upper fold. At the unique cusp \(t=1\), the pole splits with cubic-root scaling when \(u^2\) is varied at fixed \(K=27/4\).

At the cusp, with \(T=\lambda t\), the exact coherence factor for any physical bias is

\[
F_a(t)=e^{-9T/4}\left[1+\left(\frac94+\frac{3\sqrt3}{4}ia\right)T+
\frac{27}{16}(1+i\sqrt3 a)T^2\right].
\]

It satisfies the strict derivative certificate

\[
\frac{d}{dT}|F_a(T/\lambda)|^2
=-\frac{27}{512}e^{-9T/2}T(9T+4)
\left[(1-a^2)(36T+16)+(27+81a^2)T^2\right]<0
\quad(T>0,\ |a|\le1).
\]

Thus \(W_a(t)\) is strictly decreasing at the *third-order* spectral cusp. An exceptional point here is not in itself a revival of extractable coherence. This is a statement about the displayed model and parameter point, not a general equivalence or non-equivalence theorem for all memory models.

## Assumptions and scope

The Laplace transform, physical parameters and unit-gap equatorial-qubit ergotropy above define the model. The exponential memory kernel and initialization convention are those of the cited literature; no microscopic derivation of a completely positive noise realization for every formal parameter is claimed. Time is \(t\ge0\), the Laplace variable is \(s\), the memory parameter \(\kappa\) and flipping parameter \(\lambda\) are strictly positive, the coupling \(v\) is strictly positive, and \(a\) is real with \(|a|\le1\). The phenomenological transfer-function classification is exact. Pole oscillations must not be confused with sign changes of \(d|F_a|/dt\); away from the cusp no general coherence-backflow classification is asserted.

## Proof

**1. Pole stability and visibility.** The cubic \(P\) has positive coefficients. The cubic Routh--Hurwitz condition follows from \(\kappa(2\kappa\lambda+v^2)-\kappa v^2=2\kappa^2\lambda>0\), so every root has strictly negative real part. Write \(N_0(s)=s^2+\kappa s+2\kappa\lambda\) and \(N_a(s)=N_0(s)+iav(s+\kappa)\). The identity \(P(s)=sN_0(s)+v^2(s+\kappa)\) holds. If \(P(s)=N_a(s)=0\), then \((s+\kappa)(v^2-iavs)=0\). But \(P(-\kappa)=-2\kappa^2\lambda\ne0\). When \(a=0\) there is no other root; for nonzero real \(a\) the other alternative \(s=v/(ia)\) is purely imaginary, contradicting strict stability. Thus no numerator cancellation conceals a pole, even at multiplicity transitions.

**2. Complete fold locus.** Dimensionless poles \(z=s/\lambda\) satisfy \(p(z)=z^3+Kz^2+(2K+w)z+Kw\). Since all roots are left-half-plane, at a repeated real root the roots can be written \(-x,-x,-tx\), where \(x,t>0\). Matching the elementary symmetric functions gives \(K=(t+2)x\), \(w=x^2t/(t+2)\), and \(2K+w=x^2(1+2t)\). Elimination yields \(x=(t+2)^2/(t+1)^2\), followed by the two exact fold expressions in the finding. Conversely direct substitution shows \(p(z)=(z+x)^2(z+tx)\) on this locus, so no folds have been omitted.

**3. Fold topology and discriminant.** Differentiate:

\[
\frac{d}{dt}u(t)^2=-\frac{2(t-1)(t+2)^2}{(t+1)^5},\qquad
\frac{dK(t)}{dt}=\frac{(t-1)(t+2)^2}{(t+1)^3}.
\]

Hence on \((0,1)\) the squared coupling increases from \(0\) to \(27/16\), while \(K\) decreases from \(8\) to \(27/4\). On \((1,\infty)\) the squared coupling decreases from \(27/16\) to \(1\) and \(K\) increases without bound. This proves the exact number and arrangement of repeated-root points in every coupling sector. For fixed \(w>0\) and \(K\downarrow0\), \(p(z)\to z(z^2+w)\), so its discriminant is negative. For \(K\to\infty\), the discriminant has the sign of \(1-w\) when \(w\ne1\), and is positive for sufficiently large \(K\) when \(w=1\). Since the sign changes only at the listed folds and the two generic folds are simple, the stated intervals follow from the usual real-cubic discriminant criterion. An explicit discriminant is

\[
\Delta=4[K^4(1-w)-K^3(8-10w)-K^2(12w+2w^2)-6Kw^2-w^3].
\]

At \(t=1\) the third root coincides with the double root, giving \(K=27/4\), \(w=27/16\), and the unique triple root \(-9/4\). The uniqueness follows because every triple root must be on the fold locus and requires \(t=1\).

**4. Triple pole and cubic-root splitting.** At the cusp, the nonzero numerator value at \(s=-9\lambda/4\) is \((27\lambda^2/8)(1+i\sqrt3 a)\). Taking the inverse Laplace transform gives the explicit second-degree polynomial times \(e^{-9T/4}\) above, proving an actual order-three pole. At fixed \(K=27/4\) and \(w=27/16+\varepsilon\), setting \(z=-9/4+y\) gives \(y^3+\varepsilon(y+9/2)=0\). Thus the three eigenvalue splittings satisfy \(y^3\sim-9\varepsilon/2\), with cubic-root sensitivity.

**5. Strict extractable-work monotonicity at the cusp.** The dimensionless real and imaginary factors are \(R=1+9T/4+27T^2/16\) and \(I=a\sqrt3(3T/4+27T^2/16)\). Differentiate \(e^{-9T/2}(R^2+I^2)\) and collect factors to obtain the displayed negative derivative. The final square bracket is strictly positive for every \(T>0\) and \(|a|\le1\), including \(|a|=1\) where its quadratic term remains positive. Because \(|F_a(0)|=1\) and \(|F_a(t)|>0\) for \(t\ge0\) (the real factor \(R\) is positive), \(W_a(t)=|F_a(t)|/2\) decreases strictly for positive times.

## Verification

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy. This script checks the exact cubic discriminant, the repeated-root factorization, both fold derivatives, the exact triple root, the Laplace-numerator and time-domain coefficients, the third-order differential equation, and the factorized monotonicity certificate. It also evaluates three *exact rational* discriminant witnesses at \(u=6/5\): \(K=6\) and \(K=9\) have a conjugate pair, whereas \(K=15/2\) has three distinct negative real roots. The checker independently compares 756 sampled cubic roots against discriminant signs and seven parametric boundary cases. Finite root sampling is a diagnostic only; the analytic factorization and monotonicity argument establish the stated all-parameter results.

## Relationship to prior work

Hadipour and Haseli (arXiv:2406.00411, initially released 2024-06-01) give the exact nonequilibrium dephasing transform and coherent/incoherent ergotropy as functions of \(|F_a|\), but do not provide this global pole bifurcation classification or the all-bias strict-monotonicity certificate at the triple cusp. Cai (arXiv:1910.14077; Sci. Rep. 2020) gives the equilibrium exponential-memory transform and a general inverse-Laplace root decomposition, explicitly credited here. The earlier noise equations are also related to Cai and Zheng (Phys. Rev. A 94, 042110, 2016). Lin and collaborators (arXiv:2406.18362) develop the concept of non-Markovian exceptional points in structured quantum reservoirs and demonstrate a distinct third-order example. Holst, Blasi and Khandelwal (arXiv:2610.26620, posted 2026-10-19) establish in other reaction-coordinate models that an EP does not universally mark a revival threshold; that **general qualitative non-equivalence is not claimed as new here**. The new exact result is the explicit reentrant pole geometry and the non-revival third-order point in the specified colored-telegraph coherent-work model. General discriminant methods and generic exceptional-point notions are also not claimed as new.

## Limitations

The theorem does not determine whether the coherence exhibits revivals at every point in the complex-pole regions; complex poles alone are not a backflow criterion. It does not establish complete positivity of every phenomenological memory kernel, entanglement behavior, or operational work under external control. The 2016 Phys. Rev. A source was accessible by abstract, but its full text was not obtained, leaving publication-priority uncertainty about any previously unindexed exact cusp calculation; later full-text sources were checked and credited. The 2026 quantum exceptional-point paper proves a broader qualitative non-equivalence in different models, so no general novelty claim about EPs versus backflow is made. The result is analytical and is not a claim of an experimentally measured phase diagram.

## References

1. M. Hadipour and S. Haseli, *Work extraction from quantum coherence in non-equilibrium environment*, arXiv:2406.00411 (first posted 2024-06-01); Sci. Rep. 14, 24876 (2024), https://doi.org/10.1038/s41598-024-75478-y.
2. X. Cai, *Quantum dephasing induced by non-Markovian random telegraph noise*, arXiv:1910.14077 (2019); Sci. Rep. 10, 88 (2020), https://doi.org/10.1038/s41598-019-57081-8.
3. X. Cai and Y. Zheng, *Decoherence induced by non-Markovian noise in a nonequilibrium environment*, Phys. Rev. A 94, 042110 (2016), https://doi.org/10.1103/PhysRevA.94.042110.
4. J.-D. Lin et al., *Non-Markovian Quantum Exceptional Points*, arXiv:2406.18362 (2024), https://arxiv.org/abs/2406.18362.
5. D. Holst, G. Blasi and S. Khandelwal, *Non-Markovian exceptional points and information backflow: a Heisenberg reaction-coordinate approach*, arXiv:2610.26620 (2026), https://arxiv.org/abs/2610.26620.
