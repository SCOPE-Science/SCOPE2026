# Fourier-diagonal derivations and sixth-root resonances in finite Latin Alexander quandle algebras

## Finding
Let \(A\) be any finite abelian group, \(\varphi\in\operatorname{Aut}(A)\) such that \(1-\varphi\) is also invertible, and \(K\) any field with characteristic not dividing \(|A|\). Form the Alexander quandle algebra \(E_K(A,\varphi)\) with basis \(e_a\) and multiplication \(e_a e_b=e_{\varphi(a)+(1-\varphi)(b)}\). After extending scalars to an algebraic closure \(L\) of \(K\), every derivation is **diagonal in the Fourier basis**
\[
 b_\chi=\frac1{|A|}\sum_{a\in A}\chi(a)e_a,
 \qquad\chi\in\widehat A=\operatorname{Hom}(A,L^\times).
\]
More exactly, its derivations are precisely \(D(b_\chi)=d_\chi b_\chi\) satisfying
\[
\boxed{d_\chi=d_{\chi\circ\varphi}+d_{\chi\circ(1-\varphi)}\quad\text{for every }\chi\in\widehat A.}
\]
Therefore the Lie algebra of derivations is abelian over **every** such base field \(K\), not only over the splitting field. Its scalar-extended dimension is the nullity of the displayed finite character-indexed linear system, which can be computed without generating the full quadratic Leibniz equations.

