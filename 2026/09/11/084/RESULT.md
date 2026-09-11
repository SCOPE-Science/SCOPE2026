# Prime-denominator simultaneous ubiquity for shift (phi^-1, pi^-1): full-measure theorem

## Context and motivation

Classical metric simultaneous Diophantine approximation (Khintchine-Groshev, Beresnevich-Dickinson-Velani ubiquity, Kim without-monotonicity) decides full versus null Lebesgue measure over all denominators. Restricting denominators to primes thins resonant mass from polynomial to Mertens log-log growth, so full-denominator divergence implies nothing about primes. Pollington-Velani thin-denominator work covers lacunary and smooth sequences, while Baier-Ghosh and Harman prime-constrained work requires prime numerators and proves small exponents on lines. No prior source states a prime-denominator inhomogeneous simultaneous full-measure theorem for a fixed planar shift at the Dirichlet exponent. This record closes that gap for the natural shift gamma=(phi^-1,pi^-1) with psi(q)=(q+1)^-1/2.

## Definitions

Let phi=(1+sqrt(5))/2, gamma=(phi^-1,pi^-1)=((sqrt(5)-1)/2,1/pi) in R^2, and psi(q)=(q+1)^-1/2 for q>=1. Work on the 2-torus T^2=[0,1]^2 with Lebesgue measure m2 and max-norm distance ||.||_infty to Z^2. For each prime p>=1000 define

E_p = { x in T^2 : ||p x - gamma||_infty < psi(p) (mod 1) },

the union of the p^2 shifted max-norm squares of side 2psi(p)/p centred at (a+gamma)/p, a in {0,...,p-1}^2. Let W = limsup_{p prime -> infinity} E_p, the prime-restricted simultaneously approximable set.

## Result (headline claim)

For gamma and psi as above, m2(W) = 1: the prime-restricted simultaneously approximable set has full Lebesgue measure on T^2.

## Proof / evidence

Step 1 (single-prime mass). For p>=1000, 2psi(p)<1 so radii psi(p)/p<1/(2p) while centre separations lie in (1/p)Z^2; the p^2 squares are pairwise disjoint. Hence m(E_p)=p^2*(2psi(p)/p)^2=4psi(p)^2=4/(p+1)=:m_p, and S(X):=sum_{1000<=p<=X} m_p diverges like prime-reciprocal (Mertens) since 1/(p+1)>=1/(2p).

Step 2 (pairwise overlap). Write G_p(z)=1_{[-psi(p),psi(p)]^2}(z) periodised so E_p={x:G_p(px-gamma)=1}. One-dimensional Fourier factors d_k=2psi(p) (k=0), sin(2pi k psi)/(pi k) else, with |d_k|<=min(2psi(p),1/(pi|k|)). Since f_p(x)=G_p(px-gamma) has frequencies only in pZ^2, for distinct primes p,q common frequencies satisfy pk=qj iff (k,j)=(qt,pt). The shift phases e(-k.gamma) have modulus 1, so uniformly in gamma: |m(E_p cap E_q)-m_p m_q|<=R_{p,q}:=(8/3)psi(p)psi(q)/(pq)+1/(9p^2q^2) (both-nonzero t gives 1/(9p^2q^2); each one-zero class gives (4/3)psi_p psi_q/(pq) using sum_{n!=0}n^-2=pi^2/3).

Step 3 (uniform tail error). psi(p)/p<=p^-3/2, so T:=sum_{p>=1000} psi(p)/p<=sum_{n>=1000}n^-3/2<=1000^-3/2+2/sqrt(1000)<=0.0633. Hence sum_{p,q>=1000} R_{p,q}<=(8/3)T^2+(1/9)U^2=:C0<=0.0107 with U=sum 1/p^2 tiny, uniformly over all tails.

Step 4 (Chung-Erdos to limsup). sumsum_{1000<=p,q<=X} m(E_p cap E_q)<=S(X)^2+S(X)+C0. Chung-Erdos gives m(union_{p<=X} E_p)>=S(X)^2/(S(X)^2+S(X)+C0)->1 as S(X)->infinity. Restarting at any Y>=1000 with the same uniform C0, every tail union has full measure, so W=intersection_Y union_{p>=Y} E_p has m2(W)=1. Overlap loss S+C0<=S^2/2 once S>=1+sqrt(1+2C0) approx 2.01.

Finite certified ledger (replay output/artifacts/verify_prime_ubiquity.py): sieve primes in [1000,3.5e6] gives S=sum 4/(p+1)=3.103655>=3; max 2psi=0.0629<1; C0<=0.010678; half-loss 3.114<=4.816; Chung-Erdos ratio>=0.7557 tending to 1. Output VERIFY_OK.

## Limitations

Max-norm squares on T^2 (Euclidean disks differ only by constant pi vs 4). The finite ledger certifies ratio 0.7557 on [1000,3.5e6] with limit 1 by divergence. Proof uses only coprimality of distinct primes, not deep sieve rates, and is uniform in the shift (irrationality of coordinates used for naturality only). No Hausdorff-measure refinement is claimed.

## Reproducibility

Run `python3 output/artifacts/verify_prime_ubiquity.py` (stdlib only, seconds to minutes): sieves to 3.5e6, checks ledger S1>=3, disjointness, 1D Fourier spot-checks, tail constant, Chung-Erdos ratio and half-loss, printing VERIFY_OK.

## References

- Beresnevich-Dickinson-Velani, Measure theoretic laws for limsup sets, Mem. AMS 2006; Beresnevich-Velani, Khintchine-Groshev revisited, IMRN 2010.
- Seongmin Kim, Inhomogeneous Khintchine-Groshev without monotonicity, arXiv:2411.07932; Khintchine inhomogeneous simultaneous with polynomial decay, arXiv:2604.22689.
- Pollington-Velani-Zafeiropoulos-Zorin, Inhomogeneous approximation on M0-sets with restricted denominators, arXiv:1906.01151.
- Baier-Ghosh, lines with prime constraints arXiv:1309.5296; Restricted simultaneous approximation arXiv:1503.07107; Inhomogeneous with prime constraints, Proc. Math. Sci. 128:44 (2018).
- Harman, Simultaneous Diophantine Approximation with Primes, JLMS s2-39.3.405 (1989).
