# One-step Arf closure and rigidity of reflective numerical semigroups

## Finding
Let \(S\) be any reflective numerical semigroup of positive genus \(g\) and multiplicity \(a\). Write \(g=qa+r\), where \(q\geq0\) and \(1\leq r<a\). The Arf closure \(\operatorname{Arf}(S)\), defined as the smallest Arf numerical semigroup containing \(S\), has the following complete description:

\[
\operatorname{Arf}(S)=
\begin{cases}
S,&q=0\text{ or }a=2,\\
\{0,a,2a,\ldots,qa\}\cup[g+1,\infty)\cap\mathbb Z,&q\geq1,\ a\geq3.
\end{cases}
\]

In the nontrivial case, its new elements are exactly \(g+a,g+2a,\ldots,g+qa\). Consequently its genus is \(g-q\), its conductor is \(g+1\), and the first application of the Arf operator already equals the Arf closure. In the remaining cases \(S\) itself is Arf. Thus the Arf index of every reflective numerical semigroup is at most one. A reflective numerical semigroup is Arf precisely when it is ordinary (\(a=g+1\)) or has multiplicity two. Among reflective semigroups of genus \(g\), exactly one is Arf when \(g\) is even or \(g=1\), and exactly two when \(g\geq3\) is odd.

## Assumptions and scope
A numerical semigroup is an additive submonoid \(S\subseteq\mathbb Z_{\geq0}\) with finite complement. Its genus \(g\) counts omitted nonnegative integers, its multiplicity \(a\) is its least positive element, and its conductor \(c\) is the least integer such that every integer at least \(c\) belongs to \(S\). It is *reflective* if its set of gaps contains exactly one integer from each residue class modulo its genus. A numerical semigroup is *Arf* if \(x+y-z\in S\) whenever \(x\geq y\geq z\) are in \(S\). Define the Arf operator \(A(U)=\{x+y-z:x,y,z\in U,\ x\geq y\geq z\}\); it contains \(U\) and is additive. Its eventual stabilization yields the Arf closure. The *Arf index* is the minimum number of applications of \(A\) required to reach that closure (zero for an already Arf semigroup).

Shor's characterization of reflective semigroups [1, Proposition 3.4] gives \(2\leq a\leq g+1\), \(a\nmid g\), the unique reflective semigroup for each permitted \((g,a)\), and the exact gap set
\[
H(S)=\{n:1\leq n<g,\ a\nmid n\}\ \cup\ \{g+ka:0\leq k\leq q\}.
\]
This established classification is the sole imported structural premise of the proof.

## Proof
**Step 1: Cases with no change.** If \(q=0\), then \(a=g+1\), so \(S=\{0\}\cup([g+1,\infty)\cap\mathbb Z)\). If the largest of an ordered triple in this semigroup is positive, \(x+y-z\geq x\geq g+1\), hence it lies in \(S\); an all-zero triple also works. Thus \(S\) is Arf.

If \(a=2\), then \(g\) is necessarily odd, and the gap description implies \(S\) consists of all even nonnegative integers together with all odd integers at least \(2g+1\). To verify the Arf property, take \(x\geq y\geq z\) from \(S\). If \(x\geq2g+1\), then \(x+y-z\geq x\) belongs to \(S\). Otherwise all three entries are even, so \(x+y-z\) is a nonnegative even integer in \(S\).

**Step 2: Explicit oversemigroup.** Assume \(q\geq1\) and \(a\geq3\). Let
\[
T=\{0,a,2a,\ldots,qa\}\cup([g+1,\infty)\cap\mathbb Z).
\]
The gap description shows that \(T\setminus S=\{g+a,g+2a,\ldots,g+qa\}\), so \(S\subset T\). The set \(T\) is Arf: for any \(x\geq y\geq z\) in \(T\), the number \(x+y-z\) is at least \(x\). If \(x\geq g+1\), it is therefore in \(T\). If \(x\leq g\), all three entries are nonnegative multiples of \(a\), and so is \(x+y-z\). Such a multiple belongs to \(T\) either because it is at most \(qa\), or because it is at least \((q+1)a>g\). Hence \(T\) is Arf.

