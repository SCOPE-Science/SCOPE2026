# An explicit isolated double-zero-Hopf point in the RNC-O family

## Finding
Consider the parameterized Rössler–Nikolov–Clodong O family
\[
\dot x=-y-z,\qquad
\dot y=x+ay+w,
\]
\[
\dot z=b+b_1x+b_2y+b_3z+b_4w+xz,\qquad
\dot w=-cz+dw.
\]
Fix
\[
a=\frac14,\quad c=\frac12,\quad d=\frac1{20},\quad
b_1=0,\quad b_2=-\frac{20}{119},\quad
b_3=-\frac3{10},\quad b_4=\frac{157}{11900},
\]
and write \(b=\mu\). Then the equilibrium equations reduce exactly to
\[
z=-y,\qquad w=-10y,\qquad x=\frac{39}4y,
\]
and
\[
\mu-\frac{39}4y^2=0.
\]
Consequently the origin is the unique equilibrium at \(\mu=0\), there are no real equilibria for \(\mu<0\), and there are two real equilibria for \(\mu>0\).

At \(\mu=0\), the Jacobian at the origin has characteristic polynomial
\[
\chi(\lambda)=\lambda^2\left(\lambda^2+\frac{1769}{1904}\right).
\]
Thus its eigenvalues are
\[
0,\quad 0,\quad +i\sqrt{\frac{1769}{1904}},\quad
-i\sqrt{\frac{1769}{1904}}.
\]
In the terminology explicitly adopted by Nikolov and Vassilev, this is an isolated zero-Hopf equilibrium. It gives a concrete counterexample to their Theorem 1 assertion that an origin equilibrium of this family cannot be of zero-Hopf type.

## Assumptions and scope
The statement concerns the parameterized vector-field family used in the source's Section 3.1. The values \(a=1/4\), \(c=1/2\), and \(d=1/20\) are the source's baseline values; \(b\) is varied and the coefficients \(b_1,b_2,b_3,b_4\) are real, as allowed by the displayed family. The source itself varies parameters outside its initial numerical slice when formulating its zero-Hopf problem.

"Zero-Hopf" is used only in the source's stated sense: an isolated equilibrium with a double-zero eigenvalue and a pair of nonzero purely imaginary eigenvalues. No claim is made here that all normal-form nondegeneracy hypotheses required by any particular zero-Hopf bifurcation theorem are satisfied.

## Proof
At an equilibrium, \(\dot x=0\) gives \(z=-y\). Next, \(\dot w=0\) gives
\[
-\frac12z+\frac1{20}w=0,
\]
hence \(w=10z=-10y\). Since \(a=1/4\), the equation \(\dot y=0\) becomes
\[
x+\frac14y-10y=0,
\]
so \(x=39y/4\).

Substitution into \(\dot z=0\) gives
\[
0=\mu-\frac{20}{119}y-\frac3{10}(-y)
+\frac{157}{11900}(-10y)
+\left(\frac{39}4y\right)(-y).
\]
The linear coefficient cancels exactly because
\[
-\frac{20}{119}+\frac3{10}-\frac{157}{1190}=0.
\]
Therefore
\[
0=\mu-\frac{39}4y^2.
\]
This proves the complete equilibrium count and, in particular, that the origin is the unique equilibrium for \(\mu=0\).

At \(\mu=0\), the Jacobian at the origin is
\[
J_0=
\begin{pmatrix}
0&-1&-1&0\\
1&1/4&0&1\\
0&-20/119&-3/10&157/11900\\
0&0&-1/2&1/20
\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\det(\lambda I-J_0)
=\lambda^2\left(\lambda^2+\frac{1769}{1904}\right).
\]
Since \(1769/1904>0\), the nonzero pair is purely imaginary. The zero eigenvalue has algebraic multiplicity two. Because the equilibrium equations have only the origin at \(\mu=0\), the equilibrium is isolated.

The source's proof restricts the origin calculation by imposing \(b=c=b_1=b_2=b_3=b_4=0\), although the displayed vector field has the origin as an equilibrium whenever \(b=0\). It also states a negative sign condition on the quadratic coefficient of a polynomial whose zero-Hopf factorization would instead be \(\lambda^2(\lambda^2+\omega^2)\) with \(\omega^2>0\). The explicit counterexample above does not rely on diagnosing either proof step: the equilibrium equations and spectrum independently establish the conclusion.

## Verification
The bundled `verify.py` checks the rational cancellations, reconstructs the characteristic polynomial coefficients from the general Jacobian formula, and confirms the equilibrium trichotomy algebraically. It uses exact rational arithmetic only.

The proof is symbolic. No finite-time orbit integration, Lyapunov-exponent estimate, or root-finding tolerance is used.

## Relationship to prior work
Nikolov and Vassilev introduce the RNC-O system, state the zero-Hopf question for one-parameter families of their model, and give Theorem 1 claiming that an origin equilibrium cannot be of zero-Hopf type. Their full text also supplies the displayed vector field and the baseline values \(a=1/4\), \(c=1/2\), and \(d=1/20\).

Broader zero-Hopf literature proves zero-Hopf equilibria and bifurcating periodic solutions in other four-dimensional hyperchaotic systems, including a different Lorenz-type quadratic system. Those results establish that the spectral configuration is meaningful but do not imply this RNC-O counterexample because the vector fields and parameter relations differ.

Searches by the exact model name, theorem language, characteristic-polynomial aliases, and the explicit parameter pattern found no published statement covering this counterexample. The closest indexed Rössler zero-Hopf result concerns a different Rössler unfolding and does not contain the RNC-O equations.

## Limitations
This result corrects the equilibrium-level nonexistence statement. It does not prove that the one-parameter \(\mu\)-family satisfies every generic unfolding or nondegeneracy condition used in a specific zero-Hopf normal-form theorem. It therefore does not claim the existence, number, or stability of small periodic or quasiperiodic invariant sets born from the point.

The parameter \(b_3=-3/10\) lies outside the positive \(b_3\) scan used for the source's displayed hyperchaotic numerical examples. The source's Theorem 1, however, is stated for the parameterized family rather than only that scan.

## References
1. S. G. Nikolov and V. M. Vassilev, "Complex Dynamics of Rössler–Nikolov–Clodong O Hyperchaotic System: Analysis and Computations," *Axioms* 12 (2023), 185. DOI 10.3390/axioms12020185.
2. J. Yang, Z. Wei, and I. Moroz, "Periodic solutions for a four-dimensional hyperchaotic system," *Advances in Difference Equations* 2020, 198. DOI 10.1186/s13662-020-02647-4.
3. Y.-M. Chen and H.-H. Liang, "Zero-zero-Hopf bifurcation and ultimate bound estimation of a generalized Lorenz–Stenflo hyperchaotic system," *Mathematical Methods in the Applied Sciences* 40 (2017), 3424–3432. DOI 10.1002/mma.4236.
