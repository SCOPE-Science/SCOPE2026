# A marginal entropy spike for weakly blocked ANNNI spin chains

## Finding

For the one-dimensional periodic axial next-nearest-neighbor Ising chain, the exponential number of configurations on which **no individual spin flip strictly lowers the energy** has three exactly computable branches. A large and physically meaningful spike occurs at the marginal coupling where the second-neighbor antiferromagnetic interaction equals the first-neighbor ferromagnetic interaction.

For each integer \(n\ge5\), let \(B_n(\kappa)\) count labelled spin configurations that are weakly stable against every individual flip, and define the entropy density \(s(\kappa)=\lim_{n\to\infty}n^{-1}\log B_n(\kappa)\). The complete classification is

\[
s(\kappa)=\begin{cases}
\log((1+\sqrt5)/2),&0<\kappa<1,\\
\log\lambda_{=},&\kappa=1,\\
\log\lambda_{>},&\kappa>1,
\end{cases}
\]
where \(\lambda_{=}\) is the unique positive Perron root of
\[
Q_{=}(t)=t^5-t^3-2t^2-t-1,
\]
and \(\lambda_{>}\) is the Perron root of
\[
Q_{>}(t)=t^7-t^5-2t^4-t^3+t+1.
\]
Their values are \(\lambda_{=}\approx1.6663019373129335\) and \(\lambda_{>}\approx1.5551872263767017\). In particular
\[
\boxed{\ s(1)>s(\kappa)\ (0<\kappa<1),\qquad s(1)>s(\kappa)\ (\kappa>1)\ },
\]
with rigorous coarse bounds \(1.665<\lambda_{=}<1.668\), \(1.618< (1+\sqrt5)/2<1.619\), and \(1.554<\lambda_{>}<1.557\). The branch for \(0<\kappa<1\) is an established domain-length classification and is included solely as a baseline. The new substantive contribution is the exact marginal and strong-frustration entropy laws, together with their sharp comparison.

## Assumptions and scope

Sites are labelled by \(i\in\mathbb Z/n\mathbb Z\), spins are \(\sigma_i\in\{-1,+1\}\), \(J>0\), and \(\kappa>0\). The Hamiltonian is
\[
H_\kappa(\sigma)=-J\sum_{i=0}^{n-1}\sigma_i\sigma_{i+1}+J\kappa\sum_{i=0}^{n-1}\sigma_i\sigma_{i+2}.
\]
All indices are cyclic. A configuration is *weakly one-spin blocked* when for each site \(i\), the energy difference between the configuration with \(\sigma_i\) reversed and the original configuration is nonnegative. Neutral flips are therefore permitted in the definition of weak stability; the configurations need not be absorbing for a dynamics accepting zero-cost flips. No assumption of random initial conditions or a dynamical stationary distribution is made.

For \(n\ge5\) define \(16\) states as ordered quadruples \(w=(a,b,c,d)\in\{-1,+1\}^4\). Set the transfer matrix \(T_\kappa\) by
\[
(T_\kappa)_{(a,b,c,d),(b,c,d,e)}=\mathbf1\{\,c(b+d-\kappa(a+e))\ge0\,\},
\]
and all other entries equal to zero. Here identical state pairs are counted once. The exact finite-ring count is \(B_n(\kappa)=\operatorname{tr}(T_\kappa^n)\), with the same matrix for every coupling in each of the three stated regimes.

## Proof

**1. Local energy condition and exact cyclic coding.** Reversing \(\sigma_i\) changes precisely its two nearest-neighbor and two next-nearest-neighbor interactions. The exact difference is
\[
\Delta_iH=2J\sigma_i\bigl(\sigma_{i-1}+\sigma_{i+1}-\kappa(\sigma_{i-2}+\sigma_{i+2})\bigr).
\]
Thus weak one-spin stability is equivalent to the indicated five-symbol condition at every site. Successive quadruples overlap in three symbols. A labelled periodic spin string of length at least five determines exactly one closed walk of length \(n\) in this de Bruijn graph with its prescribed start-site state, and conversely any such walk determines exactly one labelled periodic string. Hence the trace identity is exact, including for nonprimitive \(n\)-periodic words.

**2. Three symbolic characteristic polynomials.** Since \(a+e\) and \(b+d\) range over \(\{-2,0,2\}\), the indicator changes only at \(\kappa=1\) within the positive coupling axis. Direct determinant expansion of the explicitly given \(16\times16\) integer matrices yields, writing \(\chi_\kappa(t)=\det(tI-T_\kappa)\),
\[
\begin{aligned}
0<\kappa<1:\quad &\chi_\kappa(t)=t^{12}(t^2-t-1)(t^2-t+1),\\
\kappa=1:\quad &\chi_1(t)=t^4(t-1)^2(t^5+t^3+t+1)(t^5-t^3-2t^2-t-1),\\
\kappa>1:\quad &\chi_\kappa(t)=t^2(t^7+t^5+t^3-t-1)(t^7-t^5-2t^4-t^3+t+1).
\end{aligned}
\]
These are polynomial identities over the integers, not numerical fits. They imply exact algebraic formulas for every \(B_n(\kappa)\) as the sum of the \(n\)-th powers of the roots of the displayed factors, counted with algebraic multiplicity (zero roots contribute nothing). For example, the weak-coupling formula reduces to \(\varphi^n+(-\varphi^{-1})^n+2\cos(n\pi/3)\) for \(\varphi=(1+\sqrt5)/2\).

