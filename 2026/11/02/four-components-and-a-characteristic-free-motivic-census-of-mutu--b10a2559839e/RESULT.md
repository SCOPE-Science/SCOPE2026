# Four components and a characteristic-free motivic census of mutual zero products in split octonions

## Finding

Let \(k\) be **any field**, including characteristic two. Let \(\mathbb O_s(k)\) be its eight-dimensional split Cayley (octonion) algebra. Equip the reduced affine zero-product variety
\[
\mathcal Z_k=\{(x,y)\in\mathbb O_s(k)^2:xy=0,\ yx=0\}_{\mathrm{red}}
\]
with the scheme structure of the reduced closed subscheme of \(\mathbb A_k^{16}\).

**Theorem.** The variety \(\mathcal Z_k\) has exactly four geometrically irreducible components, all defined over \(k\): the two coordinate axes, each of dimension \(8\); the closure of the nonzero-trace isotropic-conjugate pairs, of dimension \(8\); and the closure of the pairs whose first factor is nonzero, trace zero, and norm zero, of dimension \(9\). In particular \(\mathcal Z_k\) is non-equidimensional and has dimension \(9\) and codimension \(7\) in \(\mathbb A_k^{16}\).

Writing \(\mathbb L=[\mathbb A_k^1]\) in the Grothendieck ring \(K_0(\mathrm{Var}_k)\), its exact class is
\[
\boxed{[\mathcal Z_k]=\mathbb L^9+3\mathbb L^8-2\mathbb L^7+\mathbb L^5-2\mathbb L^4.}
\]
Consequently, for every prime power \(q\) and every \(r\ge1\),
\[
\boxed{\#\mathcal Z_{\mathbb F_q}(\mathbb F_{q^r})
=q^{9r}+3q^{8r}-2q^{7r}+q^{5r}-2q^{4r}.}
\]
Its Hasse–Weil zeta function is
\[
\boxed{Z(\mathcal Z_{\mathbb F_q},T)=
\frac{(1-q^7T)^2(1-q^4T)^2}
{(1-q^9T)(1-q^8T)^3(1-q^5T)}.}
\]
These are counts of **ordered pairs** annihilating in **both orders**, not counts of conjugacy classes or of the one-sided equation \(xy=0\).

## Assumptions and scope

The split Cayley algebra is realized by Zorn matrices \(x=(a,u,v,b)\) with \(a,b\in k\) and \(u,v\in k^3\). For \(y=(c,s,t,d)\), write
\[
xy=(ac+u\cdot t,\;as+du-v\times t,\;cv+bt+u\times s,\;bd+v\cdot s).
\]
The bilinear dot and alternating cross products use their ordinary coordinate formulas over \(k\); this multiplication also works in characteristic two. Its norm, trace, conjugate, and norm polarization are
\[
N(x)=ab-u\cdot v,\qquad \operatorname{tr}(x)=a+b,\qquad
\bar x=(b,-u,-v,a),
\]
\[
B(x,y)=N(x+y)-N(x)-N(y).
\]
The unit is \((1,0,0,1)\). Direct substitution establishes \(x\bar x=\bar xx=N(x)1\), \(x^2-\operatorname{tr}(x)x+N(x)1=0\), the composition identity \(N(xy)=N(x)N(y)\), and alternativity. No assumption that \(2\) is invertible is used.

Define the isotropic cone \(Q=\{x:N(x)=0\}\subset\mathbb A^8\) and the pure isotropic cone \(P=\{x:N(x)=\operatorname{tr}(x)=0\}\subset\mathbb A^8\). Their dimensions are \(7\) and \(6\), respectively.

## Proof

**1. Universal annihilator rank stratification.** For all \(x,y\), polarizing the quadratic identity yields
\[
xy+yx=\operatorname{tr}(x)y+\operatorname{tr}(y)x-B(x,y)1,
\]
while taking the trace of the product gives
\[
\operatorname{tr}(xy)=\operatorname{tr}(x)\operatorname{tr}(y)-B(x,y).
\]
For \(x\ne0\), let \(K_x=\{y:xy=yx=0\}\).

If \(N(x)\ne0\), multiplication by \(x\) is invertible, hence \(K_x=0\). If \(N(x)=0\) but \(t=\operatorname{tr}(x)\ne0\), the two equations force \(B(x,y)=t\operatorname{tr}(y)\) and then
\[
y=\frac{\operatorname{tr}(y)}{t}(t1-x)=\frac{\operatorname{tr}(y)}{t}\bar x.
\]
Conversely, \(x\bar x=\bar xx=0\), so \(K_x=k\bar x\), of dimension \(1\).

