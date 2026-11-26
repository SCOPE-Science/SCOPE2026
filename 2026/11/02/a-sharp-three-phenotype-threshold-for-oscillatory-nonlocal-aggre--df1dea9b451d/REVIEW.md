# Independent mathematical audit

## correctness

PASS

The base-state potential gradient vanishes, so the perturbation of the prefactor contributes no first-order term. The Fourier matrix is −k²I+β̃ L_N+qBCᵀ with q=k²μ̃Up(U)K̂(k)≥0. In N=2 the unshifted determinant is −qβ̃(sum B)(sum C): q>0 gives two simple real roots of opposite signs before shifting, and q=0 gives the real diffusion spectrum. N=1 is scalar. For the exact N=3 example the heat kernel is positive, C is strictly positive, and sum(A)=9. After scaling as in the record, the rank-one determinant lemma gives det(zI−L₃−a bcᵀ)=z³+(4−11a)z²+(3+26a)z−33a. At a=1 it has one real root r in (1,2) by strict monotonicity, and its remaining roots form a nonreal pair. In the n=±1 growth matrix the pair has real part (5−r)/2>3/2, larger than the real eigenvalue r−1∈(0,1). Exact cubic Hurwitz margins at |n|=2,3 are 917/2 and 139168425/16384 with all positive coefficients. For |n|≥4 the Hermitian-part bound is Re λ≤−n²+2n²2^{−n²}||b||||c||<0. At n=0 the eigenvalues are 0, −1, −3. Thus only n=±1 are unstable among nonconstant modes, and there is also a slower unstable real eigenvalue there. Independent exact replay: python3 /workspace/review-evidence/reproduce.py 1 (SymPy). The supplied checker and verification note were inspected, not executed.

## originality

PASS

The supported novelty is the sharp phenotype restriction under positive aggregate interaction in the rank-one switching class, and a normalized positive-aggregate witness with just one unstable spatial harmonic up to sign. It is not generic three-population wave instability or the model itself. The closest same-model wave example has negative aggregate interaction. Distinct adjacent thresholds without the prescribed switching and sign structure do not entail the bound result.

## value

PASS

Positive aggregate interaction is a natural restriction separating overall attraction from entrywise attraction. The result resolves exactly how many phenotypes are needed for a dominant growing complex mode in that class; neither the previously illustrated negative-net witness nor an entrywise-positive theorem settles it. The three-phenotype example saturates the obstruction under a normalized interaction and identifies all unstable harmonics by a proof across the whole Fourier lattice. The certificate isolates a structural boundary, not merely a new tuple in a known parameter regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
