# Characteristic-free five-term rigidity for augmented Rota–Baxter tensor products

## Finding
Let \(k\) be **any field**, of arbitrary characteristic, and fix a weight \(\lambda\in k\). For unital associative augmented Rota–Baxter algebras \((A,P_A,\varepsilon_A)\) of weight \(\lambda\), put \(e_A=1_A\varepsilon_A\). Consider a tensor-product operator with field coefficients independent of the objects:
\[
\mathscr P_{A,B}=aP_A\otimes\mathrm{id}_B+bP_A\otimes e_B+c\,\mathrm{id}_A\otimes P_B+d e_A\otimes P_B+h P_A\otimes P_B.
\]
Suppose that using \((A\otimes_k B,\mathscr P_{A,B},\varepsilon_A\otimes\varepsilon_B)\) on objects and the usual tensor on morphisms makes the entire category of augmented weight-\(\lambda\) Rota–Baxter algebras monoidal **with the ordinary algebraic associator, ordinary left and right unit maps, and unit object \((k,0,\mathrm{id}_k)\)**. Then precisely two coefficient vectors are possible:
\[
\boxed{(a,b,c,d,h)=(0,1,1,0,0)\quad\text{or}\quad(1,0,0,1,0).}
\]
Conversely both choices give the stated monoidal structure, for every field and weight.

This completes the characteristic-zero five-term uniqueness theorem of Guo–Xie–Zhang (2026, Theorem 3.6) for **all positive characteristics, including characteristic two**. The decisive missing obstruction is a four-point function-algebra calculation which does not vanish modulo two.

## Assumptions and scope
A weight-\(\lambda\) Rota–Baxter map satisfies
\[
P(x)P(y)=P(P(x)y+xP(y)+\lambda xy)
\]
for all \(x,y\) in the algebra. Here \(\varepsilon\) is a unital algebra homomorphism to \(k\) and \(\varepsilon P=0\), and \(e(x)=\varepsilon(x)1\). No commutativity of the underlying algebras is assumed. The coefficient vector is fixed across **all** objects, and only the displayed five natural operator terms are considered; no arbitrary natural transformations or modified associators are classified.

## Proof
**Step 1: the unit and associator force four discrete cases.** The ordinary left and right units yield \(c+d=1\) and \(a+b=1\), respectively. One can detect every coefficient by taking the augmented algebra \(E=k1\oplus kx\oplus ky\), with square-zero ideal \(kx\oplus ky\), \(\varepsilon(1)=1\) and \(\varepsilon(x)=\varepsilon(y)=0\). Set \(P(1)=0\). If \(\lambda=0\), set \(P(x)=y,P(y)=0\); otherwise set \(P(x)=-\lambda x,P(y)=0\). These are weight-\(\lambda\) Rota–Baxter maps: on a square-zero ideal, the nontrivial unit condition is \(P^2=-\lambda P\), which holds in either case. In particular \(\mathrm{id},e,P\) are linearly independent over every field, so their 27 triple tensor products are linearly independent operators on \(E^{\otimes 3}\).

Expanding the operator in the two ways of parenthesizing \(E^{\otimes3}\), and using the ordinary associator, coefficient comparison gives
\[
a^2=a,\quad b^2=b,\quad ab=0;\qquad c^2=c,\quad d^2=d,\quad cd=0;\qquad h(a-c)=h(b-d)=0.
\]
For a field these equations together with \(a+b=c+d=1\) imply each pair \((a,b)\) and \((c,d)\) is either \((1,0)\) or \((0,1)\). If the two pairs differ, \(h=0\), leaving exactly the two announced coefficient vectors. It remains to exclude the two equal-pair possibilities.

**Step 2: exclude the equal-pair cases at weight zero.** In the preceding algebra \(E\), now with \(\lambda=0\), evaluate the Rota–Baxter identity for \(\mathscr P\) at \(x\otimes1\) and \(1\otimes x\). With \(a=c=1\), its left and right sides are \(y\otimes y\) and \(2y\otimes y\); with \(a=c=0\), they are \(y\otimes y\) and zero. These contradictions hold in **every** characteristic (in characteristic two, \(2y\otimes y=0\), still not \(y\otimes y\)). The scalar \(h\) cancels in these tests.

**Step 3: constrain the equal-pair cases at nonzero weight.** Suppose \(\lambda\ne0\). On \(D=k[t]/(t^2)\), use the standard augmentation and \(P_D=-\lambda(\mathrm{id}-e)\). Evaluating the Rota–Baxter identity for \(\mathscr P_{D,D}\) at \(t\otimes1,1\otimes t\) gives the necessary conditions
\[
 h=\lambda^{-1}\quad\text{if }a=c=1,\qquad h=-\lambda^{-1}\quad\text{if }a=c=0.
\]
Indeed its left side is \(\lambda^2 t\otimes t\) in both cases; its right side is respectively \((2\lambda^2-h\lambda^3)t\otimes t\) and \(-h\lambda^3t\otimes t\). These identities are valid independently of characteristic.

