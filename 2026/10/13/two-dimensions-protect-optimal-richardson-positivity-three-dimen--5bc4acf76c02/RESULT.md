# Two dimensions protect optimal Richardson positivity; three dimensions do not
## Finding
Let \\(A\\) be a real symmetric positive-definite Stieltjes matrix, so its off-diagonal entries are nonpositive, and let \\(b\\ge0\\). Consider stationary Richardson iteration
\[
x^{(k+1)}=x^{(k)}+\\alpha\\bigl(b-Ax^{(k)}\\bigr),\\qquad x^{(0)}=0,
\]
with the spectrally optimal fixed parameter
\[
\\alpha=\\frac{2}{\\lambda_{\\min}(A)+\\lambda_{\\max}(A)}.
\]
In dimensions \\(n=1\\) and \\(n=2\\), every iterate is componentwise nonnegative for every \\(k\\ge0\\). This universal property fails already in dimension \\(3\\), so dimension three is minimal for transient sign loss.

An exact witness is
\[
A=\\begin{pmatrix}10&-1&0\\\\-1&10&0\\\\0&0&1\\end{pmatrix},\\qquad
b=\\begin{pmatrix}0\\\\1\\\\0\\end{pmatrix}.
\]
The spectrum is \\(\\{1,9,11\\}\\), hence \\(\\alpha=1/6\\). The first three iterates are
\[
x^{(1)}=\\begin{pmatrix}0\\\\1/6\\\\0\\end{pmatrix},\\qquad
x^{(2)}=\\begin{pmatrix}1/36\\\\1/18\\\\0\\end{pmatrix},\\qquad
x^{(3)}=\\begin{pmatrix}-1/108\\\\29/216\\\\0\\end{pmatrix}.
\]
Thus the third iterate has a negative coordinate even though the iteration converges and
\[
A^{-1}b=\\begin{pmatrix}1/99\\\\10/99\\\\0\\end{pmatrix}\\ge0.
\]

## Assumptions and scope
The claim concerns real symmetric positive-definite Stieltjes matrices, nonnegative right-hand sides, the zero initial vector, and the single fixed Richardson parameter chosen from the exact extreme eigenvalues. It is a coordinatewise-order statement, not a Euclidean-norm monotonicity statement. No claim is made for nonsymmetric \\(M\\)-matrices, preconditioned Richardson iteration, varying relaxation parameters, or nonzero initial guesses.

## Proof
For \\(n=1\\), the optimal parameter is the reciprocal of the single eigenvalue, so the first Richardson step is the exact solution and all subsequent iterates coincide with it.

For \\(n=2\\), write
\[
A=\\begin{pmatrix}a&-c\\\\-c&d\\end{pmatrix},\\qquad a>0,\\quad d>0,\\quad c\\ge0,\\quad ad-c^2>0.
\]
Because the sum of the two eigenvalues equals \\(a+d\\), the optimal parameter is \\(\\alpha=2/(a+d)\\). Set
\[
T=I-\\alpha A
 =\\frac1{a+d}\\begin{pmatrix}d-a&2c\\\\2c&a-d\\end{pmatrix}.
\]
A direct multiplication gives
\[
T^2=q^2I,\\qquad
q^2=\\frac{(a-d)^2+4c^2}{(a+d)^2}
=\\left(\\frac{\\lambda_{\\max}(A)-\\lambda_{\\min}(A)}{\\lambda_{\\max}(A)+\\lambda_{\\min}(A)}\\right)^2<1.
\]
Moreover, \\(I+T\\) is entrywise nonnegative because its diagonal entries are \\(2d/(a+d)\\) and \\(2a/(a+d)\\), and its off-diagonal entries are \\(2c/(a+d)\\).

