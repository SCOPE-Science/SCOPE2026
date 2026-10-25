# Involution quotients and branch passports of extremal elliptic Artin–Schreier curves

## Finding
Let \(k\) be algebraically closed of characteristic \(2\), let \(q=2^h\) with \(h\ge3\), and let \(X=X(E,\omega,\lambda,q)\) be the genus-\(q+1\) ordinary elliptic Artin–Schreier cover defined below. Write \(u\) for its deck involution, \(t\) for the order-\(q\) lift of a generator of \(E[q](k)\), and \(w\) for the order-two lift of elliptic inversion. Thus \(\operatorname{Aut}(X)=\langle t,w\rangle\times\langle u\rangle\simeq\operatorname{Dih}(C_q)\times C_2\) by Tafazolian.

There are exactly seven conjugacy classes of involutions in this full group. Their geometric fixed-point counts, quotient genera, and types are:

| Involution classes | Number of classes | Fixed points on \(X\) | Genus of quotient | Geometry |
| --- | ---: | ---: | ---: | --- |
| \(u\) | 1 | \(q\) | \(1\) | ordinary elliptic |
| \(t^{q/2},\;ut^{q/2}\) | 2 | \(0\) | \(q/2+1\) | ordinary bielliptic, not hyperelliptic |
| \(t^{2i}w,\;ut^{2i}w\) | 2 | \(2\) | \(q/2\) | ordinary hyperelliptic |
| the two odd-reflection classes \(t^{2i+1}w,\;ut^{2i+1}w\) | 2 | respectively \(4\) and \(0\), in some order | respectively \(q/2-1\) and \(q/2+1\) | ordinary hyperelliptic |

In the last line the assignment of four or zero fixed points depends on the chosen lift of inversion; the two possible choices exchange the classes. Thus the hyperelliptic quotient genera are exactly \(q/2-1\), \(q/2\), and \(q/2+1\), whereas each central nondeck quotient of genus \(q/2+1\) is nonhyperelliptic.

There is an explicit reduced Artin–Schreier branch equation for the minimal-genus quotient. Fix an odd element \(Q\in T=E[q](k)\), let \(r(P)=Q-P\), and choose the unique lift \(s\) of \(r\) having four fixed points on \(X\). The elliptic quotient \(B=E/\langle r\rangle\) is a projective line. Choose a rational coordinate \(x\) on \(B\) in which the two branch points of \(E\to B\) are \(0\) and \(\infty\). The \(q/2\) orbits \(O\in T/\langle r\rangle\) yield pairwise distinct points \(x_O\in k^\times\). Define
\[
 c_O=\lambda\left.\frac{dx}{\omega}\right|_P\in k^\times,\qquad P\in O,
\]
where \(dx\) is pulled back to \(E\). This is independent of the representative \(P\). Then \(Y=X/\langle s\rangle\) has function field
\[
 k(Y)=k(x,v),\qquad v^2+v=\sum_{O\in T/\langle r\rangle}\frac{c_O}{x-x_O}.
\]
The right side has precisely \(q/2\) simple poles; its smooth projective model is ordinary hyperelliptic of genus \(q/2-1\). No genericity condition on \((E,\omega,\lambda)\) is needed.

## Assumptions and scope
The underlying elliptic curve \(E/k\) is ordinary. Set \(T=E[q](k)\cong C_q\), choose an invariant nonzero differential \(\omega\) and \(\lambda\in k^\times\). Take \(f\in k(E)\) whose poles are simple and exactly at \(T\), with \(\operatorname{Res}_P(f\omega)=\lambda\) for all \(P\in T\). Let \(X\) be the smooth projective model of \(z^2+z=f\). Existence and uniqueness of the resulting cover, the group presentation, and its short-orbit data are established in [1]. The theorem addresses quotients by individual geometric involutions of \(\operatorname{Aut}_k(X)\), not arbitrary subgroups, base-field descent, or \(q=4\).

