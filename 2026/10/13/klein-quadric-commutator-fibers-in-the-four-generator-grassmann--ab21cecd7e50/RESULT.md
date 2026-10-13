# Klein-quadric commutator fibers in the four-generator Grassmann algebra

## Finding

Let \(q\) be **any odd prime power**, let \(k=\mathbb F_q\), and let \(E=\bigwedge_k V\) for \(V=k^4\). Thus \(\dim_k E=16\). Fix a basis \(e_1,e_2,e_3,e_4\) and \(\omega=e_1\wedge e_2\wedge e_3\wedge e_4\). For \(z\in E\), write
\[
F_q(z)=\#\{(X,Y)\in E^2: (XY-YX)/2=z\}.
\]
All ordinary commutator fibers are recovered by replacing \(z\) with \(z/2\) in this normalized formula; division by two is legitimate because \(q\) is odd. Every nonzero fiber target lies in \(\bigwedge^2V\oplus k\omega\). Write \(z=a+b\omega\), \(a\in\bigwedge^2V\), \(b\in k\), and put \(D=q^5+q^4-q-1\). Then, **for every such target**, the complete fiber law is
\[
F_q(a+b\omega)=q^{16}\begin{cases}
q^8+Dq^7,&a=0,\ b=0,\\
Dq^7,&a=0,\ b\ne0,\\
q^8(q^2-1),&a\ne0,\ a\wedge a=0,\\
0,&a\wedge a\ne0.
\end{cases}
\]
For targets outside \(\bigwedge^2V\oplus k\omega\), the fiber is zero. The last two cases do not depend on \(b\). In dimension four over odd characteristic, \(a\ne0\) and \(a\wedge a=0\) mean precisely that \(a\) is a decomposable bivector. Hence the exact commutator image is the cone over the Klein quadric, with an unrestricted top-degree coordinate:
\[
\operatorname{Im}([\cdot,\cdot])=\{2(a+b\omega):a\in\bigwedge^2V,\ a\wedge a=0,\ b\in k\}.
\]
Its cardinality is
\[
q\left[1+(q-1)(q^2+1)(q^2+q+1)\right].
\]
The additive commutator subspace equals \([E,E]_{\mathrm{lin}}=\bigwedge^2V\oplus\bigwedge^4V\), but a single commutator does **not** exhaust it. Every element of this seven-dimensional subspace is a sum of **at most two** ordinary commutators, and two are necessary for some elements. Consequently the additive commutator width is exactly \(2\). The first failure of width one among exterior algebras on a finite number of generators in odd characteristic occurs with four generators: with at most three generators every element of the derived linear subspace is itself one commutator.

The full centralizer dimension profile is also exact. As \(X\) ranges over \(E\), the centralizer \(C_E(X)=\{Y:XY=YX\}\) has size \(q^{16}\), \(q^{15}\), or \(q^{12}\), with respective multiplicities
\[
q^8,\qquad q^8(q^4-1),\qquad q^{12}(q^4-1).
\]
In particular the probability that two uniformly chosen elements commute is
\[
\Pr(XY=YX)=q^{-4}+q^{-5}-q^{-9}.
\]

## Assumptions and scope

All calculations are over \(k=\mathbb F_q\), with \(q\) an odd prime power; no assumption that \(q\) is prime rather than a prime power is needed. The exterior product is alternating and uses the usual increasing-order basis. Write \(E_{\rm even}=\bigwedge^0V\oplus\bigwedge^2V\oplus\bigwedge^4V\) and \(E_{\rm odd}=\bigwedge^1V\oplus\bigwedge^3V\); each has dimension \(8\). The centralizer profile counts elements of the full unital algebra, not only the nilpotent radical or its group of units. Commutator width is the smallest integer \(r\) such that every element of the **linear span** of associative commutators is a sum of \(r\) such commutators (zero summands are permitted).

## Proof

