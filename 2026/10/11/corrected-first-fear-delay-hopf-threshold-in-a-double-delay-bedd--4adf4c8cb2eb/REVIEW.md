# Independent mathematical audit

## correctness

PASS

Reconstructed printed 2-state nonlinear model and tau_2=0 equilibrium independently (x*,y*)=(0.121908145169124554729929382673...,0.570158908561061634596216471872...). Independently symbolically differentiated vector field (SymPy rational coefficients) to obtain A11=-0.0295992170402710, A12=-0.04272458459092165, B12=-0.04781531925074255, A22=-0.11140317817122123, C21=0.44210677105029230,C22=0.05126950150910599. The determinant is lambda^2+P lambda+Q+R exp(-lambda tau1) with P=0.0897328937023862753,Q=0.0206687378849088765,R=0.0211394764006846687. Eliminating phase gives z^2+(P^2-2Q)z+(Q^2-R^2)=0, with one positive root z+=0.0338666086691450845 and one negative root z-=-0.000581125111531086; omega=sqrt(z+)=0.184028825647356356. Both sin and cos equations require principal positive phase phi=0.896531174337346... so first delay tau=4.8716888301798779245...; Delta(i omega,tau) magnitude <1e-60. At published tau=4.5923, Delta(i omega,tau) magnitude 0.001086779110941..., and uniqueness of positive frequency rules out any other imaginary crossing there. Zero-delay quadratic is Hurwitz since P>0, Q+R>0; Delta(0,tau)=Q+R>0, no zero eigenvalue. Implicit crossing speed Re(dlambda/dtau)=+0.00578097609286525. Retarded DDE spectral continuity therefore proves linear stability before first crossing and first instability at it. The paper's 3.5,5 simulations still straddle the true boundary. This does NOT prove nonlinear Hopf criticality or any two-delay region; high-precision signs are numerically robust but not machine-verified interval certificates.

## originality

PASS

Best-of-knowledge PASS restricted to an actual correction of a published false first-crossing numerical value and its phase-branch evaluation, not to the source's already published generic frequency polynomial or the classical imaginary-axis criterion. Cui et al., Axioms 12:73 (2023), Section 3 Case II Eqs. (12)-(17), derive the same characteristic equation and frequency quadratic but publish tau_1*=4.5923 in Section 5 Case II; their displayed arctan phase in Eq. (17) uses denominator Q-omega^2, which here is negative, and its literal principal branch does not yield a positive first delay. Simultaneously imposing their Eqs. (13)-(14) gives the correct quadrant-aware first phase 0.896531174337... and tau=4.871688830179..., whereas the source's printed first threshold does not satisfy its own root equation. Search and inspected adjacent full texts did not find this correction independently. The theoretical delay-crossing framework is prior art; the distinct surviving point is a material source-specific correction. Residual risk includes an unindexed erratum, alternate published computation, and the borderline originality of a numerically explicit consequence of known governing equations.

## value

PASS

Motivated numerical correction of the actual first delay-induced local stability boundary of a published prominent Case II example. The 0.2793888301798779 difference is about 6.08% of the printed value and changes the predicted linear stability for 4.5923<tau1<4.87169, not merely a rounding digit. It also diagnoses phase-branch handling as mathematically consequential and explains why published simulations at 3.5 and 5 did not expose the wrong number. The object/invariant are natural within a published DDE bifurcation diagram; exact first crossing is useful for reproduction and any later nonlinear analysis. It remains a single source-parameter correction, not a new general Hopf theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
