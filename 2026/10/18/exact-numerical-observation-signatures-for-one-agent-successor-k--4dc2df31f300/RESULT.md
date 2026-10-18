# Exact numerical-observation signatures for one-agent successor knowing-value logic

## Finding

Fix any integer \(k\geq 0\). In the standard natural-number semantics of the announcement-free knowing-value logic with successor, take one \(\mathsf{S5}\) agent, one non-rigid numeric constant \(c\), no propositional letters, and restrict the available atomic numerical observations to the equalities
\[
E_j:\quad c\approx S^j0,\qquad 0\leq j<k,
\]
with Boolean constants permitted. Boolean operations, \(K\), and conditional \(\mathrm{Kv}(\varphi,t)\) for all successor terms \(t\) are allowed with *unbounded modal nesting*. Call this language \(\mathcal L_k\). More formally, every atomic equality in \(\mathcal L_k\) must reduce in standard successor arithmetic to a Boolean constant or one of the displayed tests; this permits equivalent offset presentations without adding observations.

For a pointed standard model \((\mathcal M,w)\), write \(H_w=\{c(v):w\sim v\}\) for the distinct values realized in the distinguished world’s epistemic class, and set
\[
B_k=\{0,\ldots,k-1\},\qquad
T_w=H_w\cap B_k,\qquad
r_w=\min\bigl(2,|H_w\setminus B_k|\bigr).
\]
Let \(\tau_w=c(w)\) if \(c(w)<k\), and let \(\tau_w=\ast\) otherwise.

**Exact pointed-theory invariant.** Two pointed models agree on every \(\mathcal L_k\) formula if and only if their signatures \((\tau_w,T_w,r_w)\) are identical. In particular every \(\mathcal L_k\) formula is equivalent, over all standard one-agent \(\mathsf{S5}\) models, to a Boolean combination of formulas with modal depth at most one drawn from
\[
E_j,\quad \Diamond E_j\ (j<k),\quad \Diamond E_\ast,\quad \mathrm{Kv}(E_\ast,c),
\qquad E_\ast:=\bigwedge_{j<k}\neg E_j,
\]
where \(\Diamond\psi:=\neg K\neg\psi\), and the empty conjunction is \(\top\). Depth one is optimal uniformly for every \(k\), including \(k=0\).

**Optimal model compression.** Every signature admits an equivalent pointed model with exactly \(|T_w|+r_w\) worlds in its accessible equivalence class, and none with fewer. Thus \(k+2\) is the smallest universal upper bound on the size of an accessible class required to preserve every formula of \(\mathcal L_k\).

**Exact spectrum.** The number \(N_k\) of distinct pointed complete \(\mathcal L_k\)-theories is
\[
N_0=2,\qquad N_k=3k\,2^{k-1}+2^{k+1}\quad(k\ge1).
\]
Consequently there are exactly \(2^{N_k}\) logical-equivalence classes of formulas in \(\mathcal L_k\). For \(k=0,1,2,3\), the respective numbers of pointed theories are \(2,7,20,52\).

## Assumptions and scope

A model consists of a nonempty world set \(W\), an equivalence relation \(\sim\), the **fixed standard** arithmetic structure \((\mathbb N,0,S)\) with \(S(n)=n+1\), and a world-dependent valuation \(c:W\to\mathbb N\). The set \(W\) may be infinite; no finite-model hypothesis is used. The agent has a single accessibility equivalence class at each evaluation point; irrelevant classes may be discarded. The term grammar is \(t::=0\mid c\mid St\). Rigid numeral terms may occur as \(\mathrm{Kv}\) targets, but are trivially known.

The atomic restriction concerns the **normal form** of an equality of successor terms, not its typography. In standard arithmetic every equation \(S^ac\approx S^bc\) is constantly true when \(a=b\) and constantly false otherwise. Every equation \(S^a0\approx S^b0\) is likewise constant. An equation \(S^ac\approx S^b0\) is false for \(b<a\), and otherwise is exactly \(c\approx S^{b-a}0\). The language admits such equations precisely when the latter index is below \(k\).

