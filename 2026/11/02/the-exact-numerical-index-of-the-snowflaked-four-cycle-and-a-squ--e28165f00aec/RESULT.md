# The exact numerical index of the snowflaked four-cycle and a square-root phase transition

## Finding
Let \(M_t=\{0,1,2,3\}\), \(1\le t\le2\), have distances \(d_t(i,j)=1\) for cyclic neighbors and \(d_t(0,2)=d_t(1,3)=t\). The real three-dimensional Lipschitz-free space \(X_t=\mathcal F(M_t,d_t)\) has numerical index
\[
\boxed{n(X_t)=\begin{cases}
(3-t)^{-1},&1\le t\le\sqrt2,\\
\dfrac{t^3}{-t^3+2t^2+8t-8},&\sqrt2\le t\le2.
\end{cases}}
\]
Equivalently, for the snowflaked graph distances \(t=2^\alpha\), the optimizing operator mechanism switches exactly at the exponent \(\alpha=1/2\). Although the dual unit ball has eighteen vertices throughout \(1<t<2\), the numerical index has a genuine derivative change at \(t=\sqrt2\). The formula tends to \(1/2\) at the equilateral endpoint \(t=1\) and equals \(1\) at the unsnowflaked square \(t=2\).

## Assumptions and scope
Everything is over \(\mathbb R\). For a real Banach space \(X\), write
\[
v(T)=\sup\{|x^*(Tx)|: \|x\|=\|x^*\|=1,\ x^*(x)=1\},\qquad
n(X)=\inf_{\|T\|=1}v(T).
\]
The base point is vertex \(0\); identify \(\mathcal F(M_t)\) with \(\mathbb R^3\) by the basis \((\delta_1,\delta_2,\delta_3)\). Its six unoriented normalized molecules are
\[
m_0=(1,0,0),\quad m_1=(-1,1,0),\quad m_2=(0,-1,1),\quad
m_3=(0,0,1),\quad m_4=(0,1/t,0),\quad m_5=(-1/t,0,1/t).
\]
Their signed convex hull is the primal unit ball. For \(1<t<2\), all twelve signed molecules are extreme (every direct distance is strictly smaller than any alternative two-edge route). The dual unit ball is
\[
K_t=\{(a,b,c):|a|,|c|,|b-a|,|b-c|\le1,\ |b|,|a-c|\le t\}.
\]
The parameter interval is exactly the range in which the prescribed distances form a metric; for the edge metric on the four-cycle, \(t=2\), and for the complete equilateral metric, \(t=1\).

## Proof
**1. A finite dual model and its symmetry.** Every dual extreme point of \(K_t\) is an intersection of three independent active distance constraints. For each \(1<t<2\), the complete set of eighteen extreme points, in one reproducible order, is
\[
\begin{aligned}
&(-1,-t,-1),\ (-1,-t,1-t),\ (-1,t-2,t-1),\ (-1,0,-1),\ (-1,0,t-1),\\
&(1-t,-t,-1),\ (1-t,-t,1-t),\ (1-t,0,1),\ (1-t,2-t,1),\\
&(t-1,t-2,-1),\ (t-1,0,-1),\ (t-1,t,t-1),\ (t-1,t,1),\\
&(1,0,1-t),\ (1,0,1),\ (1,2-t,1-t),\ (1,t,t-1),\ (1,t,1).
\end{aligned}
\]
Denote these by \(v_0,\ldots,v_{17}\). To verify that this is exhaustive without sampling parameters, enumerate the \(\binom{12}{3}\) triples of signed linear constraints of \(K_t\). Each independent triple determines a point affine in \(t\); its twelve feasibility slacks are affine, and their simultaneous solution intervals can be solved exactly. They yield exactly these eighteen points, each valid for the entire open interval, with no additional intermediate phase; `verify.py` reproduces these exact calculations.

An extreme norming pair is \((m_i,v_k)\) with \(v_k(m_i)=1\). There are exactly twenty-eight such pairs, indexed \(A_j=v_k\otimes m_i\) (meaning \(A_j(T)=v_k(Tm_i)\)), with the corresponding ordered \((i,k)\) list:
\[
\begin{gathered}
(0,13),(0,14),(0,15),(0,16),(0,17),
(1,3),(1,4),(1,8),(1,11),(1,12),\\
(2,1),(2,2),(2,6),(2,7),(2,14),
(3,7),(3,8),(3,12),(3,14),(3,17),\\
(4,11),(4,12),(4,16),(4,17),
(5,2),(5,4),(5,7),(5,8).
\end{gathered}
\]
The finite-dimensional extreme-pair formula therefore gives \(v(T)=\max_{0\le j\le27}|A_j(T)|\) for every real linear operator \(T\) on \(X_t\). Likewise \(\|T\|=\max_{i,k}|v_k(Tm_i)|\).

