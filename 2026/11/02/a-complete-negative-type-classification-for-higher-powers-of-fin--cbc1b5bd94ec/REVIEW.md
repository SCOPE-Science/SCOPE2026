# Independent mathematical audit

## correctness

PASS

The graph power metric is d(u,v)=ceil(min(|u−v|,n−|u−v|)/k). The symmetric circulant distance matrix has nonconstant eigenvalues λ_j=−sum_{r=0}^{h−1}sin((2rk+1)πj/n)/sin(πj/n), with h=ceil(floor(n/2)/k) and removable cases separately −h. CND requires all λ_j<=0. Complete graph n=2k+1 and cocktail-party n=2k+2 are admitted. Exact sine signs of frequencies j=2/3 (or specified modes) exclude all other n<=4k+3, except listed four. For k>=4 and n>=4k+4, an explicit six-site induced matrix T with zero-sum w=(2,-2,-2,3,-3,2) has w^T T w=2; for k3 n>=22, twelve consecutive-site weights yield +2. The four exceptions have exact zero frequency/nullities listed in RESULT.md; independent Fourier calculation for k3..13 and n<8k+16 reproduces the admitted list and zero modes. Schoenberg and centered rank establish kernel and squared-Euclidean consequences. Finite loop alone is not universal: the local certificates and finite interval Fourier sign proofs are necessary.

## originality

PASS

Sánchez 2011 provides general finite negative-type algebraic tests but not this exhaustive arithmetic list. Sander–Sander compute adjacency spectra of graph powers, not their transformed shortest-path distance spectra. Lin et al. characterize recognition of cycle/path powers, not negative-type metrics. General distance-spectral surveys may include partial diameter-two facts; these do not derive uniform large-order obstructions or the four exceptional k,n pairs. Resultary related graph records found no directly covering classification.

## value

PASS

This is a complete natural decision classification for Hilbert-squared embeddability and all-scale Gaussian positivity of graph-power shortest-path metrics. The four sporadic survivors, their exact small embedding dimensions, and uniform finite obstruction certificates distinguish an entire infinite graph family rather than a small sample of numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
