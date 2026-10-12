# The endomorphism rank spectrum of radical-square-zero cyclic Nakayama algebras

## Finding
For every field \(K\) and integer \(n\ge 2\), let \(Q_n\) be the directed cycle with vertices \(\mathbb Z/n\mathbb Z\), arrows \(a_j:j\to j+1\), and let \(A_n(K)=KQ_n/J^2\), where \(J\) is the arrow ideal. All unital \(K\)-algebra endomorphisms of \(A_n(K)\) have the unique normal form given below by a vertex map, one scalar for each edge on which that vertex map changes, and one scalar for each edge it sends to a forward edge. This is a classification of **all** endomorphisms, not only graded or automorphic ones.

For every prime power \(q\), write \(R_{n,q}(T)=\sum_F T^{\operatorname{rank}_{\mathbb F_q}F}\), the sum over unital \(\mathbb F_q\)-algebra endomorphisms of \(A_n(\mathbb F_q)\). For any function \(\phi:\mathbb Z/n\mathbb Z\to\mathbb Z/n\mathbb Z\), set
\[
 d(\phi)=\#\{j:\phi(j)\ne\phi(j+1)\},\qquad
 m_i(\phi)=\#\{j:\phi(j)=i,\ \phi(j+1)=i+1\}.
\]
Then the **complete labeled linear-rank distribution** is
\[
 \boxed{R_{n,q}(T)=\sum_{\phi}q^{d(\phi)}T^{|\operatorname{im}\phi|}
 \prod_{i\in\mathbb Z/n\mathbb Z}\bigl(1+(q^{m_i(\phi)}-1)T\bigr).}
\]
In particular, its sum of coefficients has the closed form
\[
 \boxed{E_{n,q}=\bigl(q^2+(n-2)q+1\bigr)^n
 +(q-1)^n\bigl[n(q^n+(-1)^n)-(q-1)^n\bigr].}
\]
There are exactly \(nq^n(q-1)^n\) automorphisms. For each fixed \(n\ge2\), the fraction of endomorphisms that are automorphisms is \(1-n/q+O_n(q^{-2})\) as \(q\to\infty\) through prime powers. Thus algebra endomorphisms of a fixed directed-cycle family are asymptotically almost surely invertible.

For \(n=3\) over \(\mathbb F_2\), the six-dimensional algebra has
\[
 R_{3,2}(T)=3T+72T^2+120T^3+72T^4+72T^5+24T^6,
\]
so there are exactly \(363\) unital endomorphisms and \(24\) automorphisms.

## Assumptions and scope
The field \(K\) is arbitrary, including characteristic two; the finite-field polynomial statement assumes \(q\) is a prime power. Vertex indices and additions of \(1\) in indices are taken modulo \(n\). The algebra has basis \(e_j,a_j\) for \(j\in\mathbb Z/n\mathbb Z\), and its complete nonzero basis products are \(e_ie_i=e_i\), \(e_ja_j=a_j\), and \(a_je_{j+1}=a_j\). In particular, \(J^2=0\) and \(A_n/J\cong K^n\). A map is called an endomorphism here only if it is \(K\)-linear, multiplicative, and preserves the unit \(\sum_j e_j\); its rank is its rank as a \(K\)-linear operator on the \(2n\)-dimensional algebra.

The **unique normal form** is as follows. Choose an arbitrary function \(\phi\) on the vertices. Define the orthogonal quotient idempotents
\[
 E_i=\sum_{\phi(j)=i}e_j.
\]
Choose \(s_j\in K\) for exactly the indices \(j\) with \(\phi(j)\ne\phi(j+1)\), and put \(s_j=0\) at every other index. Set \(u=1+\sum_j s_ja_j\), whose inverse is \(1-\sum_j s_ja_j\). Choose \(\beta_j\in K\) for exactly the indices \(j\) with \(\phi(j+1)=\phi(j)+1\). The corresponding endomorphism is
\[
 F(e_i)=uE_iu^{-1},\qquad
 F(a_i)=\sum_{\substack{j:\phi(j)=i\\\phi(j+1)=i+1}}\beta_j a_j.
\]
Every endomorphism is obtained exactly once in this way. In the rank formula, the exponent \(m_i(\phi)\) is the number of independently selectable coordinates in the image of the arrow \(a_i\).

