# Upper-bound epigraphs and monotone-supremum completeness for operator-gauge cones

## Finding

**Theorem (complete upper-bound profile).** Let \(X\) and \(Y\) be real Banach spaces, and let \(T:X\to Y\) be bounded and injective. Set \(Z=\mathbb R\oplus_1 X\) and order it by the operator-gauge cone
\[
C_T=\{(t,x)\in Z:t\geq\|Tx\|_Y\}.
\]
For every increasing net \((z_i)=(t_i,x_i)\) in \(Z\) that has an order upper bound, the limits
\[
s=\lim_i t_i\in\mathbb R,\qquad y=\lim_i Tx_i\in\overline{T(X)}
\]
exist, with the second limit in the norm of \(Y\). The **entire** upper-bound set is the epigraph
\[
\operatorname{UB}((z_i))=\big\{(u,w)\in Z:u\geq s+\|Tw-y\|_Y\big\}.
\]
Moreover, \((z_i)\) has a least upper bound in \(Z\) if and only if \(y\in T(X)\). In that case its supremum is \((s,T^{-1}y)\). Consequently, the following three assertions are equivalent:

1. \(T(X)\) is norm closed in \(Y\).
2. Every increasing order-bounded **sequence** in \(Z\) has a supremum.
3. Every increasing order-bounded **net** in \(Z\) has a supremum.

Here ``order bounded'' means bounded from above and below. For general directed nets, an upper bound need not supply a common lower bound; the epigraph and leastness claims require only an upper bound. The equivalence of the three assertions also holds when the sequence/net assertions require only an upper bound.

## Assumptions and scope

All spaces and cones are real. The direct sum carries \(\|(t,x)\|_Z=|t|+\|x\|_X\). The cone is closed by continuity of \(T\), pointed by injectivity, and generating since \((1,0)\) is an interior point: for \(\varepsilon>0\) sufficiently small, \(\|(t,x)-(1,0)\|_Z<\varepsilon\) implies \(t>\|Tx\|\). No reflexivity, order normality, separability, surjectivity, or lattice structure is assumed. Limits of nets use the directed-set meaning and convergence in the indicated norms.

## Proof

**Step 1: scalar and image convergence.** For \(i\leq j\), monotonicity reads
\[
0\le t_j-t_i,\qquad\|Tx_j-Tx_i\|_Y\le t_j-t_i.
\]
An upper bound \((b,v)\) forces \(t_i\le b\). Hence the increasing real net \((t_i)\) converges to its finite supremum \(s\). For \(j,k\ge i\), the triangle inequality gives
\[
\|Tx_j-Tx_k\|_Y\le(t_j-t_i)+(t_k-t_i)\le2(s-t_i).
\]
Thus \((Tx_i)\) is Cauchy and converges to some \(y\in\overline{T(X)}\), because \(Y\) is complete. Passing \(j\) to the limit also gives
\[
\|y-Tx_i\|_Y\le s-t_i\quad\text{for every }i.
\]

**Step 2: every upper bound, exactly.** For any candidate \((u,w)\), being above every \(z_i\) means \(u-t_i\ge\|Tw-Tx_i\|_Y\) for all \(i\). Letting \(i\) tend to infinity proves necessity of \(u\ge s+\|Tw-y\|_Y\). Conversely that inequality and Step 1 imply, for every \(i\),
\[
u-t_i\ge\|Tw-y\|_Y+(s-t_i)\ge\|Tw-y\|_Y+\|y-Tx_i\|_Y\ge\|Tw-Tx_i\|_Y,
\]
so the profile is exact. It also explicitly proves the upper-bound set is nonempty.

**Step 3: detect leastness rather than mere minimality.** If \(y=Tx_*\), the point \((s,x_*)\) is an upper bound by Step 2, and every upper bound \((u,w)\) lies above it, because \(u-s\ge\|T(w-x_*)\|_Y\). Hence it is the supremum.

Conversely assume \((u,w)\) is a supremum. For every index \(i\), the point
\[
q_i=(s+\|Tx_i-y\|_Y,x_i)
\]
is an upper bound by Step 2. Since the supremum lies below \(q_i\),
\[
u+\|T(x_i-w)\|_Y\le s+\|Tx_i-y\|_Y.
\]
Taking the limit yields \(u+\|y-Tw\|_Y\le s\). But the supremum itself is an upper bound, so Step 2 gives \(u\ge s+\|Tw-y\|_Y\). These two inequalities force \(Tw=y\). This argument rules out **any** least upper bound when \(y\notin T(X)\), even though there may be multiple minimal upper bounds.

