# Involution-rank series and a domain-density limit for rooted-tree partial symmetries

## Finding

The partial automorphism inverse monoid of the finite regular rooted tree admits an exact domain-rank enumerator for all self-inverse elements. In the binary case, a uniformly chosen self-inverse partial automorphism has an asymptotically deterministic domain fraction: if the tree has height \(h\) and \(N_h=2^{h+1}-1\) vertices, then
\[
\frac{|\operatorname{Dom}f_h|}{N_h}\xrightarrow[h\to\infty]{\mathbb P}\alpha=0.708075950588044670778\ldots.
\]
The convergence constant is defined rigorously by the derivative recurrences below. There is also an explicit inversion-equivariant bijection between the set of binary-tree partial automorphisms augmented by one formal point and the automorphism group of the binary tree one level taller. This explains the already-known unrefined involution-count sequence; novelty is **not** claimed for that sequence or its previously tabulated exponential growth constant.

## Assumptions and scope

Let \(T_{d,h}\) denote the complete rooted \(d\)-ary tree of height \(h\), with vertices the words of lengths at most \(h\) over \(\{0,\ldots,d-1\}\). Let \(\mathcal P_{d,h}\) consist of root-preserving rooted-tree isomorphisms between nonempty connected ancestor-closed induced subtrees of \(T_{d,h}\). Composition is partial composition. The domain rank is its number of vertices, **including** the root. A self-inverse element \(f\) means \(f=f^{-1}\), equivalently \(f^2=\operatorname{id}_{\operatorname{Dom}f}\). Thus it has equal domain and range. All probabilities below sample uniformly from this finite self-inverse set, not from the full inverse monoid.

For \(d\ge1\), let
\[
S_{d,h}(t)=\sum_{f\in\mathcal P_{d,h}}t^{|\operatorname{Dom}f|},\quad
J_{d,h}(t)=\sum_{f=f^{-1}}t^{|\operatorname{Dom}f|}.
\]
At height zero, \(S_{d,0}(t)=J_{d,0}(t)=t\).

## Proof

**1. Root decomposition and exact enumerators.** Every partial rooted-tree isomorphism determines a partial injection between the active root-child sets. For each chosen source child and target child it specifies a smaller partial rooted-tree isomorphism. Consequently, for every \(d\ge1\) and \(h\ge1\),
\[
S_{d,h}(t)=t\sum_{r=0}^{d}\binom dr^2r!\,S_{d,h-1}(t)^r.
\]
For an involution, the root-child partial injection is itself a partial involution. It has \(r\) fixed children and \(s\) disjoint transposed pairs. The fixed children carry self-inverse smaller maps. A transposed pair carries one arbitrary smaller map and its inverse, with both domains contributing to the rank. Choosing the fixed points and pairing the remaining selected children yields
\[
\boxed{J_{d,h}(t)=t\sum_{\substack{r,s\ge0\\r+2s\le d}}
\frac{d!}{(d-r-2s)!\,r!\,2^ss!}
J_{d,h-1}(t)^r S_{d,h-1}(t^2)^s.}
\]
The choices are uniquely recoverable, so the formulas hold coefficient by coefficient and exhaust every case.

**2. Binary specialization and the known unrefined coincidence.** Put \(S_h=S_{2,h}\), \(J_h=J_{2,h}\), \(F_h=S_h(1)\), \(I_h=J_h(1)\), and \(U_h=I_h+1\). Then
\[
S_h(t)=t\bigl(1+4S_{h-1}(t)+2S_{h-1}(t)^2\bigr),\quad
J_h(t)=t\bigl((1+J_{h-1}(t))^2+S_{h-1}(t^2)\bigr).
\]
It follows inductively that
\[
F_h=2^{2^{h+1}-1}-1,\qquad U_0=2,\qquad
U_h=U_{h-1}^{\,2}+2^{2^h-1}.
\]
The values \(U_h\) are **already known**: \(U_h\) is OEIS A332757 shifted to the count of involutions in the automorphism group of a binary tree of height \(h+1\). We supply a direct structural explanation, without asserting numerical priority. Write \(\mathcal P_{2,h}^{+}=\mathcal P_{2,h}\sqcup\{\star\}\), with \(\star^{-1}=\star\). At \(h=0\), send the one partial identity and \(\star\) to the two elements of \(C_2\). Inductively, represent an element by a permutation \(\pi\in S_2\) together with two labels in \(\mathcal P_{2,h-1}^{+}\). For a nonempty active-child injection, \(\pi\) is the unique complete binary permutation extending it, and an inactive child receives label \(\star\); active child labels are its two sections. For the root-only element choose all labels \(\star\) and \(\pi=\mathrm{id}\); for the extra element \(\star\) choose all labels \(\star\) and \(\pi=(0\ 1)\). These assignments are bijective and send inversion to the ordinary wreath-product inverse. Applying the induction to the two section labels gives an inversion-equivariant bijection
\[
\mathcal P_{2,h}^{+}\longleftrightarrow
\operatorname{Aut}(T_{2,h+1}).
\]
This is a bijection of **sets with inversion**, not an asserted semigroup or group isomorphism.