For \(A=\mathbb Z/p\mathbb Z\), \(p\) an odd prime, over \(\mathbb C\), and \(\varphi(a)=ta\) with \(t\in\mathbb F_p\setminus\{0,1\}\), the exact dimension is
\[
\boxed{\dim_{\mathbb C}\operatorname{Der}(E_{p,t})=
\#\{\eta\in\widehat{\mathbb F_p^\times}:\eta(t)+\eta(1-t)=1\}.}
\]
It vanishes unless \(6\mid(p-1)\). If \(p>3\) and \(t^2-t+1=0\) in \(\mathbb F_p\), its value is exactly \((p-1)/3\). The first prime-order Latin Alexander quandles with nonzero complex derivations occur at \(p=7\), \(t=3,5\), when the dimension is \(2\); at \(p=13\), \(t=4,10\), it is \(4\).

## Assumptions and scope
A derivation is an additive \(K\)-linear map \(D:E\to E\) satisfying \(D(xy)=D(x)y+xD(y)\) for all \(x,y\in E\), with no assumption of associativity or commutativity. All groups \(A\) are finite and abelian, and \(\varphi\), \(1-\varphi\) are automorphisms (the Latin condition). The base-field characteristic need only be coprime to \(|A|\); the prime-cyclic multiplicative-character formula is stated over \(\mathbb C\). Here \(\widehat A\) is the full \(L\)-valued character group, of size \(|A|\). The general theorem concerns *all* derivations of the stated algebras, not merely Fourier-preserving derivations.

## Proof
**1. Fourier product.** Character orthogonality is valid because \(|A|\) is invertible in \(K\), and all characters take values in \(L\). Define permutations of \(\widehat A\)
\[
\tau(\chi)=\chi\circ\varphi^{-1},\qquad
\sigma(\chi)=\chi\circ\varphi^{-1}(1-\varphi).
\]
Substituting the quandle product into the Fourier sums, changing variables \(c=\varphi(a)+(1-\varphi)(b)\), and summing a character over \(A\) gives
\[
b_\chi b_\psi=
\begin{cases}
 b_{\tau(\chi)},&\psi=\sigma(\chi),\\
 0,&\psi\ne\sigma(\chi).
\end{cases}
\tag{1}
\]
To check normalization, in the nonzero case the coefficient at each \(e_c\) is \(\chi(\varphi^{-1}c)/|A|\), precisely the coefficient in \(b_{\tau(\chi)}\). Both \(\tau\) and \(\sigma\) are permutations, since \(\varphi\) and \(1-\varphi\) are automorphisms.

**2. All off-diagonal derivation coefficients vanish.** Write an arbitrary \(L\)-linear derivation as \(D(b_i)=\sum_k d_{k,i}b_k\), where \(i,j,k\) label characters. Whenever \(j\ne\sigma(i)\), the zero-product Leibniz equation and (1) give
\[
0=D(b_i)b_j+b_iD(b_j)
=d_{\sigma^{-1}(j),i}b_{\tau\sigma^{-1}(j)}
+d_{\sigma(i),j}b_{\tau(i)}.
\tag{2}
\]
The two displayed basis vectors are **distinct**: their equality would imply \(\sigma^{-1}(j)=i\), contradicting \(j\ne\sigma(i)\). Thus both coefficients vanish. For any \(k\ne i\), choose \(j=\sigma(k)\) to obtain \(d_{k,i}=0\). Consequently every derivation is diagonal in the Fourier basis.

**3. Diagonal equations and converse.** With \(D(b_i)=d_i b_i\), applying the Leibniz identity to the unique nonzero product \(b_i b_{\sigma(i)}=b_{\tau(i)}\) gives
\[
d_{\tau(i)}=d_i+d_{\sigma(i)}.\tag{3}
\]
Conversely (3) guarantees Leibniz for all nonzero products, while all zero products satisfy Leibniz automatically because a diagonal map preserves their zero value. Put \(i=\chi\circ\varphi\). Then \(\tau(i)=\chi\) and \(\sigma(i)=\chi\circ(1-\varphi)\), giving the claimed system. Since diagonal operators commute, all derivations over \(L\) commute. For \(K\), scalar extension is faithful, so the commutator of any two \(K\)-derivations is zero as well. The same equations show the Lie algebra is a finite-dimensional kernel after splitting, with no claim that all individually diagonal Fourier maps descend to \(K\).

**4. Prime cyclic formula.** Index the additive characters of \(\mathbb F_p\) by \(j\in\mathbb F_p\). The diagonal equations are
\[
d(0)=0,\qquad d(j)=d(tj)+d((1-t)j)
\quad(j\in\mathbb F_p^\times).\tag{4}
\]
The multiplicative characters \(\eta:\mathbb F_p^\times\to\mathbb C^\times\) form a basis for functions on \(\mathbb F_p^\times\). Substituting \(d(j)=\eta(j)\) into (4) yields the eigenvalue equation \(1=\eta(t)+\eta(1-t)\); counting its zero eigenvalues proves the dimension formula.

The values \(u=\eta(t)\) and \(v=\eta(1-t)\) are roots of unity, so both lie on the unit circle. If \(u+v=1\), then \(|1-u|=1\), giving \(\Re(u)=1/2\) and
\[
\{u,v\}=\{e^{\pi i/3},e^{-\pi i/3}\}.\tag{5}
\]
Thus a sixth-order multiplicative character must exist, requiring \(6\mid(p-1)\). Equivalently, for a primitive root \(g\) of \(\mathbb F_p^\times\), writing \(t=g^a\), \(1-t=g^b\), and \(n=p-1\), the dimension is the number of \(0\le k<n\) for which
\[
(ka,kb)\equiv(n/6,5n/6)\quad\text{or}\quad(5n/6,n/6)\pmod n.
\tag{6}
\]
If \(t^2-t+1=0\) and \(p>3\), then \(1-t=t^{-1}\) and \(t\) has order exactly six. The restriction map from multiplicative characters of \(\mathbb F_p^\times\) to those of its order-six subgroup is onto; exactly \(2(p-1)/6=(p-1)/3\) characters take \(t\) to either primitive sixth root. This proves the stated formula and the examples. At \(p=3,5\), (5) forces dimension zero. At \(p=7\), the two roots of \(t^2-t+1\) are \(3,5\); direct application of (6) eliminates the other three admissible parameters. At \(p=13\), the two roots are \(4,10\).

## Verification
The standalone standard-library script `verify.py` independently builds the full \(p^2\)-variable Leibniz linear system from (1), checks its rank modulo \(1009\) against the \(p\)-variable diagonal system for all admissible \(t\) at \(p=3,5,7\), and compares the diagonal nullities with the exact discrete-log character formula for selected parameters at \(p=11,13\). It prints `VERIFY_OK cases= 15`. Modular finite checks corroborate—but do **not** replace—the characteristic-free algebraic proof over the prescribed base fields or provide exhaustive checks at arbitrary prime order.

## Relationship to prior work
Elhamdadi, Makhlouf, Silvestrov and Zappala developed general derivation equations for quandle algebras and, in particular, proved zero derivations for odd dihedral quandle algebras in characteristic zero. Our result agrees with the dihedral parameter \(t=-1\) and goes beyond it: non-dihedral Latin Alexander quandles can have positive-dimensional derivation Lie algebras, even though these Lie algebras are necessarily abelian. Existing exact square-zero subspace, Boolean ideal-lattice, and finite-field commuting-pair classifications concern other invariants of Latin Alexander quandle algebras; none of their recorded statements classifies derivations. Another finite-field idempotent count features a formally similar power-sum resonance condition in coefficient characteristic dividing the quandle order, but it neither concerns derivations nor supplies the present complex character decomposition. The Fourier multiplication approach builds on prior Fourier analysis of Alexander quandle algebras, including Zhang's October 2026 paper, rather than claiming that the Fourier product itself is new. The contribution is the **global diagonalization of every derivation**, its complete linear-character constraint, and the sixth-root arithmetic classification in prime order.

## Limitations
The Latin hypothesis and invertibility of \(|A|\) are essential to the proof: when \(1-\varphi\) is singular, \(\sigma\) need not permute the character basis, and when the coefficient characteristic divides \(|A|\), the Fourier decomposition can fail. The multiplicative-character count is only asserted over \(\mathbb C\), although the full diagonal theorem holds in the stated wider characteristic range. The source inspection was incomplete for an independently relevant September 2026 Fourier/idempotents preprint; its abstract describes idempotents, not derivations, but unforeseen overlap cannot be categorically excluded. The outcome is a theoretical derivation classification, not an independently audited publication or priority certificate.

## References
1. M. Elhamdadi, A. Makhlouf, S. Silvestrov and E. Zappala, *The derivation problem for quandle algebras*, arXiv:2106.08289 (first posted 2021-06-15), particularly Section 3. https://arxiv.org/abs/2106.08289 .
2. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first posted 2026-10-06), especially the Fourier multiplication description. https://arxiv.org/abs/2610.08204 .
3. M. Elhamdadi, L. Ta and M. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026-09; abstract inspected). https://arxiv.org/abs/2609.03799 .
4. A. Sangare and L. Ta, *Idempotents, automorphism groups and commutator widths of quandle algebras*, arXiv:2608.01550 (2026-08; abstract inspected). https://arxiv.org/abs/2608.01550 .