## Proof
**Step 1: the semisimple vertex map.** Every arrow satisfies \(a_j^2=0\). Hence its image under a homomorphism is nilpotent, and therefore has zero image in the reduced quotient \(A_n/J\cong K^n\); so \(F(J)\subseteq J\). A unital \(K\)-algebra endomorphism of \(K^n\) is uniquely a pullback along a set map \(\phi\) on its \(n\) coordinates. Consequently \(F(e_i)\) reduces modulo \(J\) to \(E_i\) as defined above.

**Step 2: classify all orthogonal idempotent lifts.** Write \(F(e_i)=E_i+\sum_j c_{ij}a_j\). The identities \(F(e_i)^2=F(e_i)\), \(F(e_i)F(e_k)=0\) for \(i\ne k\), and \(\sum_iF(e_i)=1\) apply independently to each arrow coordinate because \(J^2=0\). At coordinate \(j\), if \(\phi(j)=\phi(j+1)\), all coefficients \(c_{ij}\) must be zero. Otherwise the only potentially nonzero coefficients are for \(i=\phi(j)\) and \(i=\phi(j+1)\), and these are negatives of each other. Thus there is a unique scalar \(s_j\) for each changed edge with
\[
 c_{ij}=s_j\bigl(\mathbf1_{\phi(j+1)=i}-\mathbf1_{\phi(j)=i}\bigr).
\]
These coefficients are exactly those of \(uE_iu^{-1}\), since \(u=1+s\) with \(s\in J\) and \(J^2=0\). This proves both existence and uniqueness of the specified lifts over every field.

**Step 3: the arrow images.** Because \(F(a_i)\in J\) and \(a_i=e_ia_ie_{i+1}\),
\[
 F(a_i)=F(e_i)F(a_i)F(e_{i+1})=E_iF(a_i)E_{i+1}.
\]
The space \(E_iJE_{i+1}\) has basis the arrows \(a_j\) satisfying \(\phi(j)=i\) and \(\phi(j+1)=i+1\). Choosing all the displayed \(\beta_j\) is therefore necessary and sufficient. Indeed, every defining relation between vertex idempotents and arrows then holds, while all arrow–arrow products vanish. Different \(\phi,s_j,\beta_j\) give different maps; the normal form is exhaustive.

**Step 4: ranks.** The induced map on \(A_n/J\) has rank \(|\operatorname{im}\phi|\). The image of \(J\) is the direct sum of the vectors \(F(a_i)\) having pairwise disjoint arrow supports. Thus \(\operatorname{rank}(F|_J)\) is the number of indices \(i\) for which the \(m_i(\phi)\)-coordinate vector defining \(F(a_i)\) is nonzero. For each \(i\), one choice gives zero and \(q^{m_i(\phi)}-1\) choices give a nonzero vector. Since \(F(A_n/J)\) injects into the quotient independently of \(F(J)\), the total rank is the sum of the two ranks. There are \(q^{d(\phi)}\) choices of lifting parameters \(s_j\). Multiplication of these independent factors proves the complete rank polynomial.

**Step 5: closed endomorphism count.** At \(T=1\), the contribution of \(\phi\) is \(q^{d(\phi)+\sum_i m_i(\phi)}\). Associate to a neighboring ordered pair \((i,j)\) the weight \(B_{ij}=1\) if \(j=i\), \(B_{ij}=q^2\) if \(j=i+1\), and \(B_{ij}=q\) otherwise. Then \(E_{n,q}=\operatorname{tr}(B^n)\). Writing \(P\) for the cyclic successor permutation matrix and \(\mathbf J\) for the all-ones matrix gives
\[
 B=q\mathbf J+(1-q)I+(q^2-q)P.
\]
On the constant vector its eigenvalue is \(q^2+(n-2)q+1\). On a nonconstant Fourier mode with \(P\)-eigenvalue \(\zeta\), its eigenvalue is \((q-1)(q\zeta-1)\). Using the complex \(n\)-th roots of unity only as a formal diagonalization device, the root-of-unity filter yields
\[
 \sum_{\zeta^n=1}(q\zeta-1)^n=n\bigl(q^n+(-1)^n\bigr),
\]
and subtracting the \(\zeta=1\) summand proves the boxed closed count. This polynomial identity gives integer counts and requires no root of unity in \(K\).

