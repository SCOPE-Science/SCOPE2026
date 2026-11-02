# Two-leader phase transitions on weighted friendship graphs

## Finding

Let \(m\ge2\) be an integer and \(t>0\). Form the friendship graph \(F_m(t)\) from \(m\) edge-disjoint triangles sharing one hub \(o\); give every hub-to-periphery edge conductance \(1\), and every edge joining the two peripheral vertices of a triangle conductance \(t\). Select exactly two distinct vertices as perfectly grounded, noise-free leaders, with every other vertex a follower. For the weighted combinatorial Laplacian \(L\), minimize
\[
J(S)=\operatorname{tr}\!\left(L_{V\setminus S,V\setminus S}^{-1}\right),\qquad |S|=2.
\]
Every minimizing set is specified by the following classification, and there are no others.

- For \(m=2\), all minimizers use the hub and one peripheral vertex if \(0<t<1/3\); both these sets and sets using peripheral vertices from two distinct triangles minimize if \(t=1/3\); only two-different-triangle peripheral pairs minimize if \(t>1/3\).
- For \(m=3\), the same alternatives hold with critical conductance \(t=3\).
- For every \(m\ge4\) and every \(t>0\), precisely the hub-plus-one-peripheral pairs minimize.

The minimizer counts are respectively \(2m\) for hub-plus-peripheral, \(2m(m-1)\) for different-triangle peripheral pairs, and their sum at a threshold. Two peripheral leaders within the same triangle are never optimal for \(t>0\).

More precisely, all leader pairs fall into three automorphism classes, with exact objective values
\[
\begin{aligned}
A_m(t)&=\frac1{1+t}+(m-1)\left(1+\frac1{1+2t}\right),\\
B_m(t)&=A_m(t)+\frac{2mt+2m-t-3}{2(1+t)},\\
C_m(t)&=A_m(t)+\frac{(2m-7)t+2m-3}{2(1+2t)}.
\end{aligned}
\]
Here \(A\) means hub plus one peripheral, \(B\) two peripheral vertices of the same triangle, and \(C\) two peripheral vertices of different triangles. Thus the minimum is exactly \(\min\{A_m(t),C_m(t)\}\).

## Assumptions and scope

There are exactly \(2m+1\) vertices, no self-loops, independent edge disturbances of equal intensity in the usual noise-free-leader interpretation, and an undirected weighted combinatorial Laplacian. The parameter \(t\) is finite and strictly positive; the conductance \(1\) of every hub edge fixes the global time scale. The claim concerns exactly two perfectly grounded leaders and the first inverse power of the grounded Laplacian, not finite leader gains, squared inverses, directed edges, or arbitrary triangle-dependent conductances. Since every proper grounded principal Laplacian is positive definite on this connected graph, every objective is finite.

## Proof

Every automorphism permutes the \(m\) triangles and may exchange the two vertices in each triangle. Accordingly, unordered pairs of distinct vertices have exactly the three orbit types \(A,B,C\) stated above. Put
\[
H=\begin{pmatrix}1+t&-t\\-t&1+t\end{pmatrix},\quad
H^{-1}\binom11=\binom11,\quad
\operatorname{tr}H^{-1}=1+\frac1{1+2t}.
\]

For type \(A\), the hub is grounded. One triangle has a single ungrounded vertex, with grounded diagonal \(1+t\), and each other triangle contributes an independent \(H\) block. The trace of the inverse is therefore \(A_m(t)\).

For type \(B\), both peripheral vertices in one triangle are grounded, leaving the hub and \(m-1\) intact peripheral pairs. The follower matrix has hub diagonal \(2m\), \(m-1\) diagonal blocks \(H\), and hub-to-block off-diagonal vector \((-1,-1)\). The hub Schur complement is
\[
s_B=2m-2(m-1)=2.
\]
Using the block inverse formula, the inverse trace is
\[
J_B=(m-1)\operatorname{tr}H^{-1}+s_B^{-1}\bigl(1+2(m-1)\bigr)
=2m-\frac32+\frac{m-1}{1+2t},
\]
which equals \(B_m(t)\).

For type \(C\), one peripheral vertex is grounded in each of two different triangles, so two follower blocks are scalar \(1+t\), while the remaining \(m-2\) blocks are \(H\). Their coupling vectors to the follower hub are respectively \((-1)\) and \((-1,-1)\). The hub Schur complement is
\[
s_C=2m-\frac{2}{1+t}-2(m-2)=4-\frac2{1+t}>0.
\]
The block inverse formula gives
\[
J_C=\frac2{1+t}+(m-2)\left(1+\frac1{1+2t}\right)
+\frac{2m-3+2/(1+t)^2}{4-2/(1+t)}=C_m(t).
\]

Direct rational simplification yields the two exact comparisons
\[
B_m(t)-C_m(t)=\frac{t(2mt+2m+5t+3)}{2(1+t)(1+2t)}>0
\]
and
\[
C_m(t)-A_m(t)=\frac{(2m-7)t+2m-3}{2(1+2t)}.
\]
For \(m=2\), the last numerator is \(1-3t\); for \(m=3\), it is \(3-t\); and for \(m\ge4\), it is strictly positive. All inequalities are exact on the stated integer and positive-real domains. Since the three orbit types exhaust all leader pairs, these comparisons prove the entire classification, all equality cases, and the minimizer counts.

## Verification

Run `python3 verify.py` using Python 3's standard library. The program reconstructs each full weighted Laplacian from its edge list, removes both leader rows and columns, and obtains exact rational traces by an independent Gauss-Jordan inverse. It tests all unordered leader pairs for \(m=2,\ldots,7\) at five rational values of \(t\), covering both critical conductances exactly, and tests representative pairs for \(m=2,\ldots,11\) at three additional rational values. The accompanying `verification_output.txt` records results from executing the supplied program. These finite checks are corroboration, not the proof for all \(m\) and real \(t\).

## Relationship to prior work

Fitch and Leonard formulate weighted noisy-consensus leader selection and derive general joint-centrality criteria, with explicit path and cycle results; their mathematical framework motivates the inverse-grounded-Laplacian objective. A previously investigated unweighted windmill classification concerns the isolated value \(t=1\), which does not imply the two conductance thresholds or the all-\(t\) rigidity when \(m\ge4\). Sun, Li, and Liu study first-order and leader-follower coherence on windmill-type graphs; their abstract indicates special-family exact solutions. The accessible evidence does not establish the specific continuous-conductance phase classification here, but an inaccessible full-text comparison leaves a meaningful priority risk. This result establishes a direct formula and a classification; it does not assert absolute priority.

## Limitations

The transition structure relies on the equal unit hub conductances and a common positive peripheral-edge conductance \(t\). It does not classify heterogeneous triangle weights, more than two leaders, or finite-strength leaders. The nearest windmill-specific source was available as metadata and abstract rather than a verifiable full-text comparison; specialist prior coverage remains possible. No independent audit has been performed.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first publicly posted July 7, 2014, https://arxiv.org/abs/1407.1569 .
2. W. Sun, Y. Li, and S. Liu, *Noisy consensus dynamics in windmill-type graphs*, Chaos 30 (2020), 123131, https://doi.org/10.1063/5.0020696 .
