# The arithmetic reduction spectrum of a five-tacnode three-conic arrangement
## Finding
Consider the reduced divisor \(D=V(Q_0Q_+Q_-)\subset\mathbb P^2_{\mathbb Z}\) defined by the primitive integral equations
\[
Q_0=x^2+y^2-z^2,\qquad Q_+=4x^2+5y^2+4yz,\qquad Q_-=4x^2+5y^2-4yz.
\]
These are the three conics of the example with parameters \(\ell=2\) and \(m=-2\) in Măcinic–Pokora, Section 3. Let \(D_p\) denote the *reduced support* after base change to an algebraic closure of \(\mathbb F_p\). For every odd prime \(p\), all three conics are smooth and distinct and every singular point lies on exactly two components. The singular-support classification is complete:

| Characteristic | \(A_1\) nodes | \(A_3\) (contact two) | \(A_7\) (contact four) | Geometric support points |
|:--|--:|--:|--:|--:|
| \(p\ge7\) | 2 | 5 | 0 | 7 |
| \(p=3\) | 2 | 1 | 2 | 5 |
| \(p=5\) | 0 | 6 | 0 | 6 |

An \(A_{2m-1}\) point here means two *smooth* branches with local intersection multiplicity \(m\). For every odd characteristic this is also the usual analytic equation \(u^2-v^{2m}=0\) after a formal change of coordinates and scaling. Thus the only exceptional odd primes for the characteristic-zero singularity basket of this fixed model are precisely \(3\) and \(5\).

All seven characteristic-zero support points are defined over the biquadratic field \(K=\mathbb Q(\sqrt{-3},\sqrt{-5})\), which is the minimal field defining all of them; the Galois-orbit lengths are \(1,2,2,2\). For every prime \(p\ge7\), the number of \(\mathbb F_p\)-rational points of the geometric singular support is
\[
N_p=1+4\mathbf1_{(-3/p)=1}+2\mathbf1_{(-5/p)=1},
\]
where parentheses denote the quadratic character. The four possible counts \(1,3,5,7\) occur with natural prime densities \(1/4\) each. The exceptional counts are \(N_3=5\) and \(N_5=2\).

## Assumptions and scope
All projective points, singularities, and local intersection multiplicities in the geometric classification are taken over an algebraic closure of the indicated prime field. A rational support point is a closed geometric singular point fixed by its prime-field Frobenius, not a rational tangent branch or a nonreduced scheme length. The fixed primitive integral equations are part of the assertion. The characteristic-zero Galois claim is over \(\mathbb Q\). Characteristic two is excluded: the three equations become squares and do not give three smooth reduced conics. Freeness, plus-one generation, and graded syzygies in positive characteristic are not asserted.

## Proof
**Smooth components and complete pairwise intersections.** For odd characteristic, the symmetric matrices of \(Q_0,Q_+,Q_-\) have determinants \(-1,-16,-16\), so all three are smooth; their defining quadrics are distinct. The exact integer identities
\[
Q_+-4Q_0=(y+2z)^2,\quad Q_--4Q_0=(y-2z)^2,\quad Q_+-Q_-=8yz
\]
locate all intersections. The first two identities give the two degree-four intersection schemes supported on
\[
Q_0\cap Q_+:\ [\pm\sqrt{-3}:-2:1],\qquad Q_0\cap Q_-:\ [\pm\sqrt{-3}:2:1].
\]
Indeed \(z=0\) is impossible because \(y=\mp2z\) would force \(x=0\), so the displayed affine chart is exhaustive. For \(p\ne3\) each of the two points in each pair is distinct and has local intersection multiplicity two. For \(p=3\) the pairs respectively coalesce at \([0:1:1]\) and \([0:1:2]\), with local multiplicity four each. For example in the first case let \(y=1\), \(z=1+Z\), \(x=X\). In characteristic three the two local equations are \(Q_+=X^2+Z\) and \(Q_0=X^2+Z-Z^2\); hence their completed local intersection algebra is \(\overline{\mathbb F}_3[[X]]/(X^4)\), of length four. Replacing \(z\) by \(-z\) proves the second case.

For the last pair, since \(8\) is invertible in every odd characteristic, \(Q_+\cap Q_-\) is contained in \(yz=0\). The line \(y=0\) gives the single point \([0:0:1]\), with intersection multiplicity two, while \(z=0\) gives \([\pm\sqrt{-5}:2:0]\). For \(p\ne5\) these are two distinct transverse nodes; when \(p=5\) they coalesce at \([0:1:0]\) with intersection multiplicity two. The local algebra there is \(\overline{\mathbb F}_5[[X,Z]]/(Z,X^2)\). The point \([0:0:1]\) is always a contact-order-two point, as the local equations on \(z=1\) reduce to \((y,x^2)\) upon subtracting them. For each pair, its intersection multiplicities sum to \(4\), as Bézout requires.

