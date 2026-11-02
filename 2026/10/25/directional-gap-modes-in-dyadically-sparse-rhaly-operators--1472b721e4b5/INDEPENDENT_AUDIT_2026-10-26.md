# Independent mathematical audit

## correctness

PASS

For u,v>0, active Rhaly rows are f_k=2^(-k/2)sum_(j<2^k)e_j multiplied by b_k, so their exact Gram is K=D_b T_(1/sqrt2)D_b, where T has entries 2^(-|i-j|/2), bounded and invertible. J=K^-1 is a positive half-line Jacobi matrix with d_0=2/u², even tail A=3/u², odd tail B=3/v², off-diagonal -sqrt2/(uv). Period-two Bloch dispersion gives essential bands [L,min(A,B)] and [max(A,B),U], L,U=(A+B∓sqrt((A-B)²+16t²))/2 with t=sqrt2/(uv). Floquet multipliers off bands permit only a simple boundary eigenvalue: algebra yields lambda*=2/u²+1/v² and decay ratio -u²/v², square-summable iff u<v, and no embedded band eigenvectors. Polar decomposition/spectral mapping gives two singular bands, one isolated singular value uv/sqrt(2v²+u²) iff u<v, zero kernel of infinite multiplicity, norm/essential norm L^-1/2 and b(1+sqrt2) at u=v=b. Independent eigenvalue calculations of 240x240 truncated Jacobi matrices confirm exactly one internal-gap mode for (u,v)=(1,2),(1.4,2.3) at formula, none for (2,1),(1,1). Truncations do not prove the entire infinite essential spectrum; the Bloch/Fredholm proof is essential.

## originality

PASS

Best-of-knowledge new all-band singular spectrum and directional half-line boundary state for this explicitly motivated dyadically sparse, two-periodic Rhaly family, distinct from classical factorable-matrix norm bounds and compact-operator Schatten theory.

## value

PASS

Natural exactly solvable noncompact Rhaly model interpolating dyadic sampling and periodic operator theory, with explicit essential-band topology, a genuinely directional localized edge eigenmode, and sharp essential norm. The u↔v boundary asymmetry is a meaningful structural phenomenon even though Floquet analysis itself is standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
