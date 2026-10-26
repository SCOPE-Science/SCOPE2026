# Four-level commutator fibers in the three-by-three upper triangular algebra

## Finding

Let \(q\) be any prime power, let \(F=\mathbb F_q\), and let \(T_3(F)\) be the six-dimensional associative \(F\)-algebra of upper triangular \(3\times3\) matrices. For \(s,t,h\in F\) set
\[
C(s,t,h)=\begin{pmatrix}0&s&h\\0&0&t\\0&0&0\end{pmatrix},\qquad
N_q(s,t,h)=|\{(A,B)\in T_3(F)^2:AB-BA=C(s,t,h)\}|.
\]
Then **every** commutator target occurs, and the entire fiber distribution is
\[
\boxed{
N_q(s,t,h)=q^5(q^2-1)^2+q^6(q^2-1)
\bigl(\mathbf1_{s=0}+\mathbf1_{t=0}\bigr)
+q^8\mathbf1_{s=t=h=0}.}
\]
In particular, the fibers take exactly four different sizes: 
\[
\begin{array}{c|c}
\text{target condition}&\text{number of ordered commutator representations}\\\hline
s\ne0,\ t\ne0&q^5(q^2-1)^2\\
\text{exactly one of }s,t\text{ is }0&q^5(q^2-1)^2+q^6(q^2-1)\\
s=t=0,\ h\ne0&q^5(q^2-1)^2+2q^6(q^2-1)\\
s=t=h=0&q^5(q^2-1)^2+2q^6(q^2-1)+q^8.
\end{array}
\]
The central coordinate \(h\) is uniformly distributed within every fiber of the projection to \((s,t)\ne(0,0)\); the only central-coordinate bias is the extra \(q^8\) representations at the zero matrix. The exact commuting-pair count is
\[
\boxed{N_q(0,0,0)=q^9+3q^8-2q^7-2q^6+q^5.}
\]

## Assumptions and scope

The field is arbitrary finite, including extension fields and characteristic two. Matrices \(A,B\) range over **all** upper triangular matrices, not just invertible ones. The operation is the additive associative-algebra commutator \([A,B]=AB-BA\), not the group commutator. The target coordinates are the entries \((1,2),(2,3),(1,3)\), respectively, so the radical \([T_3(F),T_3(F)]\) is identified with \(F^3\) in that order. The algebra has dimension six over \(F\), and its total number of ordered pairs is \(q^{12}\).

## Proof

Write arbitrary elements as
\[
A=\begin{pmatrix}a_1&x&u\\0&a_2&z\\0&0&a_3\end{pmatrix},\quad
B=\begin{pmatrix}b_1&y&v\\0&b_2&w\\0&0&b_3\end{pmatrix}.
\]
Define the diagonal differences \(\alpha=a_1-a_2\), \(\gamma=a_2-a_3\), \(\beta=b_1-b_2\), and \(\delta=b_2-b_3\). Direct multiplication gives
\[
[A,B]_{12}=\alpha y-\beta x,\quad
[A,B]_{23}=\gamma w-\delta z,\quad
[A,B]_{13}=(\alpha+\gamma)v-(\beta+\delta)u+xw-yz.
\]
For a nontrivial additive character \(\psi:F\to\mathbb C^\times\), and a dual target \(\ell=(r,k,l)\in F^3\), define
\[
\widehat N_q(\ell)=\sum_{A,B\in T_3(F)}
\psi\bigl(r[A,B]_{12}+k[A,B]_{23}+l[A,B]_{13}\bigr).
\]
In the ordered five coordinates \((\alpha,\gamma,x,z,u)\) for \(A\) and \((\beta,\delta,y,w,v)\) for \(B\), the bilinear pairing is represented by the alternating matrix
\[
M(r,k,l)=\begin{pmatrix}
0&0&r&0&l\\
0&0&0&k&l\\
-r&0&0&l&0\\
0&-k&-l&0&0\\
-l&-l&0&0&0
\end{pmatrix}.
\]
The two omitted diagonal coordinates \(a_3,b_3\) contribute freely. If \(l=0\), the two disjoint alternating blocks have ranks \(2\mathbf1_{r\ne0}\) and \(2\mathbf1_{k\ne0}\). If \(l\ne0\), the principal minor on indices \((1,3,4,5)\) has determinant \(l^4\), hence rank at least four. Since a \(5\times5\) alternating matrix has even rank at most four over **every** field (including characteristic two), the rank is exactly four. Thus
\[
\operatorname{rank}M(r,k,l)=
\begin{cases}
0,&r=k=l=0,\\
2,&l=0\text{ and exactly one of }r,k\text{ is nonzero},\\
4,&\text{otherwise}.
\end{cases}
\]
Now fix \(A\) and sum over \(B\). By the orthogonality of additive characters, this sum is \(q^6\) if the linear functional \(B\mapsto\ell([A,B])\) vanishes identically, and zero otherwise. The space of such \(A\) has dimension \(6-\operatorname{rank}M\), so
\[
\widehat N_q(r,k,l)=q^{12-\operatorname{rank}M(r,k,l)}.
\]
Equivalently, writing \(e_1,e_2\) for the two coordinate axes in the dual space,
\[
\widehat N_q(\ell)=q^8+
(q^{10}-q^8)\mathbf1_{\ell\in(e_1\cup e_2)\setminus\{0\}}+
(q^{12}-q^8)\mathbf1_{\ell=0}.
\]
Fourier inversion on \(F^3\), with \(\sum_{r\ne0}\psi(-rs)=q\mathbf1_{s=0}-1\), gives
\[
\begin{aligned}
N_q(s,t,h)=q^{-3}\bigl[&q^8q^3\mathbf1_{s=t=h=0}
+(q^{10}-q^8)(q\mathbf1_{s=0}+q\mathbf1_{t=0}-2)\\
&+(q^{12}-q^8)\bigr].
\end{aligned}
\]
The constant term simplifies to \(q^9-2q^7+q^5=q^5(q^2-1)^2\); the coefficient of each of the first two zero-coordinate indicators simplifies to \(q^6(q^2-1)\). This proves the boxed formula. Inverting a function defined on all of \(F^3\) also shows \(\sum_{s,t,h}N_q(s,t,h)=q^{12}\). All four values are strictly positive and distinct for every \(q\ge2\), so every target occurs and no additional fiber values exist.

