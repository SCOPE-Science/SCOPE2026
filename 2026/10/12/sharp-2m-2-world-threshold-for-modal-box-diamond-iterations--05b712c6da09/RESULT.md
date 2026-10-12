# Sharp \(2m+2\)-world threshold for modal box–diamond iterations

## Finding

For each integer \(m\ge 1\), define the variable-free classical modal formula
\[
\alpha_m=(\Box\Diamond)^m\top,
\]
where \(\alpha_0=\top\). Over the class of all nonempty finite Kripke frames with an arbitrary binary accessibility relation, **the least cardinality of a frame invalidating** \(\alpha_m\leftrightarrow\alpha_{m+1}\) **is exactly** \(2m+2\). Equivalently, the two formulas agree at every world on every frame with at most \(2m+1\) worlds, but disagree at the initial world of the directed path on \(2m+2\) worlds.

The lower bound follows from a more informative fact, valid also on infinite frames: if a world first falsifies an iteration at stage \(k\ge1\), there exist \(k\) distinct worlds of finite failure ranks \(1,\ldots,k\) and \(k\) further distinct worlds which never falsify any finite iteration. The latter are forced by successive universal-successor witnesses and cannot be reused across ranks.

## Assumptions and scope

A Kripke frame is \(F=(W,R)\), where \(W\ne\varnothing\) and \(R\subseteq W\times W\) is arbitrary, with no reflexivity, seriality or transitivity assumption. Write \(R[x]=\{y\in W:xRy\}\). The usual normal modal clauses are used: \(\Box\varphi\) holds at \(x\) if all members of \(R[x]\) satisfy \(\varphi\), and \(\Diamond\varphi\) holds if some member does. In particular, a dead end satisfies every boxed formula and no diamond formula. There are no propositional variables in \(\alpha_m\), so valuations do not affect the result.

For any frame, set \(B_0=\varnothing\) and recursively define
\[
B_{j+1}=\{x\in W:\exists y\in R[x]\quad R[y]\subseteq B_j\},\qquad j\ge0.
\]
The modal satisfaction clauses give \(B_j=\{x:F,x\not\models\alpha_j\}\). Since the defining operator is monotone and \(B_0\subseteq B_1\), the sets \(B_j\) are increasing. Let \(U=\bigcup_{j\ge0}B_j\), and for \(x\in U\) define its *failure rank* as the least \(k\ge1\) with \(x\in B_k\). Points outside \(U\) have infinite failure rank.

## Proof

**Rank-core lemma.** Every \(x\in U\) has at least one successor outside \(U\). Suppose otherwise, and choose a counterexample \(x\in U\) of smallest finite failure rank \(k\), so \(R[x]\subseteq U\). Because \(x\in B_k\), there is a point \(y\in R[x]\) such that \(R[y]\subseteq B_{k-1}\). Our assumption on \(x\) places \(y\) in \(U\). Let \(\ell\) be the failure rank of \(y\). By the definition of \(B_\ell\), some \(z\in R[y]\) has \(R[z]\subseteq B_{\ell-1}\subseteq U\). But \(z\in R[y]\subseteq B_{k-1}\), so \(z\in U\) and its failure rank is at most \(k-1\). Hence \(z\) is a counterexample of smaller rank, a contradiction. This proves the lemma; the argument needs no finiteness assumption.

**Two distinct points per failure rank.** Suppose \(x_k\in B_k\setminus B_{k-1}\), with \(k\ge1\). Recursively for \(j=k,k-1,\ldots,1\), choose \(y_{j-1}\in R[x_j]\) such that
\[
R[y_{j-1}]\subseteq B_{j-1}.
\]
If \(j\ge2\), it is impossible that \(R[y_{j-1}]\subseteq B_{j-2}\), because that would imply \(x_j\in B_{j-1}\). Thus one may also choose
\[
x_{j-1}\in R[y_{j-1}]\cap(B_{j-1}\setminus B_{j-2}).
\]
When \(j=1\), the chosen \(y_0\) is a dead end. The points \(x_1,\ldots,x_k\) are distinct because their failure ranks are \(1,\ldots,k\).

