# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed exact printed treatment differential equation w_dot=w(beta*z-b-c) and prey differential equation x_dot=r*x*(1-x/K)-m*x*y/(a1+x²)-n*x*z/(a2+x²). For interior equilibrium w>0, beta>0, z=(b+c)/beta; x>0,y,z>0 and positive parameters force 0<x<K, independent of any delay (constant histories). Printed R3 b=1/5,c=1/10,beta=1/10,K=1 forces z=3, but printed E*=(227/1000,1/2,3/2,2/5) has w_dot=-3/50 exactly, and direct full residual check from fraction arithmetic is nonzero. Earlier tuple x=3.36,z=8.85 violates both necessary identities. The exact assertion is that those two printed tuples cannot support the reported local stability/Hopf base-point calculations, NOT that model has no other equilibrium or Hopf bifurcation. Full original 42-page OA paper inspected including equations and numeric tables/figure captions; own check verifies source script fractional reconstruction.

## originality

PASS

PASS, qualified: The original source actually PRINTS the equilibrium z=(b+c)/beta symbolically, but subsequently uses incompatible numerical points. The new scientific assertion is the source-specific comparison and exact contradiction at R3 and earlier point, not new algebraic conservation identities in general. Material reading of original AIMS primary PDF and source-specific erratum search did not identify a correction. A different three-compartment treatment model from Mondal et al. is not the same equations.

## value

PASS

PASS: Exposes an exactly demonstrable, quantitatively nonzero defect in the base point used for published local stability and Hopf figures; such a defect breaks the applicability of those calculations to the stated model, a substantive correction to a published biological dynamical analysis. The two necessary identities are elementary, but their contradiction with claimed key numerical outputs gives clear scientific motivation and consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
