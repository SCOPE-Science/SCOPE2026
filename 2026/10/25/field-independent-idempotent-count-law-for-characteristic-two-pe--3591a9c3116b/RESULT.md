# Field-independent idempotent-count law for characteristic-two perfect evolution algebras

## Finding

The complete distribution of the number of idempotent **elements** of a uniformly sampled perfect evolution algebra structure matrix in characteristic two is independent of the field extension degree. This statement concerns idempotent elements, not the terminology “idempotent evolution algebra” sometimes used for the condition \(E^2=E\).

For integers \(n,e\ge1\), let \(q=2^e\). Select \(A\) uniformly from \(\mathrm{GL}_n(\mathbb F_q)\), and let \(I(A)\) be the number of elements \(v\) satisfying \(v^2=v\) in the evolution algebra whose structure matrix is \(A\). If \(C\) is uniform in \(\mathrm{GL}_n(\mathbb F_2)\), then

\[
 I(A)\ \overset{\mathrm d}=\ 2^{\dim_{\mathbb F_2}\ker(C-I_n)}.
\]

In particular every possible number of idempotents is a power of two; the law depends only on \(n\), not on \(q\). It is **matrix-uniform**, not uniform over isomorphism classes.

For \(m\ge0\), put \(G_m=|\mathrm{GL}_m(\mathbb F_2)|\), with \(G_0=1\), and let \({a\brack b}_2\) denote the Gaussian binomial coefficient, with \({a\brack0}_2=1\). For \(0\le k\le n\), define

\[
N_{n,k}={n\brack k}_2\sum_{j=0}^{n-k}(-1)^j2^{\binom j2}
{n-k\brack j}_2\,2^{(k+j)(n-k-j)}G_{n-k-j}.
\]

Then the number of invertible structure matrices \(A\) having exactly \(2^k\) idempotent elements is **exactly**

\[
 |\mathrm{GL}_n(\mathbb F_q)|\frac{N_{n,k}}{G_n},
\qquad
\Pr(I(A)=2^k)=\frac{N_{n,k}}{G_n}.
\]

The latter formula also applies when \(N_{n,k}=0\), e.g. \(n=1,k=0\). For \(n=2\), the probabilities of respectively \(1,2,4\) idempotents are \(1/3,1/2,1/6\), for every field \(\mathbb F_{2^e}\). For \(n=3\), the counts among the \(168\) matrices over \(\mathbb F_2\) are \(48,98,21,1\) for respectively \(1,2,4,8\) idempotents.

## Assumptions and scope

An evolution algebra over \(\mathbb F_q\) has a natural basis \(e_1,\ldots,e_n\), satisfies \(e_i e_j=0\) whenever \(i\ne j\), and has products \(e_i^2=\sum_j A_{ij}e_j\). No associativity is assumed. “Perfect” means \(E^2=E\); equivalently the square matrix \(A\) is invertible. Thus every matrix in \(\mathrm{GL}_n(\mathbb F_q)\) parametrizes a perfect evolution-algebra structure in the specified basis.

Vectors are columns. For a matrix or vector \(X\), the notation \(X^{[t]}\) means apply the \(t\)-th power to each entry. The coordinate equation for an idempotent is

\[
 x=A^{\mathsf T}x^{[2]}.
\]

The absolute algebraic closure \(\overline{\mathbb F}_2\) is used for the proof. The resulting distribution concerns the \(\mathbb F_q\)-rational idempotents and every positive \(n,e\), not merely asymptotic field sizes.

## Proof

**Step 1 (geometric Frobenius coordinates).** Set \(M=A^{\mathsf T}\). The semilinear map \(F_M(x)=Mx^{[2]}\) acts on \(\overline{\mathbb F}_2^n\). Lang's theorem for \(\mathrm{GL}_n\), equivalently the semilinear normal-form theorem, gives \(B\in\mathrm{GL}_n(\overline{\mathbb F}_2)\) with

\[
 M=B(B^{[2]})^{-1}.
\]

For \(x=By\), the equation \(F_M(x)=x\) is equivalent to \(y^{[2]}=y\). Therefore **all geometric idempotents** form precisely the \(n\)-dimensional \(\mathbb F_2\)-vector space \(B\mathbb F_2^n\), consisting of \(2^n\) points. This invocation of Lang's theorem is classical and is not claimed as a new lemma.

**Step 2 (finite-field descent).** Define \(C=B^{-1}B^{[q]}\), with \(q=2^e\). Since \(M^{[q]}=M\), the displayed equation for \(M\) implies

\[
 C^{[2]}=(B^{[2]})^{-1}B^{[2q]}=B^{-1}B^{[q]}=C.
\]

Hence \(C\in\mathrm{GL}_n(\mathbb F_2)\). A geometric fixed point \(By\), for \(y\in\mathbb F_2^n\), lies in \(\mathbb F_q^n\) exactly when

\[
 (By)^{[q]}=By\quad\Longleftrightarrow\quad Cy=y.
\]

Consequently \(I(A)=2^{\dim\ker(C-I_n)}\). Changing \(B\) by right multiplication with any element of \(\mathrm{GL}_n(\mathbb F_2)\) conjugates \(C\), so its conjugacy class is well-defined.

