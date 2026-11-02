# A reducibility threshold for commuting tuples in symmetric Kronecker trivial extensions

## Finding
Let \(k\) be any field, let \(r\ge1\) and \(m\ge2\), and let \(K_r=kQ_r\), where \(Q_r\) has two vertices and \(r\) arrows from the first vertex to the second. Form the symmetric trivial-extension algebra \(T_r=K_r\ltimes D(K_r)\), where \(D(K_r)=\operatorname{Hom}_k(K_r,k)\) has its usual bimodule structure. Let \(\mathcal C_{r,m}\) denote the **reduced** affine variety of ordered pairwise-commuting \(m\)-tuples in \(T_r\).

**Component theorem.** If \(r=1\), \(\mathcal C_{1,m}\) is geometrically irreducible of dimension \(4m+2\). If \(r\ge2\), it has exactly two geometrically irreducible components, both defined over \(k\). The first, \(\mathcal D_{r,m}\), is a rank-at-most-one determinantal variety times \(\mathbb A_k^{3m}\), of dimension \(4m+2r\). The second, \(\mathcal I_{r,m}\), is an isotropic-matrix variety times \(\mathbb A_k^{3m}\): its dimension is
\[
3m+sm+s(2r-s)-\binom{s}{2},\qquad s=\min\{m,r\}.
\]
Their reduced intersection is a rank-at-most-one determinantal variety times \(\mathbb A_k^{3m}\), of dimension \(4m+2r-1\).

**Finite-field census.** For any prime power \(q\), define
\[
I_{r,s}(q)=\prod_{i=0}^{s-1}\frac{q^{2r-i}-q^i}{q^s-q^i},\qquad I_{r,0}(q)=1.
\]
Then the number of pairwise-commuting ordered \(m\)-tuples in \(T_r(\mathbb F_q)\) is exactly
\[
\boxed{N_{r,m}(q)=q^{3m}\left[(q^m-1)q^{2r}+\sum_{s=0}^{\min\{m,r\}}I_{r,s}(q)\prod_{i=0}^{s-1}(q^m-q^i)\right].}
\]
For pairs this specializes to
\[
\boxed{N_{r,2}(q)=q^{4r+5}+q^{2r+8}-q^{2r+5}},
\qquad
\boxed{\Pr(XY=YX)=q^{-3}+q^{-2r}-q^{-2r-3}.}
\]
The probabilities refer to independent uniform elements of the \((4+2r)\)-dimensional algebra, not to conjugacy classes.

## Assumptions and scope
All fields and characteristics, including characteristic two, are allowed. The integer \(r\) counts **parallel oriented arrows**; \(m\) counts independently labeled elements, each chosen from the full unital algebra. The variety is the reduced common zero locus of all commutators. Components, dimensions and intersections are geometric (after extension to an algebraic closure). No claim of reducedness of the original commutator scheme is made.

A basis of \(T_r\) is \(e_1,e_2,a_1,\ldots,a_r,b_1,\ldots,b_r,p_1,p_2\), where \(a_i\) is a forward arrow, \(b_i\) its dual reverse arrow, and \(p_j\) is dual to \(e_j\). The nonzero products of basis vectors are precisely those imposed by
\[
e_i^2=e_i,\quad e_1a_i=a_i=a_ie_2,\quad e_2b_i=b_i=b_ie_1,\quad
 a_i b_j=\delta_{ij}p_1,\quad b_j a_i=\delta_{ij}p_2,\quad e_jp_j=p_j=p_je_j.
\]
All products of three arrows and products involving a socle basis element and an arrow vanish. This presentation follows directly from the canonical dual-bimodule multiplication, not from a choice of characteristic.

