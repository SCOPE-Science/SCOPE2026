# Complete exceptional fibers of a triangle-invariant Fermat-square pencil

## Finding
For every prime power \(q=p^e>2\), set \(m=q-1\) and let \(k=\overline{\mathbb F}_q\). The fixed homogeneous equations
\[
S=X^m+Y^m+Z^m,\qquad T=(XY)^m+(YZ)^m+(ZX)^m
\]
define a pencil \(C_\lambda: T+\lambda S^2=0\) for \(\lambda\in k\), completed by \(C_\infty:S^2=0\). Its complete geometric singular-fiber classification is:

1. \(C_\infty\) is the nonreduced double of a smooth Fermat curve of degree \(m\).
2. \(C_0\) is geometrically integral with precisely three ordinary \(m\)-fold singular points at \([1:0:0]\), \([0:1:0]\), \([0:0:1]\). Its normalization is the smooth degree-\(m\) Fermat curve and its geometric genus is \((m-1)(m-2)/2\).
3. If \(p\neq2\), the fiber at \(\lambda=-1/4\) consists of four distinct smooth degree-\(m/2\) Fermat-type curves. Its only singularities are \(3m\) points on the coordinate sides, each with two smooth branches of contact order \(m/2\), hence singularity type \(A_{m-1}\) and local \(\delta=m/2\).
4. If \(p\neq3\), the fiber at \(\lambda=-1/3\) consists of two distinct smooth degree-\(m\) Fermat-type curves meeting transversely in exactly \(m^2\) ordinary nodes. Both components are defined over \(\mathbb F_q\) if \(q\equiv1\pmod3\); otherwise they are defined over \(\mathbb F_{q^2}\) and interchanged by arithmetic Frobenius.
5. Every remaining finite fiber is smooth and geometrically integral, of genus \((2m-1)(2m-2)/2\). All finite-fiber geometric singular points in cases 2–4 are \(\mathbb F_q\)-rational.

The cases conditional on characteristic are omitted when their denominators vanish. For each \(q>2\) the exceptional finite parameters that exist are distinct.

## Assumptions and scope
All geometric properties are over \(k\). Arithmetic assertions concern the displayed equations over \(\mathbb F_q\); the pencil parameter may range over \(k\). The statement concerns the fixed homogeneous integral-coordinate formulas, not any alternative model of their curves. An ordinary \(r\)-fold point has \(r\) distinct tangent lines over \(k\). Here a type \(A_{m-1}\) germ means two smooth branches having contact order \(m/2\) (the characteristic is odd in that case).

## Proof
Write \(u=X^m,v=Y^m,w=Z^m\), \(s=u+v+w\), and \(G_\lambda=uv+vw+wu+\lambda s^2\). Since \(p\nmid m\), the map \([X:Y:Z]\mapsto[u:v:w]\) is étale on the dense coordinate torus. We analyze the torus, open coordinate sides, and the three vertices separately.

On the torus, subtracting two partial derivatives of \(G_\lambda\) yields \(v-u\), \(w-v\), and \(u-w\), in every characteristic. Hence a critical point must have \(u=v=w\). There the vanishing-gradient and equation conditions hold exactly when \(3\lambda+1=0\); this occurs only for \(p\neq3\), including the case \(p=2,\lambda=1\). These give exactly \(m^2\) torus points. For any \(\omega\) with \(\omega^2+\omega+1=0\), we have the exact identity
\[
-3G_{-1/3}=(u+\omega v+\omega^2w)(u+\omega^2v+\omega w).
\]
The two linear factors are distinct and intersect transversely at \(u=v=w\); étaleness proves the \(m^2\) nodes. Their respective pullbacks are smooth degree-\(m\) Fermat-type curves because their coefficients are nonzero and \(p\nmid m\). The arithmetic field assertion follows from whether \(\omega\in\mathbb F_q\) or \(\omega\in\mathbb F_{q^2}\setminus\mathbb F_q\). The torus nodes have coordinates satisfying \(X^m=Y^m=Z^m\), so all lie in \(\mathbb P^2(\mathbb F_q)\).

