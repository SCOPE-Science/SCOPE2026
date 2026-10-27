# Two revealed Poisson points already obstruct continuous exploration

## Finding

There exists a graph-measurable bounded stopping set \(Z\) for a diffuse, finite-intensity Poisson point process \(\Phi\) on a compact subset of the real line such that \(\Phi(Z(\Phi))\leq 2\) almost surely, but \(Z\) is **not attainable** at any stopping time by any intensity-continuous continuous-time decision tree (CTDT), even in the weaker sense of equality of explored regions modulo intensity measure. Thus the one-point attainability theorem of Khezeli [1, Theorem 1.3] has a sharp revealed-point threshold: replacing one by two is false.

## Assumptions and scope

Put \(C_1=[0,1]\), \(C_2=[2,3]\), \(C_3=[4,5]\), \(X=C_1\cup C_2\cup C_3\), and let \(\mu\) be Lebesgue measure restricted to \(X\). Let \(\Phi\) be the Poisson process with intensity \(\mu\); in particular \(\mu(X)=3\), and every specified finite occupancy pattern of the three cells has positive probability.

For every locally finite counting measure \(\varphi\) on \(X\), define \(b_i(\varphi)={\bf1}\{\varphi(C_i)>0\}\). Define its *first-point prefix* \(P_i(\varphi)\): if \(\varphi(C_i)=0\), set \(P_i(\varphi)=C_i\); otherwise let \(v_i(\varphi)\) be the leftmost point of \(\varphi\) in \(C_i\), and set \(P_i(\varphi)=C_i\cap(-\infty,v_i(\varphi)]\). In the next table, the three-digit string encodes \((b_1,b_2,b_3)\), and the right column gives selected *indices* (not selected whole cells). Define \(Z(\varphi)=\bigcup_{i\in J(b(\varphi))}P_i(\varphi)\).

| Occupancy bits | \(J\) |
|---|---|
| `000` | `2,3` |
| `001` | `1,2,3` |
| `010` | `1,2` |
| `011` | `1,2` |
| `100` | `2,3` |
| `101` | `1,3` |
| `110` | `1,2,3` |
| `111` | `1,3` |

An intensity-continuous CTDT here means an increasing adapted family \((A_t)_{t\geq0}\) of stopping sets, with \(\mu(A_0)=0\) and continuous trajectories \(t\mapsto\mu(A_t(\varphi))\), as in [1, Definitions 3.1 and 4.1]. Attainment at an observed-history stopping time \(\tau\) requires, in particular, \(\mu(A_{\tau(\Phi)}(\Phi)\mathbin{\triangle}Z(\Phi))=0\) almost surely, in addition to the observed-point equality in [1]. The counterexample rules out even the former requirement.

## Proof

