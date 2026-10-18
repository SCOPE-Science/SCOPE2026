# Congruence cuts and renewal spectra of finite tense Heyting chains

## Finding
For each integer \(m\ge1\), take the fixed \((m+1)\)-element Gödel chain
\[C_m=\{0<1<\cdots<m\},\qquad x\to y=\begin{cases}m,&x\le y,\\y,&x>y.\end{cases}\]
A tense Heyting expansion is a quadruple \((G,H,F,P)\) satisfying (T0)–(T4) in Pelaitay–Zuluaga [1]. The paper's congruence–filter theorem yields a bijection between congruences and tense filters. Here an exact, chain-specific normal form makes the entire congruence spectrum enumerable.

Write \(g=G\), \(h=H\). Every expansion is specified uniquely by two nondecreasing maps \(g,h:C_m\to C_m\) with \(g(0)=h(0)=0\), \(g(m)=h(m)=m\), subject only to
\[g(i)\le f_h(i),\qquad h(i)\le p_g(i)\quad(0\le i\le m),\]
where the unique left adjoints are
\[f_h(i)=\min\{j:i\le h(j)\},\qquad p_g(i)=\min\{j:i\le g(j)\}.\]
The other operators are \(F=f_h\), \(P=p_g\). Define the **congruence-cut set**
\[K(g,h)=\{k\in\{1,\ldots,m-1\}:g(k)=h(k)=k\}.\]
The congruence lattice is a chain of precisely \(2+|K(g,h)|\) elements, including the universal and identity congruences. Every interior cut is simultaneously fixed by \(G,H,F,P\).

A cut separates the expansion canonically into two independent tense Heyting expansions on shorter chains. Cutting at all interior fixed points gives a unique ordered factorization into **simple** expansions (ones having only the identity and universal congruences).

Let \(B_0=1\), and for \(m\ge1\) let \(B_m\) be the number of all expansions of \(C_m\), and \(I_m\) the number of simple expansions. Then
\[I_1=B_1=1,\qquad I_m=B_m-\sum_{j=1}^{m-1}I_j B_{m-j}\quad(m\ge2).\]
The ordinary formal generating series satisfy
\[B(z)=1+\sum_{m\ge1}B_m z^m=\frac{1}{1-I(z)},\qquad I(z)=\sum_{m\ge1}I_mz^m.\]
For every integer \(r\) with \(1\le r\le m\), the number of expansions whose congruence lattice contains exactly \(r+1\) elements is
\[\boxed{\ [z^m]I(z)^r\ }.\]
The full congruence polynomial, weighting the number of *interior* congruence cuts, is
\[\boxed{\ Q_m(t)=[z^m]\frac{I(z)}{1-tI(z)}\ }.\]
Thus the coefficient of \(t^s\) counts expansions with exactly \(s+2\) congruences, \(0\le s\le m-1\). The first six \((B_m,I_m)\) pairs are \((1,1),(4,3),(29,22),(266,203),(2762,2118),(31004,23876)\). In particular,
\[Q_4(t)=203+53t+9t^2+t^3,\]
\[Q_5(t)=2118+538t+93t^2+12t^3+t^4,\]
\[Q_6(t)=23876+5938t+1032t^2+142t^3+15t^4+t^5.\]

## Assumptions and scope
The lattice is the **fixed labelled ordered chain**, with its **ordinary Heyting implication**, not an arbitrary DLI implication and not a negative-tense reduct. Tense Heyting means exactly the four operations and axioms (T0)–(T4) in [1, Definition 8.3]: \(G(0)=H(0)=0\); \(P\dashv G\) and \(F\dashv H\); and the two cross-operator inequalities involving meets and joins. No extra unmentioned commutativity, seriality, involution, or idempotence axioms are imposed. For \(m=0\), the one-element algebra is used only as a formal counting base \(B_0=1\), not in the positive-length factorization.

All formal generating functions are interpreted coefficientwise; no analytic convergence is assumed. The order of operators \(G,H,F,P\) is fixed, and different labelled operation tables count separately. A finite chain has no nontrivial order automorphism, so this is also an isomorphism count for fixed chain size.

## Proof
**1. Unique adjoints and the chain normal form.** Every right adjoint of a finite-chain map is nondecreasing and preserves the greatest element; (T0) fixes the least element. Conversely, every such \(g,h\) has unique left adjoints \(p_g,f_h\) given by the displayed minimum formulas. On a chain, the (T4) inequality \(G(x\vee y)\le G(x)\vee F(y)\), evaluated at \(x=0\), gives \(g(y)\le f_h(y)\) because \(g(0)=0\). The symmetric inequality gives \(h(y)\le p_g(y)\).

Conversely, assume these two pointwise inequalities. If \(x\le y\), then \(g(x)\wedge f_h(y)\le g(x)\le f_h(x)=f_h(x\wedge y)\); if \(x>y\), the left side is at most \(f_h(y)=f_h(x\wedge y)\). This proves the first part of (T3); the second is symmetric. If \(x\le y\), then \(g(x\vee y)=g(y)\le f_h(y)\le g(x)\vee f_h(y)\); if \(x>y\), then the right side contains \(g(x)\). This proves (T4) and its symmetric form. Therefore the pointwise inequalities are **necessary and sufficient**. In particular the implication-dependent (T5)–(T6) conditions of [1, Definition 3.1] also hold, either by its Proposition 8.1 or directly from the displayed Gödel implication and monotonicity.

