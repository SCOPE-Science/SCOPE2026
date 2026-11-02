# Rational forcing-set generating functions for alternating-matching temporal paths

## Finding

For each integer \(n\ge 2\) and horizon \(T\ge 1\), put vertices \(1,\ldots,n\) in a path. At odd rounds activate just the disjoint edges \(\{1,2\},\{3,4\},\ldots\); at even rounds activate just \(\{2,3\},\{4,5\},\ldots\). Starting with a chosen blue set, apply one simultaneous layer-local zero-forcing round per snapshot: a blue vertex with precisely one white neighbor in the current snapshot makes it blue at the end of that round. Since each snapshot is a matching, this means that any active edge with a blue endpoint has both endpoints blue after the round.

Let \(F_{n,T}(z)=\sum_{S}z^{|S|}\), summing over **all labelled initial sets** \(S\subseteq\{1,\ldots,n\}\) that turn every vertex blue by time \(T\). Introduce formal variables \(x,z\), and write
\[
 p=\left\lfloor\frac{T-1}{2}\right\rfloor,\quad
 r=\left\lfloor\frac T2\right\rfloor,\quad
 W(z)=2z+z^2,\quad
 A_p(x)=\sum_{a=0}^{p}x^a,\quad
 B_r(x)=\sum_{b=1}^{r}x^b,\quad
 G_T(x)=\sum_{d=1}^{T}x^d.
\]
The empty sum \(B_0(x)\) is zero. As identities of formal series in \(x\) with coefficients in \(\mathbb Z[z]\), the entire two-parameter family of forcing-set polynomials is determined by
\[
 \boxed{\displaystyle\sum_{m\ge1}F_{2m,T}(z)x^m
 =\frac{xW(z)A_p(x)^2}{1-W(z)G_T(x)}},
\]
\[
 \boxed{\displaystyle\sum_{m\ge0}F_{2m+1,T}(z)x^m
 =\frac{A_p(x)\bigl(z+W(z)B_r(x)\bigr)}{1-W(z)G_T(x)}}.
\]
For the second series only, the auxiliary one-vertex case is defined by \(F_{1,T}(z)=z\). No interpretation of an edge-bearing path is needed at one vertex.

In particular the least exponent with nonzero coefficient is
\[
 s_{n,T}=\begin{cases}
 \left\lceil\frac{n}{2T}\right\rceil,&T\text{ odd},\\[2pt]
 \left\lceil\frac{n+1}{2T}\right\rceil,&T\text{ even}.
 \end{cases}
\]
Thus the temporal scheduling phase creates a genuine boundary-parity penalty at horizons such as \(n=2T\). For fixed \(n=2T\), one source suffices precisely when \(T\) is odd.

The number \(M_{n,T}\) of **minimum-cardinality labelled forcing sets** is also exact. With \(s=s_{n,T}\),
\[
 M_{2m,T}=2^s[x^{m-1}]A_p(x)^2G_T(x)^{s-1},
\]
\[
 M_{2m+1,T}=2^{s-1}[x^m]A_p(x)G_T(x)^{s-1}\bigl(1+2B_r(x)\bigr).
\]
The rational generating functions and these multiplicities, rather than previously investigated scalar zero-forcing numbers, are the principal enumerative claims. For example, \(F_{8,2}(z)=16z^3+40z^4+44z^5+26z^6+8z^7+z^8\): exactly 16 three-source initial sets succeed after two rounds on eight vertices. If each vertex is independently seeded with probability \(\theta\in(0,1)\), the exact probability of complete infection by \(T\) is \((1-\theta)^nF_{n,T}(\theta/(1-\theta))\), so the full polynomial has a direct reliability interpretation.

## Assumptions and scope

All graphs are finite, undirected and loopless; labels, round parity, and the starting time are fixed. For \(T\ge2\), the union of snapshots is the ordinary path on \(n\) vertices. For \(T=1\), the union consists only of disjoint odd-edge pairs; this boundary case is included explicitly. The forcing rule is **layer-local**, evaluated against the matching active in that round, not against the union graph and not allowing an infection created within a round to force again in that same round. All initially blue vertices remain blue. Formulas count distinct labelled initial sets, not subsets up to reflection or symmetry.

