# Affine contingency over S5: exact expressive and teaching dimensions with a sharp world cutoff

## Finding

Fix an integer \(k\ge 1\). In classical single-agent \(\mathsf{S5}\), take precisely the \(k\) propositional variables \(p_1,\ldots,p_k\) and the connectives \(\mathbf 0\), \(\mathbf 1\), exclusive-or \(\oplus\), and unary contingency \(\mathcal C\), with
\[
\mathcal C\varphi:=\Diamond\varphi\wedge\Diamond\neg\varphi.
\]
The Boolean operations \(\wedge\), \(\vee\), and unrestricted modal operators are *not* primitives of this fragment. All formulas, including arbitrarily nested contingencies, have one and only one semantic normal form
\[
 c\oplus\bigoplus_{i=1}^k a_i p_i
 \oplus\bigoplus_{0\ne s\in\mathbb F_2^k}b_s\mathcal C(\ell_s),
 \qquad \ell_s=\bigoplus_{i:s_i=1}p_i,
 \qquad c,a_i,b_s\in\mathbb F_2.
\]
The empty exclusive-or is \(\mathbf 0\). Here uniqueness means uniqueness of the coefficient vector under equivalence on **all pointed \(\mathsf{S5}\) models**, finite or infinite. Consequently there are exactly
\[
 2^{k+2^k}
\]
semantic equivalence classes of formulas in this fragment.

An example is a pointed \(\mathsf{S5}\) model together with the truth label of a target formula at its distinguished world. The minimum number of examples uniquely characterizing **any** one of these formulas against the entire \(k\)-variable fragment is exactly \(k+2^k\). A single *fixed*, explicit collection of that many pointed examples works simultaneously for every target, each example having at most \(k+1\) worlds.

The world bound is sharp: on the class of frames with at most \(k\) worlds there are exactly \(2^{k+2^k-1}\) equivalence classes, and the one new identity there is
\[
  \bigoplus_{0\ne s\in\mathbb F_2^k}\mathcal C(\ell_s)\equiv\mathbf 0.
\]
This identity fails on a \((k+1)\)-world universal \(\mathsf{S5}\) cluster. In particular, arbitrary formulas of the fragment are equivalent on all \(\mathsf{S5}\) frames if and only if they agree on every pointed \(\mathsf{S5}\) frame of at most \(k+1\) worlds, and no smaller uniform bound works.

## Assumptions and scope

A model is \((W,R,V)\) with \(W\ne\varnothing\), \(R\) an equivalence relation, and \(V(p_i)\subseteq W\). Satisfaction is the ordinary classical local Kripke satisfaction relation. The fragment does not contain additional propositional variables, unrestricted conjunction, or a primitive \(\Diamond\)/\(\Box\). Contingency has the displayed compound-modal semantics; \(\oplus\) is addition modulo two on truth values.

Every equivalence class of \(R\) is a universal cluster. At a chosen world \(w\), write \(v(w)\in\mathbb F_2^k\) for its valuation vector and \(S=\{v(u):uRw\}\) for the nonempty set of valuation vectors realized in the cluster; multiplicity does not matter. Define
\[
 L(S)=\operatorname{span}_{\mathbb F_2}\{u-u':u,u'\in S\}.
\]
For nonzero \(s\), set \(C_s(S)=1\) precisely when the parity \(\langle s,u\rangle\) takes both Boolean values as \(u\) ranges over \(S\). Equivalently,
\[
 C_s(S)=\mathbf1_{\{s\notin L(S)^\perp\}}.
\]
All equalities of formulas in this report are semantic equivalences on the stipulated model class. Statements about teaching sets use truth-labelled *pointed* models, not arbitrary labelled syntactic examples.

## Proof

