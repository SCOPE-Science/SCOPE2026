# Independent mathematical audit

## correctness

PASS

The original slogan/RESULT asserted raw rank-one coefficients depend only on the rational-root set, which is false. Over F_2 with n=5, irreducible X^5+X^2+1 and (X^2+X+1)(X^3+X+1) are squarefree with no F_2 roots but have centralizer sizes 31 and 21, hence S=322560 and 476160 and distinct trace-zero rank-one values -21504 and -31744. The complete corrected RESULT.md and SLOGAN.txt distinguish normalized and unnormalized profiles. For any q,n and squarefree f, rational canonical form makes V_f a single semisimple conjugacy class, of size |GL_n(q)|/product_i(q^d_i-1). For fixed u!=0 the stabilizer in GL_n(q) is transitive on vectors outside F_q u. A simple rational eigenvalue has exactly q-1 nonzero eigenvectors in each matrix. Double-counting yields N_{lambda u}=S(q-1)/(q^n-1) for roots and zero otherwise; off-line N_w=(S-sS(q-1)/(q^n-1))/(q^n-q). Taking additive characters of v^T Mu gives the c!=0 root-character sum and the c=0 scalar formula. Finite-field Fourier orthogonality yields root inversion using S. This proof works for characteristic two and arbitrary prime powers, not merely the checked fields. An independently written finite enumeration verified all squarefree fibres and all fixed-e1 rank-one probes for (q,n)=(2,3),(3,2),(5,2): 4+6+20 fibres, 28+48+480 probes; the original checker was inspected but not trusted as proof. The F2 quintic polynomial factorization was independently confirmed over GF(2).

## originality

PASS

For the corrected claim, full primary Section 3 of Browning–Gundlach–Sawin concerns the same finite-field fibres and provides stratified bounds, not exact normalized rank-one coefficients or the character-inversion identity. Older semisimple counting determines the scalar fibre size S; no inspected stronger theorem implies the full additive rank-one profile. An uninspected orbital-Fourier identity could still cover this calculation.

## value

PASS

The corrected theorem exactly evaluates the entire rank-one additive Fourier transform of a natural family of finite-field matrix conjugacy orbits, and reconstructs the rational-root indicator from normalized harmonic data. Fixed-characteristic-polynomial matrix fibres are motivated by contemporary Fourier estimates, while the complete formula and inversion reveal a nontrivial arithmetic statistic not supplied by a generic bound. It is not a known-table recomputation of the dual rank-one matrix shell. The meaningful normalization correction is essential; no claim is made of extracting higher-degree factors or full spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
