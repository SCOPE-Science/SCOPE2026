# Dynamical equivalence gives an exact oscillatory invasion advantage for juvenile predators
## Finding
For the nondimensional Beverton–Holt + Nicholson–Bailey model of Seno and Goyal with \(\sigma=0\), the exact dynamical equivalence between the juvenile-predator native system and the adult-predator native system also fixes the relative growth rate of rare alien predators on any corresponding positive recurrent resident state.

Let \(\mu\) be an invariant probability measure supported on a compact positive invariant set of native juvenile-predator Model J, and write \(\bar p=\int p\,d\mu\). Let \(\nu\) be its image under the source's conjugacy \(x=r_0h/(1+h)\) to native adult-predator Model A. For an adult-specific alien introduced at vanishing density into Model J and a juvenile-specific alien introduced at vanishing density into the conjugate Model A, with the same reproduction parameter \(\alpha>0\), their transverse Lyapunov exponents satisfy

\[
\chi_J(\alpha)-\chi_A(\alpha)=\bar p.
\]

Consequently, whenever \(\bar p>0\), the juvenile-specific alien has strictly larger local rare-invader growth for every equal \(\alpha\). The zero-exponent thresholds obey

\[
\alpha_{J,c}=e^{-\bar p}\alpha_{A,c}<\alpha_{A,c},
\qquad
\mathscr R_{0,c}^J=e^{-\bar p}\mathscr R_{0,c}^A.
\]

For a positive period-\(k\) resident cycle, this is equivalently

\[
\Lambda_J=e^{\sum_{j=0}^{k-1}p_j}\Lambda_A.
\]

## Assumptions and scope
The statement concerns the source's specific nondimensional system (27), with \(r_0>1\), \(\sigma=0\), and a fixed native predator parameter \(\alpha_N>0\). The resident state is assumed to lie in a compact invariant subset of the strictly positive state space, so \(\log h\) is integrable and \(\bar p>0\) is meaningful. The two native systems are compared through the exact source transformation \(x=r_0h/(1+h)\), and the alien predators are compared at the same reproduction parameter \(\alpha\). Because the basic replacement number is \(\mathscr R_0=\alpha(r_0-1)\), equal \(\alpha\) also means equal basic replacement number.

The claim is about local transverse growth when the alien is rare. A positive transverse exponent does not by itself prove ultimate establishment, coexistence, competitive exclusion, or any global basin statement.

## Proof
In native Model J, define

\[
x_n=\frac{r_0h_n}{1+h_n}.
\]

The first Model-J equation gives

\[
h_{n+1}=e^{-p_n}x_n,
\qquad	ext{hence}\qquad
\log x_n=p_n+\log h_{n+1}.
\]

The source proves that the transformation \(x_n=r_0h_n/(1+h_n)\) converts native Model J into native Model A with the same predator coordinate. If \(\mu\) is invariant for Model J and \(\nu\) is the pushed-forward invariant measure for Model A, invariance therefore gives

\[
\int\log x\,d\nu
=\int p\,d\mu+\int\log h\circ f\,d\mu
=\bar p+\int\log h\,d\mu.
\]

Now linearize only in the absent alien coordinate. In full system (27), an adult-specific alien obeys

\[
p^A_{n+1}=\alpha(1-e^{-p^A_n})h_n,
\]

so at \(p^A=0\) its scalar transverse derivative is \(\alpha h_n\). Thus

\[
\chi_A(\alpha)=\log\alpha+\int\log h\,d\mu.
\]

For a juvenile-specific alien in the corresponding Model-A resident system, the juvenile prey quantity available in the next season is \(x_{n+1}\). The second equation of (27), linearized at zero juvenile-alien density, therefore has scalar transverse factor \(\alpha x_{n+1}\). Since \(\nu\) is invariant,

\[
\chi_J(\alpha)=\log\alpha+\int\log x\,d\nu
=\chi_A(\alpha)+\bar p.
\]

If \(\bar p>0\), strict ordering follows. Solving \(\chi_A(\alpha)=0\) and \(\chi_J(\alpha)=0\) yields

\[
\alpha_{A,c}=\exp\left(-\int\log h\,d\mu\right),
\qquad
\alpha_{J,c}=e^{-\bar p}\alpha_{A,c}.
\]

Multiplication by the common factor \(r_0-1\) gives the identical ratio for the source's basic replacement numbers. On a period-\(k\) orbit, multiplying the scalar transverse factors over one period and using \(x_j=e^{p_j}h_{j+1}\) gives

\[
\Lambda_A=\alpha^k\prod_{j=0}^{k-1}h_j,
\qquad
\Lambda_J=\alpha^k\prod_{j=0}^{k-1}x_j
=e^{\sum_{j=0}^{k-1}p_j}\Lambda_A.
\]

## Verification
The identities above use only the published recurrence relations, the published conjugacy, invariance of the resident measure, and first-order expansion \(1-e^{-z}=z+O(z^2)\). The accompanying verifier checks the one-step source identity \(x_n=e^{p_n}h_{n+1}\), the cyclic product identity, and the resulting threshold ratio on deterministic positive test data. These checks supplement, rather than replace, the algebraic proof.

## Relationship to prior work
Seno and Goyal derive equilibrium-based invasion conditions and conclude analytically that, at a stable coexistent equilibrium, a juvenile-specific alien can be more successful than an adult-specific alien. They explicitly state that they have no analytical success/failure result when the native system is oscillatory, and then report numerical evidence that the same stage ordering persists there. The present result converts that numerical stage-ordering observation into an exact local invasion-exponent comparison for every corresponding compact positive invariant resident state of the specific model, including positive periodic cycles and invariant measures on oscillatory attractors.

The source itself relates the native systems to earlier discrete-time stage-specific predator models of Weide et al. and to Model 3 of Marcinko and Kot. Those works address resident dynamics and bifurcation structure rather than the two-alien comparison above. General Floquet and transverse-Lyapunov methods explain how rare invaders are assessed on recurrent resident states, but they do not imply the source-specific identity \(\chi_J-\chi_A=\bar p\), which depends on the exact conjugacy and the placement of stage-specific predation in system (27).

## Limitations
The theorem compares infinitesimal alien growth on dynamically corresponding resident states. It does not determine nonlinear fate after the alien becomes appreciable, and it does not prove coexistence, native-predator extinction, or global invasion success. Strictness requires \(\bar p>0\); boundary invariant measures with zero resident-predator load are outside the stated positive-resident scope. The proof is specific to the \(\sigma=0\) Beverton–Holt + Nicholson–Bailey specialization and its exact conjugacy.

## References
1. H. Seno and A. Goyal, “Discrete-time exploitative competition model of different stage-specific predators,” *Journal of Mathematical Biology* 93, 11 (2026). DOI: 10.1007/s00285-026-02427-w.
2. A. E. Weide, M. Varriale, and F. M. Hilker, “Hydra effect and paradox of enrichment in discrete-time predator-prey models,” *Mathematical Biosciences* 310 (2019), 120–127. DOI: 10.1016/j.mbs.2018.12.010.
3. C. L. Marcinko and M. Kot, “A comparative analysis of host–parasitoid models with density dependence preceding parasitism,” *Journal of Biological Dynamics* 14 (2020), 479–514. DOI: 10.1080/17513758.2020.1783005.
4. C. Kuehn and T. Gross, “Nonlocal generalized models of predator-prey systems,” arXiv:1105.3662.