**3. Domain-density constant.** Set \(M_h=S_h'(1)\), \(V_h=J_h'(1)\). Differentiating the exact polynomials gives the *integer* recurrences
\[
\begin{aligned}
&M_0=V_0=1,\\
&M_h=F_h+4(F_{h-1}+1)M_{h-1},\\
&V_h=I_h+2U_{h-1}V_{h-1}+2M_{h-1}.
\end{aligned}
\]
Define \(q_h=V_h/(2^hU_h)\). Let \(B_h=(F_{h-1}+1)/U_h\). As \(0\le V_{h-1}\le (2^h-1)I_{h-1}\) and \(0\le M_{h-1}\le(2^h-1)F_{h-1}\), the preceding recurrences imply
\[
|q_h-q_{h-1}|\le2^{-h}+4B_h.
\]
For \(h\ge2\), since \(U_{h-1}\ge6^{2^{h-2}}\) and \(F_{h-1}+1=2^{2^h-1}\),
\[
0<B_h\le\frac{F_{h-1}+1}{U_{h-1}^2}\le
\tfrac12(2/3)^{2^{h-1}}.
\]
Thus \(\sum_h|q_h-q_{h-1}|<\infty\). Set
\[
\boxed{\alpha=\tfrac12\lim_{h\to\infty}\frac{V_h}{2^hU_h}.}
\]
Then the expected normalized domain size converges to \(\alpha\), because \(I_h/U_h\to1\) and \(N_h/2^h\to2\). The numeric expansion stated above is reproducible from the integer recurrences; a precise tail bound follows by subtracting the limiting increments \(2^{-h}\). In fact
\[
\left|q_h-q_{h-1}-2^{-h}\right|
\le4 B_h+2^{-h}/U_h,
\]
so \(\alpha\) is approximated by \((q_H+2^{-H})/2\) with error at most one half the corresponding summable tail; already \(H=10\) yields many accurate decimal places.

**4. Concentration.** At the root of a uniformly chosen involution, the probability that both children are present and individually fixed is \(I_{h-1}^2/I_h\). Its complementary probability is at most \(2/U_{h-1}+(F_{h-1}+1)/U_{h-1}^2\), tending to zero. Therefore, for any fixed \(L\), with probability tending to one as \(h\to\infty\), *every* vertex in the first \(L\) levels is in the domain and is fixed. On this event, the \(2^L\) subtrees hanging below level \(L\) carry independent uniform involutive partial maps of height \(h-L\). Apart from the deterministic top \(2^L-1\) vertices, normalized total domain size is the average of \(2^L\) independent variables in \([0,1]\), up to a deterministic multiplicative factor tending to one. Its conditional variance is at most \(1/(4\cdot2^L)\); the conditional mean tends to \(\alpha\). First take \(h\to\infty\), then \(L\to\infty\), and apply Chebyshev's inequality to obtain convergence in probability as stated.

## Verification

The companion standalone script `verify_tree_involutions.py` independently constructs the finite partial rooted-tree mappings, checks their inverses as partial maps, and compares every domain-rank coefficient at heights \(0,1,2,3\). It exhausts \(1+7+127+32767\) partial mappings across these heights, confirms the polynomial recurrences to height \(6\), and checks the binary cardinality recurrences and the derivative evaluation of \(\alpha\). The all-height proof is the decomposition above; finite enumeration is corroboration rather than exhaustive evidence at unbounded height.

## Relationship to prior work

Kochubinska's earlier full texts establish the partial-wreath-product model, the total cardinality and idempotent-related enumerations, and asymptotic spectral properties of unrestricted random partial automorphisms. Kochubinska and Oliynyk (2024) investigate free inverse subsemigroups and finite automata; their published claims do not state this involution-support distribution or conditioned domain-density limit. Crucially, the unrefined recursion for \(U_h\), its values and its asymptotic growth constant already appear as OEIS A332757 for a wreath-product group; they are **not** asserted to be new here. The scope claimed as not covered in inspected literature is the coefficient-wise self-inverse rank enumerator for partial tree symmetries and the limiting typical domain fraction. The inversion-equivariant bijection supplies a direct explanation of the known numerical coincidence. Equivalent results concealed in other wreath-product or combinatorial presentations remain a priority risk.

## Limitations

The domain limit concerns uniform sampling from self-inverse partial rooted-tree maps for fixed binary branching \(d=2\) and height tending to infinity; no analogous limit is asserted for arbitrary growing branching degree. The explicit bijection preserves inversion but not multiplication or domain size. The known involution-count sequence is not original. Literature coverage does not establish historical uniqueness; publication-level priority requires broader independent comparison. The numerical constant is defined by exact recurrences, not by finite-model curve fitting.

## References

1. E. Kochubinska and A. Oliynyk, *Monogenic free inverse semigroups and partial automorphisms of regular rooted trees*, Matematychni Studii 61 (2024), 3–9, doi:10.30970/ms.61.1.3-9, https://matstud.org.ua/ojs/index.php/matstud/article/download/476/226/ .
2. E. Kochubinska, *Combinatorics of partial wreath power of finite inverse symmetric semigroup*, Algebra and Discrete Mathematics (2007), https://admjournal.luguniv.edu.ua/index.php/adm/article/download/834/365 .
3. E. Kochubinska, *Spectral properties of partial automorphisms of a binary rooted tree*, Algebra and Discrete Mathematics 26 (2018), 280–289, https://admjournal.luguniv.edu.ua/index.php/adm/article/download/532/pdf .
4. E. Kochubinska, *Spectrum of partial automorphisms of regular rooted tree*, arXiv:2006.15558, https://arxiv.org/pdf/2006.15558 .
5. OEIS Foundation, A332757, *Number of involutions (including identity) in an iterated wreath product of \(C_2\)*, https://oeis.org/A332757 .
