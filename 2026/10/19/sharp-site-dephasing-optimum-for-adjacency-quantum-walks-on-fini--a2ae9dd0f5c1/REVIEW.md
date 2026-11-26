# Independent mathematical audit

## correctness

PASS

The frozen equality for the shifted standard cubic in line 92 is false: at m=3, for example, its true quadratic factor is w²+w+2 rather than w²+3w+4. The complete replacement /workspace/repairs/5/RESULT.md gives w[w²+(2s−s^(-1))w+2s²] with s=sqrt(m−2) and retains strict decay of the other two shifted roots. Exact symbolic expansion verified the corrected shift, the sign identity, and the shifted trivial cubic. Independently, apply the determinant lemma to the Hamiltonian commutator plus diagonal projection. The projected commutator resolvent is the Laplace transform of squared transition amplitudes and acts on constant populations, leaf contrasts, and the hub–leaf contrast by three explicit scalar transfer functions. The resulting full characteristic determinant gives the stated multiplicities for all m≥2, including m=2, and simple zero. The standard cubic supplies a real root strictly between the claimed optimum boundary and zero at any other positive rate for m≥3; the repaired quadratic and shifted trivial Hurwitz inequalities establish attainment. For m=2 the discriminant-zero standard pair bounds the gap, and the trivial cubic is strictly Hurwitz after the shift at that point. See reviews/evidence/star_spectrum.md for the determinant and optimizer reconstruction. Only the proof lines in RESULT.md needed replacement; the unchanged characteristic polynomial and theorem agree with the independently verified ones. The frozen finite verifier was read, not executed. This is a spectral-gap result, not a state-specific or uniform finite-time convergence optimum.

## originality

PASS

The repair preserves the scientifically distinct claim: the full, trace-preserving adjacency-star Liouvillian polynomial and unique optimal positive site-dephasing rate for its spectral gap. The closest indexed adjacency-star result instead assumes a hub sink and minimizes mean absorption time. The closest gap paper treats a Laplacian commutator, with weak/strong dephasing observations rather than the stated full characteristic polynomial and global optimizer. The two Hamiltonians are not related by an irrelevant scalar shift and common scale on an irregular star. The optimum is not taken from a checked table or the indexed integrated-return calculation. This is a bounded comparison, not a claim that no equivalent prior master-equation analysis can exist.

## value

PASS

The result solves the full spectral relaxation design question for a natural family of inhomogeneous graphs. It identifies which sector limits relaxation, distinguishes a two-leaf exceptional point from all higher degrees, and establishes the opposing asymptotic scalings of optimum noise and achievable gap. The corrected factorization supports exactly the same structural theorem, not just a fit or finite-size optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
