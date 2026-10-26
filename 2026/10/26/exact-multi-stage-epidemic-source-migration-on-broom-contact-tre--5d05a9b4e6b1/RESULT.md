# Exact multi-stage epidemic-source migration on broom contact trees

## Finding

On a broom-shaped contact tree, the mean size of an independent-edge outbreak has an exact multi-stage source-location phase diagram. With the definitions below, the unique optimal source visits consecutive handle vertices \(v_0,v_1,\ldots,v_R\), with one tie at each of the \(R\) strictly ordered transmission thresholds. Since \(R\) can be arbitrarily large, arbitrarily many genuinely intermediate optimal sources occur even on trees.

The thresholds are the unique numbers \(t_j\in(0,1)\) satisfying
\[
\sum_{a=0}^{L-2j-2}t_j^a=m,\qquad j=0,\ldots,R-1,
\]
where \(R=\max\{0,\lfloor(L-m)/2\rfloor}\). They obey \(t_0<t_1<\cdots<t_{R-1}\). Define \(t_{-1}=0\), \(t_R=1\). For each \(j=0,\ldots,R\), vertex \(v_j\) uniquely maximizes expected outbreak size when \(t_{j-1}<p<t_j\). At \(p=t_j\), exactly the adjacent pair \(v_j,v_{j+1}\) maximizes. If \(R=0\), the hub uniquely maximizes throughout \(0<p<1\). All additional pendant leaves are strictly suboptimal.

## Assumptions and scope

Let \(m\ge2\) and \(L\ge1\) be integers. The broom \(B_{m,L}\) has handle vertices \(v_0,\ldots,v_L\) joined by consecutive edges and additional leaves \(w_1,\ldots,w_m\) adjacent only to hub \(v_0\). Each edge is independently retained with common probability \(0<p<1\). An outbreak starting from a single source spreads through every retained edge in the source's connected component, with no transmissions across deleted edges. The objective is the **population expectation** of final outbreak size \(E_s(p)\), not an estimate based on finite observations. Since the underlying graph is a tree, the probability of connecting a source to a target is exactly \(p\) raised to their graph distance. There is no independent-reinfection or nonlinear epidemic mechanism in this model.

## Proof

**Step 1: exact outbreak means.** Since the unique path between vertices at distance \(d\) survives with probability \(p^d\), linearity of expectation gives
\[
E_{v_j}(p)=\sum_{i=0}^L p^{|i-j|}+mp^{j+1},\qquad 0\le j\le L.
\]
For each pendant leaf \(w\),
\[
E_w(p)=1+p+\sum_{i=1}^L p^{i+1}+(m-1)p^2.
\]
Consequently
\[
E_{v_0}(p)-E_w(p)=(1-p)\left[(m-1)p+\sum_{i=1}^L p^i\right]>0.
\]
Thus none of the added leaves can maximize.

**Step 2: adjacent handle differences.** Direct subtraction of the first display gives the exact identity
\[
E_{v_{j+1}}(p)-E_{v_j}(p)=p^{j+1}\big[1-p^{L-2j-1}-m(1-p)\big],\qquad 0\le j<L.
\]
Write \(k=L-2j-1\). If \(k\le0\), the bracket is strictly negative because \(p^k\ge1\). If \(1\le k\le m\), the difference equals \(p^{j+1}(1-p)(\sum_{a=0}^{k-1}p^a-m)<0\). If \(k>m\), then \(S_k(p)=\sum_{a=0}^{k-1}p^a\) increases strictly from \(1\) to \(k\) as \(p\) increases from \(0\) to \(1\). Hence there is a unique \(t\in(0,1)\) with \(S_k(t)=m\); the adjacent difference is negative before \(t\), zero at \(t\), and positive after \(t\).