## Proof
**1. Seven involution classes.** Write elements of \(G=\operatorname{Dih}(C_q)\times C_2\) as \(t^iw^eu^f\), with \(e,f\in\{0,1\}\). Apart from the three nonidentity central elements \(u,t^{q/2},ut^{q/2}\), the involutions are reflections \(t^iw u^f\). Conjugation by \(t\) replaces \(i\) by \(i+2\); conjugation by \(w\) replaces \(i\) by \(-i\). Since \(q\) is even, parity and \(f\) exactly distinguish the four reflection classes. This gives seven classes.

**2. Fixed points.** From [1, Proposition 4.1], \(G\) has two short orbits: \(\Omega_2\) of size \(q\), consisting of the points over \(T\) with stabilizer \(\langle u,t^{2i}w\rangle\) at the point over \(iP_0\), and \(\Omega_1\) of size \(2q\), with point stabilizer of order two. All other stabilizers are trivial. Thus \(u\) fixes exactly \(q\) points; either central nondeck involution, being a lift of nontrivial elliptic translation, fixes none. Each even reflection (with or without \(u\)) fixes exactly two points of \(\Omega_2\): solve \(2i\equiv 2j\pmod q\) in \(j\), giving two solutions. Odd reflections fix no point of \(\Omega_2\).

The projections to \(E\) of an odd reflection \(s\) and \(us\) equal \(r(P)=Q-P\) with odd \(Q\in T\). The fixed locus of \(r\) has exactly two geometric points, because multiplication by two on an ordinary elliptic curve in characteristic two has exactly two geometric preimages of every point. These fixed points lie outside \(T\), because \(2P=Q\) has no solution in the cyclic group \(T\). The cover \(X\to E\) is étale there, and \(s\) or \(us\) fixes both points of each two-point fiber, while the other exchanges them. Consequently the two odd lifts have a total of four fixed points among them. The short orbit \(\Omega_1\) is a *single transitive* \(G\)-orbit, and its order-two stabilizers are all conjugate. The two odd-reflection conjugacy classes are disjoint and each has \(q/2\) members, so exactly one class accounts for all stabilizers on \(\Omega_1\). Every member of that class fixes \(2q/(q/2)=4\) points, and every member of the other fixes zero.

**3. Genus and ordinarity.** By [1, Lemma 2.1], every involution on ordinary \(X\) has weak ramification, so each fixed point contributes different exponent exactly two. Riemann–Hurwitz for \(X\to X/\langle s\rangle\) therefore reads
\[
2(q+1)-2=2\bigl(2g(X/\langle s\rangle)-2\bigr)+2r_s,
\qquad g(X/\langle s\rangle)=\frac{q+2-r_s}{2}.
\]
Substitution of \(r_s\in\{q,0,2,4\}\) gives all genera in the table. The same lemma implies ordinarity for every quotient.

**4. Quotient types.** For any reflection \(s\), the deck involution \(u\) commutes with \(s\) and is not in \(\langle s\rangle\). Its induced action on \(Y=X/\langle s\rangle\) has quotient \(X/\langle u,s\rangle=E/\langle r\rangle\cong\mathbb P^1\). Hence \(Y\) is hyperelliptic, with genus at least three since \(q\ge8\). For \(s=t^{q/2}\) or \(ut^{q/2}\), its quotient \(Y\) still has an involution induced by \(u\) with elliptic quotient \(E/\langle t^{q/2}\rangle\). It is therefore bielliptic. Were \(Y\) also hyperelliptic, the distinct degree-two maps to curves of genera one and zero would violate the Castelnuovo–Severi bound \(g(Y)\le3\). In fact \(g(Y)=q/2+1\ge5\), so it is nonhyperelliptic.

