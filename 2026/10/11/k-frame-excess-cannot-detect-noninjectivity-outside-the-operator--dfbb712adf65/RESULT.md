# K-frame excess cannot detect noninjectivity outside the operator range

## Finding
Corollary 5.11 of Agheshteh Moghaddam--Arefijamaal states that, under its commutation and invariance hypotheses, equality of three excesses is equivalent to injectivity of the ambient operator. The implication from excess equality to global injectivity is false.

Let
\[
H=M\oplus N,
\qquad
M=\operatorname{span}\{e_0\},
\qquad
N=\ell^2(\mathbb N),
\]
and let
\[
K=P_M.
\]
On \(N\), choose the unilateral backward shift
\[
Bf_1=0,
\qquad
Bf_{n+1}=f_n
\quad(n\ge1),
\]
and set
\[
U=I_M\oplus B.
\]
The operator \(U\) is onto: for
\[
a e_0\oplus\sum_{n\ge1}b_nf_n
\]
one preimage is
\[
a e_0\oplus\sum_{n\ge1}b_nf_{n+1}.
\]
It is not injective because
\[
Uf_1=0.
\]
Moreover,
\[
UK=KU,
\]
and
\[
R(K)^\perp=N
\]
is invariant under \(U\).

Take the singleton sequence
\[
\Phi=\{e_0\}.
\]
For every \(x\in H\),
\[
|\langle x,e_0\rangle|^2
=
\|K^*x\|^2,
\]
so \(\Phi\) is a Parseval \(K\)-frame. Removing its only element leaves no \(K\)-frame, hence
\[
E_K(\Phi)=0.
\]
All atoms of \(\Phi\) already lie in
\[
R(K)=M.
\]
Since \(Ue_0=e_0\),
\[
U\Phi=\Phi
\]
and
\[
UP_M\Phi=\Phi.
\]
The projected singleton is an ordinary Parseval frame for \(M\), also with excess \(0\). Consequently
\[
E_K(\Phi)
=
E(UP_M\Phi)
=
E_K(U\Phi)
=
0,
\]
even though \(U\) is not injective.

The exact structural obstruction is that the excess data in the source's argument only see the restriction
\[
V=U|_{R(K)}.
\]
They cannot detect a kernel contained in \(R(K)^\perp\).

## Assumptions and scope
The counterexample satisfies every operator hypothesis printed in Corollary 5.11: \(K\) has closed range, \(U\) is bounded and onto, \(UK=KU\), and \(R(K)^\perp\) is invariant under \(U\).

The ordinary excess in the middle expression is taken on the projected frame space \(R(K)\), which is the frame space used by the source's projection construction.

The example deliberately has
\[
\Phi\subseteq R(K).
\]
Therefore it does not rely on any possible discrepancy between \(K\)-frame excess and the excess of a projected \(K\)-frame.

The repair below is stated at the ordinary projected-frame level and, for the exact numerical formula, assumes finite excess. It does not claim that every separate bridge from \(K\)-excess to projected excess is valid for arbitrary \(K\)-frames.

## Proof
First verify the source hypotheses. The backward shift \(B\) is a bounded surjection on \(N\) with
\[
N(B)=\operatorname{span}\{f_1\}.
\]
Therefore
\[
U=I_M\oplus B
\]
is a bounded surjection on \(H\) and
\[
N(U)=\operatorname{span}\{f_1\}.
\]
Because \(K=P_M\) and \(U\) is block diagonal with respect to \(M\oplus N\),
\[
UK=KU.
\]
The subspace
\[
N=M^\perp
\]
is visibly \(U\)-invariant.

For
\[
\Phi=\{e_0\},
\]
the \(K\)-frame identity is
\[
\sum_{\phi\in\Phi}|\langle x,\phi\rangle|^2
=
|\langle x,e_0\rangle|^2
=
\|P_Mx\|^2
=
\|K^*x\|^2.
\]
Thus \(\Phi\) is Parseval relative to \(K\). It has no redundant element, so
\[
E_K(\Phi)=0.
\]

Since
\[
P_Me_0=e_0
\]
and
\[
Ue_0=e_0,
\]
we have
\[
UP_M\Phi=\Phi=U\Phi.
\]
As an ordinary frame for \(M\), the singleton \(\{e_0\}\) has excess \(0\). Hence the three displayed excesses in the corollary are equal although \(U\) has the nonzero kernel vector \(f_1\).