**Step 3 (uniformity of the descent class).** Put \(G=\mathrm{GL}_n(\mathbb F_q)\). It acts on invertible \(M\) by the twisted conjugation \(M\mapsto P M(P^{[2]})^{-1}\). Each orbit determines a \(\mathrm{GL}_n(\mathbb F_2)\)-conjugacy class of \(C\). Conversely, if two choices of \(B\) give the same \(C\), their quotient \(P=B'B^{-1}\) is fixed by the \(q\)-th Frobenius, hence \(P\in G\), and they describe matrices in the same twisted orbit. Every \(C\in\mathrm{GL}_n(\mathbb F_2)\) occurs: a solution of \(B^{[q]}=BC\) exists by Lang's theorem for the \(q\)-th Frobenius; the corresponding \(M=B(B^{[2]})^{-1}\) is \(q\)-rational. Thus the twisted orbits are indexed bijectively by conjugacy classes of \(\mathrm{GL}_n(\mathbb F_2)\).

A rational stabilizer \(P\) of \(M\), written as \(P=BQB^{-1}\), satisfies \(Q^{[2]}=Q\) and \(CQC^{-1}=Q\). Thus its order is \(|Z_{\mathrm{GL}_n(\mathbb F_2)}(C)|\). By orbit–stabilizer, the fraction of all \(M\in G\) in the orbit associated with a class \([C]\) equals

\[
\frac{1}{|Z_{\mathrm{GL}_n(\mathbb F_2)}(C)|}
=\frac{|[C]|}{G_n}.
\]

This is exactly the conjugacy-class distribution obtained from a *uniform* matrix \(C\in\mathrm{GL}_n(\mathbb F_2)\). Since transposition is a bijection on \(G\), the same statement holds for uniform \(A\).

**Step 4 (closed finite formula).** Fix a subspace \(U\subseteq\mathbb F_2^n\) of dimension \(s\). Exactly \(2^{s(n-s)}G_{n-s}\) invertible binary matrices fix every vector in \(U\) (write them in block upper-triangular form relative to a basis extending \(U\)). The Möbius function for a codimension-\(j\) interval in the binary subspace lattice is \((-1)^j2^{\binom j2}\). Möbius inversion on the lattice of subspaces containing a fixed \(k\)-space, followed by multiplication by the number \({n\brack k}_2\) of such \(k\)-spaces, gives precisely \(N_{n,k}\). Therefore \(N_{n,k}\) counts binary invertible matrices whose fixed space has dimension exactly \(k\), proving the stated probability and exact number of original structure matrices.

All four steps are exact and uniform over the full stated domain. The proof uses the classical Lang/semilinear theorem as an input and proves the finite-field descent and counting refinement.

## Verification

The standalone Python 3 checker `evolution_idempotent_checker.py` represents finite fields as polynomial residue fields, enumerates **all** invertible structure matrices in the specified small cases, and directly counts the vectors solving \(x=Mx^{[2]}\). The checker independently computes the Gaussian-binomial inclusion–exclusion formula and compares every frequency.

The exhaustive instances are \((q,n)=(2,1),(4,1),(8,1),(2,2),(4,2),(8,2),(2,3),(2,4)\). They cover exactly \(24{,}053\) invertible structure matrices. In particular for \(q=4,n=2\) the frequencies at \(1,2,4\) are \(60,90,30\), while for \(q=8,n=2\) they are \(1176,1764,588\). For \(q=2,n=4\), the respective frequencies at \(1,2,4,8,16\) are \(5824,11640,2590,105,1\). The program reports `ALL_CHARACTERISTIC_TWO_EVOLUTION_CHECKS_PASSED 24053`.

These finite checks are not proofs for arbitrary \(n\) or \(q\); those are given by the Lang descent and orbit argument above. The checker uses no external packages.

## Relationship to prior work

Wei and Zou's 2023 work classifies **perfect evolution algebras up to isomorphism** by a monomial group action and counts those classes in finite fields. Its main theorem computes an isomorphism-class count, not the distribution of the number of rational idempotent elements under a uniform invertible structure matrix. The present calculation samples matrices in a fixed natural basis instead.

Kaygorodov, Martín González, and Viruel (2026), Remark 23, proved that a random invertible evolution structure matrix over **any** finite field has **mean exactly one nonzero idempotent**. They also discuss geometric idempotents and the generic characteristic-zero permutation-Galois conjecture. These are prior results; the present complete binary-characteristic probability distribution refines the mean but does not claim it as new. In fact its expected number of idempotents is \(2\), agreeing with their result.

Dempwolff, Fisher, and Herman (2000) prove the semilinear normal-form theorem used in Step 1. That theorem is acknowledged in full. The application here is the exact descent-class distribution and explicit lattice-inversion census for idempotent elements of perfect evolution algebras.

## Limitations

The theorem assumes characteristic two and an **invertible** structure matrix. It neither covers singular evolution matrices nor asserts that the same law holds over odd characteristic. Its sampling measure is uniform over \(\mathrm{GL}_n(\mathbb F_q)\), not uniform over algebra isomorphism classes. The proof is an application of classical semilinear descent and group counting; it does not independently establish historical novelty among all papers on Frobenius-linear equations. Specialist literature could contain an equivalent result using different terminology. No independent mathematical audit has been performed.

## References

1. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first posted 2023-10-18; https://arxiv.org/pdf/2310.12368. In particular Introduction, Theorem 1.1 and Theorem 2.1.
2. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (2026), especially §1.1 and Remark 23; https://arxiv.org/html/2610.22248v1.
3. U. Dempwolff, J. C. Fisher and A. Herman, *Semilinear Transformations over Finite Fields are Frobenius Maps*, Glasgow Mathematical Journal 42 (2000), 289–295, DOI:10.1017/S0017089500020164. Classical semilinear normal form.
