# A connected three-agent counterexample to a repulsive-confidence diameter conjecture

## Finding

For the signed, one-dimensional, synchronous bounded-confidence model of Kann and Feng (2023), the **diameter inequality proposed as Theorem 4.11** is false, even when the underlying graph is connected, the process converges after one update, and both attractive and repulsive edges occur.

More precisely, consider the connected three-vertex path \(0-1-2\) with a repulsive edge \(\{0,1\}\), an attractive edge \(\{1,2\}\), and confidence radius \(c=1\). With initial opinions
\[
(x_0(0),x_1(0),x_2(0))=(0,\tfrac14,\tfrac74),
\]
the process freezes after exactly one update at
\[
(x_0(t),x_1(t),x_2(t))=(-\tfrac38,\tfrac58,\tfrac74)\quad(t\ge1).
\]
There are \(m=2\) edges. The initial diameter is \(7/4\), whereas the terminal diameter is \(17/8\); hence
\[
\operatorname{diam}(x(\infty))=\tfrac{17}{8}
>2=\max\{\operatorname{diam}(x(0)),mc\}.
\]
This contradicts the universally quantified diameter **conjecture**, without making any assertion against its separate conjectural claim that all model trajectories converge.

In fact, the obstruction persists throughout an open two-parameter family. For any \(c>0\), \(0<a<1\), and \((3+a)/2<b<2\), start with
\[
(x_0(0),x_1(0),x_2(0))=c(0,a,b).
\]
The process freezes after one step, and its terminal diameter exceeds the claimed bound by the strictly positive amount
\[
\operatorname{diam}(x(\infty))-\max\{\operatorname{diam}(x(0)),2c\}
=c\left(b-\frac{3+a}{2}\right)>0.
\]
The excess has supremum \(c/2\) **within this specified open family**. The three-agent size is minimal for a connected-graph counterexample: the two-agent inequality is established by Kann and Feng, Proposition 4.1.

## Assumptions and scope

The graph is a fixed undirected signed graph with signed adjacency \(A_{ii}=1\) (self-weight), \(A_{01}=A_{10}=-1\), \(A_{12}=A_{21}=+1\), and other off-diagonal entries zero. At time \(t\), only neighbors satisfying the **strict** condition \(|x_j(t)-x_i(t)|<c\) enter the update. The update is exactly equations (3.1) and (3.2) of Kann and Feng: a receptive attractive neighbor contributes its own opinion, and a receptive repulsive neighbor contributes an extrapolated opinion \(x_j-c\) when \(x_j>x_i\), or \(x_j+c\) when \(x_j<x_i\). Agent \(i\) averages these contributions together with its own opinion. Equal-opinion repulsive ties are defined in the source, but none occur in the stated initial conditions or their active interactions.

The claim concerns deterministic synchronous iterations, scalar real opinions, positive \(c\), and finite graphs with the stated signs. It does not assert a universal replacement diameter bound for other graphs or confidence conventions.

## Proof

For the open family, the initial repulsive gap is \(ac<c\), while the initial attractive gap is \((b-a)c>c\) because \(b>(3+a)/2\) and \(a<1\). Consequently, only edge \(\{0,1\}\) contributes at the first update. Equation (3.2), including self-weights, gives
\[
\begin{aligned}
x_0(1)&=\tfrac12\bigl(0+(ac-c)\bigr)=\tfrac{a-1}{2}c,\\
x_1(1)&=\tfrac12\bigl(ac+(0+c)\bigr)=\tfrac{a+1}{2}c,\\
x_2(1)&=bc.
\end{aligned}
\]
At time one, the repulsive gap equals \(c\) **exactly**, and is therefore no longer receptive because the source uses \(<c\), not \(\le c\). The attractive gap is
\[
 x_2(1)-x_1(1)=\left(b-\tfrac{a+1}{2}\right)c>c.
\]
Thus both nonloop edges are inactive. Self-weights alone leave every opinion unchanged, proving \(x(t)=x(1)\) for all integer \(t\ge1\).

The initial width is \(bc<2c\). In the final state the opinion order is \(x_0(1)<x_1(1)<x_2(1)\), and
\[
\operatorname{diam}(x(1))=\left(b+\frac{1-a}{2}\right)c.
\]
Subtracting \(2c\) yields \(c(b-(3+a)/2)>0\). The supremum of this excess over the displayed parameter domain is \(c/2\), approached as \(a\downarrow0\), \(b\uparrow2\), but not attained within the open domain. At \(a=1/4\), \(b=7/4\), and \(c=1\), the stated rational witness follows. Finally, Kann and Feng prove the required upper bound for two agents in Proposition 4.1 of their source, so no smaller connected graph can refute the proposed universal inequality.

## Verification

Execute the standalone `verify.py` with Python 3. It independently implements the original signed-increment rule (3.1)–(3.2) and the equivalent receptive-neighbor averaging rule, compares them on exact rational test states, checks the rational witness, and tests rational members of the full open family. Exact arithmetic is used throughout. These computations check transcription and representative cases; the preceding symbolic argument proves the infinite parameter family.

## Relationship to prior work

Kann and Feng (2023) define the model in equations (3.1)–(3.2), prove the two-agent bound in Proposition 4.1, and prove diameter results for all-repulsive graphs. Their page 14 (Theorem 4.11) explicitly marks the mixed-sign, general-graph bound as suspected from numerics and does not provide a proof. The present example falsifies only its diameter clause in the mixed-sign case; it is not a correction to their proven all-repulsive result. Previous signed bounded-confidence variants and the unsigned bounded-confidence survey use different interaction formulas and do not by themselves establish this counterexample.

## Limitations

This result neither establishes nor refutes convergence for all initial conditions. The path's *underlying graph* is connected, but its initially receptive subgraph has an isolated third node; a conjecture additionally requiring initial receptive connectivity is a different, untested statement. Strict confidence is essential to immediate freezing of the repulsive edge at gap exactly \(c\). The \(c/2\) supremum is only for the specified family, not a general extremal theorem over all signed graphs. A complete independent publication-priority investigation has not been performed.

## References

- C. Kann and M. Feng, *Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1 (first public posting 2023-01-05), especially equations (3.1)–(3.2), Proposition 4.1 and proposed Theorem 4.11. https://arxiv.org/pdf/2301.02210
- C. Bernardo, C. Altafini, A. V. Proskurnikov and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302. https://doi.org/10.1016/j.automatica.2023.111302
- Related distinct discrete-time signed bounded-confidence model, Neurocomputing article (2020), DOI:10.1016/j.neucom.2019.12.061; only bibliographic and abstract material was available for comparison. https://doi.org/10.1016/j.neucom.2019.12.061
