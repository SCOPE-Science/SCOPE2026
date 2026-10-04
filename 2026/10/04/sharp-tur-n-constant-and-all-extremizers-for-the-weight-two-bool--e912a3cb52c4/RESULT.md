# Sharp Turán constant and all extremizers for the weight-two Boolean Hamming shell
## Finding
For every integer \(d\ge2\), put \(G=\mathbb F_2^d\) and
\[
\Omega_d=\{0\}\cup\{x\in G:|x|=2\}.
\]
With counting measure, define the Turán constant
\[
\tau_d=\sup\left\{\sum_{x\in G}f(x): f(0)=1,\ f\text{ positive definite},\ \operatorname{supp}f\subseteq\Omega_d\right\}.
\]
Then
\[
\tau_d=\begin{cases}d,&d\text{ even},\\ d+1,&d\text{ odd}.\end{cases}
\]
There is also a complete equality classification. Write \(e_1,\ldots,e_d\) for the standard basis and \(a_{ij}=f(e_i+e_j)\). If \(d\) is odd, the extremizer is unique:
\[
a_{ij}=\frac{2}{d-1}\qquad(1\le i<j\le d).
\]
If \(d\) is even, \(f\) is extremal exactly when there are real \(u_1,\ldots,u_d\) satisfying
\[
\sum_{i=1}^d u_i=1,\qquad a_{ij}=u_i+u_j,
\]
and
\[
\sum_{i\in B}u_i\le\frac12\qquad\text{for every }B\subseteq\{1,\ldots,d\}\text{ with }|B|<\frac d2.
\]
For \(d=2\) this still gives the unique function \(a_{12}=1\). For every even \(d\ge4\), small zero-sum perturbations of \(u_i=1/d\) give a continuum of genuinely nonradial extremizers.

## Assumptions and scope
Positive definiteness is in the finite-abelian-group sense. Since every element of \(G\) is its own inverse, every eligible positive-definite \(f\) is real on \(\Omega_d\). The support condition means that the only potentially nonzero values besides \(f(0)=1\) are the \(a_{ij}\). No permutation invariance is assumed; the equality classification includes all nonradial extremizers.

## Proof
For a character indexed by \(y\in\mathbb F_2^d\), set \(s_i=(-1)^{y_i}\). Fourier nonnegativity is equivalent to
\[
Q(s):=1+\sum_{i<j}a_{ij}s_i s_j\ge0\qquad(s\in\{-1,1\}^d).
\]
The objective is
\[
\sum_{x\in G}f(x)=1+\sum_{i<j}a_{ij}.
\]
Let \(A=\sum_{i<j}a_{ij}\).

If \(d\) is even, average \(Q\) over the balanced sign vectors \(\sum_i s_i=0\). Symmetry gives
\[
\mathbb E(s_i s_j)=-\frac1{d-1}\qquad(i\ne j),
\]
so
\[
0\le\mathbb E Q=1-\frac{A}{d-1}.
\]
Thus \(A\le d-1\) and \(\tau_d\le d\). The radial choice \(a_{ij}=2/d\) gives
\[
Q(s)=\frac1d\left(\sum_i s_i\right)^2\ge0,
\]
so equality holds.

If \(d\) is odd, average over the slice \(\sum_i s_i=1\). Since \((\sum_i s_i)^2=1\) on this slice,
\[
\mathbb E(s_i s_j)=-\frac1d,
\]
and hence \(A\le d\), giving \(\tau_d\le d+1\). The radial choice \(a_{ij}=2/(d-1)\) gives
\[
Q(s)=\frac{(\sum_i s_i)^2-1}{d-1}\ge0,
\]
because an odd sum of \(d\) signs has absolute value at least one. This proves the sharp values.

It remains to classify equality. In either parity, equality makes the relevant slice average of the nonnegative function \(Q\) equal to zero, so \(Q\) vanishes at every sign vector in that slice.

