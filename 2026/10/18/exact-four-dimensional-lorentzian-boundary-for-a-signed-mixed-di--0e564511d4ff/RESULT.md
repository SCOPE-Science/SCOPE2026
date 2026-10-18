# Exact four-dimensional Lorentzian boundary for a signed mixed discriminant

## Finding
Let \(Z\neq0\) be a real symmetric \(4\times4\) matrix with eigenvalues \(\lambda_1\le\lambda_2\le\lambda_3\le\lambda_4\), and let \(e_k(Z)\) denote the \(k\)-th elementary symmetric polynomial in these four eigenvalues. Let \(\mathsf D\) be the symmetric polarization of the determinant, normalized by \(\mathsf D(I_4,I_4,I_4,I_4)=1\). The real quadratic form
\[
Q_Z(A)=\mathsf D(A,A,Z,I_4),\qquad A\in\operatorname{Sym}_4(\mathbb R),
\]
has **exactly one positive eigenvalue**, with every other eigenvalue nonpositive (zero eigenvalues allowed), **if and only if**
\[
\boxed{\lambda_1+\lambda_2\ge0\quad\text{and}\quad e_1(Z)e_3(Z)\ge4e_4(Z).}
\]
The boundary case of equality in the second condition is included. Under these equivalent conditions the reverse Cauchy–Schwarz inequality
\[
\mathsf D(A,B,Z,I_4)^2\ge Q_Z(A)Q_Z(B)
\]
holds for every real symmetric \(A\) and \(B\) for which \(Q_Z(B)\ge0\); more precisely, the assertion holds for all \(A\) whenever \(Q_Z(B)>0\), and also when \(Q_Z(B)=0\) by the trivial nonnegativity of the squared term if \(Q_Z(A)Q_Z(B)=0\). In particular it holds for all positive semidefinite \(A,B\).

The criterion strictly extends the previously established sufficient spectral-balance condition. For instance \(Z=\operatorname{diag}(-1,3,4,100)\) satisfies the displayed conditions although it violates \(\lambda_1+\lambda_2+\lambda_3\ge\lambda_4\). Conversely, \(Z=\operatorname{diag}(-1,1,2,3)\) satisfies the nonnegative complementary-pair condition but violates the determinant condition and the reverse inequality **even for positive definite arguments**. Specifically, with \(B=I_4\), \(H=\operatorname{diag}(0,1,3,-4)\), and \(A_t=I_4+tH\), \(0<t<1/4\), the reverse-inequality deficit is
\[
\mathsf D(A_t,B,Z,I_4)^2-Q_Z(A_t)Q_Z(B)=-\frac{5t^2}{144}<0.
\]
These examples are consequences and sharp domain demonstrations of the single spectral-classification theorem.

## Assumptions and scope
All matrices are real symmetric. The quadratic form acts on the full ten-dimensional vector space \(\operatorname{Sym}_4(\mathbb R)\), not merely diagonal or positive-semidefinite matrices. By "one positive eigenvalue" we mean positive index exactly one, counting multiplicities, with the remaining signature possibly degenerate; it is independent of the chosen Euclidean inner product on the matrix space. The condition \(Z\ne0\) excludes the identically zero quadratic form. Repeated eigenvalues and endpoint equalities are permitted. \(\mathsf D\) is defined by
\[
\det(t_1A_1+\cdots+t_4A_4)=\sum_{i_1,\ldots,i_4=1}^4 \mathsf D(A_{i_1},\ldots,A_{i_4})\,t_{i_1}\cdots t_{i_4}.
\]