**1. Reduction to a wedge fiber.** Exterior supercommutativity makes every even element central, and the product of two odd elements skew-commutative. Write the odd parts of arbitrary \(X,Y\) as \(u+c\) and \(v+d\), where \(u,v\in V\) and \(c,d\in\bigwedge^3V\). Since wedges of total degree greater than four vanish,
\[
(XY-YX)/2=u\wedge v+u\wedge d+c\wedge v.
\]
The two independent even parts of \(X,Y\) can be chosen in \(q^{16}\) ways; therefore every odd-pair fiber count receives the same factor \(q^{16}\). Every commutator lies in the indicated seven-dimensional subspace. Conversely, \(u\wedge v\) span \(\bigwedge^2V\), and \(u\wedge d\) span \(\bigwedge^4V\), so this is exactly the commutator **linear span**.

**2. The Klein-quadric dichotomy.** A nonzero \(a\in\bigwedge^2V\) is \(u\wedge v\) for some independent \(u,v\) if and only if it has alternating matrix rank two. In dimension four and characteristic not two, the condition is equivalent to \(a\wedge a=0\): in coordinates \(a=\sum_{i<j}a_{ij}e_i\wedge e_j\), the coefficient of \(\omega\) in \(a\wedge a\) is \(2(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})\). Alternating matrix rank can be zero, two, or four; this Pfaffian vanishes precisely for ranks zero and two. For a prescribed **nonzero** decomposable \(a\), its underlying two-plane is determined, and the ordered bases \((u,v)\) with \(u\wedge v=a\) form one \(\mathrm{SL}_2(k)\)-torsor; thus their number is \(q(q^2-1)\). Since \(u\ne0\), the functional
\[
\bigwedge^3V\oplus\bigwedge^3V\longrightarrow\bigwedge^4V,
\qquad(c,d)\longmapsto u\wedge d+c\wedge v
\]
is nonzero, hence surjective. Its kernel has dimension seven, so every prescribed \(b\) admits exactly \(q^7\) pairs \((c,d)\). Multiplying gives \(q^{16}\,q(q^2-1)q^7=q^{16}q^8(q^2-1)\) as asserted.

**3. The zero-bivector fiber.** For each \(u=0\), all \(q^4\) choices of \(v\) satisfy \(u\wedge v=0\); for each \(u\ne0\), exactly its \(q\)-element span is allowed. Therefore the number of pairs with \(u\wedge v=0\) is \(q^4+(q^4-1)q=q^5+q^4-q\). Exactly one of these is \((u,v)=(0,0)\); its top-degree contribution vanishes for all \(q^8\) choices of \((c,d)\). For each remaining pair, at least one of \(u,v\) is nonzero, so the displayed linear functional is surjective and has exactly \(q^7\) preimages of each \(b\). Multiplication by \(q^{16}\) proves the first two fiber formulas.

**4. Image cardinality.** Nonzero decomposable bivectors are indexed by a two-plane and a nonzero scalar; the number of two-planes in \(k^4\) is the Gaussian binomial \({4\brack2}_q=(q^2+1)(q^2+q+1)\). Thus the number of admissible bivectors is \(1+(q-1){4\brack2}_q\); all \(q\) top-degree scalars occur. This proves the image formula. Summing the fiber law over all targets gives \(q^{32}\), the cardinality of \(E^2\), as an independent mass check.

**5. Centralizers.** For fixed odd part \(u+c\), the normalized commutator with the variable odd part \(v+d\) is a linear map from an eight-space into \(\bigwedge^2V\oplus\bigwedge^4V\). If \(u=c=0\), its rank is zero. If \(u=0\) but \(c\ne0\), the map \(v\mapsto c\wedge v\) is a nonzero functional \(V\to\bigwedge^4V\), so its rank is one. If \(u\ne0\), the map \(v\mapsto u\wedge v\) has rank three with kernel \(ku\). On this kernel, the independent functional in the top degree has rank one because \(d\mapsto u\wedge d\) is surjective. Therefore the total rank is four, irrespective of \(c\). The unrestricted eight-dimensional even part of \(Y\) multiplies kernel sizes by \(q^8\), giving \(q^{16}\), \(q^{15}\), \(q^{12}\). Counting the corresponding choices of \((u,c)\) and the even part of \(X\) gives the stated multiplicities. The zero-target fiber is \(q^{28}+q^{27}-q^{23}\), and division by \(q^{32}\) proves the commuting-probability formula.