**1. Stopping property and observed-point bound.** The table satisfies the exact finite *cylinder condition*: for any two occupancy words \(b,b'\), if \(b_i=b'_i\) for every \(i\in J(b)\), then \(J(b')=J(b)\). This is checked row by row (and exhaustively by the accompanying program). If \(\varphi'\) agrees with \(\varphi\) when restricted to \(Z(\varphi)\), then the occupancy bits on the selected prefixes cannot change: an empty selected cell exposes the entire cell, and a nonempty selected prefix contains its first point; agreement determines that first point and its prefix. Therefore \(J(b(\varphi'))=J(b(\varphi))\), all selected prefixes are unchanged, and \(Z(\varphi')=Z(\varphi)\). Graph measurability follows from the measurable first-point maps on three compact cells and the finite table. This establishes the stopping-set axioms for every locally finite counting measure, including nonsimple measures.

With probability one, \(\Phi\) is simple. Each nonempty selected prefix then contains exactly its one leftmost Poisson point; empty selected cells contribute none. The table gives \(\sum_{i\in J(b)}b_i\leq2\) for all eight words, hence \(\Phi(Z(\Phi))\leq2\) almost surely. The upper bound is attained with positive probability, for instance for occupancy word `111`.

**2. Nonattainment, even modulo intensity.** Assume for a contradiction that an intensity-continuous CTDT \((A_t)\) and an observed-history stopping time \(\tau\) attain \(Z\). The empty configuration \(0\) has probability \(e^{-3}>0\), so the almost-sure equality must hold on that configuration. By the first row of the table, \(Z(0)=C_2\cup C_3\). Thus \(\mu(A_{\tau(0)}(0)\mathbin{\triangle}(C_2\cup C_3))=0\). The continuous, nondecreasing trajectory \(t\mapsto\mu(A_t(0))\) starts at zero and reaches two at \(\tau(0)\). Choose a finite deterministic \(t<\tau(0)\) such that, writing \(U=A_t(0)\), we have \(0<\mu(U)<1\). Necessarily \(\mu(U\cap C_1)=0\) and \(\mu(U\cap(C_2\cup C_3))>0\).

Choose \(i\in\{2,3\}\) with \(\mu(U\cap C_i)>0\). Each \(C_j\setminus U\) has positive intensity because \(\mu(U)<1=\mu(C_j)\). If \(i=2\), consider Poisson configurations with no points in \(U\), exactly one point in each of \(C_1\setminus U\) and \(C_3\setminus U\), and no other points of \(X\). This event has strictly positive probability. Its occupancy word is `101`, whence \(Z(\Phi)=P_1(\Phi)\cup P_3(\Phi)\) and \(Z(\Phi)\cap C_2=\emptyset\). If \(i=3\), instead choose the strictly positive-probability event with no points in \(U\), exactly one point in \(C_2\setminus U\) and no other points. Its occupancy word is `010`, whence \(Z(\Phi)=P_1(\Phi)\cup P_2(\Phi)\) and \(Z(\Phi)\cap C_3=\emptyset\).

On either event, \(\Phi|_U=0|_U\). For every \(s\leq t\), the stopping-set property of \(A_s\), together with \(A_s(0)\subseteq U\), gives \(A_s(\Phi)=A_s(0)\). Hence the observed processes agree up to \(t\). As \(\tau\) is a stopping time for that observed process and \(\tau(0)>t\), we have \(\tau(\Phi)>t\) on this event. Monotonicity yields \(U\subseteq A_{\tau(\Phi)}(\Phi)\), whereas \(Z(\Phi)\) omits the entire cell \(C_i\). Therefore

\[\mu\bigl(A_{\tau(\Phi)}(\Phi)\mathbin{\triangle}Z(\Phi)\bigr)\geq\mu(U\cap C_i)>0,\]

on an event of positive probability, contradicting attainment. This proof uses only the region-equality part of the attainment definition, and hence also precludes stronger attainment requiring equality of observed configurations. \(\square\)

## Verification

The standalone Python 3 program `check_result.py` checks all eight occupancy words, all \(8\times8\) cylinder implications, the selected occupancy count, the three decisive table rows, and finite first-prefix stability on 64 simple discrete configurations. Run `python3 check_result.py`. These finite checks are **not** a proof of nonattainability: the latter is the measure-continuity and positive-probability argument in Step 2. The argument does not rely on numerical approximation.

## Relationship to prior work

Khezeli [1, Theorem 1.3] proves attainability under the one-point restriction, exactly the assertion whose next cardinality case is refuted here. Khezeli's Definition 4.1 allows stopping at a random observed-history time and identifies regions only modulo intensity, both accommodated by Step 2. Last, Peccati and Yogeshwaran [2, Appendix B, Proposition B.1 and Examples 2–3] give earlier **nonattainable** stopping sets based on three disjoint cells, including a randomized-CTDT obstruction, but their displayed stopping sets include whole cells and can reveal arbitrarily many Poisson points. They do not supply the two-point revealed-count bound here. The present first-point-prefix construction adds that bound and a direct contradiction valid for attainment at a stopping time, rather than equality with an ultimate union alone.

## Limitations

The nonattainability theorem is confined to intensity-continuous CTDTs satisfying the standard stopping-set and observed-history requirements; it does not rule out discontinuous or clairvoyant algorithms. The two-point restriction holds almost surely for diffuse Poisson input, not on arbitrary counting measures with coincident multiple points. No claim is made about minimal number of spatial cells, optimal intensity, or other spaces. Novelty is assessed against [1], [2], relevant indexed records and targeted literature; uncatalogued equivalent stopping-set constructions remain possible.

## References

[1] Ali Khezeli, *On Stopping Sets and Continuous-Time Decision Trees*, arXiv:2610.22011v1, publicly posted 2026-10-15, Theorem 1.3 and Definitions 2.1, 3.1, 4.1. https://arxiv.org/html/2610.22011v1

[2] Günter Last, Giovanni Peccati and D. Yogeshwaran, *Phase transitions and noise sensitivity on the Poisson space via stopping sets and decision trees*, arXiv:2101.07180v3, Appendix B (especially Proposition B.1 and Examples 2–3). https://arxiv.org/pdf/2101.07180
