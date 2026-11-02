# Abstract automorphism rigidity of finite scalar-affine monoids

## Finding
For a prime power \(q=p^f\) and a nonnegative integer \(d\), let \(V=\mathbb F_q^d\) and define
\[
S_{q,d}=\{(a,v):a\in\mathbb F_q,\ v\in V\},\qquad
(a,v)(b,w)=(ab,v+aw).
\]
For \(d\ge1\), this is faithfully the monoid of all scalar-affine transformations \(\tau_{a,v}(x)=ax+v\), including constants. **Theorem.** Every *abstract* monoid automorphism of \(S_{q,d}\) has the unique form
\[
(a,v)\longmapsto\bigl(\sigma(a),\ L(v)+(1-\sigma(a))t\bigr),
\]
where \(t\in V\), \(\sigma\in\operatorname{Gal}(\mathbb F_q/\mathbb F_p)\), and \(L:V\to V\) is an invertible \(\sigma\)-semilinear map. In particular,
\[
\operatorname{Aut}(S_{q,d})\cong\operatorname{A\Gamma L}_d(q),\qquad
|\operatorname{Aut}(S_{q,d})|=q^d f\prod_{j=0}^{d-1}(q^d-q^j).
\]
These monoids are pairwise nonisomorphic for distinct parameter pairs \((q,d)\). In contrast, for \(d=0\), \(S_{q,0}\) is the multiplicative monoid of \(\mathbb F_q\) and
\(\operatorname{Aut}(S_{q,0})\cong (\mathbb Z/(q-1)\mathbb Z)^\times\), with the trivial-group convention for \(q=2\).

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary, including characteristic two and nonprime finite fields; \(d\) is arbitrary and finite. An automorphism means a permutation of the finite underlying set preserving multiplication and identity; it is **not** assumed linear, polynomial, continuous, or to preserve specified coordinates. The left-zero set is \(Z_\ell(S)=\{s\in S:sx=s\ \text{for all }x\in S\}\). The group \(\operatorname{A\Gamma L}_d(q)\) consists of affine transformations \(x\mapsto L(x)+t\), with an invertible semilinear \(L\), under composition.

## Proof
**1. Constants are intrinsic.** If \(d\ge1\), the left-zero elements are precisely \((0,v)\), for \(v\in V\). Indeed, these elements satisfy \((0,v)(b,w)=(0,v)\); if \(a\ne0\), comparing products with \((0,0)\) and \((0,w)\) for a nonzero \(w\) contradicts the left-zero property. These \(q^d\) constants form a characteristic subset \(C\). Left multiplication gives \((a,v)(0,w)=(0,aw+v)\), so the action of \(S_{q,d}\) on \(C\) is faithful: equality for all \(w\) gives equal translations at \(w=0\) and equal multipliers using some nonzero \(w\).

**2. An abstract automorphism is a point conjugation.** For an abstract monoid automorphism \(\Theta\), its permutation on \(C\) is a uniquely determined \(\pi\in\operatorname{Sym}(V)\). The product identity in step 1 implies \(\Theta(\tau)=\pi\tau\pi^{-1}\) for all \(\tau\in S_{q,d}\). Conversely, any permutation normalizing \(S_{q,d}\) induces such an automorphism; uniqueness follows from its action on constants. As \(S_{q,d}\) is the disjoint union of its units \(U=\{\tau_{a,v}:a\ne0\}\) and constants \(C\), and conjugation by any permutation preserves constant maps, normalizing \(S_{q,d}\) is equivalent to normalizing \(U\).

**3. Translate to an origin-fixing normalizer.** The translation group \(T=\{\tau_{1,v}:v\in V\}\) is a normal subgroup of \(U\), of order \(q^d=p^{fd}\). As \(|U|=q^d(q-1)\) and \(p\nmid(q-1)\), \(T\) is the unique Sylow \(p\)-subgroup of \(U\). Hence each \(\pi\in N_{\operatorname{Sym}(V)}(U)\) normalizes \(T\). Composing \(\pi\) with a translation, assume \(\pi(0)=0\). For every \(v\in V\), conjugation by \(\pi\) sends the translation by \(v\) to the translation by \(\pi(v)\), proving \(\pi(x+v)=\pi(x)+\pi(v)\). Thus \(\pi=L\) is an additive bijection, equivalently an invertible \(\mathbb F_p\)-linear map.

