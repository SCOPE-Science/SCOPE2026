# Exact periodic squaring spectra of the Hu–Wen evolution-algebra family over odd finite fields

## Finding
Let \(K=\mathbb F_q\) have odd characteristic \(p\), let \(\lambda\in K^\times\), and let \(E_\lambda\) be the three-dimensional evolution algebra with natural basis \(e_1,e_2,e_3\) and products
\[
e_1^2=-e_1-e_3,\qquad e_2^2=-2e_1+\lambda e_2+(\lambda-2)e_3,\qquad e_3^2=e_1+e_3,
\]
all mixed products between distinct basis elements being zero. Put \(Q(x)=x^2\), regarded as a nonlinear self-map of the finite set \(E_\lambda\). For every integer \(m\ge1\), write \(F_m(\lambda,q)=|\{x:Q^{\circ m}(x)=x\}|\), and set \(g_m=\gcd(2^m-1,q-1)\).

**Theorem (complete periodic squaring spectrum).** If \(\lambda\ne2\) and \(t=2/\lambda\in K^\times\), then
\[
\boxed{F_m(\lambda,q)=1+g_m\bigl(1+(q-1)\mathbf1_{t^m=1}\bigr).}
\]
For the idempotent-free exceptional member \(\lambda=2\), instead
\[
\boxed{F_m(2,q)=\begin{cases}1,&p\nmid m,\\1+qg_m,&p\mid m.\end{cases}}
\]
Here \(2\) denotes the image of the integer in \(K\), and \(\mathbf1\) is the stated condition's indicator. The number of points having *least* period exactly \(m\), and the number of distinct cycles of length \(m\), are respectively
\[
\boxed{P_m=\sum_{d\mid m}\mu(m/d)F_d,\qquad C_m=P_m/m.}
\]
These expressions determine the complete cycle-length distribution and the finite dynamical zeta function \(\exp(\sum_{m\ge1}F_m z^m/m)=\prod_{m\ge1}(1-z^m)^{-C_m}\).

Let \(h\) be the odd part of \(q-1\). **For every admissible \(\lambda\), the complete periodic locus has exactly \(1+qh\) points**, even though the period distributions depend sharply on \(\lambda\). At \(\lambda=2\), every nonzero periodic point has least period divisible by \(p\); consequently the algebra has no nonzero idempotent but does have nonzero periodic points. For example, over \(\mathbb F_3\) it has one fixed point and one 3-cycle; over \(\mathbb F_5\) it has one fixed point and one 5-cycle; over \(\mathbb F_7\) it has one fixed point, one 7-cycle and one 14-cycle.

## Assumptions and scope
All fields here are finite fields of odd characteristic. The parameter \(\lambda\) is nonzero, and \(Q\) is the *elementwise quadratic map* \(x\mapsto x^2\), not the basis-dependent linear evolution operator sending \(e_i\) to \(e_i^2\). Iteration means composition of this quadratic map, not associative exponentiation in a nonassociative algebra. This distinction is essential.

Every periodic point belongs to \(E_\lambda^2\), because \(Q(E_\lambda)\subseteq E_\lambda^2\). With \(u=e_1+e_3\) and \(v=e_2+e_3\), the stable square \(S=E_\lambda^2=Ku\oplus Kv\) obeys
\[
u^2=0,\qquad uv=u,\qquad v^2=-u+\lambda v.
\]
The algebra is non-solvable and its stable square has these products for all admissible parameters; these background properties were established by Hu and Wen.

## Proof
For \(a,b\in K\), the square of \(au+bv\) is
\[
Q(au+bv)=(2ab-b^2)u+\lambda b^2v.
\]
Set \(c=\lambda b\). The coordinates \((c,a)\in K^2\) identify the stable square with \(K^2\), and the quadratic map becomes
\[
\boxed{c'=c^2,\qquad a'=(2/\lambda)ca-c^2/\lambda^2.}\tag{1}
\]
If \(\lambda\ne2\), set
\[
t=2/\lambda,\qquad \alpha=1/[\lambda(2-\lambda)],\qquad y=a-\alpha c.
\]
Substitution in (1) gives the exact skew-product conjugacy
\[
(c,y)\longmapsto(c^2,tcy).
\]
A direct induction gives
\[
\boxed{Q^{\circ m}(c,y)=(c^{2^m},t^m c^{2^m-1}y).}\tag{2}
\]
For \(c=0\), the only point fixed by a positive iterate is \((0,0)\). For \(c\ne0\), fixedness of the first coordinate means \(c^{2^m-1}=1\). There are exactly \(g_m\) such elements because \(K^\times\) is cyclic of order \(q-1\). Under that condition, the second coordinate in (2) is \(t^m y\). Its fixed-point set has size \(q\) if \(t^m=1\), and size one otherwise. This proves the first formula.

