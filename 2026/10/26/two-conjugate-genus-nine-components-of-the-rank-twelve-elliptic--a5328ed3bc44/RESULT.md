# Two conjugate genus-nine components of the rank-twelve elliptic threefold discriminant

## Finding
In the explicitly specified elliptic Calabi--Yau threefold of Burek [1], the reduced residual discriminant \(D\) is geometrically reducible, although irreducible over \(\mathbb Q\). Its two geometrically irreducible components are conjugate over \(\mathbb Q(\sqrt{481})\). Each component has degree eight over the \(v\)-ruling, exactly 32 ordinary cusps and normalization of genus nine. Their intersection consists of 96 ordinary transverse nodes; the arithmetic genus of each component is 41 and the arithmetic genus of their union is 177. Each normalization is a connected unramified cyclic degree-four cover of a genus-three hyperelliptic curve.

## Assumptions and scope
Work over characteristic zero. On the affine chart in [1, equations (1.2)--(1.4) and (5.5)], put
\[
A(v)=v^8+14v^4+1,\quad B(v)=v(v^4-1),\quad C(v)=v^{12}-33v^8-33v^4+1,
\]
\[
a=481,\quad b=30,\quad c=-4879,\quad d=54b^4,\quad u^2=a^3,\quad u=a\sqrt a.
\]
The residual discriminant polynomial, up to a nonzero factor, is
\[
R(v,t)=\bigl(dt^8+cC(v)t^4+54B(v)^4\bigr)^2-a^3A(v)^3t^8.
\]
By \(D\) we mean the reduced closure of this affine curve on the blown-up Hirzebruch base in [1, Sections 6--8], rather than the boundary discriminant curves of multiplicity four. The source proves its boundary smoothness and describes its 96 ordinary nodes and 64 ordinary cusps [1, Lemma 8.2].

## Proof
**1. Factorization and fields.** Set \(q=t^4\). The polynomial identity
\[
A^3-C^2=108B^4,\qquad a^3-c^2=108b^4
\]
leads to the exact factorization \(R=G_-G_+\) over \(\mathbb Q(u)\), where
\[
G_-=dt^8-(u-c)Ct^4-\frac{(u-c)^2}{2b^4}B^4,
\]
\[
G_+=dt^8+(u+c)Ct^4-\frac{(u+c)^2}{2b^4}B^4.
\]
Here unadorned \(B,C\) denote evaluation at \(v\). The identity is polynomial, not merely a generic numerical factorization; its exact coefficient verification is reproduced in the attached checker. Conjugation \(u\mapsto-u\) interchanges the factors.

**2. Absolute irreducibility.** Work over \(K=\mathbb C(v)\). Since \(A\) has eight distinct roots, it is not a square in \(K\), and \(L=K(w)\), \(w^2=A(v)\), is the function field of a smooth hyperelliptic genus-three curve \(W\). Each quadratic factor in \(q\) has discriminant equal to a nonzero constant times \(A^3\); adjoining a root therefore gives precisely \(L\). In \(L\), the root \(q\) is a nonzero constant multiple of \(C+Aw\) or \(C-Aw\). Neither is a square in \(L\): if \(C+Aw=(r+sw)^2\) with \(r,s\in K\), then \(2rs=A\) and \(r^2+As^2=C\), whence
\[
2r^2=C\pm\sqrt{C^2-A^3}=C\pm6\sqrt{-3}B^2.
\]
But the exact identities
\[
C\pm6\sqrt{-3}B^2=\bigl(v^4\pm2\sqrt{-3}v^2+1\bigr)^3
\]
show the right side is not a square in \(K\): each displayed quartic has four distinct roots. The same reasoning applies to \(C-Aw\) by the involution of \(L/K\). Because \(\mathbb C\) contains all fourth roots of unity, adjoining \(t\) with \(t^4=q\) gives degree four over \(L\) when \(q\) is not a square. Thus \([K(t):K]=8\) for either factor, proving both \(G_\pm\) absolutely irreducible. As distinct Galois-conjugate factors, their product is irreducible over \(\mathbb Q\), with exactly two components after base change to \(\mathbb C\).

