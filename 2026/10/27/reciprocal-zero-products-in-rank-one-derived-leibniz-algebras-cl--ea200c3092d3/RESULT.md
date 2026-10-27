# Reciprocal zero products in rank-one-derived Leibniz algebras: classification and finite-field census

## Finding
Let \(L\) be an \(n\)-dimensional right Leibniz algebra over a field \(K\) of characteristic different from \(2\), where \(n\ge2\) and \(\dim_K[L,L]=1\). Suppose its zero products are reciprocal:
\[
[x,y]=0\quad\Longleftrightarrow\quad[y,x]=0\qquad(x,y\in L).
\]
Then its bracket is **either symmetric or alternating**. The non-Lie cases have central derived line and are precisely the nonzero symmetric bilinear forms on the quotient by that line, up to scalar congruence. The Lie cases are either central and represented by nonzero alternating forms on the quotient, or are isomorphic to \(\mathfrak{aff}_1(K)\oplus K^{n-2}\).

For every odd prime power \(q\), the number of isomorphism classes of these algebras over \(\mathbb F_q\) is exactly
\[
n+2\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Their number of *labelled algebra laws* on a fixed \(n\)-dimensional vector space over \(\mathbb F_q\) is exactly
\[
\boxed{\frac{q^n-1}{q-1}\left(q^{n(n-1)/2}+q^{(n-1)(n-2)/2}-2+q^{n-2}(q^{n-1}-1)\right).}
\]
(The first exponential equals \(q^{m(m+1)/2}\) for \(m=n-1\).)

The rank-one-derived hypothesis is sharp for the symmetric/alternating dichotomy: there exists a four-dimensional two-step nilpotent right Leibniz algebra with two-dimensional derived ideal whose zero products are reciprocal although its bracket is neither symmetric nor alternating.

## Assumptions and scope
The right Leibniz identity is taken to mean
\[
[x,[y,z]]=[[x,y],z]-[[x,z],y].
\]
The zero-product property means the displayed equivalence for **all ordered pairs**; it does not assume the bracket itself is symmetric or antisymmetric. The derived ideal has **exactly** dimension one (not dimension at most one). The isomorphism and labelled-count statements concern every finite field \(\mathbb F_q\) of odd cardinality; the structural dichotomy holds over any field with \(\operatorname{char}K\ne2\). Here \(\mathfrak{aff}_1(K)\) has basis \(h,z\) and bracket \([h,z]=z\), with antisymmetry.

## Proof
**1. Centrality in the non-Lie case.** Right Leibniz implies \([x,[y,y]]=0\) for all \(x,y\). If the bracket is not alternating, choose \(y\) with \([y,y]\ne0\); since the derived ideal is a line, it equals \(K[y,y]\), and \([L,[L,L]]=0\). Reciprocal zeros then imply \([[L,L],L]=0\). Therefore the derived line is central, and after choosing a nonzero \(z\) in it, the bracket descends to a nonzero bilinear form \(B:(L/Kz)^2\to K\), via \([x,y]=B(\bar x,\bar y)z\).

**2. Reciprocity lemma for bilinear forms.** Suppose a scalar bilinear form \(B\) satisfies \(B(x,y)=0\iff B(y,x)=0\). Let \(T(x)=B(x,-)\) and \(S(x)=B(-,x)\), elements of the dual space. Equality of kernels means \(\ker T=\ker S\), and for every \(x\) with \(T(x)\ne0\), the functionals \(T(x),S(x)\) are nonzero proportional. If \(\operatorname{rank}T=1\), linearity and equality of kernels force \(S=cT\) for one nonzero scalar \(c\). If \(\operatorname{rank}T\ge2\), choosing pairs with independent images, applying linearity to their sum, and connecting any other nonzero image through an independent one again shows \(S=cT\) with the same scalar for all \(x\). Thus \(B(y,x)=cB(x,y)\) for every pair. Transposing twice gives \(c^2=1\), hence \(c=1\) or \(c=-1\); the form is symmetric or alternating (using \(\operatorname{char}K\ne2\)). In the non-Lie case it is necessarily symmetric, since an alternating bracket is Lie.

**3. Lie case.** If all squares vanish, polarization makes the bracket alternating; its right Leibniz identity becomes Jacobi. Let \([L,L]=Kz\). If \(Kz\) is central, the preceding construction gives a nonzero alternating form on \(L/Kz\). Otherwise write \([x,z]=\phi(x)z\), where \(\phi(z)=0\) and \(\phi\ne0\). Writing \([x,y]=b(x,y)z\), Jacobi is \(\phi\wedge b=0\). For \(\phi\ne0\), elementary exterior linear algebra gives \(b=\phi\wedge\alpha\), and \(b(x,z)=\phi(x)\) gives \(\alpha(z)=1\). Choosing \(h\) with \(\phi(h)=1\) and then a basis of \(\ker\phi\) containing \(z\) shows that all brackets other than \([h,z]=z\) vanish after replacing each remaining basis vector by a suitable central combination. The resulting algebra is \(\mathfrak{aff}_1(K)\oplus K^{n-2}\).

**4. Isomorphism types over odd finite fields.** For central algebras the derived line is characteristic. Replacing its generator rescales the associated form, and changing the quotient basis acts by congruence. Conversely scalar congruence yields an algebra isomorphism. A nonzero symmetric form of rank \(r\), with \(1\le r\le n-1\), has one similarity class for odd \(r\), and two for even \(r\), because finite-field nonsingular symmetric forms have two determinant-square classes and scaling exchanges them exactly when \(r\) is odd. This contributes \((n-1)+\lfloor(n-1)/2\rfloor\). Alternating forms have one class in each even positive rank up to \(n-1\), contributing \(\lfloor(n-1)/2\rfloor\). The single noncentral Lie class adds one. These are disjoint since square products distinguish non-Lie from Lie, and centrality distinguishes the Lie types. The sum is the stated \(n+2\lfloor(n-1)/2\rfloor\).

**5. Labelled counts.** The derived line can be chosen in \((q^n-1)/(q-1)\) ways. Fix it and choose a generator \(z\). A central bracket is a nonzero symmetric or alternating form on the \(m=n-1\)-dimensional quotient. There are \(q^{m(m+1)/2}-1\) symmetric forms and \(q^{m(m-1)/2}-1\) alternating forms; the two collections meet only at the excluded zero form. For a noncentral Lie bracket, \(\phi(x)\) is defined by \([x,z]=\phi(x)z\), with \(\phi(z)=0\) and \(\phi\ne0\); there are \(q^{n-1}-1\) choices. Each \(b=\phi\wedge\alpha\) satisfying \(\alpha(z)=1\) has exactly \(q\) descriptions (\(\alpha\) and \(\alpha+t\phi\) agree), and therefore \(q^{n-2}\) distinct possibilities. The three families are disjoint and every bracket is counted once, proving the formula.

**6. Two-dimensional-derived boundary.** On the vector space with basis \(e_1,e_2,z_1,z_2\), define \([e_1,e_1]=z_1\), \([e_1,e_2]=z_2\), \([e_2,e_1]=-z_2\), and all other basis brackets zero. The derived ideal is central of dimension \(2\), so the right Leibniz identity holds. For \(x=ae_1+be_2+u\), \(y=ce_1+de_2+v\), with \(u,v\) central, the pair of bracket coordinates is \((ac,ad-bc)\), while the reversed pair is \((ac,bc-ad)\). These pairs vanish simultaneously for every \(x,y\), but the bracket has a nonzero square and a nonzero antisymmetric part.

## Verification
The included Python 3 standard-library checker `verify.py` exhausts all bilinear products on \(\mathbb F_3^2\), selecting exactly those satisfying the right Leibniz identity, derived dimension one, and reciprocal zero products. It finds \(8\) symmetric and \(8\) alternating laws, matching the formula's \(16\) labelled laws. Over \(\mathbb F_3^3\) it constructs and checks all \(364\) central and \(312\) noncentral laws, matching the total \(676\). It also checks the four-dimensional boundary example over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\). Run `python3 verify.py` from the unpacked folder. These finite checks corroborate, but cannot replace, the unrestricted proof.

## Relationship to prior work
Elhamdadi and Virgin (arXiv:2604.17043, Proposition 5.1) give the reciprocal-zero condition as a criterion for the Noether property of their smooth real Leibniz-rack families; they do not give the all-dimension, all-odd-field rank-one-derived classification, orbit count, or labelled algebra-law count above. Classical bilinear-form reflexivity and finite-field congruence theorems are acknowledged ingredients rather than claimed discoveries. Di Bartolo, La Rosa and Mancini (arXiv:2307.09102) classify nonnilpotent *non-Lie* rank-one-derived Leibniz algebras; their one-sided-bracket cases do not satisfy reciprocity. La Rosa, Mancini and Nagy (arXiv:2302.08306) classify relevant nilpotent algebras up to **isotopy**, a coarser equivalence than the isomorphism counted here. The present contribution is the conditional combined classification and exact finite-field labelled and isomorphism census, not the stand-alone standard bilinear lemma.

## Limitations
The Noether interpretation is formally established by the cited 2026 paper for finite-dimensional **real** Leibniz algebras. Over finite fields, the same zero-product relation is studied algebraically, without claiming the existence of the cited smooth real rack structure. The formula does not include characteristic two or algebras with derived dimension zero or greater than one. The displayed four-dimensional counterexample only proves failure of the dichotomy when derived dimension two is permitted; it does not assert minimum possible ambient dimension. Earlier literature on congruence and nilpotent Leibniz classifications could contain an implicit derivation of portions of the result; independent literature review remains useful.

## References
1. M. Elhamdadi and B. Virgin, *Lie Quandles, Leibniz Racks and Noether's First Theorem*, arXiv:2604.17043v1 (first public April 18, 2026); SIGMA 22 (2026), 096.
2. A. Di Bartolo, G. La Rosa and M. Mancini, *Non-Nilpotent Leibniz Algebras with One-Dimensional Derived Subalgebra*, arXiv:2307.09102 (2023), Mediterranean Journal of Mathematics 21 (2024), 138.
3. G. La Rosa, M. Mancini and G. P. Nagy, *Isotopisms of nilpotent Leibniz algebras and Lie racks*, arXiv:2302.08306 (2023).
4. I. Demir, K. C. Misra and E. L. Stitzinger, *Classification of some Solvable Leibniz Algebras*, arXiv:1501.00890 (2015).