For a term \(S^ac\), conditional knowing value \(\mathrm{Kv}(\varphi,S^ac)\) is equivalent to \(\mathrm{Kv}(\varphi,c)\) because successor is injective. For every rigid numeral \(S^a0\), \(\mathrm{Kv}(\varphi,S^a0)\) is true. Thus one may take the primitive syntax to be \(\top\), \(E_0,\ldots,E_{k-1}\), \(\neg\), \(\land\), \(K\), and \(\mathrm{Kv}(-,c)\), without loss of expressive power.

The semantics used are
\[
\mathcal M,w\models K\varphi\iff\forall v\,(w\sim v\Rightarrow\mathcal M,v\models\varphi)
\]
and
\[
\mathcal M,w\models\mathrm{Kv}(\varphi,c)\iff
\bigl|\{c(v):w\sim v,\ \mathcal M,v\models\varphi\}\bigr|\le1.
\]
In particular, knowing value under an impossible condition holds vacuously.

## Proof

**1. Signature invariance at arbitrary nesting depth.** Fix an equivalence class and let \(T\) and \(r\) be its signature components. For each formula \(\varphi\) define a Boolean \(b_\varphi(a;T,r)\), where \(a\) ranges over the present named tags \(j\in T\), together with the tag \(\ast\) when \(r>0\). We prove by structural induction that each world of tag \(a\) satisfies \(\varphi\) if and only if \(b_\varphi(a;T,r)=1\). This statement is independent of the number of worlds carrying any one numeric value, and independent of the identities of the unnamed values.

For atoms, \(b_{E_j}(a;T,r)=1\) exactly when \(a=j\); Boolean operations are pointwise. For knowledge, the induction hypothesis makes \(K\varphi\) true exactly when \(b_\varphi(j;T,r)=1\) for every \(j\in T\) and, if \(r>0\), \(b_\varphi(\ast;T,r)=1\).

For conditional knowing value, distinct values, not multiplicities of worlds, matter. Each named \(j\in T\) contributes one distinct selected value when \(b_\varphi(j;T,r)=1\). All unnamed values satisfy \(\varphi\) together, because they have the same tag. If the unnamed tag satisfies \(\varphi\), its distinct-value contribution is at least two exactly when \(r=2\), one when \(r=1\), and zero when \(r=0\). Therefore
\[
\mathrm{Kv}(\varphi,c)\iff
\sum_{j\in T}b_\varphi(j;T,r)
+r\,b_\varphi(\ast;T,r)\le1,
\]
where the last summand is defined to be zero for \(r=0\). Truncating the actual number of unnamed distinct values at two is sufficient because the test is whether the number of distinct selected values is at most one. This completes the induction for every finite formula, independently of whether the model has infinitely many worlds.

**2. Every signature is definable at depth one.** Let \(L_\tau=E_\tau\) for named \(\tau\in B_k\), and \(L_\ast=E_\ast\). Presence or absence of a named value \(j\) in the accessible class is expressed by \(\Diamond E_j\) or \(\neg\Diamond E_j\). The three possible unnamed-value counts are distinguished by
\[
D_0=\neg\Diamond E_\ast,\qquad
D_1=\Diamond E_\ast\land\mathrm{Kv}(E_\ast,c),\qquad
D_2=\neg\mathrm{Kv}(E_\ast,c).
\]
Consequently each realizable signature \(\sigma=(\tau,T,r)\) is defined by the depth-one characteristic formula
\[
\chi_\sigma=L_\tau\land
\bigwedge_{j\in T}\Diamond E_j\land
\bigwedge_{j\in B_k\setminus T}\neg\Diamond E_j\land D_r.
\]
This proves the converse implication in pointed-theory equivalence. Since every formula is constant on finitely many characteristic classes, disjoining their characteristic formulas yields the depth-one Boolean normal form. The existence of two models with equal local tag and respectively one or two distinct unnamed values shows that depth zero cannot express \(\neg\mathrm{Kv}(E_\ast,c)\); take no named values for any \(k\). Thus depth one is necessary in general.

**3. Minimal representatives.** For any realizable \((\tau,T,r)\), construct an equivalence class with one world of numeric value \(j\) for each \(j\in T\), and exactly \(r\) worlds with distinct values \(k,k+1\) as needed. Place the distinguished world at its prescribed named value or at value \(k\) when \(\tau=\ast\). The resulting model has exactly \(|T|+r\) worlds and the given signature. Conversely, any model with the same theory has the same signature by Step 2: it must realize each \(j\in T\), plus at least \(r\) unnamed distinct values. Each distinct value requires a separate world. Hence \(|T|+r\) is optimal. The maximal value is \(k+2\), realized by \(T=B_k\) and \(r=2\), with a suitable named or unnamed root.

