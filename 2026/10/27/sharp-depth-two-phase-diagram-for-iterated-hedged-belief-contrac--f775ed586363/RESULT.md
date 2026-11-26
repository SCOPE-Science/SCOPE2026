# Sharp stabilization times for truth-gated edge insertion with depth-two modal formulas

## Finding

In a finite one-agent Kripke model, fix a modal formula \(\varphi\). At each step add edges to every current falsifier of \(\varphi\) from every world where \(\varphi\) is currently true. Repeat until the accessibility relation stops changing. For \(n\ge3\), the maximum numbers of strict updates on \(n\) worlds are
\[
\begin{array}{c|cccc}
\varphi&\Diamond\Box p&\Box\Box p&\Diamond\Diamond p&\Box\Diamond p\\
\hline
\max h_\varphi&1&2&n-1&n.
\end{array}
\]
For \(n=1\) all four maxima are zero; for \(n=2\) all are one. This classification is for the **truth-gated** rule above, not for Belardinelli–Zhang contraction, which uses a belief gate.

## Assumptions and scope

The world set \(W\) is nonempty and finite. The initial accessibility relation \(R_0\subseteq W^2\) is arbitrary, and the valuation \(P=V(p)\) does not change. Boxes quantify over all successors and diamonds over some successor, including the usual vacuity conventions. In the model at step \(t\), let \(T_t=\{w:w\models\varphi\}\) and \(N_t=W\setminus T_t\). The synchronous update replaces \(R_t(w)\) by \(R_t(w)\cup N_t\) if \(w\in T_t\) and leaves it unchanged otherwise. Write \(h_\varphi=\min\{t\ge0:R_{t+1}=R_t\}\). The maxima allow all relations and valuations; worlds are never removed.

## Proof

If \(T_{t+1}=T_t\), then \(R_{t+2}=R_{t+1}\): every active row already contains the common falsifier set. Also an empty or full truth set forces a fixed point. A fixed relation remains fixed on all subsequent iterations. Define the inner truth sets
\[
G_t=\{w:R_t(w)\subseteq P\},\qquad D_t=\{w:R_t(w)\cap P\ne\varnothing\}.
\]
As the relation expands, \(G_t\) can only shrink and \(D_t\) can only grow.

### \(\Diamond\Box p\)

Initially false rows are unchanged at the first update and cannot become true because \(G_1\subseteq G_0\). If \(N_0\cap G_0\ne\varnothing\), a world in this intersection stays in \(G_1\) and becomes a successor of every active world, so all initially true worlds stay true. If \(N_0\cap G_0=\varnothing\) and \(N_0\subseteq P\), then \(G_1=G_0\) and initially true worlds again stay true. Otherwise \(G_0\subseteq T_0\) and the update adds a non-\(p\) successor to every world in \(G_0\), so \(G_1=T_1=\varnothing\). In each case there is at most one strict update. For every \(n\ge2\), let one world \(v\) see only itself, set \(P=\{v\}\), and give all other worlds no successors. Only \(v\) is initially true, and it adds every other world to its row.

### \(\Box\Box p\)

Again initially false rows cannot become true because their rows are unchanged and \(G_1\subseteq G_0\). If \(N_0\not\subseteq G_0\), every active row acquires a successor outside \(G_0\), hence outside \(G_1\), and \(T_1=\varnothing\). If \(N_0\subseteq G_0\cap P\), then \(G_1=G_0\) and \(T_1=T_0\). In the remaining case \(N_0\subseteq G_0\) but \(N_0\not\subseteq P\), each world of \(T_0\) receives a non-\(p\) successor and is outside \(G_1\). If \(T_1=T_0\), the first update is terminal. Otherwise any \(y\in T_0\setminus T_1\) is outside \(G_1\); the second update makes \(y\) a successor of every remaining true world, and \(y\) remains outside \(G_2\). Thus \(T_2=\varnothing\) and at most two strict updates occur.

For \(W=\{0,\ldots,n-1\}\), \(n\ge3\), take \(P=\{1\}\), \(R_0(0)=\varnothing\), \(R_0(1)=\{0\}\), and \(R_0(i)=\{1\}\) for all \(i\ge2\). Write \(C=\{2,\ldots,n-1\}\). Initially \(G_0=\{0\}\cup C\) and \(T_0=\{0,1\}\); the addition of \(C\) to both active rows gives \(G_1=C\) and \(T_1=\{0\}\). The next update adds 1 to row 0, strictly changing it, and \(T_2=\varnothing\).

### \(\Diamond\Diamond p\)

Here \(T_t=\{w:R_t(w)\cap D_t\ne\varnothing\}\) is increasing. A strict update requires \(T_t\ne\varnothing,W\); two successive strict updates require strict growth of \(T_t\) between them. Since the active truth-set sizes at strict updates must be distinct integers in \(\{1,\ldots,n-1\}\), there are at most \(n-1\) such updates.