**2. A sharp universal inequality.** Put \(W_{i,k}=v_k\otimes m_i\). The dihedral eight-element group of square isometries acts isometrically on both balls; conjugating tensors \(W_{i,k}\) preserves their absolute evaluation norms and maps the twenty-eight norming tensors to themselves, up to sign. Thus the 108 functionals \(W_{i,k}\) reduce to ten symmetry representatives, where the flattened position is \(18i+k\):
\[
0,1,3,5,6,72,73,74,75,76.
\]
The following identities are exact identities of matrices/tensor functionals on all operators, not numerical approximations. In the stated indexing they read
\[
\begin{aligned}
W_0&=-A_4,&W_1&=-A_3,&W_3&=-A_1,\\
W_5&=(2-t)A_0-(t-1)A_3-(2-t)A_4,\\
W_6&=\frac{2-t}{t}A_0+\frac{(t-1)(2-t)}{t}A_1-A_3,\\
W_{72}&=-A_{23},&W_{73}&=-A_{22},\\
W_{74}&=\frac{2(t-1)}{t^3}(A_6+A_{15}-A_0-A_{13})-\frac{2-t}{t}A_{22},\\
W_{75}&=\frac{A_5-A_1}{t},&W_{76}&=\frac{A_6-A_0}{t}.
\end{aligned}
\]
The sums of the absolute coefficients in this list are bounded by
\[
C(t)=\max\left\{3-t,\frac{-t^3+2t^2+8t-8}{t^3}\right\}.
\]
Specifically the first seven cost at most \(3-t\); the eighth cost is exactly the second displayed expression; the last two cost \(2/t\le3-t\). The ten dihedral orbits cover every \(W_{i,k}\) up to sign. Hence \(\|T\|\le C(t)v(T)\) for *every* \(T\), establishing \(n(X_t)\ge1/C(t)\).

**3. Matching operators.** For \(1<t<2\), consider the two real matrices (relative to the fixed molecule basis)
\[
T_A=\begin{pmatrix}
1&0&0\\-2/t&-(2-t)/t&0\\0&0&(3t-4)/t
\end{pmatrix},\quad
T_B=\begin{pmatrix}
-1&-2/t&-2/t\\
2(2-t)/t^2&-1+2(2-t)/t^2&0\\
0&2/t&(2-t)/t
\end{pmatrix}.
\]
Each of the twenty-eight norming evaluations of \(T_A\) has modulus at most one for \(1\le t\le2\), and \(W_5(T_A)=3-t\). Each norming evaluation of \(T_B\) has modulus at most one for \(\sqrt2\le t\le2\), and \(W_{74}(T_B)=(-t^3+2t^2+8t-8)/t^3\). These are finite exact polynomial inequalities on the *entire* stated parameter intervals: multiply by the positive powers of \(t\), and check the endpoint and real critical-point values of the resulting degree-at-most-three polynomials. The accompanying checker implements the complete symbolic validation. Thus \(v(T_A)=v(T_B)=1\) on their respective ranges and their operator norms attain the required bounds. The lower inequality is therefore sharp.

Finally,
\[
\frac{-t^3+2t^2+8t-8}{t^3}-(3-t)
=\frac{(2-t)^2(t^2-2)}{t^3}.
\]
This proves the two branches and the unique crossing at \(t=\sqrt2\). The family \(K_t\), its polar ball, and the numerical index depend continuously on \(t\in[1,2]\) in this finite-dimensional nondegenerate setting, so the endpoint formulas follow by limits. Equivalently the same inequalities and test operators can be evaluated at the endpoint polytopes directly. \(\square\)

## Verification
Run `python verify.py` with SymPy installed. Its output is:

`VERIFIED: 18 dual vertices, 28 norming pairs, 10 symmetry orbits,`

`10 tensor identities, both exact sharp-operator families,`

`and symbolic inequalities on their full parameter intervals.`

The checker enumerates all twelve-constraint triples, computes exact feasible parameter intervals, verifies every tensor decomposition, generates square-isometry orbits, and tests each extremal-operator inequality analytically using exact polynomial critical points. These symbolic calculations are auditable algebraic certificates; no finite floating-point sweep is used as an infinite-parameter argument. The public proof specifies the underlying reduction and the required identities independently of the code.

## Relationship to prior work
Cobollo–Guirao–Montesinos (arXiv:2304.13183v1) calculate numerical indices of real *two*-dimensional Lipschitz-free spaces over three-point metrics; that theorem does not cover the present four-point (three-dimensional) family. Sain–Paul–Bhunia–Bag (arXiv:1809.04778) develop numerical-index estimates for finite-dimensional polyhedral Banach spaces, but their general methods do not state this exact two-branch formula. Gordon–Petrov (arXiv:1608.06848) treat Lipschitz-polytope face combinatorics; the tight-facet framework alone does not determine numerical indices. Published calculations for the *shortened one-edge* four-cycle concern a distinct metric with four successive weighted cycle edges, rather than the square with two simultaneously varying opposite diagonals. A known facet-count classification of the same snowflaked complete-bipartite metric determines the eighteen dual vertices but expressly leaves numerical indices undetermined; the new assertion involves the operator numerical-radius optimization, its two sharp extremizers, and their square-root crossing.

## Limitations
The classification concerns real scalars and the symmetric four-point snowflake metric only. It does not determine numerical indices of arbitrary weighted four-point metrics or complex scalar spaces. Its nontrivial content is the optimization over operators, not the already known dual facet count or the endpoint facts. There remains bibliographic risk from equivalent formulas in less readily indexed three-dimensional polyhedral literature. Independent scientific review has not been performed.

## References
1. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first public 2023-04-25), https://arxiv.org/abs/2304.13183 .
2. D. Sain, K. Paul, P. Bhunia and S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778, https://arxiv.org/abs/1809.04778 .
3. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, https://arxiv.org/abs/1608.06848 .
4. *Sharp facet-count transitions for snowflaked complete bipartite metrics*, publicly available mathematical note (2026); same family, different invariant.
5. *Exact numerical index along the short-edge four-cycle deformation*, publicly available mathematical note (2026); different four-point metric family.
