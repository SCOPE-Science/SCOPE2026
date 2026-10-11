# Banach \(g\)-\(p\)-fusion synthesis requires adjoint projections
## Finding
For the Banach-space \(g\)-\(p\)-fusion framework of Ghosh and Samanta, the printed synthesis operator in Theorem 3.5 is not an operator on the stated spaces. The paper defines \(P_{V_i}:X\to X\) and \(\Lambda_i:X\to X_i\), hence \(\Lambda_i^*:X_i^*\to X^*\). Therefore \(P_{V_i}\Lambda_i^*g_i\) is not a defined composition in general. The correct synthesis operator is
\[
T_c(g)=\sum_i v_i P_{V_i}^*\Lambda_i^*g_i.
\]
With this correction, Theorem 3.5 has an exact norm form: a family is \(g\)-\(p\)-fusion Bessel if and only if \(T_c\) is well-defined and bounded, and then the optimal Bessel constant equals \(\|T_c\|\). Theorem 3.9(i) becomes \(U^*=T_c\), and Theorem 3.10 becomes valid with \(T_c\): the family is a \(g\)-\(p\)-fusion frame if and only if \(T_c\) is bounded and surjective.

## Assumptions and scope
Let \(X\) and \(X_i\) be Banach spaces, \(1<p<\infty\), and \(q\) conjugate to \(p\). Let \(P_{V_i}\in\mathcal B(X)\) be bounded projections, \(\Lambda_i\in\mathcal B(X,X_i)\), and \(v_i>0\). Define
\[
Uf=(v_i\Lambda_iP_{V_i}f)_i.
\]
The claim concerns the operator-theoretic characterization of Bessel and frame families. It does not alter the analysis inequality or assert corrections to unrelated perturbation results.

## Proof
For \(g=(g_i)\in\ell^q((X_i^*))\) and \(f\in X\),
\[
\langle Uf,g\rangle=\sum_i v_i\langle \Lambda_iP_{V_i}f,g_i\rangle=\sum_i v_i\langle f,P_{V_i}^*\Lambda_i^*g_i\rangle.
\]
Hence
\[
U^*g=\sum_i v_iP_{V_i}^*\Lambda_i^*g_i=T_cg.
\]
If the family is Bessel with bound \(B\), then \(\|U\|\le B\), hence \(T_c=U^*\) is bounded and \(\|T_c\|=\|U\|\le B\). For infinite index sets, unconditional convergence follows from convergence of finite coordinate truncations in \(\ell^q((X_i^*))\) and boundedness of \(U^*\).

Conversely, if \(T_c\) is well-defined and bounded, duality gives
\[
\|Uf\|=\sup_{\|g\|_q\le1}|\langle Uf,g\rangle|=\sup_{\|g\|_q\le1}|\langle f,T_cg\rangle|\le\|T_c\|\,\|f\|.
\]
Thus the family is Bessel with bound \(\|T_c\|\). Therefore \(\|T_c\|=\|U\|\) and this is the optimal Bessel constant.

A positive lower frame bound is equivalent to \(U\) being bounded below. The Banach closed-range theorem gives that \(U\) is bounded below if and only if \(U^*\) is surjective. Since \(U^*=T_c\), the corrected synthesis operator is bounded and onto exactly for \(g\)-\(p\)-fusion frames.

The missing adjoint is not benign. On \(X=\mathbb R^2\), let \(P(x,y)=(x+y,0)\), \(X_1=\mathbb R\), \(v_1=1\), and \(\Lambda(x,y)=x\). Then \(U(x,y)=x+y\), so \(U^*(1)\) is represented by \((1,1)\). Under the Euclidean identification of \(X^*\) with \(X\), the printed \(P\) sends \(\Lambda^*(1)=e_1\) to \(e_1\), not \((1,1)\).

## Verification
The target paper was inspected at Theorem 3.5 and at Theorems 3.9--3.10, where the identity \(U^*=T\) and surjectivity of \(T\) are used. Earlier declarations place \(P_{V_i}\) on \(X\) and \(\Lambda_i^*g_i\) in \(X^*\). The 2007 precursor has no fusion projections and defines its synthesis operator as the adjoint-compatible sum of coefficient functionals.

## Relationship to prior work
Abdollahpour, Faroughi, and Rahimi's 2007 \(p\)-\(g\)-frame theory defines analysis and synthesis as an adjoint pair before fusion projections are introduced. The 2022 paper inserts Banach projections but does not adjoint them when passing to the dual. Searches for the exact theorem number, arXiv identifier, adjoint-projection formulation, synthesis-operator aliases, and erratum language found no source stating this correction or the exact norm identity.

## Limitations
The correction assumes the projections \(P_{V_i}\) are bounded, so \(P_{V_i}^*\) exists as a bounded operator. No claim is made about downstream results that may remain true for independent reasons after correcting their synthesis operator.

## References
1. P. Ghosh and T. K. Samanta, *Generalized p-fusion frame in separable Banach space*, arXiv:2202.12266v1, first posted 2022-02-23; GANITA 72(2) (2022), 173--187. Primary MSC 42C15.
2. M. R. Abdollahpour, M. H. Faroughi, and A. Rahimi, *PG-Frames in Banach Spaces*, Methods of Functional Analysis and Topology 13(3) (2007), 201--210.
