# Sharp positivity-restricted triangular truncation in dimension three

## Finding
Let \(M_3(\mathbb C)\) denote the space of complex \(3\times3\) matrices. Define the Schur truncation operator \(T\) by
\[
(T(A))_{ij}=\begin{cases}A_{ij},&i>j,\\0,&i\le j.\end{cases}
\]
For every positive semidefinite \(A\in M_3(\mathbb C)\),
\[
\boxed{\|T(A)\|_{\mathrm{op}}\le \frac{1+2\sqrt2}{7}\|A\|_{\mathrm{op}}.}
\]
This coefficient is optimal. Set \(t=(4+\sqrt2)/14\) and let \(v=(\sqrt t,\sqrt{1-2t},\sqrt t)^{\mathsf T}\). The rank-one orthogonal projection \(A=vv^*\) attains equality. Identical optimality holds on real symmetric positive semidefinite matrices.

## Assumptions and scope
Throughout, \(A\succeq0\) means Hermitian positive semidefinite, \(\|\cdot\|_{\mathrm{op}}\) is the largest singular value, and the matrix order of coordinates is fixed. This result concerns the norm of a Schur multiplier **restricted to the positive cone**; it does not assert the unrestricted multiplier norm on all matrices. It applies to every nonzero positive semidefinite complex or real \(3\times3\) matrix, including singular matrices, by positive homogeneity. The zero matrix is trivial.

## Proof
Normalize \(\|A\|_{\mathrm{op}}=1\), so \(0\preceq A\preceq I\). The spectral resolution gives \(A=\int_0^1 P_s\,ds\), where each \(P_s\) is an orthogonal projection (the integral is an ordinary finite-dimensional spectral sum). Linearity of \(T\) and convexity of the operator norm imply
\[
\|T(A)\|_{\mathrm{op}}\le\int_0^1\|T(P_s)\|_{\mathrm{op}}\,ds.
\]
In dimension three a projection has rank \(0,1,2\), or \(3\). The ranks \(0,3\) give zero. If \(P\) has rank two, then \(P=I-Q\) with \(Q\) rank one; because \(T(I)=0\), we have \(T(P)=-T(Q)\). Hence it is enough to optimize over rank-one projections \(P=vv^*\), \(\|v\|_2=1\).

Conjugation by a diagonal unitary matrix commutes with \(T\) and preserves the operator norm. Thus put \(x=|v_1|^2\), \(y=|v_2|^2\), \(z=|v_3|^2\), with \(x,y,z\ge0\) and \(x+y+z=1\), and assume \(v_i\ge0\). The only nonzero block of \(T(P)\), on rows \(2,3\) and columns \(1,2\), is
\[
B=\begin{pmatrix}\sqrt{xy}&0\\sqrt{xz}&\sqrt{yz}\end{pmatrix}.
\]
Writing \(p=xz\), its squared operator norm \(\lambda=\|B\|_{\mathrm{op}}^2\) is the larger root of
\[
\lambda^2-\bigl(y(1-y)+p\bigr)\lambda+py^2=0,
\qquad 0\le p\le\frac{(1-y)^2}{4}.
\]
For \(0<y<1\), the polynomial at \(\lambda=y^2\) equals \(y^3(2y-1)\). For \(0<y<1/2\), the larger root exceeds \(y^2\), so implicit differentiation gives
\[
\frac{d\lambda}{dp}=\frac{\lambda-y^2}{2\lambda-y(1-y)-p}>0.
\]
Consequently its maximum for fixed \(y\) occurs at \(x=z=(1-y)/2\). For \(1/2<y<1\), the larger root is below \(y^2\) (as it is at \(p=0\), and it cannot cross \(y^2\)), so \(\lambda\) decreases in \(p\). Its maximum there is \(y(1-y)\le1/4\). At \(y=1/2\) the larger root is \(1/4\) for all admissible \(p\). The endpoint values \(y=0\) and \(y=1\) are obtained directly from \(B\) and are at most \(1/2\) in norm.

