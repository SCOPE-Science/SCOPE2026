# Exact extinction clocks for prime-power toroidal Laplacian cellular automata

## Finding

For every prime \(p\) and integers \(a\ge b\ge1\), the nearest-neighbor discrete Laplacian on the rectangular periodic torus \(G=\mathbb Z/p^a\mathbb Z\times\mathbb Z/p^b\mathbb Z\), with values in \(\mathbb F_p\), is nilpotent with *exact* index
\[
T(p;a,b)=\begin{cases}
2^{a-1},&p=2,\\[2pt]
(p^a+p^b)/2,&p\text{ odd}.
\end{cases}
\]
Here exact means that the time-\(T\) update vanishes on every configuration and the time-\(T-1\) update is nonzero.

For odd \(p\), the last nonzero update has rank one and is completely explicit. For every configuration \(f:G\to\mathbb F_p\) and every \(z\in G\),
\[
(\Delta^{T-1}f)(z)=(-1)^{b(p-1)/2}\sum_{w\in G}f(w).
\]
Precisely \((p-1)p^{p^{a+b}-1}\) configurations survive to time \(T-1\), and all others vanish by time \(T-1\). Thus the odd-characteristic extinction clock depends on both side lengths, while its characteristic-two counterpart depends only on the larger side length.

## Assumptions and scope

Let \(p\) be any prime and \(a,b\) integers satisfying \(a\ge b\ge1\). Points of \(G\) have cyclic coordinates \((i,j)\). Define a simultaneous update on the vector space \(\mathbb F_p^G\) by
\[
(\Delta f)(i,j)=f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)-4f(i,j).
\]
All additions of coordinates are modulo the appropriate side length and all values are reduced modulo \(p\). Repeated neighbors on a two-site cyclic side occur with their multiplicity; this convention is essential in characteristic two. Set \(\Delta^0=I\). The universal extinction time is the least integer \(T\ge1\) such that \(\Delta^T=0\) as an operator on *all* configurations.

The statement concerns *constant-modulus linear* cellular automata with periodic boundaries of precisely the indicated prime-power sizes. It does not assert transient decay on the infinite lattice, nor does it cover arbitrary ring sizes or changing-modulus schedules.

## Proof

**1. A truncated-polynomial representation.** Write \(m=p^a\), \(n=p^b\). Convolution by the Laplacian corresponds to multiplication by
\[
P=X+X^{-1}+Y+Y^{-1}-4
\]
in \(R=\mathbb F_p[X^{\pm1},Y^{\pm1}]/(X^m-1,Y^n-1)\). Put \(u=X-1\), \(v=Y-1\). Frobenius gives \(X^m-1=(X-1)^m\), and similarly for \(Y\). Consequently,
\[
R\simeq \mathbb F_p[u,v]/(u^m,v^n),\qquad
P=\frac{u^2}{1+u}+\frac{v^2}{1+v}=:A+B.
\]
Both denominators are units of the truncated ring, so the displayed fractions mean finite inverse-polynomial expansions. In particular,
\[
A^j=0\iff 2j\ge m,\qquad
B^k=0\iff2k\ge n.
\]

**2. An exact criterion for a surviving iterate.** Define \(h_m=\lfloor(m-1)/2\rfloor\), \(h_n=\lfloor(n-1)/2\rfloor\). For every integer \(t\ge0\), the binomial expansion
\[
P^t=\sum_{j+k=t}\binom{t}{j}A^j B^k
\]
is nonzero precisely when there exist integers \(j,k\ge0\) with \(j+k=t\), \(j\le h_m\), \(k\le h_n\), and \(\binom{t}{j}\not\equiv0\pmod p\). To prove the nontrivial direction, take any such pair and inspect the coefficient of \(u^{2j}v^{2k}\): it is exactly \(\binom{t}{j}\), since all unit denominators have constant term one. A different pair \((j',k')\) with \(j'+k'=t\) could contribute at that bidegree only if \(j'\le j\) and \(k'\le k\), hence only if \((j',k')=(j,k)\). No cancellation is possible. Conversely, when every allowed binomial coefficient is zero, the whole polynomial is zero. By Lucas's theorem, the binomial coefficient is nonzero modulo \(p\) precisely when the base-\(p\) addition of \(j\) and \(k\) has no carry.

**3. The exact maximal surviving time.** For odd \(p\), both \(m,n\) are odd, so \(h_m=(m-1)/2\), \(h_n=(n-1)/2\). Any surviving \(t=j+k\) is at most
\[
h_m+h_n=(m+n)/2-1.
\]
Equality is attained by \((j,k)=(h_m,h_n)\): in base \(p\), each of the \(a\) digits of \(h_m\) is \((p-1)/2\), and similarly for the \(b\) digits of \(h_n\). Their addition is carry-free, since \((p-1)/2+(p-1)/2=p-1\) in the overlapping positions. Thus the last surviving time is \((m+n)/2-1\), and \(T=(m+n)/2\).

