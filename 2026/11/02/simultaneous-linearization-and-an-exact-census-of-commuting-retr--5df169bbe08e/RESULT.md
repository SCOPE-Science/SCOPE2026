# Simultaneous linearization and an exact census of commuting retractions of truncated free associative algebras

## Finding
Let \(k\) be any field, \(n\geq1\), \(L\geq2\), and \(m\geq1\). Write \(V=k^n\) and let \(A_{n,L}=\bigoplus_{d=1}^{L}V^{\otimes d}\) be the **nonunital** free associative algebra truncated above word length \(L\), with truncated concatenation product. Suppose \(E_1,\ldots,E_m\) are algebra endomorphisms of \(A_{n,L}\) satisfying \(E_i^2=E_i\) and \(E_iE_j=E_jE_i\) for all \(i,j\).

**Simultaneous linearization theorem.** There exists an algebra automorphism \(g\in\operatorname{Aut}(A_{n,L})\) such that each \(gE_i g^{-1}\) is the degreewise tensor extension of a linear projection \(P_i:V\to V\), and the \(P_i\) commute. Two ordered tuples are conjugate if and only if the dimensions of their simultaneous eigenspaces on \(A_{n,L}/A_{n,L}^2\cong V\) agree. Thus they are classified over every field by \(2^m\) nonnegative integers \(n_\epsilon\), indexed by \(\epsilon\in\Omega=\{0,1\}^m\), with \(\sum_\epsilon n_\epsilon=n\).

**Complete finite-field census.** If \(k=\mathbb F_q\), define
\[
S=\sum_{d=2}^{L}n^d,\qquad
M_\epsilon(\mathbf n)=\sum_{d=2}^{L}\ \sum_{\epsilon_1\wedge\cdots\wedge\epsilon_d=\epsilon}
\prod_{j=1}^{d}n_{\epsilon_j},\qquad
H(\mathbf n)=\sum_{\epsilon\in\Omega}n_\epsilon M_\epsilon(\mathbf n),
\]
where \(\wedge\) is coordinatewise Boolean AND; the inner sum is over ordered \(d\)-tuples of weights. The number of commuting ordered retraction tuples with the prescribed eigenspace dimensions is precisely
\[
\boxed{C_{\mathbf n}(q)=\frac{|\operatorname{GL}_n(q)|}{\prod_{\epsilon\in\Omega}|\operatorname{GL}_{n_\epsilon}(q)|}\,q^{nS-H(\mathbf n)}.}
\]
Here \(|\operatorname{GL}_0(q)|=1\), and the numerator is \(\prod_{j=0}^{n-1}(q^n-q^j)\). The total number of tuples is \(\sum_{\sum n_\epsilon=n}C_{\mathbf n}(q)\).

For the rank of each endomorphism on the **whole** algebra, put \(r_i=\sum_{\epsilon:\epsilon_i=1}n_\epsilon\). Its rank is exactly \(\rho_i=\sum_{d=1}^{L}r_i^d\). Consequently
\[
\boxed{\mathcal R_{n,L,m}(z_1,\ldots,z_m)
=\sum_{\sum n_\epsilon=n}C_{\mathbf n}(q)\prod_{i=1}^m z_i^{\sum_{d=1}^{L}r_i^d}}
\]
is the complete joint linear-rank enumerator (coefficients count actual ordered algebra endomorphisms, not conjugacy classes).

For \(n=2\), \(L=2\), \(m=2\), the total simplifies to
\[
\boxed{4+(q+1)(5q^5+q^7).}
\]
The five comparable pairs of distinct Boolean weights each give \(q^5(q+1)\) tuples, whereas the unique incomparable weight pair gives \(q^7(q+1)\); four singleton-weight decompositions give one tuple each. The extra factor \(q^2\) for incomparable supports is a genuine nonlinear deformation effect and is absent from the mere linear-projection classification.

## Assumptions and scope
The algebra is the positive-degree tensor algebra \(T^+(V)\) modulo all words of degree \(L+1\) or greater. No commutativity, unit, algebraic closure, or restriction on the field characteristic is assumed. Every algebra homomorphism is \(k\)-linear. All tuple indices are ordered, all endomorphisms are ordinary algebra endomorphisms, and their composition is ordinary map composition. The classification applies to all fields; the counting polynomials apply to every prime power \(q\).

