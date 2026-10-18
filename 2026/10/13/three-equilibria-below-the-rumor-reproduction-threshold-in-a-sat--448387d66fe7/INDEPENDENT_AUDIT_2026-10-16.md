# Independent mathematical audit

## correctness

PASS

For the exact four-compartment Mohamed (2026) ODE and all fourteen positive parameters b=28, d=h1=h2=h3=k1=k2=r1=r2=1, sigma1=10, sigma2=5/2, alpha1=1577/4000, alpha2=alpha3=1/1000, direct substitution gives R0=102067/117000<1, E0=(28,0,0,0) and E1=(20,1,1/4,11/2). Reconstruct C=z>0: S=z(9+4z)/(2(1+z)), D=10S/(1+S)+5z/(2(1+z)), U=28/(1+L). H(z)=-z(4z-1)Q(z)/P(z), P>0, with Q sextic whose coefficient sequence has one sign change and Q(1/4)=-561250<0<Q(1/2)=10802295/8. Descartes and IVT imply exactly one additional simple positive root, hence exactly two positive equilibria and just E0 on the boundary. Independent SymPy rational substitution/reduction verifies H and both 4x4 characteristic polynomials; Routh-Hurwitz at E0 and the sign-changing cubic at E1 prove local stability/instability. Implicit-function/simple-root arguments make multiplicity robust, not two stable attractors. Finite arithmetic is corroborative; the exact signs, Descartes and stability arguments prove the general stated assertions.

## originality

PASS

The source paper expressly states global rumor-free attraction for R0<1, incompatible with E1 as a positive stationary state; its general backward-bifurcation mechanism is known from other epidemic ODEs and is not claimed new. The original model-specific, robust rational subthreshold example plus exhaustive two-positive-root census and correction of the 2026 global theorem are not logically supplied by the compared works. Best-of-knowledge PASS; old saturated-recovery full text was not fully read, so an abstract general framework might overlap.

## value

PASS

Global elimination below the source reproduction-number threshold is central to interpretation of this model. An explicit admissible rational counterexample, the sharp entire stationary-state census, different local types, and persistence on open parameter sets materially delimit the source theorem; this is not an arbitrary numerical test nor a generic rediscovery of backward bifurcation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
