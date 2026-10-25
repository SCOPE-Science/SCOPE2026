# Independent mathematical audit

## correctness

PASS

The theorem fixes b,c,γ>0, independent rate-r alarms and constant speed v inactive returns, with z=rb/c, ε=γb/c, h=c/v. The previous Radice mean-time formula is explicitly credited, not claimed: E T=(b/c)[A_ε(z)+hB_ε(z)]. The source proof derives renewal success p=e^(−w)/(1+z/w), w=√(z(z+2ε)), and failed-cycle return cost via the killed telegraph resolvent. Critically, B has a locally uniformly convergent series 1+1/(z+2ε)+sum_n[2z^n(z+2ε)^n/(2n+1)!+2z^n(z+2ε)^(n−1)/(2n)!]. All polynomial summands have nonnegative coefficients and the rational term has positive second derivative, so Bʺ>0 globally. I independently expanded n=1,2,3 series and checked g1=1+2ε/3−1/(4ε²), g2=ε²/15+ε/6+1/3+1/(8ε³), and ε_c≈0.4396926207859 solves strictly increasing cubic 8ε³+12ε²−3=0. The sign of Bʹ(0) gives unique positive B-minimizer ζ_ε for ε<ε_c versus boundary infimum for ε≥ε_c. A~(2ε+1)/√(2ε) z^(−1/2) as z↓0 and both terms diverge for large z; comparison localizes all large-h global minimizers to ζ or 0 and strict convexity there gives eventual uniqueness. Balancing Aʹ∼−a z^(−3/2)/2 with h g1 or h 2g2 z gives h^(−2/3) and h^(−2/5) laws with the stated constants; implicit function gives O(h^−2) correction in persistent regime. These are mathematical asymptotics, not Monte Carlo inference. Frozen verify.py was inspected; its 70 reported numerical checks are not independent proof.

## originality

PASS

Best-of-knowledge originality PASS with substantial access risk: Radice (2021) published the exact finite-return-speed mean first-passage formula (Eq.129) and killed resolvent. The audited claim does NOT present that formula as new; it isolates a mathematically nontrivial strict convexity lemma for the return-cost factor and a sharp optimizer phase transition with exponents 2/5,2/3 and explicit prefactors. Tucci et al. employ a different harmonic-trap-induced reset protocol. The inaccessible full Radice article may contain a closely related asymptotic conclusion, so this judgment cannot exclude that possibility and is not a whole-article NOT_COVERING certificate.

## value

PASS

Optimal alarms during finite-speed return search are a natural renewal-search control variable. The exact phase boundary for an optimizer that remains positive or vanishes at two different critical exponents reveals a real, model-specific transition that practitioners of first-passage optimization may need. Mere differentiation of a known formula does not by itself give global strict convexity, uniqueness, localization or sharp crossover prefactors; those arguments are the scientific addition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