**4. Normalization forces field semilinearity.** The stabilizer of zero in \(U\) is exactly the group of nonzero scalar multiplications \(m_a:x\mapsto ax\). Because \(L(0)=0\) and \(L\) normalizes \(U\), for each \(a\ne0\) there is a unique \(\sigma(a)\ne0\) with \(Lm_aL^{-1}=m_{\sigma(a)}\). Set \(\sigma(0)=0\). Composition yields \(\sigma(ab)=\sigma(a)\sigma(b)\); additivity of \(L\) gives
\[
\sigma(a+b)L(x)=L((a+b)x)=\sigma(a)L(x)+\sigma(b)L(x)
\]
for every \(x\), hence \(\sigma(a+b)=\sigma(a)+\sigma(b)\) (choose \(x\ne0\)). Therefore \(\sigma\) is a field automorphism of \(\mathbb F_q\), necessarily a power of Frobenius, and \(L(ax)=\sigma(a)L(x)\). This also covers \(q=2\), where \(\sigma\) is the identity. Conversely each such \(L\), and every translation \(t\), normalizes all scalar-affine transformations; direct conjugation gives the formula stated above. The factorization into \(t\), \(L\), and \(\sigma\) is unique once a field basis is fixed (\(L=A\circ\sigma\) with \(A\in\operatorname{GL}_d(q)\)). Thus the automorphism group is \(V\rtimes(\operatorname{GL}_d(q)\rtimes\operatorname{Gal}(\mathbb F_q/\mathbb F_p))\), with the stated order.

**5. Rigidity of parameters.** Any monoid isomorphism preserves left-zero elements, so it preserves both \(|S|=q^{d+1}\) and \(|Z_\ell(S)|=q^d\). Their quotient recovers \(q\), and the latter recovers \(d\). For \(d=0\), the unique zero is the sole left-zero element, distinguishing this case from \(d\ge1\); then the multiplicative nonzero elements form the cyclic group \(C_{q-1}\). Each automorphism fixes the absorbing zero, acts arbitrarily by an automorphism of \(C_{q-1}\), and conversely every such cyclic automorphism extends by fixing zero. The case \(q=2\) has a trivial unit group and trivial automorphism group.

## Verification
Run `python3 check_modular_monoid.py` and `python3 check_direct.py`, from the directory containing the scripts. Both use only the Python standard library. The first checks multiplication, intrinsic constant sets, and normalizer permutations for \((q,d)=(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)\) and the rank-zero boundary for \(q=2,3,4,5,7\). The second independently enumerates all monoid automorphisms for \((q,d)=(2,1),(2,2),(3,1)\) by their multiplication tables. Both return `VERIFY_OK`; the scripts and expected outputs are included. The finite computations are cross-checks, not the proof of the universal quantifiers.

## Relationship to prior work
Arzhantsev, Avdeev, and Zaitseva classify algebraic monoid **structures** on affine three-space over algebraically closed fields of characteristic zero. Their table includes the polynomial law \((a,v)(b,w)=(ab,v+aw)\) in dimension three, while their center and idempotent computations do not determine the abstract automorphisms of finite-field rational points. Shafarevich computes algebraic automorphism groups of reductive and active root monoids in characteristic zero. For \(d\ge2\), the unit group of our monoid has a one-dimensional torus acting by scalars on a \(d\)-dimensional unipotent radical, hence is neither reductive nor active in that sense. Shahzamanian and Steinberg study the Gabriel quiver of the affine monoid over a finite commutative ring; their one-dimensional finite-field object is a boundary member here, but their theorem concerns a different invariant. Cleary's 2026 dissertation studies the quiver of the **full** affine transformation monoid; only its abstract/landing record was accessible, not its dissertation PDF. The normalizer of scalar groups and the embedding into a point-permutation group are classical ingredients; the new assertion is the complete *abstract monoid* automorphism classification and parameter recovery across every finite field and dimension.

## Limitations
No claim is made for all affine transformations with arbitrary linear parts, arbitrary finite commutative base rings, or positive-dimensional abstract monoid automorphisms over infinite fields. The proof classifies finite rational-point monoids, not polynomial automorphism group schemes. Historical priority for this exact family is not independently certified: a general existing normalizer theorem could implicitly imply the classification. The 2026 dissertation PDF was inaccessible; its accessible abstract describes a different invariant but does not exclude undiscovered related material.

## References
1. I. Arzhantsev, R. Avdeev, and Y. Zaitseva, *Algebraic monoid structures on the affine 3-space*, arXiv:2412.09559, first public 2024-12-12, §§1,5, Table 1. https://arxiv.org/html/2412.09559v3
2. A. Shafarevich, *Automorphism Groups of Reductive and Root Monoids*, arXiv:2605.11207, first public 2026-05-11, §§1–3. https://arxiv.org/html/2605.11207v1
3. M. H. Shahzamanian and B. Steinberg, *The Quiver of an Affine Monoid*, arXiv:2009.12340, 2020, §§1–2. https://arxiv.org/pdf/2009.12340
4. J. J. C. Cleary, *Quiver of Affine Monoid of a Vector Space Over Finite Field*, doctoral dissertation, CUNY Graduate Center (2026), abstract/landing page. https://academicworks.cuny.edu/gc_etds/6647/
