# Self-review

## Correctness (C): PASS

The argument starts from the strongly regular adjacency identity \(A^2=(k-\mu)I+(\lambda-\mu)A+\mu J\). Hence the two nonzero unit-Laplacian eigenvalues satisfy \(q_1+q_2=2k-\lambda+\mu\) and \(q_1q_2=\mu v\). The exact identity \(P(h)=I-tL_0d(tL_0)^{-1}\), interpolation on \(0,q_1,q_2\), and explicit edge/nonedge \(L_0^2\) entries yield the stated rational kernels. Denominators are positive for real \(t\ge0\). The edge quadratic has one positive root iff \(\Delta>0\), while nonedges and diagonals stay strictly positive, proving the entire interval and no reentry. Both asymptotics follow from the highest-degree terms. The result treats all real timesteps for all graphs meeting the hypotheses; it does not extrapolate from finite experiments. The attached exact-rational checker was executed successfully: 10 named graphs, 50 rational matrices, 8740 off-diagonal entry checks.

## Originality (O): PASS, with explicit prior coverage and residual risk

**Closest prior theorem [3]:** Bendito–Carmona–Encinas–Mitjana establish the graph-Laplacian pseudoinverse \(M\)-property in strongly regular graphs, with condition \(\mu\ge k-k^2/(v-1)\). Using the standard SRG counting identity, this is algebraically equivalent to \(2k-\lambda+\mu\ge v\). Their primitive-complement duality, conference equality, and triangular graph boundary therefore predate the present work and are not claimed. Their inspected material does not give the \([2/2]\) Padé step kernel, exact *finite* timestep endpoint, positive nonedge coefficient, or critical temporal asymptotic. General Padé positivity sources [1,2] provide sufficient or negative results for general positive systems, not this exact SRG classification. Relevant published-finding corpus records on Markov Padé counterexamples, Crank–Nicolson resolvents and lattice filtering concern other generator classes or integrators. A special historical paper on the *same* Padé operator and strongly regular graph family might still exist; no exhaustive priority claim is made.

## Mathematical value (V): PASS

Unconditional stability of a rational Laplacian integrator does not imply preservation of nonnegative mass-transfer coefficients. For the standard and structurally motivated strongly regular graph class, the result gives a complete and directly usable time-domain positivity decision, a closed sharp maximal admissible step when positivity eventually fails, and proof that no disconnected windows exist. It separates the previously known static asymptotic M-property boundary from exact finite-step dynamics, which is not determined by the static criterion alone. Examples include the Petersen graph with \(H=(1+\sqrt5)/c\), critical conference graphs with quadratic edge decay, and the finite triangular/rook transition families. No claim of an algorithmic improvement or wider graph coverage is made.

## Closest literature and limits

[1] Zappavigna et al., *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, https://mural.maynoothuniversity.ie/id/eprint/2195/ . [2] Zappavigna et al., *Essentially Negative News About Positive Systems*, 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ . [3] Bendito et al., *Distance-regular graphs having the M-property*, 2012, DOI 10.1080/03081087.2011.589047, primary conference PDF https://mapthe.upc.edu/en/congresses/docs/congresses_2011_the-m-property-for-distance-regular-graphs.pdf . [4] van Dam–Omidi, *Strongly walk-regular graphs*, arXiv:1208.3067. The known static parameter criterion is fully credited; independent audit and broader specialized-paper verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
