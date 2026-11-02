# Exact frame correspondence and labelled chain census for intuitionistic monotone possibility

## Finding

In constructive-neighbourhood semantics for intuitionistic monotone modal logic, the formula
\[\mathsf I_{\Diamond}(p):=(\Box\top\to\Diamond p)\to\Diamond p\]
has an exact frame correspondent for *arbitrary nonempty preordered world sets*, not merely the previously used sufficient condition of continual neighbourhood support. The condition is the stable-neighbourhood downset-refinement property (SNDR) in the next section. The same correspondent works for every substitution instance \(\mathsf I_{\Diamond}(\varphi)\).

For the fixed labelled chain \(W=[n]=\{0,\ldots,n-1\}\), \(n\ge1\), with unrestricted concrete neighbourhood families \(N(i)\subseteq\mathcal P(\mathcal P(W))\), put
\[
c_{-1}=2^n,\qquad c_m=2^n-2^m\ (0\le m\le n),\qquad q_m=2^{c_m}-1\ (-1\le m\le n).
\]
Then the **exact number of frames validating \(\mathsf I_{\Diamond}\) under every persistent valuation** is
\[
\boxed{C_n=1+q_{-1}^{\,n}+
\sum_{\ell=0}^{n-2}\sum_{m=-1}^{n-1}
(1+q_m)^{\ell}\left(q_m^{\,n-\ell-1}-q_{m+1}^{\,n-\ell-1}\right).}
\]
Here an empty sum is zero; the frames are counted with labelled worlds and distinct families, not up to isomorphism. The first counts are
\[C_1=4,\quad C_2=241,\quad C_3=16690673,\quad C_4=18446303034659832065.\]

The published *continual* condition holds on exactly
\[R_n=\sum_{j=0}^{n}q_{-1}^{\,j}\]
such chain frames. Its sufficiency is strict from three worlds onward: \(C_3-R_3=44017\), although \(C_2=R_2\). No one- or two-world preordered frame can witness strictness; a three-world chain can.

## Assumptions and scope

Fix a nonempty set \(W\), an arbitrary preorder \(\le\), and \(N:W\to\mathcal P(\mathcal P(W))\). The empty family \(N(w)=\varnothing\) and the empty neighbourhood \(\varnothing\in N(w)\) are both allowed and are distinct. A propositional valuation assigns an upward-closed set to each atom. Propositional implication is intuitionistic, and the modal clauses are:
\[
\begin{aligned}
w\Vdash\Box\varphi&\iff \forall v\ge w\ \exists A\in N(v)\ \forall x\in A\ (x\Vdash\varphi),\\
w\Vdash\Diamond\varphi&\iff \forall v\ge w\ \forall A\in N(v)\ \exists x\in A\ (x\Vdash\varphi).
\end{aligned}
\]
All formulas have upward-closed truth sets. Write \(\uparrow w=\{v:w\le v\}\) and \(\downarrow A=\{x:\exists a\in A,\ x\le a\}\). Define the stable worlds
\[S=\{s\in W:\forall t\ge s,\ N(t)\ne\varnothing\}.\]
The **SNDR property** is
\[
\tag{SNDR}
\forall w\in W\ \forall v\ge w\ \forall A\in N(v)\ \exists s\ge w\ \exists B\in N(s)
\bigl(s\in S\ \wedge\ B\subseteq\downarrow A\bigr).
\]
Equivalently, any neighbourhood visible above \(w\) admits a neighbourhood contained in its downward closure at some *stable* world above \(w\). This is a statement about the entire concrete neighbourhood family; quotienting by a frame equivalence is not assumed.

## Proof

**Exact frame correspondence.** Let \(U\subseteq W\) be upward-closed, and let \(D(U)\) denote the truth set of \(\Diamond p\) for \(V(p)=U\). By the modal clauses,
\[
D(U)=\{w:\forall v\ge w\ \forall A\in N(v),\ A\cap U\ne\varnothing\};
\]
\(D(U)\) is upward-closed, and the truth set of \(\Box\top\) is precisely \(S\). Because \(U\) is an upset, \(A\cap U=\varnothing\) if and only if \(\downarrow A\cap U=\varnothing\).

Assume SNDR. If \(w\notin D(U)\), choose \(v\ge w\) and \(A\in N(v)\) disjoint from \(U\). SNDR supplies \(s\ge w\), \(s\in S\), and \(B\in N(s)\) with \(B\subseteq\downarrow A\). Hence \(B\cap U=\varnothing\) and \(s\notin D(U)\), while \(s\Vdash\Box\top\). Thus \(w\not\Vdash\Box\top\to\Diamond p\), and so the axiom holds at \(w\). Every formula also has an upset as its truth set, so the same argument proves every substitution instance.

Conversely, suppose SNDR fails at \(w,v,A\). Take the *single* propositional valuation \(V(p)=U:=W\setminus\downarrow A\), which is an upset. Since \(A\cap U=\varnothing\), \(w\not\Vdash\Diamond p\). Failure of SNDR says every \(B\in N(s)\) for stable \(s\ge w\) meets \(U\). Because \(S\) is upward-closed, each such \(s\) has \(s\Vdash\Diamond p\). Thus \(w\Vdash\Box\top\to\Diamond p\), which falsifies \(\mathsf I_{\Diamond}(p)\) at \(w\). The equivalence holds for any cardinality of \(W\).

