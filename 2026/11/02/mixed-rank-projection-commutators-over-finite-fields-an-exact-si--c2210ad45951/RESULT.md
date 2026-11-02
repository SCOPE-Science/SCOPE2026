# Mixed-rank projection commutators over finite fields: an exact similarity census

## Finding
Let \(q\) be any prime power and let \(n,r\) be integers satisfying \(n\ge4\) and \(2\le r\le n-2\). Set \(s=n-r\) and, for each integer \(m\ge1\), define
\[
U_m=(q^m-1)q^{m-1},\qquad W_m=(q^m-1)(q^{m-1}-1).
\]
Fix **any** rank-\(r\) idempotent \(Q\in M_n(\mathbb F_q)\). Among the rank-one idempotents \(P\in M_n(\mathbb F_q)\), classify the ordered pair of invariants \((\alpha,C)\), where \(\alpha=\operatorname{tr}(PQ)\in\mathbb F_q\) and \(C=PQ-QP\). The following table gives the **exact number of \(P\) for each fixed \(Q\)**, together with the complete similarity type of \(C\):

| Product trace | Similarity type of \(C\) | Number |
| --- | --- | ---: |
| \(\alpha=0\) | \(0_n\) | \(U_s/(q-1)\) |
| \(\alpha=0\) | \(J_2(0)\oplus0_{n-2}\) | \(2(q^r-1)U_s/(q-1)\) |
| \(\alpha=0\) | \(J_3(0)\oplus0_{n-3}\) | \(W_rU_s/(q-1)\) |
| \(\alpha=1\) | \(0_n\) | \(U_r/(q-1)\) |
| \(\alpha=1\) | \(J_2(0)\oplus0_{n-2}\) | \(2(q^s-1)U_r/(q-1)\) |
| \(\alpha=1\) | \(J_3(0)\oplus0_{n-3}\) | \(W_sU_r/(q-1)\) |
| each \(\alpha\notin\{0,1\}\) | \(C_2(t^2-\alpha(\alpha-1))\oplus0_{n-2}\) | \(U_rU_s/(q-1)\) |

Here \(J_j(0)\) is one nilpotent Jordan block of size \(j\), and \(C_2(f)\) denotes the \(2\)-by-\(2\) companion matrix of the monic quadratic \(f\). **No separability assumption is made**: in characteristic two the quadratic may be a square, and the stated companion block remains correct.

The product also obeys \[(PQ)^2=\alpha PQ,\] so the same trace parameter detects square-zero products (\(\alpha=0\)), idempotent products (\(\alpha=1\)), and products with nontrivial periodic powers (\(\alpha\notin\{0,1\}\)).

The number of rank-\(r\) idempotents \(Q\) is \({n\brack r}_q q^{r(n-r)}\). Multiplying each table entry by this number gives the exact number of **ordered pairs** \((P,Q)\) with the stated invariants. To aggregate across product traces into ordinary similarity types, sum the last-row multiplicity over the actual roots \(\alpha\in\mathbb F_q\setminus\{0,1\}\) of \(\alpha(\alpha-1)=\delta\), for the desired \(\delta\ne0\).

As a consequence, a uniformly random rank-one idempotent commutes with the fixed \(Q\) with exact probability
\[
\frac{U_r+U_s}{q^{n-1}(q^n-1)}.
\]
For each fixed \(q\) and \(r\ge2\), as \(s\to\infty\), the rank of its commutator converges in law to \(\operatorname{Binomial}(2,1-q^{-r})\). In particular, the commuting probability converges to \(q^{-2r}\). If both \(r\) and \(s\) tend to infinity, the commutator has rank two with probability tending to one.

## Assumptions and scope
All matrices act linearly on \(\mathbb F_q^n\); **idempotent** means \(P^2=P\), not an orthogonal/Hermitian projection. The integer ranks are genuine matrix ranks, whereas \(\alpha\) is a field element. Every prime power is admitted, including even characteristic. A rank-one idempotent is nonzero by definition. The theorem concerns \(2\le r\le n-2\), because the rank-one-versus-rank-one edge is already represented by earlier work. The formulas themselves remain algebraically meaningful at both boundary ranks, but no originality is claimed there.

## Proof
Every idempotent of rank \(r\) is conjugate to \(Q=\operatorname{diag}(I_r,0_s)\). Conjugating both factors preserves \(\alpha\), the rank of \(C\), and the similarity class of \(C\); it therefore suffices to treat that diagonal \(Q\). Every rank-one idempotent has the representation \(P=uv^\top\) with \(v^\top u=1\). Exactly \(q-1\) pairs \((u,v)\) yield each \(P\), via \((u,v)\mapsto(cu,c^{-1}v)\) for \(c\ne0\). Decompose
\[
u=(a,b)\in\mathbb F_q^r\oplus\mathbb F_q^s,\qquad
v=(c,d)\in\mathbb F_q^r\oplus\mathbb F_q^s.
\]
Define \(\alpha=c^\top a\) and \(\beta=d^\top b=1-\alpha\). A direct multiplication gives
\[
C=PQ-QP=\begin{pmatrix}0&-ad^\top\\bc^\top&0\end{pmatrix},\quad
C^2=-\begin{pmatrix}\beta ac^\top&0\\0&\alpha bd^\top\end{pmatrix},\quad
C^3=\alpha(\alpha-1)C.
\]
The two nonzero off-diagonal blocks have disjoint target summands, so
\[
\operatorname{rank}C={\bf1}_{a\ne0,\ d\ne0}+{\bf1}_{b\ne0,\ c\ne0}.
\]
If \(\alpha\notin\{0,1\}\), then all four vectors \(a,b,c,d\) are nonzero and \(C\) has rank two. Its image is \(\langle(a,0),(0,b)\rangle\). On this invariant two-space, \(C\) has a nonscalar, off-diagonal \(2\)-by-\(2\) matrix with square \(\alpha(\alpha-1)I_2\); it is cyclic with characteristic polynomial \(t^2-\alpha(\alpha-1)\). Since this polynomial has nonzero constant term, the remaining kernel splits as an invariant zero summand. This gives its claimed companion block (including inseparable characteristic-two cases).

