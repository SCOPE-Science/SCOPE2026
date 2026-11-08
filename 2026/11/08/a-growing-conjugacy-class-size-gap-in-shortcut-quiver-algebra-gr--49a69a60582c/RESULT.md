# A growing conjugacy-class-size gap in shortcut-quiver algebra groups

## Finding

For every prime power \(q\) and integer \(m\geq1\), let \(Q_m\) be the acyclic quiver with four vertices, individual arrows \(a:1\to2\), \(b:2\to3\), \(c:3\to4\), and \(m\) independent arrows \(d_i:1\to3\), \(1\leq i\leq m\). Let \(J=\operatorname{rad}(\mathbb F_qQ_m)\), and let \(G=1+J\) be the algebra group. Put \(N=2m+6\), \(\rho(x)=\dim_{\mathbb F_q}[x,J]\), and \(T_r=|\{x\in J:\rho(x)=r\}|\). The distribution is given **completely** by the following additive specification (entries with equal indices are summed):

\[
\begin{aligned}
T_0&\mathrel{+}=q^{m+1},\\
T_1&\mathrel{+}=q^{m+1}(q^2-1)+q^{m+2}(q^m-1),\\
T_2&\mathrel{+}=(q-1)q^{m+3}+(q-1)q^{2m+3}
 +(q^m-1)(q-1)q^{m+2},\\
T_3&\mathrel{+}=(q-1)(q^{m+1}-1)q^{m+3},\\
T_{m+2}&\mathrel{+}=(q-1)q^{2m+4},\\
T_{m+3}&\mathrel{+}=(q-1)^2q^{2m+4}.
\end{aligned}
\]

Every unlisted \(T_r\) is zero. In particular, the precise number of conjugacy classes of size \(q^r\) is \(T_r/q^r\), and the total number of conjugacy classes is

\[
\boxed{k(G)=q^m\bigl(2q^{m+2}+2q^3-q^m-q^2-2q+1\bigr).}
\]

For every \(m\geq3\), the conjugacy-class sizes \(q^4,q^5,\ldots,q^{m+1}\) are *absent*, whereas sizes \(q^{m+2}\) and \(q^{m+3}\) both occur. This forbidden interval length grows with \(m\).

## Assumptions and scope

The field is any \(\mathbb F_q\), with no restriction on characteristic. Paths are multiplied by concatenation when endpoints agree and by zero otherwise. The radical \(J\) has basis

\[
a,b,c,d_1,\ldots,d_m,ab,bc,d_1c,\ldots,d_mc,abc
\]

and dimension \(N=2m+6\). The group \(1+J\) has \(q^N\) elements. Counts concern individual elements and conjugacy classes of this particular algebra group, not abstract isomorphism types or arbitrary quiver dimension vectors.

## Proof

Every element has a unique expression

\[
x=\alpha a+\beta b+\gamma c+\sum_i\delta_i d_i
 +Aab+Bbc+\sum_i E_i d_ic+Cabc.
\]

The \(m+1\) coefficients \(E_1,\ldots,E_m,C\) do not affect the commutator of \(x\) with any element of \(J\); they always contribute a free multiplicative factor \(q^{m+1}\) to rank strata. Write primed coefficients for a general \(y\in J\). Direct concatenation gives precisely the following commutator constraints:

\[
\begin{aligned}
\alpha\beta'-\alpha'\beta&=0,\\
\beta\gamma'-\beta'\gamma&=0,\\
\delta_i\gamma'-\delta_i'\gamma&=0\quad(1\leq i\leq m),\\
\alpha B'-\alpha'B+A\gamma'-A'\gamma&=0.
\end{aligned}
\]