## Proof
**1. Commutator reduction.** Write an arbitrary element uniquely as
\[
x=\lambda e_1+\mu e_2+\sum_{j=1}^r(u_ja_j+v_jb_j)+\rho p_1+\sigma p_2,
\]
and set \(d=\lambda-\mu\) and \(w=(u_1,\ldots,u_r,v_1,\ldots,v_r)\in W=k^{2r}\). The parameters \(\mu,\rho,\sigma\) are three free central coordinates. With \(w'=(u',v')\), direct multiplication gives
\[
[x,y]=\sum_j(du'_j-d'u_j)a_j+\sum_j(d'v_j-dv'_j)b_j
+\omega(w,w')(p_1-p_2),
\]
where \(\omega((u,v),(u',v'))=u\cdot v'-u'\cdot v\). Its matrix is nonsingular and alternating in every characteristic. Hence \(m\)-tuples commute exactly when, for every \(i<j\),
\[
d_iw_j-d_jw_i=0,\qquad \omega(w_i,w_j)=0.
\]
The remaining \(3m\) coordinates are unrestricted, giving a direct affine-space factor.

**2. Determinantal-versus-isotropic decomposition.** If \((d_1,\ldots,d_m)\ne0\), select \(j\) with \(d_j\ne0\). The first relations yield \(w_i=(d_i/d_j)w_j\) for all \(i\). They automatically imply the symplectic relations. The closure of this locus is the variety \(\mathcal D_{r,m}\) where the \(m\times(2r+1)\) matrix with rows \((d_i,w_i)\) has rank at most one. This determinantal cone is geometrically irreducible, of dimension \(m+2r\) before the affine factor.

When every \(d_i=0\), the remaining equations say that the span of the \(w_i\) is a totally isotropic subspace of \((W,\omega)\). Call this closed locus \(\mathcal I_{r,m}\). Every commuting tuple lies in the union \(\mathcal D_{r,m}\cup\mathcal I_{r,m}\). Their intersection has \(d_i=0\) and \(\operatorname{rank}(w_i)\le1\), giving dimension \(m+2r-1\) before the free factor.

**3. Irreducibility and the threshold.** For any \(0\le t\le\min(m,r)\), the rank-exactly-\(t\) stratum of isotropic tuples is a Zariski-locally trivial bundle over the symplectic isotropic Grassmannian \(\operatorname{IG}(t,2r)\), with fiber the open variety of surjections \(k^m\twoheadrightarrow k^t\). In particular its dimension is
\[
t(2r-t)-\binom{t}{2}+mt.
\]
For \(t=s=\min(m,r)\), this stratum is irreducible and dense in the whole isotropic locus: any smaller isotropic image extends to an isotropic \(s\)-plane, inside which the tuple can be deformed to have rank \(s\). These statements remain valid over an algebraic closure in characteristic two. Thus \(\mathcal I_{r,m}\) is geometrically irreducible, of the asserted dimension.

If \(r=1\), all pairwise-symplectically-orthogonal vectors in \(W=k^2\) lie on a single line; hence \(\mathcal I_{1,m}\subset\mathcal D_{1,m}\), so there is one component. If \(r\ge2\), two linearly independent vectors in an isotropic plane yield an \(\mathcal I_{r,m}\)-point outside \(\mathcal D_{r,m}\); and \(\mathcal D_{r,m}\) contains points with a nonzero \(d_i\) outside \(\mathcal I_{r,m}\). Therefore the two indicated irreducible closed sets are precisely the irreducible components. Their descriptions and all equations are defined over \(k\).

**4. Arithmetic.** With \(d=(d_1,\ldots,d_m)\ne0\), there are \((q^m-1)q^{2r}\) choices of \((d_i,w_i)\), because the \(w_i\) are determined by one common vector \(w\in\mathbb F_q^{2r}\). With \(d=0\), partition by the rank \(t\) of the isotropic span. The number of totally isotropic \(t\)-planes is \(I_{r,t}(q)\): choose an ordered isotropic basis in \(\prod_{i=0}^{t-1}(q^{2r-i}-q^i)\) ways and divide by \(|\operatorname{GL}_t(\mathbb F_q)|=\prod_{i=0}^{t-1}(q^t-q^i)\). For each isotropic plane the number of surjective maps \(\mathbb F_q^m\to\mathbb F_q^t\) is \(\prod_{i=0}^{t-1}(q^m-q^i)\). Multiply the sum and open-stratum count by \(q^{3m}\) for the unrestricted coordinates, proving the all-arity formula.

For \(m=2\), counting \(\omega(w_1,w_2)=0\) directly yields \(q^{2r}+(q^{2r}-1)q^{2r-1}\), because each nonzero \(w_1\) has a codimension-one orthogonal hyperplane. This simplifies the pair formula. Dividing by the total \(q^{2(4+2r)}\) ordered pairs gives the probability formula.

## Verification
A standalone checker `verify.py` builds the original \((4+2r)\)-dimensional multiplication law, tests associativity and the unit on basis triples over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), then exhaustively counts commuting tuples **after factoring out exactly the three proven central coordinates per tuple entry**. It evaluates the full algebra commutator for each quotient pair, not merely the reduced symplectic formula. Eleven tuple/field cases, including \((q,r,m)=(4,2,2)\) and \((2,3,3)\), agree with the exact closed formula. Run `python3 verify.py`; recorded output is in `verification_output.txt`. The checker is finite corroboration, not a proof for arbitrary fields or tuple length.

## Relationship to prior work
Schroll's 2014 work on trivial extensions of gentle algebras identifies their relationship with Brauer graph algebras and motivates studying concrete symmetric extensions; its results classify algebras, not commuting-element loci. Bennis and Fahid's 2016 work develops derivations and first cohomology of trivial extensions; it does not calculate commuting varieties. The established geometry of symplectic isotropic Grassmannians supplies a proof ingredient, not an existing assertion about commuting tuples of these extensions. Related studies of commuting varieties in reductive or nilpotent Lie algebras involve different Lie brackets. A known Kronecker **path-algebra** commuting-count result does not cover its **symmetric trivial extension**: the additional reverse arrows create the nonzero symplectic bracket. No complete equivalent theorem was found in the comparisons performed; this is not proof of historical priority.

## Limitations
The result is for full-algebra commuting tuples, not tuples of units, radical-only tuples, simultaneous conjugacy classes, or a general finite quiver. It describes reduced geometric supports, not the potentially nonreduced scheme defined by the commutator equations. Classical symplectic Grassmannian geometry is used rather than reproved from first principles. Historical-priority verification is necessarily nonexhaustive, and independent mathematical audit has not been performed.

## References
1. S. Schroll, *Trivial Extensions of Gentle Algebras and Brauer Graph Algebras*, arXiv:1405.6419, originally submitted 2014-05-25. https://arxiv.org/abs/1405.6419
2. D. Bennis and B. Fahid, *Derivations and the First Cohomology Group of Trivial Extension Algebras*, arXiv:1604.02758, originally submitted 2016-04-10. https://arxiv.org/abs/1604.02758
3. S. M. Goodwin and G. Röhrle, *On Commuting Varieties of Nilradicals of Borel Subalgebras of Reductive Lie Algebras*, arXiv:1209.1289, 2012. https://arxiv.org/abs/1209.1289
