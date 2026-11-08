# Independent mathematical audit

## correctness

PASS

Let q=2^s. For odd prime p, every intermediate coefficient binom(p,k)^r is divisible by p^2 since r>=2. Using binom(2p,p)=2 prod(1+p/j) and reciprocal pairing gives binom(2p,p)=2 mod p^2. Translated H(Y)=q^p B((Y-1)/q) has H(Y)=qY^p mod p, with leading p-unit. Its constant term is q(2^(s(p-1))-1) mod p^2; the non-Wieferich hypothesis v_p(2^(p-1)-1)=1 together with p not dividing s makes this divisible by p but not p^2. Eisenstein applies and invertible affine transformation preserves irreducibility. No inference about Wieferich primes, p=2, composite index or infinitely many non-Wieferich primes. Independently tested 105 Eisenstein polynomials and 1620 coefficients.

## originality

PASS

Sun, Guo-Zeng and Pan study Apéry polynomial congruences, and OEIS records the stronger conjecture of irreducibility for every n. This work proves a stated subset indexed by non-Wieferich prime n, not the conjecture in full. The shift-Eisenstein method is transparent but nontrivial to discover; a broad irreducibility theorem in polynomial literature might subsume this family and remains a historical-priority risk.

## value

PASS

The source conjectures irreducibility for two classical Apéry polynomial families at all indices. A proven arithmetic subfamily of both is a mathematically motivated partial advance; the general (r,s) extension and explicit affine Eisenstein shift provide a reusable proof principle. No unsupported infinitude claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
