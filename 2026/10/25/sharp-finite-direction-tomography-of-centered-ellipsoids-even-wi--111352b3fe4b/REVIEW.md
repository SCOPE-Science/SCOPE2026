# Independent mathematical audit

## correctness

PASS

For n>=2, Q SPD, E_Q={x:x^T Q^-1 x<=1}, derive by affine coarea the (n-1)-section formula A_Q(u,s)=kappa_{n-1} sqrt(D)/sqrt(q) (1-s^2/q)_+^((n-1)/2), D=det Q, q=u^T Q u. Central observations yield u^T H u=kappa_{n-1}^2/A_Q(u,0)^2 with H=Q/D. The m=n(n+1)/2 normals e_i and (e_i+e_j)/sqrt2 reconstruct each H_ij by polarization; D=(det H)^(-1/(n-1)) then recovers Q without separately knowing volume. For arbitrary N<m normals, a nonzero kernel T of the symmetric quadratic sampling map exists. If normals span, no nonzero semidefinite kernel T is possible, hence T indefinite. If not, T=vw^T+wv^T with v perpendicular to all normals and w independent of v is indefinite and annihilates samples. The positive-definite pencil I+zT has bounded interval endpoints where determinant tends to zero; by IVT it admits distinct negative and positive z with equal positive determinant (e.g., 1/2), identical sampled q, hence identical complete all-offset section profiles and total volume. Scaling preserves pair ambiguity and forces arbitrarily large minimum eigenvalues. For single noncentral offset t>0 with known determinant and Q> n t^2 I, the scalar F_t(q)=(q-t^2)^((n-1)/2)q^(-n/2) has logarithmic derivative (n t^2-q)/(2q(q-t^2))<0 and each m-sample uniquely recovers q; the previous ambiguity persists under sufficient simultaneous scaling. Independent exact 3D inversion, 2D equal-determinant ambiguity and derivative checks passed.

## originality

PASS

Qualified PASS for the sharp number of prescribed angular directions for oriented centered ellipsoid reconstruction, including equal-volume ambiguity from every smaller fixed direction set and fixed noncentral-height thickness regime. Classical ellipsoid section formula, quadratic-form polarization and all-direction geometric tomography are prior work. A textbook finite quadratic-form sampling result might imply some portions, but the volume-preserving all-offset lower bound is an additional universal quantifier not shown in inspected all-angle articles.

## value

PASS

A natural finite-angle tomography design problem is solved exactly: m viewing angles are both necessary and sufficient even with infinitely many offsets and a known volume. The indistinguishable equal-volume pairs identify a real global identifiability obstruction; the explicit optimal design and thick-body single-offset variant are useful exact benchmarks, rather than an unmotivated finite invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
