# Scientific review: rational-resonance capture on two-coupling hypercubes

## Correctness — PASS

The mathematical domain is a finite \((a+b)\)-dimensional Boolean cube with \(a,b\ge1\), uniform positive coordinate-flip couplings within each block, and one irreversible positive-rate sink at zero. The proof identifies the Walsh spectrum and an orthonormal bright projector for each distinct energy. Dissipativity excludes real-spectrum eigenvectors from the bright subspace, which decays in finite dimension. Its dimension is therefore the number of distinct \(k+\rho l\) energies, and its sitewise projection gives all probabilities. For a reduced resonant \(\rho=u/v\), lattice fibers are disjoint primitive-step chains whose exact edge count gives the dimension deficit. Complete-capture sites are classified by Fourier signs in the single-weight subspaces, then by parity along each resonance chain. Cauchy–Schwarz proves the individual-site monotonicity at resonance.

Both standalone checkers have been executed on their packaged source files. One compares exact-rational Krawtchouk predictions with independently assembled full Walsh matrices over 144 parameter cases and 8,100 initial-site cases. The second propagates a genuinely dissipative effective Hamiltonian at long finite times for 168 site cases. The raw scientific outputs appear in `CHECKS.txt`. Checks cannot certify every finite dimension; the arbitrary-size proof supplies that part. The result does not make claims about transient evolution rates.

## Originality — PASS on examined evidence, with explicit historical-priority risk

Moore–Russell (2001, arXiv:quant-ph/0104137) supplies the known uniform-hypercube Walsh diagonalization but no two-block rational-collision census, sitewise capture law, or full-capture parity transition. Le–Donati–Severini–Caruso (2017, arXiv:1707.07482) gives the general degeneracy/dark-state framework, not this exact arithmetic phase diagram. Razzoli–Paris–Bordone (2021, DOI:10.3390/e23010085) develops bright/Krylov projection methods and capture examples on other families, not this two-block weighted hypercube classification. Makmal et al. (2015, arXiv:1510.08388) analyze discrete-time coined rather than this absorptive continuous-time model.

Related hypercube calculations for independently weighted edges, two absorbing sites, and absorbing Hamming shells have distinct operators and trap configurations. Those different hypotheses do not by themselves imply the two-block exceptional-ratio list or the full-capture-site parity law. A published closest result on weighted \(P_4\) Cartesian powers concerns a different graph family with its own spectral coalescences. A specialized earlier controllability theorem for exactly this parameterization could exist and is the residual risk; database search alone does not prove absence. No independent priority audit has been conducted.

## Mathematical value — PASS

The two-rate Boolean cube is a natural, experimentally interpretable model of anisotropic coherent transport. All irrational and all but finitely many rational couplings have the same capture capacity, whereas explicitly enumerable reduced rationals cause quantized dark-subspace increases. The exact size of every jump, all starting-site efficiencies, and the orientation-dependent two-corner survivor rule are motivated transport quantities. Unlike a generic matrix calculation, this classifies an infinite set of network sizes and their complete parameter-driven boundary. It offers quantitative benchmark cases for quantum transport and trap design without claiming applicability to noise or finite-time rates.

## Limits

The stated scientific novelty is provisional pending independent work. A highly specialized earlier result on two-rate Walsh-spectral controllability may be unlocated; no claim of exhaustive literature search is made. All sources supporting generic background are attributed. Only the exact model proved here is covered.

Self-review: passed. Independent audit: not yet performed.