**5. The explicit odd-reflection equation.** The quotient map \(E\to B=E/\langle r\rangle\) is separable of degree two. Its two ramification points on \(E\) are the solutions of \(2P=Q\), and they are not in \(T\); the morphism is étale at \(T\). The four-point fixed lift \(s\) acts trivially on both fibers of \(X\to E\) over those two ramification points, so the map \(Y=X/\langle s\rangle\to B\), of degree two, is unramified at their images. In contrast, the \(q/2\) images of \(T\) are branch points: over them the V-four inertia includes \(u\), which remains nontrivial modulo \(\langle s\rangle\). There are no further branch points. Since \(Y\) is ordinary, the lower jump is one at each branch point.

The diagram \(X\to Y\to B\) and \(X\to E\to B\) is an independent biquadratic function-field diagram. Thus the Artin–Schreier extension \(k(Y)/k(B)\), pulled back along the étale local map \(E\to B\) at \(P\in T\), equals the original extension \(k(X)/k(E)\). A local parameter \(x-x_O\) has nonzero derivative at \(P\). The prescribed residue \(\operatorname{Res}_P(f\omega)=\lambda\) therefore converts to the reduced local Artin–Schreier coefficient \(c_O=\lambda (dx/\omega)(P)\). In characteristic two the pullback of the invariant differential by \(P\mapsto Q-P\) equals \(\omega\), and \(x\) is invariant, proving that \(c_O\) is independent of the choice of \(P\in O\).

Every degree-two Artin–Schreier cover of \(\mathbb P^1\) branched with jump one at prescribed points has a rational defining function whose only poles are simple at those points. The local coefficients determined above therefore give the displayed partial-fractions sum, possibly plus a constant. Since \(k\) is algebraically closed, a constant is absorbed by shifting \(v\) by a solution of \(b^2+b=c\). The equality of reduced local classes ensures no other poles remain. The sum has exactly \(q/2\) simple poles, giving \(g=q/2-1\) and \(2\)-rank \(q/2-1\) by Riemann–Hurwitz and Deuring–Shafarevich. This completes the proof.

## Verification
The included `verify_quotient_spectrum.py` enumerates the abstract group action on the two specified short-orbit coset sets for \(q=8,16,32,64,128\). It checks seven involution types, fixed-point counts, and all quotient genera. Successful output ends in `QUOTIENT_SPECTRUM_SANITY_OK`. This finite check is supplementary; the proof for arbitrary \(q\) uses the orbit structure, local ramification, and the function-field argument above.

## Relationship to prior work
Tafazolian [1] proves the construction, full automorphism group, two short orbits, and two free central quotients, and provides an explicit model of the original curve. The seven-class spectrum and especially the residue-normalized Artin–Schreier equation for its odd-reflection quotient are the conclusions addressed here; they are not claimed as a new construction of \(X\) or of its automorphism group. Giulietti–Korchmáros [2,3] develop the earlier extremal-group classification. The detailed relevance of [3]'s inaccessible complete text remains a priority risk, not proof of noncoverage.

## Limitations
This theorem assumes an algebraically closed field, an ordinary elliptic base, \(q\ge8\), and the specific residue-uniform covering family. It does not provide a finite-field model of the quotient for every parameter nor determine isomorphism equivalences between quotient curves from different base parameters. Genus alone need not distinguish the free odd quotient from the nonhyperelliptic central quotients; the hyperellipticity criterion does. Priority against uninspected earlier full texts is not certified. No independent audit has been performed.

## References
[1] S. Tafazolian, *Nakajima-extremal Artin–Schreier covers of ordinary elliptic curves in characteristic 2*, arXiv:2609.14830v1 (first public 2026-09-13), especially Lemma 2.1, Proposition 3.1, Proposition 4.1, Corollary 6.1, and Section 7. https://arxiv.org/abs/2609.14830

[2] M. Giulietti and G. Korchmáros, *Large 2-groups of automorphisms of curves with positive 2-rank*, arXiv:1104.5159. https://arxiv.org/abs/1104.5159

[3] M. Giulietti and G. Korchmáros, *Large 2-groups of automorphisms of algebraic curves over a field of characteristic 2*, Journal of Algebra **427** (2015), 264–294. https://doi.org/10.1016/j.jalgebra.2014.12.019
