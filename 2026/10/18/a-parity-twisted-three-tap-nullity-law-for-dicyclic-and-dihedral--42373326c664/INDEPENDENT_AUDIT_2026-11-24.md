# Independent mathematical audit

## correctness

PASS

Use the regular Fourier basis e_z=Σ_j z^(−j)[a^j] and b e_z for z^(2m)=1; left multiplication by a acts with eigenvalues z,z⁻¹ and the reflection square gives the factor z^m (or 1 in the split case). This accounts for every dimension, including z=±1. Pure supports factor to 1+a^u+a^v: if ξ=z^g gives a cubic pair, its order is exactly 3 because gcd(q,u/g,v/g)=1, and both primitive choices work precisely for the stated residue pair and 3|q. Each lifts to g characters and kills both block coordinates. Mixed supports translate to 1+a^u+a^v b, preserving the same-coset displacement up to sign. The block is singular exactly at a primitive cubic z^u, restricted to z^m=1 in the dicyclic case, with kernel dimension one since the off-diagonal entries are nonzero. Counting preimages yields both gcd formulas and the shared singularity test; gcd(2m,u)/gcd(m,u)=2 precisely at the stated 2-adic threshold. For the pure census, at each common valuation t<r there are 2(N/3^(t+1))² ordered displacement pairs per anchor; count both cosets and divide by six. For mixed supports, count N choices for the first tap in the pair and N for the singleton, both pair cosets, and divide ordered pairs by two. Of the displacements not divisible by 3^r, the fraction divisible by 2^(s+1) is 2^(−s−1), by coprimality. This verifies all three counts and the r=0 case. An independent exact-QQ sparse regular-matrix checker ranked identity-anchored triples and used left translation in each group to check every labeled support for m=2,3,4,6,9, obtaining (pure,mixed,halved)=(16,144,72),(128,1152,288),(480,5184,2592) in the three divisible cases. Finite checks are corroboration, not the proof for all m.

## originality

PASS

The split dihedral branch and its singular support census already occur in a distinct Resultary record, and the central-twist factors are known. The supported distinct claim is the paired exact comparison on the same labels: identical singular supports, a strict factor-of-two drop on the specified mixed parity stratum, and the closed census of that stratum. The indexed date does not resolve priority for the shared branch.

## value

PASS

The full paired law detects a difference in kernel dimension where support singularity alone cannot distinguish the split and central-twisted extensions. It locates and counts exactly when the twist removes half of the kernel directions, beyond the already-covered split census. The support class and coordinate comparison are natural and the result applies at every group order in scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
