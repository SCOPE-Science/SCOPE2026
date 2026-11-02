# The four-stratum two-sided flip spectrum of bilinear finite braces

## Finding

For every odd prime power \(q\), put \(V=\mathbb F_q^2\). For every invertible \(2\times2\) matrix \(M\) over \(\mathbb F_q\), form the associative nilpotent algebra \(R_M=V\oplus\mathbb F_qz\), whose multiplication is
\[
(u,s)(v,t)=(0,u^{\mathsf T}Mv).
\]
The circle operation \(x\circ y=x+y+xy\) defines a two-sided brace, and the associated involutive Yang--Baxter map is
\[
r_M((u,s),(v,t))=((v,t+u^{\mathsf T}Mv),(u,s-v^{\mathsf T}Mu)).
\]
For a solution \(r(x,y)=(\lambda_x(y),\rho_y(x))\), write \(P_{\mathrm{flip},1}\) for the fraction of ordered pairs on which \(r\) acts as the flip in *both* orders, \(P_{\mathrm{flip},2}\) for the fraction with \(r^2(x,y)=(x,y)\) and \(\lambda_x(y)=y\), and \(P_{\mathrm{left}},P_{\mathrm{right}}\) for the individual coordinate-fixed fractions (the definitions of Ferrara--Trombetti--Tsang).

The three latter probabilities are independent of \(M\):
\[
P_{\mathrm{flip},2}=P_{\mathrm{left}}=P_{\mathrm{right}}=\frac{q^2+q-1}{q^3}.
\]
The first probability has **three possible values for \(q=3\), and exactly four for all odd \(q\geq5\)**. The exact distribution over the *labeled matrices* \(M\in\mathrm{GL}_2(\mathbb F_q)\) is:

| \(P_{\mathrm{flip},1}\) | Number of matrices \(M\) |
| --- | ---: |
| \(\dfrac{2q^2-1}{q^4}\) | \(\dfrac{q(q-1)^3}{2}\) |
| \(\dfrac{3q-2}{q^3}\) | \((q-1)(q^2-1)\) |
| \(\dfrac{(2q-1)^2}{q^4}\) | \(\dfrac{q(q-1)(q+1)(q-3)}{2}\) |
| \(\dfrac{q^2+q-1}{q^3}\) | \((q-1)(q^2+1)\) |

