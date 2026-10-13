# Additive invariant factors of the first finite-plateau Lie ring

## Finding
Let \(L_1\) be the explicit \(N=1\) Lie ring in Example 3.2 of Ionin–Mikhailov–Petrov, defined as the indicated quotient of the free metabelian Lie ring on \(x_1,\ldots,x_5\). Its underlying additive abelian group is
\[
L_1^+\cong \mathbb Z^5\oplus \mathbb Z/2\mathbb Z\oplus(\mathbb Z/4\mathbb Z)^{22}\oplus \mathbb Z/8\mathbb Z\oplus(\mathbb Z/16\mathbb Z)^{15}\oplus(\mathbb Z/64\mathbb Z)^7\oplus(\mathbb Z/256\mathbb Z)^3.
\]
Hence the torsion subgroup of \(L_1^+\) has order \(2^{174}\) and exponent \(256\). In particular, the additive torsion exponent is strictly larger than the exponent \(64\) of the terminal lower-central term \(\gamma_4(L_1)\cong\mathbb Z/64\mathbb Z\).

## Assumptions and scope
The object is exactly the \(N=1\) specialization of the integral metabelian construction in arXiv:2610.02042v1. The computation is over \(\mathbb Z\); no field base change is used. The statement concerns the underlying additive group only. It does not give invariant factors for \(L_N\) when \(N>1\), nor does it refine the dimension-series theorem proved in the source.

## Proof
Use the generator order \(x_5<x_1<x_2<x_3<x_4\) fixed in the source. In the free metabelian Lie ring truncated at class \(4\), the standard Hall basis consists of the five generators together with left-normed commutators
\[
[x_{i_0},x_{i_1},\ldots,x_{i_r}],\qquad x_{i_0}>x_{i_1}\le x_{i_2}\le\cdots\le x_{i_r}.
\]
Through weight \(4\) this gives respectively \(5,10,40,105\) basis elements, hence \(160\) additive generators.

For \(N=1\), put \(t=[x_4,x_5]\), \(c_i=[t,x_i]\), and \(u_i=[c_i,x_i]\) for \(1\le i\le3\). Start with the three source relators
\[
r_1=4x_1+2c_3+c_2,\qquad r_2=16x_2+4c_3-c_1,\qquad r_3=64x_3-4c_2-2c_1.
\]
Close these relators under brackets with the five generators through weight \(4\). Add the relations killing every weight-\(4\) Hall element except \(u_1,u_2,u_3\), and finally add
\[
u_1-16u_3=0,\qquad u_2-4u_3=0,\qquad64u_3=0.
\]
This is precisely the additive relation module of the quotient presentation: ideal generation is obtained by repeated adjoint action of the generators, and all brackets of weight at least \(5\) vanish. After zero rows are omitted only implicitly, the resulting integer presentation matrix has \(483\) relation rows and \(160\) columns.

Exact Smith reduction over \(\mathbb Z\) has \(155\) nonzero diagonal entries. The nonunit diagonal entries occur with multiplicities
\[
2^{\times1},\quad4^{\times22},\quad8^{\times1},\quad16^{\times15},\quad64^{\times7},\quad256^{\times3},
\]
and the remaining five columns are free. The structure theorem for finitely generated abelian groups gives the displayed decomposition. The torsion order exponent is
\[
1+2\cdot22+3+4\cdot15+6\cdot7+8\cdot3=174,
\]
while the largest invariant factor is \(256\).

## Verification
The accompanying `artifacts/verify.py` reconstructs the Hall basis and bracket normal form rather than reading a stored matrix. It checks the Jacobi identity on all generator triples and the metabelian tail-symmetry identity used by the normal form. It then reconstructs the six displayed bracket relations from equation (3.5) of the source after imposing the source's weight-\(4\) killing relations. Finally it builds the \(483\times160\) integer presentation matrix and computes its Smith normal form. As an additional check on the unreduced matrix, modular Gaussian elimination gives rank \(106\) modulo \(2\) and rank \(155\) modulo \(3\), exactly as predicted by the Smith factors. The recorded run in `artifacts/verify.txt` ends with `CHECK_OK` and reports free rank \(5\) and torsion multiplicities \(\{2:1,4:22,8:1,16:15,64:7,256:3\}\).

## Relationship to prior work
Ionin–Mikhailov–Petrov introduce \(L_N\), spell out the \(N=1\) presentation, and prove \(\gamma_{N+3}(L_N)=\langle u_3\rangle\cong\mathbb Z/64\mathbb Z\). Their paper uses invariant-factor decompositions abstractly later and uses Smith normal form in a different group-theoretic computation, but it does not state the additive invariant factors of \(L_1\). Passi–Sicking and Bartholdi–Passi establish structural results for dimension subrings and dimension quotients; those results do not determine the underlying additive group of this 2026 explicit plateau example. Targeted published-result and web searches for the exact object, invariant-factor tuple, torsion exponent, and Smith-normal-form formulation found no covering statement.

## Limitations
This is a single-object exact invariant, not a general formula for the family \(L_N\). The proof depends on an exact integer Smith-normal-form computation, although the entire presentation matrix is regenerated from the source presentation and all arithmetic is exact. The verification uses SymPy's integer Smith-normal-form implementation; an independent implementation or independent audit has not been performed. Because the motivating preprint is very recent, unindexed contemporaneous computations remain a residual originality risk.

## References
1. Vasily Ionin, Roman Mikhailov, Tima Petrov, “Dimension subrings of Lie rings,” arXiv:2610.02042v1, 1 October 2026. In particular §3.1, Example 3.2, Lemma 3.3, and equation (3.5).
2. Inder Bir S. Passi, Thomas Sicking, “Dimension quotients of metabelian Lie rings,” International Journal of Algebra and Computation 27 (2017), 251–258, DOI 10.1142/S0218196717500114.
3. Laurent Bartholdi, Inder Bir S. Passi, “Lie dimension subrings,” International Journal of Algebra and Computation 25 (2015), 1301–1325, DOI 10.1142/S0218196715500423.
