# Affine threshold and unbounded non-contingency cycles on binary-successor frames

## Finding

Let \(F=(W,R)\) be any finite nonempty Kripke frame, with \(|W|=n\). For an event \(X\subseteq W\), define the usual non-contingency (knowing-whether) operation
\[
\Delta_R(X)=\{w\in W:R(w)\subseteq X\ \text{or}\ R(w)\cap X=\varnothing\},
\qquad R(w)=\{v:wRv\}.
\]
Identify events with vectors in \(\mathbb F_2^n\). The operation \(\Delta_R:\mathbb F_2^n\to\mathbb F_2^n\) is affine over \(\mathbb F_2\) **if and only if** every world has at most two distinct successors. This is a sharp algebraic-degree threshold: a world with exactly \(r\ge2\) successors has local non-contingency coordinate of algebraic normal-form degree exactly \(r-1\), whereas worlds with zero or one successor yield the constant \(1\).

In that affine class, form the matrix \(B\in M_n(\mathbb F_2)\) whose row at \(w\) has ones exactly in the two successor columns if \(|R(w)|=2\), and is zero otherwise. Write \(\boldsymbol1\) for the all-one vector. Then for every \(x\in\mathbb F_2^n\) and integer \(k\ge1\),
\[
\boxed{\Delta_R^{\,k}(x)=\boldsymbol1+B^k x.}
\]
Define \(a\ge1\) as the smallest integer satisfying \(\operatorname{rank}(B^a)=\operatorname{rank}(B^{a+1})\), and put \(U=\operatorname{im}(B^a)\). The restriction \(B_U=B|_U\) is invertible. Put \(p=\operatorname{ord}(B_U)\), adopting \(p=1\) if \(U=0\). Then \(a\) is the **least uniform eventual preperiod**, and \(p\) is its **least eventual period**:
\[
\boxed{\Delta_R^{\,k+p'}=\Delta_R^{\,k}\ \text{on every event}\iff
k\ge a\ \text{and}\ p\mid p'}
\]
for all integers \(k\ge1\), \(p'\ge1\).

The smallest size at which a nontrivial eventual period is possible is \(n=3\): the three successor sets \(\{0,1\},\{1,2\},\{0,2\}\) give \((a,p)=(1,3)\). Moreover, the periods are **unbounded despite the two-successor restriction**. For every odd integer \(n\ge3\), the relation \(R(i)=\{i,i+1\pmod n\}\) has \(a=1\) and period \(p\ge n-1\).

## Assumptions and scope

The frame is finite and nonempty; its accessibility relation is arbitrary and may have self-loops and empty successor sets. Events range over **all** \(2^n\) valuations of one propositional atom. Equality of operator iterates means equality of functions on the entire event algebra, not merely equality for a selected input. The Boolean affine and polynomial degrees are over \(\mathbb F_2\). No reflexivity, symmetry, transitivity or seriality assumption is imposed. The unbounded-period family concerns separate finite frames of increasing odd cardinality; no statement about a single infinite frame is made.

## Proof

**Step 1: exact local Boolean polynomial.** Let \(r=|R(w)|\) and name the distinct successor bits \(x_1,\ldots,x_r\). When \(r=0\) or \(r=1\), the bits vacuously or necessarily agree, so the output bit is \(1\). For \(r\ge2\), over \(\mathbb F_2\) the two disjoint all-equal cases give
\[
f_r(x_1,\ldots,x_r)=\prod_{i=1}^{r}x_i+\prod_{i=1}^{r}(1+x_i)
=1+\sum_{\varnothing\ne S\subsetneq\{1,\ldots,r\}}\prod_{i\in S}x_i.
\]
Every degree-\(r-1\) monomial occurs with coefficient \(1\), so \(\deg f_r=r-1\). Algebraic normal forms of Boolean functions are unique. A vector-valued Boolean function is affine exactly when every coordinate has degree at most one. Hence the claimed **if and only if** follows, including the boundary cases \(r=0,1,2,3\). Distinct successor variables prevent identification-induced cancellation.

**Step 2: iterate the affine operation.** Under the two-successor bound, Step 1 gives the rowwise identity \(\Delta_R(x)=\boldsymbol1+Bx\). Each row of \(B\) has either zero or two ones, hence \(B\boldsymbol1=0\). Induction on \(k\) yields \(\Delta_R^{\,k}(x)=\boldsymbol1+B^k x\) for all \(k\ge1\). The same equality holds when some rows have no successors.

**Step 3: exact least preperiod and period.** The image chain \(\operatorname{im}B\supseteq\operatorname{im}B^2\supseteq\cdots\) stabilizes. At its first stabilization index \(a\ge1\), let \(U=\operatorname{im}B^a\). Then \(BU=U\), so \(B_U\) is invertible by finite dimensionality. Also
\(\mathbb F_2^n=\ker(B^a)\oplus U\): the intersection is zero because \(B|_U\) is invertible, and dimensions sum to \(n\). The restriction of \(B\) to \(\ker B^a\) is nilpotent with index exactly \(a\). For \(k<a\), ranks of \(B^k\) and \(B^{k+p'}\) differ for every \(p'\ge1\), making operator equality impossible. For \(k\ge a\), the nilpotent summand vanishes and \(B^k\) is onto \(U\), so \(B^{k+p'}=B^k\) exactly when \(B_U^{p'}=I_U\), equivalent to \(p\mid p'\). Equality of the two powers is equivalent to equality of the two affine iterates by Step 2. This proves minimality in both coordinates, including \(U=0\).

**Step 4: sharp three-world onset.** Since \(B\boldsymbol1=0\), its stable image has dimension at most \(n-1\). For \(n\le2\), the invertible part therefore has dimension at most one, and every invertible \(\mathbb F_2\)-linear map in that dimension is the identity; thus \(p=1\). On \(W=\{0,1,2\}\) with rows \(R(0)=\{0,1\}\), \(R(1)=\{1,2\}\), \(R(2)=\{0,2\}\), the matrix is
\[
B=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.
\]
Direct multiplication gives \(B^4=B\) but \(B^2\ne B\) and \(B^3\ne B\); also \(\operatorname{rank}B=\operatorname{rank}B^2=2\). The characterization in Step 3 yields \((a,p)=(1,3)\).

**Step 5: arbitrarily long periods.** For odd \(n\ge3\), let \(P\) cyclically permute the \(n\) coordinates, and take \(B=I+P\). Each row has exactly two ones, so it is the matrix of the stated frame. A coordinate vector is cyclic for \(P\), so its minimal polynomial is \(t^n-1\) in \(\mathbb F_2[t]\). Translation \(P=B+I\) gives \(m_B(t)=(t+1)^n-1\). Since \(n\) is odd, \(m_B(t)=t g(t)\), where \(g(0)=1\) and \(\deg g=n-1\). The zero root has multiplicity exactly one; by the coprime primary decomposition, \(a=1\) and the minimal polynomial of \(B_U\) is exactly \(g\). If its finite order is \(p\), then \(g(t)\mid(t^p-1)\). Comparing degrees forces \(p\ge n-1\), proving unboundedness. For illustration, the periods at odd sizes \(3,5,7,9\) are respectively \(3,15,7,63\); the growth lower bound, not these examples, is proved for every odd size.

## Verification

The accompanying standalone standard-library script `verify_delta_affine.py` independently evaluates the semantic agreement condition on all valuations, multiplies bit matrices, identifies first repeated powers, computes the Fitting rank index, and compares the predicted affine iteration with direct non-contingency iteration. The script exhausts all **15,002** frames with one through four labelled worlds and successor sets of size at most two, comprising **237,068** frame/valuation pairs; it also checks all local algebraic normal-form degrees for \(0\le r\le6\), all possible one- and two-world frames, and four odd cyclic examples up to nine worlds. Run `python3 verify_delta_affine.py` and expect `VERIFY_OK`. The general claims are consequences of the symbolic proof; finite tests are cross-checks only.

## Relationship to prior work

Non-contingency semantics and its proof-theoretic treatment are established in Sierra Miranda--Wang--Zenger [1]. Humberstone [2] formalized agreement and non-contingency, while Fan--Wang--van Ditmarsch [3] developed knowing-whether logics. Those papers supply the broader semantic setting, **not** a claim of discovery here. The novel claim assessed here concerns the *exact Boolean-affine branching threshold*, *complete uniform eventual dynamics for every finite binary-successor frame*, and *unbounded periods witnessed by odd cyclic frames*. Ordinary Boolean algebraic normal forms and the Fitting decomposition are classical ingredients, not independently new results. Known stabilization on finite transitive frames is compatible: the odd cycle frames in Step 5 are generally nontransitive and exhibit periodic rather than eventually constant behavior.

## Limitations

The theorem addresses iteration of one non-contingency operator on event truth sets, not arbitrary Boolean combinations of modal formulas, general modal axiomatizations, or infinite-state dynamics. The matrix construction requires at most two successors; for higher branching the polynomial has nonlinear coordinates and these linear-dynamics conclusions cannot be inferred. Broad historical agreement/knowing-whether literature may contain equivalent statements not found by targeted searches. In particular, a full-document implication comparison against every older treatment is not claimed; the scientific novelty assessment remains provisional until independent literature review.

## References

[1] B. Sierra Miranda, Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975v1, first submitted 30 September 2026, https://arxiv.org/abs/2609.38975 (semantic Definition 1 and labelled proof systems).

[2] L. Humberstone, *The Modal Logic of Agreement and Noncontingency*, Notre Dame Journal of Formal Logic **43** (2002), 95–127, https://doi.org/10.1305/ndjfl/1071509431.

[3] J. Fan, Y. Wang and H. van Ditmarsch, *Contingency and Knowing Whether*, Review of Symbolic Logic **8** (2015), 75–107, https://doi.org/10.1017/S1755020314000343.
