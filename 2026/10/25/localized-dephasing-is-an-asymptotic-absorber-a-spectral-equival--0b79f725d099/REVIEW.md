# Scientific review

## Correctness — PASS

The graph-theoretic key is the strictly positive matrix element \(\langle s|H^d|f\rangle>0\) at graph distance \(d\). Any nondecaying eigenoperator commutes with every site-dephaser projector and annihilates all absorbing vertices. Commutation with the Hamiltonian forces annihilation of their entire cyclic Krylov spaces; the positive path matrix element forces the diagonal element at every dephasing vertex to vanish, so its Krylov space is also annihilated. This proves the equivalence and rules out extra peripheral operators. Contractivity excludes Jordan defects. The cycle corollary follows by the sine Fourier basis and a root-of-unity identity. The standalone program passed 1,198 finite checks with maximum discrepancy \(3.109\times10^{-15}\); it corroborates rather than certifies the infinite claims. Valid only for nonzero positive local rates, connected real positive-weight hopping, finite size and fixed-time-to-infinity ordering.

## Originality — PASS relative to the inspected evidence, with priority risk

The relevant earlier models distinguish extraction from Lindblad dephasing but do not state the evaluated universal equality of infinite-time survival for *arbitrary sparse site-noise support* and an augmented absorber set. The original ring coherent two-trap spectral arithmetic is substantially known from Agliari–Mülken–Blumen (2009), so the corollary's Fourier computation is not presented as a separately original mechanism. Rebentrost et al. (2008) investigate noise-assisted transport with loss, Celardo et al. (2014) focus on collective openness, and Behzadi et al. (2014) investigate designed network dephasing. The later Le et al. (2018) paper was inspected in full relevant sections: it identifies a framework for noise suppression of dark states, with homogeneous dephasing examples, but does not give the claimed general sparse-support equivalence. The 2018 article, especially its citations to earlier general dark-state theory, means that a general result outside these searches may still imply the new theorem. Thus originality is a best-knowledge comparison, not proof of absolute historical priority.

## Value — PASS

For a physically natural finite network with site-selective environmental noise, the exact *location* and positivity of dephasing decide the eventual absorption fraction while its intensity does not; the theorem converts an open-system peripheral-spectrum problem to a finite Hamiltonian Krylov-space calculation. It distinguishes single-site dephasing from uniform dephasing and yields a complete arithmetic location rule on cycles. This is a motivated structural inference about sparse noise-induced dark-subspace suppression, not an arbitrary graph-size calculation. The equivalence is a long-time statement; it has no finite-time or noise-rate-uniform consequences.

## Nearest comparisons and residual limitations

Earlier work: Rebentrost et al. 2008 (arXiv:0807.0929), Agliari et al. 2009 (arXiv:0903.3288), Celardo et al. 2014 (arXiv:1403.5660), Behzadi et al. 2014 (arXiv:1412.3745), and Le et al. 2018 (DOI 10.1088/1751-8121/aad3e6). A general theorem on invariant enclosures of quantum Markov semigroups might subsume the mathematical mechanism; no independent historical-priority audit has been performed. The protected space can remain nontrivial after sparse dephasing; no claim of universally perfect absorption is made.

Self-review: passed. Independent audit: not yet performed.