Now suppose \(x\ne0\), \(N(x)=\operatorname{tr}(x)=0\). Since \(x\) cannot be scalar, the polar identity for a mutual annihilator shows \(\operatorname{tr}(y)=B(x,y)=0\). Conversely, if \(\operatorname{tr}(y)=0\) and \(xy=0\), then the standard conjugation reversal gives
\[
yx=\bar y\bar x=\overline{xy}=0,
\]
because \(\bar x=-x\) and \(\bar y=-y\), even in characteristic two. Thus
\[
K_x=\ker(L_x)\cap\ker(\operatorname{tr}),
\]
where \(L_x:z\mapsto xz\).

Here is an independent proof of its dimension. The quadratic identity gives \(x^2=0\), so alternativity gives \(L_x^2=0\), hence \(\operatorname{rank}L_x\le4\). For all \(z\), alternativity also gives \(\bar x(xz)=N(x)z\). Polarizing this in \(x\) yields
\[
\bar x(yz)+\bar y(xz)=B(x,y)z.
\]
Choose \(y\) with \(B(x,y)=1\), possible because the norm polarization is nondegenerate. As \(\bar x=-x\), the identity writes the identity operator as a sum of two operators, each of rank at most \(\operatorname{rank}L_x\). Therefore \(8\le2\operatorname{rank}L_x\), giving \(\operatorname{rank}L_x=4\). Moreover \(z=xy\) belongs to \(\ker L_x\), while \(\operatorname{tr}(z)=-B(x,y)=-1\). Thus trace is nonzero on the four-dimensional kernel, and \(\dim K_x=3\). In summary, the simultaneous annihilator dimensions are \(8,0,1,3\) in the cases \(x=0\), \(N(x)\ne0\), \(N(x)=0\ne\operatorname{tr}(x)\), and \(x\ne0\) with \(N(x)=\operatorname{tr}(x)=0\), respectively.

**2. The four components.** The quadric \(Q\) is geometrically irreducible: its defining polynomial \(ab-u\cdot v\) has a nondegenerate eight-dimensional quadratic polarization, hence cannot be a product of two linear forms. After imposing \(b=-a\), the cone \(P\) has equation \(a^2+u\cdot v=0\). This is also geometrically irreducible; the quadratic has polar rank at least six, and cannot split into linear factors. These arguments hold in characteristic two. Both punctured cones are smooth (the gradients vanish on their respective zero loci only at the origin).

The nonzero-trace open set \(U=Q\setminus P\) is geometrically irreducible and \(\dim U=7\). The set of solutions above \(U\) is the trivial affine line bundle \((x,c\bar x)\), of dimension \(8\), with geometrically irreducible closure \(C_{\mathrm{tr}}\).

Above \(P\setminus\{0\}\), the simultaneous annihilator is the kernel of a morphism of trivial bundles of constant rank \(5\), so the solution space is a rank-three vector bundle. It is geometrically irreducible of dimension \(6+3=9\); denote its closure by \(C_{\mathrm{nil}}\). The remaining solutions are covered by \(C_x=\{(x,0)\}\) and \(C_y=\{(0,y)\}\), each isomorphic to \(\mathbb A^8\). The four sets are incomparable under containment: the axes have points with anisotropic first or second factor, \(C_{\mathrm{tr}}\) has both factors nonzero with nonzero first trace, and \(C_{\mathrm{nil}}\) has dimension \(9\), while its first trace is identically zero. Hence these are exactly the four geometrically irreducible components.

