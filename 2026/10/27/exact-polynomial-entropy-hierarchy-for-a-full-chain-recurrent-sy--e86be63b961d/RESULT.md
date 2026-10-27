# Exact polynomial-entropy hierarchy for a full-chain-recurrent symmetric-product counterexample

## Finding

Let \(X\subset\{0,1\}^{\mathbb Z}\) consist of all two-sided binary sequences having at most one occurrence of the transition \(01\) and at most one occurrence of \(10\). Let \(\sigma\) be the left shift. Identify the two constant sequences \(0^{\mathbb Z}\) and \(1^{\mathbb Z}\), and no other points; write \(q:X\to Y\) for the compact metrizable quotient and \(g:Y\to Y\) for the induced homeomorphism. This is the canonical example from Đorić (2026) with \(\operatorname{NW}(g)=\operatorname{Fix}(g)=\{p\}\), \(\operatorname{CR}(g)=Y\), and infinitely many nonfixed nonwandering configurations in its second symmetric product.

For every integer \(n\ge1\), the polynomial entropy of the finite symmetric-product map \(F_n(g)\) is exactly
\[
 h_{\mathrm{pol}}(F_n(g))=2n.
\]
For every integer \(n\ge2\), collapse the singleton subspace \(F_1(Y)\subset F_n(Y)\) to one point to form the ordinary symmetric-product suspension \(\mathcal SF_n(Y)\), with induced homeomorphism \(\mathcal SF_n(g)\). Then
\[
 h_{\mathrm{pol}}(\mathcal SF_n(g))=2n.
\]
In particular, \(h_{\mathrm{pol}}(g)=2\) and the induced map on the full hyperspace \(\mathcal K(Y)\) of nonempty compact subsets has infinite polynomial entropy. Every finite symmetric-product map has zero topological entropy, while its polynomial entropy grows unboundedly with \(n\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\) and the permitted bi-infinite sequences have at most one transition in each direction, not merely an arbitrary bound on transition density. The shift acts by \((\sigma x)_j=x_{j+1}\). The quotient identifies exactly the two fixed constant sequences; its unique identified point is \(p\). Both \(X\) and \(Y\) are compact metric spaces, and all maps above are homeomorphisms. The first-public source is arXiv:2610.23058v1, released October 16, 2026, with primary MSC2020 37B40.

Write \(F_n(Y)=\{A\subset Y:1\le |A|\le n\}\) with the Hausdorff metric, \(F_n(g)(A)=g(A)\). For \(n\ge2\), \(\mathcal SF_n(Y)=F_n(Y)/F_1(Y)\); the induced map is well-defined because singleton sets are invariant. The full hyperspace \(\mathcal K(Y)\) comprises all nonempty compact subsets, with induced map \(K\mapsto g(K)\).

For a continuous self-map \(T\) of a compact metric space \((Z,d)\), let
\[
 d_N^T(z,z')=\max_{0\le j<N}d(T^jz,T^jz'),
 \quad s_N(T,\eta)=\max\{|E|: E\text{ is }(N,\eta)\text{-separated}\}.
\]
The polynomial entropy used here is
\[
 h_{\mathrm{pol}}(T)=\lim_{\eta\downarrow0}\limsup_{N\to\infty}
 \frac{\log s_N(T,\eta)}{\log N}.
\]
It is independent of the compatible metric. In the proof \(n\) is held fixed and \(N\to\infty\); constants may depend on \(n\) and on the fixed scale \(\eta\).

## Proof

**1. Two-transition word complexity gives a universal upper bound.** Every finite word in the language of \(X\) has at most two changes of symbol. Conversely every binary word of length \(L\) with at most two changes occurs in \(X\), by extending both tails constantly. Thus the exact number of possible length-\(L\) windows is
\[
 P(L)=2\left(1+(L-1)+\binom{L-1}{2}\right)=L^2-L+2
 \qquad(L\ge1).
\]
Equip \(X\) with any standard product metric and \(Y\) with any quotient-compatible metric. Uniform continuity of \(q\) implies that for every \(\eta>0\) there is an integer \(R\ge1\) such that agreement of two sequences in positions \([-R,R]\) makes their quotient images \(\eta\)-close. If two configurations in \(Y\) admit representatives with the same word in the longer window \([-R,N-1+R]\), their first \(N\) forward iterates remain \(\eta\)-close.