**Step 6: units of the endomorphism monoid and asymptotics.** An endomorphism is invertible exactly when \(\phi\) is a permutation and each arrow image is nonzero. The latter forces \(\phi\) to preserve the directed cycle, so \(\phi\) is one of the \(n\) rotations. Each rotation permits \(q^n\) lift parameters and \((q-1)^n\) nonzero arrow scalars; this proves the automorphism count. Expansion of the closed formula shows \(E_{n,q}=nq^{2n}+O_n(q^{2n-2})\); division by this expression proves the stated asymptotic automorphism density.

## Verification
Run `python checker.py` with Python 3 (only the standard library is required). The checker implements the multiplication in the algebra, enumerates **all** orthogonal idempotent lifts and possible arrow images independently of the parameter count for \((n,q)=(2,2),(2,3),(3,2)\), checks multiplication on every basis pair, and compares the resulting exact rank distributions to the normal-form polynomial. It separately compares the normal-form enumeration with the transfer-matrix trace and the closed expression at \((n,q)=(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)\). Its successful exit prints `VERIFY_OK`.

The direct enumeration verifies small instances and does **not** imply the arbitrary-field or all-rank theorem by itself. Those are established in the preceding proof.

## Relationship to prior work
The algebra is the radical-square-zero self-injective cyclic Nakayama algebra (an oriented-cycle bound quiver algebra). Chen (2011) describes singularity categories of radical-square-zero algebras and the distinguished role of oriented cycles. Sen (2018) studies homological \(\varphi\)-dimension for cyclic Nakayama algebras. Vaso (2021) characterizes radical-square-zero bound quiver algebras with higher cluster-tilting subcategories. Haugland, Jacobsen, and Schroll (2021) identify radical-square-zero Nakayama algebras in the classification of higher-homological gentle algebras. These results motivate the family and its structural significance, but concern module categories, homological invariants, and tilting structures; none states the explicit classification of unital algebra self-maps or its finite-field rank and cardinality distribution proved here. In particular, a module endomorphism ring is **not** the monoid of unital self-homomorphisms of the underlying algebra.

## Limitations
The formulas concern the specific Loewy-length-two cyclic Nakayama family and unital \(K\)-algebra maps; they do not enumerate nonunital, semilinear, or homomorphisms for longer Loewy lengths. The finite-field rank polynomial is an exact finite sum over \(n^n\) vertex functions, while the total count has a closed scalar expression. Broad bibliographic completeness under every possible terminology is not asserted. The verification program tests finite cases but is not an independent mathematical proof of the all-field result.

## References
- X.-W. Chen, *The Singularity Category of an Algebra with Radical Square Zero*, arXiv:1104.4006 (first public version 2011-04-20), https://arxiv.org/abs/1104.4006.
- E. Sen, *The \(\varphi\)-Dimension of Cyclic Nakayama Algebras*, arXiv:1806.01449 (first public version 2018-06-05), https://arxiv.org/abs/1806.01449.
- L. Vaso, *\(n\)-Cluster Tilting Subcategories for Radical Square Zero Algebras*, arXiv:2105.05830 (first public version 2021-05-12), https://arxiv.org/abs/2105.05830.
- J. Haugland, K. M. Jacobsen, and S. Schroll, *The Role of Gentle Algebras in Higher Homological Algebra*, arXiv:2107.01045 (first public version 2021-07-02), https://arxiv.org/abs/2107.01045.
