# Positive-density prime-power divisibility two-cycles anchored at five

## Finding
For each integer \(r\ge2\) and \(k\ge1\), write \(H_r(k)=\sum_{j=0}^{2k}(-r)^j=(r^{2k+1}+1)/(r+1)\). There is a positive-natural-density set of primes \(q\) such that \(q\equiv29\pmod{40}\), \(5\mid H_q(2)\), and \(q\mid H_5(a)\) for some positive \(a\). It suffices to choose \(q\equiv29\pmod{40}\) for which \(-5\) is a fourth power modulo \(q\); set \(a=(\operatorname{ord}_q(-5)-1)/2\).

Additionally, for distinct odd primes \(p,q\) and positive integers \(a,b\), simultaneous divisibilities \(q\mid H_p(a)\) and \(p\mid H_q(b)\) require \(p\equiv q\equiv1\pmod4\).

## Assumptions and scope
All primes are rational. The multiplicative order is taken in \((\mathbb Z/q\mathbb Z)^\times\). Natural density is among rational primes. These statements concern **only divisibility by the first power of each prime**. They do **not** assert that \(5^a q^2\) makes \(\sum_{i=1}^n 1/\gcd(n,i)\) integral. No explicit numerical value for the positive density is claimed.

## Proof
**1. Arithmetic seed.** For \(q=29\), \(4^4\equiv-5\pmod{29}\) because \(4^4=256\equiv24\pmod{29}\). The polynomial \(T^4+5\) has four distinct roots modulo \(29\), as \(29\equiv1\pmod4\). Note also that \(29\equiv29\pmod{40}\).

**2. Positive-density field argument.** Let \(K=\mathbb Q(\zeta_{40},\alpha)\), with \(\alpha^4=-5\) and \(\zeta_{40}\) a primitive fortieth root of unity. This is the splitting field of the two separable polynomials \(T^{40}-1\) and \(T^4+5\), since \(i\in\mathbb Q(\zeta_{40})\). It is Galois over \(\mathbb Q\) and unramified at \(29\) (the only possible ramified rational primes divide \(2\cdot5\)). For any prime of \(K\) above \(29\), the Frobenius \(g\) sends \(\zeta_{40}\) to \(\zeta_{40}^{29}\) and fixes \(\alpha\): all roots of \(T^4+5\) are in \(\mathbb F_{29}\), so its Frobenius fixes each root. The full conjugacy class \(C\) of \(g\) acts on \(\zeta_{40}\) by exponent \(29\), because the cyclotomic Galois group is abelian. It also fixes \(\alpha\): each conjugate of \(\alpha\) is \(i^j\alpha\), and \(g\) fixes both \(i\) and \(\alpha\); consequently every conjugate \(hgh^{-1}\) fixes \(\alpha\). Chebotarev's theorem gives density \(|C|/[K:\mathbb Q]>0\) for primes \(q\) having Frobenius class \(C\). Every such \(q\) satisfies \(q\equiv29\pmod{40}\) and admits a root of \(T^4+5\) in \(\mathbb F_q\).

**3. Producing the mutual divisibilities.** Fix one of these primes \(q\). Since \(q\equiv5\pmod8\), the integer \((q-1)/4\) is odd. As \(-5\) is a fourth power in \(\mathbb F_q\), its order \(d\) divides \((q-1)/4\) and is odd. Because \(q\ge29\), \(-5\not\equiv1\pmod q\), so \(d\ge3\) and \(a=(d-1)/2\ge1\). The geometric-series identity gives \(H_5(a)=\sum_{j=0}^{d-1}(-5)^j\equiv0\pmod q\). In the opposite direction, \(q\equiv29\equiv-1\pmod5\), so \(H_q(2)=\sum_{j=0}^4(-q)^j\equiv5\equiv0\pmod5\).

**4. Reciprocity obstruction.** Suppose distinct odd primes \(p,q\) satisfy \(q\mid H_p(a)\), \(p\mid H_q(b)\). Then \((-p)^{2a+1}\equiv1\pmod q\) and \((-q)^{2b+1}\equiv1\pmod p\). Because these exponents are odd, \(-p\) is a quadratic residue modulo \(q\) and \(-q\) is a quadratic residue modulo \(p\). Let \(u=(p-1)/2\bmod2\), \(v=(q-1)/2\bmod2\). Quadratic reciprocity and the supplementary law give \(1=\left(\frac{-p}q\right)\left(\frac{-q}p\right)=(-1)^{u+v+uv}\). Among \(u,v\in\{0,1\}\), the exponent is even only for \(u=v=0\). Therefore \(p\equiv q\equiv1\pmod4\).

## Verification
The seed can be checked without factorization: \(4^4\bmod29=24\), \(H_5(3)=13021=29\cdot449\), and \(H_{29}(2)=683705=5\cdot136741\). The accompanying `verify.py` checks the seed and further prime witnesses using exact integer arithmetic. The infinite-density result follows from Chebotarev, **not** from the finite tests.

## Relationship to prior work
De Koninck and Letendre [1] study integer values of \(\sum_{i=1}^n1/\gcd(n,i)\) and organize prime-support dependencies into directed graphs, analyzing two-cycles in Section 5. Its prime-power local factor is \(H_r(k)\). The present statement constructs a positive-density family of **mutual prime-divisibility relations across unrestricted exponents**, which is not the same as either full integrality or a two-cycle in the source's cubefree-only component. Chebotarev's theorem [2] supplies the positive-density step.

## Limitations
The constructed exponent \(a\) varies with \(q\), and may exceed two. In the decomposition of [1], large exponents lie in the cubefull component, not necessarily its special cubefree two-cycle component. This result does not show infinitely many integers with integral reciprocal-gcd sum, does not give the density constant, and does not certify novelty beyond inspected indexed literature.

## References
[1] J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^n 1/\gcd(n,i)\)*, arXiv:2610.10572 (first publicly available October 4, 2026), https://arxiv.org/abs/2610.10572 .

[2] Chebotarev density theorem, *Encyclopedia of Mathematics*, https://encyclopediaofmath.org/wiki/Chebotarev_density_theorem .
