# Resolution of the Stern \(22\)–\(27\) dyadic divisibility conjecture

## Finding

Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for integers \(n\geq1\). Define
\[
T(N;m)=\#\{0\leq n<N:m\mid s(n)\}.
\]
For every integer \(r\geq0\),
\[
\boxed{T(2^r;22)=T(2^r;27).}
\]
This resolves the precise open conjecture printed in Reznick's 2006 preprint and 2008 journal paper [1,2]. The shared dyadic-level counts
\[
Z(k)=\#\{2^k\leq n<2^{k+1}:22\mid s(n)\}
\]
(which are also the corresponding counts for modulus \(27\)) have the rational generating function
\[
\sum_{k\geq0}Z(k)z^k=\frac{4z^7-4z^8+8z^9-16z^{10}+32z^{11}}{D(z)},
\]
where
\[
D(z)=1-3z+4z^2-6z^3+9z^4-13z^5+14z^6-18z^7+12z^8-16z^9+32z^{11}-64z^{12}.
\]
Its first sixteen values are \(0,0,0,0,0,0,0,4,8,16,24,52,136,248,464,932\).

## Assumptions and scope

All calculations take place over the integers or the residue rings \(\mathbb Z/22\mathbb Z\) and \(\mathbb Z/27\mathbb Z\). The integer \(r\) and the level index \(k\) may be arbitrarily large and nonnegative. Divisibility includes the zero term \(s(0)=0\). The projective state space for modulus \(m\) consists of pairs \((a,b)\) with \(\gcd(a,b,m)=1\), modulo simultaneous multiplication by an invertible residue modulo \(m\). For \(m=22\), there are \(360\) primitive ordered residue pairs and \(\varphi(22)=10\) units; for \(m=27\), there are \(648\) primitive ordered pairs and \(\varphi(27)=18\) units. A unit fixing a primitive pair fixes a Bézout combination congruent to \(1\) modulo \(m\), so the unit action is free. Both quotients therefore have exactly \(360/10=648/18=36\) states; the checker independently enumerates these quotients. No hypothesis about a prime modulus is used.

## Proof

**1. Exact finite-state model.** Let \(\mathcal P_m\) denote the preceding set of \(36\) projective states, and put
\[
L[a,b]=[a,a+b],\qquad R[a,b]=[a+b,b].
\]
Both maps preserve primitivity and unit-scaling equivalence. On functions \(f:\mathcal P_m\to\mathbb Z\), define
\[
(\mathcal T_m f)(P)=f(LP)+f(RP).
\]
Write \(e_m([a,b])=1\) if \(a=0\pmod m\), and \(0\) otherwise. This definition is independent of the representative because multiplication by a unit preserves vanishing. The dyadic Stern identities give
\[
(s(2n),s(2n+1))=(s(n),s(n)+s(n+1)),
\]
\[
(s(2n+1),s(2n+2))=(s(n)+s(n+1),s(n+1)).
\]
Consequently all binary words of length \(k\), applied by \(L,R\) to \([1,1]\), enumerate the pairs \([s(n),s(n+1)]\) for exactly \(2^k\le n<2^{k+1}\), with multiplicities. Thus
\[
Z_m(k)=(\mathcal T_m^ke_m)([1,1]).
\]
By Cayley–Hamilton for the integer \(36\times36\) matrix of \(\mathcal T_m\), each \(Z_m\) obeys some monic constant-coefficient recurrence of order \(36\) (not necessarily minimal).

**2. Exact order-twelve recurrence certificate.** Consider the polynomial \(D(z)=\sum_{j=0}^{12}c_jz^j\) displayed above, with coefficient tuple
\[
(c_0,\ldots,c_{12})=(1,-3,4,-6,9,-13,14,-18,12,-16,0,32,-64).
\]
For each \(m\in\{22,27\}\) the standalone exact-integer program `stern_22_27_checker.py` constructs all \(36\) projective states, the two transition maps and the output vector, and verifies
\[
\sum_{j=0}^{12}c_jZ_m(k-j)=0\qquad(12\le k\le47).
\]
This finite verification **proves** the relation for every \(k\ge12\): write \(h_m(t)=\sum_{j=0}^{12}c_jZ_m(t+12-j)\). Since \(h_m\) is a linear combination of translates of an output of the same \(36\)-dimensional transfer matrix, Cayley–Hamilton gives it a monic recurrence of order \(36\); its first \(36\) terms, \(h_m(0),\ldots,h_m(35)\), are all zero by the exact check, so induction gives \(h_m(t)=0\) for all \(t\ge0\). No assertion that a finite experiment alone proves an infinite identity is used.

