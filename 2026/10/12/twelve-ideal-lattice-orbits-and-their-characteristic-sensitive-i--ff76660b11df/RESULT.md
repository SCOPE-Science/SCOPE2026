# Twelve ideal-lattice orbits and their characteristic-sensitive incidences in a short local algebra

## Finding

For every prime power \(q\), put \(k=\mathbb F_q\) and
\[
A=k[x,y]/(x,y)^3,\qquad \mathfrak m=(x,y)/(x,y)^3,\qquad W=\mathfrak m^2.
\]
The full \(k\)-algebra automorphism group has exactly **twelve orbits** on the set of all two-sided ideals of \(A\). The total number of ideals is
\[
\boxed{3q^2+4q+7}.
\]
Moreover, the following tables give **all twelve orbit sizes** and the complete point-to-plane incidence profiles inside the three-dimensional socle \(W\). The incidence data changes essentially in characteristic two, although the number of orbits does not.

Four orbits are the singleton ideals \(0\), \(W\), \(\mathfrak m\), and \(A\). Three further orbits consist of one-dimensional ideals in \(W\), classified by binary quadratic factorization:

| Type of nonzero quadratic (up to scalar) | Orbit size |
| --- | ---: |
| A square (type \(C\)) | \(q+1\) |
| Two distinct \(k\)-rational linear factors (type \(E\)) | \(q(q+1)/2\) |
| Irreducible over \(k\) (type \(I\)) | \(q(q-1)/2\) |

Another three orbits consist of two-dimensional subspaces \(T\le W\), each an ideal. A *point* means a one-dimensional ideal \(P\le W\). For each such \(T\), its **incidence profile** \((c,e,i)\) counts contained points of types \(C,E,I\), respectively.

When \(q\) is odd:

| Plane orbit | Orbit size | Profile \((c,e,i)\) |
| --- | ---: | --- |
| Tangent (\(T=U L\) for a line \(L\le U\)) | \(q+1\) | \((1,q,0)\) |
| Secant | \(q(q+1)/2\) | \((2,(q-1)/2,(q-1)/2)\) |
| External | \(q(q-1)/2\) | \((0,(q+1)/2,(q+1)/2)\) |

When \(q\) is even:

| Plane orbit | Orbit size | Profile \((c,e,i)\) |
| --- | ---: | --- |
| Frobenius plane \(W_{\square}=\langle x^2,y^2\rangle\) | \(1\) | \((q+1,0,0)\) |
| Tangent (\(T=UL\)) | \(q+1\) | \((1,q,0)\) |
| Other planes | \(q^2-1\) | \((1,q/2,q/2)\) |

Here \(U=\mathfrak m/\mathfrak m^2\) is identified with the space of linear forms, and \(UL\subset W\) denotes its products with the line \(L\). In even characteristic, \(W_{\square}\) is the **unique automorphism-invariant plane ideal properly contained in \(W\)**; in odd characteristic no such plane exists.

The remaining two orbits, besides the four singleton and six socle orbits, have sizes \(q(q+1)\) and \(q+1\): they are respectively the ideals whose image in \(U\) is a line \(L\) and whose intersection with \(W\) is \(UL\), and the ideals \(L+W\). These twelve sizes sum to the stated total number of ideals.

This also determines every covering relation in the ideal lattice: every point is covered by precisely the planes containing it; each socle plane is covered by \(W\), and a tangent plane \(UL\) is additionally covered by exactly \(q\) ideals of dimension three projecting to \(L\); each of those has the unique dimension-four cover \(L+W\); \(W\) is covered by all \(q+1\) dimension-four ideals \(L+W\); these are covered by \(\mathfrak m\), which is covered by \(A\). The zero ideal is covered by all point ideals. Thus the orbit-size and incidence tables, together with these rules, describe the entire ideal-lattice covering graph equivariantly.

## Assumptions and scope

The algebra is commutative, unital and six-dimensional over the finite field \(k=\mathbb F_q\); its radical has Hilbert function \((1,2,3)\), its socle equals \(W\), and \(\mathfrak m^3=0\). Automorphisms are \(k\)-algebra automorphisms fixing the identity. The theorem applies to all prime powers, including nonprime fields and characteristic two. An orbit is an orbit of individual ideals, not an isomorphism class of abstract modules.

## Proof

