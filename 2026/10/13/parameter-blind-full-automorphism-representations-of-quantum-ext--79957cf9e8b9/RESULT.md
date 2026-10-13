# Parameter-blind full automorphism representations of quantum exterior algebras over finite fields

## Finding

For each finite field \(k=\mathbb F_q\), consider the four-dimensional quantum complete intersections
\[
A_\lambda=k\langle x,y\rangle/(x^2,y^2,yx-\lambda xy),\qquad
\lambda\in k^\times\setminus\{1,-1\}.
\]
Use the ordered vector-space basis \((1,x,y,z)\), where \(z=xy\). All members have the **same full automorphism subgroup of \(\operatorname{GL}_4(k)\)** in these coordinates:
\[
G(k)=\left\{\begin{pmatrix}1&0&0&0\\0&a&0&0\\0&0&b&0\\0&c&d&ab\end{pmatrix}:a,b\in k^\times,\ c,d\in k\right\}.
\]
Despite this identical faithful linear representation, two algebras in the family are isomorphic if and only if \(\mu=\lambda\) or \(\mu=\lambda^{-1}\). Thus there are exactly \((q-3)/2\) mutually nonisomorphic members with the same symmetry representation for odd \(q\), or \((q-2)/2\) for even \(q\). These numbers become unbounded with \(q\).

The complete fixed-space distribution of \(G(k)\) on \(A_\lambda\), counting the unit as a fixed direction, is
\[
N_1=q^2(q-2)(q-3),\quad N_2=3q^2(q-2),\quad
N_3=q^2-1,\quad N_4=1.
\]
The action on all elements has precisely \(5q\) orbits, with orbit-size multiset
\[
\left\{1^{\times q},\ (q-1)^{\times q},\
\bigl(q(q-1)\bigr)^{\times2q},\
\bigl(q(q-1)^2\bigr)^{\times q}\right\}.
\]
The algebra has exactly \(q+5\) two-sided ideals, in seven automorphism orbits with sizes \(1,1,1,1,1,1,q-1\). The unordered eigenvalues of the Nakayama automorphism on the radical quotient are \(\{\lambda,\lambda^{-1}\}\), so this intrinsic datum distinguishes parameters that the full ordinary linear automorphism action cannot distinguish.

## Assumptions and scope

The field \(k=\mathbb F_q\) has arbitrary positive characteristic, including \(2\), and \(q\) is any prime power for which \(k^\times\setminus\{1,-1\}\ne\varnothing\), equivalently \(q\ge4\). The algebra is associative, unital, and a \(k\)-algebra; automorphisms and isomorphisms fix \(k\) pointwise. Its Jacobson radical \(J=(x,y)\) has basis \((x,y,z)\), its square is \(J^2=kz\), and \(J^3=0\). The only products in \(J\) that need not vanish are \(xy=z\) and \(yx=\lambda z\). Here a fixed-space dimension always means the dimension in the **whole unital vector space**, not merely in \(J\).

## Proof

**Automorphisms.** An algebra automorphism preserves the radical filtration and acts invertibly on \(J/J^2\). Write its generator images as \(f(x)=ax+by+cz\) and \(f(y)=dx+ey+fz\). Their squares vanish precisely when \((1+\lambda)ab=(1+\lambda)de=0\). Since \(\lambda\ne-1\), both columns of the induced invertible \(2\times2\) matrix have at most one nonzero entry, and hence the matrix is either diagonal or antidiagonal. In the antidiagonal case the relation \(yx=\lambda xy\), imposed after applying \(f\), would give \(\lambda^2=1\), excluded. Thus \(f(x)=ax+cz\), \(f(y)=by+dz\) with \(a,b\ne0\), and \(f(z)=abz\). Conversely every such map respects the defining relations and is an automorphism because its matrix is triangular with nonzero diagonal. This proves the displayed group formula and \(|G(k)|=q^2(q-1)^2\).

**Nonisomorphism and its intrinsic witness.** For an isomorphism \(A_\lambda\to A_\mu\), the same square-zero argument in the target makes the radical-quotient matrix monomial. In the diagonal case, preservation of the mixed relation forces \(\lambda=\mu\); in the antidiagonal case it forces \(\lambda\mu=1\). Identity and generator exchange, respectively, realize the converse cases. For the Frobenius functional \(\ell\) extracting the \(z\)-coefficient, the Nakayama automorphism defined by \(\ell(uv)=\ell(v\nu(u))\) satisfies \(\nu(x)=\lambda^{-1}x\), \(\nu(y)=\lambda y\). Its eigenvalues on \(J/J^2\) thus give an independent isomorphism invariant up to inversion. In the generic parameter set the involution \(\lambda\mapsto\lambda^{-1}\) has no fixed points, because a fixed point would satisfy \(\lambda^2=1\); this yields the stated counts for odd and even fields.

**Fixed-space distribution.** In the basis \((1,x,y,z)\), the restriction of \(f-1\) to the radical is triangular, with diagonal \((a-1,b-1,ab-1)\) and bottom row \((c,d,ab-1)\). If \(a,b\ne1\) and \(ab\ne1\), its rank is \(3\) and the full fixed space has dimension \(1\). There are \((q-2)(q-3)\) such choices of \((a,b)\), each with \(q^2\) choices of \((c,d)\). If exactly one of \(a,b\) equals \(1\), or if \(ab=1\) with \(a,b\ne1\), the radical-fixed dimension is \(1\) and the full fixed dimension is \(2\); altogether there are \(3(q-2)q^2\) such automorphisms. If \(a=b=1\), then nonzero \((c,d)\) gives radical rank \(1\), hence full fixed dimension \(3\), while \((c,d)=(0,0)\) gives the identity with fixed dimension \(4\). Summing gives the stated \(N_j\), whose sum is \(q^2(q-1)^2\).

