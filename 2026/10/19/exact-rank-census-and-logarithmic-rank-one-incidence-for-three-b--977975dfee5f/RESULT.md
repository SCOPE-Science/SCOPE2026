# Exact rank census and logarithmic rank-one incidence for three-by-three prime-power Fourier minors

## Finding
Let \(p\) be any prime, \(k\ge 2\), \(N=p^k\), and \(F_N=(e^{2\pi i rc/N})_{r,c\in\mathbb Z_N}\). Choose any three distinct rows \(R\) and three distinct columns \(C\). For a triple \(R\), put
\[
t_R=\min_{r\ne r'\in R} v_p(r-r'),\qquad s_R=\max_{r\ne r'\in R}v_p(r-r'),
\]
where differences are nonzero modulo \(N\) and the valuations lie in \(\{0,\dots,k-1\}\). Define \(t_C,s_C\) analogously. The exact rank is
\[
\operatorname{rank}F_N[R,C]=
\begin{cases}
1,&t_R+t_C\ge k,\\
2,&t_R+t_C<k\text{ and }(s_R+t_C\ge k\text{ or }s_C+t_R\ge k),\\
3,&s_R+t_C<k\text{ and }s_C+t_R<k.
\end{cases}
\]

The more substantial new census is as follows. Fix \(R\), write \(t=t_R\), \(s=s_R\), and set
\[
L(v)=p^{k-v}\binom{p^v}{3},\qquad T=\binom N3.
\]
Among all \(T\) unordered column triples, the **exact** counts of ranks one, two, three are, respectively,
\[
\boxed{B_1(t,s)=L(t),\quad
B_2(t,s)=L(s)-L(t)+p^{k-t}\binom{p^t}{2}(N-p^s),\quad
B_3(t,s)=T-B_1(t,s)-B_2(t,s).}
\]
All these counts are nonnegative integers. The formula applies to every prime, including \(p=2\), and at every depth \(k\ge2\).

For a **complete global rank census**, let
\[
E_t=p^t\binom p3p^{3(k-t-1)},\qquad
I_{t,s}=\frac N2(p^{k-s}-p^{k-s-1})(p^{k-t}-p^{k-t-1})\quad(0\le t<s<k).
\]
Here \(E_t\) is the number of row triples of type \((t,t)\), and \(I_{t,s}\) the number of type \((t,s)\). The exact number of ordered pairs of unordered triples \((R,C)\) giving rank \(j\in\{1,2,3\}\) is
\[
\boxed{\mathcal R_j=\sum_{t=0}^{k-1}E_tB_j(t,t)
+\sum_{0\le t<s<k}I_{t,s}B_j(t,s).}
\]
In particular the rank-one count simplifies to the elementary closed form
\[
\boxed{\mathcal R_1=\frac{N^2}{36}\left[\bigl(N^2(1-p^{-2})+9N(1-p^{-1})\bigr)k-(1+6/p)N^2+(-3+6/p)N+4\right].}
\]
Consequently, with \(p\) fixed and \(k\to\infty\),
\[
\boxed{\frac{N^2\mathcal R_1}{\binom N3^2}=(1-p^{-2})k-1-6/p+O_p(k/N).}
\]
Thus the probability of rank one among uniformly sampled three-by-three Fourier minors has a logarithmic-in-\(N\) enhancement over a fixed multiple of \(N^{-2}\).

## Assumptions and scope
All ranks are over \(\mathbb C\), and both index triples consist of distinct residues in the cyclic group \(\mathbb Z/p^k\mathbb Z\). Multiplying Fourier rows or columns by nonzero constants does not alter rank. A valuation \(v_p(d)\) for a difference of distinct residues is the largest \(v<k\) such that \(p^v\) divides an integer lift of \(d\). The outer count \(\mathcal R_j\) treats row and column triples as a distinguished ordered pair, while each triple is an unordered subset. Empty binomial coefficients (for example \(\binom{1}{3}\)) are zero. The rank-one asymptotic is at fixed prime \(p\), not uniform in \(p\).

## Proof
**1. Previously known three-by-three phase rigidity.** A known elementary lemma for unit-modulus matrices states that a singular three-by-three matrix with all entries on the unit circle must have two proportional rows or two proportional columns. For completeness, normalize the first row and column to ones to obtain rows \((1,1,1),(1,u,v),(1,w,z)\). Vanishing of the determinant is \((u-1)(z-1)=(v-1)(w-1)\). If a factor vanishes, inspection gives repeated rows or columns. Otherwise conjugate, use \(\overline{u-1}=-(u-1)/u\), and divide: \(uz=vw\). Expanding the original equality gives \(u+z=v+w\). Two pairs with identical sum and product coincide as multisets, and again a row or column repeats. This lemma is an established ingredient, not the novelty of the census.

For the Fourier matrix, two selected rows are proportional exactly when some row difference has valuation at least \(k-t_C\), hence when \(s_R+t_C\ge k\). The transposed condition is \(s_C+t_R\ge k\). Every entry in the normalized minor is one exactly when every row difference times every column difference vanishes modulo \(N\); this is equivalent to \(t_R+t_C\ge k\) and to rank one. The phase lemma then gives rank two versus three, proving the rank criterion without an unverified cyclotomic assumption.

