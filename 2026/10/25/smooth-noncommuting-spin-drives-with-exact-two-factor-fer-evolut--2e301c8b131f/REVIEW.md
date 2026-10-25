# Scientific review

## Correctness — PASS

The pulse is explicitly \(C^\infty\): the chosen switch has flat endpoint jets, and the radial and constant-radius pieces glue smoothly. The standard Fer recursion in the full text of Bagnasacco–Giovannetti (arXiv:2609.28302v1, Section II, equations (2)–(4)) is independently reduced by Rodrigues conjugation to a vector map with coefficients \(\alpha(r)\) and \(\beta(r)\). Every positive root of \(\tan(2r)=2r\) makes \(\beta(r)=0\), while \(A_n=r_n^2\alpha(r_n)\ne0\). The initial radial portion has zero first remainder; the constant-radius angular portion has a pure \(T_z\) remainder \(A_n\dot\vartheta T_z\), which commutes with its own time integral, hence the second remainder vanishes identically. Noncommutation is witnessed by two pulse times with nonparallel directions. The qubit norm integral is exactly the radial plus angular path length, \(r_n(1+\Theta)\). The independent ODE numerical tests check eight spin/angle/root configurations and 3256 finite assertions; these are corroboration rather than infinite proof.

## Originality — PASS (best knowledge)

The September 2026 paper treats a universal **sufficient** convergence radius and does not construct smooth noncommuting pulses with exact two-factor termination outside it. The 1998 primary paper establishes earlier sufficient radius/error bounds, not the present construction. The October 2026 Bagnasacco–Burgarth–Giovannetti–Yuasa theorem rules out this behavior only under **real-analytic** drive hypotheses, so it does not subsume a nonzero compactly supported \(C^\infty\) drive. The later paper's explicit closed map is an alternative route to one step of this proof, not the new root-family construction itself. Published literature comparisons and topical searches revealed no equivalent statement. The residual risk is an unlocated antecedent using flat smooth controls or finite-factor Fer resonance loops. These searches and comparisons support only a best-knowledge originality conclusion, not a proof of global priority.

## Value — PASS

Finite exact Fer termination for noncommuting spin controls is a structural effect, not the routine substitution of an easier commuting model. It sharply separates analytic rigidity from smooth control and exhibits countably many resonant strengths with continuously variable winding, allowing arbitrary integrated pulse area while retaining only two exact unitary factors. This directly clarifies what a uniform sufficient convergence bound does—and does not—predict for designed quantum control pulses. The phenomenon survives every nontrivial finite spin representation, not just a qubit example.

## Closest literature and limits

Bagnasacco–Giovannetti (2026, arXiv:2609.28302v1); Blanes–Casas–Oteo–Ros (1998, DOI:10.1088/0305-4470/31/1/023); Bagnasacco–Burgarth–Giovannetti–Yuasa (2026, arXiv:2610.27979v1). The construction is special and relies on an exact transcendental root; no robustness, genericity, or improved universal radius is asserted. No independent literature-wide priority audit or external mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
