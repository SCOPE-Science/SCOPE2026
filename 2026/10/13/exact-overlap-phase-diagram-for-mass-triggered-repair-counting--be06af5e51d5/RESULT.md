# Exact overlap phase diagram for mass-triggered repair counting
## Finding
Consider a finite ordered family of integer intervals
\[
I_j=[u_j,v_j],\qquad j=1,\ldots,J,
\]
with checkpoints \(p_j\) and nonnegative weights \(h_1,\ldots,h_n\). Assume that \(u_j\le p_j\le v_j\), that
\[
u_{j+1}\ge p_j+1,
\]
that \(v_1<\cdots<v_J\), and that fixed constants \(L>0\) and \(U\ge0\) satisfy
\[
\sum_{t=u_j}^{v_j}h_t\ge L,
\qquad
\sum_{t=p_j+1}^{v_j}h_t\le U
\]
for every repair \(j\). Let
\[
M=\max_t\#\{j:t\in I_j\}
\]
be the maximum overlap multiplicity.

There is an exact phase diagram.

If \(L\le U\), no finite universal bound on \(M\) exists. If \(L>U\), then
\[
M\le 2+\left\lfloor\frac{U}{L-U}\right\rfloor,
\]
and this bound is sharp for every pair \((L,U)\). Moreover, the stronger consecutive-separation conclusion
\[
p_{j+1}>v_j\quad\text{for every }j
\]
is universally valid exactly when \(L>2U\).

The repair bookkeeping in Liu--Ye, *Silver Rate Is (Almost) Optimal for Gradient Descent: The Strongly Convex Case*, is the specialization
\[
L=S_0,\qquad U=\frac{S_0}{4}.
\]
Hence it lies strictly in the \(L>2U\) regime. Consecutive repairs satisfy \(p_{j+1}>v_j\), every index belongs to at most two repair intervals, and the counting conclusion
\[
\sum_{j=1}^J n_j\le2n,
\qquad n_j=v_j-u_j+1,
\]
follows. With the source bounds \(J\le B\) and \(n\le Bm\), concavity then gives
\[
\sum_{j=1}^J\log(n_j+1)\le B\log(2m+1).
\]
This removes the specific overlap-counting obstruction in Lemma 5.2; it does not assess unrelated arguments in that paper.

## Assumptions and scope
The statement is purely combinatorial. The weights are arbitrary nonnegative real numbers. Empty residual tails have mass zero. The interval endpoints and checkpoints are integer indices, and \(v_j\) is strictly increasing, as in the source where successive repairs terminate at successively later block ends. The condition \(u_{j+1}\ge p_j+1\) forces the checkpoints, and therefore the interval starts, to move strictly to the right.

The theorem classifies only what follows from the two mass inequalities and the ordering assumptions. It makes no assertion about how a repair is chosen, about the objective function in the optimization construction, or about the correctness of any theorem beyond the counting step to which these inequalities are applied.

## Proof
Assume first that \(L>U\), and put
\[
\delta=L-U>0,
\qquad
q=\left\lfloor\frac{U}{\delta}\right\rfloor.
\]
Fix an index \(t\) that belongs to \(r\) repair intervals. Because the starts and ends are both increasing, the repairs containing \(t\) form one consecutive run, say \(j,j+1,\ldots,j+r-1\).

For each interior repair \(k=j+1,\ldots,j+r-2\), its pre-checkpoint segment has mass at least
\[
\sum_{s=u_k}^{p_k}h_s
=
\sum_{s=u_k}^{v_k}h_s-
\sum_{s=p_k+1}^{v_k}h_s
\ge L-U=\delta.
\]
Since the next repair also contains \(t\),
\[
p_k<u_{k+1}\le t\le v_j.
\]
Since checkpoints increase, \(u_k\ge p_j+1\). Thus every segment \([u_k,p_k]\) lies inside the residual tail \([p_j+1,v_j]\) of the first repair. These interior pre-checkpoint segments are pairwise disjoint because \(u_{k+1}\ge p_k+1\). Consequently
\[
(r-2)\delta
\le
\sum_{s=p_j+1}^{v_j}h_s
\le U.
\]
Therefore
\[
r\le2+\left\lfloor\frac{U}{L-U}\right\rfloor.
\]
Taking the maximum over \(t\) proves the upper bound.

The bound is sharp. If \(q=0\), choose three indices with weights \(h_1=L\), \(h_2=0\), \(h_3=L\), and repairs
\[
(u_1,p_1,v_1)=(1,1,2),
\qquad
(u_2,p_2,v_2)=(2,3,3).
\]
Both mass conditions hold and the two intervals overlap at index \(2\).

Now suppose \(q\ge1\), and write
\[
U=q\delta+R,
\qquad 0\le R<\delta.
\]
On indices \(1,\ldots,2q+3\), set
\[
h_i=\delta\quad(1\le i\le q+1),
\qquad h_{q+2}=R,
\]
\[
h_i=\delta\quad(q+3\le i\le2q+2),
\qquad h_{2q+3}=R+\delta.
\]
For \(j=1,\ldots,q+1\), define
\[
(u_j,p_j,v_j)=(j,j,q+j+1).
\]
Each of these repairs has pre-checkpoint mass \(\delta\), residual-tail mass exactly \(U\), and total mass exactly \(L\). Add the last repair
\[
(u_{q+2},p_{q+2},v_{q+2})=(q+2,q+3,2q+3).
\]
Its residual-tail mass is exactly \(U\), while its pre-checkpoint mass is \(R+\delta\ge\delta\), so its total mass is at least \(L\). All \(q+2\) intervals contain index \(q+2\). Thus the upper bound is attained.