If \(\alpha\in\{0,1\}\), the cubic identity makes \(C\) nilpotent with index at most three. If its rank is zero the type is \(0_n\); if its rank is one then \(C^2=0\), yielding \(J_2(0)\oplus0_{n-2}\). For rank two with \(\alpha=0\), both \(a,c\ne0\) and \(\beta=1\), so \(C^2\) contains the nonzero block \(-ac^\top\). Similarly, if \(\alpha=1\), both \(b,d\ne0\) and the lower block \(-bd^\top\) of \(C^2\) is nonzero. Thus rank two has nilpotency index three and type \(J_3(0)\oplus0_{n-3}\).

For a positive integer \(m\), the number of ordered vector/covector pairs \((x,y)\in\mathbb F_q^m\times(\mathbb F_q^m)^*\) with \(y(x)=t\ne0\) is \(U_m\): choose nonzero \(x\) and one of \(q^{m-1}\) solutions \(y\). When \(t=0\), the possibilities divide into four disjoint classes: \((x,y)=(0,0)\), counted once; exactly one of \(x,y\) zero, counted \(q^m-1\) times for each choice; and both nonzero, counted \(W_m\). Indeed the latter count is \((q^m-1)(q^{m-1}-1)\). For \(\alpha=0\) the \((a,c)\)-pair has dot product zero while \((b,d)\) has dot product one. The corresponding three zero-status cases for \((a,c)\) give respectively \(U_s\), \(2(q^r-1)U_s\), and \(W_rU_s\) choices of \((u,v)\); dividing by \(q-1\) yields the first three table rows. The \(\alpha=1\) rows follow by exchanging \(r\) with \(s\). For each other fixed \(\alpha\), both dot products are nonzero, giving \(U_rU_s\) representatives and hence \(U_rU_s/(q-1)\) distinct \(P\). This proves the table.

A rank-\(r\) idempotent specifies an ordered decomposition into image and kernel of dimensions \(r\) and \(s\), so its number is \({n\brack r}_q q^{rs}\). Summing the table over traces and types produces exactly \(q^{n-1}(q^n-1)/(q-1)\) rank-one idempotents, independently of \(r\). The zero-commutator rows yield the commuting probability. Finally, divide the rank-zero, rank-one and rank-two counts by this total, hold \(q,r\) fixed, and let \(s\to\infty\): their respective limits are \(q^{-2r}\), \(2q^{-r}(1-q^{-r})\), and \((1-q^{-r})^2\). By symmetry in \(r,s\), if both grow, the rank-two probability tends to one.

## Verification
The standalone `verify.py` enumerates normalized rank-one idempotents for \((q,n,r)=(2,4,2),(3,4,2),(4,4,2),(5,4,2),(2,5,2),(2,5,3),(3,5,2),(3,5,3),(2,6,2),(2,6,3),(2,6,4)\). It checks all table counts, totals and complement symmetry; for \(n\le4\) it explicitly multiplies matrices, calculates commutator ranks and verifies the cubic identity and nilpotent-index distinctions. The \(q=4\) case uses direct arithmetic in \(\mathbb F_2[t]/(t^2+t+1)\). Execute `python verify.py` using Python 3. The reproduced output ends with `VERIFY_OK all mixed-rank projection counts and cubic laws`. Finite checks support but do not establish unrestricted validity, which follows from the proof.

## Relationship to prior work
Ferraz–Polcino Milies–Taufer (2017) count idempotent generators of each fixed-rank left ideal of a finite-field matrix ring; those counts supply the one-element context, not a joint trace-and-commutator similarity distribution. Britnell–Wildon (2010/2011) study which similarity classes admit commuting representatives, rather than exact multiplicities within a rank-one-versus-rank-\(r\) pair, product traces, or the displayed probabilistic limit. An existing narrower result determines the bracket similarity law when **both** factors have rank one. The present theorem does not claim that boundary case: it classifies all higher interior ranks \(2\le r\le n-2\) and resolves the new rank-versus-corank dependence, including the limiting binomial law. These prior results do not state or by themselves imply the displayed interior-rank counts; the proof here is independent of any assertion of publication priority.

## Limitations
No independent audit or exhaustive publication-priority certification has been performed. A differently parameterized enumeration in the matrix-semigroup or projection-geometry literature remains possible. The method explicitly relies on one factor having rank one; it does **not** classify pairs of two arbitrary interior ranks. No asymptotic rate is asserted in the joint regime where both ranks tend to infinity beyond convergence of the rank-two probability to one. The finite verifier does not constitute a proof for general prime powers or dimensions.

## References
1. R. A. Ferraz, C. Polcino Milies and E. Taufer, *Left ideals in matrix rings over finite fields*, initial arXiv version 25 November 2017, arXiv:1711.09289, https://arxiv.org/abs/1711.09289.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (6 January 2010), *J. London Math. Soc.* 83 (2011), 470–492, https://arxiv.org/abs/1001.0811.