**3. Equality and generating function.** The checker also verifies, by independent integer iteration for both moduli, that
\[
(Z_{22}(0),\ldots,Z_{22}(11))=(Z_{27}(0),\ldots,Z_{27}(11))
=(0,0,0,0,0,0,0,4,8,16,24,52).
\]
The common recurrence in Step 2 gives \(Z_{22}(k)=Z_{27}(k)\) for all \(k\ge0\). Applying the recurrence to the initial values gives the rational generating function above. Finally, because \(s(0)=0\), the disjoint decomposition \([0,2^r)=\{0\}\sqcup\bigcup_{k=0}^{r-1}[2^k,2^{k+1})\) yields
\[
T(2^r;m)=1+\sum_{k=0}^{r-1}Z_m(k),
\]
and hence the claimed equality for every \(r\ge0\).

**4. Direct independent recurrence certificate.** The same program checks equality of all first \(72\) dyadic level counts. The difference of outputs of two \(36\)-state systems is an output of their block-diagonal direct sum, a \(72\)-dimensional integer matrix. Cayley–Hamilton therefore gives a recurrence of order \(72\) for the difference. Its \(72\) initial zero values imply equality forever independently of the particular order-twelve polynomial. This is a separate finite-to-infinite proof route with the same foundational state model.

## Verification

Execute `python3 stern_22_27_checker.py` with the standard Python library. The program deterministically lists primitive pairs and orbits, checks exactly \(36\) states per modulus, evaluates the two transition systems over the integers, tests the \(36\) consecutive recurrence residuals at each modulus, checks the first \(72\) levels directly, and independently constructs the raw Stern row through level \(11\). Its calculations are exact and have no random sampling, symbolic black box, tolerance, or unbounded search. The two independent finite-to-infinite arguments rely on Cayley–Hamilton, not on the size of a finite experiment alone.

## Relationship to prior work

Reznick [1,2] defines the same counting function and explicitly conjectures \(T(2^r;22,0)=T(2^r;27,0)\), reporting verification only up to \(r\le19\). Reznick also states that the separate identities between moduli \(4,5\) and between \(6,9,11\) are proved; those are not claimed here as new. His concluding discussion outlines characteristic-polynomial methods for earlier identities but does not prove the \(22\)–\(27\) case. The present contribution is an actual all-level exact recurrence and proof certificate for the stated unresolved case, plus a concrete rational generating function. The class notes [3] are a potentially pertinent subsequent item that was not materially accessible; no claim of comprehensive historical uniqueness is made.

## Limitations

The proof is a reproducible, finite-state, exact-computation-assisted proof, rather than a short hand-derived factorization of the characteristic polynomials. It establishes this particular modulus pair and its common rational level series, not a general classification of all modulus pairs. The earlier 2012 class notes [3] were identified but not inspected in full, leaving a residual priority/coverage risk. The verification and literature comparison have not undergone independent auditing.

## References

[1] Bruce Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, arXiv:math/0610601v1, first submitted 19 October 2006, especially introduction equation (1.15) and discussion at end of Section 5, https://arxiv.org/pdf/math/0610601.

[2] Bruce Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, Journal of Integer Sequences 11 (2008), https://cs.uwaterloo.ca/journals/JIS/VOL11/Reznick/reznick4.pdf.

[3] Bruce Reznick, *A Stern Introduction to Combinatorial Number Theory*, University of Illinois class notes (2012), cited in subsequent scholarship; primary text not available in the present comparison.
