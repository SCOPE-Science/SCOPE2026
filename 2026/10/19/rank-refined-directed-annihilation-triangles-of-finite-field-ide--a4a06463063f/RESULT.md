# Rank-refined directed annihilation triangles of finite-field idempotents

## Finding
Let \(q\) be any prime power, \(n\ge 2\), and \(0\le r,s,t\le n\). Write \(\mathbb F_q\) for the field of order \(q\), and let \(T_{n,q}(r,s,t)\) count **ordered** triples \((P,Q,R)\) in \(M_n(\mathbb F_q)\) satisfying
\[
P^2=P,\qquad Q^2=Q,\qquad R^2=R,\qquad PQ=QR=RP=0,
\]
with \(\operatorname{rank}P=r\), \(\operatorname{rank}Q=s\), and \(\operatorname{rank}R=t\). Products are ordinary ordered matrix products; no pairwise commutativity is assumed.

Set \(\genfrac{[}{]}{0pt}{}{a}{b}_q\) equal to the Gaussian coefficient, extended by zero when \(b\notin\{0,\ldots,a\}\); empty products equal one. If \(r+s>n\), then \(T_{n,q}(r,s,t)=0\). Otherwise,
\[
\boxed{\begin{aligned}
T_{n,q}(r,s,t)={}&{n\brack r}_q q^{r(n-r)}{n-r\brack s}_q q^{s(n-r-s)}\\
&\times\sum_{u=\max(0,r+s+t-n)}^{\min(r,s)}
{s\brack u}_q\left(\prod_{i=0}^{u-1}(q^r-q^i)\right)
{n-r-s+u\brack t}_q q^{t(n-t-u)}.
\end{aligned}}
\]
The sum is zero if its lower bound exceeds its upper bound. In every nonzero summand, all exponents are nonnegative integers. This formula enumerates matrices, not similarity classes, and includes the zero and identity idempotents at the boundary ranks.

For \(1\le r,s,t\le n-1\), such triples are precisely ordered directed three-cycles in the loopless graph whose vertices are nonzero proper idempotents and whose arrows are \(P\to Q\) exactly when \(PQ=0\). Their rank support is **exactly**
\[
\boxed{\quad r+s\le n,\qquad s+t\le n,\qquad t+r\le n.\quad}
\]
Consequently the largest sum of three ranks appearing in such a directed cycle is \(\lfloor3n/2\rfloor\), attained for every \(n\ge2\). For even \(n=2m\) with \(m\ge1\), the number of extremal ordered directed cycles with all three ranks equal to \(m\) is
\[
\boxed{T_{2m,q}(m,m,m)={2m\brack m}_q\,q^{m^2}\,|\mathrm{GL}_m(\mathbb F_q)|.}
\]
Each such extremal triple has all three reverse products \(QP\), \(RQ\), and \(PR\) of full rank \(m\), although all forward products vanish.

## Assumptions and scope
All matrices are \(n\times n\) over one finite field \(\mathbb F_q\), where \(q\) may have even or odd characteristic and may be a nonprime prime power. For the counting formula, \(0\le r,s,t\le n\). For the directed graph interpretation, exclude \(P=0\) and \(P=I\); then each nonzero idempotent has no zero-product loop, and any three-cycle has three distinct vertices. The parameter \(u\) below is the rank of \(QP\), which can be nonzero although \(PQ=0\).

## Proof
**1. Fix \(P\).** Every rank-\(r\) idempotent corresponds uniquely to a direct sum \(\mathbb F_q^n=E\oplus K\), where \(E=\operatorname{im}P\) has dimension \(r\) and \(K=\ker P\) has dimension \(n-r\). There are \({n\brack r}_q\) choices of \(E\), and \(q^{r(n-r)}\) complementary choices of \(K\). Relative to this sum, \(P=\operatorname{diag}(I_r,0)\).

**2. Count \(Q\) with \(PQ=0\) and \(\operatorname{rank}Q=s\).** Every such matrix has the unique block form
\[
Q=\begin{pmatrix}0&0\\ C&D\end{pmatrix},
\qquad D^2=D,\quad DC=C.
\]
Thus \(D\) is an idempotent of rank \(s\) on \(K\); \(\operatorname{im}C\subseteq\operatorname{im}D\), and \(\operatorname{rank}Q=s\). The number of possible \(D\) is \({n-r\brack s}_q q^{s(n-r-s)}\). When \(u=\operatorname{rank}C=\operatorname{rank}(QP)\), first choose the \(u\)-subspace \(\operatorname{im}C\) inside the \(s\)-space \(\operatorname{im}D\), then a surjection \(E\twoheadrightarrow\operatorname{im}C\). Their number is
\[
{s\brack u}_q\prod_{i=0}^{u-1}(q^r-q^i),\qquad 0\le u\le\min(r,s).
\]
In particular \(r+s\le n\) is necessary.

