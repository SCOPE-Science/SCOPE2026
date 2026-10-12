# Orbit-minimum classification and rooted-tree census for the Alex law on finite chains

## Finding

For a finite linearly ordered Alexandrov space, the interaction axiom
\[
\mathsf{Alex}:\quad \Diamond\mathsf F p\;\longrightarrow\;\mathsf F\Diamond p
\]
does **not** characterize temporal continuity: the class of all, including discontinuous, temporal maps satisfying the axiom has a precise orbit-minimum description and a rooted-tree enumeration.

**Theorem.** For every integer \(n\ge1\) and arbitrary map \(f:C_n\to C_n\), validity of \(\mathsf{Alex}\) at all worlds under every valuation is equivalent to monotonicity of
\[
q_f(x)=\min\{f^t(x):t\ge0\}.
\]
When valid, let \(S=\{s_1<\cdots<s_k\}\) be the fixed points of \(q_f\). Then \(s_1=0\), and with \(s_{k+1}=n\) each interval \(B_i=\{s_i,\ldots,s_{i+1}-1\}\) has the following exact structure: the outgoing edges of the nonroot points form a labeled directed spanning tree toward the root \(s_i\); the root has one freely chosen outgoing edge to a world in \(\{s_i,\ldots,n-1\}\). These choices independently describe every valid map, without double counting.

Put \(\tau(1)=1\) and \(\tau(b)=b^{b-2}\) for \(b\ge2\). The exact number of valid maps, among all \(n^n\) maps, is
\[
A_n=\sum_{\substack{k\ge1,\ b_1+\cdots+b_k=n\\b_i\ge1}}\ \prod_{i=1}^k
\left(n-\sum_{j<i}b_j\right)\tau(b_i).
\]
Equivalently, the following recurrence computes it without enumerating maps:
\[
F_n(n)=1,\qquad
F_n(s)=(n-s)\sum_{b=1}^{n-s}\tau(b)F_n(s+b)
\quad(0\le s<n),\qquad A_n=F_n(0).
\]
The values for \(n=1,2,\ldots,10\) are
\[
1,\ 4,\ 24,\ 188,\ 1825,\ 21420,\ 299572,\ 4932880,\ 94435713,\ 2073167150.
\]

## Assumptions and scope

Let \(C_n=\{0,1,\ldots,n-1\}\), \(n\ge1\), with its usual total order. Its open sets are upsets. The spatial modality \(\Diamond\) is **topological closure**, so for every \(P\subseteq C_n\),
\[
\mathcal C(P)=\{x\in C_n:\exists y\in P\ (x\le y)\}.
\]
For any total endofunction \(f:C_n\to C_n\), with no continuity hypothesis, the temporal eventuality operator is
\[
\mathcal E_f(P)=\{x\in C_n:\exists t\in\mathbb N\ (f^t(x)\in P)\},
\]
where \(\mathbb N\) includes zero and \(f^0\) is the identity. Every propositional valuation is an arbitrary subset \(P\subseteq C_n\), and \(\mathsf{Alex}\) is valid iff \(\mathcal C(\mathcal E_f(P))\subseteq\mathcal E_f(\mathcal C(P))\) for every such \(P\). The logical vocabulary agrees with the axiom named \(\mathsf{Alex}\) in Vooijs and Fernández-Duque [1], but relaxing temporal continuity is deliberate: maps in this theorem need not be dynamic topological models as defined in [1].

## Proof

**1. Valuation elimination.** Finiteness ensures that the minimum \(q_f(x)=\min_{t\ge0}f^t(x)\) exists and is attained at some finite time. Suppose \(\mathsf{Alex}\) is valid. Let \(x\le y\) and \(t\ge0\), and use the singleton valuation \(P=\{f^t(y)\}\). Then \(y\in\mathcal E_f(P)\), hence \(x\in\mathcal C(\mathcal E_f(P))\). Validity yields some \(m\ge0\) with \(f^m(x)\le f^t(y)\), and thus
\[
q_f(x)\le f^t(y).
\]
Choosing \(t\) attaining \(q_f(y)\) gives \(q_f(x)\le q_f(y)\). Conversely, suppose \(q_f\) is nondecreasing and \(x\in\mathcal C(\mathcal E_f(P))\). Choose \(y\ge x\) and \(t\ge0\) with \(f^t(y)\in P\). At a time \(m\) attaining \(q_f(x)\),
\[
f^m(x)=q_f(x)\le q_f(y)\le f^t(y),
\]
so \(f^m(x)\in\mathcal C(P)\), yielding \(x\in\mathcal E_f(\mathcal C(P))\). This proves the first equivalence for all valuations and all worlds.

**2. Orbit-minimum retractions.** For any map \(f\), \(q_f(x)\le x\), because time zero is included. The orbit of \(f(x)\) is the tail of the orbit of \(x\), and if \(r=q_f(x)\), then \(r=f^t(x)\) for some \(t\). Since no point on the whole orbit is smaller than \(r\), and \(r\) itself begins its own orbit, \(q_f(r)=r\). Thus \(q_f\) is idempotent. Under its monotonicity, its set of fixed points \(S\) is nonempty and contains zero. If \(s\in S\) and \(s\le x\), monotonicity gives \(s=q_f(s)\le q_f(x)\). Since \(q_f(x)\le x\) and is fixed, it is exactly the greatest member of \(S\) not exceeding \(x\). Consequently the fibers of \(q_f\) are the successive intervals
\[
B_i=[s_i,s_{i+1}-1]\cap C_n,
\]
with the final boundary interpreted as \(s_{k+1}=n\).