The table entries sum to \(|\mathrm{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\). This is a distribution for matrices giving bilinear products in a fixed basis, *not* a count of nonisomorphic braces.

There is also a uniform higher-dimensional invariant: for any \(d\geq1\), nondegenerate bilinear product determined by \(M\in\mathrm{GL}_d(\mathbb F_q)\), and cosquare \(T=M^{-1}M^{\mathsf T}\), put
\[
s(M)=\sum_{\lambda\in\mathbb F_q}\left(q^{\dim\ker(T-\lambda I)}-1\right).
\]
Then
\[
P_{\mathrm{flip},1}=q^{-2}+(1-q^{-d})q^{-d}+(q^{-1}-q^{-2})s(M)q^{-d}.
\]
In particular the probability is constant under congruence of the bilinear form, because its cosquare changes by similarity.

## Assumptions and scope

Throughout, \(q\) is any odd prime power. All vector spaces, matrices, kernels, quadratic characters, and counts are over \(\mathbb F_q\). The algebra has no required identity; \(z\) spans an annihilating ideal and \(R_M^3=0\). Nondegeneracy means \(\det M\ne0\). The brace's underlying set has cardinality \(q^3\) for \(d=2\), and cardinality \(q^{d+1}\) in general. A probability always uses uniformly random *ordered* pairs of brace elements; there is no isomorphism weighting.

## Proof

**1. Construction and the solution.** Bilinear multiplication has \(R_M^2\subseteq\mathbb F_qz\) and \(R_M^3=0\), so associativity holds and every element is quasi-regular: its circle inverse is \(-x+x^2\). The standard radical-ring/brace construction gives a two-sided brace with additive abelian group. Since \(\lambda_x(y)=y+xy\), and the inverse lambda map subtracts multiplication by \(x\), the usual brace Yang--Baxter formula simplifies exactly to the displayed \(r_M\); equivalently substitution directly verifies \(r_M^2=\mathrm{id}\). In particular, an ordered pair is a two-sided flip pair precisely when both \(u^{\mathsf T}Mv=0\) and \(v^{\mathsf T}Mu=0\). Since the solution is involutive, \(P_{\mathrm{flip},2}=P_{\mathrm{left}}\), while the right probability counts the transpose equation and agrees by interchanging inputs.

**2. General cosquare formula.** Fix \(u\in\mathbb F_q^d\). If \(u=0\), every one of the \(q^d\) possible \(v\) satisfies both equations. If \(u\ne0\), the two linear functionals of \(v\), with coefficient rows \(u^{\mathsf T}M\) and \(u^{\mathsf T}M^{\mathsf T}\), are nonzero. They are dependent exactly when \(u\) is an eigenvector of \(T=M^{-1}M^{\mathsf T}\): transposing proportionality gives \(M^{\mathsf T}u=\lambda Mu\). Hence the common kernel contains \(q^{d-1}\) vectors when the functionals are dependent, and \(q^{d-2}\) otherwise. Distinct eigenvalues have disjoint nonzero eigenspaces, so the number of nonzero \(u\) in the dependent case is precisely \(s(M)\). The number of vector pairs obeying both equations is therefore
\[
q^d+s(M)q^{d-1}+(q^d-1-s(M))q^{d-2}.
\]
The two extra central coordinates multiply the numerator and total number of pairs by the same factor \(q^2\). Division by \(q^{2d}\) proves the formula. For a single equation, every \(u\ne0\) gives \(q^{d-1}\) partner vectors, so
\[
P_{\mathrm{left}}=P_{\mathrm{right}}=q^{-d}+(1-q^{-d})q^{-1}.
\]
With \(d=2\) this is \((q^2+q-1)/q^3\), and the joint numerator is \(2q^2-1+(q-1)s(M)\).

**3. The possible cosquare eigenspace sizes when \(d=2\).** Write
\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad h=b-c,\qquad D=ad-bc\ne0,\qquad \delta=h^2/D.
\]
Direct matrix multiplication gives
\[
\operatorname{tr}T=2-\delta,\quad\det T=1,\quad
\operatorname{disc}\det(tI-T)=\delta(\delta-4).
\]
When \(h=0\), the form is symmetric, so \(T=I\); when \(M\) is alternating, \(T=-I\). Both cases yield \(s=q^2-1\). Otherwise \(h\ne0\), and \(\delta\ne0\). When \(\delta=4\), the characteristic polynomial is \((t+1)^2\), and the excluded alternating case is the only diagonalizable one; thus there is one eigenline and \(s=q-1\). For \(\delta\ne4\), the characteristic polynomial has distinct roots over \(\mathbb F_q\) precisely when \(\chi(\delta(\delta-4))=1\), giving \(s=2(q-1)\); the nonsquare case gives no eigenlines and \(s=0\). Here \(\chi\) is the quadratic character with \(\chi(0)=0\). This proves the four possible probabilities, subject to realizing the types.

**4. Counting matrices in each type.** The symmetric invertible matrices number \(q^3-q^2\): of \(q^3\) symmetric matrices, exactly \(q^2\) have determinant zero. There are \(q-1\) invertible alternating matrices. Their combined count is \((q-1)(q^2+1)\).

For each fixed \(h\ne0\), write
\[
M=S+\frac h2\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad S=S^{\mathsf T},\qquad D=\det S+h^2/4.
\]
For fixed \(\delta\ne0\) the required symmetric determinant is \(k=h^2(4-\delta)/(4\delta)\). Elementary counting gives \(q^2\) symmetric \(2\times2\) matrices of determinant zero and, for nonzero \(k\), exactly \(q(q+\chi(-k))\) of determinant \(k\). The latter is \(q(q+\chi(\delta(\delta-4)))\) by the square-class identity. Thus \(\delta=4\) yields \(q^2\) matrices per \(h\ne0\), exactly one of them alternating, giving \((q-1)(q^2-1)\) with a single eigenline.