For \(n\ge3\), take the directed cycle on \(\{0,\ldots,n-1\}\) with \(R_0(i)=\{(i+1)\bmod n\}\) and \(P=\{0\}\). For \(0\le t\le n-2\), put \(k=n-2-t\). Then
\[
D_t=\{k+1,\ldots,n-1\},\qquad T_t=\{k,\ldots,n-2\}.
\]
These identities hold at \(t=0\). When \(k>0\), world 0 is false and the update adds it to row \(k\), strictly changing that row. All other active rows are already in \(D_t\), so \(D_{t+1}=D_t\cup\{k\}\). By monotonicity, every currently false row has been unchanged up to this stage; of those rows, exactly \(k-1\) sees a member of \(D_{t+1}\), namely \(k\). This proves the induction. When \(k=0\), the only falsifier is \(n-1\). Row 0 was not previously active and has only successor 1, so the addition of \(n-1\) is strict. It does not enlarge \(D_t\); the row of \(n-1\) remains unchanged and sees only 0, outside \(D_t\). Thus the truth set is unchanged at this last strict update and the terminal falsifier set is \(\{n-1\}\). The total is \(n-1\) strict updates.

### \(\Box\Diamond p\)

Here \(T_t=\{w:R_t(w)\subseteq D_t\}\). Suppose a strict update leaves \(D_{t+1}=D_t\). If \(N_t\subseteq D_t\), the active rows stay true and the inactive rows stay false, by the unchanged inner set and the update rule. Otherwise every active row gains a target in \(N_t\setminus D_t\) and becomes false, while inactive rows remain false. Hence a strict update with no growth of \(D_t\) is terminal. If \(D_t\) becomes all of \(W\), no further strict update is possible. Thus either every strict update grows \(D_t\), yielding at most \(n\) strict updates, or at most \(n-1\) growth steps precede a final update with no growth.

For \(n\ge3\) take the directed path \(R_0(i)=\{i+1\}\) for \(i<n-1\), \(R_0(n-1)=\varnothing\), and \(P=\{0\}\). At stage \(t\) for \(0\le t\le n-1\), put \(k=n-1-t\). Inductively, rows \(i\le k\) are still original, and each row \(i>k\) equals \(W\setminus\{i\}\). Thus \(D_t=\{k+1,\ldots,n-1\}\). Row \(k\) is true (vacuously at \(t=0\)), rows \(i<k\) see a successor outside \(D_t\), and every row \(i>k\) sees 0 outside \(D_t\). The only active row is therefore \(k\); the update fills it to \(W\setminus\{k\}\), strictly, so the induction continues until \(k=0\) has also been updated. This gives \(n\) strict updates.

### Small sizes

For \(n=1\) every truth set is empty or full. For \(n=2\), a first strict update requires a singleton active world \(w\) and a missing edge \(w\to y\) to the other world. A second strict update would have to be from \(y\) to \(w\), because no other new edge could be added. If \(y\to w\) is already present, this is impossible. If it is absent, all worlds reachable from \(y\) are confined to \(\{y\}\), with its valuation and row unchanged by the first update, so \(y\) stays false. The one-step example for \(\Diamond\Box p\) also works for \(\Diamond\Diamond p\). For \(\Box\Box p\) take \(P=\varnothing\), \(R_0(0)=\varnothing\), \(R_0(1)=\{1\}\); for \(\Box\Diamond p\) take \(P=\varnothing\), \(R_0(0)=\varnothing\), \(R_0(1)=\{0\}\). In both examples the initially active row 0 gains successor 1.

## Verification

The companion `checker.py` specifies an exhaustive check on labelled relations and valuations for \(1\le n\le4\), and tests the uniform witness families for \(3\le n\le35\). It evaluates the truth-gated update, not the belief-gated contraction. The proof above supplies the uniform bounds and the terminal falsifier set of the cycle witness; finite counts alone do not establish them.

## Relationship to prior work and limitations

Belardinelli and Zhang, *Belief Contraction in Dynamic Epistemic Logic* ([arXiv:2606.31861](https://arxiv.org/abs/2606.31861), Definition 4.1), add the same false-content targets as this rule but activate a source that **believes** the content \(\theta\) (all its successors satisfy \(\theta\)), not one at which \(\theta\) is true. The source test and target predicate here are instead complementary truth sets of a single formula. The published result [*Sharp finite convergence of iterated possibility contraction*](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-finite-convergence-of-iterated-possibility-contraction--5680885de989/RESULT.md) uses the belief gate on content \(\Diamond p\). It shares the guard \(\Box\Diamond p\) and a sharp \(n\)-step directed-path lifetime with the last case above, but adds falsifiers of \(\Diamond p\) rather than of \(\Box\Diamond p\). For example, on the initial directed path above it adds a self-loop at the terminal vertex, which the truth-gated rule cannot do. Neither comparison gives a classification of the truth-gated rule for the four formulas. No assertion about repeated belief-gated contraction on those four contents, arbitrary modal depths, or multi-agent models is made.
