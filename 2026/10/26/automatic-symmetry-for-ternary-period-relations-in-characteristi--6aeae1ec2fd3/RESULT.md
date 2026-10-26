# Automatic symmetry for ternary period relations in characteristic two

## Finding
Let \(R\) be a commutative \(\mathbb F_2\)-algebra and \(f\in R[x,y,z]\) an arbitrary polynomial. Suppose
\[
f(x,y,z)=f(y,z,x),\qquad
f(x,y,z)+f(y,x+y,z)+f(x+y,x,z)=0.
\]
Then
\[
\boxed{f(x,y,z)=f(y,x,z).}
\]
Together with cyclic invariance, this proves that \(f\) is invariant under every permutation of \(x,y,z\). This includes all degrees, including nonhomogeneous polynomials.

## Assumptions and scope
The coefficient ring \(R\) is any unital commutative algebra over \(\mathbb F_2\); no integrality, field, or degree assumption is imposed. The transformations below act by linear substitution over \(\mathbb F_2\). All matrix products and ranks in the certificate are calculated exactly over \(\mathbb F_2\).

## Proof
Represent a linear substitution on \((x,y,z)\) by the three nonzero binary masks encoding its images of \(x,y,z\). Write \(I=(1,2,4)\), \(A=(2,3,4)\), \(C=(2,4,1)\), and \(S=(2,1,4)\). Thus \(A(x,y,z)=(y,x+y,z)\), \(C(x,y,z)=(y,z,x)\), and \(S(x,y,z)=(y,x,z)\). Their substitution group \(G\) is the 168-element group \(\mathrm{GL}_3(\mathbb F_2)\). Indeed, exact closure under these generators gives 168 distinct matrices, and \(|\mathrm{GL}_3(\mathbb F_2)|=(8-1)(8-2)(8-4)=168\).

Write \(e_g\) for the standard basis vector in \(\mathbb F_2^G\) indexed by \(g\in G\). The two assumed polynomial identities, after substituting \(g(x,y,z)\) for \((x,y,z)\), give for every \(g\in G\):
\[
f(g\mathbf x)+f(Cg\mathbf x)=0,\qquad
f(g\mathbf x)+f(Ag\mathbf x)+f(A^2g\mathbf x)=0.
\]
Thus every evaluation map \(e_g\mapsto f(g\mathbf x)\) annihilates the span \(L\) of the 336 relation vectors
\[
 e_g+e_{Cg},\qquad e_g+e_{Ag}+e_{A^2g}\quad(g\in G).
\]

The standalone exact verifier `verify_group_algebra.py` constructs every \(g\in G\), forms these 336 binary column vectors, and performs deterministic bitwise Gaussian elimination. It proves \(\dim_{\mathbb F_2}L=160\) and, crucially, checks for every one of the 168 elements \(g\in G\) that
\[
\boxed{e_g+e_{Sg}\in L.}
\]
This is a finite exhaustive calculation, not a statistical sample: group generation, multiplication, binary elimination, and 168 membership reductions are implemented using exact integers, with all parameters and loops visible in the self-contained verifier. In particular, \(e_I+e_S\in L\), so its image under the evaluation map is zero: \(f(\mathbf x)+f(S\mathbf x)=0\). This gives the asserted swap symmetry. Since the transposition \(S\) and 3-cycle \(C\) generate the permutation group on three coordinates, complete symmetry follows.

The argument is a universal group-algebra identity over \(\mathbb F_2\); consequently every step remains valid after extension of coefficients to any commutative \(\mathbb F_2\)-algebra \(R\).

## Verification
Run `python3 verify_group_algebra.py` with a standard Python 3 interpreter. It must print `VERIFY_OK group=168 rank=160 swaps=168`. The code first confirms the generated group has exactly 168 elements and every generator-induced composition remains in it; then it computes the exact relation-space rank and verifies inclusion of all swap vectors.

## Relationship to prior work
Ilin and Ono, *Ternary polynomial relations and periods of cusp forms* (arXiv:2610.19309v1, first publicly submitted 13 October 2026), classify the same two relations over characteristic-zero coefficient fields. Their Section 5 and Appendix D calculate an exact kernel for **symmetric** characteristic-two polynomials as part of an integral-lift argument. The statement here is different: it proves that the cyclic and three-term relations themselves **force** symmetry in characteristic two, without assuming symmetry and without any restriction on polynomial degree or coefficient algebra. It therefore supplies a structural reduction from the full modular solution problem to their symmetric modular kernel. It does not claim that the published symmetric kernel computation is new.

## Limitations
This is a characteristic-two theorem only, not a classification in odd prime characteristic. It does not independently rederive the complete symmetric-kernel basis of Ilin and Ono. The proof uses a finite group-algebra certificate whose verification requires executing the included exact-arithmetic algorithm or reproducing its elimination. No independent audit has been performed.

## References
1. V. Ilin and K. Ono, *Ternary polynomial relations and periods of cusp forms*, arXiv:2610.19309v1 (13 October 2026), especially introduction, Section 5.3, and Appendix D.
2. The self-contained executable certificate `verify_group_algebra.py`, embedded with this result.