**1. The automorphism group and parametrization of ideals.** Write \(U=kx\oplus ky\) and \(W=kx^2\oplus kxy\oplus ky^2\), so \(\mathfrak m=U\oplus W\) as vector spaces and multiplication induces the canonical isomorphism \(\operatorname{Sym}^2 U\simeq W\). The radical and its square are characteristic ideals. The images of \(x,y\) under any automorphism have arbitrary quadratic terms and an invertible linear part; conversely every such assignment extends to an automorphism, because all cubic monomials vanish. Thus
\[
G=\operatorname{Aut}_k(A)\cong \operatorname{Hom}_k(U,W)\rtimes\operatorname{GL}(U),\qquad |G|=q^6|\operatorname{GL}_2(q)|,
\]
and its action on \(W\) is the symmetric-square action of \(\operatorname{GL}_2(k)\). The first factor acts trivially on \(W\).

Every proper ideal lies in \(\mathfrak m\). For any such ideal \(J\) let \(S\le U\) be the projection of \(J\) and \(T=J\cap W\). Since \(\mathfrak mW=0\), the condition for a subspace with these data to be an ideal is exactly \(US\subseteq T\). Once \(S,T\) are fixed, all such ideals are graphs of linear maps \(S\to W/T\), hence their number is \(q^{\dim S(3-\dim T)}\).

If \(S=0\), \(T\) may be any of the \(2(q^2+q+1)+2\) subspaces of \(W\). If \(\dim S=1\), multiplication gives \(\dim US=2\) and \(T\) is either \(US\) (\(q\) graphs for each of \(q+1\) possible \(S\)) or \(W\) (one graph for each \(S\)). If \(S=U\), then \(US=W\), hence \(J=\mathfrak m\). Finally \(A\) is one ideal. Therefore
\[
\#\{\text{ideals of }A\}=
\bigl(2q^2+2q+4\bigr)+q(q+1)+(q+1)+1+1
=3q^2+4q+7.
\]
The additive automorphisms \(U\to W\) act transitively on the graphs with fixed \(S,T\), while \(\operatorname{GL}_2(k)\) acts transitively on lines \(S\le U\). Thus the two non-socle intermediate cases each form a single orbit.

**2. Point ideals in the socle.** A nonzero line in \(W\simeq\operatorname{Sym}^2(k^2)\) is a binary quadratic form up to scalar. Since \(k\) is finite, it is (i) a square of a linear form, (ii) a product of two distinct rational linear forms, or (iii) irreducible. The natural \(\operatorname{GL}_2(k)\) action is transitive within each type: in the first two cases, this is transitivity on one or on unordered pairs of distinct projective points; for the third, a pair of conjugate points on the projective line becomes an irreducible quadratic, and nonsplit tori give transitivity. The orbit sizes are \(q+1\), \(\binom{q+1}{2}\), and \((q^2-q)/2\). In characteristic two the square locus is a projective line rather than a nonsingular conic, but the same factorization classification and sizes remain valid.

**3. Plane ideals for odd characteristic.** The square locus \(C\subset\mathbb P(W)\) is the nonsingular conic given parametrically by \([\ell^2]\) for \(0\ne\ell\in U\). Projective lines in \(\mathbb P(W)\) fall into three \(\operatorname{PGL}_2(k)\)-orbits by their intersections with \(C\): tangent (one rational point with multiplicity two), secant (two distinct rational points), and external (no rational point). Their orbit sizes are respectively \(q+1\), \(q(q+1)/2\), and \(q(q-1)/2\). Representatives are \(\langle x^2,xy\rangle\), \(\langle x^2,y^2\rangle\), and \(\{a x^2+bxy+c y^2:a=\delta c\}\) with \(\delta\in k^*\) nonsquare.

On the tangent line all nonsquare points are split; on the secant line the two conic points are squares and the other \(q-1\) points divide equally into split and irreducible quadratics. The external representative has no square: for \(c=0\) its unique point is \([xy]\), and for \(c\ne0\) its remaining points are \([\delta x^2+bxy+y^2]\) as \(b\) runs through \(k\). The standard finite-field identity \(\sum_{b\in k}\chi(b^2-4\delta)=-1\), with \(\chi\) the quadratic character, shows that exactly \((q-1)/2\) of these are split and \((q+1)/2\) are irreducible, yielding the table.

**4. Plane ideals in characteristic two.** The Frobenius map on \(k\) is bijective, so all squares in \(W\) form the projective line \(\mathbb P(W_{\square})\) for \(W_{\square}=kx^2\oplus ky^2\). It is invariant under substitutions and is the only invariant plane because every other plane belongs to one of the nontrivial orbits described next. A plane other than \(W_{\square}\) meets it in exactly one projective point; transitivity of \(\operatorname{GL}_2(k)\) on that point permits assuming it is \([x^2]\). The stabilizer of \([x^2]\) has two orbits on the other planes through \([x^2]\): \(\langle x^2,xy\rangle\) and \(\langle x^2,xy+y^2\rangle\). The first is \(Ux\), and across all \([x^2]\) this yields \(q+1\) tangent planes. There are \((q^2+q+1)-1-(q+1)=q^2-1\) planes of the second type.