## Proof

**1. Single-source intervals and superposition.** Work first on the doubly infinite path. Starting with a single blue vertex \(2j+1\), the successive infected intervals after \(t\ge1\) rounds are
\[
 [2j+2-t,\ 2j+1+t].
\]
Starting at its partner \(2j+2\) gives **the same interval** after the first round, and hence after every later round. This follows by induction: at each successive alternating matching, the two current boundary vertices have active edges pointing outward, and the interior stays blue. On the finite path, intersect the interval with \([1,n]\); no exterior vertex is needed for infection within the path. Because a matching propagates infection across an edge whenever either endpoint is blue, each round commutes with unions of blue sets. Consequently, the final blue set from arbitrary seeds is exactly the union of these single-source intervals.

Group vertices in blocks \(Q_j=\{2j+1,2j+2\}\cap[1,n]\), for \(0\le j< L=\lceil n/2\rceil\). The last block is a singleton if \(n\) is odd. A block is selected when it contains one or more seeds. Any nonempty selection inside the same full block produces the same final influence interval, namely
\[
 I_j=[2j+2-T,\ 2j+1+T]\cap[1,n].
\]
The weight-generating polynomial for a selected full block is \(2z+z^2=W(z)\), while that for a selected final singleton is \(z\).

**2. Exact block-gap criterion.** Let \(j_1<\cdots<j_s\) be all selected block indices. The intervals \(I_j\) have left and right endpoints strictly increasing with \(j\), and each contains its own seed. Their union covers the path if and only if its first interval reaches vertex 1, its last interval reaches vertex \(n\), and consecutive intervals touch or overlap. Written arithmetically, these conditions are
\[
 j_1\le p=\left\lfloor\frac{T-1}{2}\right\rfloor,
 \qquad j_{i+1}-j_i\le T\quad(1\le i<s),
\]
\[
 j_s\ge \begin{cases}L-1-p,&n\text{ even},\\ L-1-r,&n\text{ odd}.
 \end{cases}
\]
There are no further constraints: any gap between selected intervals occurs inside the path, because both intervals contain a selected path vertex. This supplies a necessary-and-sufficient combinatorial characterization of **every** time-\(T\) forcing set.

**3. Rational enumeration: even vertex count.** Write \(n=2m\), so \(L=m\) and all blocks have weight \(W(z)\). A valid ordered selection is specified uniquely by its first offset \(a=j_1\in[0,p]\), last offset \(b=(m-1)-j_s\in[0,p]\), and the positive internal gaps \(d_i=j_{i+1}-j_i\in[1,T]\). Their relation is \(m=1+a+b+\sum_i d_i\). With \(s\) selected blocks its weight is \(W(z)^s\). Summing over all \(s\ge1\), offsets and gaps gives
\[
 \sum_{m\ge1}F_{2m,T}(z)x^m
 =xW(z)A_p(x)^2\sum_{s\ge1}\bigl(W(z)G_T(x)\bigr)^{s-1},
\]
which is the first displayed rational function.

**4. Rational enumeration: odd vertex count.** Write \(n=2m+1\). There are \(m\) complete blocks and one final singleton. Let \(b=m-j_s\) be the right-end offset. The block-gap criterion requires \(0\le b\le r\). If \(b=0\), the final singleton is selected, contributes \(z\), and all preceding selected blocks contribute \(W(z)\). If \(1\le b\le r\), all selected blocks are complete and each contributes \(W(z)\). With \(m=a+b+\sum_i d_i\), the geometric-series sum is
\[
 A_p(x)\bigl(z+W(z)B_r(x)\bigr)
 \sum_{k\ge0}\bigl(W(z)G_T(x)\bigr)^k,
\]
proving the second displayed rational function, including \(m=0\).