If \(L\le U\), fix any positive integer \(K\), put the only nonzero weight at index \(K+1\) with value \(L\), and use
\[
(u_j,p_j,v_j)=(j,j,K+j),
\qquad j=1,\ldots,K.
\]
Every repair has total mass \(L\), residual-tail mass \(L\le U\), and all \(K\) intervals contain index \(K+1\). Hence no finite universal multiplicity bound exists.

It remains to identify the stronger separation threshold. If \(p_{j+1}\le v_j\), then the pre-checkpoint segment of repair \(j+1\) is contained in the residual tail of repair \(j\). Its mass is at least \(L-U\), whereas that containing tail has mass at most \(U\). Therefore
\[
L-U\le U,
\]
so \(L\le2U\). The contrapositive proves universal separation when \(L>2U\).

Conversely, if \(U<L\le2U\), let \(\delta=L-U\) and choose weights
\[
h_1=U,\quad h_2=\delta,\quad h_3=0,\quad h_4=U.
\]
The repairs \((1,1,3)\) and \((2,3,4)\) satisfy all mass conditions but have \(p_2=v_1\), so strict separation fails. If \(L\le U\), take weights \(h_1=0\), \(h_2=L\), \(h_3=0\) and repairs \((1,1,2)\), \((2,2,3)\); again \(p_2=v_1\). Hence \(L>2U\) is necessary and sufficient.

For the Liu--Ye constants, \(L=S_0\) and \(U=S_0/4\), so \(L>2U\). Therefore \(p_{j+1}>v_j\), and then
\[
u_{j+2}\ge p_{j+1}+1>v_j.
\]
Thus nonadjacent repair intervals are disjoint and the overlap multiplicity is at most two, proving \(\sum_j n_j\le2n\). Finally Jensen's inequality gives
\[
\sum_{j=1}^J\log(n_j+1)
\le
J\log\!\left(1+\frac{2n}{J}\right).
\]
The function \(x\mapsto x\log(1+2n/x)\) is increasing for \(x>0\). Using \(J\le B\) and \(n\le Bm\) yields the displayed \(B\log(2m+1)\) bound.

## Verification
The bundled `verify.py` uses exact rational arithmetic to check the source specialization \((L,U)=(4,1)\), sharp constructions in several finite-overlap regimes, an arbitrarily long overlap example at \(L=U\), and a boundary example at \(L=2U\) where consecutive separation fails. These computations are finite sanity checks only. The universal upper bound, the unbounded regime, and the exact thresholds are proved analytically above.

## Relationship to prior work
Liu and Ye state the repair-trigger lower bound, the residual-tail cap, and the desired twofold-overlap counting lemma in Lemma 5.2 of arXiv:2609.26873v1. The written proof contains an overlap-counting step that has been publicly flagged as insufficient. A public Pith review of the paper also observes that the source's particular constants can be salvaged by comparing the next repair's pre-checkpoint mass \(3S_0/4\) with the previous residual tail \(S_0/4\). That special-case observation is therefore not claimed as new here.

The new statement is the parameterized and sharp classification: the exact finite-multiplicity regime is \(L>U\), the sharp multiplicity is \(2+\lfloor U/(L-U)\rfloor\), and the exact threshold for universal consecutive separation is \(L>2U\), with explicit examples at every boundary and in every phase. The smooth-convex silver-rate paper arXiv:2609.09152v2 and the checkpoint lower-bound paper arXiv:2609.04032v2 use related checkpoint constructions, but targeted full-text inspection did not locate this mass-triggered repair interval theorem or an implication-equivalent statement.

Targeted searches of published mathematical finding records for the exact formula, the ratio \(U/(L-U)\), repair-tail overlap, and the \(L>2U\) threshold returned no statement-equivalent or stronger result. The closest records concerned unrelated step-safety and overlap phenomena rather than this interval-mass classification.

## Limitations
The result repairs only the specific counting mechanism under the source's stated mass inequalities and ordering properties. It does not independently validate the source's hard-instance construction, its other lemmas, or its final lower bound. The special source-case mass comparison has already been noted publicly; originality here is restricted to the exact generalized phase diagram, sharp multiplicity formula, and sharp constructions. Literature searches cannot prove absolute uniqueness, so an uncatalogued equivalent combinatorial lemma remains a residual risk.

## References
1. K. Liu and Y. Ye, “Silver Rate Is (Almost) Optimal for Gradient Descent: The Strongly Convex Case,” arXiv:2609.26873v1, 2026. See Lemma 5.2 and equation (28).
2. Pith, public review of “Silver Rate Is (Almost) Optimal for Gradient Descent: The Strongly Convex Case,” paper identifier JUVW4DZL, 2026. See the discussion of Lemma 5.2 and its mass-based salvage.
3. Y. Ye and K. Liu, “Silver Rate Is (Almost) Optimal for Gradient Descent,” arXiv:2609.09152v2, 2026.
4. M. Jung, H. Cho, and C. Yun, “Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent,” arXiv:2609.04032v2, 2026.
