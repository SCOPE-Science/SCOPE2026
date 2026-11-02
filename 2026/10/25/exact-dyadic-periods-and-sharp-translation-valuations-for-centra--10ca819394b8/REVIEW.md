# Independent mathematical audit

## correctness

PASS

Legendre/Delannoy identity D_n=sum_k 2^k binom(n,k)^2 is fixed. For s>=2, M=2^s, Vandermonde gives valuation v2(binomial(M,j))=s-v2(j) for 1<=j<M; the resulting termwise binomial-square expansion proves D_(n+2^s)=D_n mod 2^(s+2) for all n. Direct n=2^s+1 coefficient analysis gives D_(2^s+1)-3=2^(s+2) mod 2^(s+3), extended to odd-multiple shifts; residues handle s=0,1. Half-period witness n=1 excludes smaller periods; b=1 Lengyel Conj4 follows by subtraction. Checked independently 240400 finite shift valuations and 11 moduli; proof, not checks, handles every n,m,h. All D_n odd, v2(0)=infty.

## originality

PASS

Lengyel 2021 expressly poses the shifted Delannoy difference as Conjecture 4; its Theorems 3–4 do not imply the new uniform-all-index translation valuations and minimal global periods. This audit regards the b=1 proof and full global period classification as new best-of-knowledge, while leaving unindexed congruence literature as a risk.

## value

PASS

The exact global minimal dyadic periods and a universal sharp same-index translation witness characterize an arithmetically important lattice-path sequence at all powers of 2. Proving a specified previously published offset case of a dyadic-difference conjecture adds concrete mathematical importance; this is much more than recomputing a finite modular table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