Now isolate the exact information visible to the projected frame. Put
\[
M=R(K).
\]
From
\[
UK=KU
\]
one gets
\[
U(M)\subseteq M.
\]
Because \(U\) is onto, if \(m=Kh\in M\), choose \(x\) with \(Ux=h\); then
\[
m=KUx=UKx\in U(M).
\]
Thus
\[
U(M)=M.
\]
Let
\[
V=U|_M.
\]
The additional invariance of \(M^\perp\) means that \(U\) is block diagonal relative to \(M\oplus M^\perp\), so
\[
UP_M=P_MU.
\]
Therefore every projected transform is governed only by \(V\).

Let \(\Psi\) be a frame for \(M\) with synthesis operator
\[
T_\Psi:\ell^2(I)\to M.
\]
Since \(\Psi\) is a frame, \(T_\Psi\) is onto. Since \(V\) is onto, the map
\[
T_\Psi:\ker(VT_\Psi)\to\ker V
\]
is onto: for \(y\in\ker V\), choose \(c\) with \(T_\Psi c=y\), and then
\[
VT_\Psi c=0.
\]
Its kernel is exactly
\[
\ker T_\Psi.
\]
Hence
\[
0\longrightarrow\ker T_\Psi
\longrightarrow\ker(VT_\Psi)
\overset{T_\Psi}{\longrightarrow}\ker V
\longrightarrow0
\]
is exact.

For an ordinary frame, excess is the dimension of the synthesis kernel. If
\[
E(\Psi)<\infty,
\]
the exact sequence gives
\[
E(V\Psi)
=
E(\Psi)+\dim\ker V.
\]
Thus
\[
E(V\Psi)=E(\Psi)
\]
holds exactly when
\[
\ker V=\{0\},
\]
or equivalently
\[
N(U)\cap R(K)=\{0\}.
\]
This is the injectivity condition visible to the projected-frame argument.

## Verification
The target full text was inspected at the definition of \(K\)-frame excess, Theorem 5.9, Corollary 5.10, and Corollary 5.11. Corollary 5.11 explicitly assumes that \(U\) is onto, commutes with \(K\), and leaves \(R(K)^\perp\) invariant, then concludes that equality of the three excesses is equivalent to global injectivity of \(U\).

The preceding paragraph in the source obtains the corollary by appealing to the corresponding ordinary-frame statement for an onto operator and by commuting \(U\) with the projection onto \(R(K)\). That passage changes the relevant operator space: after projection, the ordinary frame lives on \(R(K)\), so the ordinary theorem applies to
\[
U|_{R(K)},
\]
not to the action of \(U\) on the orthogonal complement.

The counterexample makes this mismatch exact. The restriction
\[
U|_{R(K)}
\]
is the identity, while all noninjectivity is placed in
\[
R(K)^\perp.
\]
Every displayed sequence in the excess comparison is unchanged.

The finite-excess repair is verified independently by the exact sequence of synthesis kernels above. No numerical experiment, truncation, or finite approximation is used.

## Relationship to prior work
Ordinary frame excess is governed by the kernel of the synthesis operator. This is the mechanism used in the source and in the classical literature on excesses of frames.

A published comparison result has already identified a different problem with the source's projected-excess identity for arbitrary \(K\)-frames: projection onto \(R(K)\) can increase deletion excess. That issue does not cover the present claim. Here the single frame atom already belongs to \(R(K)\), so projection changes neither the sequence nor its excess. The failure comes solely from attempting to infer global injectivity from data confined to \(R(K)\).

Targeted searches for the exact source, Corollary 5.11, excess preservation under onto operators, restricted injectivity on \(R(K)\), and errata did not locate an indexed correction of this global-injectivity claim.

## Limitations
The finding refutes only the necessity of global injectivity in Corollary 5.11. It does not re-audit the source's separate claims about projected \(K\)-frame excess.

The exact formula
\[
E(V\Psi)=E(\Psi)+\dim\ker V
\]
is used here in the finite-excess regime to avoid cardinal cancellation when both sides are infinite.

A nonindexed erratum, thesis remark, or informal correction may contain the same restricted-injectivity observation.

## References
1. E. Agheshteh Moghaddam and A. A. Arefijamaal, *New aspects of weaving \(K\)-frames: the excess and duality*, Hacettepe Journal of Mathematics and Statistics 53(3) (2024), 652--666, DOI 10.15672/hujms.1008448; early public date 15 August 2023.
2. D. Bakić and T. Berić, *On excesses of frames*, Glasnik Matematički 50(2) (2015), 415--427, DOI 10.3336/gm.50.2.10; arXiv:1403.0632.