**Step 3: count and order all switches.** The condition \(L-2j-1>m\) holds precisely for the consecutive indices \(j=0,\ldots,R-1\), where \(R=\max\{0,\lfloor(L-m)/2\rfloor}\). For consecutive such indices \(k_j=L-2j-1\) and \(k_{j+1}=k_j-2\). At every \(0<p<1\), \(S_{k_j}(p)>S_{k_{j+1}}(p)\). Therefore, their unique level-\(m\) crossings satisfy \(t_j<t_{j+1}\). For any \(t_{j-1}<p<t_j\), the differences \(E_{v_{a+1}}-E_{v_a}\) are strictly positive for \(a<j\) and strictly negative for \(a\ge j\). This proves that \(v_j\) is the unique maximizer. At \(p=t_j\), only difference \(a=j\) vanishes, giving exactly two neighboring maximizers. The leaf comparison from Step 1 completes the classification.

**Step 4: unlimited intermediate phases.** Fix \(m=2\) and choose \(L=2r+2\) with any integer \(r\ge2\). Then \(R=r\), so \(r+1\) distinct handle vertices are uniquely optimal on nonempty open intervals. All but the initial hub and eventual terminal source are intermediate phase optimizers. This yields an unbounded number of transitions.

## Verification

The accompanying standalone `verify.py` enumerates all independent edge-survival states for \(m\in\{2,3,4\}\), \(L\in\{1,\ldots,6\}\), and five rational transmission probabilities. It independently recomputes every component expectation and checks the formula, adjacent differences, and predicted maximizers. It also brackets the algebraic transition thresholds over an additional finite parameter range using rational bisection and confirms strict ordering. Run `python verify.py` with Python 3; its exact deterministic output is recorded in `certificate.json`. The finite checks do not substitute for the analytical proof for arbitrary \(m,L,p\).

For \(m=2,L=6\), the two successive thresholds solve \(1+t+\cdots+t^4=2\) and \(1+t+t^2=2\), approximately \(0.5187900637\) and \(0.6180339887\), so the maximizer changes from \(v_0\) to \(v_1\) to \(v_2\).

## Relationship to prior work

The outbreak expectation on trees coincides up to the harmless source-self term with **decay centrality**, a well-established graph invariant. Tsakas (2016) proves that degree-maximizing vertices dominate for sufficiently low decay and closeness-maximizing vertices dominate sufficiently near one, with sufficient intermediate comparisons; neither those general asymptotic statements nor their numeric observations supply the precise multi-switch broom phase diagram and all algebraic thresholds above. Coroničová Hurajová, Gago, and Madaras (2018) investigate changing decay-centrality rankings, but full-text coverage of their article was not established here, so potential overlap under generalized-closeness terminology remains a bibliographic risk. Riveros, Salas, and Skibski (2023) analyze abstract tree-rooting behavior; their explicit observation that decay centrality is not a general tree-rooting measure does not classify the parameter-dependent maximizer on this graph family. The stochastic outbreak interpretation is a standard unique-path reduction, not a claim to a new model or new definition of decay centrality.

## Limitations

Independent, homogeneous, static edge retention on finite trees is essential. This does not cover cycles, reinfection, time-varying transmission, random contact networks, heterogeneous probabilities, extinction risk, variance of outbreak size, or identification from finite samples. The theorem is a special-family complete phase classification, not a universal result for all trees. A result equivalent under generalized closeness or percolation terminology in uninspected literature may exist; separate bibliographic and independent mathematical auditing remain necessary.

## References

1. N. Tsakas, *On Decay Centrality*, first public arXiv version 19 April 2016, arXiv:1604.05582, https://arxiv.org/pdf/1604.05582.
2. J. Coroničová Hurajová, S. Gago, and T. Madaras, *On decay centrality in graphs*, Mathematica Scandinavica **123** (2018), 39–50, doi:10.7146/math.scand.a-106210.
3. C. Riveros, J. Salas, and O. Skibski, *How Do Centrality Measures Choose the Root of Trees?*, ICDT 2023, doi:10.4230/LIPIcs.ICDT.2023.12, https://drops.dagstuhl.de/storage/00lipics/lipics-vol255-icdt2023/LIPIcs.ICDT.2023.12/LIPIcs.ICDT.2023.12.pdf.