**Step 4: exclude the first candidate at nonzero weight.** Let \(F_3=k^{\{0,1,2\}}\) with pointwise multiplication, \(\varepsilon(f)=f(0)\), and
\[
(Pf)(j)=\lambda\sum_{i<j}f(i).
\]
The sum is zero when the index set is empty. This is a weight-\(\lambda\) Rota–Baxter operator because in \((Pf)(j)(Pg)(j)\), pairs of indices partition into \(i<\ell\), \(\ell<i\), and \(i=\ell\). It also satisfies \(\varepsilon P=0\). Write \(\delta_i\) for the coordinate idempotents. For \(a=c=1\), \(h=\lambda^{-1}\), the difference between the two sides of the Rota–Baxter identity, evaluated at \(\delta_0\otimes\delta_1\) and \(\delta_1\otimes\delta_0\), is
\[
\lambda^2(\delta_1+\delta_2)\otimes(\delta_1+\delta_2)\ne0.
\]
This is the three-point obstruction of Guo–Xie–Zhang, which works over every field.

**Step 5: a characteristic-free four-point obstruction excludes the second candidate.** Instead take \(F_4=k^{\{0,1,2,3\}}\) with the same augmentation and exclusive prefix-sum operator. Write \(u=\delta_2+\delta_3\) and take
\[
X=\delta_1\otimes\delta_1,\qquad Y=\delta_1\otimes\delta_2.
\]
For the remaining symmetric candidate \((a,b,c,d,h)=(0,1,0,1,-\lambda^{-1})\), \(e(\delta_1)=e(\delta_2)=0\) and \(P(\delta_1)=\lambda u\), \(P(\delta_2)=\lambda\delta_3\). Hence
\[
\mathscr P(X)=h\lambda^2u\otimes u,\qquad \mathscr P(Y)=h\lambda^2u\otimes\delta_3.
\]
The pointwise products \(XY\), \(\mathscr P(X)Y\) and \(X\mathscr P(Y)\) all vanish, because \(\delta_1u=0\) and \(\delta_1\delta_2=0\). Thus the **right** side of the Rota–Baxter identity is zero, whereas its **left** side is
\[
\mathscr P(X)\mathscr P(Y)=h^2\lambda^4u\otimes\delta_3=\lambda^2u\otimes\delta_3\ne0.
\]
The nonzero coefficient is \(\lambda^2\), not \(2\lambda^2\); this contradiction remains valid in characteristic two. There are no surviving equal-pair cases.

**Step 6: sufficiency.** Guo–Xie–Zhang, Theorems 3.2 and 3.3 and Proposition 3.5, prove that the two displayed formulas define augmented weight-\(\lambda\) Rota–Baxter operators natural in the objects, compatible with the ordinary associator and unit maps. Those constructions and proofs work over general commutative base rings, hence over every field. Combining this with Steps 1–5 gives the claimed classification. \(\square\)

## Verification
The standalone program `verify.py` uses finite prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and function algebras of two, three and four points. It independently evaluates the Rota–Baxter identity on **all pairs of coordinate idempotents**, checks the two surviving operators, excludes the two symmetric candidates, and confirms that the subtle characteristic-two candidate passes the three-point test but fails on four points. It prints `VERIFY_OK` when every assertion holds. Run `python3 verify.py` from this directory. These finite checks are corroboration only; the preceding algebraic argument proves the statements over all fields.

## Relationship to prior work
Guo, Xie and Zhang (arXiv:2610.17525v1, first public October 13, 2026), Section 3.2, Theorem 3.6, already prove this five-term classification **in characteristic zero** and derive Steps 1–4. Their last test of the second symmetric candidate gives \(2\lambda^2\delta_2\otimes\delta_2\), which does not rule out characteristic two. The four-point argument in Step 5 provides the missing characteristic-independent exclusion. Their positive construction in Theorems 3.2–3.3 and Proposition 3.5 is unchanged. The predecessor Zheng–Guo–Qiu (arXiv:2401.11363v2), Eq. (25), constructs an oriented operator for a particular free commutative algebra, not a classification of five-term formulas on the entire augmented category.

## Limitations
This theorem says nothing about monoidal structures with different unit/associativity constraints, other possible natural transformations, nonconstant coefficients, general base rings with nontrivial idempotents, or subcategories of the full augmented category. The five-term ansatz is essential. The four-point construction is an obstruction, not a claim about minimal possible witness size. The attached computations are finite corroboration and are not an independent mathematical audit.

## References
1. Li Guo, Yunzhou Xie, Yi Zhang, *Monoidal structure on Rota-Baxter algebras via augmentation, and free cocycle bialgebras*, arXiv:2610.17525v1 (2026), especially Section 3, Theorems 3.2, 3.3, 3.6, Proposition 3.5. https://arxiv.org/abs/2610.17525
2. Shanghua Zheng, Li Guo, Huizhen Qiu, *Extended Rota-Baxter algebras, diagonally colored Delannoy paths and Hopf algebras*, arXiv:2401.11363v2 (2024), especially Eq. (25). https://arxiv.org/abs/2401.11363