Suppose first that \(d\) is odd. Fix distinct \(i,j\), choose \(s_i=1\), \(s_j=-1\), and let \(r=(s_k)_{k\ne i,j}\) range over sign vectors with \(\sum r_k=1\). Swap the signs at \(i,j\). Subtracting the two equations \(Q=0\) gives
\[
\sum_{k\ne i,j}(a_{ik}-a_{jk})r_k=0.
\]
The sign vectors in \(\{-1,1\}^{d-2}\) with coordinate sum one span \(\mathbb R^{d-2}\): their pairwise swaps span the zero-sum hyperplane and any one such vector has nonzero coordinate sum. Therefore \(a_{ik}=a_{jk}\) for all distinct \(i,j,k\). All edge coefficients are equal, and the already proved equality \(A=d\) forces \(a_{ij}=2/(d-1)\). This proves uniqueness.

Now let \(d\) be even. For distinct \(i,j\), use balanced sign vectors with \(s_i=1\), \(s_j=-1\); the remaining \(d-2\) signs are balanced. The same subtraction shows that the vector
\[
(a_{ik}-a_{jk})_{k\ne i,j}
\]
is orthogonal to every balanced sign vector in \(\mathbb R^{d-2}\). Balanced sign vectors span the zero-sum hyperplane, because differences of two balanced vectors obtained by swapping one positive and one negative coordinate generate every \(e_p-e_q\). Hence the displayed row difference is constant in \(k\). For \(d\ge4\), these constant row differences imply the additive representation
\[
a_{ij}=u_i+u_j
\]
for suitable real \(u_i\). Substituting any balanced sign vector into \(Q=0\) then gives \(\sum_i u_i=1\). The case \(d=2\) is the same final representation directly.

For an arbitrary sign vector put
\[
S=\sum_i s_i,\qquad T=\sum_i u_i s_i.
\]
Using \(\sum_i u_i=1\), one obtains exactly
\[
Q(s)=S T.
\]
When \(S>0\), let \(B=\{i:s_i=-1\}\); then \(|B|<d/2\) and
\[
T=1-2\sum_{i\in B}u_i.
\]
Thus \(Q(s)\ge0\) for every sign vector if and only if
\[
\sum_{i\in B}u_i\le\frac12
\]
for every \(|B|<d/2\). Negating all signs handles \(S<0\), while \(S=0\) gives \(Q=0\) automatically. This proves both necessity and sufficiency of the stated even-dimensional classification.

## Verification
The accompanying exact-arithmetic verifier checks dimensions \(2\) through \(10\). It verifies the sharp radial values on every character, the full rank of the odd equality-slice system, the predicted \(d-1\)-dimensional affine family in each even dimension at least four, and explicit nonradial feasible points. It prints:

`VERIFY_OK dimensions=2..10 radial_values=exact odd_unique_ranks=exact even_extremal_dimensions=exact nonradial_examples=exact`

These finite checks corroborate the algebraic proof; they are not used to infer the all-dimensional statement.

## Relationship to prior work
Kolountzakis and Révész formulate Turán's extremal problem on arbitrary locally compact abelian groups, explicitly emphasize finite groups, and identify positive definiteness with nonnegative Fourier transform. Their finite-group theorems provide general packing and spectral-set upper-bound mechanisms. The inspected full text does not state the weight-two Boolean Hamming-shell problem or classify its equality cases.

The distance-two graph of the Boolean cube is the disjoint union of two halved cubes. Krotov studies perfect colorings of the halved \(24\)-cube, confirming that the same distance-two geometry is a classical object, but that work concerns equitable colorings rather than positive-definite Turán optimization. Standard association-scheme or graph-spectral methods can plausibly recover the sharp numerical value; the substantive addition here is the complete classification of all translation-invariant positive-definite equality cases, including the odd-dimensional rigidity and even-dimensional nonradial polytope.

## Limitations
The theorem classifies extremizers for the positive-definite Turán problem with support restricted to Hamming weights zero and two. It does not classify arbitrary semidefinite-program optimizers without translation invariance, nor does it treat other Hamming shells. The originality comparison found no covering source for the equality classification, but older coding-theory or association-scheme literature using different terminology remains a residual risk.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first public 2003-12-10.
2. D. Krotov, *On perfect colorings of the halved 24-cube*, arXiv:0803.0068, first public 2008-03-02.
