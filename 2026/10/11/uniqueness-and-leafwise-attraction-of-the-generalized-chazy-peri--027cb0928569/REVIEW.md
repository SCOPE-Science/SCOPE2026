# Independent mathematical audit

## correctness

PASS

With f(x)=|x|^q and a_q(x)=f(x)/x (continuous at zero), direct differentiation of H=xz−y²/2+x f(x)y gives XH=0 for all integer q>=2; the vector field is C1. The w=z+f(x)y transform gives H=xw−y²/2; U=x+w, V=x−w turn H=−h<0 into V²+2y²−U²=4h, a smooth cylinder without equilibria. The ambient divergence is −|x|^q. Because H is a regular first integral, its leafwise coarea area form obeys L_X omega_h=−|x|^q omega_h. Any contractible closed orbit bounds a disk, and two distinct essential closed orbits on a cylinder bound a compact annulus; Stokes gives zero flux through the tangent periodic boundary but strictly negative interior divergence, a contradiction. Thus at most one cycle/leaf. The Poincare transverse multiplier within the surface is rho_q=exp(−int_cycle |x(t)|^qdt)∈(0,1); two other full-flow multipliers equal 1 from time translation and conserved regular H (without semisimplicity claim). Scaling x→lambda x(lambda^q t), y→lambda^{q+1}y(lambda^q t), z→lambda^{2q+1}z(lambda^q t) scales H by lambda^{2q+2} and makes int |x|^qdt energy-independent. For bounded forward orbits, omega-limits are compact on the no-equilibrium cylinder; Poincare–Bendixson yields the sole periodic orbit as the limit. Existence through q=100 is imported from the original publication, not independently reproved. The theorem does not assert all trajectories are bounded. Source finite symbolic diagnostic is corroborative only.

## originality

PASS

The 2023 originating theorem constructs periodic cylinders for a range of q but does not assert a unique cycle per energy leaf or exact transverse Floquet spectrum and bounded-basin attraction. A 2024 paper publicly states existence for all q; its inaccessible full text is a genuine priority risk, explicitly documented without inventing its absence of a competing theorem.

## value

PASS

The global one-cycle-per-energy-leaf theorem, precise attracting Floquet multiplier, and convergence of all bounded forward trajectories convert a known existential periodic cylinder into a rigid dynamical classification. These are nontrivial geometric consequences of the coarea-divergence structure, not routine coordinate changes or another finite existence list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
