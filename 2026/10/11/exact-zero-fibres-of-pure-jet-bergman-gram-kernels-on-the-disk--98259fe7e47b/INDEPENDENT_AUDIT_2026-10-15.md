# Independent mathematical audit

## correctness

PASS

From K(z,w)=π^-1Σ(k+1)(z wbar)^k, differentiating m times in both variables with /(m!)² gives π^-1Σ(j+m+1) C(j+m,m)² t^j. Euler hypergeometric transform yields (m+1)P_m(t)/(π(1−t)^(2m+2)); Jacobi identity P_m(t)=(1−t)^m P_m^(0,1)((1+t)/(1−t)) is exact. Orthogonality puts m simple zeros on (-1,1) in x, hence negative t; (1+x)P_m^(0,1)=L_m+L_(m+1) and strict interlacing plus parity give ceil(m/2) positive x, hence t in (-1,0), with no x=0. Every such t is z wbar for points strictly in disk. m=0 zero-free. Package code independently checks exact identities m<=12; infinite theorem rests on Jacobi/Legendre argument.

## originality

PASS

Gehlawat--Jain--Sarkar define the canonical derivative Gram kernel and establish upper-half-plane pure-jet zero-freeness; the audited disk family uses its distinct non-affine geometry. The result derives every pure-order disk root fibre via Jacobi and Legendre interlacing. Prior first-jet disk theorem is the m=1 special case but does not imply arbitrary m or the ceil(m/2) count. This is a genuine infinite-order exact classification beyond the m=1 result.

## value

PASS

This supplies a complete order-by-order disk zero-fibre classification of canonical positive-definite jet kernels, quantitatively separating pure jets on the disk from the upper half-plane and answering an exact Lu Qi-Keng question. The natural object and sequence m are intrinsic to derivative evaluation and are not an arbitrary finite parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
