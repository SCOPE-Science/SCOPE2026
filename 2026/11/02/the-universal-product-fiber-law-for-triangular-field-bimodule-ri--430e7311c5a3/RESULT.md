# The universal product-fiber law for triangular field-bimodule rings and a center-blindness pair

## Finding
Let \(K,L\) be finite fields of the same characteristic, \(M\ne0\) a finite unital \((K,L)\)-bimodule, and put \(Q=|K|\), \(T=|L|\), \(m=|M|\). In the triangular ring \(R=R(K,M,L)\), identify elements with triples and write
\[
(a,v,c)(x,y,z)=(ax,ay+vz,cz).
\]
For a target \((u,v,w)\), let \(N_R(u,v,w)\) count ordered pairs whose product is this target. Define \(c_s(t)=2s-1\) when \(t=0\) and \(c_s(t)=s-1\) when \(t\ne0\), for elements of a field of order \(s\). Then
\[
N_R(u,v,w)=m c_Q(u)c_T(w)+\mathbf1_{u=w=0}QT\left(m^2\mathbf1_{v=0}-m\right).
\]
This is the complete multiplication-fiber law, not merely the zero-product probability; division by \((QTm)^2\) gives the product probability at each target. All finite unital bimodule structures with the same \(Q,T,m\) give the same pointwise count under a set identification preserving zero in the off-diagonal coordinate.

There exist two nonisomorphic unital rings of order \(256\) with identical target-by-target product-fiber counts under a natural coordinate identification, but with centers of sizes \(4\) and \(2\). Thus multiplication-fiber statistics do not determine the center, even among radical-square-zero triangular finite rings with two field factors.

## Assumptions and scope
A unital \((K,L)\)-bimodule is an additive abelian group \(M\) with commuting unital left \(K\)- and right \(L\)-actions. A nonzero such finite bimodule requires the fields to have the same characteristic. The triangular multiplication is associative and has identity \((1,0,1)\). The strict-upper-triangular ideal \(\{(0,v,0):v\in M\}\) has square zero; the semisimple quotient is \(K\times L\). No commutativity of \(R\) is assumed.

## Proof
For a finite field of order \(s\), the equation \(ab=t\) has exactly \(s-1\) ordered solutions if \(t\ne0\), and exactly \(2s-1\) if \(t=0\): for nonzero \(t\) choose any nonzero \(a\), while for zero use the union of the two coordinate axes.

Fix a target \((u,v,w)\). There are \(c_Q(u)c_T(w)\) choices of diagonal variables \((a,x,c,z)\) satisfying \(ax=u\), \(cz=w\). The middle equation is \(ay+bz=v\) with \(y,b\in M\). If \(a\ne0\), the left action of \(a\) is bijective, so this equation has exactly \(m\) solutions. The same holds if \(z\ne0\), by bijectivity of right multiplication by \(z\). In the remaining case \(a=z=0\), the equation becomes \(0=v\), giving exactly \(m^2\) solutions when \(v=0\) and none otherwise. Such exceptional diagonal choices exist only if \(u=w=0\), and their number is \(QT\) because \(x\in K,c\in L\) are then unrestricted. Starting with the uniform \(m\) middle solutions and replacing those \(QT\) exceptional choices gives the displayed formula. The argument is exact for every permitted field and bimodule.

For the nonisomorphism example, put \(F=\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), and \(M=F\oplus F\). Both rings have the standard left action \(a\cdot(u_1,u_2)=(au_1,au_2)\). For \(R_0\), use the standard right action \((u_1,u_2)\cdot c=(u_1c,u_2c)\). For \(R_1\), use \((u_1,u_2)\cdot c=(u_1c,u_2c^2)\). Squaring is a unital field automorphism of \(F\), so the latter defines another associative unital bimodule. Both rings have \(4\cdot16\cdot4=256\) elements. The universal formula gives the same four product-fiber multiplicities for both: \(144\) targets have \(144\) factorizations each; \(96\) targets have \(336\); \(15\) have \(528\); and the zero target has \(4624\). These account for all \(256^2=65536\) ordered pairs.

To calculate each center, let \(e=(1,0,0)\). Commutation with \(e\) forces the off-diagonal component of any central element to be zero. Such a diagonal element \((a,0,c)\) commutes with all diagonal elements automatically. It commutes with every \((0,y,0)\) exactly when \(ay=yc\) for all \(y\in M\). In \(R_0\), this forces \(a=c\) and leaves four choices. In \(R_1\), the first coordinate forces \(a=c\), and the second forces \(a=c^2\); hence \(a=c\in\mathbb F_2\), giving two choices. Therefore \(|Z(R_0)|=4\ne2=|Z(R_1)|\); in particular, these rings are not isomorphic.

## Verification
The standalone program `verify_product.py` enumerates all \(65536\) ordered products in each of the two \(256\)-element rings using an explicit bit-polynomial implementation of \(\mathbb F_4\). For each target it checks the exact general formula and checks that the two entire fiber-count functions coincide. It also enumerates each center by direct commutation with all ring elements, obtaining four and two. The recorded output is `verify_output.txt`; its final line is `FIBERS_EQUAL_EXACTLY; VERIFY_OK`. Exhaustion verifies these two finite examples; the universal field/bimodule result is established by the symbolic argument above.

## Relationship to prior work
David Dolžan, *The multiplication probability of a finite ring* (first public arXiv version April 17, 2025, arXiv:2504.12886), develops the same fixed-target probability invariant. Its Section 3 explicitly treats matrix/simple rings; its Section 4 treats local rings, including local rings with radical square zero. The inspected introduction and Sections 2–4 do not give this nonlocal triangular-bimodule formula or exhibit an equal-product-statistics, unequal-center ring pair. The elementary factorization-count identity in Section 2 is a conceptual antecedent, not the stated triangular classification. A separate published research record on Kronecker path algebras studies commutator fibers rather than multiplication fibers. A broader, unlocated ring-theoretic enumeration could imply this result; historical priority is not independently certified.

## Limitations
This result concerns triangular rings with two finite-field diagonal corners and a unital off-diagonal bimodule. It does not classify product distributions of arbitrary finite rings or prove this example has minimal possible cardinality. The pointwise comparison uses the displayed coordinate identifications and does not assert an isomorphism of multiplication tables. No independent mathematical audit has been performed.

## References
- D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886 (first posted 2025-04-17), https://arxiv.org/abs/2504.12886 .
- *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, published mathematical research record, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d3f (distinct commutator invariant).