The tangent plane has one square and \(q\) split points. The other representative has one square and its other \(q\) points are the forms \([a x^2+xy+y^2]\) for \(a\in k\). These are split precisely when \(z^2+z+a\) has a root in \(k\), equivalently when its absolute trace from \(k\) to \(\mathbb F_2\) is zero. The trace takes each value on \(q/2\) elements, proving the \((1,q/2,q/2)\) profile. The Frobenius plane consists entirely of squares, proving its profile and uniqueness.

**5. Cover relations.** Ideals contained in \(W\) form its ordinary subspace lattice; the point-plane incidences therefore give exactly its rank-one-to-rank-two covers. A dimension-three nonsocle ideal with projection \(L\) intersects \(W\) precisely in \(UL\), so it covers just that plane and is covered by the unique dimension-four ideal \(L+W\). Each tangent plane has \(q\) such dimension-three superideals. Every socle plane is covered by \(W\); every \(L+W\) covers \(W\) as well as the \(q\) nonsocle dimension-three ideals with projection \(L\). The full rank filtration and the absence of other ideals with a given projection prove that there are no further covering relations. This proves the complete statement.

## Verification

The standalone `verify.py` builds finite fields of orders \(2,3,4,5,7,8,9\), generates the projective \(\operatorname{GL}_2\)-action on quadratic forms and its dual action on planes, and computes every orbit and point-plane incidence profile directly. It checks the twelve orbit sizes, the profile tables and the total ideal count for each field. As an independent small-case check, it also enumerates **all 374 subspaces** of the five-dimensional radical over \(\mathbb F_2\), filters the **26 proper ideals**, adds \(A\), and constructs all **384 automorphisms**, yielding the claimed twelve ideal orbits directly. Saved replay output is in `verification_output.txt` and ends in `VERIFY_OK` for the projective checks; its last line confirms the direct \(\mathbb F_2\) enumeration. These finite computations check consistency; the arbitrary-prime-power theorem follows from the symbolic proof above.

## Relationship to prior work

De Stefani's study of low-socle-degree Artinian level algebras (arXiv:1208.3506v1, first public 16 August 2012) establishes structural and Hilbert-function results in characteristic zero, including the socle-degree-two range. It does not enumerate finite-field automorphism orbits on the ideal lattice or their incidence profiles. Classical finite projective geometry supplies the three binary-quadratic point types and conic-line orbit geometry, which are explicitly reused here, not claimed as novel in isolation. Earlier general work on finite-field ideal counting includes Kassel–Reutenauer's Laurent-polynomial ideal enumeration (arXiv:1505.07229); that is a different ring and counting question.

Related published results give a criterion for monomializing two-generated short local algebras (the Segre-quadric criterion) and automorphism normal forms for truncated coordinate-cross algebras. The former classifies **algebras**, not the ideals within this fixed algebra. The latter assumes vanishing mixed products, whereas the present algebra has nonzero \(xy\). Neither statement implies the present twelve-orbit and characteristic-sensitive incidence theorem. Searches for the ideal-lattice classification and equivalent quadratic-form and projective-incidence descriptions did not locate a published complete statement; this negative search cannot prove uniqueness.

## Limitations

The theorem concerns this one canonical six-dimensional Artinian algebra; it does not classify ideal orbits for higher truncation exponents, other local algebras of Hilbert type \((1,2,3)\), or arbitrary commutative rings. The projective orbit ingredients are classical; any originality resides in their exact integration with **all** nonhomogeneous ideals and the full incidence structure, especially the characteristic-two Frobenius-plane transition. Earlier literature using different terminology may contain an equivalent special-case enumeration. Independent external audit has not been performed.

## References

1. A. De Stefani, *Artinian level algebras of low socle degree*, arXiv:1208.3506v1 (16 August 2012), https://arxiv.org/abs/1208.3506; later published in *Communications in Algebra* 42 (2014), 729–754, https://doi.org/10.1080/00927872.2012.722736.
2. C. Kassel and C. Reutenauer, *Counting the ideals of given codimension of the algebra of Laurent polynomials in two variables*, arXiv:1505.07229 (2015), https://arxiv.org/abs/1505.07229.
3. *Segre-quadric monomiality criterion for two-generated short local algebras* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-segre-quadric-monomiality-two-generated-short-local-algebras--0eb926948571.
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb.