**3. Motivic computation.** Stratify the cone \(Q\) using whether \(u=0\). For \(u=0\), the equation \(ab=0\) has class \(2\mathbb L-1\) and \(v\) is arbitrary. For \(u\ne0\), freely choose \(a,b\) and solve the single nonzero linear equation \(u\cdot v=ab\), leaving an affine-plane bundle. Thus
\[
[Q]=(2\mathbb L-1)\mathbb L^3+(\mathbb L^3-1)\mathbb L^4
=\mathbb L^7+\mathbb L^4-\mathbb L^3.
\]
Likewise \(P\) is cut out by \(b=-a\) and \(a^2+u\cdot v=0\). When \(u=0\), necessarily \(a=0\), and when \(u\ne0\), choose \(a\) freely and solve for two free coordinates of \(v\). Hence
\[
[P]=\mathbb L^3+(\mathbb L^3-1)\mathbb L^3=\mathbb L^6.
\]
The disjoint first-factor cases and their affine-kernel fibers now give
\[
[\mathcal Z_k]=\mathbb L^8+(\mathbb L^8-[Q])
+\mathbb L([Q]-[P])+\mathbb L^3([P]-1).
\]
Substituting the two cone classes yields the boxed polynomial. The vector-bundle rank is constant on each stratum, so these are identities of classes of varieties, not merely analogies obtained by substituting field sizes. Point-count specialization over every extension \(\mathbb F_{q^r}\) proves the formula, and exponentiating the point counts proves the displayed zeta function.

## Verification

The standalone file `verify_split_octonion_zero_products.py` constructs the Zorn product directly over \(\mathbb F_2\), \(\mathbb F_3\), and genuine \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). For every possible first factor, it constructs the full \(16\)-by-\(8\) linear map \(y\mapsto(xy,yx)\), independently row-reduces it over the field, verifies its predicted nullity, and sums the exact kernel cardinalities. This exhausts \(256\), \(6{,}561\), and \(65{,}536\) first factors, respectively. The totals are \(1{,}024\), \(35{,}073\), and \(426{,}496\), all matching the theorem. The program checks the full norm/trace partition sizes separately. The executable's standard output is included as `verification_output.txt`.

## Relationship to prior work

Baez's *The Octonions* (first publicly posted 2001-05-17, MSC primary including 17A35) gives foundational octonionic and composition-algebra structure. Baez and Huerta's *G2 and the Rolling Ball* (first posted 2012-05-11) studies null subalgebras of imaginary split octonions; its Proposition 7 proves a three-dimensional annihilator for nonzero imaginary null elements in the real setting, and its Theorem 10 identifies their pairwise annihilation incidence relation. **Those pure-null geometric facts are established prior work, not claimed as new here.**

The present statement instead addresses *all* simultaneous zero-product pairs in the full eight-dimensional split algebra, including nonzero-trace zero divisors and both coordinate axes, with four reduced components, a uniform Grothendieck class for arbitrary fields (including characteristic two), and finite-field and zeta formulas. Gogberashvili's 2015 discussion of split-octonion zero divisors gives algebraic examples, not this motivic classification. Guterman and Zhilina's 2020/2023 work specifically concerns zero-divisor and relation graphs of **real** split Cayley–Dickson algebras and is a relevant unresolved full-text comparison: only its abstract and bibliographic description were available in the present source inspection. Its real-algebra scope alone cannot supply a characteristic-free motivic identity, but a stronger theorem could overlap the geometric description.

## Limitations

The variety is explicitly **reduced**; no assertion is made that the scheme cut out by the sixteen quadratic coordinate equations is reduced, and no intersection multiplicities or embedded components are classified. The result concerns split Cayley algebras, not anisotropic octonion division algebras. Component geometry, motivic classes, and arithmetic counts are proved as stated, but a completely exhaustive historical-priority search and independent expert verification have not been performed. The nilpotent incidence component has substantial classical antecedents.

## References

1. J. C. Baez, *The Octonions*, preprint arXiv:math/0105155, first submitted 2001-05-17; *Bull. Amer. Math. Soc.* **39** (2002), 145–205. https://arxiv.org/abs/math/0105155 ; https://doi.org/10.1090/S0273-0979-01-00934-X .
2. J. C. Baez and J. Huerta, *G2 and the Rolling Ball*, arXiv:1205.2447, first submitted 2012-05-11; *Trans. Amer. Math. Soc.* **366** (2014), 5257–5293. https://arxiv.org/abs/1205.2447 . Especially Proposition 7 and Theorem 10.
3. M. Gogberashvili, *Geometrical Applications of Split Octonions*, *Adv. Math. Phys.* (2015), article 196708. https://doi.org/10.1155/2015/196708 .
4. A. E. Guterman and S. A. Zhilina, *Cayley–Dickson Split-Algebras: Doubly Alternative Zero Divisors and Relation Graphs*, *Fundam. Appl. Math.* **23** (2020), 95–129; English translation *J. Math. Sci.* **269** (2023), 331–355. https://doi.org/10.1007/s10958-023-06285-5 . Full text not verified in the comparison.