## Proof
**Step 1 (endomorphisms and automorphisms).** Each endomorphism is uniquely determined by arbitrary elements \(E(v)\in A_{n,L}\) assigned linearly to the generators \(v\in V\). Every such assignment extends to an endomorphism because products of \(L+1\) images vanish. The linear part \(P_E:V=A/A^2\to V\) determines the action on the graded quotient \(A^d/A^{d+1}\cong V^{\otimes d}\) as \(P_E^{\otimes d}\). Consequently an endomorphism is invertible precisely when \(P_E\) is invertible. Over \(\mathbb F_q\) this gives \(|\operatorname{Aut}(A_{n,L})|=|\operatorname{GL}_n(q)|q^{nS}\), since there are \(nS\) freely chosen coefficients of degree at least two.

**Step 2 (degreewise elimination).** The linear parts \(P_i\) of commuting idempotents are commuting idempotent linear maps and therefore have a simultaneous decomposition \(V=\bigoplus_{\epsilon\in\Omega}V_\epsilon\), with \(P_i\) acting as the scalar bit \(\epsilon_i\) on \(V_\epsilon\). No field restriction is needed because \(t(t-1)\) has distinct roots in all characteristics.

Lift each \(P_i\) to the graded endomorphism \(\widetilde P_i\). Suppose by induction that all differences \(E_i-\widetilde P_i\), evaluated on generators, have zero components of degrees below \(d\) (with \(2\le d\le L\)). Let \(f_i:V\to V^{\otimes d}\) denote the degree-\(d\) component. On a source eigenspace \(V_s\) and target tensor eigenspace \((V^{\otimes d})_t\), write \(f_i^{t,s}\) for this component. The tensor target's weight \(t\) is the coordinatewise AND of its letter weights. Idempotence yields
\[
(s_i+t_i-1)f_i^{t,s}=0,
\]
and commutativity yields
\[
(s_j-t_j)f_i^{t,s}=(s_i-t_i)f_j^{t,s}.
\]
When \(s=t\), the first equation forces every \(f_i^{t,s}=0\): the scalar is \(1\) or \(-1\). When \(s\neq t\), choose any \(i\) with \(s_i-t_i\neq0\); the second equation implies \(f_j^{t,s}=(s_j-t_j)h^{t,s}\) for a single linear map \(h^{t,s}\). Define the degree-\(d\) shear \(g(v)=v-h(v)\), where \(h\) comprises these components and is zero on equal-weight components. Its linear part is the identity, so it is an automorphism. The degree-\(d\) correction in \(gE_i g^{-1}\) becomes \(f_i-hP_i+P_i^{\otimes d}h=f_i-(s_i-t_i)h=0\). Earlier degrees remain zero. Induction through \(L\) proves simultaneous linearization in every characteristic.

**Step 3 (uniqueness of the orbit invariant).** Algebra conjugation restricts to linear conjugation on \(V=A/A^2\), hence preserves the simultaneous weight-space dimensions. Conversely, two sets of commuting linear projections with the same dimensions are simultaneously linearly conjugate by a member of \(\operatorname{GL}_n(k)\), whose tensor extension is an algebra automorphism. Together with Step 2, this gives exactly one algebra-automorphism orbit for each nonnegative weight dimension vector summing to \(n\).

**Step 4 (stabilizers and counts).** Fix a graded representative. An automorphism commutes with every \(\widetilde P_i\) precisely when its linear part preserves each \(V_\epsilon\), and the image of a generator in \(V_\epsilon\) has higher-degree terms entirely in the weight-\(\epsilon\) tensor space. The degree-at-least-two weight-\(\epsilon\) space has dimension \(M_\epsilon(\mathbf n)\), so there are exactly \(q^{H(\mathbf n)}\) choices of nonlinear coefficients. Its stabilizer therefore has order \(\prod_\epsilon|\operatorname{GL}_{n_\epsilon}(q)|q^{H(\mathbf n)}\). The orbit–stabilizer formula and Step 1 yield \(C_{\mathbf n}(q)\). Finally, \(\widetilde P_i\) is the identity on precisely the tensor powers of its linear image of dimension \(r_i\), giving \(\rho_i=\sum_{d=1}^{L}r_i^d\) and the rank enumerator.