Each \(y_i\) has \(R[y_i]\subseteq B_i\subseteq U\). By the rank-core lemma, \(y_i\notin U\); hence none of the \(y_i\) can equal any \(x_j\). The \(y_i\) are pairwise distinct as well: for \(i\ge1\), their successor sets are contained in \(B_i\) but not \(B_{i-1}\), whereas \(R[y_0]=\varnothing\). If \(i<j\), then \(R[y_i]\subseteq B_i\subseteq B_{j-1}\) but \(R[y_j]\not\subseteq B_{j-1}\), so \(y_i\ne y_j\). We have therefore exhibited \(2k\) distinct points of \(W\). In particular, failure of \(\alpha_m\leftrightarrow\alpha_{m+1}\) entails a point in \(B_{m+1}\setminus B_m\), and hence \(|W|\ge2m+2\). Here we used \(B_m\subseteq B_{m+1}\), so the biconditional can fail only by \(\alpha_m\) being true and \(\alpha_{m+1}\) false.

**Sharpness.** Consider the path with vertices \(0,1,\ldots,2m+1\), whose only arrows are \(iR(i+1)\) for \(i<2m+1\). At a vertex having exactly \(r\) edges remaining before the terminal dead end, \(\alpha_j\) is false precisely when
\[
r\in\{1,3,5,\ldots,2j-1\}.
\]
Indeed, \(\alpha_0\) is everywhere true, the terminal point satisfies every \(\alpha_j\), the point one edge before it falsifies every \(\alpha_j\) with \(j\ge1\), and for \(r\ge2\) the truth of \(\alpha_{j+1}\) at distance \(r\) equals that of \(\alpha_j\) at distance \(r-2\). Induction gives the displayed failure distances. The path's initial point has \(r=2m+1\), so it satisfies \(\alpha_m\) and falsifies \(\alpha_{m+1}\). This supplies the matching \(2m+2\)-world upper bound.

## Verification

The accompanying standard-library Python program `verify_rank.py` independently computes the failure sets via the existential/universal predecessor recurrence and the modal truth sets via direct \(\Box\)-then-\(\Diamond\) evaluation. It checks their equality, the rank-core lemma, and explicit distinct-witness extraction. Run:

```text
python3 verify_rank.py
```

The run completed with `VERIFY_OK`: all \(66{,}066\) labeled relations on one through four worlds were exhaustively checked (counts \(2,16,512,65{,}536\)), along with \(9{,}000\) reproducibly sampled relations on five through ten worlds. Directed-path examples were checked for \(m=0,1,\ldots,50\). This evidence tests the definitions and sharpness constructions; the preceding rank argument, not these finite computations, proves the theorem for every \(m\).

## Relationship to prior work

Alpay and Basaran (2026, arXiv:2606.15437) introduce semantic mirages measured by their first separating frame size. Their Proposition 5 certifies the \(m=2\) instance, and Lemma 2 constructs a separating directed path of size \(2m+2\) for every \(m\ge1\). Their Table 3 establishes the matching minimum by bounded SAT certificates for \(m=1,2,3\), while explicitly not extending minimality to arbitrary \(m\). The new step here is a universal lower bound, proved through the finite-rank/infinite-rank witness separation, so that the known path upper bound is exact for every positive \(m\). The already certified small cases are included in, not claimed separately from, this theorem.

Standard bisimulation-depth and filtration results concern fixed-model observations or generic finite countermodel upper bounds; they do not themselves give this exact cardinality for the indicated variable-free pair. The theorem is about ordinary \(\mathsf K\)-frames and makes no modal \(\mu\)-calculus hierarchy claim.

## Limitations

No claim is made about the least distinguishing size for arbitrary modal-formula pairs or for other frame classes such as serial, reflexive or transitive frames. In particular the directed-path witnesses are not reflexive or serial. The proof also does not classify every isomorphism type of minimal separating frame. The novelty comparison is relative to the inspected primary article and searched literature: an equivalent old result phrased in terms of alternating predecessor attractors or game ranks cannot be completely excluded. Independent scholarly validation has not been conducted.

## References

1. F. Alpay and B. Basaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437 (first version, June 13, 2026), especially Section 7, Proposition 5, Lemma 2, Table 3. https://arxiv.org/abs/2606.15437
2. P. Blackburn, M. de Rijke and Y. Venema, *Modal Logic*, Cambridge University Press (2001). Background for standard Kripke modal semantics and finite-model methods.