**Normal-form reduction.** Each \(\mathcal C\theta\) has a cluster-constant truth value, because the accessible set from every point of the same equivalence class is identical. If \(g\) is cluster-constant then
\[
 \mathcal C(\theta\oplus g)\equiv\mathcal C\theta:
\]
adding the same Boolean bit at every accessible world cannot change whether both values occur. Similarly, \(\mathcal C\mathbf0\equiv\mathbf0\). Proceed by structural induction. An affine combination of normal forms is again a normal form (coefficients add modulo two). For a contingency of a normal form, remove the constant and all already cluster-constant \(\mathcal C(\ell_s)\) terms; only the linear local parity \(\ell_a\) remains. Its contingency equals \(\mathcal C(\ell_a)\) for \(a\ne0\), or \(\mathbf0\) for \(a=0\). Thus all modal nesting collapses to depth at most one, establishing existence of the claimed forms.

**Independence and exact expressive dimension.** On singleton clusters every \(C_s=0\), so the truth function of a normal form at valuation \(v\) is \(c+\langle a,v\rangle\) modulo two. Vanishing for all singleton valuations forces \(c=0\) and \(a=0\). Suppose next that
\[
 F(S)=\bigoplus_{s\ne0}b_sC_s(S)=0
\]
for every finite nonempty \(S\). Put \(T=\bigoplus_{s\ne0}b_s\). On \(S=\{0,e_1,\ldots,e_k\}\), the difference span is all of \(\mathbb F_2^k\), so \(C_s=1\) for all \(s\ne0\), giving \(T=0\). For each fixed \(s_0\ne0\), choose \(S=\{0\}\) together with a vector-space basis of the hyperplane \(s_0^\perp\). Then \(L(S)=s_0^\perp\). Exactly one of the nonzero parity indicators, \(C_{s_0}\), vanishes, so \(F(S)=T\oplus b_{s_0}=0\) forces \(b_{s_0}=0\). This includes \(k=1\), when the hyperplane is \(\{0\}\). Hence the \(1+k+(2^k-1)=k+2^k\) generators are linearly independent as Boolean functions on pointed \(\mathsf{S5}\) models. Every coefficient vector occurs syntactically, proving uniqueness and the count \(2^{k+2^k}\).

**Sharp world cutoff.** Every cluster of \(m\) worlds has difference span of dimension at most \(m-1\). If \(m\le k\), then \(L=L(S)\) is proper and
\[
 \bigoplus_{s\ne0}C_s(S)
 \equiv\left|\mathbb F_2^k\setminus L^\perp\right|\pmod2
 =\left(2^k-2^{k-\dim L}\right)\pmod2=0.
\]
For \(S=\{0,e_1,\ldots,e_k\}\) this expression is instead \((2^k-1)\bmod2=1\), so a \((k+1)\)-world countermodel exists. Moreover, after the local and constant coefficients are eliminated using singleton examples, the evaluations on all hyperplane spans give the \((2^k-1)\)-square matrix \(J+I\) over \(\mathbb F_2\): its row indexed by \(s_0\) is one in every contingency column except the \(s_0\) column. Since \(2^k-1\) is odd, \(J+I\) has kernel exactly the all-ones vector. Thus the displayed parity identity is the **only** coefficient relation on clusters of at most \(k\) worlds. The rank there is \(k+2^k-1\), giving \(2^{k+2^k-1}\) equivalence classes. Adding the full-span cluster removes the last relation and proves the sharp universal bound \(k+1\).

**Optimal teaching dimension.** Formula equivalence classes form a vector space of dimension \(D=k+2^k\) over \(\mathbb F_2\), since pointwise exclusive-or preserves the fragment. Every list of fewer than \(D\) pointed labelled examples imposes fewer than \(D\) independent linear constraints on the difference of two formulas, so a nonzero difference formula vanishes on all those examples. Thus no target admits a smaller uniquely characterizing set.

For the matching universal construction, use singleton clusters with distinguished vectors \(0,e_1,\ldots,e_k\) (\(k+1\) examples), one cluster with vectors \(0,e_1,\ldots,e_k\) distinguished at \(0\), and for each nonzero \(s\) except one fixed \(s_*\), a cluster of \(0\) and a basis of \(s^\perp\), distinguished at \(0\). These are
\[
 (k+1)+1+(2^k-2)=k+2^k=D
\]
pointed models, each containing at most \(k+1\) worlds. The singleton tests recover \(c,a_1,\ldots,a_k\). The full-span test recovers \(T=\bigoplus b_s\); the hyperplane test indexed by \(s\) then recovers \(b_s\) as \(T\) exclusive-or that test's contingency contribution. All \(b_s\), including the omitted one \(b_{s_*}\), are determined. Hence these \(D\) examples uniquely characterize each formula. No independence or optimality claims about smaller syntactic descriptions are needed.

