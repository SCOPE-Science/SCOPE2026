# Sharp logarithmic discrepancy envelopes for generalized hiccup complements

## Finding
For fixed integers \(k\ge2\) and \(x\ge3\), consider the increasing integer sequence \(g\) with \(g(1)=x\) and, for \(j\ge2\),
\[
g(j)-g(j-1)=\begin{cases}1,&j\in\{g(1),\ldots,g(j-1)\},\\ k+1,&j\notin\{g(1),\ldots,g(j-1)\}.\end{cases}
\]
Let \(U(n)\) count the positive integers at most \(n\) absent from the range of \(g\). Put \(D(n)=kU(n)-(k-1)n\), \(q=x-2\), and for integers \(h\ge0\),
\[
L_h=\frac{k^{h+1}-1}{k-1},\qquad T_h=1+\sum_{j=0}^{h-1}(qL_j+1).
\]
(The empty sum is zero, so \(T_0=1\).) Then the **exact discrepancy extrema at every full hierarchical stage** are
\[
\boxed{\max_{T_h\le n\le T_{h+1}}D(n)=q+1+qh,}
\]
\[
\boxed{\min_{T_h\le n\le T_{h+1}}D(n)
=\min\{1+h(q-k+1),\,1+(h+1)(q-k+1)\}.}
\]
In particular, the complement has density \((k-1)/k\), and its logarithmic discrepancy has sharp and generally unequal extremal slopes:
\[
\boxed{\liminf_{n\to\infty}\frac{D(n)}{\log_k n}=x-k-1,\quad
\limsup_{n\to\infty}\frac{D(n)}{\log_k n}=x-2.}
\]
Both limits range over **all positive integers**, without selecting a probability distribution or subsequence. For example, when \(x=k+1\), the lower slope is zero but the upper slope equals \(k-1\).

## Assumptions and scope
The parameters \(k,x\) are fixed positive integers satisfying \(k\ge2\) and \(x\ge3\). Every occurrence of \(n\) denotes a positive integer, and \(\log_k\) denotes the real logarithm to base \(k\) (used for \(n>1\)). The finite-stage maxima and minima include both endpoints; the common endpoint can belong to two adjacent stages. The case \(x=2\) is excluded, since it has a finite complement and a different discrepancy scale. No uniform estimate when \(k\) or \(x\) varies with \(n\) is asserted.

## Proof
**1. Exact characteristic word.** In Proposition 4.3 of Cloitre's *Counting with Hiccup Sequences* [1], the characteristic word of the integers absent from the values of \(g\), encoding absence by \(0\) and presence by \(1\), is proved to be
\[
\mathcal W=0\prod_{h\ge0}(W_h^{\,q}1),\qquad W_0=0,\quad W_{h+1}=W_h^{\,k}1.
\]
We use this established identification, rather than assuming a correspondence from finite data. Induction gives \(|W_h|=L_h\). Consequently the first \(T_h\) letters are the initial \(0\) followed by all stages of indices smaller than \(h\).

**2. Prefix weight induction.** Give each symbol \(0\) weight \(+1\) and each \(1\) weight \(-(k-1)\). Thus \(D(n)\) equals the total weight of the first \(n\) symbols of \(\mathcal W\). Let \(P_h(t)\) be the weight of the first \(t\) letters of \(W_h\), for \(0\le t\le L_h\). We claim
\[
P_h(L_h)=1,\quad\min_{0\le t\le L_h}P_h(t)=0,\quad
\max_{0\le t\le L_h}P_h(t)=1+h(k-1).
\]
For \(h=0\), the only weights are \(0,1\). If the claims hold for \(h\), in \(W_{h+1}=W_h^{\,k}1\) the successive copies of \(W_h\) have starting weights \(0,1,\ldots,k-1\); their prefix minima stay nonnegative and their maximum is \((k-1)+1+h(k-1)\). The terminal \(1\) has weight \(-(k-1)\), returning the total from \(k\) to \(1\). This proves all three claims at height \(h+1\). For explicit attainment, the first maximum is attained at index \(u_h\), where \(u_0=1\) and \(u_{h+1}=(k-1)L_h+u_h\). In particular, \(1\le u_h\le L_h\).

**3. Exact extrema on a stage.** The initial \(0\) has weight \(+1\), and each stage \(W_h^q1\) has total weight \(q-(k-1)\). Therefore
\[
D(T_h)=1+h(q-k+1),\quad D(T_{h+1})=1+(h+1)(q-k+1).
\]
Inside the stage, the \(q\) successive copies of \(W_h\) begin at offsets \(0,1,\ldots,q-1\); their nonnegative prefix weights peak in the final copy, at offset \((q-1)+(1+h(k-1))\). The final stage symbol has negative weight \(-(k-1)\). Thus the whole stage's maximum is
\[
1+h(q-k+1)+(q-1)+1+h(k-1)=q+1+qh,
\]
attained at index \(R_h=T_h+(q-1)L_h+u_h\). Every prefix within the \(q\) copies has weight at least the initial stage weight, while the last symbol can only decrease the value. The smallest value is therefore at one of the two stage endpoints. This proves both displayed finite-stage identities, including \(q=1\) and \(q<k-1\).