**6. Sharp width and the first transition.** Every alternating bivector on a four-space has rank at most four and hence is a sum of at most two decomposable bivectors. The fiber classification shows that a single ordinary commutator can realize any decomposable bivector together with **any** prescribed top-degree coordinate. Therefore two commutators suffice for every element of the commutator linear span. The bivector \(e_1\wedge e_2+e_3\wedge e_4\) has nonzero wedge square \(2\omega\), so no single commutator has this degree-two component, and width is not one. For at most three generators, every bivector is decomposable (rank at most two); commutators have no higher nonzero graded component except the degree-two one. Thus width one holds whenever the commutator span is nonzero for those smaller exterior algebras.

## Verification

The bundled stand-alone standard-library program `verify.py` evaluates multiplication using the sixteen squarefree monomial basis elements and alternating signs. It fully enumerates the degree-one ordered pairs and all bivector targets for the prime fields of orders \(3\) and \(5\); verifies zero, decomposable and nondecomposable bivector multiplicities; evaluates the commutator linear-map rank for every odd element over \(\mathbb F_3\) and for a deterministic sample over \(\mathbb F_5\); compares full multiplication against the graded formula on deterministic test pairs; and checks fiber mass and central count. Running `python3 verify.py` prints `VERIFY_OK`. These finite tests check the implementation and small fields; the proof above establishes the result for every odd prime power, including extension fields that the checker does not explicitly enumerate.

## Relationship to prior work

The Grassmann multiplication rules and the classical Plücker/Klein-quadric characterization of decomposable bivectors are standard and are **not** claimed as new. Bekh-Ochir and Rankin's 2009 finite-field paper (arXiv:0905.2388) describes polynomial identities and central polynomials for finite-dimensional unitary Grassmann algebras. Koshlukov, Krasilnikov and da Silva's 2009 paper gives generators of central-polynomial spaces over infinite fields of odd characteristic, and establishes standard triple-commutator identities. These results give the natural prior PI-theoretic context, but their proved statements do not provide the finite-field **pointwise single-commutator fiber distribution**, image cardinality, centralizer multiplicities and sharp width specified here. Demir and Nazemian's 2025 preprint / 2026 publication classifies automorphism-stable *linear subspaces and subalgebras*, another invariant distinct from individual commutator fibers. The counting theorem above is a finite-field refinement of the classical exterior-product description; its originality is limited to the simultaneous exact quantitative profile, not to the underlying exterior identities or Plücker criterion.

## Limitations

The result applies only to exterior algebras on **four** generators over fields of **odd** characteristic. In characteristic two, the exterior algebra is commutative and every ordinary commutator vanishes, so the normalized map is undefined. No formula for the full higher-generator commutator image is asserted. The accessible full text of the 2009 central-polynomials article was inspected; the directly matching 2011 finite-field identities paper was available by abstract and bibliographic description, not by readable full text, leaving a specific residual bibliographic risk. The 2026 automorphism-stable-subspaces work was compared through its indexed theorem statements, not a complete local PDF. No independent audit has been performed.

## References

1. C. Bekh-Ochir and S. A. Rankin, *The identities and central polynomials of the finite dimensional unitary Grassmann algebras over a finite field*, arXiv:0905.2388, first posted 2009-05-14; later *Communications in Algebra* **39** (2011), 2697–2706. DOI: 10.1080/00927872.2010.489915.
2. P. Koshlukov, A. Krasilnikov, and E. Alves da Silva, *The central polynomials for the finite dimensional Grassmann algebras*, *Algebra and Discrete Mathematics* **2009**(3), 69–76; lawful journal full text: https://admjournal.luguniv.edu.ua/index.php/adm/article/download/788/318.
3. M. K. Demir and Z. Nazemian, *Aut-stable subspaces of Grassmann algebras*, arXiv:2508.16945 (2025); *Communications in Algebra* (2026), DOI: 10.1080/00927872.2026.2631169.
4. Classical Plücker embedding of \(\operatorname{Gr}(2,4)\) as the Klein quadric, used here as an established characterization of simple bivectors.