Starting from zero,
\[
x^{(k)}=\\alpha\\sum_{j=0}^{k-1}T^j b.
\]
For \\(m\\ge1\\), pairing consecutive powers yields
\[
x^{(2m)}
=\\alpha\\sum_{r=0}^{m-1}q^{2r}(I+T)b\\ge0.
\]
For odd iterates,
\[
x^{(2m+1)}=x^{(2m)}+\\alpha q^{2m}b\\ge0.
\]
This proves universal nonnegativity in dimension two.

For the displayed three-dimensional witness, the iteration matrix is
\[
T=I-\\frac16A
=\\begin{pmatrix}-2/3&1/6&0\\\\1/6&-2/3&0\\\\0&0&5/6\\end{pmatrix}.
\]
Its eigenvalues are \\(5/6\\), \\(-1/2\\), and \\(-5/6\\), so the iteration converges. Exact multiplication gives the three iterates displayed above, with \\(x^{(3)}_1=-1/108\\). Therefore dimension three is sufficient for sign loss, while the preceding argument shows dimensions one and two are impossible; minimality follows.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to reconstruct the witness, the Richardson matrix, the first three iterates, the exact solution, and the characteristic polynomial values at \\(1\\), \\(9\\), and \\(11\\). It also checks the two-dimensional algebraic identity \\(T^2=q^2I\\) symbolically at the coefficient level. Its role is to replay the finite exact computations; the universal two-dimensional result is proved above, not inferred from finite testing.

## Relationship to prior work
Richardson iteration is classical. A public Royal Society report was already described in a Nature notice dated 20 January 1910. Later numerical-linear-algebra literature studies Richardson and cyclic Richardson acceleration under MSC 65F10. Vajteršic's 1985 paper explicitly writes the Richardson iteration matrix in the form \\(I-bM\\) and analyzes cyclic convergence parameters; Reichel's 1988 paper studies polynomial choices for Richardson iteration. These sources address convergence and acceleration rather than the present coordinatewise Stieltjes positivity/minimal-dimension statement.

The closest published-result search located a stagewise-safe Richardson result about Euclidean nonexpansion and acceleration barriers, not nonnegative cones or Stieltjes matrices. Separate searches for Richardson positivity, Stieltjes matrices, and \\(M\\)-matrices did not locate a statement implying the dimension-two protection theorem or the three-dimensional minimal counterexample. A 1979 paper of Micchelli and Willoughby characterizes scalar functions preserving the class of Stieltjes matrices; its accessible abstract concerns preservation of the Stieltjes sign class itself, not the entrywise nonnegativity of finite Richardson inverse approximants used here.

## Limitations
The result is specific to the exact spectral-optimal fixed parameter and the zero start. It does not classify all fixed relaxation parameters, all higher dimensions, or preconditioned variants. The three-dimensional witness is reducible; the negative third-iterate entry is strict, so the phenomenon persists under sufficiently small Stieltjes couplings by continuity, but no quantitative perturbation radius is claimed. Older matrix-iteration literature may use different terminology for coordinatewise monotonicity, which remains the principal originality risk.

## References
- L. F. Richardson, “The Approximate Arithmetical Solution by Finite Differences of Physical Problems Involving Differential Equations, with an Application to the Stresses in a Masonry Dam,” *Philosophical Transactions of the Royal Society A*, 210, 307–357. DOI: 10.1098/rsta.1911.0009. A public Nature notice describing the work appeared 20 January 1910, DOI: 10.1038/082357a0.
- M. Vajteršic, “Some iterative Poisson solvers applied to numerical solution of the model fourth-order elliptic problem,” *Aplikace matematiky* 30 (1985), 176–186. DOI: 10.21136/AM.1985.104140.
- L. Reichel, “Polynomials by Conformal Mapping for the Richardson Iteration Method for Complex Linear Systems,” *SIAM Journal on Numerical Analysis* 25 (1988), 1359–1368. DOI: 10.1137/0725077.
- C. A. Micchelli and R. Willoughby, “On functions which preserve the class of Stieltjes matrices,” *Linear Algebra and its Applications* (1979).