Thus \(\rho(x)\) is the rank of the following matrix, with columns ordered as \((\alpha',\beta',\gamma',\delta_1',\ldots,\delta_m',A',B')\):

\[
\begin{pmatrix}
-\beta&\alpha&0&0&\cdots&0&0&0\\
0&-\gamma&\beta&0&\cdots&0&0&0\\
0&0&\delta_1&-\gamma&\cdots&0&0&0\\
\vdots&\vdots&\vdots&\vdots&&\vdots&\vdots&\vdots\\
0&0&\delta_m&0&\cdots&-\gamma&0&0\\
-B&0&A&0&\cdots&0&-\gamma&\alpha
\end{pmatrix}.
\]

Elementary row operations yield this exhaustive rank classification; here \(\delta=(\delta_1,\ldots,\delta_m)\):

| Conditions | Rank |
| --- | ---: |
| \(\gamma\ne0,\ \beta\ne0\) | \(m+3\) |
| \(\gamma\ne0,\ \beta=0\) | \(m+2\) |
| \(\gamma=0,\ \alpha\ne0,\ (\beta,\delta)\ne0\) | \(3\) |
| \(\gamma=0,\ \alpha\ne0,\ (\beta,\delta)=0\) | \(2\) |
| \(\alpha=\gamma=0,\ \beta\ne0\) | \(2\) |
| \(\alpha=\beta=\gamma=0,\ \delta\ne0,\ B\ne0\) | \(2\) |
| \(\alpha=\beta=\gamma=0,\ \delta\ne0,\ B=0\) | \(1\) |
| \(\alpha=\beta=\gamma=\delta=0,\ (A,B)\ne0\) | \(1\) |
| \(\alpha=\beta=\gamma=\delta=A=B=0\) | \(0\) |

For clarity about the two high ranks: when \(\gamma\ne0\), the \(m\) rows indexed by \(\delta_i\) are independent, and the last row has the unique \(A'\)-pivot, while the first two rows have rank two exactly when \(\beta\ne0\), otherwise rank one. When \(\gamma=0\), the \(m\) indexed rows all lie in the single \(\gamma'\)-column, leaving the remaining small matrix whose pivots give the other seven cases.

Counting each row of this classification over \(\alpha,\beta,\gamma,\delta,A,B\), then multiplying by \(q^{m+1}\) for the unused \(E_i,C\), gives each of the six additive contributions to \(T_r\) in the finding. The case partitions are disjoint and exhaustive, so \(\sum_rT_r=q^{2m+6}\). This is an identity for every finite field, not an inference from examples.

The group elements \(1+x\) and \(1+y\) commute exactly when \([x,y]=0\). Hence \(|C_G(1+x)|=q^{N-\rho(x)}\), and its conjugacy class has size \(q^{\rho(x)}\). Accordingly there are \(T_r/q^r\) classes of that size and

\[
k(G)=\sum_r\frac{T_r}{q^r}
=q^m\bigl(2q^{m+2}+2q^3-q^m-q^2-2q+1\bigr).
\]

All six displayed contributions are strictly positive for \(q\ge2\), including both large ranks. For \(m\ge3\), the listed exponents contain none of \(4,\ldots,m+1\); this proves the sharp gap. For \(m=1\), the contributions indexed by \(3\) and \(m+2\) coalesce and must be added.

## Verification

The standalone script `verify.py` builds the radical directly from the list of arrow paths, constructs every multiplication product by concatenation, and for every radical element computes the rank of its actual adjoint map using modular Gaussian elimination. It asserts the complete rank distributions and conjugacy-class totals for \((q,m)=(2,1),(2,2),(2,3),(3,1)\). It separately exhausts all \(2^{16}\) ordered pairs in the smallest binary case, directly testing commutation rather than using the rank formula. It terminates with `VERIFY_OK`.

For \((q,m)=(2,1)\), it obtains rank multiplicities \((4,20,56,112,64)\) at ranks \(0,1,2,3,4\), and \(46\) classes. For \((q,m)=(2,3)\), ranks \(0,1,2,3,5,6\) occur with multiplicities \((16,272,800,960,1024,1024)\), and there are \(520\) classes. These finite checks are independent of the symbolic case count but do not replace the unrestricted proof.

## Relationship to prior work

Hennecart and Perry (2022) formulate a quiver analogue of Higman's commuting-pair counting question for radicals of endomorphism algebras of projective quiver representations. Their solved families include quivers with no directed path longer than two and their reduction operations. The present quiver has the genuine length-three path \(abc\), and its direct arrows \(1\to3\) create an extra family of commutator constraints; its unique source and sink are not separating vertices for the relevant splitting operation. The present theorem gives a stronger elementwise centralizer-rank distribution, not just one commuting-pair total.

Pak and Soffer (2015) study conjugacy classes of unitriangular and pattern groups with a broad computational-recurrence approach. This source provides background; no priority claim is made on the basis of its abstract alone. The displayed rank spectrum and gap are proved independently here. No claim of definitive literature priority is made.

## Limitations

The theorem does not cover longer paths, nontrivial projective multiplicity vectors, relations among arrows, or arbitrary pattern groups. The full family is proved algebraically, while the verifier tests only the listed small prime-field cases. The possibility that a broader centralizer or pattern-group theorem subsumes these formulas remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1, publicly posted 2022-08-16. https://arxiv.org/html/2208.07738v1
2. I. Pak and A. Soffer, *On Higman's \(k(U_n(\mathbb F_q))\) conjecture*, arXiv:1507.00411, publicly posted 2015-07-02. https://arxiv.org/abs/1507.00411