## Verification

A standalone Python 3 program, `checker.py`, checks the truth-vector ranks of all \(D\) generators over all nonempty valuation-vector sets of size at most \(k+1\) for \(k=1,2,3,4\), verifies the unique one-relation loss when model size is limited to \(k\), and independently checks that the explicit teaching families have rank \(D\). It tests the parity cutoff over every small valuation subset, and for \(k\le3\) compares direct recursive semantics of 1,200 reproducibly generated nested formulas against the canonical normal form. Reproduction: `python3 checker.py`. Expected final output: `ALL CHECKS PASSED`.

The general quantifiers are established by the preceding linear-algebraic proof. Finite tests do not certify its unbounded cases and cannot establish external priority.

## Relationship to prior work

Bezhanishvili, ten Cate, Ganguly and Meier (2026) survey modal fragments generated by Boolean bases and arbitrary modal connectives. They explicitly include contingency as an example of a bundled, non-simple connective and point to unresolved affine-fragment questions, together with the teachability perspective. The present theorem treats the specific \(\{\oplus,\mathbf0,\mathbf1,\mathcal C\}\) basis over one-agent \(\mathsf{S5}\) and counts its equivalence classes and optimal teaching examples; these conclusions are not stated in the inspected survey. It does **not** solve their general affine complexity questions.

Krebs and Meier (first public preprint 2025) prove an \(\mathsf{NP}\)-hardness result for **two-agent** affine modal satisfiability using primitive possibility operators. That logic is not the one-operator contingency fragment here, and their complexity theorem yields neither this canonical basis nor the sharp teaching/world counts. Ding and Yang (2026) develop broad bisimulation and axiomatization techniques for bundled operators, including contingency; their inspected treatment likewise does not give the restricted affine free-algebra dimension. Humberstone's older noncontingency literature is relevant background, not claimed as a source of this new numerical theorem. The numerical sequence \(2^{2^k+k}\) is independently listed in OEIS A073113 under a generic integer-formula description; the sequence itself is not new, while the modal interpretation and sharp teaching and world bounds are the scientific claim.

## Limitations

The theorem concerns only **single-agent \(\mathsf{S5}\)**, a *fixed finite variable vocabulary*, and exactly the stated affine Boolean operations plus contingency. It does not extend as stated to general \(\mathsf K\), multi-agent products, primitive \(\Diamond\), or the addition of \(\land\). It provides no optimal formula-size bounds, and no hardness classification for a related satisfiability problem. A broader modal-algebra or noncontingency normal-form theorem under different terminology could affect priority; comparison with all historical literature is not exhaustive. No independent audit is claimed.

## References

1. N. Bezhanishvili, B. ten Cate, A. Ganguly, A. Meier, *Modal Fragments*, first public March 5, 2026, arXiv:2603.05055; https://arxiv.org/abs/2603.05055. Sections 4.1, 4.4, 4.5, 6.
2. A. Krebs, A. Meier, *When Symmetry Yields NP-Hardness: Affine ML-SAT on S5 Frames*, first public December 19, 2025, arXiv:2512.17378; https://arxiv.org/abs/2512.17378. Section 3, Theorem 3.1.
3. Y. Ding, Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, first public March 27, 2026, arXiv:2603.26268; https://arxiv.org/abs/2603.26268. Sections 1 and 4.
4. L. Humberstone, *The Logic of Non-Contingency*, Notre Dame Journal of Formal Logic 36 (1995), 214–229, doi:10.1305/ndjfl/1040248455. Relevant historical background; not fully inspected here.
5. OEIS Foundation, *A073113: \(a(k)=2^{2^k+k}\)*, https://oeis.org/A073113. Numerical sequence only; no matching modal interpretation established by this source.