It remains to put \(x=z=t\) and \(y=1-2t\), where \(1/4\le t\le1/2\). The corresponding block has diagonal entries \(\sqrt{t(1-2t)}\) and subdiagonal entry \(t\). The elementary singular-value formula for a \(2\times2\) triangular matrix gives
\[
\|B\|_{\mathrm{op}}=g(t):=\frac{t+\sqrt{4t-7t^2}}{2}.
\]
Here \(g(1/4)=g(1/2)=1/2\). Differentiating on \((1/4,1/2)\) shows
\[
g'(t)=\frac12+\frac{4-14t}{4\sqrt{4t-7t^2}}.
\]
The sign switches once, from positive to negative, at the unique admissible solution of
\(\sqrt{4t-7t^2}=7t-2\), namely \(t=(4+\sqrt2)/14\). At that parameter,
\[
g(t)=\frac{t+(7t-2)}2=4t-1=\frac{1+2\sqrt2}{7}>\frac12.
\]
Because \(x=z=t\) and \(y=1-2t\) are nonnegative and sum to one, the stated unit vector produces a rank-one orthogonal projection attaining this value. The earlier reduction covers every positive contraction, and scaling covers every positive semidefinite \(A\). The extremal vector is real, proving the real variant as well.

## Verification
The accompanying `verify_cone.py` checks exact algebraic identities in \(\mathbb Q(\sqrt2)\), verifies the extremal matrix's singular-value characteristic equation, and performs a reproducible numerical simplex stress test. Run `python verify_cone.py` using Python 3 (standard library only). The sample test is **not** an infinite proof; the preceding projection reduction and scalar monotonicity argument supply the global proof.

For comparison, in dimension two the analogous positive-cone constant is \(1/2\), since rank-one reductions give \(\sqrt{x(1-x)}\le1/2\). Dimension three is the first setting where two subdiagonal levels interact and the sharp constant is strictly larger.

## Relationship to prior work
The classical Schur multiplier formulation and the fact that triangular truncation is a characteristic-function multiplier are discussed by Todorov–Turowska [1], whose original public preprint was posted on 2009-11-03. Oswald–Zhou [2] investigate positive semidefinite matrices and triangular parts in iterative-method estimates, while Zhou [3] obtains sharp **unrestricted** triangular-truncation estimates and examples; their results do not state this positivity-restricted \(3\times3\) operator-norm extremum. Bhatia [4] discusses matrix trimming and general norm bounds; the 1992 Angelos–Cowen–Narayan paper [5] concerns the unrestricted Hadamard multiplier norm. The positivity-restricted constant must not be confused with any unrestricted Schur multiplier norm. These comparisons describe investigated coverage, not a claim of exhaustive global novelty.

## Limitations
Only the positive cone in dimension three is covered. No formula for general dimensions, no unrestricted Schur multiplier norm, and no full classification of all positive semidefinite maximizers is asserted. The entire full text of [5] was not accessible, and a still earlier triangular-projection paper [6] could not be inspected in full; unindexed or inaccessible historical results remain a residual originality risk. The mathematical proof is elementary and exact but has not received independent audit.

## References
[1] I. G. Todorov and L. Turowska, *Schur and operator multipliers*, arXiv:0911.0606 (first posted 2009-11-03); Banach Center Publications 91 (2010), 385–410, primary MSC 47L25; DOI: 10.4064/bc91-0-23.

[2] P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, arXiv:1510.04727 (first posted 2015-10-15).

[3] W. Zhou, *Triangular truncation and its extremal matrices*, Numerical Linear Algebra with Applications 23 (2016), 642–655; DOI: 10.1002/nla.2045.

[4] R. Bhatia, *Pinching, Trimming, Truncating, and Averaging of Matrices*, American Mathematical Monthly 107 (2000), 602–608; DOI: 10.1080/00029890.2000.12005245.

[5] J. R. Angelos, C. C. Cowen, and S. K. Narayan, *Triangular truncation and finding the norm of a Hadamard multiplier*, Linear Algebra and its Applications 170 (1992), 117–135; DOI: 10.1016/0024-3795(92)90414-6.

[6] S. Kwapień and A. Pełczyński, *The main triangle projection in matrix spaces and its applications*, Studia Mathematica 34 (1970), 43–67; DOI: 10.4064/sm-34-1-43-67.