The exact total \(B_m\) is consequently the finite expression
\[B_m=\sum_{\substack{g,h:C_m\to C_m\ \mathrm{nondecreasing}\\g(0)=h(0)=0,\ g(m)=h(m)=m}}\ \prod_{i=0}^{m}\mathbf1_{\{g(i)\le f_h(i)\}}\mathbf1_{\{h(i)\le p_g(i)\}}.\]
No reference to a previously computed enumeration is required.

**2. Common fixed cuts characterize congruences.** Every Heyting congruence of the chain corresponds to a terminal filter \([k,m]\) for some \(k\in\{0,\ldots,m\}\): the equivalence identifies the elements of this terminal interval and leaves smaller elements singleton. By the tense-filter correspondence of [1, Proposition 6.1], it survives the unary expansion precisely when \(g(k)\ge k\) and \(h(k)\ge k\). As \(P=p_g\dashv g\) and \(F=f_h\dashv h\), these inequalities imply \(p_g(k)\le k\) and \(f_h(k)\le k\), respectively. By Step 1, \(k\le g(k)\le f_h(k)\le k\) and \(k\le h(k)\le p_g(k)\le k\). Therefore all four values are \(k\). The converse is immediate. There are two endpoint congruences plus exactly one for every common interior fixed point. A sublattice of the chain of Heyting congruences is again a chain.

**3. Exact splitting at a cut.** Fix \(k\in K(g,h)\). The preceding inequalities show also \(p_g(k)=f_h(k)=k\). Since these are *least* arguments at which \(g,h\), respectively, reach \(k\), they imply \(g(j),h(j)<k\) for every \(j<k\). All four monotone maps therefore restrict to \([0,k]\) and \([k,m]\). Their restrictions satisfy the pointwise normal form in Step 1. After shifting the upper interval down by \(k\), each restriction is a tense Heyting expansion of a chain of lengths \(k\) and \(m-k\).

Conversely, each admissible smaller expansion is **top-reflecting**: if its top is \(d\), the normal form at \(i=d\) forces \(f_h(d)=p_g(d)=d\); hence neither \(g\) nor \(h\) reaches \(d\) earlier. Given two expansions on \(C_k\) and \(C_{m-k}\), translate the second by \(k\) and glue at the common endpoint. By top reflection, the two left adjoints glue exactly as the two right adjoints do; the pointwise inequalities hold on both sides. This construction is inverse to splitting and introduces the common fixed cut \(k\).

**4. Unique factorization and spectrum.** Split at every element of \(K(g,h)\), in increasing order. Every resulting factor has no internal common fixed point, hence is simple by Step 2. The ordered list of positive factor lengths is a composition of \(m\), and the factorization is unique because its cuts are intrinsically recoverable from \(G,H\). Conversely, any ordered concatenation of simple factors has **exactly** the joining cuts, since no factor contains an interior cut. If there are \(r\) factors, there are exactly \(r-1\) internal cuts and \(r+1\) congruences. Multiplying factor counts and summing over compositions proves \([z^m]I(z)^r\), the series identities, and the recurrence for \(I_m\).

## Verification
Run `python3 verify.py` from this package. The script independently enumerates pairs of finite monotone maps, reconstructs both left adjoints, and compares the normal-form criterion against all (T0)–(T6) identities through \(m=4\). For all 300 admissible expansions through \(m=4\), it also enumerates set partitions and directly checks operation compatibility to corroborate the claimed congruence count. It checks the product count for *every* prescribed subset of cuts through \(m=6\), then verifies the renewal recurrence and complete congruence polynomial through \(m=6\). The generated small values are stated above; the checker prints `VERIFY_OK` on success. These finite computations are checks of a general proof, not substitutes for it.

## Relationship to prior work
Pelaitay and Zuluaga [1] established the definition of tense Heyting algebras, the DLI/Nelson comparison, and a general congruence–tense-filter correspondence. The present finding uses these established ingredients and specializes to the fixed Gödel chain. Its additional statements are the two-inequality normal form, four-operator common-cut rigidity, free factorization at every congruence, and exact all-ranks renewal generating series. The earlier general congruence correspondence by itself does not state the counted factorization or congruence-rank distribution. Work on negative tense Heyting operators [2] uses different tense axioms and is not identified with the present positive tense variety merely because initial enumeration totals may coincide.

## Limitations
No asymptotic formula for \(I_m/B_m\) is claimed. The theorem does not cover arbitrary DLI implications, lattice products, or tense expansions without (T0). The first six numerical rows are computed; the all-sizes theorem is the normal form and formal coefficient identity, not an unproved extrapolation from the rows. Independent mathematical validation and exhaustive historical priority checking have not been performed.

## References
[1] Gustavo Pelaitay and William Zuluaga, *Tense operators on distributive lattices with implication*, arXiv:2208.13889v1 (first posted 2022-08-29), especially Definition 3.1, Proposition 6.1, Definition 8.3, and Proposition 8.1; journal DOI: 10.1007/s11225-023-10047-4.

[2] Federico Almiñana, Gustavo Pelaitay, and William Zuluaga, *On Heyting Algebras with Negative Tense Operators*, arXiv:2212.14756 (2022), cited solely for distinction from a different negative-tense signature.