**5. Exact minimum and its multiplicity.** Each distinct chosen block requires at least one initial seed. If \(L=\lceil n/2\rceil\), the boundary and gap constraints imply
\[
 L-1\le p+r_n+(s-1)T,
 \qquad r_n=\begin{cases}p,&n\text{ even},\\r,&n\text{ odd}.
 \end{cases}
\]
Together with \(s\ge1\), this gives the stated ceilings for both parities of \(T\). They are attained by selecting the leftmost permissible block \(\min\{p,L-1\}\) and advancing in positive steps of at most \(T\) until the right threshold is reached. Thus every minimum initial set has exactly one seed in each of its \(s\) selected blocks. In the even case there are two choices per block and the offsets-and-gap equation yields the coefficient formula for \(M_{2m,T}\). In the odd case, selecting the last singleton contributes one choice (right offset zero), while ending at a complete block contributes two (right offset between 1 and \(r\)), giving the formula for \(M_{2m+1,T}\).

This is a universal proof for all admissible \(n,T\). The finite tests in the verifier are corroborative only.

## Verification

The self-contained Python 3 script `verify.py` reproduces the finite comparisons from the original graph snapshots, without consulting a symbolic proof oracle or using external dependencies. Run `python3 verify.py`. It independently checks all \(2^n\) initial subsets for each \(2\le n\le14\) and \(1\le T\le10\), comparing direct synchronous dynamics against the block criterion; compares the full size polynomial against both a block enumeration and the displayed rational generating functions; checks the exact minimum and minimum-set coefficient formulas; and separately tests the \(n=2T\) parity obstruction through \(T=12\). A passing run prints `VERIFY_OK`.

## Relationship to prior work

Baste, Dreyer, Marcille, Rabie and Toullec-Streicher (arXiv:2609.29054, publicly posted 2026-09-24) define layer-local temporal zero forcing and give complexity results, including an algorithm for bounded-degree temporal trees. The definitions and this broad algorithmic context are prior work. Their available opening full-text material does not furnish the two rational generating functions; later sections were not accessible during this comparison and must not be represented as completely inspected.

A separate recent enumeration for temporal networks whose snapshots are **two perfect matchings** gives all-size polynomials through cyclic gap compositions on the components of their union. That theorem explicitly assumes both matchings are perfect, while the alternating path snapshots leave their boundary vertices unmatched in one phase. Its cyclic result therefore does not state or directly imply the present open-boundary, two-terminal-offset rational path-length generating functions. We do not claim novelty for the basic union-preserving matching update, generic bounded-gap counting, or the cyclic complete-matching formula.

An earlier research archive by Krishna Harish, *Zero forcing on temporal graphs: Layer-local and footprint-constrained dynamics*, advertises **exact scalar values for alternating paths and even cycles**. Consequently the scalar minimum formula above is recorded as context/consequence, **not as a claim of independent numerical priority**. The indexed archive summary does not announce a full generating polynomial or minimizer multiplicities. Its manuscript was not recoverable during this comparison, so priority of the enumerative formulas remains provisional.

## Limitations

This theorem is about a fixed odd-first alternating schedule of matchings on a path, with simultaneous layer-local forcing and a finite horizon. It does not cover aggregate-footprint uniqueness rules, arbitrary temporal path schedules, time-reversed schedules without a corresponding parity adjustment, or general bounded-degree temporal trees. The originating paper's later sections and the Harish manuscript could not be fully compared; priority is provisional. The explicit scalar optimum may already be present in the Harish study. No independent mathematical audit has been performed.

## References

1. Julien Baste, Simon Dreyer, Clara Marcille, Mikaël Rabie and Ronan Toullec-Streicher, *Zero Forcing Sets in Temporal Graphs*, arXiv:2609.29054v1 (2026-09-24). https://arxiv.org/abs/2609.29054 ; accessible HTML: https://arxiv.org/html/2609.29054 .
2. Krishna Harish, *Zero forcing on temporal graphs: Layer-local and footprint-constrained dynamics*, research archive, https://github.com/krishnatheaverage/temporal-zero-forcing (indexed description inspected; underlying manuscript inaccessible at check time).
