# Independent mathematical audit

## correctness

PASS

Independent exact-rational evaluation on the monomial basis gives \(S_2-S_1=0\) through degree three, \(D(t^4)=-1/4\), and \(D(t^6)=-5/16\); odd monomials vanish by symmetry. Thus on \(\mathcal P_6\), \(D(p)=-a_4/4-5a_6/16\). The exact two-panel errors are \(-a_4/60-23a_6/336\); imposing \(4a_4+5a_6=0\) reduces this to \(-a_6/21\). When degree is at most five, the kernel forces \(a_4=0\), so Simpson is exact; degree six is therefore minimal. For \(p_*(t)=-t^6+5t^4/4+1/84\), positivity follows from \(t^4(5/4-t^2)+1/84\), while direct rational evaluation gives \(S_1=S_2=4/21\) and exact integral \(5/21\). Affine change of variables multiplies all three linear functionals by \((b-a)/2\), giving the stated general-interval formula.

## originality

PASS

Premature termination of adaptive Simpson and accidental cancellation of difference-based estimators are established prior phenomena, but the inspected primary literature does not determine the first polynomial degree at which the classical one-panel/two-half-panel signal can vanish incorrectly. Plaskota's explicit catastrophic polynomial has degree ten and vanishes at the five sampled nodes; Gonnet treats estimator reliability broadly. Neither implies the exact degree-six nullspace, missed-error functional, or strictly positive cancellation witness. Targeted Resultary and web searches found no equivalent low-degree classification.

## value

PASS

The first exact blind degree is a natural sharp boundary of a classical stopping criterion. The result distinguishes a minimal cancellation mechanism from previously documented high-degree node-hiding failures, gives the complete kernel and exact missed-error functional, and supplies a strictly positive 20-percent-error regression witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