## Proof
**1. Coordinate formula and orthogonal blocks.** Orthogonally diagonalize \(Z\). Let \(w_{ij}=\sum_{k\notin\{i,j\}}\lambda_k\) for \(i\ne j\) and define \(W=(w_{ij})_{i,j=1}^4\) with zero diagonal. The four-dimensional specialization of the mixed-discriminant polarization identity (also derivable directly from the determinant expansion) gives, for \(A=(a_{ij})\),
\[
Q_Z(A)=\frac1{12}\sum_{1\le i<j\le4}w_{ij}(a_{ii}a_{jj}-a_{ij}^2).
\]
Consequently, writing \(v=(a_{11},\ldots,a_{44})\),
\[
Q_Z(A)=\frac1{24}v^{\mathsf T}Wv-\frac1{12}\sum_{i<j}w_{ij}a_{ij}^2.
\]
Thus the inertia of \(Q_Z\) is exactly the inertia of the real symmetric \(4\times4\) matrix \(W\), augmented by one negative direction when \(w_{ij}>0\), one positive direction when \(w_{ij}<0\), or a kernel direction when \(w_{ij}=0\), for each of the six pairs. Factors \(1/24\) and \(1/12\) do not affect inertia.

**2. Positivity of complementary pairs is necessary.** The matrix \(W\) is not zero if \(Z\ne0\): if every complementary pair sum vanished, pairwise subtraction would make all four \(\lambda_i\) equal and hence zero. Since \(\operatorname{tr}W=0\) and \(W\ne0\), \(W\) has at least one strictly positive eigenvalue. If any \(w_{ij}<0\), the corresponding off-diagonal matrix direction is a second independent positive direction of \(Q_Z\), making its positive index at least two. Hence a one-positive form must satisfy \(w_{ij}\ge0\) for all pairs, equivalent to the smallest complementary sum \(\lambda_1+\lambda_2\ge0\).

**3. The determinant decides the remaining signature exactly.** Assume all \(w_{ij}\ge0\). Then \(W\) is a real symmetric nonzero entrywise-nonnegative matrix, with \(\operatorname{tr}W=0\). The Perron–Frobenius bound ensures that its largest positive eigenvalue \(\mu_1\) equals the spectral radius; write the remaining eigenvalues in decreasing order \(\mu_2\ge\mu_3\ge\mu_4\). If \(\mu_2>0\) and \(\mu_3\ge0\), then \(\mu_4=-\mu_1-\mu_2-\mu_3<-\mu_1\), contradicting that spectral-radius bound. Thus \(\mu_2>0\) implies \(\mu_3,\mu_4<0\), so \(\det W>0\). If instead \(\mu_2\le0\), \(W\) has exactly one positive eigenvalue and \(\det W\le0\). The converse follows because \(\det W>0\) is impossible if \(\mu_2\le0\), and \(\det W\le0\) impossible if \(\mu_2>0\). Therefore \(W\) has exactly one positive eigenvalue if and only if \(\det W\le0\).

**4. Exact symmetric-polynomial identity.** Write the upper-triangle entries of \(W\), in order \((12),(13),(14),(23),(24),(34)\), as \(a,b,c,d,e,f\). A direct expansion gives
\[
\det W=a^2f^2+b^2e^2+c^2d^2-2(abef+acdf+bcde).
\]
Substituting the complementary eigenvalue sums and collecting symmetric monomials yields
\[
\boxed{\det W=-4\bigl(e_1(Z)e_3(Z)-4e_4(Z)\bigr).}
\]
Every step is a polynomial identity in four arbitrary real eigenvalues, so degeneracies are included. Combining Steps 1–4 gives the claimed necessary-and-sufficient criterion. The executable symbolic check independently expands the identity over \(\mathbb Z[\lambda_1,\ldots,\lambda_4]\), rather than sampling only finitely many matrices.