**Step 5 (two-generator example).** For \(n=2,L=2,m=2\), weight distributions either put both generators in one of four weights, or put one generator in each of two different weights. Among the six distinct unordered pairs of weights in \(\{0,1\}^2\), five are comparable and have \(H=4\), while \(01\) and \(10\) are incomparable and have \(H=2\). Since \(nS=8\) and \(|\operatorname{GL}_2(q)|/(q-1)^2=q(q+1)\), Step 4 gives the displayed total.

## Verification
The independently constructed checker `verify.py` enumerates original algebra homomorphisms on \(\mathbb F_q\langle x,y\rangle/(\text{words of length}\ge3)\) as images of two generators, multiplies their images directly in the six-dimensional algebra, checks the idempotence equations, and then checks commutation by composing homomorphisms. It does **not** assume simultaneous linearizability when selecting the candidates.

It exhaustively inspected all \(4096\) endomorphisms over \(\mathbb F_2\), all \(531441\) over \(\mathbb F_3\), all \(9604\) ordered pairs of binary idempotent endomorphisms, all \(948676\) ordered pairs of ternary idempotent endomorphisms, and all \(941192\) ordered triples of binary idempotent endomorphisms. The respective idempotent totals were \(98\) and \(974\); commuting pair totals were \(868\) and \(13612\); the commuting binary triple total was \(5288\). Every complete weight-dimension histogram agreed with the formula. Full output is in `verification_output.txt`. These finite experiments are cross-checks, not substitutes for the all-field induction proof.

## Relationship to prior work
Work of Berzins (2005) and Lipyanski (2005) studies automorphisms **of the endomorphism semigroup** of free associative or relatively free nilpotent algebras. Their main results do not state the automorphism-conjugacy classification of arbitrary commuting idempotent *elements* of that semigroup, nor the complete finite-field orbit sizes and joint-rank enumerator. Fountain and Gould (2007) address idempotent generation questions for endomorphism monoids of stable basis algebras, a different problem. Mikhalev and Yu (1998) characterize retracts in several types of free Nielsen–Schreier algebras; that related work has not been read in full and is a residual priority risk. Simultaneous diagonalization of commuting linear projections and the ordinary \(\operatorname{GL}_n\) part of the count are standard; the contribution claimed here is the explicit all-arity simultaneous **algebra** linearization and nonlinear weight-sensitive finite-field census.

## Limitations
The free nilpotent associative algebra is essential: a quotient by further relations may obstruct the required generator shears. The theorem does not classify arbitrary (non-idempotent) endomorphisms, noncommuting retraction tuples, or endomorphism-conjugacy under noninvertible maps. It concerns set-theoretic rational points and algebra automorphism orbits, not the reducedness or geometry of the defining representation schemes. Although direct searches found no equivalent formula, a broader formal-linearization or semilattice-action theorem could subsume part of the claim; historical priority is provisional and independent mathematical audit is not performed.

## References
- A. Berzins, *The group of automorphisms of semigroup of endomorphisms of free commutative and free associative algebras*, arXiv:math/0504015 (first public version 2005-04-01), https://arxiv.org/abs/math/0504015.
- R. Lipyanski, *Automorphisms of the semigroup of endomorphisms of free algebras of homogeneous varieties*, arXiv:math/0511654 (first public version 2005-11-27), https://arxiv.org/abs/math/0511654.
- J. Fountain and V. Gould, *Products of idempotent endomorphisms of relatively free algebras with weak exchange properties*, Proc. Edinburgh Math. Soc. 50 (2007), 343–362, DOI:10.1017/S0013091504000902.
- A. A. Mikhalev and J.-T. Yu, *Test elements, retracts and automorphic orbits of free algebras*, Int. J. Algebra Comput. 8 (1998), 295–310, DOI:10.1142/S0218196798000144 (abstract inspected; full text not obtained).