**Continual frames and strictness.** The existing sufficient condition is: \(N(v)\ne\varnothing\) and \(v\le s\) imply \(N(s)\ne\varnothing\). Under this condition, in SNDR choose \(s=v\) and \(B=A\), since \(v\in S\) and \(A\subseteq\downarrow A\). It is not necessary. On \(W=\{0<1<2\}\) let
\[N(0)=\{\{2\}\},\quad N(1)=\varnothing,\quad N(2)=\{\{0\}\}.\]
Then \(S=\{2\}\). Every neighbourhood visible anywhere is refined by \(\{0\}\in N(2)\) because \(\{0\}\subseteq\downarrow\{2\}=W\); the neighbourhood at \(2\) refines itself. SNDR holds, but continual support fails at \(0<1\). With one or two worlds, any failure of continual support has a nonempty neighbourhood above some \(w\) and no stable successor above that \(w\); SNDR fails. Hence three worlds are minimal for a strict example.

**Chain normal form and count.** On the \(n\)-element chain define the rank of a neighbourhood \(A\) to be \(-1\) if \(A=\varnothing\) and \(\max A\) otherwise. Then \(B\subseteq\downarrow A\) is equivalent to \(\operatorname{rank}(B)\le\operatorname{rank}(A)\). Exactly \(c_m\) of the \(2^n\) subsets of \(W\) have rank at least \(m\), for \(-1\le m\le n\).

If every \(N(i)\) is nonempty, the frame is continual and there are \(q_{-1}^{\,n}\) choices. If \(N(n-1)=\varnothing\), SNDR forces all \(N(i)=\varnothing\), one choice. Otherwise let \(\ell\in\{0,\ldots,n-2\}\) be the last index for which \(N(\ell)=\varnothing\), and set \(t=n-\ell-1\). Then \(S=\{\ell+1,\ldots,n-1\}\), and SNDR holds exactly when the smallest neighbourhood rank anywhere in the stable suffix is no greater than every rank in the first \(\ell\) rows. Indeed, the stable suffix is accessible above each earlier world, and each later neighbourhood is a valid self-refinement.

For prescribed smallest suffix rank \(m\in\{-1,\ldots,n-1\}\), each of the first \(\ell\) rows can be any subfamily of the \(c_m\) rank-at-least-\(m\) neighbourhoods, hence \((1+q_m)^{\ell}\) choices. The \(t\) stable rows must be nonempty and have least rank exactly \(m\), giving \(q_m^t-q_{m+1}^t\) choices. Sum over \(m\) and \(\ell\) and add the two boundary cases. Continual rows form precisely an initial zero block followed by a nonempty block, giving \(R_n\). This proves the formulas and the claimed boundary cases.

## Verification

An independent direct-semantics checker (`checker.cpp`) enumerates all \(2^{n2^n}\) concrete neighbourhood assignments on chains of \(n=1,2,3\) worlds; it evaluates every upward-closed propositional valuation and the full intuitionistic implication clause rather than the counting normal form. It obtains \(4,241,16690673\) valid frames respectively. It also compares the structural criterion with semantics on additional random chains. A separate Python checker (`verify_posets.py`) checks the semantics against SNDR on each of the 19 labelled three-world posets with random neighbourhoods, further random posets with four or five worlds, the strictness example, and every two-world partial-order frame. Execute:

```sh
c++ -O3 -std=c++17 checker.cpp -o checker && ./checker
python3 verify_posets.py
```

Both commands completed with the indicated `ALL_CHECKS_OK` and `ALL_POSET_CHECKS_OK` outputs. The computations are finite corroboration; arbitrary-world correctness follows from the proof above. The program requires a C++17 compiler and Python 3 but no third-party packages.

## Relationship to prior work

Dalmonte and de Groot (2026, arXiv:2606.31870, Definition 2.3 and Lemma 2.4) introduced the constructive-neighbourhood semantics used here and gave continual support as a **sufficient** frame condition for \(\mathsf I_{\Diamond}\). De Groot (arXiv:2507.13746; see its constructive-semantics discussion in Section 4) likewise uses continual frames for completeness; these claims do not provide a necessary-and-sufficient characterization of every concrete frame satisfying the axiom, or the labelled chain enumeration above. Dalmonte (arXiv:2210.09937) developed earlier Wijesekera-style neighborhood semantics, but considers different axioms and does not supply this census. The precise extension here is the SNDR converse, the strict three-world example, and the formula for all chain sizes. All of these refer to concrete neighbourhood families, not equivalence classes of their induced algebraic operators.

## Limitations

This theorem concerns the single interaction axiom \(\mathsf I_{\Diamond}\), not validity of every formula of the full logic or of its optional modal extensions. It does not yield a new decision procedure for the unrestricted logic. The enumeration counts labelled concrete frames on a *fixed total-order preorder*, with empty families and empty neighbourhoods allowed; it is not a count of frames up to isomorphism, nor of finite preorders in general. Historical priority of a differently worded correspondence is not independently certified. The source inspections and research-record comparisons are documented in `REVIEW.md` and `AUDIT.json`.

## References

1. T. Dalmonte and J. de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics*, arXiv:2606.31870v1 (first public 2026-06-30), https://arxiv.org/abs/2606.31870.
2. J. de Groot, *Intuitionistic monotone modal logic via translation*, arXiv:2507.13746 (first public 2025-07-18), https://arxiv.org/abs/2507.13746; subsequently *Journal of Logic and Computation* 36 (2026), exag017.
3. T. Dalmonte, *Wijesekera-style constructive modal logics*, arXiv:2210.09937v1 (2022), https://arxiv.org/abs/2210.09937.