To count the other discriminants, \(\sum_{\delta\in\mathbb F_q}\chi(\delta(\delta-4))=-1\). Indeed, changing variables \(t=\delta-2\) gives \(t^2-4\), and counting \(y^2=t^2-4\) is equivalent to factoring \((t-y)(t+y)=4\), which has precisely \(q-1\) solutions; therefore the character sum is \((q-1)-q=-1\). Of the \(q-2\) values \(\delta\notin\{0,4\}\), exactly \((q-3)/2\) yield square discriminant and \((q-1)/2\) nonsquare discriminant. Each square-discriminant \(\delta\) gives \(q(q+1)\) matrices for each of the \(q-1\) choices of \(h\), whereas each nonsquare discriminant gives \(q(q-1)\). Multiplication yields the first and third multiplicities in the table. This also establishes that the split case first appears at \(q=5\). All four counts sum to \(|\mathrm{GL}_2(\mathbb F_q)|\).

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 standard library. The verifier enumerates every invertible \(2\times2\) matrix over the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), computes the dependent-eigenvector count directly, and checks every listed stratum and its matrix count. For one representative of each nonempty stratum, it also directly enumerates all vector pairs to check the unilateral and bilateral fiber numerators. At \(q=3\), it exhaustively verifies involutivity and the Yang--Baxter identity on all triples of each representative brace. Its successful final line is \(\texttt{VERIFY_OK}\). The proof for arbitrary odd prime powers is the symbolic argument above; prime-field tests alone would not prove it.

## Relationship to prior work

Ferrara, Trombetti and Tsang (arXiv:2608.20620v1, 2026) introduced the four solution probabilities, proved universal probability bounds, and computed specific examples, including the alternating determinant brace over prime fields in Example 4.2. The alternating row in the table is therefore an extension of a **known example**, not the discovery of that probability. Bachiller (arXiv:1407.5224v1, 2014) classified all braces of prime-cube order up to isomorphism and parametrized a relevant class by bilinear-form congruence; no new brace-isomorphism classification is asserted here. Mondal and Yadav (arXiv:2603.16771v1, 2026) studied commuting probability of skew left braces with bounds related to annihilators. The new assertions assessed here are the *simultaneous two-sided/one-sided spectral formula for all nondegenerate bilinear radical braces*, and the *complete labeled four-stratum finite-field matrix distribution*, not the general brace construction, the probability definitions, or general bilinear-form congruence classification.

## Limitations

The four-row histogram is a labeled-matrix count, not an isomorphism-class count; counting congruence orbits with stabilizer weights is a different problem. The formulas hold for odd prime powers and invertible forms; degenerate forms, characteristic two, and higher-dimensional histogram multiplicities are not classified. Earlier classification literature may imply parts of the result through nontrivial specialization; the listed comparisons do not establish absolute historical priority. The Yang--Baxter identity is verified symbolically by the brace construction; exhaustive tests cover only the stated small prime fields. No independent external validation has been performed.

## References

1. M. Ferrara, M. Trombetti and C. S. Y. Tsang, *A probabilistic approach to the Yang--Baxter equation and skew braces*, arXiv:2608.20620v1 (first public 2026-08-20), especially Definitions 1.1--1.2, Proposition 3.1 and Example 4.2. https://arxiv.org/abs/2608.20620
2. D. Bachiller, *Classification of braces of order p³*, arXiv:1407.5224v1 (2014), especially Section 5.3 on bilinear-form parameters and congruence. https://arxiv.org/abs/1407.5224
3. S. Mondal and M. K. Yadav, *Commuting probability of skew left braces*, arXiv:2603.16771v1 (2026). https://arxiv.org/abs/2603.16771