## Verification

Run the included standalone script with `python3 verify.py`; its success sentinel is `VERIFY_OK_TRIANGULAR_COMMUTATOR_FIBERS`. It independently constructs upper triangular matrices and their **literal products**, then exhaustively enumerates all \(q^{12}\) ordered pairs for \(q=2,3\), comparing each target count with the formula. It separately computes all skew-pairing ranks over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\), and checks that the predicted counts sum to \(q^{12}\) for several field sizes. All calculations use the Python standard library; the \(\mathbb F_4\) multiplication is explicit. These finite computations support but do not replace the all-field rank-and-Fourier proof.

## Relationship to prior work

Britnell and Wildon (2010) investigate the existence of commuting representatives in similarity classes of full matrix algebras and describe centralizers by class type. Their Theorems 2.7–2.8 concern equivalences of full-matrix similarity-class centralizers and existence of commuting pairs, not fixed additive commutator fibers of an upper triangular subalgebra.

Goodwin and Röhrle (2012) study components of commuting varieties of the **nilradical** of a Borel Lie algebra, predominantly over algebraically closed characteristic-zero fields. Their Theorem 1.1 is geometric and concerns \([X,Y]=0\) with both variables in the nilradical. It neither determines finite-field fibers of nonzero commutators nor concerns all matrices in the full upper triangular algebra.

Kaur, Sharma and Singh (2020) determine branching matrices and commuting-tuple probabilities for **invertible triangular groups**, including the three-by-three group. Their Theorem 3.1 classifies conjugacy branching for invertible matrices rather than the additive algebra commutator distribution on all triangular matrices. Thus their group-theoretic result does not directly supply this full fiber formula.

The public result “Commutator fibers and commuting probabilities of finite Kronecker path algebras” concerns two-vertex parallel-arrow quivers whose radicals have square zero, and whose nonzero commutator fibers are all equal. Here there are three vertices and a surviving composable length-two path, and the fibers have four distinct values; the earlier result does not imply this one. The four-level formula should not be interpreted as a historical uniqueness claim: a coadjoint-rank table or an unpublished equivalent formulation could contain it.

## Limitations

This is an exact complete statement for \(T_3(\mathbb F_q)\). It does not count group commutators or constrain matrices to be invertible, and it does not describe fibers for larger triangular sizes. The proof does not establish a general phenomenon for all Borel algebras. No independent audit or exhaustive historical priority certification is claimed.

## References

1. J. R. Britnell and M. Wildon, “On types and classes of commuting matrices over finite fields,” arXiv:1001.0811v1 (first public 6 January 2010), later *J. London Math. Soc.* 83 (2011), 470–492. https://arxiv.org/abs/1001.0811
2. S. M. Goodwin and G. Röhrle, “On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras,” arXiv:1209.1289v1 (first public 6 September 2012), later *Proc. Edinburgh Math. Soc.* 58 (2015), 169–181. https://arxiv.org/abs/1209.1289
3. D. Kaur, U. B. Sharma and A. Singh, “Branching rules and commuting probabilities for triangular and unitriangular matrices,” arXiv:2006.01493v1 (first public 2 June 2020). https://arxiv.org/abs/2006.01493
4. “Commutator fibers and commuting probabilities of finite Kronecker path algebras,” public research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d
