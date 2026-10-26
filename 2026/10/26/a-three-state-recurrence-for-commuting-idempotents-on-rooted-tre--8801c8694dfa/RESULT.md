# A three-state recurrence for commuting idempotents on rooted trees

## Finding
Let \(T\) be a finite rooted tree with root \(r\), with the ancestor order \(x\le y\) meaning that \(x\) lies on the root-to-\(y\) path. Let \(\mathcal C(T)\) be the monoid of order-preserving regressive maps \(f:V(T)\to V(T)\), so \(f(x)\le x\) for every vertex. Write \(c(T)\) for the number of ordered pairs of idempotents \((e,f)\in\mathcal C(T)^2\) satisfying \(ef=fe\).

For each vertex \(v\), with children \(w\), put
\[
P_s(v)=\prod_{w\text{ child of }v}F_w(s),\qquad s\in\{0,A,B\},
\]
where empty products equal \(1\), and define
\[
\begin{aligned}
F_v(0)&=2P_0(v)+P_A(v)+P_B(v),\\
F_v(A)&=P_0(v)+2P_A(v),\\
F_v(B)&=P_0(v)+2P_B(v).
\end{aligned}
\]
Then the exact number of ordered commuting idempotent pairs is
\[
\boxed{c(T)=\prod_{w\text{ child of }r}F_w(0).}
\]
The number of idempotents is \(2^{n-1}\), so the proportion of ordered idempotent pairs that commute is \(c(T)/4^{n-1}\). The recurrence takes \(O(n)\) integer-arithmetic operations on a tree with \(n\) vertices.

## Assumptions and scope
The tree is finite and rooted, and the order is ancestry. Composition is ordinary function composition. The counted pairs are ordered; the identity pair and pairs with equal entries are included. This is a statement about idempotents of the regressive order-preserving transformation monoid, not about all self-maps, maximal commuting families, arbitrary finite posets, or arbitrary rooted directed graphs.

## Proof
**Idempotent normal form.** For every subset \(S\subseteq V(T)\) containing \(r\), define \(e_S(x)\) to be the deepest ancestor of \(x\) that belongs to \(S\). This map is regressive and order-preserving, and every value is fixed, so \(e_S^2=e_S\). Conversely, if \(e\) is an idempotent in \(\mathcal C(T)\), its fixed set \(S\) contains \(r\). For every \(x\), the value \(e(x)\) is a fixed ancestor of \(x\). If \(s\in S\) is any ancestor of \(x\), monotonicity gives \(s=e(s)\le e(x)\). Hence \(e(x)\) is the deepest fixed ancestor of \(x\), and \(e=e_S\). Thus idempotents are in bijection with the \(2^{n-1}\) subsets containing \(r\).

**Path criterion.** Encode an ordered pair \((e_S,e_U)\) by labeling each vertex \(11\) if it belongs to both sets, \(10\) if it belongs only to \(S\), \(01\) if it belongs only to \(U\), and \(00\) if it belongs to neither. The root is labeled \(11\). On the root-to-\(x\) path, let \(a\) and \(b\) be the deepest vertices in \(S\) and \(U\), respectively. Then \(e_S e_U(x)\) is the deepest \(S\)-vertex at or above \(b\), and \(e_U e_S(x)\) is the deepest \(U\)-vertex at or above \(a\). These values differ exactly when \(a\) and \(b\) are distinct exclusive vertices with no common \(11\)-vertex between them. Equivalently, the pair commutes if and only if, on every root-to-vertex path, the labels \(10\) and \(01\) do not both occur after the most recent \(11\).

**Three-state count.** For a subtree rooted at \(v\), let \(F_v(s)\) count valid labelings when the path state inherited from the parent is \(s\). State \(0\) means that no exclusive label has occurred since the last \(11\); state \(A\) means that \(10\) has occurred but \(01\) has not; state \(B\) is the reverse. At \(v\), choosing \(11\) resets every child to state \(0\); choosing \(00\) preserves the inherited state; choosing \(10\) is allowed unless the inherited state is \(B\), and then passes state \(A\); choosing \(01\) is allowed unless the inherited state is \(A\), and then passes state \(B\). Child subtrees are independent conditional on this state. Summing these four choices gives exactly the displayed recurrence for \(F_v(0),F_v(A),F_v(B)\). Since the root must be \(11\), all child subtrees start in state \(0\), giving \(c(T)=\prod_{w\text{ child of }r}F_w(0)\).

**Checks and special cases.** For a star with \(k\) leaves, each leaf has \(F(0)=4\), so \(c(T)=4^k\), and every idempotent pair commutes. For a chain, symmetry gives \(F_m(A)=F_m(B)=b_m\) for a subtree of size \(m\), while \(a_m=F_m(0)\). The recurrence becomes \(a_m=2a_{m-1}+2b_{m-1}\), \(b_m=a_{m-1}+2b_{m-1}\), with \(a_0=b_0=1\). Eliminating \(b_m\) gives \(a_0=1\), \(a_1=4\), and \(a_m=4a_{m-1}-2a_{m-2}\) for \(m\ge2\). Thus the chain on \(n\) vertices has \(c(T)=a_{n-1}\); for three vertices this is \(14\) commuting ordered pairs out of \(16\) ordered idempotent pairs.

## Verification
The proof reduces the infinite family of possible rooted trees to a finite-state recurrence proved by a bijection between idempotent pairs and valid vertex labelings. The boundary checks are: a one-vertex tree has \(c(T)=1\); a two-vertex chain has \(c(T)=4\); a three-vertex chain has \(c(T)=14\); and a root with \(k\) leaves has \(c(T)=4^k\). No finite enumeration is used as evidence for the theorem. The recurrence does not assert a closed form for arbitrary tree shape.

## Relationship to prior work
Ganyushkin and Mazorchuk identify the Catalan monoid as the monoid of order-preserving and order-decreasing total transformations on a finite chain, giving the chain setting for this problem. The result here treats ancestry-ordered rooted trees and the ordered-pair commutativity count, an invariant not stated in the portions of that paper inspected. The chain recurrence is a specialization of the tree recurrence, not a claim that the Catalan monoid classification itself is new.

## Limitations
The result is limited to finite rooted-tree posets. It does not classify commuting pairs on arbitrary posets, count maximal commuting families, or provide asymptotics over families of tree shapes. The literature search was semantic and targeted rather than exhaustive; independent validation has not been performed.

## References
1. O. Ganyushkin and V. Mazorchuk, “On Kiselman quotients of 0-Hecke monoids,” arXiv:1006.0316v1, submitted 2010-06-02. https://arxiv.org/abs/1006.0316