**5. Reverse inequality and explicit boundary counterexample.** A symmetric quadratic form of positive index one satisfies reverse Cauchy–Schwarz when its second argument has positive value, by orthogonal decomposition into its positive line and nonpositive orthogonal complement. If the second value is zero, the stated inequality is automatic. The formula above shows \(Q_Z(B)\ge0\) for positive-semidefinite \(B\) whenever all \(w_{ij}\ge0\): all \(2\times2\) principal minors of \(B\) are nonnegative. For \(Z=\operatorname{diag}(-1,3,4,100)\), we have \(\lambda_1+\lambda_2=2\) and \(e_1e_3-4e_4=56528>0\), yet \(\lambda_1+\lambda_2+\lambda_3=6<100\). For \(Z=\operatorname{diag}(-1,1,2,3)\), the complementary sums \((w_{12},w_{13},w_{14},w_{23},w_{24},w_{34})\) are \((5,4,3,2,1,0)\), and \(e_1e_3-4e_4=-1\); the diagonal direction \(H=\operatorname{diag}(0,1,3,-4)\) yields \(Q_Z(I_4)=5/4\), \(Q_Z(H)=1/6\), and \(\mathsf D(H,I_4,Z,I_4)=5/12\). Polarization then gives the deficit \(-5t^2/144\), as displayed. The eigenvalues of \(A_t\) are \(1,1+t,1+3t,1-4t\), all positive for \(0<t<1/4\).

## Verification
Execute the fully embedded standalone program `verify.py` with Python 3 and SymPy installed. It checks the generic coefficient identity for arbitrary symbolic eigenvalues, the normalized mixed-discriminant expansion, both explicit examples, and the strict positive-definite failure, using exact symbolic arithmetic. The analytic Perron–Frobenius argument in Step 3 establishes the infinite-dimensional quantification over real parameter tuples; a finite numerical census is neither asserted nor needed. All formulas and the code are contained in this package.

## Relationship to prior work
Brauner and Ortega-Moreno (arXiv:2610.08746v1, 6 October 2026) prove hyperbolicity of related mixed-discriminant forms under a sufficient spectral-balance condition. Their Proposition 4.5 treats exactly this two-free-argument base case using the stronger vanishing-trace hyperplane criterion; their Lemma 4.2 supplies the polarization formula. The present theorem answers the more specific necessary-and-sufficient **inertia** question in dimension four using a determinant boundary, includes degenerate cases, provides a signed example outside their balance cone, and shows that nonnegative complementary sums alone do not suffice. Ross–Süss–Wannerer (arXiv:2304.08399) give general mixed-discriminant AF inequalities with positive-definite reference forms and dually Lorentzian operators, not this spectral decision criterion for a fixed indefinite reference. Classical AF theory similarly covers positive-semidefinite reference matrices. The exact polynomial-sign boundary and both example implications were compared with these specific statements; no claim of exhaustive historical priority is made.

## Limitations
The classification is special to four dimensions and the reference tuple \((Z,I_4)\). It does not classify the analogous quadratic form with multiple arbitrary reference matrices, nor the infinite-dimensional support-function mixed-volume form. Singular nonzero \(Z\) are allowed; \(Z=0\) is intentionally excluded. The proof uses Perron–Frobenius, not an explicit formula for the four eigenvalues of \(W\). Published-source coverage may be incomplete, so originality remains subject to independent literature assessment. No independent audit has been performed.

## References
1. Leo Brauner and Oscar Ortega-Moreno, *Hyperbolicity Beyond Convexity in the Alexandrov–Fenchel Inequality*, arXiv:2610.08746v1 (first publicly posted 6 October 2026), https://arxiv.org/html/2610.08746v1. In particular §4.1 Lemma 4.2 and §4.2 Proposition 4.5.
2. Julius Ross, Hendrik Süß, and Thomas Wannerer, *Dually Lorentzian Polynomials*, arXiv:2304.08399 (2023), §8.1 Theorems 8.1–8.2; *Monatshefte für Mathematik* **208** (2025), 495–524; https://link.springer.com/article/10.1007/s00605-025-02134-6.
3. Yair Shenfeld and Ramon van Handel, *Mixed Volumes and the Bochner Method*, arXiv:1811.08710 (2018), https://arxiv.org/abs/1811.08710.
