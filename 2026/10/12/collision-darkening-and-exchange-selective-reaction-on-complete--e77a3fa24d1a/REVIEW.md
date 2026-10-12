# Scientific review

## Correctness (PASS)
The claim uses the exact domain \(n\ge4\), positive hopping strengths and strictly positive diagonal loss rates. The Hamiltonian has four tensor eigenvalue sectors, with precisely one collision of eigenvalues when the hopping strengths agree. The detector Gram matrix in the doubly zero-sum sector has eigenvalues \((n-2)/n\) and \((n-1)/n\), strictly positive on the entire stated domain. This supplies an actual projector and all ranks, not an experimental extrapolation. The dissipation argument ensures the surviving component is precisely the dark spectral subspace. Direct matrix identities produce the claimed localized and exchange-state probabilities. The standalone numerical checker independently reconstructed eigenspaces, verified 24 rank cases and 2,012 probability cases, tested nonuniform positive absorption, and compared four long-time evolutions. It is supporting evidence only.

## Originality (PASS, residual priority risk)
The closest primary literature is Štefaňák et al. (2007, discrete-time infinite-line meetings), Carson et al. (2015, complete-graph coined two-particle entanglement without absorption), and Razzoli et al. (2020 preprint, continuous-time spectral trapping with one detector). Each full text was inspected in relevant sections. The exact complete-graph, all-coincidence-absorber classification is not obtained from these claims. A rectangular detector family cannot imply the fully diagonal configuration, and distinct star and cycle geometries do not cover the complete-graph theorem. Searches found no matching table or stronger statement, but a broader unidentified observability theorem remains a possible priority risk. Absence from searched sources is not proof of universal novelty.

## Value (PASS)
All-to-all coupling is a natural benchmark for coherent reaction networks, and capture upon particle meeting is a motivated physical observable. The theorem gives the entire absorbing projector for all initial states, its rank, and experimentally interpretable closed probabilities. The \(1/n\) localization discontinuity is traced exactly to exchange-antisymmetric modes, whereas the symmetric capture probability is insensitive to changing either positive hopping rate. This supplies a nontrivial structural comparison rather than a small case enumeration or a restated spectral method.

## Limitations
The result assumes perfectly homogeneous complete-graph hopping, no coherent interactions between walkers, strictly positive losses at every meeting site, and asymptotic time. The formalism does not establish finite-time speed bounds. An independently exhaustive publication-priority audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