**Element orbits.** Write an arbitrary element \(r+ux+vy+tz\) with \(r,u,v,t\in k\). Its scalar coordinate \(r\) is fixed. For each \(r\), the five orbits are \((u,v,t)=(0,0,0)\), \((u,v)=(0,0),t\ne0\), \(u\ne0,v=0\), \(u=0,v\ne0\), and \(u,v\ne0\), with sizes respectively \(1,q-1,q(q-1),q(q-1),q(q-1)^2\). The diagonal scalings act transitively on every indicated nonzero support type, and whenever \((u,v)\ne(0,0)\), the free parameters \((c,d)\) shift \(t\) arbitrarily. This proves all orbit sizes. Independently, Burnside's lemma and the fixed-space distribution give
\[
\frac{\sum_{j=1}^4 N_jq^j}{q^2(q-1)^2}=5q.
\]

**Ideal orbits.** Every proper ideal lies in \(J\). If a proper ideal contains an element with a nonzero image in \(J/J^2\), multiplying that element by \(x\) and \(y\) shows it contains \(z\) (because \(\lambda\ne0\)). Therefore the full list of ideals is
\[
0,\quad kz,\quad J,\quad A_\lambda,\quad
I_{[u:v]}=k(ux+vy)+kz\quad([u:v]\in\mathbb P^1(k)).
\]
There are \(q+5\) in all. The four non-line ideals are characteristic. The diagonal quotient action fixes the two coordinate projective points \([1:0]\), \([0:1]\), and is transitive on the other \(q-1\) points. Hence the seven ideal-orbit sizes are exactly \(1,1,1,1,1,1,q-1\).

## Verification

The standalone file `verify.py` uses only Python 3 standard-library facilities. Run `python3 verify.py` from its directory. It independently enumerates every invertible relation-preserving pair of radical generator images, all group elements and their fixed-space ranks, full element-orbit partitions, every linear subspace of the radical and its two-sided-ideal test, and ideal orbits. For \(q=4,5,7,8,9\) it checks every admissible \(\lambda\) using explicit arithmetic in prime fields and two extension-field models, and prints `VERIFY_OK` on success. The respective fixed-space spectra \((N_1,N_2,N_3,N_4)\) are \((32,96,15,1)\), \((150,225,24,1)\), \((980,735,48,1)\), \((1920,1152,63,1)\), and \((3402,1701,80,1)\). This finite computation corroborates, but does not replace, the preceding proof for every prime power.

## Relationship to prior work

Buchweitz–Green–Madsen–Solberg [1] study exactly this family under the equivalent parameter convention \(xy+\eta yx=0\); their research addresses Hochschild cohomology and homological pathologies, not finite-field full linear automorphism-action coincidence. Hou–Xu [2] investigate a \(\mathbb Z_2\times\mathbb Z_2\)-Galois covering and its Hochschild invariants. Bergh–Erdmann [3] analyze quantum-complete-intersection module and stable Auslander–Reiten theory. Lambre–Zhou–Zimmermann [4], notably Remark 3.6 and Section 5.3, discuss the same parameter family, its Nakayama eigenvalues, and Hochschild–BV theory; those antecedents motivate the distinction between Nakayama-sensitive and automorphism-representation-blind data. Their results are not asserted to give the simultaneous full group representation, exact finite-field fibers, element-orbit multisets, and two-sided ideal action. The algebra and its homological context are prior work; the assertion here concerns their exact parameter-blind full automorphism action and its limitations as a classification invariant.

## Limitations

All automorphisms are \(k\)-linear; the result does not classify semilinear maps involving field automorphisms. The exceptional parameters \(\lambda=0,1,-1\) are deliberately excluded, and no formula here is claimed for them. No comparison with all possible isomorphism invariants or all forms of representation-theoretic equivalence is claimed. Existing literature may contain an equivalent group-action statement under alternative quantum-plane terminology; absence from the inspected sources does not prove exhaustive novelty. Numerical verification covers only the five named finite fields; the generality comes solely from the proof.

## References

[1] R.-O. Buchweitz, E. L. Green, D. Madsen, Ø. Solberg, *Finite Hochschild cohomology without finite global dimension*, arXiv:math/0407108v1 (first public 2004-07-07); published in Mathematical Research Letters 12 (2005), 805–816. https://arxiv.org/abs/math/0407108

[2] H. Bo and X. Yunge, *Hochschild (co)homology of \(\mathbb Z_2\times\mathbb Z_2\)-Galois coverings of quantum exterior algebras*, Bulletin of the Australian Mathematical Society 78 (2008), 35–54. DOI:10.1017/S0004972708000312. https://doi.org/10.1017/S0004972708000312

[3] P. A. Bergh and K. Erdmann, *The stable Auslander–Reiten quiver of a quantum complete intersection*, arXiv:0909.5568v1 (2009). https://arxiv.org/abs/0909.5568

[4] T. Lambre, G. Zhou, A. Zimmermann, *The Hochschild cohomology ring of a Frobenius algebra with semisimple Nakayama automorphism is a Batalin–Vilkovisky algebra*, arXiv:1405.5325v1 (2014). https://arxiv.org/abs/1405.5325