**Step 4: all sequences and nets.** If \(T(X)\) is closed, every image limit in Step 1 belongs to \(T(X)\), giving a supremum for every net. Conversely, if \(T(X)\) is not closed, take \(y\in\overline{T(X)}\setminus T(X)\) and choose \(x_n\in X\) with \(\|Tx_n-y\|_Y\le2^{-n}\). Let
\[
t_1=0,\qquad t_n=\sum_{k=1}^{n-1}\|T(x_{k+1}-x_k)\|_Y\quad(n\ge2).
\]
The sum of increments is finite since \(\|T(x_{k+1}-x_k)\|_Y\le 2^{-k}+2^{-(k+1)}\). Therefore \((t_n,x_n)\) increases in the cone order and \(s=\lim_nt_n<\infty\), while \(Tx_n\to y\). The bound \(s-t_n\ge\|y-Tx_n\|_Y\) follows by telescoping, and hence \((s+\|y\|_Y,0)\) is above the entire sequence. Step 3 shows it has no supremum. This proves the contraposition of the remaining implication.

**Concrete diagonal witness.** On \(X=Y=\ell_1(\mathbb N;\mathbb R)\), put \((Ta)_k=2^{-k}a_k\). Define
\[
x_n=\sum_{k=1}^n e_k,\qquad t_n=\sum_{k=1}^n2^{-k}=1-2^{-n}.
\]
The increments satisfy \((t_{n+1}-t_n,x_{n+1}-x_n)=(2^{-(n+1)},e_{n+1})\in C_T\), and \((2,0)\) is an upper bound. Here \(s=1\) and \(y=(2^{-k})_{k\ge1}\in\ell_1\), but \(y\notin T(\ell_1)\), since its unique coordinatewise preimage is the nonsummable constant-one sequence. Thus the increasing order-bounded sequence has no supremum. More precisely, its upper bounds are **exactly**
\[
\bigg\{(u,w)\in\mathbb R\oplus_1\ell_1:\ u\ge1+\sum_{k=1}^{\infty}2^{-k}|w_k-1|\bigg\}.
\]

## Verification

The general formula is derived directly from two cone-order inequalities and completeness of \(Y\); no finite experiment is used to assert an infinite-dimensional result. The proof independently checks the converse (every upper bound satisfies the formula), the possible gap between minimal and least upper bounds, arbitrary directed nets, and construction of an actual order-bounded sequence for each nonclosed range. In the concrete diagonal example, \(\sum_{k\ge1}2^{-k}=1\), \(t_n\nearrow1\), and \(2-t_n\ge t_n\), which verifies the exhibited upper bound \((2,0)\). The nonclosedness witness is the image limit \((2^{-k})\) with no \(\ell_1\) preimage.

## Relationship to prior work

Glück's study of increasing sequences in ordered Banach spaces (arXiv:2409.19768v1, Section 3 and Open Problem 3.2) asks for a global relation between existence of monotone suprema and normality. Its general theorem assumes normality and separability. The present result computes all upper bounds and the exact supremum obstruction for **operator-gauge cones**, a restricted but concrete family; it does not answer the unrestricted open problem. Messerschmidt's treatment of quasi-lattices and cone normality (arXiv:1307.1415v2) concerns pairwise quasi-suprema and normality, not this order-bounded-net epigraph. A related closed-range criterion for weak-to-norm monotone convergence does not itself identify which individual increasing nets have least upper bounds, nor their upper-bound sets. No independence or priority claim beyond these inspected comparisons is asserted.

## Limitations

The result concerns injective bounded linear operators and their associated real operator-gauge cones. It does not classify arbitrary closed generating cones, noninjective operator gauges as partial orders, or Banach lattices. It is possible for the scalar coordinates and images \(Tx_i\) to converge while \(x_i\) does not converge in \(X\), and such strong convergence is **not** asserted. Unindexed treatments of Lorentz-type orders may already contain equivalent epigraph observations; independent literature audit has not been performed.

## References

1. J. Glück, *Increasing sequences in ordered Banach spaces – new theorems and open problems*, arXiv:2409.19768v1, first public 29 September 2024, https://arxiv.org/html/2409.19768v1 (Sections 1–3, including Open Problem 3.2).
2. M. Messerschmidt, *Normality of spaces of operators and quasi-lattices*, arXiv:1307.1415v2, https://arxiv.org/html/1307.1415v2 (pairwise quasi-suprema and normality).