**4. Exact census.** When \(r=0\), a signature is possible precisely when \(T\ne\varnothing\) and \(\tau\in T\). There are \(\sum_{T\subseteq B_k}|T|=k2^{k-1}\) such signatures for \(k\ge1\). For each of \(r=1,2\), any \(T\subseteq B_k\) is allowed and the root tag can be any member of \(T\) or \(\ast\), giving \(k2^{k-1}+2^k\) cases each. Summing yields \(3k2^{k-1}+2^{k+1}\); when \(k=0\), only \((\ast,\varnothing,1)\) and \((\ast,\varnothing,2)\) occur. Characteristic formulas show that all subsets of the \(N_k\) signatures are definable, giving exactly \(2^{N_k}\) formula-equivalence classes.

## Verification

The accompanying `check_signature.py` computes the original standard-world semantics and the independent signature recurrence. With deterministic pseudorandom seed, it exhausts all nonempty supports in \(\{0,\dots,k+2\}\) for \(k=0,1,2,3\), tries every possible distinguished support value, and compares 80 generated formulas per parameter up to nesting depth four, including the conditional knowing-value operator. It also checks duplicate-world cases and canonical representative sizes. Its output is:

```text
k=0: signatures=2 optimal_max_worlds=2
k=1: signatures=7 optimal_max_worlds=3
k=2: signatures=20 optimal_max_worlds=4
k=3: signatures=52 optimal_max_worlds=5
KNOWING_VALUE_SIGNATURE_VERIFY_OK 82880
```

Execute `python check_signature.py` using Python 3; no external Python packages are required. The unrestricted equivalence, model bound, and census follow from the proof above, not extrapolation from these finite tests.

## Relationship to prior work

Wang [1] introduces successor arithmetic into conditional knowing-value logic and proves decidability and the finite-model property for its unrestricted announcement-free language. The source's general model construction is much larger and does not state a single-constant bounded-numeral signature classification, an exact number of pointed theories, or a sharp linear one-class cutoff.

Wang and Fan [2] establish completeness for conditional knowing-value logic in multi-agent epistemic frames, building on their earlier single-agent work, but without numerical equality observations or the explicit finite signature census. Gu and Wang [3] provide a normal-modal presentation and bisimulation analysis of conditional knowing value for general values; those methods are relevant to the invariant, but the examined statements do not give the exact arithmetic-observation classes, their sharp minimum model sizes, or the finite Boolean spectrum calculated here. A published quantitative certificate bound extracted from Wang's result [4] concerns unrestricted input-formula length, and neither subsumes the exact observation-bound classification nor contradicts it.

## Limitations

The classification is specific to **one agent, one non-rigid numeric constant, no unrelated propositional letters, and a finite, fixed collection of numeral observations**. It does not extend here to several agents, several independently valued constants, arbitrary extra propositional valuations, unbounded numerical observations as one language, public announcements, or arithmetic beyond successor. The characteristic formulas preserve truth of the entire restricted language, not numeric isomorphism types or the cardinality of underlying world sets. Prior work on generalized knowing-value bisimulation leaves a residual priority risk of an equivalent formulation under different terminology. An independent audit has not been performed.

## References

[1] Hongyi Wang, “Knowing-Value Logic with Successor Arithmetic,” arXiv:2606.31891, first version June 30, 2026; EPTCS 447 (2026), 731–749. https://arxiv.org/abs/2606.31891

[2] Yanjing Wang and Jie Fan, “Conditionally Knowing What,” *Advances in Modal Logic*, volume 10 (2014), pp. 569–587. https://www.aiml.net/volumes/volume10/Wang-Fan.pdf

[3] Tao Gu and Yanjing Wang, “'Knowing Value' Logic as a Normal Modal Logic,” arXiv:1604.08709 (2016). https://arxiv.org/abs/1604.08709

[4] “Successor knowing-value satisfiability has singly-exponential certificates,” published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-successor-knowing-value-satisfiability-has-singly-exponential-ce--9c9b7f880828