**3. Identifying the unique exponential rate.** The directed graph of each \(T_\kappa\) has a unique cyclic strongly connected component of maximum size: ten states in the weak-coupling regime and fourteen states in each of the other two regimes. Every remaining component is acyclic. Each maximal cyclic component is irreducible and aperiodic (the greatest common divisor of its directed cycle lengths is one), so its adjacency matrix is primitive. Perron–Frobenius theory gives the existence of the entropy limit and identifies its exponential as the unique dominant positive eigenvalue. The characteristic polynomials in Step 2 identify the stated algebraic roots.

For additional exact control that avoids numerical eigenvalue selection, enumerate quadruples lexicographically with \(-1<+1\). In both the marginal and strong-frustration regimes, the nontrivial component has indices \((0,1,2,3,4,6,7,8,9,11,12,13,14,15)\). At \(\kappa=1\), the positive integer vector
\[
(9006898,6001313,2757411,10000000,4594679,7656122,9006898,9006898,7656122,4594679,10000000,2757411,6001313,9006898)
\]
satisfies \(1665v_i<1000(T_1v)_i<1668v_i\) throughout the component. For \(\kappa>1\), the vector
\[
(4134611,6430094,3621368,10000000,5631906,8758668,6793204,6793204,8758668,5631906,10000000,3621368,6430094,4134611)
\]
satisfies \(1554v_i<1000(T_\kappa v)_i<1557v_i\). The matrix–vector inequalities are exact integer checks and imply the strict Perron bounds by the Collatz–Wielandt inequalities. The known golden-ratio value is strictly between the two stated rational ranges. Hence the marginal entropy strictly exceeds both neighboring regimes.

**4. Physical source of the spike.** At \(\kappa=1\), precisely two additional five-spin patterns become allowed relative to the \(0<\kappa<1\) regime (an isolated spin opposite four neighboring spins); relative to \(\kappa>1\), two all-aligned patterns become allowed. These are neutral-energy motifs at the marginal coupling, not energy-reducing moves. Permitting both kinds of motifs raises the exponential count above the count on either strict side. The theorem concerns weak local minima and does not assert that these motifs persist under neutral-spin-flip dynamics.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy. The supplied standalone script constructs all three matrices directly from the five-spin inequality, verifies the symbolic characteristic polynomials, identifies the stated strongly connected components, checks exact integer Perron inequalities and aperiodicity, and compares the trace count with an independent enumeration using full Hamiltonian recomputation before and after each possible flip for every \(n=5,6,\ldots,12\) and all three coupling regimes. This covers \(24{,}480\) labelled configurations. All checks passed. The finite brute force is a regression test, not the proof of the all-size statement; that proof is Steps 1–3.

## Relationship to prior work

Redner and Krapivsky (1998) analyze zero-temperature Glauber coarsening in the same chain, including the special dynamics at \(\kappa=1\) and the regime \(\kappa>1\). Sen and Dasgupta (2004) study persistence, spin-domain coarsening and the separate role of \(\kappa=1\); their weak-coupling domain-length discussion explains the previously known golden-ratio baseline. Dhar, Shastry and Dasgupta (2000) analyze equilibrium ground-state degeneracy and dynamics at the distinct equilibrium multiphase coupling \(\kappa=1/2\). None of the inspected full-text results supplies the present marginal and strong-frustration polynomial enumeration of *all weakly one-spin blocked configurations*. These are statement-level distinctions: ground states and typical Glauber trajectories are not the whole set of weak local energy minima. The known locations of dynamical or equilibrium transitions are not claimed as new. Exact equivalent coverage in other literature remains a bibliographic risk.

## Limitations

Only periodic chains of length at least five, positive couplings and individual spin flips are covered. The classification uses non-strict local energetic stability; a zero-cost flip is not a blocking defect under dynamics that accept neutral moves. The entropy is an unweighted count over all spin configurations and does not describe their dynamical likelihoods or energy-resolved distribution. No many-spin cooperative stability, relaxation rate, or equilibrium thermodynamics is claimed. Bibliographic comparison cannot rule out independently known equivalent enumerations outside the sources inspected.

## References

1. S. Redner and P. L. Krapivsky, “Slow Coarsening in an Ising Chain with Competing Interactions” (first posted 1998-05-28), arXiv:cond-mat/9805385.
2. P. Sen and S. Dasgupta, “Persistence and dynamics in ANNNI chain” (first posted 2004-11-19), arXiv:cond-mat/0411504.
3. A. Dhar, B. S. Shastry and C. Dasgupta, “Equilibrium and dynamical properties of the ANNNI chain at multiphase point” (first posted 2000-04-13), arXiv:cond-mat/0004207.