**Step 3: Every new element is forced in one step.** For \(1\leq k\leq q\), set \(h_k=g+ka\). The two preceding integers \(h_k-1\) and \(h_k-2\) are both at least \(g+1\) because \(a\geq3\); neither is congruent to \(g\) modulo \(a\), hence neither lies in the high-gap progression. Therefore both belong to \(S\). Taking \(x=y=h_k-1\), \(z=h_k-2\), we obtain
\[
x+y-z=2(h_k-1)-(h_k-2)=h_k.
\]
Thus \(T\subseteq A(S)\). Conversely, \(T\) is Arf and contains \(S\), so \(A(S)\subseteq T\). It follows that \(A(S)=T=\operatorname{Arf}(S)\), and the Arf index is one since the \(q\) newly added gaps are nonempty.

**Step 4: Invariants and counting.** Precisely \(q\) gaps are filled, giving genus \(g-q\). The integer \(g\) remains a gap whereas all larger integers belong to \(T\), giving conductor \(g+1\). In the cases of Step 1 the closure leaves \(S\) unchanged. Finally Shor's bijection between reflective semigroups of genus \(g\) and multiplicities \(2\leq a\leq g+1\) not dividing \(g\) shows that the ordinary member \(a=g+1\) always occurs and the additional Arf member \(a=2\) occurs precisely for odd \(g>1\). This yields the enumeration stated above.

## Verification
A standalone Python 3 verifier, `verify_arf.py`, independently constructs each reflective semigroup from Shor's generators using finite additive reachability and computes its Arf saturation using sums and the equivalent two-variable condition \(2x-y\). For genera \(1\) through \(90\), it checks all \(3{,}760\) admissible multiplicity cases: initial gap sets, exact final closures, number of added gaps, and stability. For genera at most \(35\), it separately evaluates the entire three-variable Arf operator and verifies one-step equality. Its recorded output is:

```
PASS cases=3760, strict_closures=3626, added_gaps=9545, original_gap_checks=229753, direct_triple_cases=534, max_genus=90
```

Reproduce with `python3 verify_arf.py`. The universal statement rests on Steps 1–4; the finite program is a diagnostic independent of those arguments.

## Relationship to prior work
Shor [1] classifies reflective semigroups by their genus and multiplicity and explicitly identifies their gaps; it does not state this Arf-closure formula or uniform one-step stabilization. García-Sánchez and coauthors [2] parametrize Arf semigroups through other invariants, without specializing to reflective semigroups. İlhan and Karakaş [3] provide general algorithms for Arf closure, but not the formula in this reflection class. Çelik [4] computes Arf closures for specific two-generator symmetric families with prime multiplicity; certain small-multiplicity reflective subfamilies overlap those hypotheses, but his treatment does not cover the full reflective family or the uniform one-step assertion. This result directly exploits [1]'s gap classification to settle the Arf-closure problem for all reflective semigroups.

## Limitations
The theorem does not classify arbitrary numerical semigroups or determine Arf indices beyond the reflective family. A general closure algorithm can compute any individual example; the contribution is the uniform symbolic classification for all admissible genera and multiplicities. It uses [1]'s previously proved gap theorem. Bibliographic searches cannot exclude an equivalent unindexed formulation, and no independent review is claimed.

## References
[1] C. M. Shor, *Reflective numerical semigroups*, arXiv:2207.00051v1, first public 2022-06-30, Proposition 3.4. https://arxiv.org/abs/2207.00051

[2] P. A. García-Sánchez, B. A. Heredia, H. İ. Karakaş, J. C. Rosales, *Parametrizing Arf numerical semigroups*, arXiv:1604.08929v2. https://arxiv.org/abs/1604.08929

[3] S. İlhan, H. İ. Karakaş, *Arf numerical semigroups*, Turkish Journal of Mathematics 41 (2017), 1448–1457, doi:10.3906/mat-1512-46. https://doi.org/10.3906/mat-1512-46

[4] A. Çelik, *On Arf closure of some symmetric numerical semigroups with multiplicity p-prime*, JP Journal of Algebra, Number Theory and Applications 62 (2023), 109–122, doi:10.17654/0972555523024. https://doi.org/10.17654/0972555523024