For \(p=2\), each admissible \(j\) satisfies \(j\le2^{a-1}-1\) and each admissible \(k\) satisfies \(k\le2^{b-1}-1\). A carry-free binary sum of two such integers has no set bit at position \(a-1\) or above, so \(t\le2^{a-1}-1\). This bound is attained by \(j=2^{a-1}-1\), \(k=0\), with no carry. Hence \(T=2^{a-1}\), including the boundary \(a=b=1\).

**4. The last-step image in odd characteristic.** At the maximal surviving time \(t=h_m+h_n\), the inequalities \(j\le h_m\), \(k\le h_n\) force the unique pair \((j,k)=(h_m,h_n)\). In \(R\),
\[
A^{h_m}=u^{m-1},\qquad B^{h_n}=v^{n-1},
\]
because multiplying the top-degree monomials by a power-series unit retains only its constant term. The characteristic-\(p\) geometric-sum identity gives
\[
u^{m-1}=\sum_{r=0}^{m-1}X^r,\qquad v^{n-1}=\sum_{s=0}^{n-1}Y^s.
\]
Lucas's theorem applied to the base-\(p\) digits of \(h_m,h_n\) yields
\[
\binom{h_m+h_n}{h_m}\equiv
\prod_{\ell=1}^{b}\binom{p-1}{(p-1)/2}
=(-1)^{b(p-1)/2}\pmod p,
\]
where \(\binom{p-1}{r}\equiv(-1)^r\pmod p\). Therefore
\[
P^{T-1}=(-1)^{b(p-1)/2}\left(\sum_{r=0}^{m-1}X^r\right)
\left(\sum_{s=0}^{n-1}Y^s\right).
\]
Convolution by the full group sum sends every function to the constant function equal to its total mass. This proves the rank-one identity. The total-mass functional is nonzero and its kernel has codimension one in the \(mn=p^{a+b}\)-dimensional vector space. Exactly \((p-1)p^{mn-1}\) configurations therefore have a nonzero terminal image. All stated conclusions follow.

## Verification

The accompanying standalone script `artifacts/verify.py` uses direct periodic cell-by-cell stencil updates, not the truncated-polynomial proof implementation. It tests 19 prime-power torus parameter triples, including characteristic two, primes \(3,5,7,11\), asymmetric side lengths, and two-site cyclic sides. For each triple it checks that a unit impulse is nonzero at every time before the stated extinction time and becomes exactly zero at that time. For odd primes it independently checks every value of the terminal impulse image and several additional initial arrays. It prints `VERIFY_OK` on success. Finite tests do not prove the infinite-parameter theorem; the algebraic argument above does.

## Relationship to prior work

Nowak-Kępczyk's work on modular Laplacian cellular automata derives Frobenius revival identities for prime-modulus dynamics, works with extended or expanding lattices, and treats recovery and special moving-corner periods. The earlier study of stabilization and periodicity also treats lattice pattern dynamics and mentions finite-torus eventual periodicity. These are motivations and background, **not** assertions of new Frobenius theory.

The publicly available *Prime-power digit factorization in modular Laplacian dynamics* establishes a general prime-power polynomial renormalization on lattice Laurent-polynomial systems. It does not give the finite periodic prime-power torus's exact nilpotency index or the odd-prime terminal rank-one operator. Its congruences are not presented here as discoveries. The result above concerns a specific geometric Laplacian and periodic quotient, where nilpotence and its exact duration depend on the quotient relations.

The algebraic steps are based on standard finite-field Frobenius and Lucas identities. Their use as ingredients is acknowledged rather than claimed to be novel. The claimed contribution is the complete sharp torus extinction and terminal-state classification for every prime and both side exponents, under the precise operator definition above.

## Limitations

The theorem is for the standard four-neighbor Laplacian with multiplicities on two cyclic prime-power factors, over the field of the *same* characteristic. It does not imply the same clock for different masks, arbitrary ring sizes, finite fields of different characteristic, or composite coefficient moduli. The rank-one terminal image is specifically an odd-prime statement. Historical priority may be affected by older literature on modular graph Laplacians, finite-group convolution rings, or linear cellular automata described with different notation.

## References

1. M. Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata: Replication, Entropy, and Information Recovery*, arXiv:2511.17389, first public version 2025-11-21, revised 2026-10-12. https://arxiv.org/abs/2511.17389
2. M. Nowak-Kępczyk, *Stabilization and Regaining Periodicity in Modular Laplacian Dynamics*, arXiv:2509.05815, first posted 2025-09-06. https://arxiv.org/abs/2509.05815
3. *Prime-power digit factorization in modular Laplacian dynamics*, publicly available mathematical finding, 2026. https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-prime-power-digit-factorization-modular-laplacian--c49cdde3a491
4. É. Lucas, *Théorie des Fonctions Numériques Simplement Périodiques*, American Journal of Mathematics 1 (1878), 184–196, 197–240, 289–321; Lucas's classical binomial congruence.