For a set \(A\in F_n(Y)\), choose representatives in \(X\) of its at most \(n\) points (either constant sequence may represent \(p\)). Associate to \(A\) the unordered set of the corresponding length-\(N+2R\) words. Two configurations with the same unordered word set have Hausdorff orbit distance less than \(\eta\) throughout the first \(N\) times: each point in either configuration has a matching point in the other with an identical word, regardless of multiplicities. The number of possible profiles is at most
\[
 \sum_{j=1}^{n}\binom{P(N+2R)}{j}=O_{n,R}(N^{2n}).
\]
Consequently \(h_{\mathrm{pol}}(F_n(g))\le2n\). By monotonicity under factors, the same bound holds for \(\mathcal SF_n(g)\) for \(n\ge2\).

**2. Two independently placed transitions per particle give a matching lower bound.** Let \(z_{a,b}\in X\), for integers \(a<b\), be the sequence equal to \(1\) on \([a,b)\cap\mathbb Z\) and \(0\) elsewhere. The two interfaces of \(\sigma^t z_{a,b}\) pass coordinate zero at times \(t=a\) and \(t=b\). If the other interface is far away, at the first passage the quotient image \(q(\sigma^t z_{a,b})\) is arbitrarily close to \(u=q(x^{(0)})\), where \(x^{(0)}_j=0\) for \(j<0\) and \(1\) for \(j\ge0\); at the second passage it is close to \(v=q(y^{(0)})\), where \(y^{(0)}\) is the reverse step. Both \(u\) and \(v\) differ from \(p\). Whenever neither interface is near zero, the quotient image is close to \(p\), since its local word is constant and both constants have quotient image \(p\).

For a fixed \(n\ge1\), choose \(2n\) ordered, mutually well-separated time windows \(I_1,\ldots,I_{2n}\) inside \(\{0,\ldots,N-1\}\), each containing \(cN\) admissible integer times on a fixed coarse grid, where \(c>0\) depends on \(n\) and the chosen observation radius but not on \(N\). The windows and the grid can be arranged so that every two distinct admissible passage times are separated by more than a prescribed fixed \(R_0\), while each chosen second passage occurs after its paired first passage. Independently choose
\[
 a_i\in I_{2i-1},\qquad b_i\in I_{2i},\qquad 1\le i\le n,
\]
and form the \(n\)-point set
\[
 A(\mathbf a,\mathbf b)=\{q(z_{a_i,b_i}):1\le i\le n\}.
\]
The points are distinct because their first interface locations lie in disjoint windows. Thus there are at least \((cN)^{2n}\) distinct configurations.

Fix disjoint sufficiently small neighborhoods of \(p\) and of each of \(u,v\). By uniform continuity of the quotient map, choose \(R_0\) large enough that (i) a block with no interface within \(R_0\) of the origin has image near \(p\); and (ii) a block at exactly one interface, with the other farther than \(R_0\), has image near \(u\) or \(v\) according to its orientation. For any two different choices of \((\mathbf a,\mathbf b)\), there is a passage time \(t\) present in one set of chosen events and absent from the other. At this time exactly one point in the first configuration lies near \(u\) or \(v\), and all points in the other configuration lie near \(p\). Their Hausdorff images at time \(t\) are separated by a uniform positive amount \(\eta_0\), independent of \(N\). Therefore
\[
 s_N(F_n(g),\eta_0)\ge(cN)^{2n},
\]
which establishes \(h_{\mathrm{pol}}(F_n(g))\ge2n\).

**3. The lower bound survives collapsing singleton sets.** Now let \(n\ge2\). In the preceding marker-separated family, at any distinguished passage time the \(n-1\) points not responsible for that passage lie near \(p\). Hence the passing configuration is near either \(\{p,u\}\) or \(\{p,v\}\), each a genuine two-point set, while the configuration with no passage is near \(\{p\}\). Under the continuous quotient \(F_n(Y)\to\mathcal SF_n(Y)\), these two-point sets remain distinct from the collapsed singleton point. Compactness and continuity provide a uniform positive separation at the same passage times after increasing \(R_0\) if necessary. Thus the \((cN)^{2n}\) configurations remain separated at a fixed scale for \(\mathcal SF_n(g)\). This proves
\[
 h_{\mathrm{pol}}(\mathcal SF_n(g))\ge2n,
\]
and equality follows from Step 1.

