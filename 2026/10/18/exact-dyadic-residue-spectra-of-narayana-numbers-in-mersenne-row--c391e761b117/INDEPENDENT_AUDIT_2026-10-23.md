# Independent mathematical audit

## correctness

PASS

For all r>=s>=2 with n=2^r−1, t=2^{r−s+1}, B=2^{s−1}, M=2^s, use binom(n,k)=(-1)^k product_{j=1}^k(1−2^r/j) in Z_2. Every j not divisible by t has v2(2^r/j)>=s so its factor is 1 mod M. The only nontrivial j=mt,1<=m<B, yield w_m=1−2^{s−1−v2(m)} oddpart(m)^−1 mod M; cumulative F_j. Since n^−1=−1 mod M, Narayana(n,k)=n^−1 binom(n,k)binom(n,k+1) reduces to adjacent F_floor(k/t)F_floor((k+1)/t). Each of B blocks has t−1 interior positions with squared F, and there are B−1 boundaries F_{m−1}F_m; last terminal k=n excluded, giving exact total Bt−1. Directly computed w=(9,13,9,15,9,5,9) mod16, F=(1,9,5,13,3,11,7,15), squared (1,1,9,9,9,9,1,1), boundaries (9,13,1,7,1,13,9): hence precisely 1 and 9 each 2^{r−1}−2, 13 twice at k=2t−1,6t−1, and 7 once at k=4t−1. Independently recomputed actual binomial Narayana integers and residues for r=2..9, s<=min(r,6), each target; infinite r,s covered algebraically.

## originality

PASS

Bóna–Sagan 2005 proves prime divisibility of Narayana numbers and in particular oddness for these Mersenne rows. Andreica 2013 supplies modular binomial computation algorithms, not a uniform complete row-residue spectrum. The exact finite-factor all-r,s histogram and locations of the sparse mod-16 exceptions are additional structure. Eu–Liu–Yeh 2006 is a plausible combinatorial congruence source; only abstract material was accessible, and authorized Oxford request returned vpn_disconnected. Best-of-knowledge PASS retains this risk instead of asserting absence of overlap from unavailable full text.

## value

PASS

Narayana rows are natural enumerative objects; classifying all residues and their exact multiplicities at arbitrary fixed binary precision is a meaningful self-contained full classification, not just a few values. The exceptionally sparse mod-16 values have precise index locations, providing usable refined information far beyond parity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