At an open coordinate side, take \(X=0,YZ\neq0\). The restriction is the binary quadratic \(\lambda(v+w)^2+vw\), and a projective singularity requires a repeated root. In odd characteristic its discriminant vanishes exactly when \(4\lambda+1=0\); the repeated root is \(v=w\). In characteristic two the derivatives force \(v=w\), but the quadratic then equals \(v^2\neq0\), so no side singularity occurs. Assume now \(p\neq2\), write \(h=m/2\), and put \(A=X^h,B=Y^h,C=Z^h\). The polynomial identity
\[
4(T-S^2/4)=(A+B+C)(-A+B+C)(A-B+C)(A+B-C)
\]
gives four distinct Fermat-type components. Their six pairwise intersections are supported on coordinate sides; each pair contributes exactly \(h\) distinct points, and no point lies on three components. At each crossing the two smooth components differ to leading order by \(X^h\) in the transverse coordinate, so their local intersection multiplicity is exactly \(h\). Thus there are \(6h=3m\) points of type \(A_{2h-1}\), each with \(\delta=h\). Their coordinates are rational over \(\mathbb F_q\): the relevant equations on a side are \(Y^h=\pm Z^h\), with \(h=(q-1)/2\), and both signs occur among the \(h\)-th powers in \(\mathbb F_q^\times\).

At a coordinate vertex, say \([1:0:0]\), the equation evaluates to \(\lambda\), so the vertex lies on the curve precisely at \(\lambda=0\). In local coordinates the degree-\(m\) initial form is \(Y^m+Z^m\), which has \(m\) distinct linear factors since \(p\nmid m\). The same is true at the other two vertices. The standard quadratic Cremona transformation \([X:Y:Z]\mapsto[YZ:ZX:XY]\) identifies the dense torus of \(C_0\) with that of the smooth Fermat curve \(U^m+V^m+W^m=0\); the latter is irreducible and contains a dense torus. No coordinate side is a component of \(C_0\), because its restriction is a nonzero monomial. Therefore \(C_0\) is geometrically integral, with the stated normalization and exactly its three ordinary multiple points.

The preceding torus–side–vertex trichotomy exhausts all singular points for every finite parameter. A smooth plane curve is geometrically integral, and the adjunction genus formula gives \((2m-1)(2m-2)/2\) for the remaining finite fibers. Finally, \(S=0\) is smooth because \(p\nmid m\), so its square is precisely the described nonreduced fiber at infinity.

## Verification
The accompanying \(`verify.py`\) checks the two factorization identities symbolically, verifies genus identities, and exhaustively enumerates singular rational points for every finite parameter over \(\mathbb F_q\) with \(q=3,4,5,7,8,11,13,16\). This confirms the expected counts \(3\), \(3m\), and \(m^2\) in the respective exceptional cases, and no rational singularities otherwise. The universal conclusion rests on the preceding proof, not on finite enumeration. Run with \(`python verify.py`\) using Python 3 and SymPy.

## Relationship to prior work
Borges–Korchmáros–Speziali, *Plane curves with a large linear automorphism group in characteristic p* (arXiv:2202.05765v1, §4.7, Theorem 4.22), introduce this triangle-invariant pencil. Their displayed classification does not provide the exceptional-fiber strata, branch types, or arithmetic splitting above; the accessible preprint also gives an unqualified nonsingularity statement about members, in tension with the exact exceptional factorizations. The theorem here concerns only the explicitly written equations, without assumptions about intended exclusions or later journal revisions. Ng Kwing King–Vallès, *New examples of free projective curves*, consider a different Fermat-related pencil involving differences of powers; their singular-fiber examples do not imply this classification.

## Limitations
The result does not classify automorphism groups, moduli of the smooth fibers, or zeta functions. The 2024 journal version of the originating work was not inspected in full; it may change the bibliographic comparison. General algebraic equivalences of symmetric Kummer pencils in unindexed literature remain possible. The small-field checks do not certify the proof independently.

## References
- H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1 (first public: 2022-02-11), §4.7 and Theorem 4.22; https://arxiv.org/html/2202.05765 . Later journal version: DOI 10.1016/j.ffa.2024.102402.
- W. Ng Kwing King and J. Vallès, *New examples of free projective curves* (2022), DOI 10.13137/2464-8728/34099.