**3. Count \(R\) for fixed \((P,Q)\).** Put \(B=\ker Q\). The conditions \(QR=0\) and \(RP=0\) are equivalent to
\[
\operatorname{im}R\subseteq B,\qquad E\subseteq\ker R.
\]
Since \(\dim B=n-s\) and \(\dim(E\cap B)=r-u\), an image \(W=\operatorname{im}R\) of dimension \(t\) must lie in \(B\) and be disjoint from \(E\cap B\). There are exactly
\[
{n-r-s+u\brack t}_q q^{t(r-u)}
\]
possible \(W\): take a \(t\)-subspace of \(B/(E\cap B)\) and lift it as a graph of a linear map to \(E\cap B\). For each such \(W\), an idempotent \(R\) with \(\operatorname{im}R=W\) and \(R(E)=0\) is determined by an arbitrary map from a complement of \(E+W\) into \(W\). There are \(q^{t(n-t-r)}\) such idempotents. Hence the number of \(R\) is
\[
{n-r-s+u\brack t}_q q^{t(n-t-u)}.
\]
Multiplying the counts in Steps 1–3 and summing over the stated \(u\)-range proves the formula.

**4. Exact rank support.** Each equation \(PQ=0\) forces \(\operatorname{im}Q\subseteq\ker P\), hence \(r+s\le n\), and cycling gives the other two inequalities. Conversely, suppose all three inequalities hold. Then \(r+s\le n\) and the integer
\[
u_0=\max(0,r+s+t-n)
\]
satisfies \(u_0\le\min(r,s)\), because \(t+r\le n\) and \(t+s\le n\). Every factor of the summand at \(u=u_0\) is strictly positive over \(\mathbb F_q\); thus the triple occurs. Summing the three pairwise bounds gives \(r+s+t\le\lfloor3n/2\rfloor\). Equality is attained by \((m,m,m)\) when \(n=2m\), and by \((m+1,m,m)\) and its cyclic permutations when \(n=2m+1\).

**5. Extremal even case.** If \(n=2m\) and \(r=s=t=m\), the \(u\)-range reduces to the single value \(u=m\). Then \(D=I_K\), \(C:E\to K\) is an isomorphism, and \(R\) is uniquely fixed by \(\operatorname{im}R=\ker Q\), \(\ker R=E\). This yields \({2m\brack m}_q q^{m^2}|\mathrm{GL}_m(\mathbb F_q)|\). Applying the same argument cyclically shows \(\operatorname{rank}(QP)=\operatorname{rank}(RQ)=\operatorname{rank}(PR)=m\).

## Verification
The supplied `check_triangles.py` independently enumerates actual idempotent matrices and their ordered products, constructs the directed relation, counts all rank-refined closed directed walks of length three, and compares **every coefficient** with the formula. Exhaustive tests cover \((n,q)=(1,2),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\). The \(q=4\) implementation uses a polynomial-basis extension field. The test also verifies cyclic symmetry, support, and the total number of idempotents; larger symbolic formula-only checks cover \((5,2),(6,2),(5,3),(4,4)\).

For example, \(T_{3,2}(2,1,1)=168\), \(T_{4,2}(2,2,2)=3360\), and the total number of ordered directed triangles on nonzero proper idempotents of \(M_4(\mathbb F_2)\) is \(752640\). The proof, not finite testing, establishes the all-parameter statement.

## Relationship to prior work
Đurić, Jevđenić and Stopar introduce and analyze the directed compressed zero-divisor graph of \(M_n(\mathbb F_q)\) and give its subspace-pair adjacency model; their Section 3 computes vertex degrees and studies Hamiltonian cycles. That model supplies important background for the present question, but the inspected theorems do not calculate the rank-refined **idempotent-induced directed three-cycle census**, its exact rank support, or extremal multiplicities. Ferraz, Polcino Milies and Taufer count idempotent generators of individual left ideals; their results support the known projection/subspace correspondence but do not impose three oriented zero-product constraints. Huang counts arbitrary **mutually annihilating pairs** and a corresponding generating series; the present problem instead involves three idempotents with cyclic **one-sided** annihilation.

Earlier pair-rank formulas for idempotents can determine the number of a single oriented zero-product edge but do not, by themselves, impose the three dependent edge conditions or determine this rank-triple count. The Gaussian subspace machinery is standard; the claim of originality concerns the combined three-edge enumeration and sharp extremal profile, not these standard ingredients.

## Limitations
The result is for a complete matrix algebra over a finite field, not arbitrary finite rings or arbitrary matrices. It counts ordered triples; unlabelled cycles require division by three only after accounting for any graph conventions. It does not classify similarity orbits of triples or longer directed cycles. The exact enumeration and maximal rank sum have a direct proof, while novelty relative to unlocated matrix-graph enumerations remains an open bibliographic risk.

## References
1. A. Đurić, S. Jevđenić, N. Stopar, *Compressed zero-divisor graphs of noncommutative rings* (2018), arXiv:1810.02776v1; later published as *Compressed zero-divisor graphs of matrix rings over finite fields*, *Linear and Multilinear Algebra* 69 (2021), 2012–2039, DOI:10.1080/03081087.2019.1655523.
2. R. A. Ferraz, C. Polcino Milies, E. Taufer, *Left ideals in matrix rings over finite fields* (2017), arXiv:1711.09289v1.
3. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (2021), arXiv:2110.15566v1; *Journal of Algebra* (2023), DOI:10.1016/j.jalgebra.2022.11.021.
