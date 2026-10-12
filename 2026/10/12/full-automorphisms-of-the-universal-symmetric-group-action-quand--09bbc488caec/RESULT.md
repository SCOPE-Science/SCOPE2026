# Full automorphisms of the universal symmetric-group action quandle

## Finding
For every integer \(n\ge 3\), let \(G=\mathfrak S_n\) act naturally on \([n]\), and equip \(Q_n=[n]\times G\) with Kai's group-action quandle product
\[
(x,g)\triangleleft(y,h)=(x^{g^{-1}h},h^{-1}gh).
\]
For every partition \(\lambda=(1^{m_1}2^{m_2}\cdots)\vdash n\), choose a permutation \(g_\lambda\in G\) of cycle type \(\lambda\), and let \(C_G(g)\) denote its centralizer. Then the **entire** automorphism group is
\[
\operatorname{Aut}(Q_n)\cong G\times K_n,\qquad
K_n=\prod_{\lambda\vdash n}Z(C_G(g_\lambda)).
\]
In explicit cyclic factors, this is
\[
K_n\cong\prod_{\lambda\vdash n}
\left(\prod_{\substack{d\ge2\\m_d>0}}C_d\right)
\times\left(\prod_{\substack{\lambda\vdash n\\m_1=2}}C_2\right).
\]
The inner automorphisms are \(G\times\langle\delta\rangle\), where \(\delta\in K_n\) is the family represented by \(g_\lambda\) in the corresponding centralizer centers. Its order is \(\ell_n=\operatorname{lcm}(1,\ldots,n)\). Consequently,
\[
\operatorname{Aut}(Q_n)/\operatorname{Inn}(Q_n)\cong K_n/\langle\delta\rangle.
\]
Define
\[
A_n=\prod_{\lambda\vdash n}2^{\mathbf1_{\{m_1(\lambda)=2\}}}
\prod_{\substack{d\ge2\\m_d(\lambda)>0}}d.
\]
Then \(|\operatorname{Aut}(Q_n)|=n!A_n\) and \(|\operatorname{Aut}(Q_n)/\operatorname{Inn}(Q_n)|=A_n/\ell_n\). In particular, for \(n=3\) all \(36\) automorphisms are inner; for \(n=4\) the full group has order \(2304\), while the inner group has order \(288\) and the outer quotient is \(C_2^3\) of order \(8\). There are non-inner automorphisms for every \(n\ge4\).

## Assumptions and scope
The underlying set is \([n]\times\mathfrak S_n\), the action is the natural faithful right action, and every automorphism is a bijective self-map preserving the displayed quandle operation. The result concerns every \(n\ge3\); the centerlessness of \(\mathfrak S_n\) is essential to the argument. The result determines automorphisms of the whole action quandle, not just automorphisms of its conjugation-quandle quotient. All groups \(C_d\) are cyclic of order \(d\), with empty products trivial. Automorphisms are composed consistently with right-action notation.

## Proof
**Step 1: intrinsic fibers.** For each \((y,h)\), its right translation is
\(R_h(x,g)=(x^{g^{-1}h},h^{-1}gh)\), independent of \(y\). If \(R_h=R_k\), their second coordinates give identical conjugations on \(G\), hence \(hk^{-1}\in Z(G)=1\). Thus the fibers \([n]\times\{g\}\) are exactly the intrinsic equivalence classes of elements with identical right translations. Every quandle automorphism \(F\) has the form \(F(x,g)=(x^{b_g},f(g))\), with \(b_g\in G\) and a permutation \(f\) of \(G\) preserving its conjugation quandle.

**Step 2: the base permutation is inner.** For a centerless group \(G\), automorphisms of its conjugation quandle preserve the group multiplication: writing \(r_g(u)=g^{-1}ug\), we have \(r_{gh}=r_h\circ r_g\); conjugation by a quandle automorphism sends \(r_g\) to \(r_{f(g)}\), and injectivity of \(g\mapsto r_g\) gives \(f(gh)=f(g)f(h)\). In particular \(f(e)=e\). Applying \(F\) to \((x,e)\triangleleft(y,h)=(x^h,e)\) gives
\[
(x^h)^{b_e}=(x^{b_e})^{f(h)}\quad\text{for all }x,h.
\]
Since \(G\) is the entire symmetric group on \([n]\), this implies \(f(h)=b_e^{-1}hb_e\). Hence even in degree six the exceptional outer group automorphisms of \(\mathfrak S_6\) cannot lift.