**4. Full-hyperspace consequence.** Each \(F_n(Y)\) is a closed invariant subspace of \(\mathcal K(Y)\); therefore \(h_{\mathrm{pol}}(\mathcal K(g))\ge2n\) for every positive integer \(n\), hence it is infinite. For each finite \(n\), the polynomial upper bound in Step 1 implies zero topological entropy, since exponential growth of separated sets is excluded at every fixed scale.

The source construction additionally satisfies \(\operatorname{NW}(g)=\{p\}\), \(\operatorname{CR}(g)=Y\) and \(\operatorname{NW}(F_2(g))\) infinite. These facts are taken from the explicitly inspected construction of Đorić (2026), not re-proved as new results. They explain why finite-chain-recurrence entropy theorems do not directly apply to the case analyzed here.

## Verification

The accompanying `checker.py` computes the exact word-language cardinality for lengths \(1\) through \(14\) and tests the two-interface marker separation for \(n=1,2,3,4\) with explicit finite configurations, including every pair among \(4^n\) chosen configurations in each case. Its recorded output is `checker_output.txt`. These finite experiments check the symbolic combinatorics and distinguishability mechanism; the all-\(n\), all-\(N\), and quotient-topology assertions follow from the analytic proof above, not from enumeration. Run with a standard Python 3 interpreter by executing `python checker.py` in the package directory.

## Relationship to prior work

Đorić, *A note on the non-wandering dynamics in the \(n\)-fold symmetric products* (arXiv:2610.23058v1, 2026), constructs exactly the compact shift and constant-point quotient studied here. The paper proves the singleton nonwandering set, full chain recurrence, and the infinite nonwandering set in the induced symmetric product; it does not state the polynomial-entropy values or a separating-family proof for them.

Đorić, *Polynomial entropy on the \(n\)-fold symmetric product and its suspension* (arXiv:2507.10126v2, 2025/2026), proves the multiplicative entropy identity under a **finite chain recurrent set** hypothesis, and obtains a general lower bound under a wandering-point hypothesis. In the present example the chain recurrent set is all of infinite \(Y\), so that equality theorem is inapplicable. Its weaker lower bound does not imply the exact value \(2n\). Our proof directly constructs the necessary upper and lower estimates on this previously excluded canonical test case. Earlier work on nonwandering points in symmetric products examines recurrence properties rather than the asserted exact entropy spectrum.

## Limitations

This is a statement about the specified countable compact quotient of a two-transition binary subshift, not a theorem for arbitrary compact homeomorphisms with singleton nonwandering set or with full chain recurrence. The entropy identity need not extend to an unrestricted class without further hypotheses. We do not characterize all nonwandering points in \(F_n(Y)\) for arbitrary \(n\), nor give an exact finite-\(N\) separated-set cardinality. The exact entropy of the full hyperspace at the polynomial scale is infinite; no claim about its exact topological entropy is made. An independent originality or mathematical audit has not been performed.

## References

1. Maša Đorić, *A note on the non-wandering dynamics in the \(n\)-fold symmetric products*, arXiv:2610.23058v1 (first public submission 2026-10-16), https://arxiv.org/html/2610.23058v1 . Primary MSC2020 37B40.
2. Maša Đorić, *Polynomial entropy on the \(n\)-fold symmetric product and its suspension*, arXiv:2507.10126v2, https://arxiv.org/html/2507.10126v2 ; original arXiv submission 2025-07-14, later published in Glasnik Matematički 61(1) (2026), 59–76.
3. J. L. Gómez-Rueda, A. Illanes and H. Méndez, *Dynamic properties for the induced maps in the symmetric products*, Chaos, Solitons & Fractals 45 (2012), 1180–1187, https://doi.org/10.1016/j.chaos.2012.05.003 .