**4. Sharp logarithmic limits.** Since \(k\ge2\) and \(q\ge1\) are fixed, \(L_h\asymp k^h\), and the stage-boundary positions \(T_h,T_{h+1}\), and maximum-attaining positions \(R_h\) all satisfy \(\log_k n=h+O_{k,q}(1)\) as \(h\to\infty\). The finite-stage maxima give the global upper bound and an infinite attaining subsequence, yielding \(\limsup D(n)/\log_k n=q\). The finite-stage minima give a lower bound and an attaining sequence of endpoints, yielding \(\liminf D(n)/\log_k n=q-k+1\). Both imply \(D(n)=O_{k,q}(\log n)\); using \(U(n)=((k-1)n+D(n))/k\) proves \(U(n)/n\to(k-1)/k\).

## Verification
The accompanying standalone `verify.py` independently generates finite prefixes from the defining recurrence for \(g\) and from the postorder word. It checks exact agreement, total weights, all single-block prefix extrema, maximum-attaining indices, and both stage extrema for \(k\in\{2,3,4,5\}\), \(x\in\{3,4,5,6,7,8\}\), and a range of hierarchical stages. Execute `python3 verify.py`; the expected terminal marker is `VERIFY_OK`. The program tests finite instances only; the proof above establishes the infinite assertions.

## Relationship to prior work
The **characteristic-word identity** is Proposition 4.3 of Cloitre [1] and is explicitly attributed there to the morphism construction of Fokkink and Joshi [2]. Cloitre also proves a nested recurrence for \(U(n)\) in Proposition 4.2. Ruskey and Deugau [3] derive exact inverse-position formulas in Theorems 25 and 27 for their shifted \(k\)-ary meta-Fibonacci families, as well as a first-order density asymptotic (Theorem 28). Theorem 31 identifies their special Cloitre--Sloane recursion, corresponding here to \(x=k+1\). Their stronger digit-sum position identities make part of that special case potentially inferable; they do not directly state this theorem's two-parameter stage-by-stage extrema for all \(x\). The new claim is the precise **deterministic** stage-extremal profile and the exact lower and upper logarithmic slopes for all the stated parameters. Their derivation uses a weighted-prefix calculation that is not an explicit consequence of a density asymptotic alone; in the special \(x=k+1\) case, exact position formulas from [3] provide a stronger possible route to the same extrema, an overlap acknowledged here. The established normal-limit theorem for uniformly sampled indices concerns typical indices; it implies neither of these pointwise extremal constants, and the constants alone imply no normal law. The OEIS entry [4] gives an example of the underlying integer sequence but not the two-parameter stage-extremal theorem.

## Limitations
The stage-word identity is an existing substantive input, not reproved here. No claim is made for varying \(k,x\), for \(x=2\), or about finer fluctuations inside the gap between the two extremal logarithmic slopes. Although the inspected sources do not state this pointwise extremal result, earlier unindexed deductions from the same morphism remain an originality risk. The known exact inverse-position formulas for the special parameter \(x=k+1\) may already imply its logarithmic envelopes after additional extremal analysis; no claim is made that the special case alone is independently novel. The theorem is a deterministic extremal complement to distributional or first-order density information, not an independent rediscovery of the characteristic word.

## References
[1] B. Cloitre, *Counting with Hiccup Sequences*, arXiv:2610.13908v1 (first public version October 9, 2026), Sections 4.1--4.2, Propositions 4.2--4.3, https://arxiv.org/html/2610.13908v1.

[2] R. Fokkink and G. Joshi, *On Cloitre's hiccup sequences*, arXiv:2507.16956v4, Section 2, Lemma 5, https://arxiv.org/html/2507.16956v4.

[3] F. Ruskey and C. Deugau, *The Combinatorics of Certain k-ary Meta-Fibonacci Sequences*, Journal of Integer Sequences 12 (2009), Article 09.4.3, https://cs.uwaterloo.ca/journals/JIS/VOL12/Ruskey/ruskey6.pdf (Sections 6.3, 6.4, 7; Theorems 25, 27, 28, 31).

[4] OEIS Foundation, A045412, https://oeis.org/A045412.

[5] B. Cloitre, *A study of a family of self-referential sequences*, arXiv:2506.18103v2, https://arxiv.org/html/2506.18103v2.