If \(\lambda=2\), division by \(2\) and \(4\) is allowed because \(p\ne2\). Formula (1) becomes
\[
(c,a)\longmapsto(c^2,ca-c^2/4).
\]
A separate induction, including the affine drift term, yields
\[
\boxed{Q^{\circ m}(c,a)=\bigl(c^{2^m},c^{2^m-1}a-(m/4)c^{2^m}\bigr).}\tag{3}
\]
Indeed, multiplication of the second coordinate by \(c^{2^m}\), followed by subtraction of \(c^{2^{m+1}}/4\), changes the drift coefficient from \(m/4\) to \((m+1)/4\). Again \(c=0\) contributes just the zero point. For each of the \(g_m\) nonzero solutions of \(c^{2^m-1}=1\), (3) reduces to \(a'=a-(m/4)c\). Every \(a\in K\) is fixed if \(p\mid m\); none is fixed otherwise. This proves the second formula and the divisibility assertion about least periods.

To count the full periodic locus, note that \(c\mapsto c^2\) on \(K^\times\) has periodic points precisely when \(c\) has odd multiplicative order. Thus there are exactly \(h\) periodic nonzero values of \(c\). Fix one, and let \(k\) be its least squaring period. In the nonexceptional case, the return map on the fiber \(\{c\}\times K\) is \(y\mapsto t^ky\), a permutation of finite order. In the exceptional case it is \(a\mapsto a-(k/4)c\), a translation of order dividing \(p\). Thus **every** point in every such fiber is periodic. For \(c=0\), only the origin is periodic. This gives \(1+qh\). Finally, Möbius inversion of \(F_m=\sum_{d\mid m}P_d\) gives \(P_m\) and then \(C_m=P_m/m\), completing the proof.

## Verification
The supplied `verify.py` evaluates the original three-dimensional multiplication table, independently of the coordinate conjugacies (2) and (3). It enumerates every point in the stable square, compares direct iterate fixed-point counts with both closed formulas, and separately determines all periodic points by orbit detection. The verifier covers \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13},\mathbb F_9\), and a representative-parameter sample over \(\mathbb F_{25}\), using explicit quadratic-field arithmetic rather than pretending that a composite field is integer modular arithmetic. In total, 636 independently evaluated parameter-and-iterate comparisons pass, together with periodic-locus checks.

For \(\lambda=2\), the first formula gives \(F_1=1\), in agreement with the already-established idempotent-free exception. The experiment is corroboration only: the unlimited claim in \(q\), \(m\), and \(\lambda\) follows from the two exact induction arguments and finite-field cyclicity.

## Relationship to prior work
Hu and Wen introduced the displayed non-solvable family, determined its stable square and every idempotent, and singled out \(\lambda=2\) as idempotent-free. Their theorem determines \(F_1\), but does not describe iterated squaring, the cycle spectra \(F_m\) for arbitrary \(m\), or the characteristic-dependent divisibility of every nontrivial period in the exceptional member. Their complete openly accessible preprint was inspected (Theorem 1, Lemma 1, Proposition 1, and the discussion of the stable square).

The published result *A single symmetry jump in the \(E_\lambda\) evolution-algebra family* computes linear algebra automorphism groups; its full displayed proof concerns stabilizers of multiplication, rather than the nonlinear self-map \(x\mapsto x^2\). The historical survey by Ceballos and collaborators discusses the *linear*, natural-basis-dependent evolution operator and its plenary-power theory, not these finite-field quadratic-map cycles. Earlier population-evolution studies use other algebras and dynamical systems. None of the inspected statements implies the present full parameter-and-period formula. Historical equivalence through general finite-field monomial skew-product dynamics remains possible and is an explicit residual literature risk.

## Limitations
The theorem is specific to the Hu–Wen family over odd finite fields. It does not classify periodic squaring on arbitrary evolution algebras, coefficient characteristic two, or all preperiodic tail lengths. Nor does it claim that polynomial skew-product iteration itself is new; the contribution is the complete, resonance-sensitive periodic spectrum of this naturally motivated algebra family. The originality assessment is based on finite searches and material source comparisons, not exhaustive world-literature coverage or independent priority certification.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb C\)*, arXiv:2609.25023v1 (2026); openly accessible version at https://www.preprints.org/manuscript/202609.0078 .
2. *A single symmetry jump in the \(E_\lambda\) evolution-algebra family* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-a-single-symmetry-jump-in-the-e-lambda-evolution-algebra-family--1a1e7e2dd0e3/RESULT.md .
3. M. Ceballos et al., *A historical perspective of Tian's evolution algebras*, arXiv:2604.13126v1, https://arxiv.org/html/2604.13126v1 .
4. U. A. Rozikov and M. V. Velasco, *A discrete-time dynamical system and an evolution algebra of mosquito population*, J. Math. Biol. 78 (2019), 1225–1244, doi:10.1007/s00285-018-1307-x.