**2. Count columns for fixed rows.** Call two columns equivalent when their normalized restrictions to \(R\) coincide. There are \(p^{k-t}\) fine equivalence classes of size \(q=p^t\), because equivalence is congruence modulo \(p^{k-t}\). All three columns in one fine class give rank one, giving \(L(t)\) choices. Exactly two in one fine class and the third elsewhere give \(p^{k-t}\binom q2(N-q)\) choices.

A pair of selected Fourier rows becomes proportional when all three columns lie in one coarse congruence class modulo \(p^{k-s}\), yielding \(L(s)\) triples, of which \(L(t)\) are rank one. The overlap between coarse-triple rank two and fine-pair rank two consists of \(p^{k-t}\binom q2(p^s-q)\) choices: two columns in a fine class and a third in its coarse class but outside its fine class. Subtracting this overlap gives \(B_2(t,s)\); subtracting both nonfull-rank counts from \(T\) gives \(B_3\). This also handles \(s=t\), including the dyadic case.

**3. Count row types.** The nonarchimedean triangle law makes the three pair valuations either all equal to \(t\), or exactly two equal to \(t\) and the third strictly larger \(s\). In the first case choose one residue class modulo \(p^t\), three distinct child classes modulo \(p^{t+1}\), and one point from each: \(E_t=p^t\binom p3p^{3(k-t-1)}\). In the second case the close pair is unique: select its unordered endpoints at exact distance valuation \(s\), in \(\tfrac N2(p^{k-s}-p^{k-s-1})\) ways, then select the third point at exact distance valuation \(t\), in \(p^{k-t}-p^{k-t-1}\) ways. This is \(I_{t,s}\), with no double counting. Summing their products with the fixed-row counts proves all three global census formulas. In particular \(\sum E_t+\sum I_{t,s}=\binom N3\).

**4. Rank-one closed form and asymptotic.** The number of triples whose pair-difference valuations are all at least \(v\) is
\[
Q_v=p^v\binom{p^{k-v}}3=\frac N6(N^2p^{-2v}-3Np^{-v}+2).
\]
Thus \(\mathcal R_1=\sum_{v=0}^{k-1}(Q_v-Q_{v+1})Q_{k-v}\). Substituting the explicit expression for \(Q_v\) and evaluating the three finite geometric sums \(\sum p^{v}\), \(\sum p^{-v}\), and \(\sum p^{-2v}\) yields the stated rank-one closed form. Finally \(\binom N3^2=N^6(1+O(N^{-1}))/36\), and division gives the displayed asymptotic, since \(N=p^k\).

## Verification
The standalone file `checker.py` uses exact cyclotomic integer arithmetic for determinant vanishing (the coefficients in each residue fiber must be equal modulo \(\Phi_{p^k}\)), and exact congruence arithmetic to distinguish ranks one and two. It exhaustively checks every ordered pair of unordered triples at \((p,k)=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\), including every fixed-row count and every global count. The respective \((\mathcal R_1,\mathcal R_2,\mathcal R_3)\) are
\[
(0,0,16),\ (0,320,2816),\ (256,26624,286720),\ (9,324,6723),\ (4455,323676,8227494),\ (2500,100000,5187500).
\]
It also checks 9000 seeded, exactly evaluated pairs at each of \((3,4),(5,3),(7,2),(2,6)\). The successful final marker is `VERIFY_OK`. The analytic argument, rather than finite sampling, establishes the unrestricted conclusion.

## Relationship to prior work
Alexeev, Cahill and Mixon (2011/2012), Theorem 9, characterize which entire row-selected Fourier frames are full spark for prime-power orders. This determines neither the number nor the ranks of singular individual minors for a non-full-spark row set. A published prime-square calculation gives the three-by-three rank census at depth two; the formulas here agree in that case but cover all deeper prime powers and also the binary case. A published prime-affine-plane result explicitly contains the general unit-modulus three-by-three rigidity lemma used above; that lemma and the corresponding easy valuation rank criterion are acknowledged as prior information. The new assertion is the **exact per-row, all-depth rank census**, its global closed combinatorial multiplicities, and the logarithmic rank-one incidence law. Results on maximal rank-deficient blocks of Kronecker Fourier matrices motivate this problem but do not, from the available material, establish this local all-depth census.

## Limitations
The result counts ranks, not determinants' magnitudes or smallest nonzero singular values; nor does it classify four-by-four minors. The phase rigidity lemma is not new. At \(k=2\) the odd-prime rank counts specialize to an existing result. The precise all-depth census and the logarithmic rank-one law were not found in the searched sources; prior independent work under different terminology may exist. A relevant 2006 Fourier-block report was available only through its abstract during comparison. The mathematical review is not an independent certification of priority.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548v1 (first public 2011-10-17); Theorem 9 in v2, https://arxiv.org/html/1110.3548v2.
2. S. Delvaux, M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Technical Report TW477 (2006), later *Linear Algebra and its Applications* 426 (2007), 349–367.
3. *All singular three-by-three minors of prime-square Fourier matrices*, publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b.
4. *Complete three-by-three Fourier-minor rank geometry on prime affine planes*, publicly accessible result (contains unit-modulus rigidity lemma), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-three-by-three-fourier-minor-rank-geometry-on-prime-aff--ba0b52ec4cec.