**3. Normalizations and genus.** Consider \(f=C+Aw\) on the smooth projective \(W\). Its norm to \(K\) is \(C^2-A^3=-108B^4\). The five simple roots \(v=0,\pm1,\pm i\) of \(B\) do not vanish on \(A\) or \(C\); at each such value exactly one point of \(W\) is a zero of \(f\), of order four. There are no other finite zeros or poles. At the two points at infinity of \(W\), the pole orders of \(f\) are 12 and 8: on one branch \(w\sim v^4\) and \(f\sim2v^{12}\), while on the other branch the norm identity forces pole order eight because \(B^4\) has pole order twenty. All valuations of \(f\) are divisible by four. Consequently the connected Kummer extension \(L(t)/L\), \(t^4\) a constant times \(f\), is unramified at every point. Its Galois group over \(L\) is cyclic of order four, and Riemann--Hurwitz yields \(2g-2=4(2\cdot3-2)=16\), so \(g=9\). Replacing \(w\) by \(-w\) gives the same genus for both factors.

**4. Singularities and the arithmetic-genus check.** The source [1, Lemma 8.2] establishes that the complete reduced residual curve has precisely 64 ordinary cusps, 96 ordinary nodes and no other singularities, including at the boundary. The 64 cusps lie above the eight simple roots of \(A\). At each such root, \(G_-\) and \(G_+\), viewed as quadratics in \(q=t^4\), have distinct nonzero repeated roots, so each factor contains exactly four cusp points over each of the eight values of \(v\), hence 32 cusps each. At every one of the 96 nodes, \(A(v)\ne0\), so each factor is smooth in the \(t\)-direction (the quadratic discriminants are nonzero), and therefore each ordinary node must be the transverse intersection of the two components. No other intersections exist because every intersection would be a singular point of \(D\). Every cusp contributes delta-invariant one; hence each component has arithmetic genus \(9+32=41\). The union has arithmetic genus \(41+41+96-1=177\), agreeing with the source's global adjunction calculation.

## Verification
Run `python3 verification/verify.py` from the extracted artifact folder. It uses only Python's standard library and checks exactly, in polynomial rings over quadratic number fields, the factorization of \(R\), the key identities for \(A,B,C\), the cubic identities used to show nonsquareness, and the numerical genus reconciliation. The printed success marker is `VERIFY_OK`. The geometrical claims depend additionally on the local valuation proof above and the complete boundary/singularity classification in [1]; the computer does not replace those arguments.

## Relationship to prior work
Burek [1, Lemmas 5.5, 8.2] established a square-free degree-16 residual discriminant and counted its 96 nodes and 64 cusps, and explicitly made genus/Euler calculations without presuming irreducibility. The two conjugate degree-eight factors, their fields of definition, the precise division of the cusps and nodes between components, and the unramified cyclic genus-nine normalization are not asserted by those statements. Kumar and Kuwata [2, Section 5] analyze elliptic K3 surfaces \(F^{(4)}\), their sections and Mordell--Weil lattices; this does not directly classify the global residual discriminant curve of the specialized threefold family. The new conclusions require the displayed factorization, its absolute-irreducibility proof and valuation analysis.

## Limitations
The statement applies to this explicit specialized family and its blown-up base, not arbitrary Kummer elliptic threefolds. Ordinary cusp/node counts and smoothness outside the affine chart rely on [1, Lemma 8.2], not a new independent classification. No independent external audit has been performed. Older unindexed calculations involving factorization of special Kummer-family discriminants remain a residual literature risk.

## References
[1] Dominik Burek, *An elliptic Calabi--Yau threefold of Mordell--Weil rank twelve*, arXiv:2610.01276v1, first public 2026-10-01, especially equations (1.2), (1.3), (5.5) and Lemma 8.2. https://arxiv.org/html/2610.01276v1

[2] Abhinav Kumar and Masato Kuwata, *Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell--Weil lattices and their fields of definition*, arXiv:1409.2931v3, especially Section 5. https://arxiv.org/html/1409.2931v3