**No three branches and singularity types.** At \([0:0:1]\), \(Q_0=-1\); at \([\pm\sqrt{-5}:2:0]\) and its characteristic-five limit, \(Q_0=-1\); at either \(Q_0\cap Q_+\) point the other quadratic is \(Q_-=-8yz\), which equals \(16\) on \(y=-2z\); similarly \(Q_+=16\) on \(y=2z\). Each is nonzero in odd characteristic, so no triple component intersections occur. A reduced divisor of two smooth plane branches with intersection multiplicity \(m\) has local analytic form \(A_{2m-1}\) when the characteristic differs from two (the local equations can be chosen \(u=0\) and \(u-v^m=0\), then complete a square). This proves the singularity baskets and shows the exceptional set is exactly \(\{3,5\}\). In each case the sum of delta invariants is \(12\), in agreement with the degree-six arithmetic genus: \(10=12-3+1\).

**Splitting field and point counts.** In characteristic zero the one rational singular point is \([0:0:1]\). The other six form three conjugate pairs: two pairs involve \(\sqrt{-3}\), one involves \(\sqrt{-5}\). Neither field \(\mathbb Q(\sqrt{-3})\) nor \(\mathbb Q(\sqrt{-5})\) contains the other, so their compositum \(K=\mathbb Q(\sqrt{-3},\sqrt{-5})\) is the exact degree-four common splitting field. For any prime \(p\ge7\), the reductions remain seven distinct points, and the two pairs depending on \(\sqrt{-3}\) (four points) are rational exactly when \((-3/p)=1\); the pair depending on \(\sqrt{-5}\) is rational exactly when \((-5/p)=1\). The remaining point is always rational. At \(p=3\), the two quadruple-contact points and the two nodes are rational; at \(p=5\), the two coalesced contact points on \(Q_+\cap Q_-\) are rational but the four remaining contact points are not. Since \(K/\mathbb Q\) is biquadratic, Chebotarev gives density \(1/4\) to each of its four Frobenius classes and hence to each of the four rational counts.

## Verification
The accompanying `verify.py` uses exact polynomial identities and symmetric-matrix determinants, verifies explicit local normal forms in characteristics three and five, and independently enumerates every point of \(\mathbb P^2(\mathbb F_p)\) for every odd prime \(p\le151\) to check the point-count formula. It prints `VERIFY_OK` on success. The proof of the universal assertions is the polynomial and Bézout argument above; the finite-field enumeration is an independent check, not an infinite-prime proof.

## Relationship to prior work
Măcinic and Pokora display the same three-conic example over \(\mathbb C\), with five tacnodes, two nodes, and its plus-one-generated property. Their choice of parameters originates in Megyesi's complex geometric normal forms for three conics with five tacnodes. Dimca–Janasz–Pokora and Bromboszcz–Jarosławski–Pokora study the complex geometry and homological/combinatorial constraints of conic arrangements with tacnodes. The new statement concerns arithmetic descent and every odd-characteristic reduction of this *specific integral presentation*: its exact exceptional prime set, contact-order jumps, rational singular support, and Galois splitting. Those arithmetic assertions are not inferred from the characteristic-zero tables alone.

## Limitations
Characteristic two is excluded. The theorem concerns only this fixed integral model and singular-support point counts, not arbitrary integral changes of projective coordinates, logarithmic derivation modules in positive characteristic, or finite-field counts of scheme-theoretic singularity lengths. Published and historical sources may contain unindexed arithmetic observations; the 2000 Megyesi full text was not available for comprehensive comparison, so no absolute priority claim is made.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228, Section 3, three-conic example (first public 2023-09-26).
2. A. Dimca, M. Janasz, and P. Pokora, *On plane conic arrangements with nodes and tacnodes*, arXiv:2108.04004 (2021).
3. A. Bromboszcz, B. Jarosławski, and P. Pokora, *On plus-one generated arrangements of plane conics*, arXiv:2507.23024 (2025).
4. G. Megyesi, *Configurations of conics with many tacnodes*, Tohoku Math. J. 52 (2000), 555–577, DOI:10.2748/tmj/1178207755 (comparison limited to accessible abstract and metadata).