**Step 3: the fiberwise kernel.** Define the diagonal quandle automorphisms \(T_h(x,g)=(x^h,h^{-1}gh)\). These realize all induced inner automorphisms of the base; after composing with one, any automorphism has the form \(F_a(x,g)=(x^{a_g},g)\). Direct substitution into the operation shows that \(F_a\) is a quandle homomorphism exactly when
\[
g^{-1}h\,a_{h^{-1}gh}=a_g\,g^{-1}h\quad(g,h\in G).
\]
Setting \(h=e\) says \(a_g\in C_G(g)\). The equation then becomes \(a_{h^{-1}gh}=h^{-1}a_gh\). For \(h\in C_G(g)\) this forces \(a_g\in Z(C_G(g))\). Conversely, choose freely one \(a_{g_\lambda}\in Z(C_G(g_\lambda))\) for every conjugacy class and transport to its other elements by conjugation. Centrality makes the transport independent of the chosen conjugator, and the displayed identity holds. Every such \(F_a\) is bijective because it permutes each finite fiber. Composition identifies the kernel with the abelian direct product \(K_n\).

**Step 4: direct product and inner subgroup.** The conjugacy-equivariance of \(a\) makes each \(F_a\) commute with every \(T_h\). Their intersection is trivial: only the identity diagonal action fixes every group-label fiber, since \(G\) has trivial center. Therefore \(\operatorname{Aut}(Q_n)=G\times K_n\). The right translations satisfy \(R_h=T_h F_\delta^{-1}\), where \(\delta_g=g\) for every \(g\). Thus \(R_e=F_\delta^{-1}\) and \(T_h=R_hR_e^{-1}\) lie in the inner group, so \(\operatorname{Inn}(Q_n)=G\times\langle\delta\rangle\). The order of \(\delta\) is the exponent \(\ell_n\) of \(G\).

**Step 5: cyclic decomposition and sharp transition.** The standard cycle centralizer is \(C_G(g_\lambda)\cong\prod_{d:m_d>0}(C_d\wr\mathfrak S_{m_d})\). For \(d\ge2\), the center of its \(d\)-block is the cyclic group of simultaneous rotations, of order \(d\). For \(d=1\), it is \(Z(\mathfrak S_{m_1})\), nontrivial exactly when \(m_1=2\), when it is \(C_2\). These facts give all cyclic factors and \(A_n\). For \(n=3\), \(K_3\cong C_2\times C_3=\langle\delta\rangle\). For \(n=4\), \(K_4\cong C_2^3\times C_3\times C_4\), and quotienting by \(\langle\delta\rangle\cong C_{12}\) gives \(C_2^3\). For \(n\ge4\), choose a class-local central twist which acts nontrivially on the transposition class and trivially on the double-transposition class. These two classes consist of elements of order two, so no uniform power \(g\mapsto g^k\) can yield such a twist. It is therefore outside \(\langle\delta\rangle\), giving the claimed threshold.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It reconstructs \(\mathfrak S_3\) and \(\mathfrak S_4\) as explicit permutations, enumerates conjugacy classes and their centralizer centers, independently builds all \(6\) and \(96\) possible fiberwise automorphisms, checks well-defined conjugacy transport and the quandle-homomorphism relation for every ordered pair \((g,h)\), and compares with the partition product. It also checks the full quandle equation for representative nontrivial fiberwise twists. It separately enumerates the partition factors through rank six. These finite tests corroborate but do not establish the arbitrary-rank theorem.

## Relationship to prior work
Kai, *Quandles associated with group actions* (arXiv:2609.17438), defines the action quandle, proves its universal embedding role, and calculates its **inner** automorphism group and connected components. The calculation \(\operatorname{Inn}(Q_n)\cong\mathfrak S_n\times C_{\ell_n}\) is prior work, recovered above for comparison; it does not determine the additional class-local centralizer symmetries or full automorphism group. Bardakov--Nasybullov--Singh, *Automorphism groups of quandles and related groups* (arXiv:1705.10607), treats automorphisms of conjugation quandles and other quandle constructions. Here that theory explains only the induced quotient action and does not classify fiberwise lifts in \(Q_n\). Standard group theory supplies the centralizers of permutations, but applying their **centers** simultaneously to every conjugacy fiber yields the new full-quandle group formula. The earlier Fenn--Rourke matrix-rack realization and its possible automorphism-theoretic descendants remain a historical-overlap risk.

## Limitations
This is a classification inside the specific natural symmetric-group action construction and does not assert a general automorphism formula for arbitrary faithful group actions, finite quandles, or rack extensions. The theorem relies on elementary group and permutation-action identities and is not independently audited. The finite computation checks ranks three and four rather than infinitely many ranks. Relevant historical formulations in rack and extension literature may contain an equivalent result not identified by the literature comparisons.

## References
1. R. Kai, *Quandles associated with group actions*, arXiv:2609.17438v2 (2026), https://arxiv.org/html/2609.17438v2.
2. V. Bardakov, T. Nasybullov and M. Singh, *Automorphism groups of quandles and related groups*, arXiv:1705.10607 (2017), https://arxiv.org/abs/1705.10607.
3. Standard centralizer structure of permutations by cycle type, \(\prod_d(C_d\wr\mathfrak S_{m_d})\), proved elementarily in Step 5.