**3. Directed-tree decomposition.** If \(x\in B_i\setminus\{s_i\}\), then \(q_f(f(x))=q_f(x)=s_i\): omitting the first orbit element cannot remove its minimum because \(x>s_i\). Hence \(f(x)\in B_i\). Because \(q_f(x)=s_i\), the forward orbit actually reaches \(s_i\). Therefore all edges departing nonroot vertices stay in their block and reach that block's root, yielding exactly one directed tree toward \(s_i\). At the root, \(q_f(s_i)=s_i\) implies merely \(f(s_i)\ge s_i\), with no further constraint.

Conversely, fix any composition \(n=b_1+\cdots+b_k\) of positive parts, form its consecutive intervals \(B_i\) with left endpoints \(s_i\), choose independently an inward directed rooted tree on each block (edges from its nonroot points), and choose \(f(s_i)\) anywhere in \(\{s_i,\ldots,n-1\}\). From every nonroot point the orbit reaches its block root. Subsequently it may follow the root edge, but all vertices visited are at least that root: each subsequent block root is no smaller than the preceding root, and the nonroot edges stay inside the current block. Therefore the minimum over the entire orbit of every point in \(B_i\) is exactly \(s_i\). Hence \(q_f\) is the nondecreasing block-floor map, proving validity. The fixed points of \(q_f\) uniquely recover the composition, so the construction is injective as well as surjective.

**4. Enumeration.** For a labeled block of size \(b\) with a predetermined root, there are \(b^{b-2}\) trees when \(b\ge2\) by Cayley's labeled-tree formula, and one empty-rooted tree when \(b=1\). Orientation toward the specified root is unique. The root at position \(s_i\) independently has \(n-s_i\) possible temporal successors. Multiplying these factors over blocks and summing over ordered compositions proves the displayed formula. Splitting a composition at its first block proves the recurrence. These arguments include the one-world boundary case.

**5. Strict separation from continuity.** On the two-world chain, let \(f(0)=1\) and \(f(1)=0\). Then \(q_f(0)=q_f(1)=0\), so \(\mathsf{Alex}\) holds, but \(f\) reverses the order and is not continuous. At five worlds, \(1825\) endofunctions validate \(\mathsf{Alex}\), whereas only \(\binom{9}{5}=126\) endofunctions are nondecreasing. Thus even on a chain the axiom is a strict and quantitatively large weakening of continuity.

## Verification

The companion source file `artifacts/check_alex.py` uses only the Python 3 standard library and can be run by

```sh
python3 artifacts/check_alex.py
```

It independently evaluates the modal implication on **every valuation of every endofunction on up to five points**, exhaustively enumerates **all endofunctions on up to seven points** to compare the orbit-minimum condition with the tree decomposition, and compares both exact counting formulas for sizes one through ten. The seven-world exhaustive stage examines \(7^7=823543\) maps. Successful execution prints `VERIFY_OK`. Finite checks do not prove the theorem for arbitrary \(n\); the preceding four proof steps do.

## Relationship to prior work

Vooijs and Fernández-Duque [1, Introduction and Example 2.10] identify \(\mathsf{Alex}\) and show that monotone temporal maps on preorders validate it. They investigate computable axiomatizability of the resulting logic, not arbitrary discontinuous maps on finite chains. In contrast, the present equivalence admits maps that fail their continuity assumption, and the block-tree bijection counts all maps preserving this single axiom. The implication 'temporal continuity implies \(\mathsf{Alex}\)' is prior work and is not claimed here.

Konev, Kontchakov, Wolter and Zakharyaschev [2] investigate dynamic topological logics with continuous temporal maps. Fernández-Duque and Montacute [3] work with scattered spaces, continuous maps, and a different topological operator (Cantor derivative). Neither covers this enumeration under arbitrary temporal endofunctions. Cayley's tree formula [4] is a classical input; the new relationship is the derivation of exactly these rooted-tree factors from modal-temporal validity and the independent root-edge choices. The present result does not settle general Alexandrov DTL axiomatizability, which [1] addresses.

## Limitations

The classification is for **finite total orders** with the upset Alexandrov topology, **all valuations** and the single displayed \(\mathsf{Alex}\) axiom. It does not classify arbitrary finite preorders, infinitely many worlds, the complete set of DTL-valid formulas, nor axioms containing 'next'. The maps allowed here are not in general continuous and so need not be ordinary dynamic topological systems under [1–3]. The quoted rooted-tree counts depend on the labeled chain, not on quotienting by order automorphisms. Independent scholarly verification and exhaustive historical literature coverage have not been performed.

## References

1. N. C. Vooijs and D. Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, LIPIcs 380, article 81 (2026), DOI: 10.4230/LIPIcs.LICS.2026.81; https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.81 .
2. B. Konev, R. Kontchakov, F. Wolter and M. Zakharyaschev, *Dynamic Topological Logics over Spaces with Continuous Functions*, Advances in Modal Logic 6 (2006), 299–318; https://www.aiml.net/volumes/volume6/Konev-Kontchakov-Wolter-Zakharyaschev.ps .
3. D. Fernández-Duque and Y. Montacute, *Untangled: A Complete Dynamic Topological Logic*, AAAI 2023, 6355–6362, DOI: 10.1609/aaai.v37i5.25782; https://ojs.aaai.org/index.php/AAAI/article/view/25782/25554 .
4. A. Cayley, *A Theorem on Trees*, Quarterly Journal of Mathematics 23 (1889), 376–378. The rooted labeled tree count is classical.
